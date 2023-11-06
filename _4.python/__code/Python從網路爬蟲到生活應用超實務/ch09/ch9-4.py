import requests 
from bs4 import BeautifulSoup

url = "https://www.msn.com/zh-tw/weather/today/台北,台灣/we-city?iso=TW"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
span = soup.find('span', class_="current")
temp = span.text
summary = span.get("aria-label")

def email_alert(first, second=None, third=None):
    URL = "https://maker.ifttt.com/trigger/{0}/with/key/{1}/?"
    event_name = "web_scraping"
    api_key = "<API金鑰>"
    url = URL.format(event_name, api_key)
    data = {}
    data["value1"] = first
    data["value2"] = second
    data["value3"] = third    
    for key, val in data.items():
        if val:
            url = url + key + "=" + str(val) + "&"
    r = requests.get(url)    
    if r.status_code == 200:
        print("已經寄送郵件通知...")
    else:
        print("錯誤! 寄送郵件通知失敗...")

email_alert(temp, summary)


