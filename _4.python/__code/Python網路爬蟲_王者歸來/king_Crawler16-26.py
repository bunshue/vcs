"""
Python網路爬蟲_大數據擷取、清洗、儲存與分析：王者歸來
ch16~ch26
"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小


def show():
    plt.show()
    pass


import bs4
import requests
import json
import csv

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# ch16_1.py

url = "https://www.biqukan.com/50_50096/"
htmlfile = requests.get(url)
print("原先編碼 : ", htmlfile.encoding)
objSoup = bs4.BeautifulSoup(htmlfile.text, "lxml")
book_author = objSoup.find("meta", property="og:novel:author")
book_title = objSoup.find("meta", property="og:novel:book_name")
book_description = objSoup.find("meta", property="og:description")
print("作者     : ", book_author["content"])
print("書名     : ", book_title["content"])
print("內文描述 : ", book_description["content"].strip())

print("------------------------------------------------------------")  # 60個

# ch16_2.py

url = "https://www.biqukan.com/50_50096/"
htmlfile = requests.get(url)
print("原先編碼 : ", htmlfile.encoding)
htmlfile.encoding = "gbk"
print("現在編碼 : ", htmlfile.encoding)
objSoup = bs4.BeautifulSoup(htmlfile.text, "lxml")
book_author = objSoup.find("meta", property="og:novel:author")
book_title = objSoup.find("meta", property="og:novel:book_name")
book_description = objSoup.find("meta", property="og:description")
print("作者     : ", book_author["content"])
print("書名     : ", book_title["content"])
print("內文描述 : ", book_description["content"].strip())

print("------------------------------------------------------------")  # 60個

# ch16_3.py

url = "https://www.biqukan.com/50_50096/"
htmlfile = requests.get(url)
htmlfile.encoding = "gbk"
objSoup = bs4.BeautifulSoup(htmlfile.text, "lxml")

storys = objSoup.find("div", "listmain")
story = storys.find_all("dt")  # 取書籍標題
print(story[1].text)  # 列出書籍標題
print()
sto = storys.find_all("dd")  # 取全部章節標題
sto = sto[12:]  # 切片捨去前12回標題
for ch in sto:  # 列出三國演義正文卷
    print(ch.text)

print("------------------------------------------------------------")  # 60個

# ch16_4.py

chapter_url = []
web_url = "https://www.biqukan.com"
url = "https://www.biqukan.com/50_50096/"
htmlfile = requests.get(url)
htmlfile.encoding = "gbk"
objSoup = bs4.BeautifulSoup(htmlfile.text, "lxml")

storys = objSoup.find("div", "listmain")
story = storys.find_all("dt")  # 取書籍標題
print(story[1].text)  # 列出書籍標題
print()
sto = storys.find_all("dd")  # 取全部章節標題
sto = sto[12:]  # 切片捨去前12回標題
for ch in sto:  # 列出三國演義正文卷
    ch_url = ch.a["href"]  # 取得章節標題片段網址
    chapter_url.append(web_url + ch_url)  # 將完整章節內容網址存入

for c_url in chapter_url:
    print(c_url)  # 列出完整章節內容網址

print("------------------------------------------------------------")  # 60個

# ch16_5.py

url = "https://www.biqukan.com/50_50096/18520412.html"  # 第一回的網址
htmlfile = requests.get(url)
htmlfile.encoding = "gbk"
objSoup = bs4.BeautifulSoup(htmlfile.text, "lxml")
title = objSoup.find("h1")  # 第一回標題
print(title.text)  # 列印第一回標題
print()
contents = objSoup.find("div", id="content")  # 內文位置
print("區塊數量 : ", len(contents))
for content in contents:
    print(" ============================================ ")
    print("資料型態 : ", type(content))
    if type(content) == bs4.element.NavigableString:
        txt = content.strip()  # 列印內文
        print(txt)

print("------------------------------------------------------------")  # 60個

# ch16_6.py

url = "https://www.biqukan.com/50_50096/18520412.html"  # 第一回的網址
htmlfile = requests.get(url)
htmlfile.encoding = "gbk"
objSoup = bs4.BeautifulSoup(htmlfile.text, "lxml")
title = objSoup.find("h1")  # 第一回標題
print(title.text)  # 列印第一回標題
print()
contents = objSoup.find("div", id="content")  # 內文位置
for content in contents:
    if type(content) == bs4.element.NavigableString:  # 確定資料格式
        txt = content.strip()
        if type(txt) == str and txt != "":  # 確定是字串和不是空字串
            txt = content.strip()
            txt = txt.replace("&1t;/p>", "")  # 將末端字元刪除
            print(txt)  # 列印每段內文
            print()

print("------------------------------------------------------------")  # 60個

# ch16_7.py

story = ""  # 小說內文
url = "https://www.biqukan.com/50_50096/18520412.html"  # 第一回的網址
htmlfile = requests.get(url)
htmlfile.encoding = "gbk"
objSoup = bs4.BeautifulSoup(htmlfile.text, "lxml")
title = objSoup.find("h1")  # 第一回標題
story = story + title.text + "\n"  # 標題加入內文
contents = objSoup.find("div", id="content")  # 內文位置
for content in contents:
    if type(content) == bs4.element.NavigableString:  # 確定資料格式
        txt = content.strip()
        if type(txt) == str and txt != "":  # 確定是字串和不是空字串
            txt = content.strip()
            txt = txt.replace("&1t;/p>", "")  # 將末端字元刪除
            story = story + txt + "\n\n"  # 加入小說內文

fn = title.text
with open(fn, "w", encoding="utf-8") as obj:
    obj.write(story)
print("小說 %s 儲存成功" % title.text)

print("------------------------------------------------------------")  # 60個

# ch17_1.py

url = "https://www.thsrc.com.tw/tw/TimeTable/SearchResult"
htmlfile = requests.get(url)
objSoup = bs4.BeautifulSoup(htmlfile.text, "lxml")
stations = objSoup.find("select", id="StartStation").find_all("option")
print("高鐵站名與ID")
for station in stations:
    if station["value"]:
        print(station.text.strip(), " : ", station["value"])

print("------------------------------------------------------------")  # 60個

# ch17_2.py

url = "http://www.thsrc.com.tw/tw/TimeTable/Search"
# 讀者執行此程式時需要調整DepartueSearchDate,例如:調整今天日期未來1週日期
form = {
    "StartStation": "977abb69-413a-4ccf-a109-0272c24fd490",  # 台北站
    "EndStation": "f2519629-5973-4d08-913b-479cce78a356",  # 左營站
    "DepartueSearchDate": "2019/09/10",  # 查詢日期
    "DepartueSearchTime": "13:00",
    "SearchType": "S",
}

htmlfile = requests.post(url, data=form)
time_table = htmlfile.json()

col = ["TrainNumber", "DepartureTime", "DestinationTime", "Duration", "NonReservedCar"]
schedules = [["班次", "出發", "抵達", "行車時間", "自由座車廂"]]
for t in time_table["data"]["DepartureTable"]["TrainItem"]:
    schedules.append([t[c] for c in col])
for s in schedules:
    print(s)

print("------------------------------------------------------------")  # 60個

# ch18_1.py

url = "https://zh.wikipedia.org/"
url_tsmc = "https://zh.wikipedia.org/wiki/%E5%8F%B0%E7%81%A3%E7%A9%8D%E9%AB%94%E9%9B%BB%E8%B7%AF%E8%A3%BD%E9%80%A0"
tsmchtml = requests.get(url_tsmc)
objSoup = bs4.BeautifulSoup(tsmchtml.text, "lxml")
tsmc = objSoup.find("div", id="content")  # 標題
print(tsmc.h1.text)

wi = tsmc.find("div", id="siteSub")  # 維基百科
print(wi.text)

info = tsmc.find("p")  # 台積電主文
print(info.text)

print("------------------------------------------------------------")  # 60個

# ch18_2.py

url = "https://zh.wikipedia.org/wiki/%E5%8F%B0%E7%81%A3%E7%A9%8D%E9%AB%94%E9%9B%BB%E8%B7%AF%E8%A3%BD%E9%80%A0"
tsmchtml = requests.get(url)
objSoup = bs4.BeautifulSoup(tsmchtml.text, "lxml")
tsmc = objSoup.find("tbody")
for t in tsmc:
    col = t.find("th", "fn org")  # 標題
    if col:
        print(col.text.strip())
    col = t.find("th", scope="row")  # 欄位名稱
    if col:
        print(col.text.strip(), ": ", end="")
    col = t.find("td")  # 欄位內容
    if col:
        print(col.text.strip())

print("------------------------------------------------------------")  # 60個

# ch18_3.py

url = "https://zh.wikipedia.org/wiki/台灣積體電路製造"
tsmchtml = requests.get(url)
objSoup = bs4.BeautifulSoup(tsmchtml.text, "lxml")
tsmc = objSoup.find("tbody")
for t in tsmc:
    col = t.find("th", "fn org")  # 標題
    if col:
        print(col.text.strip())
    col = t.find("th", scope="row")  # 欄位名稱
    if col:
        print(col.text.strip(), ": ", end="")
    col = t.find("td")  # 欄位內容
    if col:
        print(col.text.strip())

print("------------------------------------------------------------")  # 60個

# ch19_1.py

url = "https://graph.facebook.com/v3.3/me/posts?limit=2&access_token=EAAIZCihE7RSkBAJ3fRRbKyOc7dDa17GkCN2YTH6AS2KJ1yjU8AY4czB5oaXk9CBpPCmtmJ9ZCPCjrILe6TfT4eDkcLoPyyZArHzyIrZAYQmd6mrZCOItIRL65fboQpLjl7vFLPrUuTZAVpp7UwwkEkKShDoHjQ0BFUsVOL8m1lLJKDA2IF6pI0eDPYrfdyOIEvezXLZCRj6fgZDZD"

data = json.loads(requests.get(url).text)  # 下載json資料轉成字典
print(data)

print("------------------------------------------------------------")  # 60個

# ch19_2.py

url = "https://graph.facebook.com/v3.3/me/posts?limit=2&access_token=EAAIZCihE7RSkBAJ3fRRbKyOc7dDa17GkCN2YTH6AS2KJ1yjU8AY4czB5oaXk9CBpPCmtmJ9ZCPCjrILe6TfT4eDkcLoPyyZArHzyIrZAYQmd6mrZCOItIRL65fboQpLjl7vFLPrUuTZAVpp7UwwkEkKShDoHjQ0BFUsVOL8m1lLJKDA2IF6pI0eDPYrfdyOIEvezXLZCRj6fgZDZD"

data = json.loads(requests.get(url).text)  # 下載json資料轉成字典

for info in data["data"]:
    print("我的Facebook發文")
    print("發文日期", info["created_time"])
    print("發文內容", info["message"])
    print("發文的id", info["id"])
    print()

print("------------------------------------------------------------")  # 60個

# ch19_3.py
import facebook

token = "EAAIZCihE7RSkBAAbuMKPfDXeCZABa8DHZBF3Arr4ZCgg62vy4cZA41Vz7SBzRLIjfnVJlgHhyIfr7MNnrXOUCQ4LrdJ841mNI600UBLS5qJAMMrXkcHZAnCvj9vZAKmGQE4DeSnWLN1UZBDsX1RYVLxXoikMuZAndv0gxGKoKumN4oJcPmI4RjKgWo5oDDIJf4fCrjphCy8VMwwZDZD"
graph = facebook.GraphAPI(access_token=token, version="3.1")

mypost = graph.get_object(id="1116138285252667_1113470975519398")
print("列出發文資料型態 : ", type(mypost))
print("列出發文資料內容 : ", mypost)
print("發文日期 : ", mypost["created_time"])
print("發文內容 : ", mypost["message"])
print("發文的id : ", mypost["id"])

print("------------------------------------------------------------")  # 60個

# ch19_4.py

import facebook

token = "EAAIZCihE7RSkBAKnGeo0AKdvoZB5n64xpQs2nJNxSywAMf5s7JDX6ADKvBBZABLeMrNKtAsaKBOmMmg2yDEaoXZA9pnFPC2OWQVoe7TLPFAFmJhS9sfpZCVq1UWIjmZAJS3YtMGBqomWScofJEhC5ulZCMIYoZC6as29rP86WHA4WMzB7DKuq5wLa6KxzrzDBbXeZA0SMZBwWxkwZDZD"
graph = facebook.GraphAPI(access_token=token, version="3.1")

idsList = ["1116138285252667_1113470975519398", "1116138285252667_1112637295602766"]
mypost = graph.get_objects(ids=idsList)

for ids in idsList:
    post = mypost[ids]  # 取得特定id發文物件
    print("列出發文資料內容 : ", post)
    print("發文日期 : ", post["created_time"])
    print("發文內容 : ", post["message"])
    print("發文的id : ", post["id"])
    print()

print("------------------------------------------------------------")  # 60個

# ch19_5.py

import facebook

token = "EAAIZCihE7RSkBAKnGeo0AKdvoZB5n64xpQs2nJNxSywAMf5s7JDX6ADKvBBZABLeMrNKtAsaKBOmMmg2yDEaoXZA9pnFPC2OWQVoe7TLPFAFmJhS9sfpZCVq1UWIjmZAJS3YtMGBqomWScofJEhC5ulZCMIYoZC6as29rP86WHA4WMzB7DKuq5wLa6KxzrzDBbXeZA0SMZBwWxkwZDZD"
graph = facebook.GraphAPI(access_token=token, version="3.1")

mypost = graph.get_object(id="1116138285252667_1113470975519398?fields=message")
print("列出發文資料內容 : ", mypost)
print("發文內容 : ", mypost["message"])

print("------------------------------------------------------------")  # 60個

# ch19_6.py

import facebook

token = "EAAPGT8IPNwcBAHAU5QjYgyAw23bUinXqBpUZC8OU3VAeeWFK4clu7cA1KQ4pQHCZARofcGhctGML7itS7GPDehMFxG9lbSANtzXDC3UXrhzB7RX0OXaDj8bR1VhqWw6VxFSlDLlmuycMZBjrrFGPJbxZAdGQKTnQLhZBPKkCbMRZC5H2L5bt4V8Ur2cRSQlyFpIOdnX5D6ZCEXnVO4FAkza406TBRKogQckPl0swBo1UgZDZD"
graph = facebook.GraphAPI(access_token=token, version="3.1")
mylikes = graph.get_connections(id="me", connection_name="likes")

likes = mylikes["data"]
print("按讚的社團數 : ", len(likes))
for like in likes:
    print(like["name"])

print("------------------------------------------------------------")  # 60個

# ch19_7.py

import facebook

token = "EAAIZCihE7RSkBABhXYIw4tJiBWtBZCzSgxws8kH0Ia0nmXJQLIosh3F5JZBtZCgb1Y7IbtSJW40Lzy5awL7ZAgZBmrzFgxJkQjZCqdm0FCrinwZCh1F6mwZCNCdx0DXnKDlrw7HHs2O0QjosayoTvx1zrQu1VihimzZAmWgQZC6mZB1ojn98GEL9xtNdFOxLOwJ8D6KYFQn5ZA6hhlQZDZD"
graph = facebook.GraphAPI(access_token=token, version="3.1")
friends = graph.get_connections(id="me", connection_name="friends")

print(friends)
print("我的臉書朋友總數 : ", friends["summary"]["total_count"])

print("------------------------------------------------------------")  # 60個

# ch19_8.py

import facebook

token = "EAAIZCihE7RSkBABhXYIw4tJiBWtBZCzSgxws8kH0Ia0nmXJQLIosh3F5JZBtZCgb1Y7IbtSJW40Lzy5awL7ZAgZBmrzFgxJkQjZCqdm0FCrinwZCh1F6mwZCNCdx0DXnKDlrw7HHs2O0QjosayoTvx1zrQu1VihimzZAmWgQZC6mZB1ojn98GEL9xtNdFOxLOwJ8D6KYFQn5ZA6hhlQZDZD"
graph = facebook.GraphAPI(access_token=token, version="3.1")
idsList = "1116138285252667_1113470975519398?fields=likes.summary(true)"
mylikes = graph.get_object(id=idsList)

# 這篇貼文必須本人有按讚
likes = mylikes["likes"]["data"]
for like in likes:
    print("按讚人 : ", like["name"])

num = mylikes["likes"]["summary"]
print("按讚總人數 : ", num["total_count"])

print("------------------------------------------------------------")  # 60個

# ch19_9.py
import facebook
import shutil

token = "EAAIZCihE7RSkBANrFuCjLGvzXurRpF3VZASyM5XOsKc8Ek3ZAF9jazB4x8YQSpKDabaTCzfLXcgZBbvJkuNWFEcs7pnrZCDMiXvxBImlXGmAh0NhXPnsYRyBqYGNHpHhS3FtbsgFZB0N0yBXgTTZAHAvBLBLhOHpYHqoHHIbj3uXs8EXynmBW6KbZCRrn518lxviw0DterMlpAZDZD"
graph = facebook.GraphAPI(access_token=token, version="3.1")

picture = graph.get_connections(id="me", connection_name="photos?fields=images")

photos = picture["data"]

mydir = "out32_9"
if not os.path.exists(mydir):
    os.mkdir(mydir)
n = 0
for p in photos:
    imageList = p["images"]
    n += 1
    if n > 10:
        break
    for pict in imageList:
        filename = pict["source"].split("/")[-1].split("?")[0]
        dst = open(mydir + "/" + filename, "wb")
        fig = requests.get(pict["source"], stream=True)
        shutil.copyfileobj(fig.raw, dst)
        dst.close()

print("------------------------------------------------------------")  # 60個

# ch20_1.py
from pprint import pprint

url = "https://maps.googleapis.com/maps/api/geocode/json?address=總統府&key=YOUR_API_KEY"
gmap = requests.get(url)
gsoup = bs4.BeautifulSoup(gmap.text, "lxml")
g_info = json.loads(gsoup.text)

data = g_info["results"][0]
address = data["formatted_address"]
lat = data["geometry"]["location"]["lat"]
lng = data["geometry"]["location"]["lng"]
print("地址 : ", address)
print("緯度 : ", lat)
print("經度 : ", lng)

print("------------------------------------------------------------")  # 60個

# ch20_2.py

import googlemaps
from pprint import pprint

api_key = "YOUR_API_KEY"
gmap_obj = googlemaps.Client(key=api_key)
gmap_info = gmap_obj.geocode("總統府")
pprint(gmap_info)  # 可以一行列印一個元素

print("------------------------------------------------------------")  # 60個

# ch20_3.py

import googlemaps
from pprint import pprint

api_key = "YOUR_API_KEY"
gmap_obj = googlemaps.Client(key=api_key)
gmap_info = gmap_obj.geocode("總統府")

address = gmap_info[0]["formatted_address"]
lat = gmap_info[0]["geometry"]["location"]["lat"]
lng = gmap_info[0]["geometry"]["location"]["lng"]
print("地址 : ", address)
print("緯度 : ", lat)
print("經度 : ", lng)

print("------------------------------------------------------------")  # 60個

# ch20_4.py

from pprint import pprint

url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=25.0329694,121.5654177&radius=3500&type=school&key=YOUR_API_KEY"
gmap = requests.get(url)
gsoup = bs4.BeautifulSoup(gmap.text, "lxml")
g_info = json.loads(gsoup.text)
schools = g_info["results"]
print("列出搜尋到結果的資料型態 : ", type(schools))
print("列出搜尋到結果的資料長度 : ", len(schools))
print("列出搜尋到第0筆資料型態  : ", type(schools[0]))
print("列出第0筆資料內容")
pprint(schools[0])

print("------------------------------------------------------------")  # 60個

# ch20_5.py

from pprint import pprint

url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=25.0329694,121.5654177&radius=3500&type=school&key=YOUR_API_KEY"
gmap = requests.get(url)
gsoup = bs4.BeautifulSoup(gmap.text, "lxml")
g_info = json.loads(gsoup.text)
schools = g_info["results"]
for data in schools:
    print(data["name"])

print("------------------------------------------------------------")  # 60個

# ch21_1.py

from selenium import webdriver

# 網址處理
url_yahoo = "https://tw.bid.yahoo.com/search/auction/product?"
url_product = "kw=薩爾達傳說&p=薩爾達傳說&sort=-ptime"
url = url_yahoo + url_product
# 擷取網頁
driverPath = "D:\geckodriver\chromedriver.exe"
browser = webdriver.Chrome(executable_path=driverPath)
browser.implicitly_wait(5)  # 等待網頁載入
browser.get(url)  # 網頁下載至瀏覽器
# 商品連結
linkPath = "//ul[@class='gridList']/li/a"
product_links = browser.find_elements_by_xpath(linkPath)
product_link = product_links[0].get_attribute("href")
print("商品連結 : ", product_link)
# 商品名稱
titlePath = "//span[contains(@class,'BaseGridItem__title___2HWui')]"
product_titles = browser.find_elements_by_xpath(titlePath)
product_title = product_titles[0].get_attribute("textContent")
print("商品名稱 : ", product_title)
# 商品價格
pricePath = "//span[contains(@class,'BaseGridItem__price___31jkj')]/em"
product_prices = browser.find_elements_by_xpath(pricePath)
product_price = product_prices[0].text
print("商品價格 : ", product_price)

print("------------------------------------------------------------")  # 60個

# ch21_2.py

from selenium import webdriver

# 網址處理
url_yahoo = "https://tw.bid.yahoo.com/search/auction/product?"
url_product = "kw=薩爾達傳說&p=薩爾達傳說&sort=-ptime"
url = url_yahoo + url_product
# 擷取網頁
driverPath = "D:\geckodriver\chromedriver.exe"
browser = webdriver.Chrome(executable_path=driverPath)
browser.implicitly_wait(5)  # 等待網頁載入
browser.get(url)  # 網頁下載至瀏覽器
# 商品連結
linkPath = "//ul[@class='gridList']/li/a"
product_links = browser.find_elements_by_xpath(linkPath)

# 商品名稱
titlePath = "//span[contains(@class,'BaseGridItem__title___2HWui')]"
product_titles = browser.find_elements_by_xpath(titlePath)

# 商品價格
pricePath = "//span[contains(@class,'BaseGridItem__price___31jkj')]/em"
product_prices = browser.find_elements_by_xpath(pricePath)

# 計算商品數量
num = len(product_titles)
print("商品數量 : ", num)
print("-" * 50)

# 列出商品資訊
for title, link, price in zip(product_titles, product_links, product_prices):
    print("商品名稱 : ", title.get_attribute("textContent"))
    print("商品連結 : ", link.get_attribute("href"))
    print("商品價格 : ", price.text)
    print("-" * 70)

print("------------------------------------------------------------")  # 60個

# ch22_1.py

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 搜尋條件
city = "台北巿"
checkin_time = "2019-11-24"
checkout_time = "2019-11-25"
# 網址處理
url = "https://tw.hotels.com/"
# 擷取網頁
driverPath = "D:\geckodriver\chromedriver.exe"
browser = webdriver.Chrome(executable_path=driverPath)
browser.implicitly_wait(10)  # 等待網頁載入
browser.get(url)  # 網頁下載至瀏覽器
time.sleep(3)
searchNode = browser.find_elements_by_xpath("//input[contains(@id,'q-destination')]")
checkInNode = browser.find_elements_by_xpath(
    "//input[contains(@id,'q-localised-check-in')]"
)
checkOutNode = browser.find_elements_by_xpath(
    "//input[contains(@id,'q-localised-check-out')]"
)

# 輸入搜尋關鍵資料
searchNode[0].clear()  # 清除城市欄位
searchNode[0].send_keys(city)  # 輸入搜尋城市
time.sleep(3)
searchNode[0].send_keys(Keys.TAB)  # 按Tab跳到check in欄位
checkInNode[0].clear()  # 清除check in欄位
checkInNode[0].send_keys(checkin_time)  # 輸入check in時間
time.sleep(3)
searchNode[0].send_keys(Keys.TAB)  # 按Tab跳至check out欄位
checkOutNode[0].clear()  # 清除check out欄位
checkOutNode[0].send_keys(checkout_time)  # 輸入check out時間
time.sleep(3)
checkOutNode[0].send_keys(Keys.ENTER)  # 表單按Enter表示輸入完成
time.sleep(3)

# 旅館名稱
hotelPath = "//ol[@class='listings infinite-scroll-enabled']//h3/a"
names = browser.find_elements_by_xpath(hotelPath)
name = names[0].text
print("旅館名稱 : ", name)

# 旅館地址
addressPath = "//ol[@class='listings infinite-scroll-enabled']//span[@class='address']"
addresses = browser.find_elements_by_xpath(addressPath)
address = addresses[0].text
print("旅館地址 : ", address)

# 旅館星級評價
starPath = (
    "//ol[@class='listings infinite-scroll-enabled']//span[@class='star-rating-text']"
)
stars = browser.find_elements_by_xpath(starPath)
star = stars[0].text
print("旅館星級 : ", star)

# 旅館定價
listingpricePath = (
    "//ol[@class='listings infinite-scroll-enabled']//del[@data-reason='DRR-448']"
)
lprices = browser.find_elements_by_xpath(listingpricePath)
lprice = lprices[0].text  # 定價listing price
print("旅館定價 : ", lprice)

# 旅館售價
pricePath = "//ol[@class='listings infinite-scroll-enabled']//ins[@class='special-deal-animation']"
prices = browser.find_elements_by_xpath(pricePath)
price = prices[0].text  # 售價
print("旅館售價 : ", price)

print("------------------------------------------------------------")  # 60個

# ch22_2.py

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 搜尋條件
city = "台北市"
checkin_time = "2019-11-24"
checkout_time = "2019-11-25"
# 網址處理
url = "https://tw.hotels.com/"
# 擷取網頁
driverPath = "D:\geckodriver\chromedriver.exe"
browser = webdriver.Chrome(executable_path=driverPath)
browser.implicitly_wait(10)  # 等待網頁載入
browser.get(url)  # 網頁下載至瀏覽器
time.sleep(3)
searchNode = browser.find_elements_by_xpath("//input[contains(@id,'q-destination')]")
checkInNode = browser.find_elements_by_xpath(
    "//input[contains(@id,'q-localised-check-in')]"
)
checkOutNode = browser.find_elements_by_xpath(
    "//input[contains(@id,'q-localised-check-out')]"
)

# 輸入搜尋關鍵資料
searchNode[0].clear()  # 清除城市欄位
searchNode[0].send_keys(city)  # 輸入搜尋城市
time.sleep(3)
searchNode[0].send_keys(Keys.TAB)  # 按Tab跳到check in欄位
checkInNode[0].clear()  # 清除check in欄位
checkInNode[0].send_keys(checkin_time)  # 輸入check in時間
time.sleep(3)
searchNode[0].send_keys(Keys.TAB)  # 按Tab跳至check out欄位
checkOutNode[0].clear()  # 清除check out欄位
checkOutNode[0].send_keys(checkout_time)  # 輸入check out時間
time.sleep(3)
checkOutNode[0].send_keys(Keys.ENTER)  # 表單按Enter表示輸入完成
time.sleep(3)

# 旅館名稱
hotelPath = "//ol[@class='listings infinite-scroll-enabled']//h3/a"
names = browser.find_elements_by_xpath(hotelPath)
# 旅館地址
addressPath = "//ol[@class='listings infinite-scroll-enabled']//span[@class='address']"
addresses = browser.find_elements_by_xpath(addressPath)
# 旅館星級評價
starPath = (
    "//ol[@class='listings infinite-scroll-enabled']//span[@class='star-rating-text']"
)
stars = browser.find_elements_by_xpath(starPath)
# 旅館定價
listingpricePath = (
    "//ol[@class='listings infinite-scroll-enabled']//del[@data-reason='DRR-448']"
)
lprices = browser.find_elements_by_xpath(listingpricePath)
# 計算旅館數量
num = len(names)
print("旅館數量 : ", num)
print("-" * 70)
# 列出系列旅館資訊
for name, address, star, lprice in zip(names, addresses, stars, lprices):
    print("旅館名稱 : ", name.text)
    print("旅館地址 : ", address.text)
    print("旅館星級 : ", star.text)
    print("旅館定價 : ", lprice.text)
    print("-" * 70)
    time.sleep(1)

print("------------------------------------------------------------")  # 60個

# ch23_1.py

from pprint import pprint

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
            Safari/537.36",
}
url = "http://www.lovewzly.com/api/user/pc/list/search?"
# 傳遞參數
form_data = {"gender": "2", "mary": "1", "page": "1"}
datahtml = requests.get(url, params=form_data, headers=headers)

data = datahtml.json()
print("資料型態 : ", type(data))  # 列出資料型態
print("資料長度 : ", len(data))  # 列出資料長度
pprint(data)  # 列出第一頁資料

print("------------------------------------------------------------")  # 60個

# ch23_2.py

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
            Safari/537.36",
}
url = "http://www.lovewzly.com/api/user/pc/list/search?"
# 傳遞參數
form_data = {"gender": "2", "mary": "1", "page": "1"}
datahtml = requests.get(url, params=form_data, headers=headers)
datas = datahtml.json()
print(datas["data"]["list"][0])
print("-" * 70)
print("暱稱     : ", datas["data"]["list"][0]["username"])
print("Userid   : ", datas["data"]["list"][0]["userid"])
print("婚姻狀態 : ", datas["data"]["list"][0]["marry"])
print("性別     : ", "女" if datas["data"]["list"][0]["gender"] == "2" else "男")
print("居住省份 : ", datas["data"]["list"][0]["province"])
print("居住城市 : ", datas["data"]["list"][0]["city"])
print("出生年   : ", datas["data"]["list"][0]["birthdayyear"])
print("身高     : ", datas["data"]["list"][0]["height"])
print("薪資     : ", datas["data"]["list"][0]["salary"])
print("照片連結 : ", datas["data"]["list"][0]["avatar"])
print("自我介紹 : ", datas["data"]["list"][0]["monolog"])

print("------------------------------------------------------------")  # 60個

# ch23_3.py

fn = "out23_3.csv"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
            Safari/537.36",
}
url = "http://www.lovewzly.com/api/user/pc/list/search?"
# 傳遞參數
form_data = {"gender": "2", "mary": "1", "page": "1"}
datahtml = requests.get(url, params=form_data, headers=headers)
datas = datahtml.json()

fields = ["暱稱", "出生年", "學歷", "身高", "居住城市", "照片連結"]
data = datas["data"]["list"]
with open(fn, "w", newline="", encoding="utf-8") as csvfile:
    csvWriter = csv.writer(csvfile)
    csvWriter.writerow(fields)
    for d in data:
        d_list = [
            d["username"].encode("utf-8"),
            d["birthdayyear"],
            d["education"].encode("utf-8"),
            d["height"],
            d["city"].encode("utf-8"),
            d["avatar"],
        ]
        csvWriter.writerow(d_list)
        print("暱稱   : ", d["username"])
        print("出生年 : ", d["birthdayyear"])
        print("身高   : ", d["height"])
        print("-" * 70)

print("------------------------------------------------------------")  # 60個

# ch23_4.py


def get_data(page):
    # 正式抓取資料
    form_data["page"] = page
    print("目前抓取第 %s 頁資料 " % (page + 1))
    datahtml = requests.get(url, params=form_data, headers=headers)
    datas = datahtml.json()
    data = datas["data"]["list"]
    for d in data:
        d_list = [
            d["username"].encode("utf-8"),
            d["birthdayyear"],
            d["education"].encode("utf-8"),
            d["height"],
            d["city"].encode("utf-8"),
            d["avatar"],
        ]
        csvWriter.writerow(d_list)
        print("暱稱   : ", d["username"])


fn = "out23_4.csv"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
            Safari/537.36",
}
url = "http://www.lovewzly.com/api/user/pc/list/search?"
# 傳遞參數
form_data = {"gender": "2", "mary": "1", "page": "1"}

fields = ["暱稱", "出生年", "學歷", "身高", "居住城市", "照片連結"]
with open(fn, "w", newline="", encoding="utf-8") as csvfile:
    csvWriter = csv.writer(csvfile)
    csvWriter.writerow(fields)
    for p in range(10):
        get_data(p)
        print("-" * 70)
        time.sleep(random.randint(3, 10))  # 時間不規律爬取資料

print("------------------------------------------------------------")  # 60個

# ch23_5.py

from urllib.parse import unquote
from pprint import pprint
from pylab import mpl

df = pd.read_csv("out23_4.csv", index_col=0)
edu = df["學歷"]  # 獲得學歷欄位
education = []
for txt in edu:
    txt = txt[1:].replace("\\x", "%")  # 將字串轉成url字串
    txt = txt.replace("'", "")  # 拿掉'
    t = unquote(txt, encoding="utf-8")  # 轉成簡體中文
    education.append(t)  # 加入學歷字串
# 計算每個學歷欄位的人數
education_count = {wd: education.count(wd) for wd in set(education)}
edu_list = []  # 學歷串列
edu_count = []  # 學歷人數
for e, c in education_count.items():
    print(e, c)
    edu_list.append(e)
    edu_count.append(c)
# 繪製圓餅圖
mpl.rcParams["font.sans-serif"] = ["SimHei"]  # 使用黑體
plt.pie(
    edu_count, labels=edu_list, explode=(0, 0, 0.2, 0, 0, 0, 0), autopct="%1.2f%%"
)  # 繪製圓餅圖
plt.show()

print("------------------------------------------------------------")  # 60個

# ch23_6.py

from pylab import mpl

df = pd.read_csv("out23_4.csv", index_col=0)
height = df["身高"]  # 獲得身高欄位
h_index = [0, 0, 0, 0, 0]  # 身高區間欄位
for h in height:
    if int(h) < 150:
        h_index[0] += 1
    elif int(h) < 160:
        h_index[1] += 1
    elif int(h) < 170:
        h_index[2] += 1
    elif int(h) < 180:
        h_index[3] += 1
    else:
        h_index[4] += 1

fields = ["<150", "15x", "16x", "17x", ">180"]
# 繪製直條圖
mpl.rcParams["font.sans-serif"] = ["SimHei"]  # 使用黑體
plt.bar(fields, h_index, width=0.35)
plt.ylabel("人數")
plt.xlabel("身高")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch23_7.py

from pylab import mpl

df = pd.read_csv("out23_4.csv", index_col=0)
ages = df["出生年"]  # 獲得出生年欄位
age_index = [0, 0, 0, 0, 0]  # 歲數區間欄位

for age in ages:
    if int(age) < 1980:
        age_index[0] += 1  # 大於40歲
    elif int(age) < 1985:
        age_index[1] += 1  # 35 < age <= 40
    elif int(age) < 1990:
        age_index[2] += 1  # 30 < age <= 35
    elif int(age) < 1995:
        age_index[3] += 1  # 25 < age <= 30
    else:
        age_index[4] += 1  # 小於25

fields = [">40", "35-40", "30-35", "25-30", "<25"]
# 繪製直條圖
mpl.rcParams["font.sans-serif"] = ["SimHei"]  # 使用黑體
plt.bar(fields, age_index, width=0.35)
plt.ylabel("人數")
plt.xlabel("年齡")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch24_1.py

from requests_html import HTMLSession

session = HTMLSession()  # 定義Session
url = "http://aaa.24ht.com.tw"
r = session.get(url)  # get()
print(type(r))
print(type(r.html))
print(r.html)
print(type(r.html.text))
print("-" * 70)
print(r.html.text)

print("------------------------------------------------------------")  # 60個

# ch24_2.py

from requests_html import HTMLSession

session = HTMLSession()  # 定義Session
url = "https://python.org/"
r = session.get(url)  # get()
url_links = r.html.links
count = 0
print("相對位址超連結數量 : ", len(url_links))
for link in url_links:
    count += 1
    print(link)
    if count >= 5:
        break
print("-" * 70)
url_a_links = r.html.absolute_links
count = 0
print("絕對位址超連結數量 : ", len(url_a_links))
for link in url_a_links:
    count += 1
    print(link)
    if count >= 5:
        break

print("------------------------------------------------------------")  # 60個

# ch24_3.py

from requests_html import HTMLSession

session = HTMLSession()  # 定義Session
url = "https://python.org/"
r = session.get(url)  # get()
about = r.html.find("#about", first=True)
print(about.text)

print("------------------------------------------------------------")  # 60個

# ch24_4.py

from requests_html import HTMLSession

session = HTMLSession()  # 定義Session
url = "https://python.org/"
r = session.get(url)  # get()
about = r.html.find("#about", first=True)
print("about.attrs屬性")
print(about.attrs)
print("-" * 70)
print("about.html屬性")
print(about.html)
print("-" * 70)
print("about.absolute_links屬性")
print(about.attrs)
print("-" * 70)
print("about.find('a')")
print(about.find("a"))

print("------------------------------------------------------------")  # 60個

# ch24_5.py

from requests_html import HTMLSession

session = HTMLSession()  # 定義Session
url = "http://python-requests.org/"
r = session.get(url)  # get()
a_element = r.html.find("a", containing="kenneth")
if a_element:
    for a in a_element:
        print(a)

print("------------------------------------------------------------")  # 60個

# ch24_6.py

from requests_html import HTMLSession

session = HTMLSession()  # 定義Session
url = "https://github.com/"
r = session.get(url)  # get()
a_element = r.html.xpath("a")
if a_element:
    for a in a_element:
        print(a)
        print("-" * 70)

print("------------------------------------------------------------")  # 60個

# ch24_7.py

from requests_html import HTMLSession

session = HTMLSession()  # 定義Session
url = "https://python.org/"
r = session.get(url)  # get()
txt = r.html.search("Python is a {} language")[0]
print(txt)

print("------------------------------------------------------------")  # 60個

# ch24_8.py

from requests_html import HTMLSession

session = HTMLSession()
url = "https://movie.douban.com/"
r = session.get(url)

print("影片名稱 : ", r.html.find("li.title", first=True).text)
print("影片評分 : ", r.html.find("li.rating", first=True).text)

print("------------------------------------------------------------")  # 60個

# ch24_9.py

from requests_html import HTMLSession

session = HTMLSession()
url = "https://movie.douban.com/"
r = session.get(url)

movies = r.html.find("li.ui-slide-item")
print("影片數量 : ", len(movies))
print("數據型態 : ", type(movies[0]))
print(movies[0])
print("-" * 70)
print(movies[0].attrs["data-title"])
print(movies[0].attrs["data-rate"])

print("------------------------------------------------------------")  # 60個

# ch24_10.py

from requests_html import HTMLSession

session = HTMLSession()
url = "https://movie.douban.com/"
r = session.get(url)

movies = r.html.find("li.ui-slide-item")
count = 0
for m in movies:
    count += 1
    print("影片編號 : ", count)
    print("影片名稱 : ", m.attrs["data-title"])
    print("影片評分 : ", m.attrs["data-rate"])
    print("-" * 70)
    if count == 20:
        break

print("------------------------------------------------------------")  # 60個

# ch24_11.py

from requests_html import HTMLSession

session = HTMLSession()  # 定義Session
url = "http://python-requests.org/"
r = session.get(url)  # get()
r.html.render()
txt = r.html.search("Python 2 will retire in only {months} months!")["months"]
print(txt)

print("------------------------------------------------------------")  # 60個

# ch25_1.py

url = "https://www.104.com.tw/jobs/search/?ro=0&keyword=Python&jobsource=2018indexpoc"
htmlFile = requests.get(url)
objSoup = bs4.BeautifulSoup(htmlFile.text, "lxml")
jobs = objSoup.find_all("article", class_="js-job-item")
for job in jobs:
    print("公司名稱 : ", job.get("data-cust-name"))
    print("職務名稱 : ", job.get("data-job-name"))

print("------------------------------------------------------------")  # 60個

# ch25_2.py

url = "https://www.104.com.tw/jobs/search/?ro=0&keyword=Python&jobsource=2018indexpoc"
htmlFile = requests.get(url)
objSoup = bs4.BeautifulSoup(htmlFile.text, "lxml")
jobs = objSoup.find_all("article", class_="js-job-item")
job_list = []
for job in jobs:
    cust_name = job.get("data-cust-name")
    print("公司名稱 : ", cust_name)
    job_name = job.get("data-job-name")
    print("職務名稱 : ", job_name)
    d = [("公司名稱", cust_name), ("職務名稱", job_name)]
    j_dict = dict(d)  # 字典
    job_list.append(j_dict)  # 字典是串列元素

myjob = {"Job": job_list}  # 轉成字典

fn = "ch25_2.json"
with open(fn, "w") as fnObj:
    json.dump(myjob, fnObj, indent=2, ensure_ascii=False)

print("------------------------------------------------------------")  # 60個

# ch25_3.py


def job_list(url):
    htmlFile = requests.get(url)
    objSoup = bs4.BeautifulSoup(htmlFile.text, "lxml")
    jobs = objSoup.find_all("article", class_="js-job-item")
    for job in jobs:
        print("公司名稱 : ", job.get("data-cust-name"))
        print("職務名稱 : ", job.get("data-job-name"))


urls = [
    "https://www.104.com.tw/jobs/search/?ro=0&keyword=Python&jobsource=2018indexpoc",
    "https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=Python&order=1&asc=0&page=2&mode=s&jobsource=2018indexpoc",
    "https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=Python&order=1&asc=0&page=3&mode=s&jobsource=2018indexpoc",
]
for url in urls:
    job_list(url)
    print("-" * 70)
    time.sleep(random.randint(3, 5))

print("------------------------------------------------------------")  # 60個

# ch25_3.py


def job_list(url):
    htmlFile = requests.get(url)
    objSoup = bs4.BeautifulSoup(htmlFile.text, "lxml")
    jobs = objSoup.find_all("article", class_="js-job-item")
    for job in jobs:
        print("公司名稱 : ", job.get("data-cust-name"))
        print("職務名稱 : ", job.get("data-job-name"))


url_H = (
    "https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=Python&order=1&asc=0&page="
)
url_T = "&mode=s&jobsource=2018indexpoc"
page_total = 5
for page in range(page_total):
    url = url_H + str(page + 1) + url_T
    job_list(url)
    print("-" * 70)
    time.sleep(random.randint(3, 5))


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
