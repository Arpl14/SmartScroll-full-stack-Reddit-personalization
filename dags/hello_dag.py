from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from reddit_pipeline import reddit_pipeline  # ✅ Import from the new file

default_args = {
    'start_date': datetime(2025, 6, 1),
}

with DAG('personalized_feed_dag',
         default_args=default_args,
         schedule_interval=None,
         catchup=False) as dag:

    fetch_posts = PythonOperator(
        task_id='fetch_and_summarize_posts',
        python_callable=reddit_pipeline,
        op_kwargs={
            'user_subreddits': ['technology', 'funny', 'AskReddit'],  # <-- Customize this
            'output_csv': 'data/reddit_posts.csv',
            'num_posts': 5
        }
    )