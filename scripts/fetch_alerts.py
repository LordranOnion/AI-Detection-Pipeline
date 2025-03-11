import requests
import json

# Elasticsearch configuration
ELASTICSEARCH_URL = "http://localhost:9200"
INDEX_NAME = "logs-*"
QUERY = {
    "query": {
        "match_all": {}
    }
}

# Function to fetch logs
def fetch_logs():
    response = requests.post(f"{ELASTICSEARCH_URL}/{INDEX_NAME}/_search", json=QUERY)
    if response.status_code == 200:
        logs = response.json()
        with open("logs/latest_alerts.json", "w") as file:
            json.dump(logs, file, indent=4)
        print("Logs fetched and saved to logs/latest_alerts.json")
    else:
        print(f"Failed to fetch logs: {response.text}")

# Fetch the logs
fetch_logs()
