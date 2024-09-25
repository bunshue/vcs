import sys

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup
import re
from selenium import webdriver
"""
url = "https://www.bloomberg.com/quote/SPX:IND"
driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get(url)
soup = BeautifulSoup(driver.page_source, "lxml")
regex = re.compile('^companyName.*')
name_box = soup.find("h1", class_= regex)
name = name_box.text
print(name)
price_box = soup.find("span", attrs={"class":re.compile("^priceText.*")})
price = price_box.text
print(price)
driver.quit()
"""
print("------------------------------------------------------------")  # 60個

import requests
import pandas as pd
import time
from fake_useragent import UserAgent

dates = [20200601, 20200701, 20200801]
stockNo = 2330
url = "https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=html&date={}&stockNo={}"
ua = UserAgent()

for date in dates :
    print(date, stockNo)
    headers = {"User-Agent": ua.random}
    r = requests.get(url.format(date, stockNo), headers=headers)
    csvfile = "tmp_{}_{}.csv".format(stockNo, date)    

    data = pd.read_html(r.text)[0]
    data.columns = data.columns.droplevel(0)
    data.to_csv(csvfile, index=False)
    time.sleep(5)

print("------------------------------------------------------------")  # 60個

import pandas_datareader as pdr

""" NG
df = pdr.DataReader("2330.TW", "yahoo")

print(df.shape)
print(df.head())
"""

print("------------------------------------------------------------")  # 60個

import datetime
import pandas_datareader as pdr

start = datetime.datetime.now() - datetime.timedelta(days=60)
end = datetime.date.today()
""" NG
df = pdr.DataReader("2330.TW", "yahoo", start, end)
print(df.shape)
print(df.head())
"""
print("------------------------------------------------------------")  # 60個

import requests

date = "20200820"
url = "https://www.twse.com.tw/fund/T86?response=json&date={}&selectType=ALL"
r = requests.get(url.format(date))
content = r.content
csv_file = open("tmp_three_major1.json", "wb")
csv_file.write(content)
csv_file.close()

print("------------------------------------------------------------")  # 60個

import requests

date = "20200820"
url = "https://www.twse.com.tw/fund/T86?response=csv&date={}&selectType=ALL"
r = requests.get(url.format(date))
content = r.content
csv_file = open("tmp_three_major2.csv", "wb")
csv_file.write(content)
csv_file.close()

print("------------------------------------------------------------")  # 60個

import requests
import pandas as pd
import json

date = "20200820"
url = "https://www.twse.com.tw/fund/T86?response=json&date={}&selectType=ALL"
r = requests.get(url.format(date))
if r.status_code == requests.codes.ok:
    print("成功爬取資料...")
    """# NG
    data = r.json() 
    df = pd.read_json(json.dumps(data["data"]))
    df.columns = data["fields"]
    print(df.head())
    df.to_csv("tmp_three_major3.csv", index=False)
    """
else:
    print("HTTP請求錯誤...")

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup
import re
from selenium import webdriver
"""
url = "https://www.bloomberg.com/quote/CCMP:IND"
driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get(url)
soup = BeautifulSoup(driver.page_source, "lxml")
regex = re.compile('^companyName.*')
name_box = soup.find("h1", class_= regex)
name = name_box.text
print(name)
price_box = soup.find("span", attrs={"class":re.compile("^priceText.*")})
price = price_box.text
print(price)
driver.quit()
"""
print("------------------------------------------------------------")  # 60個

