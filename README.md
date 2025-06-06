# InfluenceIQ API

An automated tool for collecting and analyzing Instagram influencer metrics using Apify for data collection and Supabase for data storage.

## Features

- Automated Instagram Reels data collection
- Metrics calculation including:
  - Average likes
  - Average views
  - Average comments
  - Engagement rate
  - Estimated value
- Historical data tracking
- Supabase database integration

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/influenceiq-api.git
cd influenceiq-api
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up Apify:
   - Create an account at [Apify](https://apify.com)
   - Go to [Apify Console](https://console.apify.com/)
   - Get your API token:
     - Click on your profile picture → "Account Settings"
     - Under "API" section, copy your API token
   - Get the Actor ID:
     - Go to [Apify Store](https://apify.com/store)
     - Search for "Instagram Reels Scraper"
     - Use the official "Instagram Reels Scraper" actor
     - Copy the Actor ID (e.g., `apify/instagram-reels-scraper`)

4. Set up Supabase:
   - Create a new Supabase project
   - Create two tables:
     - `influencers` (id, instagram_url, username, created_at)
     - `influencer_metrics` (id, influencer_id, average_likes, average_views, average_comments, engagement_rate, scraped_at)

5. Create a `.env` file in the root directory with the following variables:
```
APIFY_API_TOKEN=your_apify_token
APIFY_ACTOR_ID=apify/instagram-reels-scraper
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
```

## Usage

Run the main script:
```bash
python src/main.py
```

Enter an Instagram profile URL when prompted. The script will:
1. Check if the influencer exists in the database
2. Collect their recent Reels data
3. Calculate metrics
4. Save the results to Supabase

## Database Schema

### Influencers Table
- `id`: UUID (primary key)
- `instagram_url`: String
- `username`: String
- `created_at`: Timestamp

### Influencer Metrics Table
- `id`: UUID (primary key)
- `influencer_id`: UUID (foreign key)
- `average_likes`: Float
- `average_views`: Float
- `average_comments`: Float
- `engagement_rate`: Float
- `estimated_value`: Float
- `scraped_at`: Timestamp

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License 