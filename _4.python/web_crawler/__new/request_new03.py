"""
# requests 一大堆
#網路爬蟲類

"""

import os
import sys
import requests
from bs4 import BeautifulSoup
import urllib.request
import json

print('------------------------------------------------------------')	#60個

print('測試 03')
print('台灣英文新聞網')

news_title = ""
news_content = ""
filename = 'engnews.txt'

url = 'https://www.taiwannews.com.tw/en/news/3610689'
url = 'https://www.taiwannews.com.tw/en/news/4966193'
html = requests.get(url).text
#print(html)
soup = BeautifulSoup(html, "html.parser")  # 解析原始碼
title = soup.find("h1", class_ = "article-title")
article = soup.find("article", class_ = "container-fluid article")
news_title = title.text
news_content = article.text
with open(filename, "w", encoding = "utf-8") as f:
    f.write(news_title + "\n")
    f.write(news_content)

print('標題')
print(news_title)
print('內容')
print(news_content)

print('------------------------------------------------------------')	#60個

print('測試 05')
print('中央通訊社新聞')

news_title = ""
news_content = ""
filename = "cna_news.txt"

#url = 'https://www.cna.com.tw/news/aopl/201901050192.aspx'
url = 'https://www.cna.com.tw/news/ait/202308280292.aspx'   #繼探月成功後 印度又將發射太陽探測器
html = requests.get(url).text
#print(html)
soup = BeautifulSoup(html, "html.parser")  # 解析原始碼
title = soup.find("title")
article = soup.find("div", class_ = "paragraph")
news_title = title.text.strip()
news_content = article.text
with open(filename, "w", encoding = "utf-8") as f:
    f.write(news_title + "\n")
    f.write(news_content)

print('標題')
print(news_title)
print('內容')
print(news_content)

print('------------------------------------------------------------')	#60個

#桃園公共自行車即時服務資料.json
url = 'https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=5ca2bfc7-9ace-4719-88ae-4034b9a5a55c&rid=a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f'

with urllib.request.urlopen(url) as jsonfile:
    data = json.loads(jsonfile.read().decode())
    #print(data)
    """ ok many
    for k in data['retVal'].keys():
        print("{:>2}/{:>2}\t{}".format(data['retVal'][k]['sbi'], data['retVal'][k]['tot'], data['retVal'][k]['sna']))
    """

print('------------------------------------------------------------')	#60個

#桃園公共自行車即時服務資料.json
url = 'https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=5ca2bfc7-9ace-4719-88ae-4034b9a5a55c&rid=a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f'

with urllib.request.urlopen(url) as jsonfile:
    data = json.loads(jsonfile.read().decode())
    msg = "<table>"
    for k in data['retVal'].keys():
        msg += "<tr><td>{:>2}</td><td>{:>2}</td><td>{}</td></tr>".format(
            data['retVal'][k]['sbi'],
            data['retVal'][k]['tot'],
            data['retVal'][k]['sna'])
    msg += "</table>"
    
html = """
<!DOCTYPE html>
<html>
  <head>
    <title>{}</title>
  </head>
  <body>
  {}
  </body>
</html>
""".format("桃園公共自行車各站可租數量", msg)
with open("桃園公共自行車各站可租數量.html", "wt", encoding='utf-8') as fp:
    fp.write(html)
print("Done!")

print('------------------------------------------------------------')	#60個

from dominate import document

html = document("My Title")
print(html)

print('------------------------------------------------------------')	#60個

from dominate import document
from dominate.tags import *

html = document("桃園公共自行車各站可租數量")
with html.head:
    meta(charset='utf-8')
with html.body:
    h1("這是一個示範網頁")
    hr()
    p("這是一個段落")
    p("這是另外一個段落，以下示範的是清單")
    items = ul()
    items += li("第一點")
    items += li("這是第二點")
with open("桃園公共自行車各站可租數量a.html", "wt", encoding='utf-8') as fp:
    fp.write(str(html))
print("Done!")

print('------------------------------------------------------------')	#60個

#以表格的方式呈現公共自行車租借站資訊
import dominate
from dominate.tags import *

#桃園公共自行車即時服務資料.json
url = 'https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=5ca2bfc7-9ace-4719-88ae-4034b9a5a55c&rid=a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f'

with urllib.request.urlopen(url) as jsonfile:
    data = json.loads(jsonfile.read().decode())
html = dominate.document(title="桃園公共自行車各站可租數量")
with html.head:
    meta(charset="utf-8")
with html:
    h1("桃園公共自行車各站可租數量")
    hr()
    with table():     
        head = tr(bgcolor='#888888')
        head += td("站名")
        head += td("可租數量")
        head += td("自行車總量")
        head += td("本站位置")
        for index, k in enumerate(data['retVal'].keys()):
            if index % 2 == 0:
                row = tr(bgcolor='#ccffcc')
            else:
                row = tr(bgcolor='#ffccff')
            row += td(data['retVal'][k]['sna'])
            row += td(data['retVal'][k]['sbi'])
            row += td(data['retVal'][k]['tot'])
            row += td(data['retVal'][k]['ar'])
with open("桃園公共自行車各站可租數量_list.html", "wt", encoding='utf-8') as fp:
    fp.write(str(html))
print("Done!")

print('------------------------------------------------------------')	#60個

import dominate
from dominate.tags import *
from dominate.util import raw

#桃園公共自行車即時服務資料.json
url = 'https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=5ca2bfc7-9ace-4719-88ae-4034b9a5a55c&rid=a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f'

with urllib.request.urlopen(url) as jsonfile:
    data = json.loads(jsonfile.read().decode())
html = dominate.document(title="桃園公共自行車各站可租數量")
with html.head:
    meta(charset="utf-8")
    script(src="http://code.jquery.com/jquery-3.3.1.slim.js", 
           integrity="sha256-fNXJFIlca05BIO2Y5zh1xrShK3ME+/lYZ0j+ChxX2DA=",
           crossorigin="anonymous")
    cmd = """
$(document).ready(function() {
    $("#bike-station").change(function() {
        $('#target').html($("select option:selected").val())
    });
});
"""
    script(raw(cmd))
with html:
    h1("桃園公共自行車各站可租數量查詢")
    hr()
    p("請選擇自行車租借站：")
    with form(method="POST"):
        with select(id='bike-station'):
            for k in data['retVal'].keys():
                option(value="{}/{}".format(
                    data['retVal'][k]['sbi'],
                    data['retVal'][k]['tot'])).add(
                    data['retVal'][k]['sna'])
    d = div()
    d += h3("可租借數量/總數：")
    d += span(id="target")
with open("桃園公共自行車各站可租數量查詢.html", "wt", encoding='utf-8') as fp:
    fp.write(str(html))
print("Done!")

print('------------------------------------------------------------')	#60個

print('解析網址')
from urllib.parse import urlparse

u = urlparse("https://tw.stock.yahoo.com/news_list/url/d/e/N1.html?q=&pg=4")
print(u.netloc)
print(u.path)
print(u.query)

print('------------------------------------------------------------')	#60個

print('拼湊網址')
url = "https://tw.stock.yahoo.com/news_list/url/d/e/N1.html?q=&pg={}"
for i in range(1,6):
    print(url.format(i))

print('------------------------------------------------------------')	#60個

print('拼湊網址')
url = "https://tw.stock.yahoo.com/news_list/url/d/e/N{}.html?q=&pg={}"
for t in [1, 997, 4]:
    for i in range(1,6):
        print(url.format(t, i))

print('------------------------------------------------------------')	#60個

print('抓取網頁')
url = 'https://tw.stock.yahoo.com/tw-market'
html = requests.get(url).text
print(html)

print('------------------------------------------------------------')	#60個

print('抓取網頁, re分析')
import re
url = 'https://tw.stock.yahoo.com/tw-market'
html = requests.get(url).text
print(re.sub(r"<script.*>.*</script>", "", html))

print('------------------------------------------------------------')	#60個

print('抓取網頁')
#博客來-中文書>暢銷榜
url = "https://www.books.com.tw/web/sys_saletopb/books/19/?loc=P_0002_020"
html = requests.get(url).text
print(type(html))
print("Python這個字在排行榜中裡面出現了{}次".format(
    html.count("Python")+html.count("python")))

print('------------------------------------------------------------')	#60個

print('抓取網頁')

#博客來-中文書>暢銷榜
url = "https://www.books.com.tw/web/sys_saletopb/books/19/?loc=P_0002_020"
html = requests.get(url).text
keyword = input("請問你要查詢的字串(end to quit)：")
while keyword != 'end':
    print("{}這個字在排行榜中裡面出現了{}次".format(
        keyword, html.count(keyword)))
    keyword = input("請問你要查詢的字串：")

print('------------------------------------------------------------')	#60個

print('抓取網頁 bs分析 1')
url = "http://aiworker2000.pixnet.net/blog/post/16062839"
html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")
print(type(soup))
print(dir(soup))

print('------------------------------------------------------------')	#60個

print('抓取網頁 bs分析 2')
url = "http://aiworker2000.pixnet.net/blog/post/16062839"
html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")
images = soup.find_all("img")
for image in images:
    print(image["src"])

print('------------------------------------------------------------')	#60個

print('抓取網頁 bs分析 3')

import os
from os.path import basename

url = "http://aiworker2000.pixnet.net/blog/post/16062839"
html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")
images = soup.find_all("img")
if not os.path.exists("download_files"):
    os.mkdir("download_files")
for image in images:
    image_url = image["src"]
    if ".jpg" in image_url:
        image_filename = basename(image_url)
        with open(os.path.join("download_files", image_filename), "wb") as fp:
            image_data = urllib.request.urlopen(image_url).read()
            fp.write(image_data)
        print(image_url)
        print(image_filename)

print('------------------------------------------------------------')	#60個

""" ok, many
print('抓取網頁 bs分析 4')
#博客來-中文書>暢銷榜
url = "https://www.books.com.tw/web/sys_saletopb/books/19/?loc=P_0002_020"
html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")
images = soup.find_all("img")
for image in images:
    if ".jpg" in image['src'] or ".png" in image['src']:
        print(image['src'])
"""
print('------------------------------------------------------------')	#60個

""" ok, many
print('抓取網頁 bs分析 5')
#博客來-中文書>暢銷榜
url = "https://www.books.com.tw/web/sys_saletopb/books/19/?loc=P_0002_020"
html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")
links = soup.find_all("a")
for link in links:
    if "http" in link['href']:
        print(link['href'])
"""        
print('------------------------------------------------------------')	#60個

""" ok, many
print('抓取網頁 bs分析 6')
#博客來-中文書>暢銷榜
url = "https://www.books.com.tw/web/sys_saletopb/books/19/?loc=P_0002_020"
html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")
titles = soup.find_all("img", {"class":"cover"})
for i, title in enumerate(titles):
    print("第{}名：{}".format(i+1, title['alt']))
"""
print('------------------------------------------------------------')	#60個

""" fail in sugar
print('抓取網頁 bs分析 7 fail')
#博客來-中文書>暢銷榜
url = "https://www.books.com.tw/web/sys_saletopb/books/19/?loc=P_0002_020"
html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")
books = soup.find_all("li", {"class":"item"})
for i, book in enumerate(books):
    print("第{}名：".format(i+1), end="")
    print(book.find("img")['alt'])
    for info in book.find("ul").find_all("li"):
        print(info.text)
    print()
"""
print('------------------------------------------------------------')	#60個

""" fail

print('抓取網頁 bs分析 8')

#教育部全球資訊網-即時新聞
url = "https://www.edu.tw/News.aspx?n=9E7AC85F1954DDA8&sms=169B8E91BB75571F"
html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")
table = soup.find("table")
for row in soup.find_all("tr"):
    cells = row.find_all("td")
    for cell in cells:
        a = cell.find("a")
        if a is not None:
            print(a.text)
"""
print('------------------------------------------------------------')	#60個

print('抓取網頁 bs分析 9')

#教育部全球資訊網-即時新聞
url = "https://www.edu.tw/News.aspx?n=9E7AC85F1954DDA8&sms=169B8E91BB75571F"
html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")
table = soup.find("table")
headlines = list()
for row in soup.find_all("tr"):
    cells = row.find_all("td")
    for cell in cells:
        a = cell.find("a")
        if a is not None and a.text != "下一頁":
            headlines.append(a.text)
news = "\n".join(headlines)
with open("教育部全球資訊網即時新聞.txt", "wt", encoding="utf-8") as fp:
    fp.write(news)
print("Done!")

print('------------------------------------------------------------')	#60個

print('抓取網頁 bs分析 10')

import dominate
from dominate.tags import *
from dominate.util import raw
import os
from os.path import basename

url = "http://aiworker2000.pixnet.net/blog/post/16062839"
index_html = dominate.document(title="圖形檔案索引")
with index_html.head:
    meta(charset="utf-8")
with index_html:
    h1("圖形檔案索引")
    hr()
    html = requests.get(url).text
    soup = BeautifulSoup(html, "lxml")
    images = soup.find_all("img")
    if not os.path.exists("download_files"):
        os.mkdir("download_files")
    for image in images:
        image_url = image["src"]
        if ".jpg" in image_url:
            image_filename = basename(image_url)
            image_link = a(href=image_filename)
            image_link += img(src=image_filename, width=200)
            with open(os.path.join("download_files", image_filename), "wb") as fp:
                image_data = urllib.request.urlopen(image_url).read()
                fp.write(image_data)
with open(os.path.join("download_files", "index.html"), "wt", encoding='utf-8') as fp:
    fp.write(str(index_html))
    
print("Done!")

print('------------------------------------------------------------')	#60個

"""
print('抓取網頁 bs分析 11')
url = "https://tw.appledaily.com/new/realtime/"
html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")
headlines = soup.find("ul", {"class": "rtddd slvl"})
items = headlines.find_all("li")
for item in items:
    print(item.find("h1").text)
    print(item.find("a")["href"])
    print()

print('------------------------------------------------------------')	#60個

print('抓取網頁 bs分析 12')

import time, random

url = "https://tw.appledaily.com/new/realtime/"
html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")
headlines = soup.find("ul", {"class": "rtddd slvl"})
items = headlines.find_all("li")
for item in items:
    time.sleep(random.randint(0,2))
    content_url = item.find("a")["href"]
    print(content_url)
    content = requests.get(content_url).text
    content_soup = BeautifulSoup(content, "lxml")
    title = content_soup.find("h1")
    print(title.text)
    article = content_soup.find("article", {"class":"ndArticle_content clearmen"})
    print(article.find("p").text)

print('------------------------------------------------------------')	#60個

"""

print('抓取網頁 bs分析 13')

url = 'https://www.ptt.cc/bbs/gossiping/index.html'

html = requests.get(url=url, cookies={'over18': '1'}).text
soup = BeautifulSoup(html, "lxml")
titles = soup.find_all('div', class_='title')
for title in titles:
    print(title.a.text)

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

import requests

url = "https://ck101.com/forum-3590-1.html?ref=nav"

res = requests.get(url)

print(res)
print(res.text)


print('------------------------------------------------------------')	#60個


import time
import requests
from bs4 import BeautifulSoup

url = "https://www.mobile01.com/topiclist.php?f=751"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
}

html_data = requests.get(url, headers=headers)

soup = BeautifulSoup(html_data.text, "html.parser")
pages = soup.find_all("a", class_="c-pagination")
last_page = int(pages[-1].text)
url_pattern = "https://www.mobile01.com/topiclist.php?f=751&p={}"
for page in range(1, last_page+1):
    current_url = url_pattern.format(page)
    html_data = requests.get(current_url, headers=headers)
    soup = BeautifulSoup(html_data.text, "html.parser")
    titles = soup.find_all("div", class_="c-listTableTd__title")
    for title in titles:
        print(title.a.text)
        print(title.a['href'])
    time.sleep(3)    


print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個

import requests
from bs4 import BeautifulSoup

url = 'https://www.mobile01.com/topiclist.php?f=751'
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
}
html_data = requests.get(url, headers=headers)

soup = BeautifulSoup(html_data.text, "html.parser")
print(soup.prettify())  #prettify()這個函數可以將DOM tree以比較美觀的方式印出。

pages = soup.find_all("a", class_="c-pagination")

print("本討論區的最後一頁是：", end="")
print(pages[-1].text)

print('------------------------------------------------------------')	#60個


import requests

url = "https://www.lexuscpo.com.tw/Home/CarStock"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
}

form_data = {
    "CarType":"", 
    "Series": "IS",
    "Price": "", 
    "Year": "", 
    "Mileage":"", 
    "StoreID":"", 
    "Page": "",
    "Limit": "20"
}

data = requests.post(url, data=form_data, headers=headers).text
print(data)


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



print('------------------------------------------------------------')	#60個


import json
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
    "Limit": "500"
}

data = requests.post(url, data=form_data, headers=headers).text
cars = json.loads(data)
cars = cars['rows']
message = "{:<10}({}年式)，{:>10,}KM，{:>10,}元"
for car in cars:
    print(message.format(
        car['Model'], 
        car['Year'],
        car['Mileage'],
        car['SellPrice']))



print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個

import json, time, os, requests
import urllib.request

api_url = "https://www.dcard.tw/_api/forums/funny/posts?limit=100"
res = requests.get(api_url).text

data = json.loads(res)
for post in data:
    if len(post["media"])>0:
        for image in post["media"]:
            imgurl = image["url"]
            print(imgurl)
            if ".jpg" in imgurl or ".png" in imgurl:
                urllib.request.urlretrieve(imgurl, os.path.join("mypics", os.path.basename(imgurl)))
            time.sleep(3)



import requests

url = "https://www.mobile01.com/topiclist.php?f=751"

print('無參數抓網頁')

res = requests.get(url)

print(res)


print('有參數抓網頁')

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
}
res = requests.get(url, headers=headers)
print(res)

print('------------------------------------------------------------')	#60個

import requests

# 郵遞區號
zipcode = "1000001"

# API 端點
api_endpoint = f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}"

# https://zipcloud.ibsnet.co.jp/api/search?zipcode=1000001

# 進行查詢
response = requests.get(api_endpoint)

# 檢查回應狀態
if response.status_code == 200:
    # 解析回應內容
    data = response.json()

    # 驗證 API 回應狀態
    if data['status'] == 200:
        print('印出完整資訊')
        print(type(data))
        print(data)
        
        # 取出第一筆地址資訊
        address_info = data['results'][0]

        # 印出完整郵遞區域
        print(f"{address_info['address1']} {address_info['address2']} {address_info['address3']}")
        
    else:
        print("API 回應錯誤，訊息：", data['message'])
else:
    print("API 查詢失敗，狀態碼：", response.status_code)


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

print('作業完成')

