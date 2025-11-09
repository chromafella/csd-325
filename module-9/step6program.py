import requests
import json

key = "ae988693c43b3767385da48ebb7c639438f333a3"

parameters = {"api_key": key, "format": "json"}

url = "https://api.getgeoapi.com/v2/currency/convert?api_key=ae988693c43b3767385da48ebb7c639438f333a3" \
"&from=GBP" \
"&to=USD" \
"&amount=10" \
"&format=json"

response = requests.get(url, parameters)

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

print("FROM GBP TO USD")

jprint(response.json())
