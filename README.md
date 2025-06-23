# SmartScroll-AI-powered personalized Reddit feed#
*Built to combat doomscrolling with Data Engineering + LLM magic*  
**By Arpita Lonakadi**

---

## 🔥 Summary

This project is a **real-time Reddit feed pipeline** built with Apache Airflow, GPT-3.5, and AWS — designed to extract content from Reddit, summarize it using LLMs, store the results in the cloud, and visualize it in an insightful dashboard.
**No more doomscrolling.** Instead, this app curates and compresses Reddit content into bite-sized insights that respect your time and focus.

---

## 🧭 Project Overview

This end-to-end data platform automatically:

- Extracts trending posts from user-selected subreddits using Reddit’s API
- Summarizes the posts using OpenAI’s GPT-3.5 (LLM integration)
- Stores CSV outputs in Amazon S3 via a version-controlled timestamp
- Loads data to AWS Glue and queries it with Amazon Athena
- Displays insights on an Amazon QuickSight dashboard
- Offers a Streamlit UI for custom user input + feed download

The pipeline is **automated using Apache Airflow**, making it scalable and production-ready.

---

## ✨ Key Features

- 🎯 Custom subreddit selection  
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

                 ┌────────────────────┐
                 │ Airflow DAG Trigger│
                 └─────────┬──────────┘
                           │
                           ▼
            [Reddit API via PRAW to Fetch Posts]
                           │
                           ▼
  [OpenAI GPT-3.5 to Summarize Posts (LLM Integration)]
                           │
                           ▼
             [Save CSV Locally → Upload to S3]
                           │
                           ▼
     [AWS Glue Crawler → Athena SQL → QuickSight Dash]
                           │
                           ▼
         [Streamlit App for Custom Feeds + Download]



         ---

## 💡 Implementation Highlights

- ✅ **Modular Code**: `reddit_pipeline.py` can run standalone or be triggered by Airflow
- ✅ **LLM Integration**: GPT-3.5 intelligently summarizes long Reddit content into digestible insights
- ✅ **Auto-saves timestamped files** in `/data/`, ideal for tracking post activity over time
- ✅ **Airflow DAG** runs `reddit_pipeline()` on schedule or manually
- ✅ **QuickSight dashboard** visualizes post volume, trending terms, and subreddit category splits

---

## ⚙️ How It Works

1. **User selects subreddits** in the app UI.
2. The app fetches posts using the Reddit API.
3. Each post is **optionally summarized by GPT**.
4. A structured CSV is created and **uploaded to AWS S3**.
5. Using **AWS Glue + Athena**, the CSV is queried.
6. In **Amazon QuickSight**, the data is visualized as:
   - Posts over time
   - Category split
   - Trending post titles (word cloud)

---

## 🏆 Achievements

- ⏱️ Reduced Reddit content overload into a 10-second digest  
- 💡 Enabled explainable AI use in social media consumption  
- 📊 Built a production-style BI dashboard on user content  
- 🐳 Dockerized pipeline for repeatable, scalable use  

---

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
-----

## Conclusion:
This project brings together the power of data engineering, automation, and generative AI to solve a modern attention problem: content overload. Instead of passively consuming what algorithms push, you get to custom-build your own feed, enriched with GPT-powered summaries and analytics.

Built by Arpita Lonakadi — no more doomscrolling. Build your own feed.
docker-compose up

