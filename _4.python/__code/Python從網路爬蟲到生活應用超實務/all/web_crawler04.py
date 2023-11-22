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

url = "https://www.ptt.cc/bbs/Gossiping/index.html"

cookies = { "over18": "1" }
r = requests.get(url, cookies=cookies)
print(r.text)

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

print('------------------------------------------------------------')	#60個

import json
import csv

csvfile = "tw_sgx.csv"
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
