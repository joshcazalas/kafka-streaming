import requests

api_endpoint = '/aggregated_metrics/complaints_by_officer'
api_url = f'http://127.0.0.1:5000/{api_endpoint}'
headers = {'Content-Type': 'application/json'}

response = requests.get(api_url, headers=headers)

print(response.status_code)
print(response.text)
