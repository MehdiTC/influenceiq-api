import requests
from config.config import SUPABASE_URL, SUPABASE_KEY, INFLUENCER_TABLE, METRICS_TABLE

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=representation"
}

class DatabaseHandler:
    def __init__(self):
        pass  # No supabase client needed

    def create_influencer(self, instagram_url, username):
        """
        Create a new influencer record
        """
        data = {
            'instagram_url': instagram_url,
            'username': username,
            'created_at': 'now()'
        }
        response = requests.post(
            f"{SUPABASE_URL}/rest/v1/{INFLUENCER_TABLE}",
            headers=headers,
            json=data
        )
        print("Status code:", response.status_code)
        print("Response text:", response.text)
        response.raise_for_status()
        # Supabase returns a list of inserted rows
        return response.json()[0]['id']

    def save_metrics(self, influencer_id, metrics):
        """
        Save influencer metrics
        """
        data = {
            'influencer_id': influencer_id,
            **metrics
        }
        response = requests.post(
            f"{SUPABASE_URL}/rest/v1/{METRICS_TABLE}",
            headers=headers,
            json=data
        )
        print("Status code:", response.status_code, flush=True)
        print("Response text:", response.text, flush=True)
        response.raise_for_status()
        print("Status code:", response.status_code, flush=True)
        print("Response text:", response.text, flush=True)
        return response.json()

    def get_influencer_by_url(self, instagram_url):
        """
        Get influencer by Instagram URL
        """
        params = {
            'instagram_url': f"eq.{instagram_url}",
            'select': '*'
        }
        response = requests.get(
            f"{SUPABASE_URL}/rest/v1/{INFLUENCER_TABLE}",
            headers=headers,
            params=params
        )
        response.raise_for_status()
        data = response.json()
        return data[0] if data else None 