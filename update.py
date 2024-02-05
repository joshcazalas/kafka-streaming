import requests
import json

# Sample data for the arrest update event
with open('sample_records/sample_data_edited.json', 'r') as file:
    json_data = json.load(file)

api_endpoint = '/arrests/update'  # Update endpoint
api_url = f'http://127.0.0.1:5000{api_endpoint}'
headers = {'Content-Type': 'application/json'}

response = requests.put(api_url, json=json_data, headers=headers)  # Use PUT for update

print(response.status_code)
print(response.text)