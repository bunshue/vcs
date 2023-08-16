import time
import pyautogui as auto
from IPython.display import clear_output

while True:
    x, y = auto.position()
    clear_output()
    print(x, y)
    time.sleep(0.5)
    if x < 10:
        break

print('------------------------------------------------------------')	#60個

import pyautogui as auto
import time

auto.PAUSE = 1
x, y = 630, 20
auto.moveTo(x, y, 2)
auto.click()
x, y = 264, 62
auto.moveTo(x, y, 2)
auto.click()
auto.typewrite("https://hophd.wordpress.com")
time.sleep(2)
auto.press("enter")

print('------------------------------------------------------------')	#60個

from selenium import webdriver
import time
url = "https://hophd.wordpress.com"
web = webdriver.Chrome("chromedriver.exe")
web.implicitly_wait(60)
web.get(url)
web.set_window_position(0, 0)
time.sleep(10)
web.quit()

print('------------------------------------------------------------')	#60個

import json
import requests

api_url = "https://www.dcard.tw/_api/forums/funny/posts?limit=100"
res = requests.get(api_url).text

data = json.loads(res)
for post in data:
    print(post["title"])

print('------------------------------------------------------------')	#60個

import urllib.request
import time
import os
data = json.loads(res)
for post in data:
    if len(post["media"])>0:
        for image in post["media"]:
            imgurl = image["url"]
            print(imgurl)
            if ".jpg" in imgurl or ".png" in imgurl:
                urllib.request.urlretrieve(imgurl, os.path.basename(imgurl))
            time.sleep(3)

print(res)

print('------------------------------------------------------------')	#60個

import json
import requests

api_url = "https://www.dcard.tw/_api/forums/funny/posts?limit=100"
res = requests.get(api_url).text

data = json.loads(res)
for post in data:
    print(post["title"])

print(res)

print('------------------------------------------------------------')	#60個

import json
import urllib.parse
import requests

url = "https://udn.com/api/more?page=2&id=&channelId=1&cate_id=0&type=breaknews&totalRecNo=6561"

html = requests.get(url).text
data = json.loads(html)

titles = data['lists']
for title in titles:
    print(title['title'])
    print(urllib.parse.urljoin("https://udn.com", title['titleLink']))

print('------------------------------------------------------------')	#60個

import requests
url = "https://ck101.com/forum-3590-1.html?ref=nav"
res = requests.get(url)
print(res)
print(res.text)

print('------------------------------------------------------------')	#60個

import requests
url = "https://ck101.com/forum-3590-1.html?ref=nav"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
}
res = requests.get(url, headers=headers)
print(res)
print(res.text)

print('------------------------------------------------------------')	#60個

import requests
url = "https://www.mobile01.com/topiclist.php?f=751"
res = requests.get(url)
print(res)

print('------------------------------------------------------------')	#60個

import requests
url = "https://www.mobile01.com/topiclist.php?f=751"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
}
html = requests.get(url, headers=headers).text

print('------------------------------------------------------------')	#60個

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "html.parser")
pages = soup.find_all("a", class_="c-pagination")
print(pages[-1].text)

print('------------------------------------------------------------')	#60個

titles = soup.find_all("div", class_="c-listTableTd__title")
print(len(titles))
for title in titles:
    print(title)
    print(title.a.text)
    print(title.a['href'])

print('------------------------------------------------------------')	#60個

import requests
url = "https://www.lexuscpo.com.tw/Home/CarStock"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
}
form_data = {
    "CarType":"", 
    "Series": "",
    "Price": "", 
    "Year": "", 
    "Mileage":"", 
    "StoreID":"", 
    "Page": "",
    "Limit": "20"
}
res = requests.post(url, data=form_data, headers=headers)
data = res.text

print('------------------------------------------------------------')	#60個

import json
cars = json.loads(data)
cars = cars['rows']
message = "{:<10}({}年式)，{:>10,}KM，售價：{:>10,}元"
for car in cars:
    print(message.format(
        car['Model'], 
        car['Year'],
        car['Mileage'],
        car['SellPrice']))

print('------------------------------------------------------------')	#60個






print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個






