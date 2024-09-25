import sys

print("------------------------------------------------------------")  # 60個

'''
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

import twstock

print(twstock.codes["2330"])

print("------------------------------------------------------------")  # 60個

import twstock

stock = twstock.Stock("2330") 
print("股票代號:", stock.sid)
print("各日收盤價:", stock.price)
print("各日最高價:", stock.high)
print("各日最低價:", stock.low)
print("各日成交股數:", stock.capacity)
print("各日的日期:", stock.date)

print("------------------------------------------------------------")  # 60個

import pandas as pd
import twstock

stock = twstock.Stock("2330") 
data = stock.fetch(2020, 7)

df = pd.DataFrame(data)
df["date"] = pd.to_datetime(df["date"]) 
df = df.set_index("date")
df[["close","open","high","low"]].plot()

print("------------------------------------------------------------")  # 60個

import pandas as pd
import twstock

stock = twstock.Stock("2330") 
data = stock.fetch_from(2020, 7)

df = pd.DataFrame(data)
df["date"] = pd.to_datetime(df["date"]) 
df = df.set_index("date")
df[["close","open","high","low"]].plot()

print("------------------------------------------------------------")  # 60個

import twstock

data = twstock.realtime.get("2330")
print(data)
print("----------------------------")
data = twstock.realtime.get(['2330', '2337', '2409'])
print(data)
'''
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

import pandas as pd
import twstock

stock = twstock.Stock("2330") 
data = stock.fetch_from(2019, 1)

df = pd.DataFrame(data)
df["date"] = pd.to_datetime(df["date"]) 
df = df.set_index("date")

df["5_Day_Mean"] = df["close"].rolling(window=5).mean()
df["20_Day_Mean"] = df["close"].rolling(window=20).mean()
df["60_Day_Mean"] = df["close"].rolling(window=60).mean()

df[["5_Day_Mean","20_Day_Mean","60_Day_Mean"]].plot(figsize=(10, 5))

print("------------------------------------------------------------")  # 60個

import twstock

stock = twstock.Stock("2330") 
ma_p = stock.moving_average(stock.price, 5)
print("五日均價:", ma_p)
ma_c = stock.moving_average(stock.capacity, 5)
print("五日均量:", ma_c)
ma_p_cont = stock.continuous(ma_p)
print("五日均價持續天數:", ma_p_cont)
ma_br = stock.ma_bias_ratio(5, 10)
print("五日、十日乖離率:", ma_br)
ma_brp = stock.ma_bias_ratio_pivot(stock.price, 5, True)
print("正乖離率轉折位置:", ma_brp)
ma_brp2 = stock.ma_bias_ratio_pivot(stock.price, 5, False)
print("負乖離率轉折位置:", ma_brp2)

print("------------------------------------------------------------")  # 60個

import twstock
from twstock import BestFourPoint

stock = twstock.Stock("2330") 
bfp = BestFourPoint(stock)

bfp_buy = bfp.best_four_point_to_buy()
print("是否為四大買點:", bfp_buy)
bfp_sell = bfp.best_four_point_to_sell()
print("是否為四大賣點:", bfp_sell)
bfp_result = bfp.best_four_point()
print("綜合判斷:", bfp_result)

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

