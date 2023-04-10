# Python 測試 BeautifulSoup

import sys
import requests
from bs4 import BeautifulSoup

def get_html_data1(url):
    print('取得網頁資料: ', url)
    resp = requests.get(url)
    # 檢查 HTTP 回應碼是否為 requests.codes.ok(200)
    if resp.status_code != requests.codes.ok:
        print('讀取網頁資料錯誤, url: ', resp.url)
        return None
    else:
        return resp

print('BeautifulSoup 測試 1')

url = 'http://tw.yahoo.com'
html_data = get_html_data1(url)
if html_data:
        soup = BeautifulSoup(html_data.text, "html.parser")
        print("取得網頁標題", soup.title)
else:
        print('無法取得網頁資料')

print('BeautifulSoup 測試 2')

url = 'https://tw.news.yahoo.com/rss/technology'
html_data = get_html_data1(url)
if html_data:
        soup = BeautifulSoup(html_data.text, "html.parser")
        type(soup)
        soup.findAll('item')

        print("取得Yahoo奇摩新聞-科技新聞-標題")
        for news in soup.findAll('item'):
                print(news.title)
else:
        print('無法取得網頁資料')

print('BeautifulSoup 測試 3')

url = 'https://www.google.com.tw/'
html_data = get_html_data1(url)
if html_data:
        soup = BeautifulSoup(html_data.text, 'html.parser')
        all_links = soup.find_all('a')

        for link in all_links:
                href = link.get('href')
                if href != None and href.startswith('http://'):
                        print('取得資料')
                        print(href)
else:
        print('無法取得網頁資料')

print('BeautifulSoup 測試 4')
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

print('BeautifulSoup 測試 5')

url = 'http://ehappy.tw/bsdemo1.htm'
html_data = get_html_data1(url)
if html_data:
        html_data.encoding = 'UTF-8'
        soup = BeautifulSoup(html_data.text, 'html.parser')

        print("取得網頁標題", soup.title)
        print("取得網頁標題", soup.title.text)
        print("取得 h1: ", soup.h1)
        print("取得 p: ", soup.p)
else:
        print('無法取得網頁資料')

print('BeautifulSoup 測試 6')

url = 'https://oldsiao.neocities.org/'
html_data = get_html_data1(url)
if html_data:
        soup = BeautifulSoup(html_data.text, 'html.parser')

        print("取得網頁標題", soup.title)
        print("取得網頁標題", soup.title.text)

        #尋找指定標籤find()、find_all()

        print("尋找標籤「<div>」")
        print(soup.find("div"))

        print("尋找標籤「<title>」")
        print(soup.find_all("title"))
else:
        print('無法取得網頁資料')


print('BeautifulSoup 測試 7')

'''
# 題問說明
question_description = "[1]牡羊座 [2]金牛座 [3]雙子座 [4]巨蟹座 [5]獅子座 [6]處女座 [7]天秤座 [8]天蠍座 [9]射手座 [10]摩羯座 [11]水瓶座 [12]雙魚座，請選擇星座(僅能填數字):"

# 限制填寫內容為數字
while True:
    ans_data = input(question_description)
    # ans_data為數字且數值介於1~12
    if ans_data.isdigit() == True and int(ans_data) > 0 and int(ans_data) < 13:
        break
    else:
        pass
'''
    
url = 'https://oldsiao.neocities.org/'
html_data = get_html_data1(url)
if html_data:
        html_data.encoding = 'UTF-8'    # 設定讀取編碼(預設 UTF-8)
        soup = BeautifulSoup(html_data.text, 'html.parser')
        print("使用 BeautifulSoup 分析網頁")
        print("取得網頁標題", soup.title)
        print("取得網頁標題", soup.title.text)
else:
        print('無法取得網頁資料')


#PTT C_Chat板每篇文章的標題

import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.request import urlopen

print('BeautifulSoup 測試 8')

url = 'https://www.ptt.cc/bbs/C_Chat/index.html'
html_data = get_html_data1(url)
if html_data:
    soup = BeautifulSoup(html_data.text, "html.parser")  # 解析原始碼
    #print(soup.prettify())  #prettify()這個函數可以將DOM tree以比較美觀的方式印出。
    # 發現所有的文章標題都在class="title"的div中

    links = soup.find_all("div", class_="title")    # 文章標題
    for link in links:
        print(link.text.strip()) # strip()用來刪除文字前面和後面多餘的空白
else:
    print('無法取得網頁資料')


print('BeautifulSoup 測試 9')

url = 'http://blog.castman.net/web-crawler-tutorial/ch1/connect.html'
html_data = get_html_data1(url)
if html_data:
    soup = BeautifulSoup(html_data.text, 'html.parser')
    #print(soup.prettify())  #prettify()這個函數可以將DOM tree以比較美觀的方式印出。
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
else:
    print('無法取得網頁資料')

print('BeautifulSoup 測試 10')

#用 BeautifulSoup 分析網頁資料

url = 'https://www.ptt.cc/bbs/C_Chat/index.html'

domain = "{}://{}".format(urlparse(url).scheme, urlparse(url).hostname)
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
                print(domain+t)

print('BeautifulSoup 測試 11')

domain = "{}://{}".format(urlparse(url).scheme, urlparse(url).hostname)
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
            if t.startswith('http'): full_path = t
            else:                    full_path = domain+t
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



print('BeautifulSoup 測試 12')

post_html = '''
</body>
</html>
'''

domain = "{}://{}".format(urlparse(url).scheme, urlparse(url).hostname)
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
            if t.startswith('http'): full_path = t
            else:                    full_path = domain+t
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







print('BeautifulSoup 測試 作業完成')

