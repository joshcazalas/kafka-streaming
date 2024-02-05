import requests
import json

# Sample data for the arrest event
with open('sample_records/sample_data.json', 'r') as file:
        json_data = json.load(file)

headers = {'Content-Type': 'application/json'}

arrests_response = requests.post("http://127.0.0.1:5000/arrests/create", json=json_data, headers=headers)
officers_response = requests.post("http://127.0.0.1:5000/officers", json=json_data, headers=headers)
complaints_response = requests.post("http://127.0.0.1:5000/complaints", json=json_data, headers=headers)

print(arrests_response.status_code)
print(arrests_response.text)
print(officers_response.status_code)
print(officers_response.text)
print(complaints_response.status_code)
print(complaints_response.text)
