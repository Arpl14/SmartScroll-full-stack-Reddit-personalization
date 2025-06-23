# SmartScroll-AI-powered personalized Reddit feed
*Built to effectively learn rather than doomscroll from social media with Data Engineering + LLM magic*  
**By Arpita Lonakadi**

---

## 🔥 Summary

This project is a **real-time Reddit feed pipeline** built with Apache Airflow, GPT-3.5, and AWS — designed to extract content user is interested in from Reddit, summarize it using LLMs, store the results in the cloud, and visualize it in an insightful dashboard.
**No more doomscrolling.** Instead, this app curates and compresses Reddit content into bite-sized insights that respect your time and focus.

---

## ⚙️ How It Works

1. **User selects topics he is interested in** in the app UI.
2.	Apache Airflow DAG is triggered to run the data pipeline asynchronously on demand or by schedule.
3.	The app fetches relevant posts using the Reddit API (via PRAW).
4.	Each post is optionally summarized using GPT-3.5, compressing long content into crisp summaries.
5.	A structured CSV is created and automatically uploaded to AWS S3.
6.  A Glue Crawler is configured to automatically scan the S3 bucket.
7.  Athena queries the Glue Catalog table directly, enabling serverless SQL access to Reddit posts 

9.  In **Amazon QuickSight**, the data is visualized as:
   - Posts over time
   - Category split
   - Trending post titles (word cloud)
---

## ✨ Key Features

- 🎯 Custom topic selection  
- 🤖 GPT-powered content summarization (via OpenAI API)  
- ☁️ Cloud storage using Amazon S3  
- 🔁 Automated orchestration via Apache Airflow  
- 📊 BI dashboard (QuickSight) with feed trends + word clouds  
- 🖥️ Streamlit frontend with image previews  
- 🐳 Dockerized environment for reproducible setup  

---

## ⚙️ Tech Stack & Pipeline Architecture

### 🔧 Tech Stack

- **Python**, **Pandas**, **PRAW** (Reddit API wrapper)  
- **OpenAI GPT-3.5** for summarization  
- **Apache Airflow** for scheduling and orchestration  
- **AWS S3, Glue, Athena, QuickSight** for data lake and analytics  
- **Streamlit** for user-facing UI  
- **Docker** + **Docker Compose** for containerization  

### 🛠️ Data Pipeline

<p align="center">
  <img src="https://github.com/user-attachments/assets/fda23105-a15b-48a6-b6b4-4a7a1bf1862a" width="300"/>
</p>

 ---

## 💡 Implementation Highlights

-  **Modular Code**: `reddit_pipeline.py` can run standalone or be triggered by Airflow
-  **LLM Integration**: GPT-3.5 intelligently summarizes long Reddit content into digestible insights
-  **Auto-saves timestamped files** in `/data/`, ideal for tracking post activity over time
-  **Airflow DAG** runs `reddit_pipeline()` on schedule or manually
-  **QuickSight dashboard** visualizes post volume, trending terms, and subreddit category splits

---

## 🏆 Achievements

-  Reduced Reddit content overload into a 10-second digest  
-  Enabled explainable AI use in social media consumption  
-  Built a production-style BI dashboard on user content  
-  Dockerized pipeline for repeatable, scalable use  

---
## Conclusion:
This project brings together the power of data engineering, automation, and generative AI to solve a modern attention problem: content overload. Instead of passively consuming what algorithms push, you get to custom-build your own feed, enriched with GPT-powered summaries and analytics.

## ▶️ How to Use

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/reddit-feed-visualizer.git
cd reddit-feed-visualizer

Setup config.ini:
[reddit]
client_id = your_id
client_secret = your_secret
user_agent = reddit-feed-agent

[openai]
api_key = your_openai_key

[aws]
access_key = your_aws_key
secret_key = your_aws_secret
bucket_name = your_s3_bucket


Run via Streamlit (for UI):
pip install -r requirements.txt
streamlit run app.py

Or Trigger via Airflow (ETL automation)
docker-compose up airflow-init


