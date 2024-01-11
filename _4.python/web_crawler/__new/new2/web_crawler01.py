import sys

print('------------------------------------------------------------')	#60個

from urllib.parse import urlparse

o = urlparse("http://www.example.com:80/test/index.php?user=joe")

print('使用urlparse()方法剖析URL網址成為組成的元素')
print("通訊協定: ", o.scheme)
print("網域名稱: ", o.netloc)
print("通訊埠號: ", o.port)
print("網頁路徑: ", o.path)
print("查詢字串: ", o.query)

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

import sys
import requests

url = "https://fchart.github.io/test.html"
response = requests.get(url)
if response.status_code == 200:
    print("Text :\n", response.text)
    print("編碼: ", response.encoding)
    print("status_code : ", response.status_code)
else:
    print("錯誤! HTTP請求失敗...")

print('------------------------------------------------------------')	#60個

url_params = {'name': '陳會安', 'grade': 95}
r = requests.get("http://httpbin.org/get", params=url_params)
if r.status_code == 200:
    print(r.text)
else:
    print("錯誤! HTTP請求失敗...")

print('------------------------------------------------------------')	#60個

url = "http://httpbin.org/user-agent"
 
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
r = requests.get(url, headers=headers)
print(r.text)

print('------------------------------------------------------------')	#60個

url = "http://httpbin.org/user-agent"
 
r = requests.get(url)
print(r.text)

print('------------------------------------------------------------')	#60個

url = "http://httpbin.org/cookies"

cookies = dict(name='Joe Chen')
r = requests.get(url, cookies=cookies)
print(r.text)

print('------------------------------------------------------------')	#60個

post_data = {'name': '陳會安', 'grade': 95}
r = requests.post("http://httpbin.org/post", data=post_data)
print(r.text)

print('------------------------------------------------------------')	#60個

url = "https://www.ptt.cc/bbs/Gossiping/index.html"

cookies = { "over18": "1" }
r = requests.get(url, cookies=cookies)
print(r.text)

print('------------------------------------------------------------')	#60個

""" fail chromedriver
from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/test.html")
print(driver.title)
html = driver.page_source
print(html)
driver.quit()

print('------------------------------------------------------------')	#60個

from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
cookie = {"name": "over18", "value": "1"}
driver.get("https://www.ptt.cc/bbs/Gossiping/index.html")
driver.add_cookie(cookie)
print(driver.title)
driver.quit()

print('------------------------------------------------------------')	#60個

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome("./chromedriver", options=options)
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/test.html")
print(driver.title)
html = driver.page_source
print(html)
driver.quit()
"""

print('------------------------------------------------------------')	#60個

url = "https://www.taifex.com.tw/cht/3/totalTableDate"
post_data = "queryType=1&goDay=&doQuery=1&dateaddcnt=&queryDate=2020%2F08%2F07"
r = requests.post(url, data=post_data)
print(r.text)

print('------------------------------------------------------------')	#60個

url = "https://api.sgx.com/derivatives/v1.0/contract-code/TW?order=asc&orderby=delivery-month&category=futures&session=-1&t=1596956628001&showTAICTrades=false"
r = requests.get(url)
print(r.text)

print('------------------------------------------------------------')	#60個

""" fail chromedriver
from selenium import webdriver
import time

url = "https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=Python&jobcatExpansionType=1&order=12&asc=0&page=6&mode=s&jobsource=2018indexpoc"
driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get(url)
print(driver.title)
print(len(driver.page_source))
for x in range(5):
    js = "window.scrollTo(0, document.body.scrollHeight)"
    driver.execute_script(js)
    time.sleep(3)
    print(x+1, len(driver.page_source))
driver.quit()
"""
print('------------------------------------------------------------')	#60個

import json
import csv

csvfile = "tmp_tw_sgx.csv"
url = "https://api.sgx.com/derivatives/v1.0/contract-code/TW?order=asc&orderby=delivery-month&category=futures&session=-1&t=1596956628001&showTAICTrades=false"
r = requests.get(url)
json_data = json.loads(r.text)
output = []
for data in json_data["data"]:
    item = []
    item.append(data["last-update-time"])
    item.append(data["last-trading-date"])
    item.append(data["symbol"])
    if data["current-trading-session"] == "0":
       item.append("T")
    else:
       item.append("T+1")
    item.append(data["change-abs"])
    item.append(data["change-percentage"])
    item.append(data["session-open-abs"])
    item.append(data["session-traded-high-abs"])
    item.append(data["session-traded-low-abs"])
    item.append(data["last-traded-price-abs"])
    item.append(data["daily-settlement-price-abs"])
    item.append(data["total-volume"])
    item.append(data["open-interest"])
    output.append(item)

with open(csvfile, 'w+', newline='') as fp:
    writer = csv.writer(fp)
    writer.writerow(["last-update-time","last-trading-date","symbol",
                     "current-trading-session","change-abs",
                     "change-percentage","session-open-abs",
                     "session-traded-high-abs","session-traded-low-abs",
                     "last-traded-price-abs","daily-settlement-price-abs",
                     "total-volume","open-interest"])
    for row in output:
        writer.writerow(row)

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

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

""" fail
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
"""
print('------------------------------------------------------------')	#60個

""" fail API key
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
"""

print('------------------------------------------------------------')	#60個

""" fail
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
"""
print('------------------------------------------------------------')	#60個

""" fail api key
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
"""
print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個

