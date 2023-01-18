import requests
from bs4 import BeautifulSoup
import json
import datetime


def parse(file):
    with open(file, 'r', encoding='utf-8') as file:
        src = file.read()
        # print(src)
    soup = BeautifulSoup(src, "lxml")

    temperature = soup.find(class_="widget-row-chart widget-row-chart-temperature") \
        .findAll(class_="unit unit_temperature_c")
    wind = soup.find(class_="widget-row widget-row-wind-speed-gust row-with-caption") \
        .findAll(class_="wind-unit unit unit_wind_m_s")
    precipitation = soup.find(class_="widget-row widget-row-precipitation-bars row-with-caption") \
        .findAll(class_="row-item")
    pressure = soup.find(class_="widget widget-pressure widget-oneday") \
        .find(class_="widget-row-chart widget-row-chart-pressure") \
        .findAll(class_="unit unit_pressure_mm_hg_atm")
    humidity = soup.find(class_="widget-row widget-row-humidity")
    day = soup.find(class_="weathertab weathertab-block tooltip").find(class_="tab-content")\
        .find("div").text.strip().split()

    today = datetime.date.today()
    today = today.replace(today.year, today.month, int(day[1]))
    print(today)

    temperature_avg = 0
    wind_avg = 0
    precipitation_avg = 0
    pressure_avg = 0
    humidity_avg = 0

    for item in precipitation:
        # print(item.text.strip())
        precipitation_avg += float(item.text.strip().replace(",", "."))

    for item in temperature:
        # print(item.text.strip())
        if item.text.strip()[0] == "−":
            temperature_avg += int(item.text.strip()[1:]) * -1
        else:
            temperature_avg += int(item.text.strip())

    for item in wind:
        # print(item.text.strip())
        # print(item.text.strip().split("-"))
        if "-" in item.text.strip():
            wind_avg = int(item.text.strip().split("-")[0]) * int(item.text.strip().split("-")[1])
        else:
            wind_avg += int(item.text.strip())

    for item in pressure:
        # print(item.text.strip())
        pressure_avg += int(item.text.strip())

    for item in humidity:
        # print(item.text.strip())
        humidity_avg += int(item.text.strip())

    # print(pressure_avg / 8, humidity_avg / 8, precipitation_avg / 8, wind_avg / 8, temperature_avg / 8)
    dictionary = {
        "temperature": temperature_avg / 8,
        "wind": wind_avg / 8,
        "precipitation": precipitation_avg / 8,
        "atmosphere_pressure": int(pressure_avg/8),
        "humidity": int(humidity_avg/8),
        "date": f'{today}'
    }
    with open("result.json", "w") as file:
        json.dump(dictionary, file, indent=4, ensure_ascii=False)
