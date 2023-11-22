import sys
import requests 
from bs4 import BeautifulSoup
 
URL = "https://maker.ifttt.com/trigger/{0}/with/key/{1}/?"
event_name = "web_scraping"
api_key = "<API金鑰>"

def email_alert(first, second=None, third=None):
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

email_alert("測試值1", 100)

print('------------------------------------------------------------')	#60個
 
URL = "https://maker.ifttt.com/trigger/{0}/with/key/{1}/?"
event_name = "web_scraping"
api_key = "<API金鑰>"

def email_alert(first, second=None, third=None):
    url = URL.format(event_name, api_key)
    data = {}
    data["value1"] = first
    data["value2"] = second
    data["value3"] = third    
    r = requests.post(url, data=data)       
    if r.status_code == 200:
        print("已經寄送郵件通知...")
    else:
        print("錯誤! 寄送郵件通知失敗...")

email_alert("測試值2", 150, 200)

print('------------------------------------------------------------')	#60個

token = "<存取權杖>"
headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/x-www-form-urlencoded"
}
params = {"message": "Python程式送出測試通知訊息"}
r = requests.post("https://notify-api.line.me/api/notify",
                   headers=headers, params=params)  
if r.status_code == 200:
    print("已經送出通知訊息...")
else:
    print("錯誤! 寄送通知訊息失敗...")

print('------------------------------------------------------------')	#60個

token = "<API權杖>"
chat_id = "<聊天室識別碼>"

def telegram_bot_sendText(msg):
    url = "https://api.telegram.org/bot{0}/sendMessage?chat_id={1}&text={2}"
    r = requests.post(url.format(token,chat_id,msg))  
    return r.json()

test = telegram_bot_sendText("大家好!")
print(test)

print('------------------------------------------------------------')	#60個

import telegram
 
token = "<API權杖>"
chat_id = "<聊天室識別碼>"

def telegram_bot_sendText(msg):
    bot = telegram.Bot(token=token)
    return bot.sendMessage(chat_id=chat_id, text=msg)
    
test = telegram_bot_sendText("測試Telegram模組!")
print(test)

print('------------------------------------------------------------')	#60個

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

print('------------------------------------------------------------')	#60個

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

print('------------------------------------------------------------')	#60個

url = "https://www.msn.com/zh-tw/weather/today/台北,台灣/we-city?iso=TW"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
span = soup.find('span', class_="current")
temp = span.text
summary = span.get("aria-label")

def telegram_bot_sendText(msg):
    token = "<API權杖>"
    chat_id = "<聊天室識別碼>"
    url = "https://api.telegram.org/bot{0}/sendMessage?chat_id={1}&text={2}"
    r = requests.post(url.format(token,chat_id,msg))  
    return r.json()

telegram_bot_sendText(temp +"/" + summary)

print('------------------------------------------------------------')	#60個

