import requests

api_endpoint = '/aggregated_metrics/arrests_by_crime_type'
api_url = f'http://127.0.0.1:5000/{api_endpoint}'
headers = {'Content-Type': 'application/json'}

response = requests.get(api_url, headers=headers)

print(response.status_code)
print(response.text)
