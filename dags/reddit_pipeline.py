# reddit_pipeline.py

import os
import csv
import praw
import boto3
import openai
import pandas as pd
from datetime import datetime
from configparser import ConfigParser
import traceback
import re


def is_valid_url(url):
    return isinstance(url, str) and url.strip().startswith("http")


def reddit_pipeline(user_subreddits, num_posts=5, summarize=True):
    config = ConfigParser()
    config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
    config.read(config_path)

    # AWS credentials
    aws_access_key = config.get('aws', 'access_key')
    aws_secret_key = config.get('aws', 'secret_key')
    bucket_name = config.get('aws', 'bucket_name')

    # Reddit credentials
    reddit = praw.Reddit(
        client_id=config.get('reddit', 'client_id'),
        client_secret=config.get('reddit', 'client_secret'),
        user_agent=config.get('reddit', 'user_agent')
    )

    # OpenAI client
    if summarize:
        client = openai.OpenAI(api_key=config.get('openai', 'api_key'))

    all_data = []

    for subreddit_name in user_subreddits:
        subreddit = reddit.subreddit(subreddit_name)
        for post in subreddit.hot(limit=num_posts):
            try:
                title = post.title.strip().replace('\n', ' ')
                body = post.selftext.strip().replace('\n', ' ') if post.selftext else ""
                content = f"{title}\n\n{body}".strip()
                if len(content) < 20:
                    content = title
                if len(content) > 4000:
                    content = content[:4000]

                if summarize:
                    try:
                        response = client.chat.completions.create(
                            model="gpt-3.5-turbo",
                            messages=[
                                {"role": "system", "content": "Summarize the Reddit post."},
                                {"role": "user", "content": content}
                            ],
                            timeout=10
                        )
                        summary = response.choices[0].message.content.strip()
                    except Exception as e:
                        print(f"[ERROR] Failed to summarize post {post.id}: {e}")
                        traceback.print_exc()
                        summary = "Summary failed"
                else:
                    summary = content[:200] + "..." if len(content) > 200 else content

                all_data.append({
                    'subreddit': subreddit_name,
                    'post_id': post.id,
                    'title': title,
                    'score': post.score,
                    'summary': summary,
                    'url': post.url.strip() if is_valid_url(post.url) else "",
                    'created_utc': datetime.utcfromtimestamp(post.created_utc).strftime('%Y-%m-%d %H:%M:%S')
                })

            except Exception as e:
                print(f"[ERROR] Skipping post due to failure: {e}")
                traceback.print_exc()
                continue

    # Ensure output directory exists
    os.makedirs('data', exist_ok=True)

    # Generate unique filename
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_csv = f"data/reddit_posts_{timestamp}.csv"

    # Save locally with quoting
    df = pd.DataFrame(all_data)
    df.to_csv(
        output_csv,
        index=False,
        encoding='utf-8',
        quoting=csv.QUOTE_ALL
    )

    # Upload to S3
    s3 = boto3.client(
        's3',
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key
    )

    object_name = os.path.basename(output_csv)
    try:
        s3.upload_file(output_csv, bucket_name, object_name)
        print(f"[SUCCESS] Uploaded {object_name} to S3 bucket '{bucket_name}'")
    except Exception as e:
        print(f"[ERROR] Upload to S3 failed: {e}")
        traceback.print_exc()

    return output_csv