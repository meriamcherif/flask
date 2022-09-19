import requests
import json

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "getApplicationPerUser/4")
print(response.json())
