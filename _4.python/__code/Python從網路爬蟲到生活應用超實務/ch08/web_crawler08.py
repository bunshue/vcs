import requests 
from bs4 import BeautifulSoup

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



#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch08\ch8-1-2.py

import requests 
from bs4 import BeautifulSoup
import csv

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

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch08\ch8-1-3.py

from bs4 import BeautifulSoup
import requests

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

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch08\ch8-1-4.py

import requests
from bs4 import BeautifulSoup
import csv
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

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch08\ch8-2-2.py

import re
import json
import requests
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

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch08\ch8-2-2a.py

import re
import json
import requests
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

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch08\ch8-3-1.py

from pytrends.request import TrendReq

pytrend = TrendReq(hl="zh-TW", tz=-480)
keywords = ["Python", "Java", "C++"]
pytrend.build_payload(
     kw_list=keywords,
     cat=0,
     timeframe="2020-07-01 2020-07-31",
     geo="TW",
     gprop="")

print(pytrend.interest_over_time())


print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch08\ch8-3-2.py

from pytrends.request import TrendReq

pytrend = TrendReq()
df = pytrend.trending_searches(pn='taiwan')
print(df.head(10))

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch08\ch8-3-2a.py

from pytrends.request import TrendReq

pytrend = TrendReq()
df = pytrend.top_charts(2019, hl="zh-tw", tz=-480, geo="TW")
print(df)

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch08\ch8-3-2b.py

import pandas as pd
from pytrends.request import TrendReq

pytrend = TrendReq()
dic = pytrend.suggestions(keyword="python")
print(pd.DataFrame(dic).drop("mid", axis=1))

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch08\ch8-3-2c.py

from pytrends.request import TrendReq

pytrend = TrendReq(hl="zh-TW", tz=-480)
pytrend.build_payload(kw_list=["Python"])

df = pytrend.interest_by_region()
print(df.sort_values(["Python"], ascending=False).head(10))

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch08\ch8-3-2d.py

from pytrends.request import TrendReq

pytrend = TrendReq(hl="zh-TW", tz=-480)
pytrend.build_payload(kw_list=["Python"])

dic = pytrend.related_queries()
print(dic["Python"]["top"].head(10))
print(dic["Python"]["rising"].head(10))

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch08\ch8-3-2e.py

from pytrends.request import TrendReq

pytrend = TrendReq(hl="zh-TW", tz=-480)
pytrend.build_payload(kw_list=["Python"])

dic = pytrend.related_topics()
df = dic["Python"]["rising"]
df = df.drop(["link","topic_mid"], axis=1)
print(df.head(10))

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch08\ch8-4.py

from pytrends.request import TrendReq

pytrend = TrendReq(hl="zh-TW", tz=-480)
pytrend.build_payload(
     kw_list=["Python", "R"],
     timeframe="today 3-m",
     geo="TW")

df = pytrend.interest_over_time()
df = df.drop(["isPartial"], axis=1)
df.plot(kind="line", title="Python vs R")


print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch08\ch8-4a.py

from pytrends.request import TrendReq

pytrend = TrendReq(hl="zh-TW", tz=-480)
pytrend.build_payload(kw_list=["Python"])

df = pytrend.interest_by_region()
df = df.sort_values(["Python"], ascending=False).head(10)
df.plot(kind="bar")

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch08\ch8-4b.py

import pandas as pd
from pytrends.request import TrendReq

pytrend = TrendReq(hl="en-US", tz=360)
pytrend.build_payload(
     kw_list=["Coronavirus"],
     timeframe="2020-02-01 2020-03-31",
     geo="US-NY")

df = pytrend.interest_over_time()
df = df.drop(["isPartial"], axis=1)
df["timestamp"] = pd.to_datetime(df.index)
print(df.head())
df.plot(kind="line", x="timestamp", y="Coronavirus", 
        title="Searches for Coronavirus in NY")


print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch08\ch8-4c.py

import pandas as pd
from pytrends.request import TrendReq

pytrend = TrendReq(hl="en-US", tz=360)

def get_trends(keywords, state): 
    pytrend.build_payload(
         kw_list=keywords,
         timeframe="2020-02-01 2020-03-31",
         geo=state)
    df = pytrend.interest_over_time()
    df = df.drop(["isPartial"], axis=1)
    df.columns = [state]
    return df
    

df = get_trends(["Coronavirus"], "US-NY")
df2 = get_trends(["Coronavirus"], "US-CA")
 
df3 = pd.concat([df, df2], axis=1)
print(df3.head())

df3["timestamp"] = pd.to_datetime(df.index)
print(df3.head())
df3.plot(kind="line", x="timestamp", y=["US-NY","US-CA"], 
        title="Searches for Coronavirus in NY/CA")

print('------------------------------------------------------------')	#60個

