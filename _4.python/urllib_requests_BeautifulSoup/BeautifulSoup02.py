# Python 測試 BeautifulSoup
#解讀 遠端 網頁資料, 都是使用 html.parser 解析器

print('----------------------------------------------------------------------')	#70個
print('準備工作')

import re
import os
import sys
import csv
import time
import json
import urllib
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_html_data1(url):
    print('取得網頁資料: ', url)
    resp = requests.get(url)    # 用 requests 的 get 方法把網頁抓下來

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

    html_data.encoding = 'UTF-8' # 或是 unicode 也可, 指定編碼方式
    soup = BeautifulSoup(html_data.text, "html.parser")  # 解析原始碼
    #soup = BeautifulSoup(html_data.text, "lxml") # 指定 lxml 作為解析器
    #print(soup.prettify())  #prettify()這個函數可以將DOM tree以比較美觀的方式印出。
    #pprint.pprint(html_data.text)
    print("取得網頁標題", soup.title)
    return soup
    
print('----------------------------------------------------------------------')	#70個
print('BeautifulSoup 測試 1')

url = 'http://www.e-happy.com.tw'
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
soup = get_soup_from_url(url)

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

url = 'https://newcar.u-car.com.tw/newcar'
soup = get_soup_from_url(url)

makes = soup.select('#makeselect > option')
makers = dict()
for make in makes:
    if make['value'] != '0':
        makers[int(make['value'])] = make.text
print(makers)

print('----------------------------------------------------------------------')	#70個
print('BeautifulSoup 測試 9')

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
print('BeautifulSoup 測試 10')

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
print('BeautifulSoup 測試 11')

url = 'https://www.bagong.cn/dog/'
soup = get_soup_from_url(url)

photos = soup.find_all('img')
for photo in photos:
    if photo['src'].startswith('http'):
        print(photo['src'])

print('----------------------------------------------------------------------')	#70個
print('BeautifulSoup 測試 12')

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

soup = BeautifulSoup(html_doc, 'html.parser') 

print(soup.find('b')) # <b>文件標題</b>
print(soup.find_all('a'))
print(soup.find_all("a", {"class":"sister"}))

data1 = soup.find("a", {"href":"http://example.com/elsie"})
print(data1.text) # Elsie

data2 = soup.find("a", {"id":"link2"}) 
print(data2.text) # Lacie

data3 = soup.select("#link3") 
print(data3[0].text) # Tillie
print(soup.find_all(['title','a'])) 

data1 = soup.find("a", {"id":"link1"}) 
print(data1.get("href")) # http://example.com/elsie
print(data1["href"])     # http://example.com/elsie

print('----------------------------------------------------------------------')	#70個
print('BeautifulSoup 測試 13')

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
print('BeautifulSoup 測試 14 無法取得網頁資料')
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
print('BeautifulSoup 測試 15 很久')

target = 'https://tw.appledaily.com/new/realtime/{}'

titles = list()
for page in range(1, 11):
    url = target.format(page)
    print(url)
    html_data = requests.get(url)
    soup = BeautifulSoup(html_data.text, 'html.parser')
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
print('BeautifulSoup 測試 16 很久')

target = 'https://tw.appledaily.com/new/realtime/{}'

titles = list()
for page in range(1, 11):
    url = target.format(page)
    print(url)
    html_data = requests.get(url)
    soup = BeautifulSoup(html_data.text, 'html.parser')
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
        print(url)
        html_data = requests.get(url)
        soup = BeautifulSoup(html_data.text, 'html.parser')
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

print('----------------------------------------------------------------------')	#70個
print('BeautifulSoup 測試 17 udn news a')

#聯合新聞網
url = 'https://udn.com/news/breaknews/1'
soup = get_soup_from_url(url)

target = soup.find_all("h2", {"class":"breaking-news"})
#print(target)

for news in target:
    print(news.a['title'])

print('----------------------------------------------------------------------')	#70個
print('BeautifulSoup 測試 17 udn news b')

url = 'https://udn.com/news/breaknews/1'
soup = get_soup_from_url(url)

links = soup.find_all(class_='story-list__text')

print(links)

headlines = list()

for link in links:
    title = link.find('h2')
    try:
        print(title.a['title'])
        print(title.a['href'])
        item = dict()
        item['title'] = title.a['title']
        if not title.a['href'].startswith('http'):
            item['link'] = "https://udn.com{}".format(title.a['href'])
        else:
            item['link'] = title.a['href']
        headlines.append(item)
    except:
        pass

print(headlines)

print('----------------------------------------------------------------------')	#70個
print('BeautifulSoup 測試 17 udn news c')

url = 'https://autos.udn.com/autos/story/9060/2187994'
soup = get_soup_from_url(url)

regex = r'http.+jpg'
links = soup.find_all("a")

print(links)

photos = list()

for link in links:
    try:
        if ".jpg" in link['href']:
            print(link['href'])
            target = link['href']
            for item in re.findall(regex, target):
                photos.append(item)
    except:
        pass

print(photos)
for link in photos:
    item = urllib.parse.urlparse(link)
    q = urllib.parse.parse_qs(item.query)
    target = urllib.parse.urlparse(q['u'][0])
    filename = os.path.basename(target.path)
    urllib.request.urlretrieve(link, os.path.join("images", filename))
    print("Storing " + filename)
    time.sleep(3)
    
print("Done...")

print('----------------------------------------------------------------------')	#70個
print('BeautifulSoup 測試 18')

url = 'https://www.ptt.cc/bbs/C_Chat/index.html'

domain = "{}://{}".format(urllib.parse.urlparse(url).scheme, urllib.parse.urlparse(url).hostname)
print('domain : ', domain)

html_data = get_html_data1(url)
soup = BeautifulSoup(html_data.text, 'html.parser')

#print(soup.prettify())  #prettify()這個函數可以將DOM tree以比較美觀的方式印出。

all_links = soup.find_all(['a','img'])

for link in all_links:
    src = link.get('src')
    href = link.get('href')
    targets = [src, href]
    for t in targets:
        if t != None and ('.jpg' in t or '.png' in t):
            if t.startswith('http'):
                print(t)
            else:
                print(domain + t)
                print('domain : ', domain + t)

print('----------------------------------------------------------------------')	#70個
print('BeautifulSoup 測試 19')

domain = "{}://{}".format(urllib.parse.urlparse(url).scheme, urllib.parse.urlparse(url).hostname)
print('domain : ', domain)

html_data = get_html_data1(url)
soup = BeautifulSoup(html_data.text, 'html.parser')

#print(soup.prettify())  #prettify()這個函數可以將DOM tree以比較美觀的方式印出。
all_links = soup.find_all(['a','img'])

for link in all_links:
    src = link.get('src')
    href = link.get('href')
    targets = [src, href]
    for t in targets:
        if t != None and ('.jpg' in t or '.png' in t):
            if t.startswith('http'):
                full_path = t
            else:
                full_path = domain + t
            print(full_path)
            image_dir = url.split('/')[-1]
            if not os.path.exists(image_dir): os.mkdir(image_dir)
            filename = full_path.split('/')[-1]
            ext = filename.split('.')[-1]
            filename = filename.split('.')[-2]
            if 'jpg' in ext: filename = filename + '.jpg'
            else:            filename = filename + '.png'
            image = urlopen(full_path)
            fp = open(os.path.join(image_dir,filename),'wb')
            fp.write(image.read())
            fp.close()


print('----------------------------------------------------------------------')	#70個
print('BeautifulSoup 測試 20')

post_html = '''
</body>
</html>
'''

domain = "{}://{}".format(urllib.parse.urlparse(url).scheme, urllib.parse.urlparse(url).hostname)
print('domain : ', domain)

html_data = get_html_data1(url)
soup = BeautifulSoup(html_data.text, 'html.parser')
#print(soup.prettify())  #prettify()這個函數可以將DOM tree以比較美觀的方式印出。

pre_html = """
<!DOCTYPE html>
<html>
<head>
<meta charset='utf-8'>
<title>網頁搜集來的資料</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
  <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
  <style>
  .carousel-inner > .item > img,
  .carousel-inner > .item > a > img {
      border: 5px solid white;
      width: 50%;
      box-shadow: 10px 10px 5px #888888;
      margin: auto;
  }
  </style>

</head>
<body>
<center><h3>以下是從網頁搜集來的圖片跑馬燈</h3></center>
"""

all_links = soup.find_all(['a','img'])

carousel_part1 = ""
carousel_part2 = ""
picno = 0

for link in all_links:
    src = link.get('src')
    href = link.get('href')
    targets = [src, href]
    for t in targets:
        if t != None and ('.jpg' in t or '.png' in t):
            if t.startswith('http'):
                full_path = t
            else:
                full_path = domain + t
            print(full_path)
            image_dir = url.split('/')[-1]
            if not os.path.exists(image_dir): os.mkdir(image_dir)
            filename = full_path.split('/')[-1]
            ext = filename.split('.')[-1]
            filename = filename.split('.')[-2]
            if 'jpg' in ext: filename = filename + '.jpg'
            else:            filename = filename + '.png'
            image = urlopen(full_path)
            fp = open(os.path.join(image_dir,filename),'wb')
            fp.write(image.read())
            fp.close()

            if picno==0:
                carousel_part1 += "<li data-target='#myC' data-slide-to='{}' class='active'></li>".format(picno)
                carousel_part2 += """
                    <div class='item active'>
                        <img src='{}' alt='{}'>  
                    </div>""".format(filename, filename)

            else:
                carousel_part1 += "<li data-target='#myC' data-slide-to='{}'></li>".format(picno)
                carousel_part2 += """
                    <div class='item'>
                        <img src='{}' alt='{}'>  
                    </div>""".format(filename, filename)
            picno += 1

            html_body = """
            <div id='myC' class='carousel slide' data-ride='carousel'>
                <ol class='carousel-indicators'>
                {}
                </ol>
                <div class='carousel-inner' role='listbox'>
                {}
                </div>
                <a class="left carousel-control" href="#myC" role="button" data-slide="prev">
                    <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
                    <span class="sr-only">前一張</span>
                </a>
                <a class="right carousel-control" href="#myC" role="button" data-slide="next">
                    <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
                    <span class="sr-only">後一張</span>
                </a>
            </div>
            """.format(carousel_part1, carousel_part2)

'''
fp = open('index.html', 'w')
fp.write(pre_html+html_body+post_html)
fp.close()            
'''

print('----------------------------------------------------------------------')	#70個
print('BeautifulSoup 測試 21')

from urllib.request import urlopen
from urllib.error import HTTPError

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

print('----------------------------------------------------------------------')	#70個
print('BeautifulSoup 測試 22')

import urllib.parse
from bs4 import BeautifulSoup
import requests

html_data = requests.get('https://www.mvdis.gov.tw/m3-emv-plate/webpickno/queryPickNo#')
soup = BeautifulSoup(html_data.text, 'html.parser')
captcha_image = soup.find('img', id='pickimg')['src'] 
csrf_token = soup.find_all('input', type='hidden') 
image_url = urllib.parse.urljoin('https://www.mvdis.gov.tw/', captcha_image)
print(image_url)

#驗證碼 = 0123456789
captcha = '0123456789'
headers = {
    "user-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
    "Cookie":'DWRSESSIONID=qNiI6i9UPxr4DV2G7PrFV8pkahn; _ga=GA1.3.1352658715.1598224971; BSESSIONID1=D106D274717EDF2C4EFDD9D698E61581.tsb22; _gid=GA1.3.615895194.1598974412; JSESSIONID1=B71AEB3133E436EA9619A6F6F3CDA2EA.tsp12'
}
data = {
    'method': 'qryPickNo',
    'selDeptCode': "2",
    'selStationCode': "30",
    'selWindowNo': "01",
    'selCarType': "M",
    'selEnergyType': "C",
    'selPlateType': "F",
    'plateVer': "2",
    'validateStr': str(captcha),
    'queryType': 0,
    'queryNo': '*',
    'CSRFToken': str(csrf_token[2]['value']),
}

html = requests.post('https://www.mvdis.gov.tw/m3-emv-plate/webpickno/queryPickNo', data = data, headers = headers).text
soup = BeautifulSoup(html, 'html.parser')
plate_numbers = soup.find_all('a','number')
print(plate_numbers)

for plate_number in plate_numbers:
    print('aaaaaaaaaaaaaa')
    print(plate_number.text)

print('----------------------------------------------------------------------')	#70個
print('BeautifulSoup 測試 23')




print('\n\nBeautifulSoup 測試 作業完成\n')

