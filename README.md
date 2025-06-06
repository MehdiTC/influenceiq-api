# InfluenceIQ API

## Overview
InfluenceIQ is an automated tool for collecting, analyzing, and storing Instagram influencer metrics. It leverages Apify for scraping Instagram Reels data and Supabase for secure, scalable data storage. The project is designed for influencer analytics, marketing research, and social media data science.

---

## Features
- **Automated Instagram Reels data collection** using Apify
- **Metrics calculation**: average likes, views, comments, engagement rate, estimated value
- **Historical data tracking** for influencers
- **Supabase integration** for cloud-based, SQL-accessible storage
- **Modular, extensible Python codebase**
- **Secure handling of API keys and secrets**

---

## Architecture
- **Python 3.10+**
- **Apify Client**: Scrapes Instagram Reels data
- **Supabase REST API**: Stores and retrieves influencer and metrics data
- **Pandas**: Data processing and metrics calculation
- **Environment variables**: All secrets and config are loaded from `.env` (never committed)

```
[User] → [Python CLI] → [Apify Scraper] → [Pandas Metrics] → [Supabase REST API]
```

---

## Setup Instructions

### 1. Clone the repository
```sh
git clone https://github.com/yourusername/influenceiq-api.git
cd influenceiq-api
```

### 2. Create and activate a virtual environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```sh
pip install -r requirements.txt
```

### 4. Configure environment variables
Create a `.env` file in the project root:
```
APIFY_API_TOKEN=your_apify_token
APIFY_ACTOR_ID=apify/instagram-reels-scraper  # or your custom actor/task
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your_supabase_anon_or_service_role_key
```
**Never commit your `.env` file!**

### 5. Set up Supabase tables
- **influencers**: `id (PK)`, `instagram_url`, `username`, `created_at`
- **influencer_metrics**: `id (PK)`, `influencer_id (FK)`, `average_likes`, `average_views`, `average_comments`, `engagement_rate`, `estimated_value`, `total_reels`, `scraped_at`
- Enable RLS and add appropriate policies for your use case.

---

## Usage

### Run the main script
```sh
python -m src.main
```

- Enter an Instagram profile URL when prompted (e.g., `https://www.instagram.com/username/reels/`)
- The script will:
  1. Check if the influencer exists in the database
  2. Scrape their recent Reels data via Apify
  3. Calculate metrics
  4. Save the results to Supabase
  5. Print the calculated metrics

### Example Output
```
Enter Instagram profile URL: https://www.instagram.com/exampleuser/reels/
Found existing influencer record for exampleuser
Collecting Instagram data...
Calculating metrics...
Saving metrics to database...
Metrics saved successfully:
average_likes: 1234.5
average_views: 56789.0
average_comments: 56.7
engagement_rate: 2.3
estimated_value: 1305.15
total_reels: 20
scraped_at: 2024-06-06T12:34:56
```

---

## Demo Instructions

1. **Fork or clone the repo**
2. **Set up your `.env` and Supabase tables** as above
3. **Run the script** with a real Instagram profile URL
4. **Check your Supabase dashboard** to see the stored influencer and metrics data
5. **(Optional)**: Extend the code to analyze more metrics, visualize data, or integrate with other platforms

---

## Security Notes
- **Never commit your `.env` or any secrets to git**
- All API keys are loaded from environment variables
- If a secret is ever exposed, rotate it immediately and remove it from git history
- See the `.gitignore` for ignored files

---

## Project Structure
```
├── config/
│   └── config.py         # Loads environment variables
├── src/
│   ├── main.py           # Main CLI entry point
│   ├── data_collector.py # Apify scraping and metrics logic
│   └── database.py       # Supabase REST API integration
├── requirements.txt      # Python dependencies
├── .gitignore            # Ignores venv, .env, etc.
├── README.md             # This file
└── apify_data.csv        # Example data (not required)
```

---

## For Recruiters & Reviewers
- **Demonstrates:**
  - API integration (REST, Apify, Supabase)
  - Secure credential management
  - Data engineering with Pandas
  - Clean, modular Python code
  - Real-world automation and analytics
- **Ready for extension:**
  - Add a web UI, dashboards, or more data sources
  - Deploy as a scheduled job or serverless function

---

## Contact
- **Author:** MehdiTC
- **GitHub:** [MehdiTC/influenceiq-api](https://github.com/MehdiTC/influenceiq-api)
- **Email:** your.email@example.com

---

**If you have questions, want a live demo, or want to discuss collaboration, please reach out!** 