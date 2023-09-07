'''
# 

'''

import requests

print('------------------------------------------------------------')	#60個

from urllib.parse import urlparse
u = urlparse("https://tw.stock.yahoo.com/news_list/url/d/e/N1.html?q=&pg=4")
print(u.netloc)
print(u.path)
print(u.query)

print('------------------------------------------------------------')	#60個

url = "https://tw.stock.yahoo.com/news_list/url/d/e/N1.html?q=&pg={}"
for i in range(1,6):
    print(url.format(i))

print('------------------------------------------------------------')	#60個

url = "https://tw.stock.yahoo.com/news_list/url/d/e/N{}.html?q=&pg={}"
for t in [1, 997, 4]:
    for i in range(1,6):
        print(url.format(t, i))


print('------------------------------------------------------------')	#60個

import requests
url = "https://tw.stock.yahoo.com/news_list/url/d/e/N4.html"
html = requests.get(url).text
print(html)

print('------------------------------------------------------------')	#60個

import requests
import re
url = "https://tw.stock.yahoo.com/news_list/url/d/e/N4.html"
html = requests.get(url).text
print(re.sub(r"<script.*>.*</script>", "", html))

print('------------------------------------------------------------')	#60個

import requests
url = "https://www.books.com.tw/web/sys_saletopb/books/19/?loc=P_0002_020"
html = requests.get(url).text
print(type(html))
print("Python這個字在排行榜中裡面出現了{}次".format(
    html.count("Python")+html.count("python")))


print('------------------------------------------------------------')	#60個

import requests
url = "https://www.books.com.tw/web/sys_saletopb/books/19/?loc=P_0002_020"
html = requests.get(url).text
keyword = input("請問你要查詢的字串(end to quit)：")
while keyword != 'end':
    print("{}這個字在排行榜中裡面出現了{}次".format(
        keyword, html.count(keyword)))
    keyword = input("請問你要查詢的字串：")

print('------------------------------------------------------------')	#60個

import requests
from bs4 import BeautifulSoup
url = "http://aiworker2000.pixnet.net/blog/post/16062839"
html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")
print(type(soup))
print(dir(soup))

print('------------------------------------------------------------')	#60個

import requests
from bs4 import BeautifulSoup
url = "http://aiworker2000.pixnet.net/blog/post/16062839"
html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")
images = soup.find_all("img")
for image in images:
    print(image["src"])

print('------------------------------------------------------------')	#60個

import requests
import os
from os.path import basename
from bs4 import BeautifulSoup
import urllib.request
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

import requests
from bs4 import BeautifulSoup
url = "https://www.books.com.tw/web/sys_saletopb/books/19/?loc=P_0002_020"
html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")
images = soup.find_all("img")
for image in images:
    if ".jpg" in image['src'] or ".png" in image['src']:
        print(image['src'])

print('------------------------------------------------------------')	#60個

import requests
from bs4 import BeautifulSoup
url = "https://www.books.com.tw/web/sys_saletopb/books/19/?loc=P_0002_020"
html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")
links = soup.find_all("a")
for link in links:
    if "http" in link['href']:
        print(link['href'])
print('------------------------------------------------------------')	#60個

import requests
from bs4 import BeautifulSoup
url = "https://www.books.com.tw/web/sys_saletopb/books/19/?loc=P_0002_020"
html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")
titles = soup.find_all("img", {"class":"cover"})
for i, title in enumerate(titles):
    print("第{}名：{}".format(i+1, title['alt']))

print('------------------------------------------------------------')	#60個

import requests
from bs4 import BeautifulSoup
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

print('------------------------------------------------------------')	#60個

import requests
from bs4 import BeautifulSoup
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

print('------------------------------------------------------------')	#60個

import requests
from bs4 import BeautifulSoup
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
with open("eduheadlines.txt", "wt", encoding="utf-8") as fp:
    fp.write(news)
print("Done!")

print('------------------------------------------------------------')	#60個

import dominate
from dominate.tags import *
from dominate.util import raw
import urllib.request, json
import requests
import os
from os.path import basename
from bs4 import BeautifulSoup
import urllib.request
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

from bs4 import BeautifulSoup
import requests
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
from bs4 import BeautifulSoup
import time, random
import requests
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
