import requests
import json

API_KEY = "GGzdd1Vm4npty4LFHS5jwWtyYbcdALf67IjpcvEu"

url = f"https://api.nasa.gov/neo/rest/v1/feed?api_key={API_KEY}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print(json.dumps(data, indent=4))
