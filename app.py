# app.py

import streamlit as st
import pandas as pd
from dags.reddit_pipeline import reddit_pipeline
from PIL import Image
import requests
from io import BytesIO

st.set_page_config(page_title="Reddit Personalized Feed", layout="wide")
st.title("📰 Personalized Reddit Feed Generator")

safe_subreddits = [
    "technology", "funny", "AskReddit", "worldnews", "science",
    "gaming", "sports", "movies", "todayilearned", "UpliftingNews"
]

selected_subreddits = st.multiselect(
    "Select subreddits to customize your feed:",
    options=safe_subreddits,
    default=["technology", "funny"]
)

num_posts = st.slider("Number of posts per subreddit", min_value=1, max_value=25, value=5)
summarize = st.checkbox("Summarize posts using GPT", value=True)

if st.button("Generate My Personalized Feed"):
    if not selected_subreddits:
        st.warning("Please select at least one subreddit.")
    else:
        with st.spinner("Fetching posts and generating your feed..."):
            output_csv = reddit_pipeline(
                user_subreddits=selected_subreddits,
                num_posts=num_posts,
                summarize=summarize
            )
            df = pd.read_csv(output_csv)
            st.success("✅ Feed generated and uploaded to S3!")

            # ✅ CSV Download Button (Table not shown)
            st.download_button(
                label="📥 Download CSV",
                data=df.to_csv(index=False),
                file_name=output_csv.split('/')[-1],
                mime="text/csv"
            )

            # ✅ Display Feed
            st.markdown("## Your Personalized Feed")
            for _, row in df.iterrows():
                with st.container():
                    st.markdown(f"### 🔗 [{row['title']}]({row['url']})", unsafe_allow_html=True)
                    st.markdown(f"**Summary:** {row['summary']}")

                    # Try to show image if URL points to media
                    try:
                        url = row['url'].strip()
                        if any(ext in url for ext in ['.jpg', '.png', '.jpeg']) or \
                           "i.redd.it" in url or "imgur.com" in url or url.startswith("https://preview.redd.it"):
                            response = requests.get(url, stream=True, timeout=5)
                            img = Image.open(BytesIO(response.content))
                            st.image(img, width=400)
                    except:
                        pass  # Don't break if image fails

                    st.markdown("---")