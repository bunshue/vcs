# Python 測試 BeautifulSoup

from bs4 import BeautifulSoup

'''
print('BeautifulSoup 測試 1')
soup = BeautifulSoup("<html> Lollipop </html>", "html.parser")
print("取得網頁標題")
print(soup.title)
print("取得網頁內容")
print(soup.text)

print('BeautifulSoup 測試 2')
import requests
from bs4 import BeautifulSoup

url = 'http://tw.yahoo.com'
html_data = requests.get(url)
soup = BeautifulSoup(html_data.text, "html.parser")
soup.title

print("取得網頁標題")
print(soup.title)


print('BeautifulSoup 測試 3')
import requests
from bs4 import BeautifulSoup

url = 'https://tw.news.yahoo.com/rss/technology'
html_data = requests.get(url)
soup = BeautifulSoup(html_data.text, "html.parser")
type(soup)
soup.findAll('item')

print("取得Yahoo奇摩新聞-科技新聞-標題")
for news in soup.findAll('item'):
	print(news.title)

print('BeautifulSoup 測試 5')
from bs4 import BeautifulSoup
import requests
import sys

url = 'https://www.google.com.tw/'
html_data = requests.get(url).text
soup = BeautifulSoup(html_data, 'html.parser')
all_links = soup.find_all('a')

for link in all_links:
    href = link.get('href')
    if href != None and href.startswith('http://'):
        print('取得資料')
        print(href)


print('BeautifulSoup 測試 6')
import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/NBA/index.html" # PTT NBA 板
html_data = requests.get(url) # 用 requests 的 get 方法把網頁抓下來
html_doc = html_data.text # text 屬性就是 html 檔案
soup = BeautifulSoup(html_data.text, "lxml") # 指定 lxml 作為解析器
#print(soup.prettify()) # 把排版後的 html 印出來

# 一些屬性或方法
print(soup.title) # 把 tag 抓出來
print("---")
print(soup.title.name) # 把 title 的 tag 名稱抓出來
print("---")
print(soup.title.string) # 把 title tag 的內容欻出來
print("---")
print(soup.title.parent.name) # title tag 的上一層 tag
print("---")
print(soup.a) # 把第一個 <a></a> 抓出來
print("---")
print(soup.find_all('a')) # 把所有的 <a></a> 抓出來


'''

'''
print('BeautifulSoup 測試 8')
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import sys

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        soup = BeautifulSoup(html, "html.parser")
        title = soup.body.h1
    except AttributeError as e:
        return None
    return title

url = 'http://www.pythonscraping.com/exercises/exercise1.html'
title = getTitle(url)
if title == None:
    print("找不到網頁標題")
else:
    print("取得網頁標題:")
    print(title)
'''

print('BeautifulSoup 測試 7')

import requests
import time
import csv
import random
import socket
import http.client
import bs4
from bs4 import BeautifulSoup

def get_content(url,data = None):
    header = {
        'Accept':'image/webp,image/apng,image/*,*/*;q=0.8',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
    timeout = random.choice(range(80,180))
    while True:
        try:
            html_data = requests.get(url,headers =header,timeout = timeout)
            html_data.encoding= 'utf-8'
            break
        except socket.timeout as e:
            print('3:', e)
            time.sleep(random.choice(range(8, 15)))

        except socket.error as e:
            print('4:', e)
            time.sleep(random.choice(range(20, 60)))

        except http.client.BadStatusLine as e:
            print('5:', e)
            time.sleep(random.choice(range(30, 80)))

        except http.client.IncompleteRead as e:
            print('6:', e)
            time.sleep(random.choice(range(5, 15)))
    return html_data.text

def get_data(html_text):
    final=[]
    soup = BeautifulSoup(html_text, "html.parser")  # 創建soup對象
    body = soup.body

    divs = soup.find_all('div', 'crumbs fl')
    print(divs)
    for div in divs:
        print('111')
        print(div)
        for di in div:
            print('222')
            print(di.text.replace('\n', ''))

    data = body.find('div',attrs={'id':'7d'})
    # data = body.find('div',{'div':'7d'})
    print(type(data))
    ul = data.find('ul')
    li =ul.find_all('li')
    for day in li:
        temp = []
        date = day.find('h1').string
        temp.append(date)
        inf = day.find_all('p')
        temp.append(inf[0].string)
        if inf[1].find('span') is None:
            temperature_highest = None
        else:
            temperature_highest=inf[1].find('span').string
            temperature_highestm  =temperature_highest.replace("℃","")
        temperature_lowest = inf[1].find('i').string
        temperature_lowest = temperature_lowest.replace('℃','')
        temp.append(temperature_highest)
        temp.append(temperature_lowest)
        final.append(temp)
    return final

def write_data(data, name):
    file_name =name
    with open(file_name, 'a', errors = 'ignore', newline = '') as f:
        f_csv = csv.writer(f)
        f_csv.writerows(data)


print('取得氣象資料')
url = 'http://www.weather.com.cn/weather/101190401.shtml'   #蘇州
url = 'http://www.weather.com.cn/weather/101340101.shtml'  #台北
html_data = get_content(url)
#print(html_data)
result = get_data(html_data)
write_data(result,'weather.csv')




