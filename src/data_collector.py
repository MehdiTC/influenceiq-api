from apify_client import ApifyClient
import pandas as pd
from datetime import datetime
from config.config import APIFY_API_TOKEN, APIFY_ACTOR_ID
import requests

class InstagramDataCollector:
    def __init__(self):
        if not APIFY_API_TOKEN:
            raise ValueError("APIFY_API_TOKEN is not set in environment variables")
            
        self.client = ApifyClient(APIFY_API_TOKEN)
        self.task_id = "el8M5C0gcHhEIWdso"  # Your specific task ID

    def run_scraper(self, instagram_profile_url):
        """
        Run the Apify Instagram scraper for a given profile URL
        
        Args:
            instagram_profile_url (str): Full Instagram profile URL (e.g., https://www.instagram.com/username/)
            
        Returns:
            pandas.DataFrame: DataFrame containing the scraped reels data
        """
        try:
            print(f"Starting Apify task {self.task_id}...")
            
            # Run the task
            run = self.client.task(self.task_id).call()
            
            print("Fetching dataset...")
            # Get the dataset
            dataset = self.client.dataset(run["defaultDatasetId"])
            
            print("Processing data...")
            # Get the items
            items = list(dataset.iterate_items())
    
            
            if not items:
                raise ValueError("No data was collected from Instagram")
            
            # Convert to DataFrame
            df = pd.DataFrame(items)
            
            # Rename columns to match expected names
            df.rename(columns={
                'likesCount': 'likes',
                'videoViewCount': 'views',
                'commentsCount': 'comments'
            }, inplace=True)
            
            # Ensure required columns exist
            required_columns = ['likes', 'views', 'comments']
            missing_columns = [col for col in required_columns if col not in df.columns]
            if missing_columns:
                raise ValueError(f"Missing required columns in data: {missing_columns}")
            
            return df
            
        except Exception as e:
            print(f"Error during scraping: {str(e)}")
            raise

    def calculate_metrics(self, df):
        """
        Calculate various metrics from the scraped data
        
        Args:
            df (pandas.DataFrame): DataFrame containing the scraped reels data
            
        Returns:
            dict: Dictionary containing calculated metrics
        """
        try:
            # Convert numeric columns to float, handling any non-numeric values
            for col in ['likes', 'views', 'comments']:
                df[col] = pd.to_numeric(df[col], errors='coerce')
            
            metrics = {
                'average_likes': float(df['likes'].mean()),
                'average_views': float(df['views'].mean()),
                'average_comments': float(df['comments'].mean()),
                'total_reels': len(df),
                'scraped_at': datetime.now().isoformat()
            }
            
            # Calculate engagement rate
            total_engagement = metrics['average_likes'] + metrics['average_comments']
            metrics['engagement_rate'] = float((total_engagement / metrics['average_views']) * 100)
            
            # Calculate estimated value (example calculation)
            # This is a simple calculation - you might want to adjust the formula
            metrics['estimated_value'] = float(metrics['engagement_rate'] * metrics['average_views'] * 0.01)
            
            return metrics
            
        except Exception as e:
            print(f"Error calculating metrics: {str(e)}")
            raise 

    def save_metrics(self, influencer_id, metrics):
        data = {
            'influencer_id': influencer_id,
            **metrics
        }
        response = requests.post(
            f"{SUPABASE_URL}/rest/v1/{METRICS_TABLE}",
            headers=headers,
            json=data
        )
        response.raise_for_status()
        return response.json() 