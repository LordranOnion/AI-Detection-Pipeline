import os
import requests
import json

# Elasticsearch configuration
ELASTICSEARCH_URL = "http://localhost:9200"
INDEX_NAME = ".siem-signals-default"

# Function to deploy a rule
def deploy_rule(rule_content):
    headers = {"Content-Type": "application/json"}
    response = requests.post(f"{ELASTICSEARCH_URL}/{INDEX_NAME}/_doc/", headers=headers, data=rule_content)
    if response.status_code == 201:
        print("Rule deployed successfully.")
    else:
        print(f"Failed to deploy rule: {response.text}")

# Deploy each rule
detections_dir = "detections"
for rule_file in os.listdir(detections_dir):
    if rule_file.endswith(".json"):
        with open(os.path.join(detections_dir, rule_file), "r") as file:
            rule_content = file.read()
        deploy_rule(rule_content)
