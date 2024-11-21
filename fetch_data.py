import json
import random
from datetime import datetime

# Simulate fetching data (e.g., Bitcoin price as a random number)
def fetch_mock_data():
    return {
        "bitcoin_price": round(random.uniform(20000, 60000), 2),  # Random Bitcoin price between 20k and 60k
        "currency": "USD"
    }

def fetch_and_save_data():
    try:
        # Fetch mock data
        data = fetch_mock_data()

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
