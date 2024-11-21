import requests
import json
from datetime import datetime

# Example API endpoint (replace with your actual API)
API_URL = "https://api.coindesk.com/v1/bpi/currentprice.json"

def fetch_and_save_data():
    try:
        response = requests.get(API_URL)
        data = response.json()

        # Add a timestamp to the data
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data['timestamp'] = timestamp

        # Save data to a JSON file
        with open("data.json", "w") as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Data updated at {timestamp}")

    except Exception as e:
        print(f"Failed to fetch data: {e}")

if __name__ == "__main__":
    fetch_and_save_data()
