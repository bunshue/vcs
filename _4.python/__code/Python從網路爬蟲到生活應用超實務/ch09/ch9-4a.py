import requests 
from bs4 import BeautifulSoup

url = "https://www.msn.com/zh-tw/weather/today/台北,台灣/we-city?iso=TW"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
span = soup.find('span', class_="current")
temp = span.text
summary = span.get("aria-label")

def LINE_alert(msg):
    token = "<存取權杖>"
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    params = {"message": msg}
    r = requests.post("https://notify-api.line.me/api/notify",
                      headers=headers, params=params)  
    if r.status_code == 200:
        print("已經送出通知訊息...")
    else:
        print("錯誤! 寄送通知訊息失敗...")

LINE_alert(temp +"/" + summary)


