import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Apify Configuration
APIFY_API_TOKEN = os.getenv('APIFY_API_TOKEN', 'apify_api_CvhYVx9iF7Qe8ngXZpwtiVeHcHeIqR3aYjUV')
APIFY_ACTOR_ID = os.getenv('APIFY_ACTOR_ID')  # Your Instagram scraper actor ID

# Supabase Configuration
SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')

# Database Table Names
INFLUENCER_TABLE = 'influencers'
METRICS_TABLE = 'influencer_metrics'

# Metrics Configuration
METRICS_TO_CALCULATE = [
    'average_likes',
    'average_views',
    'average_comments',
    'engagement_rate',
    'estimated_value'
]

# Engagement Rate Calculation
ENGAGEMENT_RATE_MULTIPLIER = 0.1  # Adjust based on your valuation model 