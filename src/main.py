from src.data_collector import InstagramDataCollector
from src.database import DatabaseHandler
import re

def extract_username(url):
    """Extract username from Instagram URL"""
    pattern = r'instagram\.com/([^/?]+)'
    match = re.search(pattern, url)
    return match.group(1) if match else None

def main():
    # Initialize components
    collector = InstagramDataCollector()
    db = DatabaseHandler()
    
    # Get Instagram profile URL from user
    instagram_url = input("Enter Instagram profile URL: ").strip()
    username = extract_username(instagram_url)
    
    if not username:
        print("Invalid Instagram URL")
        return
    
    # Check if influencer already exists
    influencer = db.get_influencer_by_url(instagram_url)
    
    if not influencer:
        # Create new influencer record
        influencer_id = db.create_influencer(instagram_url, username)
        print(f"Created new influencer record for {username}")
    else:
        influencer_id = influencer['id']
        print(f"Found existing influencer record for {username}")
    
    # Collect and process data
    print("Collecting Instagram data...")
    df = collector.run_scraper(instagram_url)
    
    print("Calculating metrics...")
    metrics = collector.calculate_metrics(df)
    
    # Save metrics
    print("Saving metrics to database...")
    db.save_metrics(influencer_id, metrics)
    
    print("\nMetrics saved successfully:")
    for key, value in metrics.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main() 