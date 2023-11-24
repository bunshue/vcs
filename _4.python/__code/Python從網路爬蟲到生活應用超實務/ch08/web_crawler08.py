import sys

print('------------------------------------------------------------')	#60個

import csv
import requests
from bs4 import BeautifulSoup

print('------------------------------------------------------------')	#60個

url = "http://app2.atmovies.com.tw/boxoffice/"
r = requests.get(url)
r.encoding = "utf8"
soup = BeautifulSoup(r.text, "lxml")
tag_table = soup.find("table")
rows = tag_table.find_all("tr") 
items = []
for row in rows:
    item = []
    for cell in row.find_all("td"):
        item.append(cell.text.replace("\n","").replace("\r","").strip())
    if item and item[0] != "more":
        items.append(item) 

print(items)

print('------------------------------------------------------------')	#60個

url = "https://movies.yahoo.com.tw/chart.html"
csvfile = "yahoomovies.csv"
r = requests.get(url)
r.encoding = "utf8"
soup = BeautifulSoup(r.text, "lxml")
tag_table = soup.find("div", class_="rank_list") 
rows = soup.find_all('div', class_='tr')
colname = list(rows.pop(0).stripped_strings)
items = []
for row in rows:
    tds = row.find_all("div", class_="td")
    item = []
    item.append(tds[0].text)
    item.append(tds[2].text)
    title = tds[3].text.strip()
    if "\n" in title:
        x = title.split("\n")
        title = x[0]
    item.append(title)
    item.append(tds[4].text.strip())
    item.append(tds[5].text.strip())
    item.append(tds[6].text.strip())
    items.append(item)

with open(csvfile, 'w+', newline='') as fp:
    writer = csv.writer(fp)
    writer.writerow(colname)
    for item in items:
        writer.writerow(item)

print('------------------------------------------------------------')	#60個

url = "https://ifoodie.tw/explore/台北市/list?sortby=rating"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
item_lst = soup.find("div", class_="item-list")
items = item_lst.find_all("div", class_="restaurant-item")
print(len(items))
for index in range(5):
    item = items[index]
    title = item.find("a", class_="title-text")
    if title: print(title.text)
    address = item.find("div", class_="address-row")
    if address: print(address.text)
    avg_price = item.find("div", class_="avg-price")
    if avg_price: print(avg_price.text[2:])
    message = item.find("div", class_="message-text")
    if message: print(message.text)
    print("-------------------")


print('------------------------------------------------------------')	#60個

from fake_useragent import UserAgent

csvfile = "books.csv"
url = "http://www.books.com.tw/web/sys_hourstop/home?loc=P_003_001"
ua = UserAgent()
headers = {'user-agent' : ua.random}
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'lxml')
tag_ul = soup.find("ul", class_="clearfix")
rows = tag_ul.find_all("li", class_="item")
print(len(rows))
items = []
for row in rows:
    item = []
    top = row.find("strong", class_="no")
    item.append(top.text.strip())
    title = row.find("h4")
    item.append(title.text.strip())
    item.append(title.find("a").get("href"))
    img = row.find("img", class_="cover")
    item.append(img.get("src"))
    price = row.find("ul", class_="msg").find("li",class_="price_a")
    item.append(price.text.strip())
    items.append(item)

with open(csvfile, 'w+', newline='') as fp:
    writer = csv.writer(fp)
    writer.writerow(["排名","名稱","網址","圖片","價格"])
    for item in items:
        writer.writerow(item)

print('------------------------------------------------------------')	#60個

import re
import json
import pandas as pd

date = "20200813"
URL = "https://trends.google.com.tw/trends/api/dailytrends?hl=zh-TW&tz=-480&ed={}&geo=TW&ns=15"
url = URL.format(date)
r = requests.get(url)
json_str = re.sub("\)\]\}\',\n", "", r.text)
data = json.loads(json_str)
results = data["default"]["trendingSearchesDays"][0]["trendingSearches"]
items = []
for item in results:
    items.append(item["title"])
df = pd.DataFrame(items)

print(df.head())


print('------------------------------------------------------------')	#60個

import re
import json
import pandas as pd
import datetime
from fake_useragent import UserAgent

URL = "https://trends.google.com.tw/trends/api/dailytrends?hl=zh-TW&tz=-480&ed={}&geo=TW&ns=15"

ua = UserAgent()
enddate = datetime.datetime.today()
startdate = enddate - datetime.timedelta(days=29)
all_items = []
start = datetime.datetime.strftime(startdate,'%Y%m%d')
end = datetime.datetime.strftime(enddate,'%Y%m%d')
for i in pd.date_range(start=start, end=end, freq='1D'):
    url = URL.format(datetime.datetime.strftime(i, '%Y%m%d'))
    print(url)
    headers = {'user-agent' : ua.random}
    r = requests.get(url, headers=headers)
    json_str = re.sub("\)\]\}\',\n", "", r.text)
    data = json.loads(json_str)
    results = data["default"]["trendingSearchesDays"][0]["trendingSearches"]
    items = []
    rank = 1
    for item in results:
        dic = item["title"]
        dic["rank"] = rank        
        items.append(dic)
        rank = rank + 1
    df = pd.DataFrame(items)
    df['date'] = datetime.datetime.strftime(i, '%Y-%m-%d')
    print(df.head())
    all_items.append(df)
   
df = pd.concat(all_items, ignore_index=True)
df.to_csv("trends.csv",index=False)

print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個
