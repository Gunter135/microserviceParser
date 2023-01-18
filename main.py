# This is a sample Python script.
import ParserExample as p
import requests
import transferJson as transfer


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# TODO: REFORMAT PROJECT STRUCTURE
# TODO: PROJECT NEEDS TO CHECK IF FORECAST ALREADY EXISTS

def print_hi(name):
    page_array = [
        "", "tomorrow/",
        "3-day/", "4-day/", "5-day/", "6-day/", "7-day/", "8-day/", "9-day/", "10-day/"
    ]
    url = f'https://www.gismeteo.ru/weather-moscow-4368/'
    header = {
        "accept": "*/*",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 "
                      "Safari/537.36"
    }
    for page in page_array:
        req = requests.get(url=url + page, headers=header)
        with open("w.html", "w", encoding='utf-8') as file:
            file.write(req.text)
        p.parse("w.html")
        transfer.send('result.json')
        #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
