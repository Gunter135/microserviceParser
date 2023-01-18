import json

import requests


def send(file):
    URL = f'http://localhost:8080/weather_forecast/report'
    data = json.load(open(file))
    req = requests.post(url=URL, json=data)
    if req.status_code == 200:
        print("WEATHER REPORT CREATED")
    else:
        print("ERROR")

