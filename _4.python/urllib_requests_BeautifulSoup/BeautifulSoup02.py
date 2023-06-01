# Python 測試 BeautifulSoup

print('----------------------------------------------------------------------')	#70個
print('準備工作')

import os
import sys
import time
import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_html_data1(url):
    print('取得網頁資料: ', url)
    resp = requests.get(url)
    # 檢查 HTTP 回應碼是否為 requests.codes.ok(200)
    if resp.status_code != requests.codes.ok:
        print('讀取網頁資料錯誤, url: ', resp.url)
        return None
    else:
        return resp

def get_soup_from_url(url):
    html_data = get_html_data1(url)
    if html_data == None:
        print('無法取得網頁資料')
        sys.exit(1)	#立刻退出程式

    soup = BeautifulSoup(html_data.text, "html.parser")  # 解析原始碼
    #print(soup.prettify())  #prettify()這個函數可以將DOM tree以比較美觀的方式印出。
    print("取得網頁標題", soup.title)
    return soup
    
print('----------------------------------------------------------------------')	#70個
print('BeautifulSoup 測試 1')

url = 'http://tw.yahoo.com'
soup = get_soup_from_url(url)

url = 'https://tw.news.yahoo.com/rss/technology'
soup = get_soup_from_url(url)

type(soup)
soup.findAll('item')

print("取得Yahoo奇摩新聞-科技新聞-標題")
for news in soup.findAll('item'):
    print(news.title)

print('----------------------------------------------------------------------')	#70個
print('BeautifulSoup 測試 2')

url = 'https://www.google.com.tw/'
soup = get_soup_from_url(url)

all_links = soup.find_all('a')

for link in all_links:
        href = link.get('href')
        if href != None and href.startswith('http://'):
                print('取得資料')
                print(href)

print('----------------------------------------------------------------------')	#70個
print('BeautifulSoup 測試 3')

url = 'http://ehappy.tw/bsdemo1.htm'

html_data = get_html_data1(url)
if html_data == None:
    print('無法取得網頁資料')
    sys.exit(1)	#立刻退出程式

html_data.encoding = 'UTF-8'
soup = BeautifulSoup(html_data.text, 'html.parser')

print("取得網頁標題", soup.title)
print("取得網頁標題", soup.title.text)
print("取得 h1: ", soup.h1)
print("取得 p: ", soup.p)

print('----------------------------------------------------------------------')	#70個
print('BeautifulSoup 測試 4')

url = 'https://oldsiao.neocities.org/'
soup = get_soup_from_url(url)

print("取得網頁標題", soup.title)
print("取得網頁標題", soup.title.text)

#尋找指定標籤find()、find_all()

print("尋找標籤「<div>」")
print(soup.find("div"))

print("尋找標籤「<title>」")
print(soup.find_all("title"))

print('----------------------------------------------------------------------')	#70個
print('BeautifulSoup 測試 5')

#PTT C_Chat板每篇文章的標題

url = 'https://www.ptt.cc/bbs/C_Chat/index.html'
soup = get_soup_from_url(url)

# 發現所有的文章標題都在class="title"的div中
links = soup.find_all("div", class_="title")    # 文章標題
for link in links:
    print(link.text.strip()) # strip()用來刪除文字前面和後面多餘的空白

print('----------------------------------------------------------------------')	#70個
print('BeautifulSoup 測試 6')

url = 'http://blog.castman.net/web-crawler-tutorial/ch1/connect.html'
soup = get_soup_from_url(url)

try:
    h1 = soup.find('h1')
except:
    h1 = None
if h1:
    print(soup.find('h1'))
    print(soup.find('h1').text)
try:
    h2 = soup.find('h2')
except:
    h2 = None
if h2:
    print(soup.find('h2').text)
else:
    print('h2 tag not found!')

print('----------------------------------------------------------------------')	#70個
print('BeautifulSoup 測試 7')

url = 'https://www.nkust.edu.tw/'
soup = get_soup_from_url(url)

print()
print('找第一個標籤p')
target = soup.p
print(target)
print()

print('找第一個標籤p')
target = soup.p
print(target)
print()

print('----------------------------------------------------------------------')	#70個
print('BeautifulSoup 測試 8')

#聯合新聞網
url = 'https://udn.com/news/breaknews/1'
soup = get_soup_from_url(url)

target = soup.find_all("h2", {"class":"breaking-news"})
#print(target)

for news in target:
    print(news.a['title'])

print('----------------------------------------------------------------------')	#70個
print('BeautifulSoup 測試 9')

url = 'https://newcar.u-car.com.tw/newcar'
soup = get_soup_from_url(url)

makes = soup.select('#makeselect > option')
makers = dict()
for make in makes:
    if make['value'] != '0':
        makers[int(make['value'])] = make.text
print(makers)

print('----------------------------------------------------------------------')	#70個
print('BeautifulSoup 測試 10')

url = 'https://newcar.u-car.com.tw/newcar'
soup = get_soup_from_url(url)

models = soup.select('#modelselect > option')
cars = list()
for model in models:
    if model['value'] != '0':
        car = dict()
        car['id'] = int(model['value'])
        car['make'] = int(model['data-make'])
        car['name'] = model.text
        cars.append(car)
print(cars)

print('----------------------------------------------------------------------')	#70個
print('BeautifulSoup 測試 11')

url = 'https://newcar.u-car.com.tw/newcar'
soup = get_soup_from_url(url)

makes = soup.select('#makeselect > option')
makers = dict()
for make in makes:
    if make['value'] != '0':
        makers[int(make['value'])] = make.text
                
models = soup.select('#modelselect > option')
cars = list()
for model in models:
    if model['value'] != '0':
        car = dict()
        car['id'] = int(model['value'])
        car['make'] = int(model['data-make'])
        car['make-name'] = makers[car['make']]
        car['name'] = model.text
        cars.append(car)
print(cars)

print('----------------------------------------------------------------------')	#70個
print('BeautifulSoup 測試 12')

url = 'https://www.bagong.cn/dog/'
soup = get_soup_from_url(url)

photos = soup.find_all('img')
for photo in photos:
    if photo['src'].startswith('http'):
        print(photo['src'])

print('----------------------------------------------------------------------')	#70個
print('BeautifulSoup 測試 13')

#台灣彩券官網首頁
url = 'http://www.taiwanlottery.com.tw/'
soup = get_soup_from_url(url)

html_doc = """
<html><head><title>網頁標題</title></head>

<p class="title"><b>文件標題</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc,'html.parser') 

print(soup.find('b')) # <b>文件標題</b>
print(soup.find_all('a'))
print(soup.find_all("a", {"class":"sister"}))

data1=soup.find("a", {"href":"http://example.com/elsie"})
print(data1.text) # Elsie

data2=soup.find("a", {"id":"link2"}) 
print(data2.text) # Lacie

data3 = soup.select("#link3") 
print(data3[0].text) # Tillie
print(soup.find_all(['title','a'])) 

data1=soup.find("a", {"id":"link1"}) 
print(data1.get("href")) # http://example.com/elsie
print(data1["href"])     # http://example.com/elsie

print('----------------------------------------------------------------------')	#70個
print('BeautifulSoup 測試 14')

#台灣彩券官網首頁
url = 'http://www.taiwanlottery.com.tw/'
soup = get_soup_from_url(url)

data1 = soup.select("#rightdown")
#print(data1)

data2 = data1[0].find('div', {'class':'contents_box02'})
#print(data2)

data3 = data2.find_all('div', {'class':'ball_tx'})
print(data3)

#台灣彩券官網首頁
url = 'http://www.taiwanlottery.com.tw/'
soup = get_soup_from_url(url)

data1 = soup.select("#rightdown")
#print(data1)

data2 = data1[0].find('div', {'class':'contents_box02'})
#print(data2)

data3 = data2.find_all('div', {'class':'ball_tx'})
#print(data3)
#
# 威力彩號碼
print("開出順序：",end="")
for n in range(0,6):
    print(data3[n].text,end="  ") 

print("\n大小順序：",end="")    
for n in range(6,len(data3)):
    print(data3[n].text,end="  ")
     
## 第二區
red = data2.find('div', {'class':'ball_red'})
print("\n第二區：{}".format(red.text)) 


print('----------------------------------------------------------------------')	#70個
print('BeautifulSoup 測試 15 無法取得網頁資料')
'''
url = 'https://tw.appledaily.com/new/realtime/2'
soup = get_soup_from_url(url)

sel = '#maincontent > div.thoracis > div.abdominis.rlby.clearmen > ul > li.rtddt > a'
data = soup.select(sel)
for item in data:
    print(item.time.text)
    print(item.h1.text)
    print(item['href'])
'''

'''
print('----------------------------------------------------------------------')	#70個
print('BeautifulSoup 測試 16 很久')

target = 'https://tw.appledaily.com/new/realtime/{}'

titles = list()
for page in range(1, 11):
    print(page)
    url = target.format(page)
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    sel = '#maincontent > div.thoracis > div.abdominis.rlby.clearmen > ul > li.rtddt > a'
    data = soup.select(sel)
    for item in data:
        title = dict()
        title['time'] = item.time.text
        title['title'] = item.h1.text
        title['link'] = item['href']
        titles.append(title)
    time.sleep(3)
print(titles)

print('----------------------------------------------------------------------')	#70個
print('BeautifulSoup 測試 17 很久')

target = 'https://tw.appledaily.com/new/realtime/{}'

titles = list()
for page in range(1, 11):
    print(page)
    url = target.format(page)
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    sel = '#maincontent > div.thoracis > div.abdominis.rlby.clearmen > ul > li.rtddt > a'
    data = soup.select(sel)
    for item in data:
        title = dict()
        title['time'] = item.time.text
        title['title'] = item.h1.text
        title['link'] = item['href']
        titles.append(title)
    time.sleep(3)
for title in titles:
    try:
        url = title['link']
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        sel = '#article-header > header > div > h2 > span'
        target = soup.select(sel)
        print(target[0].text)
        title['title'] = target[0].text
    except:
        pass
    time.sleep(3)
    
filename = 'C:/_git/vcs/_1.data/______test_files2/news_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.json';
with open(filename, "w", encoding = 'utf-8') as fp:
    print(filename + " is dumping...")
    json.dump(titles, fp)

'''


print('BeautifulSoup 測試 作業完成')

