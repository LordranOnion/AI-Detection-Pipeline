import requests
import random

# Caldera server configuration
CALDERA_API_URL = "http://localhost:8888/api/v2"
CALDERA_API_KEY = "your_caldera_api_key"  # Replace with actual API key

# Available adversary profiles in Caldera
adversary_profiles = ["adversary_id_1", "adversary_id_2", "adversary_id_3"]  # Replace with actual adversary IDs
selected_adversary = random.choice(adversary_profiles)

# Headers for authentication
headers = {
    "Authorization": f"Bearer {CALDERA_API_KEY}",
    "Content-Type": "application/json"
}

# Function to start an operation
def start_operation(adversary_id):
    operation_data = {
        "name": f"Automated Operation - {adversary_id}",
        "adversary_id": adversary_id,
        "state": "running"
    }
    response = requests.post(f"{CALDERA_API_URL}/operations", json=operation_data, headers=headers)
    if response.status_code == 200:
        print(f"Started operation with adversary: {adversary_id}")
    else:
        print(f"Failed to start operation: {response.text}")

# Initiate the attack simulation
start_operation(selected_adversary)
