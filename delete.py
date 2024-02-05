import requests
import json

# Sample data for the arrest event
with open('sample_records/sample_data.json', 'r') as file:
        json_data = json.load(file)

api_endpoint = 'arrests/delete'
api_url = f'http://127.0.0.1:5000/{api_endpoint}'
headers = {'Content-Type': 'application/json'}

response = requests.delete(api_url, json=json_data, headers=headers)

print(response.status_code)
print(response.text)