from supabase import create_client
from config.config import SUPABASE_URL, SUPABASE_KEY, INFLUENCER_TABLE, METRICS_TABLE

class DatabaseHandler:
    def __init__(self):
        self.supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

    def create_influencer(self, instagram_url, username):
        """
        Create a new influencer record
        """
        data = {
            'instagram_url': instagram_url,
            'username': username,
            'created_at': 'now()'
        }
        
        result = self.supabase.table(INFLUENCER_TABLE).insert(data).execute()
        return result.data[0]['id']

    def save_metrics(self, influencer_id, metrics):
        """
        Save influencer metrics
        """
        data = {
            'influencer_id': influencer_id,
            **metrics
        }
        
        result = self.supabase.table(METRICS_TABLE).insert(data).execute()
        return result.data

    def get_influencer_by_url(self, instagram_url):
        """
        Get influencer by Instagram URL
        """
        result = self.supabase.table(INFLUENCER_TABLE)\
            .select('*')\
            .eq('instagram_url', instagram_url)\
            .execute()
        
        return result.data[0] if result.data else None 