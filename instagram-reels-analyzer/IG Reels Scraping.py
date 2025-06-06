import requests
import csv
import json

# Apify Dataset URL (Replace with your Apify export URL for 100 reels)
APIFY_DATASET_URL = input("Your Apify export URL for 100 reels: ")
#https://api.apify.com/v2/datasets/p6qSeBXVORwYVLQPr/items?attachment=true&clean=true&fields=likesCount,videoViewCount,commentsCount&format=csv
#https://api.apify.com/v2/datasets/NBXnlnSeeEQyLDeCZ/items?attachment=true&clean=true&fields=likesCount,videoViewCount,commentsCount&format=csv

# Airtable API credentials (Replace with your Airtable Personal Access Token and Base/Table details)
AIRTABLE_PERSONAL_ACCESS_TOKEN = "patclibXxtz0jtBEn.d6e9ee4543610da4a3b911569e2d5e74a5350b2185da6d885800d41ccb5a67c9"
BASE_ID = "appnHtwzWIizZSJDu"
TABLE_NAME = "Influencers"

# Step 1: Download CSV data from Apify
def download_apify_data(apify_url):
    try:
        response = requests.get(apify_url)
        response.raise_for_status()  # Raise HTTPError for bad responses
        # Save the CSV data locally
        with open("apify_data.csv", "w") as file:
            file.write(response.text)
        print("Data successfully downloaded from Apify.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch data from Apify: {e}")

# Step 2: Parse CSV Data and Calculate Averages
def calculate_averages(file_path):
    total_likes = 0
    total_views = 0
    total_comments = 0
    record_count = 0

    with open(file_path, "r", encoding="utf-8-sig") as file:  # Handle BOM
        reader = csv.DictReader(file)
        
        # Debugging: Print the headers from the CSV file
        print(f"CSV Headers: {reader.fieldnames}")
        
        for row in reader:
            try:
                # Use the corrected header name after stripping BOM
                total_likes += int(row["likesCount"].strip())
                total_views += int(row["videoViewCount"].strip())
                total_comments += int(row["commentsCount"].strip())
                record_count += 1
            except KeyError as e:
                print(f"KeyError: {e} - Verify column names in CSV.")
            except ValueError:
                print("Skipping record with invalid data.")

    # Calculate averages
    avg_likes = total_likes / record_count if record_count > 0 else 0
    avg_views = total_views / record_count if record_count > 0 else 0
    avg_comments = total_comments / record_count if record_count > 0 else 0

    print(f"Averages calculated: Likes={avg_likes}, Views={avg_views}, Comments={avg_comments}")
    return {
        "avg_likes": avg_likes,
        "avg_views": avg_views,
        "avg_comments": avg_comments,
    }

# Step 3: Upload Averages to Airtable
def upload_averages_to_airtable(averages):
    url = f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}"
    headers = {
        "Authorization": f"Bearer {AIRTABLE_PERSONAL_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    # Step 1: Find the record ID for the row to update (filter by Influencer ID or another unique field)
    influencer_id = input("Your Influencer ID (e.g I001): ")  # Replace with the ID or criteria for the row you want to update
    filter_query = f"?filterByFormula={{Influencer ID}}='{influencer_id}'"
    response = requests.get(f"{url}{filter_query}", headers=headers)

    if response.status_code == 200:
        records = response.json()["records"]
        if records:
            record_id = records[0]["id"]  # Get the first matching record's ID
            print(f"Found record to update: {record_id}")

            # Step 2: Update the record
            update_url = f"{url}/{record_id}"
            airtable_record = {
                "fields": {
                    "Avg Likes": round(averages["avg_likes"], 2),
                    "Avg Video Views": round(averages["avg_views"], 2),
                    "Avg Comments": round(averages["avg_comments"], 2)
                }
            }
            update_response = requests.patch(update_url, headers=headers, data=json.dumps(airtable_record))
            if update_response.status_code == 200:
                print(f"Averages successfully updated in Airtable: {airtable_record}")
            else:
                print(f"Failed to update averages: {update_response.status_code}, {update_response.text}")
        else:
            print(f"No record found with Influencer ID: {influencer_id}")
    else:
        print(f"Failed to fetch record: {response.status_code}, {response.text}")

# Main function to execute the workflow
def main():
    print("Starting the process...")
    
    # Step 1: Download data from Apify
    download_apify_data(APIFY_DATASET_URL)

    # Step 2: Calculate averages from the CSV file
    averages = calculate_averages("apify_data.csv")

    # Step 3: Upload averages to Airtable
    upload_averages_to_airtable(averages)
    print("Process completed successfully!")

# Run the script
if __name__ == "__main__":
    main()