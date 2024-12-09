# Python 測試 BeautifulSoup
# 解讀 本地 / 遠端 網頁資料, 都是使用 html.parser 解析器

# 以BeautifulSoup套件進行網頁解析

# 1. 展開的html text成string
# 2. 本地html檔案
# 3. 網頁資料

# 共同抽出
# print(soup.prettify())  #prettify()這個函數可以將DOM tree以比較美觀的方式印出。
# print(soup.prettify()) # 把排版後的 html 印出來
# print("列印BeautifulSoup物件資料型態 ", type(soup))
# print("取得網頁內容 : ", soup.text)

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

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個
print("準備工作")

import re
import os
import sys
import csv
import time
import json
import urllib
import requests
import urllib.parse
from bs4 import BeautifulSoup
from datetime import datetime
from urllib.request import urlopen


def get_html_data1(url):
    # print("取得網頁資料: ", url)
    resp = requests.get(url)  # 用 requests 的 get 方法把網頁抓下來

    # 檢查 HTTP 回應碼是否為 requests.codes.ok(200)
    if resp.status_code != requests.codes.ok:
        print("讀取網頁資料錯誤, url: ", resp.url)
        return None
    else:
        return resp


def get_soup_from_url(url):
    html_data = get_html_data1(url)
    if html_data == None:
        print("無法取得網頁資料")
        sys.exit(1)  # 立刻退出程式

    html_data.encoding = "UTF-8"  # 或是 unicode 也可, 指定編碼方式
    soup = BeautifulSoup(html_data.text, "html.parser")  # 解析原始碼
    # soup = BeautifulSoup(html_data.text, "lxml") # 指定 lxml 作為解析器
    # pprint.pprint(html_data.text)
    # print("取得網頁標題", soup.title)
    return soup


print("------------------------------------------------------------")  # 60個

string_html_data = """
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <title>BeautifulSoup套件進行網頁解析</title>
    <meta charset="utf-8">
</head>
<body>
<h1 style="background-color:red; color:white; font-family:Segoe Script; border:3px #000000 solid;">Python is funny</h1>
Python簡單易學又有趣
<h1 style="color:rgb(255, 99, 71);">程式設計網站推薦</h1>
<a href="https://www.google.com111/">超連結1</a><br>
<a href="https://www.google.com222/">超連結2</a><br>
<a href="https://www.google.com333/">超連結3</a><br>
<a href="https://www.google.com444/">超連結4</a><br>
<a href="https://www.google.com555/">超連結5</a><br>

<p id="p1">段落1</p>
<p id="p2" class='red'>段落2 p2</p>
<p id="p2" class='red'>段落3 p3</p>
<p id="p1">段落4</p>
<p id="p1">段落5</p>

<h1>文件標題</h1>
<img src="https://www.google.com.tw/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png">

<div class="content">
    <div class="item1">
        <a href="http://example.com/one" class="red" id="link1">超連結a</a>
        <a href="http://example.com/two" class="red" id="link2">超連結b</a>
    </div>
    <a href="http://example.com/three" class="blue" id="link3">
        <img src="https://s.yimg.com/cv/apiv2/twfrontpage/logo/Yahoo-TW-desktop-FP@2x.png">超連結c
    </a>
</div>

<h1 class="large">我是標題</h1>
<div>
<p>我是段落</p>
<img src="https://www.w3.org/html/logo/downloads/HTML5_Logo_256.png" alt="我是圖片">
<a href="http://www.e-happy.com.tw">我是超連結</a>
</div>

</body>
"""

soup = BeautifulSoup(string_html_data, "html.parser")
# soup = BeautifulSoup(string_html_data, "lxml")

print("取得第一個 h1: ", soup.h1)
print("取得 第一個 p: ", soup.p)
print("取得 第一個 <a></a>: ", soup.a)

print("網頁標題 整行")
print(soup.title)
print("網頁標題 內容")
print(soup.title.text)
print("網頁標題 名稱")
print(soup.title.name)
print("網頁標題 字串")
print(soup.title.string)
print("網頁標題 上層")
print(soup.title.parent.name)
print("網頁標題 上一層Tag")
print(soup.title.parent)

print(soup.find("title"))  # 傳回網頁含<title>~</title>
print(soup.find("title").text)  # 傳回網頁<title>標籤內的資料

print("------------------------------")  # 30個
print("網頁html語法區塊：")
# print(soup.find("html"))  # <html>標籤
print("------------------------------")  # 30個
print("網頁表頭範圍：")
# print(soup.find("head"))  # <head>標籤
print("------------------------------")  # 30個
print("網頁身體範圍：")
# print(soup.find("body"))  # <body>標籤
print("------------------------------")  # 30個
print("find 超連結<a>")
cc = soup.find("a", {"href": "https://www.google.com333/"})
print(cc)
print(cc.text)

print("取得 全部 <a></a>: ", soup.find_all("a"))

print(soup.find_all("a", {"class": "red"}))

print("取得 全部 <p></p>: ", soup.find_all("p"))

print("------------------------------")  # 30個
print("find 段落<p>")
print('find("p") 1 找 第一個<p>')
print(soup.find("p"))
print('find("p") 2 找 第一個<p>')
print(soup.find("p"))
print('find("p") 3 找 第一個<p>')
print(soup.find("p"))

print('find("p") 有條件找<p>')
print(soup.find("p", {"id": "p2", "class": "red"}))

print('find("p") 有條件找<p>')
print(soup.find("p", id="p2", class_="red"))

print('find("p") 第一個<h1>')
print(soup.find("h1"))

print("多重取得 全部 <xx></xx>: ", soup.find_all(["title", "h1"]))

print("------------------------------")  # 30個

print("select() title")
print(soup.select("title"))
print("select() 全部 p")
print(soup.select("p"))
print("select() 全部 #p1")
print(soup.select("#p1"))
print("select() 全部 .red")
print(soup.select(".red"))

print("------------------------------")  # 30個

print("select().get()")
print(soup.select("img")[0].get("src"))
print(soup.select("a")[0].get("href"))
print(soup.select("img")[0]["src"])
print(soup.select("a")[0]["href"])

print("------------------------------")  # 30個

cc = soup.select("#link1")
print(cc[0].text)  # 超連結a
print(cc[0].get("href"))  # http://example.com/one
print(cc[0]["href"])  # http://example.com/one

print(soup.select("div img")[0]["src"])  # http://example.com/three.jpg

print("------------------------------------------------------------")  # 60個

string_html_data = """
<body>
<p class="title"><b>The test1</b></p>
<p class="title"><b>The test2</b></p>
<p class="title"><b>The test3</b></p>
<a class="redcolor" href="http://powenko.com/1.html" id="link1">test1</a>
<a class="bluecolor" href="http://powenko.com/2.html" id="link2">test2</a>
<a class="redcolor" id="link3" href="http://powenko.com/3.html" id="link3">test3</a>
</body>
"""
soup = BeautifulSoup(string_html_data, "html.parser")
print("取得 第一個 p: ", soup.p)
print('soup.p["class"]')
print(soup.p["class"])
print("取得 第一個 a: ", soup.a)
print("取得 第一個 <a></a>: ", soup.a)
print("取得 全部 <a></a>: ", soup.find_all("a"))

print("一一列出連結")
for link in soup.find_all("a"):  # 取得 全部 <a></a>
    print(link.get("href"))
print(soup.select("a"))
print(soup.select(".redcolor"))  # class="redcolor"
print(soup.select("#link3"))  # id="link3"
for link in soup.select("a"):
    print(link.string)

print("------------------------------------------------------------")  # 60個

string_html_data = """
<html>
  <body>
    <div class="section" id="main">
      <img alt="旗標圖示" src="https://zh.wikipedia.org/static/images/icons/wikdddipedia.png">
      <p>產品類別</p>
      <button id="books"><h4 class="bk">圖書</h4></button>
      <button id="maker"><h4 class="pk">創客</h4></button>
      <button id="teach"><h4 class="pk">教具</h4></button>
    </div>
    <div class="section" id="footer">
      <p>杭州南路一段15-1號19樓</p>
      <a href="http://flag.tw/contact">聯絡我們</a>
    </div>
  </body>
</html>
"""

soup = BeautifulSoup(string_html_data, "lxml")

print("取得 第一個 <a></a>: ", soup.a)
print(soup.a.text)
print(soup.a.get("href"))
print(soup.a["href"])

print(soup.find("h4"))
print(soup.find("h4", {"class": "pk"}))
print(soup.find("h4").text)

print("取得 全部 <h4></h4>: ", soup.find_all("h4"))

print(soup.find_all("h4", {"class": "pk"}))

print("多重取得 全部 <xx></xx>: ", soup.find_all(["title", "p"]))
print(soup.find_all(["title", "p"])[1].text)  # ← 傳回第 1 個 (由 0 算起) 符合標籤中的文字

print("h4:", soup.select("h4"))  # ←查詢所有 h4 標籤
print("#book:", soup.select("#books"))  # ←查詢所有 id 為 'books' 的標籤
print(".pk:", soup.select(".pk"))  # ←查詢所有 class 為 'pk' 的標籤
print("h4.bk", soup.select("h4.bk"))  # ←查詢所有 class 為 'bk' 的 h4 標籤

print(soup.select("#main button .pk"))

print(soup.select("#main button .pk")[1].text)
print(soup.select("#footer a")[0]["href"])

print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 12")

string_html_data = """
<html>
<p class="title"><b>文件標題</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup = BeautifulSoup(string_html_data, "html.parser")

print(soup.find("b"))  # <b>文件標題</b>

print("取得 全部 <a></a>: ", soup.find_all("a"))

print(soup.find_all("a", {"class": "sister"}))

data1 = soup.find("a", {"href": "http://example.com/elsie"})
print(data1.text)  # Elsie

cc2 = soup.find("a", {"id": "link2"})
print(cc2.text)  # Lacie

data3 = soup.select("#link3")
print(data3[0].text)  # Tillie

print("多重取得 全部 <xx></xx>: ", soup.find_all(["title", "a"]))

data1 = soup.find("a", {"id": "link1"})
print(data1.get("href"))  # http://example.com/elsie
print(data1["href"])  # http://example.com/elsie

print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 2")

string_html_data = """
<div class="content">
    E-Mail：<a href="mailto:mail@test.com.tw">mail</a><br>
    E-Mail2：<a href="mailto:mail2@test.com.tw">mail2</a><br>
    <ul class="price">定價：360元 </ul>
    <img src="http://test.com.tw/p1.jpg">
    <img src="http://test.com.tw/p2.jpg">
    <img src="http://test.com.tw/p3.png">
</div>
"""

soup = BeautifulSoup(string_html_data, "html.parser")

print("用 re 搭配搜尋")
print("搜尋網頁中的 e-mail")
emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", string_html_data)
for email in emails:
    print(email)

print("搜尋網頁中的 價格")
price = re.findall(r"[\d]+", soup.select(".price")[0].text)[0]  # 價格
print(price)

print("搜尋網頁中的 jpg圖片連結")
regex = re.compile(".*\.jpg")
imglist = soup.find_all("img", {"src": regex})
for img in imglist:
    print(img["src"])

print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 1")

string_html_data = """
<html>
  <head><meta charset="big5"><title>Perl學習手札</title></head>
  <body>
    <div class="content">
      <img src="https://easun.org/perl/perl-toc/index_2.png">
    </div>
    <p class="header">
      <h1>h1 : Perl學習手札</h1>
    </p>
    <h2 class="heading">h2 : 第一章 : 關於Perl</h2>
    <h2 class="heading" id="this">h2 : 第二章 : 純量變數</h2>
    <h2 class="heading">h2 : 第三章 : 串列與陣列</h2>
    <div class="content">
      <div class="item1">
        <a href="https://easun.org/perl/perl-toc/ch04.html" class="red" id="link1">第四章 : 基本的控制結構</a>
        <br>
        <a href="https://easun.org/perl/perl-toc/ch05.html" class="red" id="link2">第五章 : 雜湊(Hash)</a>
      </div>
      <a href="https://easun.org/perl/perl-toc/ch06.html" class="blue" id="link3">第六章 : 副常式</a>
      <br>
    </div>
    <p id="p1">p1 : 第七章 : 正規表示式</p>
    <p id="p2" class='red'>p2 : 第八章 : 更多關於正規表示式</p>
    <div class="main">
     <div class="container">
      <p>p : 對於我們剛剛提出來的資料結構需求，希望能把相同的東西簡單的存取，並且讓它們能被歸納在一起。陣列正是解決這個問題的方案，也就是把一堆性質接近的變數放在同一個資料結構裡，這樣可以很方便的處理跟存取。</p>
     </div>
    </div>
  </body>
</html>
"""

print("解讀本地網頁資料1")

soup = BeautifulSoup(string_html_data, "html.parser")

print("取得<h1>??</h1>: ", soup.find("h1"))  # 印出整行資料
print("取得<h1>??</h1>: ", soup.find("h1").text)  # 只印出text部分

print("多重取得 全部 <xx></xx>: ", soup.find_all(["title", "h1"]))

print("取得 全部 <a></a>: ", soup.find_all("a"))
print("有3個, 需要縮小範圍")
print("取得全部 a class red : ", soup.find_all("a", {"class": "red"}))
print("有2個, 需要縮小範圍")
data1 = soup.find("a", {"href": "https://easun.org/perl/perl-toc/ch05.html"})
print("取得a 指明 href: ", data1)  # 印出整行資料
print("取得a 指明 href: ", data1.text)  # 只印出text部分

print("取得超連結")
cc = soup.select("#link1")
print("取得link1: ", cc)  # 印出整行資料
print("取得link1 text: ", cc[0].text)  # 只印出text部分
print("取得link1 get : ", cc[0].get("href"))  # https://easun.org/perl/perl-toc/ch01.html
print("取得link1 href: ", cc[0]["href"])  # https://easun.org/perl/perl-toc/ch01.html

print("取得圖片超連結")
print(
    "取得div img: ", soup.select("div img")[0]["src"]
)  # https://easun.org/perl/perl-toc/index_2.png

print("解讀本地網頁資料2")

# 用find
print("取得一個 p", soup.find("p"))
print("取得 全部 <p></p>: ", soup.find_all("p"))
print("取得 p, p2 class red", soup.find("p", {"id": "p2", "class": "red"}))
print("取得 p, p2 class red", soup.find("p", id="p2", class_="red"))
# 用select
print("select title", soup.select("title"))
print("select p", soup.select("p"))
print("select #p1", soup.select("#p1"))
print("select .red", soup.select(".red"))
# 用select
print("取得圖片超連結 取得 img src", soup.select("img")[0].get("src"))
print("取得網頁超連結 取得 a href", soup.select("a")[0].get("href"))
print("取得圖片超連結 取得 img src", soup.select("img")[0]["src"])
print("取得網頁超連結 取得 a href", soup.select("a")[0]["href"])

print("多重條件選擇")
data = soup.select("div div p")  # 尋找 div 標籤裡面的 div 標籤裡面的 p 標籤 三者都要符合的抓出來
print("符合條件的資料", len(data), "筆")
print(data)

print("解讀本地網頁資料3")

print("尋找符合標籤的第一個節點 find h1")
h1 = soup.find("h1")
print("取得<h1>??</h1>: ", h1)  # 印出整行資料
print("取得<h1>??</h1>: ", h1.text)  # 只印出text部分

print("尋找符合標籤的第一個節點 find by class")
# 使用class屬性定位，但因為在Python中已經有class保留字了，所以改用class_
container = soup.find("div", class_="container")
print("取得div container: ", container)  # 印出整行資料
print("取得div container: ", container.text)  # 只印出text部分

print("尋找符合標籤的第一個節點 find by id")
# 用id屬性定位。
this = soup.find("h2", id="this")
print("取得h2 this: ", this)  # 印出整行資料
print("取得h2 this: ", this.text)  # 只印出text部分

print("取得 全部 <h2></h2>")
h2s = soup.find_all("h2")  # 取得 全部 <h2></h2>
length = len(h2s)
print("共找到", length, "筆資料")
for nn in range(length):
    print(h2s[nn].text)  # 使用索引值, 只印出text部分
# print("取得全部 h2: ", h2s)        #印出全部資料, 一個list

# 定位多個標籤，則將標籤打包成一個列表就好了。limit屬性則可以限制數量。
h1_h2s = soup.find_all(["h1", "h2"], limit=3)  # 多重取得 全部 <xx></xx>
length = len(h1_h2s)
print("共找到", length, "筆資料")
for nn in range(length):
    print(h1_h2s[nn].text)  # 使用索引值, 只印出text部分
# print("取得全部 h1 h2: ", h1_h2s)        #印出全部資料, 一個list

# 用select_one
# select_one()使用CSS選擇器的語法來定位節點
h1 = soup.select_one("h1")
print(h1)
print("取得<h1>??</h1>: ", h1)  # 印出整行資料
print("取得<h1>??</h1>: ", h1.text)  # 只印出text部分

h2s = soup.select("h2")
length = len(h2s)
print("共找到", length, "筆資料")
for nn in range(length):
    print(h2s[nn].text)  # 使用索引值, 只印出text部分
# print("取得全部 h2: ", h2s)        #印出全部資料, 一個list

# 用select_one by class
# class 定位
p = soup.select_one("div.container")
print("取得div.container: ", p)  # 印出整行資料
print("取得div.container: ", p.text)  # 只印出text部分

# 用select_one by id
# id定位
this = soup.select_one("h2#this")
print("h2#this: ", this)  # 印出整行資料
print("h2#this: ", this.text)  # 只印出text部分

# 尋找parent和sibling
# this = soup.find("h2", id="this")
# print(this)
# print(this.find_previous_sibling())
# print(this.find_next_sibling())
# print(this.find_parent())

# 取得文字
# 定位到指定的節點後，可以使用text或string取得文字，或者也可以用getText()
h1 = soup.find("h1")
print("h1 getText(): ", h1.getText())
print("h1 text: ", h1.text)
print("h1 strint: ", h1.string)
print("取得<h1>??</h1>: ", h1)  # 印出整行資料
print("取得<h1>??</h1>: ", h1.text)  # 只印出text部分

# 取得屬性值
# 對於有屬性值的節點，就用get("屬性")或類似字典的方式["屬性"]取得屬性值。
# 取得<img>標籤中的src屬性值：
img = soup.find("img")
print("取得圖片超連結 取得 img src", img["src"])
print("取得圖片超連結 取得 img src", img.get("src"))

# 下載圖片 另存新檔
filename = img["src"].split("/")[-1]  # 取得圖檔名
foldername = "C:/_git/vcs/_1.data/______test_files2/"
filename2 = os.path.join(foldername, filename)

img = requests.get(img["src"])

with open(filename2, "wb") as file:
    file.write(img.content)
print("圖片下載完成, 檔案 : " + filename2)

print("下載網頁中的所有圖片")

# 以標題建立目錄儲存圖片
title = soup.title.text
images_dir = "下載圖片_" + title + "/"
if not os.path.exists(images_dir):
    os.mkdir(images_dir)

all_imgs = soup.find_all("img")  # 取得 全部 <img></img>
print(all_imgs)

# 處理所有 <img> 標籤
n = 0
for img in all_imgs:
    print(img)
    # 讀取 src 屬性內容
    src = img.get("src")
    print(src)
    # 讀取 .jpg 檔
    if src != None and (".png" in src):
        # 設定圖檔完整路徑
        full_path = src
        print(full_path)
        filename = full_path.split("/")[-1]  # 取得圖檔名
        print(filename)
        # 儲存圖片
        try:
            print(full_path)
            image = urlopen(full_path)  # 問題在此
            print("aaaaaaaaaaaa")
            """
            with open(os.path.join(images_dir, filename),'wb') as f:
                f.write(image.read())  
            n+=1
            if n>=1000: # 最多下載 1000 張
                break
            """
        except:
            print("{} 無法讀取!".format(filename))

print("共下載", n, "張圖片")

print("------------------------------------------------------------")  # 60個

string_html_data = """
<!doctype html>
<html>
<head>
   <meta charset="utf-8">
   <title>洪錦魁著作</title>
   <style>
      h1#author { width:400px; height:50px; text-align:center;
	     background:linear-gradient(to right,yellow,green);
      }
	  h1#content { width:400px; height:50px;
		 background:linear-gradient(to right,yellow,red); 
      }
      section { background:linear-gradient(to right bottom,yellow,gray); }
   </style>
</head>
<body>
<h1 id="author">洪錦魁</h1>
<img src="hung.jpg" width="100">
<section>
   <h1 id="content">一個人的極境旅行 - 南極大陸北極海</h1>
   <p>2015/2016年<strong>洪錦魁</strong>一個人到南極</p>
   <img src="travel.jpg" width="300"
</section>
<section>
   <h1 id="content">HTML5+CSS3王者歸來</h1>
   <p>本書講解網頁設計使用HTML5+CSS3</p>
   <img src="html5.jpg" width="300">
</section>
</body>
</html>
"""

soup = BeautifulSoup(string_html_data, "lxml")

print("------------------------------")  # 30個

cc = soup.find("h1")
print("資料型態       = ", type(cc))
print("列印Tag        = ", cc)
print("Text屬性內容   = ", cc.text)
print("String屬性內容 = ", cc.string)

cc = soup.find_all("h1", limit=2)  # 取得 全部 <h1></h1>
for c in cc:  # 列印串列元素內容
    print(c.text)

cc = soup.find_all("h1")  # 取得 全部 <h1></h1>
print("資料型態    = ", type(cc))  # 列印資料型態
print("列印Tag串列 = ", cc)  # 列印串列

print("\n使用Text屬性列印串列元素 : ")
for c in cc:  # 列印串列元素內容
    print(c.text)
print("\n使用getText()方法列印串列元素 : ")
for c in cc:
    print(c.getText())

print("------------------------------")  # 30個

cc = soup.find(id="author")
print(cc)
print(cc.text)

print("------------------------------")  # 30個

cc = soup.find_all(id="content")
for c in cc:
    print(c)
    print(c.text)

print("------------------------------")  # 30個

cc = soup.select("#author")
print("資料型態     = ", type(cc))  # 列印資料型態
print("串列長度     = ", len(cc))  # 列印串列長度
print("元素資料型態 = ", type(cc[0]))  # 列印元素資料型態
print("元素內容     = ", cc[0].getText())  # 列印元素內容

print("------------------------------")  # 30個

cc = soup.select("#author")
print("列出串列元素的資料型態    = ", type(cc[0]))
print(cc[0])
print("列出str()轉換過的資料型態 = ", type(str(cc[0])))
print(str(cc[0]))

print("------------------------------")  # 30個

cc = soup.select("#author")
print(str(cc[0].attrs))

print("------------------------------")  # 30個

cc = soup.select("p")
print("含<p>標籤的串列長度 = ", len(cc))
for c in cc:
    print(str(cc))  # 內部有子標籤<strong>字串
    print(c.getText())  # 沒有子標籤
    print(c.text)  # 沒有子標籤

print("------------------------------")  # 30個

cc = soup.select("img")
print("含<img>標籤的串列長度 = ", len(cc))
for c in cc:
    print(c)

print("------------------------------")  # 30個

cc = soup.select("img")
print("含<img>標籤的串列長度 = ", len(cc))
for c in cc:
    print("列印標籤串列 = ", c)
    print("列印圖檔     = ", c.get("src"))
    print("列印圖檔     = ", c["src"])

sys.exit()

print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 1")

url = "http://www.e-happy.com.tw"
url = "http://tw.yahoo.com"

soup = get_soup_from_url(url)

url = "https://tw.news.yahoo.com/rss/technology"
soup = get_soup_from_url(url)

soup.findAll("item")

print("取得Yahoo奇摩新聞-科技新聞-標題")
for news in soup.findAll("item"):
    print(news.title)

print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 2")

url = "https://www.google.com.tw/"
soup = get_soup_from_url(url)

all_links = soup.find_all("a")  # 取得 全部 <a></a>

for link in all_links:
    href = link.get("href")
    if href != None and href.startswith("http://"):
        print("取得資料")
        print(href)

print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 5")

# PTT C_Chat板每篇文章的標題

url = "https://www.ptt.cc/bbs/C_Chat/index.html"
soup = get_soup_from_url(url)

# 發現所有的文章標題都在class="title"的div中
all_links = soup.find_all("div", class_="title")  # 文章標題
for link in all_links:
    print(link.text.strip())  # strip()用來刪除文字前面和後面多餘的空白

print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 6")

url = "http://blog.castman.net/web-crawler-tutorial/ch1/connect.html"
soup = get_soup_from_url(url)

try:
    h1 = soup.find("h1")
except:
    h1 = None
if h1:
    print(soup.find("h1"))
    print(soup.find("h1").text)
try:
    h2 = soup.find("h2")
except:
    h2 = None
if h2:
    print(soup.find("h2").text)
else:
    print("h2 tag not found!")

print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 8")

url = "https://newcar.u-car.com.tw/newcar"
soup = get_soup_from_url(url)

makes = soup.select("#makeselect > option")
makers = dict()
for make in makes:
    if make["value"] != "0":
        makers[int(make["value"])] = make.text
print(makers)

print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 9")

url = "https://newcar.u-car.com.tw/newcar"
soup = get_soup_from_url(url)

models = soup.select("#modelselect > option")
cars = list()
for model in models:
    if model["value"] != "0":
        car = dict()
        car["id"] = int(model["value"])
        car["make"] = int(model["data-make"])
        car["name"] = model.text
        cars.append(car)
print(cars)

print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 10")

url = "https://newcar.u-car.com.tw/newcar"
soup = get_soup_from_url(url)

makes = soup.select("#makeselect > option")
makers = dict()
for make in makes:
    if make["value"] != "0":
        makers[int(make["value"])] = make.text

models = soup.select("#modelselect > option")
cars = list()
for model in models:
    if model["value"] != "0":
        car = dict()
        car["id"] = int(model["value"])
        car["make"] = int(model["data-make"])
        car["make-name"] = makers[car["make"]]
        car["name"] = model.text
        cars.append(car)
print(cars)

print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 11")

url = "https://www.bagong.cn/dog/"
soup = get_soup_from_url(url)

photos = soup.find_all("img")  # 取得 全部 <img></img>
for photo in photos:
    if photo["src"].startswith("http"):
        print(photo["src"])

print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 17 udn news a")

# 聯合新聞網
url = "https://udn.com/news/breaknews/1"
soup = get_soup_from_url(url)

target = soup.find_all("h2", {"class": "breaking-news"})
# print(target)

for news in target:
    print(news.a["title"])

print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 17 udn news b")

url = "https://udn.com/news/breaknews/1"
soup = get_soup_from_url(url)

all_links = soup.find_all(class_="story-list__text")
print(all_links)

headlines = list()

for link in all_links:
    title = link.find("h2")
    try:
        print(title.a["title"])
        print(title.a["href"])
        item = dict()
        item["title"] = title.a["title"]
        if not title.a["href"].startswith("http"):
            item["link"] = "https://udn.com{}".format(title.a["href"])
        else:
            item["link"] = title.a["href"]
        headlines.append(item)
    except:
        pass

print(headlines)

print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 17 udn news c")

url = "https://autos.udn.com/autos/story/9060/2187994"
soup = get_soup_from_url(url)

regex = r"http.+jpg"

photos = list()

all_links = soup.find_all("a")  # 取得 全部 <a></a>
print(all_links)

for link in all_links:
    try:
        if ".jpg" in link["href"]:
            print(link["href"])
            target = link["href"]
            for item in re.findall(regex, target):
                photos.append(item)
    except:
        pass

print(photos)

for link in photos:
    item = urllib.parse.urlparse(link)
    q = urllib.parse.parse_qs(item.query)
    target = urllib.parse.urlparse(q["u"][0])
    filename = os.path.basename(target.path)
    urllib.request.urlretrieve(link, os.path.join("images", filename))
    print("Storing " + filename)
    time.sleep(3)

print("Done...")

print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 18")

url = "https://www.ptt.cc/bbs/C_Chat/index.html"

domain = "{}://{}".format(
    urllib.parse.urlparse(url).scheme, urllib.parse.urlparse(url).hostname
)
print("domain : ", domain)

html_data = get_html_data1(url)
soup = BeautifulSoup(html_data.text, "html.parser")

all_links = soup.find_all(["a", "img"])  # 多重取得 全部 <xx></xx>

for link in all_links:
    src = link.get("src")
    href = link.get("href")
    targets = [src, href]
    for t in targets:
        if t != None and (".jpg" in t or ".png" in t):
            if t.startswith("http"):
                print(t)
            else:
                print(domain + t)
                print("domain : ", domain + t)

print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 19")

domain = "{}://{}".format(
    urllib.parse.urlparse(url).scheme, urllib.parse.urlparse(url).hostname
)
print("domain : ", domain)

html_data = get_html_data1(url)
soup = BeautifulSoup(html_data.text, "html.parser")

all_links = soup.find_all(["a", "img"])  # 多重取得 全部 <xx></xx>

for link in all_links:
    src = link.get("src")
    href = link.get("href")
    targets = [src, href]
    for t in targets:
        if t != None and (".jpg" in t or ".png" in t):
            if t.startswith("http"):
                full_path = t
            else:
                full_path = domain + t
            print(full_path)
            image_dir = url.split("/")[-1]
            if not os.path.exists(image_dir):
                os.mkdir(image_dir)
            filename = full_path.split("/")[-1]
            ext = filename.split(".")[-1]
            filename = filename.split(".")[-2]
            if "jpg" in ext:
                filename = filename + ".jpg"
            else:
                filename = filename + ".png"
            image = urlopen(full_path)
            fp = open(os.path.join(image_dir, filename), "wb")
            fp.write(image.read())
            fp.close()


print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 20")

post_html = """
</body>
</html>
"""

domain = "{}://{}".format(
    urllib.parse.urlparse(url).scheme, urllib.parse.urlparse(url).hostname
)
print("domain : ", domain)

html_data = get_html_data1(url)
soup = BeautifulSoup(html_data.text, "html.parser")

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

all_links = soup.find_all(["a", "img"])  # 多重取得 全部 <xx></xx>

carousel_part1 = ""
carousel_part2 = ""
picno = 0

for link in all_links:
    src = link.get("src")
    href = link.get("href")
    targets = [src, href]
    for t in targets:
        if t != None and (".jpg" in t or ".png" in t):
            if t.startswith("http"):
                full_path = t
            else:
                full_path = domain + t
            print(full_path)
            image_dir = url.split("/")[-1]
            if not os.path.exists(image_dir):
                os.mkdir(image_dir)
            filename = full_path.split("/")[-1]
            ext = filename.split(".")[-1]
            filename = filename.split(".")[-2]
            if "jpg" in ext:
                filename = filename + ".jpg"
            else:
                filename = filename + ".png"
            image = urlopen(full_path)
            fp = open(os.path.join(image_dir, filename), "wb")
            fp.write(image.read())
            fp.close()

            if picno == 0:
                carousel_part1 += "<li data-target='#myC' data-slide-to='{}' class='active'></li>".format(
                    picno
                )
                carousel_part2 += """
                    <div class='item active'>
                        <img src='{}' alt='{}'>  
                    </div>""".format(
                    filename, filename
                )

            else:
                carousel_part1 += (
                    "<li data-target='#myC' data-slide-to='{}'></li>".format(picno)
                )
                carousel_part2 += """
                    <div class='item'>
                        <img src='{}' alt='{}'>  
                    </div>""".format(
                    filename, filename
                )
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
            """.format(
                carousel_part1, carousel_part2
            )

"""
fp = open('index.html', 'w')
fp.write(pre_html+html_body+post_html)
fp.close()            
"""

print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 21")

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


url = "http://www.pythonscraping.com/exercises/exercise1.html"
title = getTitle(url)
if title == None:
    print("找不到網頁標題")
else:
    print("取得網頁標題:")
    print(title)

print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 22")

url = "https://www.mvdis.gov.tw/m3-emv-plate/webpickno/queryPickNo#"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
captcha_image = soup.find("img", id="pickimg")["src"]
csrf_token = soup.find_all("input", type="hidden")
image_url = urllib.parse.urljoin("https://www.mvdis.gov.tw/", captcha_image)
print(image_url)

# 驗證碼 = 0123456789
captcha = "0123456789"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
    "Cookie": "DWRSESSIONID=qNiI6i9UPxr4DV2G7PrFV8pkahn; _ga=GA1.3.1352658715.1598224971; BSESSIONID1=D106D274717EDF2C4EFDD9D698E61581.tsb22; _gid=GA1.3.615895194.1598974412; JSESSIONID1=B71AEB3133E436EA9619A6F6F3CDA2EA.tsp12",
}
data = {
    "method": "qryPickNo",
    "selDeptCode": "2",
    "selStationCode": "30",
    "selWindowNo": "01",
    "selCarType": "M",
    "selEnergyType": "C",
    "selPlateType": "F",
    "plateVer": "2",
    "validateStr": str(captcha),
    "queryType": 0,
    "queryNo": "*",
    "CSRFToken": str(csrf_token[2]["value"]),
}

html = requests.post(
    "https://www.mvdis.gov.tw/m3-emv-plate/webpickno/queryPickNo",
    data=data,
    headers=headers,
).text
soup = BeautifulSoup(html, "html.parser")
plate_numbers = soup.find_all("a", "number")
print(plate_numbers)

for plate_number in plate_numbers:
    print("aaaaaaaaaaaaaa")
    print(plate_number.text)

print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 23")

# Python 測試 BeautifulSoup Yahoo電影 台北票房榜

import ssl
from urllib import request, parse

# urlopen https時需要驗證一次SSL證書，
# 當網站目標使用自簽名的證書時就會跳出錯誤
# 使用SSL module把證書驗證改成不需要驗證
# context = ssl._create_unverified_context()

url = "https://movies.yahoo.com.tw/chart.html"
req_obj = request.Request(url)

""" 有問題
#with request.urlopen(req_obj,context=context) as res_obj:
with request.urlopen(req_obj) as res_obj:
    html_data = res_obj.read()
    html_data = html_data.decode('utf-8')
    print(html_data)
    soup = BeautifulSoup(html_data, 'html.parser')
    
    rows = soup.find_all('div', class_ = 'tr')

    colname = list(rows.pop(0).stripped_strings)
    contents = []
    for row in rows:
        thisweek_rank = row.find_next('div' , attrs={'class' : 'td'})
        updown = thisweek_rank.find_next('div')
        lastweek_rank = updown.find_next('div')

        if thisweek_rank.string == str(1):
            movie_title = lastweek_rank.find_next('h2')
        else:
            movie_title = lastweek_rank.find_next('div' , attrs={'class' : 'rank_txt'})

        release_date = movie_title.find_next('div' , attrs={'class' : 'td'})
        trailer = release_date.find_next('div' , attrs={'class' : 'td'})

        if trailer.find('a') is None:
            trailer_address = ''
        else:
            trailer_address = trailer.find('a')['href']

        starts = row.find('h6' , attrs={'class' : 'count'})
        lastweek_rank = lastweek_rank.string if lastweek_rank.string else ''

        c = [thisweek_rank.string , lastweek_rank , movie_title.string , release_date.string , trailer_address , starts.string]
        print('加入: ', c)
        contents.append(c)

print(contents)
"""

print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 2")

filename = "C:/_git/vcs/_1.data/______test_files2/kkbox_songs.csv"

# KKBOX華語新歌日榜
url = "https://kma.kkbox.com/charts/api/v1/daily?category=390&lang=tc&limit=50&terr=tw&type=newrelease"

# 取得歌曲資訊json檔
response = requests.get(url)
# print(response.status_code)
# print(response.text)

# 將json字串轉為Python的字典型態
data = json.loads(response.text)
song_list = data["data"]["charts"]["newrelease"]

# 印10筆資料就好
cnt = 0
with open(filename, "w", newline="", encoding="big5") as csvfile:
    # 建立 CSV 檔寫入器
    writer = csv.writer(csvfile)
    # 寫入一列資料
    writer.writerow(["排名", "歌名", "作者", "發行日期", "連結"])
    # 取得每首歌的排名、曲名、連結、作者、時間
    for song in song_list:
        song_rank = song["rankings"]["this_period"]
        song_name = song["song_name"]
        song_url = song["song_url"]
        song_artist = song["artist_name"]
        song_timestamp = int(song["release_date"])
        # 從timestamp轉為日期格式
        song_date = time.strftime("%Y-%m-%d", time.localtime(song_timestamp))

        print("排名:", song_rank)
        print("歌名:", song_name)
        print("作者:", song_artist)
        print("發行日期:", song_date)
        print("連結:", song_url)

        writer.writerow(
            [song_rank, song_name, song_artist.encode("utf-8"), song_date, song_url]
        )

        # # 從歌曲連結取得歌詞
        # song_response = requests.get(song_url)
        # soup = BeautifulSoup(song_response.text, "html.parser")
        # lyric = soup.find("div", class_="lyrics").text
        # print("歌詞:", lyric)

        print("-" * 30)
        cnt += 1
        if cnt == 10:
            break

print("將資料寫入檔案 : " + filename)
print("OK")

print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 3")

# Python 測試 BeautifulSoup 好樂迪 K歌排行
import ssl
from urllib import request, parse
import pandas as pd

# urlopen https時需要驗證一次SSL證書，
# 當網站目標使用自簽名的證書時就會跳出錯誤
# 使用SSL module把證書驗證改成不需要驗證
# context = ssl._create_unverified_context()
# 使用 ssl 模組，避免遇到 CERTIFICATE_VERIFY_FAILED 錯誤
context = ssl._create_unverified_context()

# 給好樂迪的網址建立 Request
url = "https://www.holiday.com.tw/SongInfo/SongList.aspx"
req_obj = request.Request(url)

""" 有問題
song_list = []
# 發送 request
with request.urlopen(req_obj,context=context) as res_obj:
       # 將 response 讀回並用 utf8 decode 
	resp = res_obj.read().decode('utf-8')
        # 使用 html.parser
	soup = BeautifulSoup(resp , 'html.parser')
        # 用 find 找到 id 為 ctl00_ContentPlaceHolder1_dgSong 的 table 標籤，並回傳 table 內所有的 tr 內容
	rank_table = soup.find('table',id='ctl00_ContentPlaceHolder1_dgSong').find_all('tr')

        #由於要避開 table 的第一列 tr 資料以及最後一列 tr 資料，所以取 [1:-2] 
	for rt in rank_table[1:-2]:
               # 找到所有的 td 並取得第 5 個 td(index 是 4)
		song_name = rt.find_all('td')[4]
               # 找到第一個 a 這個標籤，因為只有歌手的資料被 a tag 包住
		singer = rt.find('a')
        # 把歌曲跟歌手的資料轉成 string 並去前後空白塞到一個 song_list
	song_list.append([song_name.string.strip(),singer.string.strip()])

# 把 song_list 使用 pandas 模組轉成 dataframe 用於後面資料分析
df = pd.DataFrame(song_list,columns=['song','singer'])
print(df)
"""

print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 4")

"""
參考 https://ithelp.ithome.com.tw/articles/10186119
BeautifulSoup 套件 是 Python 上的 網頁解析工具
requests 套件允許我們發送與接收有機及草飼的 HTTP/1.1 請求（這真的是美式幽默。）
"""

import numpy as np
import pandas as pd

url = "https://www.ptt.cc/bbs/NBA/index.html"  # PTT NBA 板

print("01. 印出網頁資料")
response = requests.get(url)  # 用 requests 的 get 方法把網頁抓下來
html_doc = response.text  # text 屬性就是 html 檔案
soup = BeautifulSoup(response.text, "lxml")  # 指定 lxml 作為解析器

print("02. 一些 BeautifulSoup 的屬性或方法")
response = requests.get(url)  # 用 requests 的 get 方法把網頁抓下來
html_doc = response.text  # text 屬性就是 html 檔案
soup = BeautifulSoup(response.text, "lxml")  # 指定 lxml 作為解析器
# 一些屬性或方法

print("取得 第一個 <a></a>: ", soup.a)
print("取得 全部 <a></a>: ", soup.find_all("a"))

# Beautiful Soup 幫我們將 html 檔案轉換為 bs4 的物件，像是標籤（Tag），
# 標籤中的內容（NavigableString）與 BeautifulSoup 物件本身。

print("03.")
response = requests.get(url)  # 用 requests 的 get 方法把網頁抓下來
html_doc = response.text  # text 屬性就是 html 檔案
soup = BeautifulSoup(response.text, "lxml")  # 指定 lxml 作為解析器

print(type(soup.a))
print("---")
print(soup.a.name)  # 抓標籤名 a
print("---")
print(soup.a["id"])  # 抓<a></a>的 id 名稱

print("04. 標籤中的內容（NavigableString）")

response = requests.get(url)  # 用 requests 的 get 方法把網頁抓下來
html_doc = response.text  # text 屬性就是 html 檔案
soup = BeautifulSoup(response.text, "lxml")  # 指定 lxml 作為解析器

print(type(soup.a.string))
print("---")
soup.a.string

print("05. BeautifulSoup")

response = requests.get(url)  # 用 requests 的 get 方法把網頁抓下來
html_doc = response.text  # text 屬性就是 html 檔案
soup = BeautifulSoup(response.text, "lxml")  # 指定 lxml 作為解析器

print("06. 爬樹")

# DOM（Document Object Model）的樹狀結構觀念在使用 BeautifulSoup 扮演至關重要的角色，所以我們也要練習爬樹。
print("06a. 往下爬")
# 從標籤中回傳更多資訊。

response = requests.get(url)  # 用 requests 的 get 方法把網頁抓下來
html_doc = response.text  # text 屬性就是 html 檔案
soup = BeautifulSoup(response.text, "lxml")  # 指定 lxml 作為解析器

print(soup.body.a.contents)
print(list(soup.body.a.children))
print(soup.body.a.string)

print("06b. 往上爬")
# 回傳上一階層的標籤。

response = requests.get(url)  # 用 requests 的 get 方法把網頁抓下來
html_doc = response.text  # text 屬性就是 html 檔案
soup = BeautifulSoup(response.text, "lxml")  # 指定 lxml 作為解析器

print("06c. 往旁邊爬")
# 回傳同一階層的標籤。

response = requests.get(url)  # 用 requests 的 get 方法把網頁抓下來
html_doc = response.text  # text 屬性就是 html 檔案
soup = BeautifulSoup(response.text, "lxml")  # 指定 lxml 作為解析器

first_a_tag = soup.body.a
next_to_first_a_tag = first_a_tag.next_sibling
print(first_a_tag)
print("---")
print(next_to_first_a_tag)
print("---")
print(next_to_first_a_tag.previous_sibling)

print("07a. 搜尋")
# 這是我們主要使用 BeautifulSoup 套件來做網站解析的方法。
# find() 方法
# find_all() 方法

response = requests.get(url)  # 用 requests 的 get 方法把網頁抓下來
html_doc = response.text  # text 屬性就是 html 檔案
soup = BeautifulSoup(response.text, "lxml")  # 指定 lxml 作為解析器

print(soup.find("a"))  # 第一個 <a></a>
print("---")
print("取得 全部 <a></a>: ", soup.find_all("a"))

print("07b. 可以在第二個參數 class_= 加入 CSS 的類別。")

response = requests.get(url)  # 用 requests 的 get 方法把網頁抓下來
html_doc = response.text  # text 屬性就是 html 檔案
soup = BeautifulSoup(response.text, "lxml")  # 指定 lxml 作為解析器

print(soup.find("div", class_="r-ent"))

print("08.")
# BeautifulSoup 牛刀小試

"""
大略照著官方文件練習了前面的內容之後，我們參考Tutorial of PTT crawler來應用 BeautifulSoup 把 PTT NBA 版首頁資訊包含推文數，作者 id，文章標題與發文日期搜集下來。
我們需要的資訊都放在 CSS 類別為 r-ent 的 <div></div> 中。
"""

response = requests.get(url)
html_doc = response.text  # text 屬性就是 html 檔案
soup = BeautifulSoup(response.text, "lxml")  # 指定 lxml 作為解析器

posts = soup.find_all("div", class_="r-ent")
print(posts)
type(posts)


# 注意這個 posts 物件是一個 ResultSet，一般我們使用迴圈將裡面的每一個元素再抓出來，先練習一下作者 id。

print("09.")

response = requests.get(url)
html_doc = response.text  # text 屬性就是 html 檔案
soup = BeautifulSoup(response.text, "lxml")  # 指定 lxml 作為解析器

author_ids = []  # 建立一個空的 list 來放置作者 id
posts = soup.find_all("div", class_="r-ent")
for post in posts:
    author_ids.extend(post.find("div", class_="author"))

print(author_ids)

print("10. #接下來我們把推文數，文章標題與發文日期一起寫進去。")

response = requests.get(url)
html_doc = response.text  # text 屬性就是 html 檔案
soup = BeautifulSoup(response.text, "lxml")  # 指定 lxml 作為解析器

author_ids = []  # 建立一個空的 list 來放作者 id
recommends = []  # 建立一個空的 list 來放推文數
post_titles = []  # 建立一個空的 list 來放文章標題
post_dates = []  # 建立一個空的 list 來放發文日期

posts = soup.find_all("div", class_="r-ent")
for post in posts:
    try:
        author_ids.append(post.find("div", class_="author").string)
    except:
        author_ids.append(np.nan)
    try:
        post_titles.append(post.find("a").string)
    except:
        post_titles.append(np.nan)
    try:
        post_dates.append(post.find("div", class_="date").string)
    except:
        post_dates.append(np.nan)

# 推文數藏在 div 裡面的 span 所以分開處理
recommendations = soup.find_all("div", class_="nrec")
for recommendation in recommendations:
    try:
        recommends.append(int(recommendation.find("span").string))
    except:
        recommends.append(np.nan)

print(author_ids)
print(recommends)
print(post_titles)
print(post_dates)

print("11. ")
# 檢查結果都沒有問題之後，那我們就可以把這幾個 list 放進 dictionary 接著轉換成 data frame 了。

response = requests.get(url)
html_doc = response.text  # text 屬性就是 html 檔案
soup = BeautifulSoup(response.text, "lxml")  # 指定 lxml 作為解析器

author_ids = []  # 建立一個空的 list 來放作者 id
recommends = []  # 建立一個空的 list 來放推文數
post_titles = []  # 建立一個空的 list 來放文章標題
post_dates = []  # 建立一個空的 list 來放發文日期

posts = soup.find_all("div", class_="r-ent")
for post in posts:
    try:
        author_ids.append(post.find("div", class_="author").string)
    except:
        author_ids.append(np.nan)
    try:
        post_titles.append(post.find("a").string)
    except:
        post_titles.append(np.nan)
    try:
        post_dates.append(post.find("div", class_="date").string)
    except:
        post_dates.append(np.nan)

# 推文數藏在 div 裡面的 span 所以分開處理
recommendations = soup.find_all("div", class_="nrec")
for recommendation in recommendations:
    try:
        recommends.append(int(recommendation.find("span").string))
    except:
        recommends.append(np.nan)

ptt_nba_dict = {
    "author": author_ids,
    "recommends": recommends,
    "title": post_titles,
    "date": post_dates,
}

ptt_nba_df = pd.DataFrame(ptt_nba_dict)
ptt_nba_df

""" old

print('BeautifulSoup 測試 4')

url = "https://www.ptt.cc/bbs/NBA/index.html" # PTT NBA 板
response = requests.get(url) # 用 requests 的 get 方法把網頁抓下來
html_doc = response.text # text 屬性就是 html 檔案
soup = BeautifulSoup(response.text, "lxml") # 指定 lxml 作為解析器

print(soup.a) # 把第一個 <a></a> 抓出來
print(soup.find_all('a')) # 把所有的 <a></a> 抓出來
"""

print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 5a")

# 文淵閣工作室官網
url = "http://www.e-happy.com.tw"
html = requests.get(url)
html.encoding = "utf-8"
# print(html.text)   #many

print("BeautifulSoup 測試 5b")
# 文淵閣工作室官網
url = "http://www.e-happy.com.tw"
html = requests.get(url)
html.encoding = "utf-8"

htmllist = html.text.splitlines()  # 將網頁資料一行一行地分割成串列
""" many
for row in htmllist:
   print(row)
"""

print("BeautifulSoup 測試 5c")

# 文淵閣工作室官網
url = "http://www.e-happy.com.tw"
html = requests.get(url)
html.encoding = "utf-8"

soup = BeautifulSoup(html.text, "html.parser")

all_links = soup.find_all("a")  # 取得 全部 <a></a>
for link in all_links:
    href = link.get("href")  # 讀取 href 屬性內容
    # 判斷內容是否為非 None，並且開頭文字是 http://
    if href != None and href.startswith("http://"):
        print(href)


print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 6")


def get_html_data1(url):
    print("取得網頁資料: ", url)
    resp = requests.get(url)
    # 檢查 HTTP 回應碼是否為 requests.codes.ok(200)
    if resp.status_code != requests.codes.ok:
        print("讀取網頁資料錯誤, url: ", resp.url)
        return None
    else:
        return resp


print("BeautifulSoup 測試 7")

# url = 'https://pornav.co/'
url = "https://www.deviantart.com/"

html_data = get_html_data1(url)
if html_data:
    soup = BeautifulSoup(html_data.text, "html.parser")
    print("取得網頁標題", soup.title)
    print("搜尋網頁中的 jpg圖片連結")
    """ many
        regex = re.compile('.*\.jpg')
        imglist = soup.find_all("img", {"src":regex})
        for img in imglist:
            print(img["src"])
        """

else:
    print("無法取得網頁資料")

print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 8")

# 某圖庫網站
url = "https://www.dreamstime.com/free-images_pg1"

html = requests.get(url)
html.encoding = "utf-8"

soup = BeautifulSoup(html.text, "html.parser")

# 建立 images 目錄儲存圖片
images_dir = "images/"
if not os.path.exists(images_dir):
    os.mkdir(images_dir)

all_links = soup.find_all(["a", "img"])  # 多重取得 全部 <xx></xx>

for link in all_links:
    # 讀取 src 和　href 屬性內容
    src = link.get("src")
    href = link.get("href")
    attrs = [src, href]
    for attr in attrs:
        # 讀取　.jpg 和　.png 檔
        if attr != None and (".jpg" in attr or ".png" in attr):
            # 設定圖檔完整路徑
            full_path = attr
            filename = full_path.split("/")[-1]  # 取得圖檔名
            print(full_path)
            # 儲存圖片
            try:
                image = urlopen(full_path)
                f = open(os.path.join(images_dir, filename), "wb")
                f.write(image.read())
                f.close()
            except:
                print("{} 無法讀取!".format(filename))

print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 9")

print("台灣英文新聞網")

news_title = ""
news_content = ""
filename = "tmp_engnews.txt"

url = "https://www.taiwannews.com.tw/en/news/3610689"
url = "https://www.taiwannews.com.tw/en/news/4966193"
html = requests.get(url).text
# print(html)
soup = BeautifulSoup(html, "html.parser")  # 解析原始碼
title = soup.find("h1", class_="article-title")
article = soup.find("article", class_="container-fluid article")
news_title = title.text
news_content = article.text
with open(filename, "w", encoding="utf-8") as f:
    f.write(news_title + "\n")
    f.write(news_content)

print("標題")
print(news_title)
print("內容")
print(news_content)

print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 10")

print("中央通訊社新聞")

""" 被禁止機器抓取
news_title = ""
news_content = ""
filename = "tmp_cna_news.txt"

#url = 'https://www.cna.com.tw/news/aopl/201901050192.aspx'
url = 'https://www.cna.com.tw/news/ait/202308280292.aspx'   #繼探月成功後 印度又將發射太陽探測器
html = requests.get(url).text
print(html)
soup = BeautifulSoup(html, "html.parser")  # 解析原始碼
title = soup.find("title")
print(title)
article = soup.find("div", class_ = "paragraph")
news_title = title.text.strip()
print(news_title)
news_content = article.text
with open(filename, "w", encoding = "utf-8") as f:
    f.write(news_title + "\n")
    f.write(news_content)

print('標題')
print(news_title)
print('內容')
print(news_content)
"""

print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 11")

print("抓取網頁 分析 1")
url = "http://aiworker2000.pixnet.net/blog/post/16062839"
html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")
print(dir(soup))

print("------------------------------------------------------------")  # 60個

print("抓取網頁 分析 2")
url = "http://aiworker2000.pixnet.net/blog/post/16062839"
html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")
images = soup.find_all("img")  # 取得 全部 <img></img>
for image in images:
    print(image["src"])

print("------------------------------------------------------------")  # 60個

print("抓取網頁 分析 3")
"""
from os.path import basename

url = "http://aiworker2000.pixnet.net/blog/post/16062839"
html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")
images = soup.find_all("img")  # 取得 全部 <img></img>
if not os.path.exists("tmp_download_files"):
    os.mkdir("tmp_download_files")
for image in images:
    image_url = image["src"]
    if ".jpg" in image_url:
        image_filename = basename(image_url)
        with open(os.path.join("tmp_download_files", image_filename), "wb") as fp:
            image_data = urllib.request.urlopen(image_url).read()
            fp.write(image_data)
        print(image_url)
        print(image_filename)
"""

print("------------------------------------------------------------")  # 60個

""" fail

print('抓取網頁 分析 8')

#教育部全球資訊網-即時新聞
url = "https://www.edu.tw/News.aspx?n=9E7AC85F1954DDA8&sms=169B8E91BB75571F"
html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")
table = soup.find("table")
for row in soup.find_all("tr"):  # 取得 全部 <td></td>
    cells = row.find_all("td")  # 取得 全部 <td></td>
    for cell in cells:
        a = cell.find("a")
        if a is not None:
            print(a.text)
"""
print("------------------------------------------------------------")  # 60個

print("抓取網頁 分析 9")

# 教育部全球資訊網-即時新聞
url = "https://www.edu.tw/News.aspx?n=9E7AC85F1954DDA8&sms=169B8E91BB75571F"
html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")
table = soup.find("table")
headlines = list()
for row in soup.find_all("tr"):  # 取得 全部 <td></td>
    cells = row.find_all("td")  # 取得 全部 <td></td>
    for cell in cells:
        a = cell.find("a")
        if a is not None and a.text != "下一頁":
            headlines.append(a.text)
news = "\n".join(headlines)
with open("tmp_教育部全球資訊網即時新聞.txt", "wt", encoding="utf-8") as fp:
    fp.write(news)
print("Done!")

print("------------------------------------------------------------")  # 60個

print("抓取網頁 分析 10")

import dominate
from dominate.tags import *
from dominate.util import raw
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
    images = soup.find_all("img")  # 取得 全部 <img></img>
    if not os.path.exists("tmp_download_files"):
        os.mkdir("tmp_download_files")
    for image in images:
        image_url = image["src"]
        if ".jpg" in image_url:
            image_filename = basename(image_url)
            image_link = a(href=image_filename)
            image_link += img(src=image_filename, width=200)
            with open(os.path.join("tmp_download_files", image_filename), "wb") as fp:
                image_data = urllib.request.urlopen(image_url).read()
                fp.write(image_data)
with open(
    os.path.join("tmp_download_files", "index.html"), "wt", encoding="utf-8"
) as fp:
    fp.write(str(index_html))

print("Done!")
"""
print('------------------------------------------------------------')	#60個

"""
print("抓取網頁 分析 11")
url = "https://tw.appledaily.com/new/realtime/"
html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")
headlines = soup.find("ul", {"class": "rtddd slvl"})
items = headlines.find_all("li")  # 取得 全部 <li></li>
for item in items:
    print(item.find("h1").text)
    print(item.find("a")["href"])
    print()

print("------------------------------------------------------------")  # 60個

print("抓取網頁 分析 12")

url = "https://tw.appledaily.com/new/realtime/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
headlines = soup.find("ul", {"class": "rtddd slvl"})
items = headlines.find_all("li")  # 取得 全部 <li></li>
for item in items:
    time.sleep(random.randint(0, 2))
    content_url = item.find("a")["href"]
    print(content_url)
    response = requests.get(content_url)
    soup = BeautifulSoup(response.text, "lxml")
    title = soup.find("h1")
    print(title.text)
    article = soup.find("article", {"class": "ndArticle_content clearmen"})
    print(article.find("p").text)

print("------------------------------------------------------------")  # 60個

"""
print('抓取網頁 分析 13')

url = "https://www.ptt.cc/bbs/gossiping/index.html"

cookies = {"over18": "1"}
response = requests.get(url=url, cookies=cookies)
html = response.text

soup = BeautifulSoup(html, "lxml")
titles = soup.find_all('div', class_='title')
for title in titles:
    print(title.a.text)

"""
print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 12")

url = "https://www.mobile01.com/topiclist.php?f=751"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
}
html = requests.get(url, headers=headers).text

soup = BeautifulSoup(html, "html.parser")
pages = soup.find_all("a", class_="c-pagination")
print(pages[-1].text)

titles = soup.find_all("div", class_="c-listTableTd__title")
print(len(titles))
for title in titles:
    print(title)
    print(title.a.text)
    print(title.a["href"])

print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 13")

url = "https://www.mobile01.com/topiclist.php?f=751"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")
pages = soup.find_all("a", class_="c-pagination")
last_page = int(pages[-1].text)
url_pattern = "https://www.mobile01.com/topiclist.php?f=751&p={}"
for page in range(1, last_page + 1):
    current_url = url_pattern.format(page)
    response = requests.get(current_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    titles = soup.find_all("div", class_="c-listTableTd__title")
    for title in titles:
        print(title.a.text)
        print(title.a["href"])
    time.sleep(3)

print("------------------------------------------------------------")  # 60個

url = "https://www.mobile01.com/topiclist.php?f=751"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

pages = soup.find_all("a", class_="c-pagination")

print("本討論區的最後一頁是：", end="")
print(pages[-1].text)

print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 14")

url = "http://www.powenko.com/wordpress/"
response = requests.get(url)
print(response.text.encode("utf-8"))
soup = BeautifulSoup(response.text.encode("utf-8"), "html.parser")
print("取得 第一個 p: ", soup.p)
print(soup.a)
print("取得 全部 <a></a>: ", soup.find_all("a"))

print("------------------------------------------------------------")  # 60個

url = "http://www.powenko.com/wordpress"
response = requests.get(url)
soup = BeautifulSoup(response.text.encode("utf-8"), "html.parser")
largefeaturepowenA2 = soup.select(".largefeaturepowenA2")
largefeature0 = largefeaturepowenA2[0]
for area in largefeature0.select(".area"):
    # print(area.select('a')[1].text)
    t1 = area.select("a")
    print(area.select("a")[1].contents[0])

print("------------------------------------------------------------")  # 60個

url = "http://news.baidu.com/tech"
response = requests.get(url)
soup = BeautifulSoup(response.text.encode("utf-8"), "html.parser")
largefeaturepowenA2 = soup.select(".fb-list")
largefeature0 = largefeaturepowenA2[0]
print(largefeature0)
for area in largefeature0.select("li"):
    t1 = area.select("a")
    print(area.select("a")[0].contents[0])

print("------------------------------------------------------------")  # 60個

url = "https://feebee.com.tw/s/?q=raspberry+pi+3"
response = requests.get(url)
soup = BeautifulSoup(response.text.encode("utf-8"), "html.parser")

for line in soup.select(".items"):
    print(line.select(".large")[0].text)
    print(line.select(".ellipsis")[0].text)
    print(line.select("a")[0].get("href"))

print("------------------------------------------------------------")  # 60個

url = "https://www.chinatimes.com/?chdtv"
response = requests.get(url)
soup = BeautifulSoup(response.text.encode("utf-8"), "html.parser")

for listRight in soup.select(".focus-news"):
    for line in listRight.select(".title"):
        print(line.select("a")[0].text)

print("------------------------------------------------------------")  # 60個

url = "https://goodinfo.tw/StockInfo/StockDividendSchedule.asp?STOCK_ID=2892"
response = requests.get(url)
soup = BeautifulSoup(response.text.encode("utf-8"), "html.parser")

for listRight in soup.select(".focus-news"):
    for line in listRight.select(".title"):
        print(line.select("a")[0].text)

print("------------------------------------------------------------")  # 60個

url = "https://deepmind.com.tw"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

print("------------------------------------------------------------")  # 60個

url = "http://www.xzw.com/fortune/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")  # 取得物件
constellation = soup.find("div", id="list")
cons = constellation.find("div", "alb").find_all("div")  # 取得 全部 <div></div>

pict_url = "http://www.xzw.com"
photos = []
for con in cons:
    pict = con.a.img["src"]
    photos.append(pict_url + pict)

destDir = "tmp_dir"
if os.path.exists(destDir) == False:  # 如果沒有此資料夾就建立
    os.mkdir(destDir)
print("搜尋到的圖片數量 = ", len(photos))  # 列出搜尋到的圖片數量
for photo in photos:  # 迴圈下載圖片與儲存
    picture = requests.get(photo)  # 下載圖片
    picture.raise_for_status()  # 如果發生錯誤的話, 會丟出 exception
    print("%s 圖片下載成功" % photo)
    # 先開啟檔案, 再儲存圖片
    pictFile = open(os.path.join(destDir, os.path.basename(photo)), "wb")
    for diskStorage in picture.iter_content(10240):
        pictFile.write(diskStorage)
    pictFile.close()  # 關閉檔案

print("------------------------------------------------------------")  # 60個

soup = BeautifulSoup("<html> Lollipop </html>", "html.parser")

print("------------------------------------------------------------")  # 60個

url = "https://tw.news.yahoo.com/rss/technology"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
soup.findAll("item")

for news in soup.findAll("item"):
    print(news.title)

print("------------------------------------------------------------")  # 60個

url = "https://acg.gamer.com.tw/billboard.php?t=2&p=Android"
response = requests.get(url)
response.encoding = "UTF-8"
soup = BeautifulSoup(response.text, "html.parser")
soup.find(class_="ACG-mainbox1").find(class_="ACG-maintitle").find("a").string

for game in soup.findAll(class_="ACG-mainbox1"):
    print(
        game.find(class_="ACG-mainumber").string
        + " "
        + game.find(class_="ACG-maintitle").find("a").string
    )

print("------------------------------------------------------------")  # 60個

url = "https://fchart.github.io/Elements.html"
response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")

tag = soup.select_one("h2")
print("h2: ", tag.text)

tags = soup.select("b")
print("b: ", tags[0].text)

tag = soup.select_one("#q2")
tag2 = tag.select_one("b")
print("b: ", tag2.text)

tags = soup.select(".response")
print("li: ", tags[0].text)
print("li: ", tags[1].text)

print("------------------------------------------------------------")  # 60個

url = "https://fchart.github.io/Elements.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

tag = soup.find("h2")
print("h2: ", tag.text)

tag = soup.find("b")
print("b: ", tag.text)

tags = soup.find_all("b")  # 取得 全部 <b></b>
print("b: ", tags[0].text)

tag = soup.find("li", {"id": "q2"})
tag_q = tag.find("b")
print("Question: ", tag_q.text)

tags_a = tag.find_all("li", {"class": "response"})
for tag in tags_a:
    print("Ans: ", tag.text)

print("------------------------------------------------------------")  # 60個

url = "https://fchart.github.io/Elements.html"
response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")

tag = soup.find("h2")
print("h2: ", tag.text)

tag = soup.find("b")
print("b: ", tag.text)

tags = soup.find_all("b")  # 取得 全部 <b></b>
print("b: ", tags[0].text)

tag = soup.find("li", {"id": "q2"})
tag_q = tag.find("b")
print("Question: ", tag_q.text)

tags_a = tag.find_all("li", class_="response")
for tag in tags_a:
    print("Ans: ", tag.text)

print("------------------------------------------------------------")  # 60個

url = "https://fchart.github.io/Elements.html"

response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
tags_li = soup.find_all("li", class_="response", limit=3)
print(tags_li)

print("------------------------------------------------------------")  # 60個

url = "https://fchart.github.io/Elements.html"

response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")

tag_ans1 = soup.find("li", class_="response")
print(tag_ans1.text)

tag_ans2 = tag_ans1.find_next()
print(tag_ans2.text)

print("------------------------------------------------------------")  # 60個

print("臺灣證交所本國上市證券")
# 查詢台灣證交所本國上市證券國際證券辨識號碼一覽表

import pandas as pd

df = pd.read_html(
    "http://isin.twse.com.tw/isin/C_public.jsp?strMode=2",
    encoding="big5hkscs",
    header=0,
)
newdf = df[0][df[0]["產業別"] > "0"]  # 產業別資料大於0
# del newdf['國際證券辨識號碼(ISIN Code)'],newdf['CFICode'],newdf['備註']
del newdf["CFICode"], newdf["備註"]  # 刪除兩個不需要欄位
df2 = newdf["有價證券代號及名稱"].str.split(" ", expand=True)  # 分成兩個欄位回存
df2 = df2.reset_index(drop=True)  # 重設索引值
newdf = newdf.reset_index(drop=True)  # 重設索引值
for i in df2.index:
    if " " in df2.iat[i, 0]:  # 將有價證券代號及名稱
        df2.iat[i, 1] = df2.iat[i, 0].split(" ")[1]  # 欄位資料內容分割為2，回存df2物件中。
        df2.iat[i, 0] = df2.iat[i, 0].split(" ")[0]  # 回存df2物件中。
newdf = df2.join(newdf)  # 將df2合併到newdf物件
newdf = newdf.rename(columns={0: "股票代號", 1: "股票名稱"})  # 修改欄位名稱
del newdf["有價證券代號及名稱"]  # 將"有價證券代號及名稱"欄位刪除

filename = "stock_.xlsx"
newdf.to_excel(filename, sheet_name="Sheet1", index=False)  # 存入excel

print("已存檔到 : ", filename)

print("------------------------------------------------------------")  # 60個

print("將網頁上的資料存成csv檔")

print("新北市不動產仲介經紀商業同業公會網站")

file_name = "tmp_新北市仲介.csv"

f = open(file_name, "w", encoding="utf8")
w = csv.writer(f)
httphead = "http://www.tcr.org.tw/a/table_blogs/index/21654"

# 根據新北市不動產仲介經紀商業同業公會網站會員介紹首頁
# 與其後各頁差異，根據頁面規則涵蓋需要抓取頁面
# 資料抓前 N 頁
N = 3
for i in range(1, N + 1):
    print("第", i, "頁")
    if i == 1:
        htmlname = httphead
    else:
        htmlname = httphead + "?page=" + str(i)

    print(htmlname)
    html = urlopen(htmlname)

    # 以BeautifulSoup的"lxml"模式解析網頁，設定為soup物件
    soup = BeautifulSoup(html, "lxml")
    count = 0

    for single_tr in soup.find("table").find("table").findAll("tr"):  # 抓取網頁資料
        if count == 0:
            cell = single_tr.findAll("th")  # 處理表頭
            F0 = cell[0].contents
            F1 = cell[1].contents
            F2 = cell[2].contents
            F3 = cell[3].contents
            F4 = cell[4].contents
        else:
            cell = single_tr.findAll("td")  # 處理表格中資料
            # print(cell)
            F0 = cell[0].a.string
            F1 = cell[1].a.string
            F2 = cell[2].a.string
            F3 = cell[3].a.string
            F4 = cell[4].a.string
        # print(F0,F1,F2,F3,F4)
        data = [[F0, F1, F2, F3, F4]]

        if i == 1:
            w.writerows(data)  # 逐行寫入csv檔案
        elif i > 1 and count > 0:
            w.writerows(data)  # 逐行寫入csv檔案

        count = count + 1

        if count > 20:
            break

f.close()

print("------------------------------------------------------------")  # 60個

addr = "https://tw.stock.yahoo.com/s/list.php?\
c=%A8%E4%A5%A6%B9q%A4l&rr=0.84235400%201556957344"

# 取得網頁原始程式碼
res = requests.get(addr).text
# 以html.parser解析程式解析程式碼
soup = BeautifulSoup(res, "html.parser")
# 以<tr>並配合屬性取得表格中每列內容
rows = soup.find_all("tr", {"height": "30"})

# 印出要查詢資料各欄位名稱
print("代號 名稱  時間  成交  買進   賣出  漲跌   張數   昨收   開盤  最高  最低")
# 讀取每列的內容，找出<td>
for row in rows:
    if row.find("td"):
        # 屬性stripped_strings去餘每欄中字串的空白符號
        cols = [item for item in row.stripped_strings]
        # 讀取List物件的元素
        for item in range(0, len(cols)):
            print(cols[item], end=" ")
        print()  # 換行

print("------------------------------------------------------------")  # 60個

# 獲取網頁內容
url = "https://acg.gamer.com.tw/billboard.php?t=2&p=iOS"
game_ranking_html = requests.get(url)

# 使用 BeautifulSoup 解析 HTML
soup = BeautifulSoup(game_ranking_html.text, "html.parser")

# 找到所有遊戲排名標題的標籤
games = soup.find_all("div", {"class": "APP-LI-NAME"})

# 顯示遊戲排名標題
for i, game in enumerate(games, 1):
    print(f"{i}. {game.text.strip()}")

print("------------------------------------------------------------")  # 60個

# 指定url變數為「Dcard熱門文章」網頁的網址
url = "https://www.dcard.tw/f"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")  # 取得物件
# 取得所有文章程式碼
listItems = soup.find_all("article", "sc-1v1d5rx-0 lmtfq")

for item in listItems:
    time = item.find_all("span", "sc-6oxm01-2 hiTIMq")[2]  # 發文時間
    print("發文時間:", time.text)
    print("文章標題:", item.h2.text)  # 文章標題
    URl = item.find("a").get("href")  # 文章網址
    print("文章網址: https://www.dcard.tw" + URl)
    print("=" * 70)
print("取得文章數量 =", len(listItems))

print("------------------------------------------------------------")  # 60個

url = "https://www.iana.org/domains/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

print(soup.select("#logo"))  # 搜尋 id 為 logo 的 tag 內容
print("\n----------\n")

print(soup.find_all("div", id="logo"))  # 搜尋所有 id 為 logo 的 div
print("\n----------\n")

divs = soup.find_all("div")  # 取得 全部 <div></div>
print(divs[1])  # 取得搜尋到的第二個項目 ( 第一個為 divs[0] )
print("\n----------\n")

# 從搜尋到的項目裡，尋找父節點裡所有的 li
print(divs[1].find_parent().find_all("li"))  # 取得 全部 <li></li>
print("\n----------\n")

# 從搜尋到的項目裡，尋找父節點裡所有 li 的第三個項目，找到他後方同層的所有 li
print(divs[1].find_parent().find_all("li")[2].find_next_siblings())
print("\n----------\n")

# 從搜尋到的項目裡，尋找父節點裡所有 li 的第三個項目，找到他前方同層的所有 li
print(divs[1].find_parent().find_all("li")[2].find_previous_siblings())

print("------------------------------------------------------------")  # 60個

url = "https://www.iana.org/domains/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

print("取得 全部 <a></a>: ", soup.find_all("a"))
print(soup.find_all("a"))  # 等同於下方的 soup('a')
print(soup("a"))  # 等同於上方的 find_all('a')

print("------------------------------------------------------------")  # 60個

url = "https://www.iana.org/domains/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

print("取得 全部 <a></a>: ", soup.find_all("a"))
print(soup.find_all("a", string="Domains"))  # 找出內容字串為 Domains 的 a tag
print(soup("a", limit=2))  # 找出前兩個 a tag

print("------------------------------------------------------------")  # 60個

url = "https://www.iana.org/domains/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
print(soup.find("a").get_text())  # 輸出第一個 a tag 的內容
print(soup.find("a")["href"])  # 輸出第一個 a tag 的 href 屬性內容

print("------------------------------------------------------------")  # 60個

url = "https://www.ptt.cc/"
url = "https://www.ptt.cc/bbs/Gossiping/index.html"

cookies = {"over18": "1"}
response = requests.get(url=url, cookies=cookies)

soup = BeautifulSoup(response.text, "html.parser")
titles = soup.find_all("div", class_="title")  # 取得 class 為 title 的 div 內容
for i in titles:
    if i.find("a") != None:  # 判斷如果不為 None
        print(i.find("a").get_text())  # 取得 div 裡 a 的內容，使用 get_text() 取得文字
        print(url + i.find("a")["href"], end="\n\n")  # 使用 ['href'] 取得 href 的屬性

print("------------------------------------------------------------")  # 60個

url = "https://www.ptt.cc/"
url = "https://www.ptt.cc/bbs/Gossiping/index.html"

cookies = {"over18": "1"}
response = requests.get(url=url, cookies=cookies)

response.encoding = "utf-8"  # 避免中文亂碼
soup = BeautifulSoup(response.text, "html.parser")
titles = soup.find_all("div", class_="title")
output = ""  # 建立 output 變數
for i in titles:
    if i.find("a") != None:
        # 將資料一次記錄到 output 變數裡
        output = (
            output + i.find("a").get_text() + "\n" + url + i.find("a")["href"] + "\n\n"
        )
print(output)

f = open("tmp_aaaaa.txt", "w")  # 建立並開啟純文字文件
f.write(output)  # 將資料寫入檔案裡
f.close()

print("------------------------------------------------------------")  # 60個

url = "https://www.ptt.cc/bbs/Beauty/M.1638380033.A.7C7.html"

cookies = {"over18": "1"}
response = requests.get(url=url, cookies=cookies)

soup = BeautifulSoup(response.text, "html.parser")  # 使用 BeautifulSoup 取得網頁結構
imgs = soup.find_all("img")  # 取得 全部 <img></img>
for i in imgs:
    print(i["src"])  # 印出 src 的屬性

print("------------------------------------------------------------")  # 60個

url = "https://www.ptt.cc/bbs/Beauty/M.1638380033.A.7C7.html"

cookies = {"over18": "1"}
response = requests.get(url=url, cookies=cookies)

soup = BeautifulSoup(response.text, "html.parser")
imgs = soup.find_all("img")  # 取得 全部 <img></img>
name = 0  #  設定圖片編號
for i in imgs:
    print(i["src"])
    jpg = requests.get(i["src"])  # 使用 requests 讀取圖片網址，取得圖片編碼
    f = open(f"tmp_test_{name}.jpg", "wb")  # 使用 open 設定以二進位格式寫入圖片檔案
    f.write(jpg.content)  # 寫入圖片的 content
    f.close()  # 寫入完成後關閉圖片檔案
    name = name + 1  # 編號增加 1

print("------------------------------------------------------------")  # 60個

url = "https://www.ptt.cc/bbs/Beauty/M.1638380033.A.7C7.html"

cookies = {"over18": "1"}
response = requests.get(url=url, cookies=cookies)

soup = BeautifulSoup(response.text, "html.parser")
imgs = soup.find_all("img")  # 取得 全部 <img></img>
name = 0
for i in imgs:
    print(i["src"])
    jpg = requests.get(i["src"])
    f = open(f"tmp_test_{name}.jpg", "wb")
    f.write(jpg.content)
    f.close()
    name = name + 1

print("------------------------------------------------------------")  # 60個

from concurrent.futures import ThreadPoolExecutor  # 加入 concurrent.futures 內建函式庫

url = "https://www.ptt.cc/bbs/Beauty/M.1638380033.A.7C7.html"

cookies = {"over18": "1"}
response = requests.get(url=url, cookies=cookies)

soup = BeautifulSoup(response.text, "html.parser")
imgs = soup.find_all("img")  # 取得 全部 <img></img>
name = 0
urls = []  # 根據爬取的資料，建立一個圖片名稱與網址的空串列
for i in imgs:  # 修改 for 迴圈內容
    urls.append([i["src"], name])  # 將圖片網址與編號加入串列中
    name = name + 1  # 編號增加 1


def download(url):  # 編輯下載函式
    print(url)  # 印出網址
    jpg = requests.get(url[0])  # 使用 requests.get 取得圖片資訊
    f = open(f"download/test_{url[1]}.jpg", "wb")  # 將圖片開啟為二進位格式 ( 請自行修改存取路徑 )
    f.write(jpg.content)  # 存取圖片
    f.close()


executor = ThreadPoolExecutor()  # 建立非同步的多執行緒的啟動器
with ThreadPoolExecutor() as executor:
    executor.map(download, urls)  # 同時下載圖片

print("------------------------------------------------------------")  # 60個

url = "https://invoice.etax.nat.gov.tw/index.html"
response = requests.get(url)  # 取得網頁內容
response.encoding = "utf-8"  # 因為該網頁編碼為 utf-8，加上 .encoding 避免亂碼

soup = BeautifulSoup(response.text, "html.parser")  # 轉換成標籤樹
td = soup.select(".container-fluid")[0].select(".etw-tbiggest")  # 取出中獎號碼的位置
ns = td[0].getText()  # 特別獎
n1 = td[1].getText()  # 特獎
# 頭獎，因為存入串列會出現 /n 換行符，使用 [-8:] 取出最後八碼
n2 = [td[2].getText()[-8:], td[3].getText()[-8:], td[4].getText()[-8:]]
print(ns)
print(n1)
print(n2)

print("------------------------------------------------------------")  # 60個

url = "https://invoice.etax.nat.gov.tw/index.html"
response = requests.get(url)  # 取得網頁內容
response.encoding = "utf-8"  # 因為該網頁編碼為 utf-8，加上 .encoding 避免亂碼

soup = BeautifulSoup(response.text, "html.parser")  # 轉換成標籤樹
td = soup.select(".container-fluid")[0].select(".etw-tbiggest")  # 取出中獎號碼的位置
ns = td[0].getText()  # 特別獎
n1 = td[1].getText()  # 特獎
# 頭獎，因為存入串列會出現 /n 換行符，使用 [-8:] 取出最後八碼
n2 = [td[2].getText()[-8:], td[3].getText()[-8:], td[4].getText()[-8:]]

while True:
    try:
        # 對獎程式
        num = input("輸入你的發票號碼：")
        if num == ns:
            print("對中 1000 萬元！")
        if num == n1:
            print("對中 200 萬元！")
        for i in n2:
            if num == i:
                print("對中 20 萬元！")
                break
            if num[-7:] == i[-7:]:
                print("對中 4 萬元！")
                break
            if num[-6:] == i[-6:]:
                print("對中 1 萬元！")
                break
            if num[-5:] == i[-5:]:
                print("對中 4000 元！")
                break
            if num[-4:] == i[-4:]:
                print("對中 1000 元！")
                break
            if num[-3:] == i[-3:]:
                print("對中 200 元！")
                break
    except:
        break

print("------------------------------------------------------------")  # 60個

url = "https://tw.stock.yahoo.com/quote/2330"  # 台積電 Yahoo 股市網址
response = requests.get(url)  # 取得網頁內容
soup = BeautifulSoup(response.text, "html.parser")  # 轉換內容
title = soup.find("h1")  # 找到 h1 的內容
a = soup.select(".Fz(32px)")[0]  # 找到第一個 class 為 Fz(32px) 的內容
b = soup.select(".Fz(20px)")[0]  # 找到第一個 class 為 Fz(20px) 的內容
s = ""  # 漲或跌的狀態
try:
    # 如果 main-0-QuoteHeader-Proxy id 的 div 裡有 C($c-trend-down) 的 class
    # 表示狀態為下跌
    if soup.select("#main-0-QuoteHeader-Proxy")[0].select(".C($c-trend-down)")[0]:
        s = "-"
except:
    try:
        # 如果 main-0-QuoteHeader-Proxy id 的 div 裡有 C($c-trend-up) 的 class
        # 表示狀態為上漲
        if soup.select("#main-0-QuoteHeader-Proxy")[0].select(".C($c-trend-up)")[0]:
            s = "+"
    except:
        # 如果都沒有包含，表示平盤
        s = "-"

print(f"{title.get_text()} : {a.get_text()} ( {s}{b.get_text()} )")  # 印出結果

print("------------------------------------------------------------")  # 60個

from concurrent.futures import ThreadPoolExecutor

# 建立要抓取的股票網址清單
stock_urls = [
    "https://tw.stock.yahoo.com/quote/2330",
    "https://tw.stock.yahoo.com/quote/0050",
    "https://tw.stock.yahoo.com/quote/2317",
    "https://tw.stock.yahoo.com/quote/6547",
]


# 將剛剛的抓取程式變成「函式」
def getStock(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.find("h1")
    a = soup.select(".Fz(32px)")[0]
    b = soup.select(".Fz(20px)")[0]
    s = ""
    try:
        if soup.select("#main-0-QuoteHeader-Proxy")[0].select(".C($c-trend-down)")[0]:
            s = "-"
    except:
        try:
            if soup.select("#main-0-QuoteHeader-Proxy")[0].select(".C($c-trend-up)")[0]:
                s = "+"
        except:
            state = ""
    print(f"{title.get_text()} : {a.get_text()} ( {s}{b.get_text()} )")


executor = ThreadPoolExecutor()  # 建立非同步的多執行緒的啟動器
with ThreadPoolExecutor() as executor:
    executor.map(getStock, stock_urls)  # 開始同時爬取股價

print("------------------------------------------------------------")  # 60個

"""
# 馬丁路德 I have a dream
url = 'http://www.analytictech.com/mb021/mlk.htm'
page = requests.get(url)
page.raise_for_status()# 如果發生錯誤的話, 會丟出 exception
soup = BeautifulSoup(page.text, 'html.parser')
p_elems = [element.text for element in soup.find_all('p')]

speech = ' '.join(p_elems)  # 將段落內容串在一起

# 修正錯字、刪除多餘的空格、移除非字母內容
speech = speech.replace(')mowing', 'knowing')
speech = re.sub('\s+', ' ', speech) 
speech_edit = re.sub('[^a-zA-Z]', ' ', speech)
speech_edit = re.sub('\s+', ' ', speech_edit)

print(speech_edit)
"""
print("------------------------------------------------------------")  # 60個

exist_url = []
g_writecount = 0

full_url = "https://zh.wikipedia.org/wiki/%E6%8B%BF%E7%A0%B4%E4%BB%91%E4%B8%80%E4%B8%96"  # 填写你要爬取的网页


def scrappy(url, depth=1):
    global g_writecount
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
        }
        r = requests.get(full_url, headers=headers)
        html = r.text
    except Exception as e:
        print("Failed downloading and saving ", full_url)
        print(e)
        exist_url.append(full_url)
        return None

    exist_url.append(url)

    # 使用BeautifulSoup提取页面的所有文本内容
    soup = BeautifulSoup(html, "lxml")

    # 提取所有文本
    chinese_text = "".join([p.get_text() for p in soup.find_all("p")])

    # 保存中文文本到文件
    with open("tmp_chinese_txt.txt", "a+", encoding="utf-8") as f:
        f.write(chinese_text)

    link_list = re.findall('<a href="/wiki/([^:#=<>]*?)".*?</a>', html)
    unique_list = list(set(link_list) - set(exist_url))

    for eachone in unique_list:
        print("找到連結 :", eachone)
        g_writecount += 1
        output = (
            "No."
            + str(g_writecount)
            + "\t Depth:"
            + str(depth)
            + "\t"
            + full_url
            + " -> "
            + eachone
            + "\n"
        )
        # print(output)

        if depth < 1:
            time.sleep(5)  # 添加5秒的延迟
            scrappy(eachone, depth + 1)


"""     
效果：给一个网页，返回一个chinese_txt文件，
里面有爬回这个网页内所有的文字，
以及网页内所有的链接内的网页文字也会被爬到。
"""
start = time.time()

scrappy(full_url)
stop = time.time()
print("所用时间：", stop - start)


print("------------------------------------------------------------")  # 60個
print("BeautifulSoup bs4 SP")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("專項")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
# 台灣水庫即時水情 water.taiwanstat.com
print("------------------------------------------------------------")  # 60個

# 台灣水庫即時水情
url = "https://water.taiwanstat.com/"
response = requests.get(url)  # 取得網頁內容
soup = BeautifulSoup(response.text, "html.parser")  # 轉換成標籤樹
print("取得網頁標題 : ", soup.title)  # 印出整行資料 # <title>網頁標題</title>
print("取得網頁標題 : ", soup.title.text)  # 只印出text部分

print("------------------------------------------------------------")  # 60個

# 台灣水庫即時水情
url = "https://water.taiwanstat.com/"
response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")  # 使用 html.parser 解析器
soup = BeautifulSoup(response.text, "html5lib")  # 使用 html5lib 解析器
print("取得網頁標題 : ", soup.title)  # 印出整行資料 # <title>網頁標題</title>
print("取得網頁標題 : ", soup.title.text)  # 只印出text部分

print("------------------------------------------------------------")  # 60個

# 台灣水庫即時水情
url = "https://water.taiwanstat.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
reservoir = soup.select(".reservoir")  # 取得所有 class 為 reservoir 的 tag
for i in reservoir:
    print(
        i.find("div", class_="name").get_text(), end=" "
    )  # 取得內容的 class 為 name 的 div 文字
    print(i.find("h5").get_text(), end=" ")  # 取得內容 h5 tag 的文字
    print()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
# www.books.com.tw
print("------------------------------------------------------------")  # 60個

url = "https://www.books.com.tw/"  # 博客來
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")  # 傳回soup物件可解析網頁
print(soup.find("h1"))  # 傳回第一個符合<h1>資料
# 若傳回None表示該網頁沒有<h1>標籤

print("------------------------------------------------------------")  # 60個

""" ok, many
print('抓取網頁 分析 4')
#博客來-中文書>暢銷榜
url = "https://www.books.com.tw/web/sys_saletopb/books/19/?loc=P_0002_020"
html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")
images = soup.find_all("img")  # 取得 全部 <img></img>
for image in images:
    if ".jpg" in image['src'] or ".png" in image['src']:
        print(image['src'])
"""
print("------------------------------------------------------------")  # 60個

""" ok, many
print('抓取網頁 分析 5')
#博客來-中文書>暢銷榜
url = "https://www.books.com.tw/web/sys_saletopb/books/19/?loc=P_0002_020"
html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")

all_links = soup.find_all("a")  # 取得 全部 <a></a>
for link in all_links:
    if "http" in link['href']:
        print(link['href'])
"""
print("------------------------------------------------------------")  # 60個

""" ok, many
print('抓取網頁 分析 6')
#博客來-中文書>暢銷榜
url = "https://www.books.com.tw/web/sys_saletopb/books/19/?loc=P_0002_020"
html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")
titles = soup.find_all("img", {"class":"cover"})
for i, title in enumerate(titles):
    print("第{}名：{}".format(i+1, title['alt']))
"""
print("------------------------------------------------------------")  # 60個

""" fail in sugar
print('抓取網頁 分析 7 fail')
#博客來-中文書>暢銷榜
url = "https://www.books.com.tw/web/sys_saletopb/books/19/?loc=P_0002_020"
html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")
books = soup.find_all("li", {"class":"item"})
for i, book in enumerate(books):
    print("第{}名：".format(i+1), end="")
    print(book.find("img")['alt'])
    for info in book.find("ul").find_all("li"):  # 取得 全部 <li></li>
        print(info.text)
    print()
"""
print("------------------------------------------------------------")  # 60個

# 博客來寵物電子書
url = "https://www.books.com.tw/web/sys_cebbotm/cebook/1003/?loc=P_0001_2_003"

response = requests.get(url)  # 使用requests的get()方法傳回可擷取網頁資訊response物件
response.encoding = "utf-8"  # 設定編碼模式避免亂碼
# 使用BeautifulSoup()函式取得解析網頁的BeautifulSoup物件soup
soup = BeautifulSoup(response.text, "lxml")
listAll = soup.find_all("div", class_="item")  # 取得<div class="item">標籤的內容
for book in listAll:  # 將資料利用迴圈依序解析
    listClass = book.get("class")  # 傳回目前標籤的類別資訊
    if len(listClass) == 2:  # ['item', 'clearfix']總數為2，即目前有兩個類別
        if listClass[1] == "clearfix":  # 遇到clearfix類別時，跳出本次迴圈
            continue
    print((book.find("h4").find("a").text))  # 搜尋第一個<h4>內的第一個<a>標籤，即書名

print("------------------------------------------------------------")  # 60個

# 博客來寵物電子書
url = "https://www.books.com.tw/web/sys_cebbotm/cebook/1003/?loc=P_0001_2_003"

response = requests.get(url)  # 使用requests的get()方法傳回可擷取網頁資訊response物件
response.encoding = "utf-8"  # 設定編碼模式避免亂碼
# 使用BeautifulSoup()函式取得解析網頁的BeautifulSoup物件soup
soup = BeautifulSoup(response.text, "lxml")
listName = soup.select("div.item>div.msg>h4>a")  # 根據路徑擷取<a>標籤，並指定給listName串列
listPrice = soup.select("li.set2")  # 取得套用set2類別的<li>標籤，並指定給listPrice串列
for i in range(0, len(listName)):  # 使用迴圈逐一印出書名與書價
    print("%s  %s" % (listName[i].text, listPrice[i].text))

print("------------------------------------------------------------")  # 60個

# html to csv

# 博客來寵物電子書
url = "https://www.books.com.tw/web/sys_cebbotm/cebook/1003/?loc=P_0001_2_003"

# 建立取得網頁資訊的Response物件，物件名稱為response
response = requests.get(url)
# 建立解析網頁的BeautifulSoup物件，物件名稱為soup
soup = BeautifulSoup(response.text, "lxml")
# 分別取的商品名稱以及價格標籤，並指定給對應串列
listName = soup.select("div.item>div.msg>h4>a")
listPress = soup.select("li.info>span>a")
listPrice = soup.select("li.set2")

print("------------")
print(len(listName))
print("------------")
print(type(listName))
print("------------")
print(listName)
print("------------")

print("書名")
for i in range(0, len(listName) // 10):
    print(listName[i].text)

print("\n出版社")
for i in range(0, len(listName) // 10):
    print(listPress[i].text)

print("\n價格")
for i in range(0, len(listName) // 10):
    print(listPrice[i].text)
    Price = listPrice[i].text.split("：")[1].split("元")[0].split("折")[-1]
    print(Price)


# 將listName與listPirce串列的資料依序存入booklist.csv檔中
f = open("tmp_booklist.csv", "w", encoding="utf-8-sig", newline="")  # 這樣才不會多一行空白
write = csv.writer(f)
write.writerow(["書名", "出版社", "價格"])
for i in range(0, len(listName)):
    # 分析價格內容，只擷取數字部分
    Price = listPrice[i].text.split("：")[1].split("元")[0].split("折")[-1]
    # 使用text屬性，將標籤內的資料寫入csv檔中
    write.writerow([listName[i].text, listPress[i].text, Price])
    # print(listName[i].text, listPress[i].text, Price)
f.close()

print("------------------------------------------------------------")  # 60個

print("下載網站圖片")

# 抓 博客來電子寵物書 圖片

# 博客來寵物電子書
url = "https://www.books.com.tw/web/sys_cebbotm/cebook/1003/?loc=P_0001_2_003"

response = requests.get(url)  # 建立取得網頁資訊的Response物件，物件名稱為response
response.encoding = "utf-8"  # 設定編碼模式避免亂碼

# 使用BeautifulSoup()函式取得解析網頁的BeautifulSoup物件soup
soup = BeautifulSoup(response.text, "lxml")
Img = soup.select("div.item>a>img")  # 擷取有圖片網址的<img>標籤

print("共找到有圖片網址的連結 :", len(Img), "個")

cnt = 0
for link in Img:
    print("圖片連結 :", link)
    # 使用split()方法解析網址
    src = link.get("src")
    ImgUrl = src.split("=")[1].split("&")[0]
    # 網址用'/'分隔取最後一筆資料 => *.jpg
    filename = ImgUrl.split("/")[-1]
    print("圖片網址 :", ImgUrl)
    print("圖片檔名 :", filename)

    try:  # 下載圖片
        response = requests.get(ImgUrl)  # 建立下載圖片的Response物件 response
        f = open((filename), "wb")  # 開啟圖片檔案
        f.write(response.content)  # 下載圖片
        f.close()
        print(filename, "下載完畢")
    except:
        print("下載失敗")
        f.close()
    cnt += 1
    if cnt > 5:
        break

print("執行完畢")

print("------------------------------------------------------------")  # 60個
# taiwanlottery ST
print("------------------------------------------------------------")  # 60個

# 台灣彩券官網首頁
url = "http://www.taiwanlottery.com.tw/"
html = requests.get(url)

soup = BeautifulSoup(html.text, "lxml")

dataTag = soup.select(".contents_box02")  # 尋找class是contents_box02

# 找尋開出順序與大小順序的球
balls = dataTag[2].find_all("div", {"class": "ball_tx ball_yellow"})
print("開出順序 : ", end="")
for i in range(6):  # 前6球是開出順序
    print(balls[i].text, end="   ")

print("\n大小順序 : ", end="")
for i in range(6, len(balls)):  # 第7球以後是大小順序
    print(balls[i].text, end="   ")

# 找出第二區的紅球
redball = dataTag[2].find_all("div", {"class": "ball_red"})
print("\n特別號   :", redball[0].text)

print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 13")

# 台灣彩券官網首頁
url = "http://www.taiwanlottery.com.tw/"
soup = get_soup_from_url(url)

cc1 = soup.select("#rightdown")
# print(cc1)

cc = cc1[0].find("div", {"class": "contents_box02"})
# print(cc)

cc3 = cc.find_all("div", {"class": "ball_tx"})
print(cc3)

# 台灣彩券官網首頁
url = "http://www.taiwanlottery.com.tw/"
soup = get_soup_from_url(url)

cc1 = soup.select("#rightdown")
# print(cc1)

cc2 = cc1[0].find("div", {"class": "contents_box02"})
# print(cc2)

cc3 = cc2.find_all("div", {"class": "ball_tx"})
# print(cc3)
#
# 威力彩號碼
print("開出順序：", end="")
for n in range(0, 6):
    print(cc3[n].text, end="  ")

print("\n大小順序：", end="")
for n in range(6, len(cc3)):
    print(cc3[n].text, end="  ")

## 第二區
red = cc2.find("div", {"class": "ball_red"})
print("\n第二區：{}".format(red.text))

url = "http://www.taiwanlottery.com.tw"
html = requests.get(url)
print("網頁下載中 ...")
html.raise_for_status()  # 如果發生錯誤的話, 會丟出 exception
print("網頁下載完成")

soup = BeautifulSoup(html.text, "lxml")

dataTag = soup.select(".contents_box02")  # 尋找class是contents_box02
print("串列長度", len(dataTag))
for i in range(len(dataTag)):  # 列出含contents_box02的串列
    print(dataTag[i])

# 找尋開出順序與大小順序的球
balls = dataTag[0].find_all("div", {"class": "ball_tx ball_green"})
print("開出順序 : ", end="")
for i in range(6):  # 前6球是開出順序
    print(balls[i].text, end="   ")

print("\n大小順序 : ", end="")
for i in range(6, len(balls)):  # 第7球以後是大小順序
    print(balls[i].text, end="   ")

# 找出第二區的紅球
redball = dataTag[0].find_all("div", {"class": "ball_red"})
print("\n第二區   :", redball[0].text)


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
# taiwanlottery SP
print("------------------------------------------------------------")  # 60個

""" NG 無檔案 Example.html
from bs4 import BeautifulSoup

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
# 使用childen屬性取得子標籤
tag_div = soup.select("#q2") # 找到第2題
tag_ul = tag_div[0].ul       # 走訪到之下的<ul>
for child in tag_ul.children:
    print(type(child))

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup
from bs4.element import NavigableString

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
# 使用childen屬性取得子標籤
tag_div = soup.select("#q2") # 找到第2題
tag_ul = tag_div[0].ul       # 走訪到之下的<ul>
for child in tag_ul.children:
    if not isinstance(child, NavigableString):
        print(child.name)

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
# 使用屬性向下走訪
print(soup.html.head.title.string)
print(soup.html.head.meta["charset"])
# 使用div屬性取得第1個<div>標籤
print(soup.html.body.div.div.p.a.string)

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup
from bs4.element import NavigableString

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
# 使用屬性取得所有子標籤
tag_div = soup.select("#q2") # 找到第2題
tag_ul = tag_div[0].ul       # 走訪到之下的<ul>
for child in tag_ul.contents:
    if not isinstance(child, NavigableString):
        print(child.span.string)

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup
from bs4.element import NavigableString

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
# 使用屬性取得所有子標籤
tag_div = soup.select("#q2") # 找到第2題
tag_ul = tag_div[0].ul       # 走訪到之下的<ul>            
for child in tag_ul.children:
    if not isinstance(child, NavigableString):
        print(child.name)
        for tag in child:
            if not isinstance(tag, NavigableString):
                print(tag.name, tag.string)
            else:
                print(tag.replace('\n', ''))

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup
from bs4.element import NavigableString

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
# 使用屬性取得所有子孫標籤
tag_div = soup.select("#q2") # 找到第2題
tag_ul = tag_div[0].ul       # 走訪到之下的<ul>            
for child in tag_ul.descendants:
    if not isinstance(child, NavigableString):
        print(child.name)

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup
from bs4.element import NavigableString

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
# 使用屬性取得所有子孫的文字內容
tag_div = soup.select("#q2") # 找到第2題
tag_ul = tag_div[0].ul       # 走訪到之下的<ul>
for string in tag_ul.strings:
    print(string.replace('\n', ''))

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
tag_div = soup.select("#q2") # 找到第2題
tag_ul = tag_div[0].ul       # 走訪到之下的<ul>
# 使用屬性取得父標籤
print(tag_ul.parent.name)
# 使用函數取得父標籤
print(tag_ul.find_parent().name)

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup
from bs4.element import NavigableString

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
tag_div = soup.select("#q2") # 找到第2題
tag_ul = tag_div[0].ul       # 走訪到之下的<ul>
# 使用屬性取得所有祖先標籤
for tag in tag_ul.parents:
    print(tag.name)
# 使用函數取得所有祖先標籤
for tag in tag_ul.find_parents():
    print(tag.name)

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
tag_div = soup.select("#q2") # 找到第2題
first_li = tag_div[0].ul.li  # 第1個<li>
print(first_li)
# 使用next_sibling屬性取得下一個兄弟標籤
second_li = first_li.next_sibling.next_sibling
print(second_li)
# 呼叫next_sibling()函數取得下一個兄弟標籤
third_li = second_li.find_next_sibling()
print(third_li)
print("---------------------------------------")
# 呼叫next_siblings()函數取得所有兄弟標籤
for tag in first_li.find_next_siblings():
    print(tag.name, tag.span.string)

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
tag_div = soup.select("#q2") # 找到第2題
tag_li = tag_div[0].ul.li  # 第1個<li>
third_li = tag_li.find_next_sibling().find_next_sibling()
print(third_li)
# 使用previous_sibling屬性取得前一個兄弟標籤
second_li = third_li.previous_sibling.previous_sibling
print(second_li)
# 呼叫previous_sibling()函數取得前一個兄弟標籤
first_li = second_li.find_previous_sibling()
print(first_li)
print("---------------------------------------")
# 呼叫previous_siblings()函數取得所有兄弟標籤
for tag in third_li.find_previous_siblings():
    print(tag.name, tag.span.string)

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
tag_html = soup.html # 找到第<html>標籤
print(type(tag_html), tag_html.name)
tag_next = tag_html.next_element.next_element
print(type(tag_next), tag_next.name)
tag_title = soup.title # 找到第<title>標籤
print(type(tag_title), tag_title.name)
tag_previous = tag_title.previous_element.previous_element
print(type(tag_previous), tag_previous.name)

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup
from bs4.element import NavigableString

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")    
tag_div = soup.find(id = "emails")
for element in tag_div.next_elements:
    if not isinstance(element, NavigableString):
        print(element.name)

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup
from bs4.element import NavigableString

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")    
tag_div = soup.find(id="q1")
for element in tag_div.previous_elements:
    if not isinstance(element, NavigableString):
        print(element.name)
   
"""
print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup

soup = BeautifulSoup("<b class='score'>Joe</b>", "lxml")    
tag = soup.b
tag.name = "p"
tag["class"] = "question"
tag["id"] = "name"
print(tag)
del tag["class"]
print(tag)   

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup

soup = BeautifulSoup("<b class='score'>Joe</b>", "lxml")    
tag = soup.b
tag.string = "Mary"
print(tag)

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup
from bs4.element import NavigableString

soup = BeautifulSoup("<b></b>", "lxml")    
tag = soup.b
tag.append("Joe")
print(tag)
new_str = NavigableString(" Chen")
tag.append(new_str)
print(tag)
new_tag = soup.new_tag("a", href="http://www.example.com")
tag.append(new_tag)
print(tag)

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup

soup = BeautifulSoup("<p><b>One</b></p>", "lxml")  
tag = soup.b  
new_tag = soup.new_tag("i")
new_tag.string = "Two"
tag.insert_before(new_tag)
print(soup.p)
new_string = soup.new_string("Three")
tag.insert_after(new_string)
print(soup.p)
tag.clear()
print(soup.p)

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup

soup = BeautifulSoup("<p><b>One</b></p>", "lxml")  
tag = soup.b  
new_tag = soup.new_tag("i")
new_tag.string = "Two"
tag.replace_with(new_tag)
print(soup.p)

print("------------------------------------------------------------")  # 60個

import requests

r = requests.get("https://fchart.github.io/Example.html")

fp = open("tmp_Example.txt", "w", encoding="utf8")
fp.write(r.text)
print("寫入檔案 tmp_Example.txt...")
fp.close()

print("------------------------------------------------------------")  # 60個

fp = open("tmp_Example.txt", "r", encoding="utf8")
str = fp.read()
print("檔案內容:")
print(str)

print("------------------------------------------------------------")  # 60個

with open("tmp_Example.txt", "r", encoding="utf8") as fp:
    str = fp.read()
    print("檔案內容:")
    print(str)

print("------------------------------------------------------------")  # 60個

with open("tmp_Example.txt", "r", encoding="utf8") as fp:
    list1 = fp.readlines()
    for line in list1:
        print(line, end="")

print("------------------------------------------------------------")  # 60個


""" webdriver skip
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/test.html")
print("-----------------------------")
print(driver.title)
html = driver.page_source
print(html)
driver.quit()

print("------------------------------------------------------------")  # 60個

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/test.html")
print("-----------------------------")
print(driver.title)
html = driver.page_source
print(html)
driver.quit()

print("------------------------------------------------------------")  # 60個

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
cookie = {"name": "over18", "value": "1"}
driver.get("https://www.ptt.cc/bbs/Gossiping/index.html")
driver.add_cookie(cookie)
print("-----------------------------")
print(driver.title)
driver.quit()

print("------------------------------------------------------------")  # 60個

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
driver.implicitly_wait(10)
cookie = {"name": "over18", "value": "1"}
driver.get("https://www.ptt.cc/bbs/Gossiping/index.html")
driver.add_cookie(cookie)
print("-----------------------------")
print(driver.title)
driver.quit()
"""
print("------------------------------------------------------------")  # 60個

""" webdriver skip
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/test.html")
print("-----------------------------")
print(driver.title)
html = driver.page_source
print(html)
driver.quit()
"""
print("------------------------------------------------------------")  # 60個

#
# Extracted from: https://github.com/micropython/micropython-lib/blob/master/collections.defaultdict/collections/defaultdict.py
# Extracted from: https://github.com/micropython/micropython-lib/blob/master/urllib.parse/urllib/parse.py
#

_safe_quoters = {}
_ALWAYS_SAFE = frozenset(b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                         b'abcdefghijklmnopqrstuvwxyz'
                         b'0123456789'
                         b'_.-')
_ALWAYS_SAFE_BYTES = bytes(_ALWAYS_SAFE)

class defaultdict:

    @staticmethod
    def __new__(cls, default_factory=None, **kwargs):
        # Some code (e.g. urllib.urlparse) expects that basic defaultdict
        # functionality will be available to subclasses without them
        # calling __init__().
        self = super(defaultdict, cls).__new__(cls)
        self.d = {}
        return self

    def __init__(self, default_factory=None, **kwargs):
        self.d = kwargs
        self.default_factory = default_factory

    def __getitem__(self, key):
        try:
            return self.d[key]
        except KeyError:
            v = self.__missing__(key)
            self.d[key] = v
            return v

    def __setitem__(self, key, v):
        self.d[key] = v

    def __delitem__(self, key):
        del self.d[key]

    def __contains__(self, key):
        return key in self.d

    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError(key)
        return self.default_factory()
        
class Quoter(defaultdict):
    """A mapping from bytes (in range(0,256)) to strings.

    String values are percent-encoded byte values, unless the key < 128, and
    in the "safe" set (either the specified safe set, or default set).
    """
    # Keeps a cache internally, using defaultdict, for efficiency (lookups
    # of cached keys don't call Python code at all).
    def __init__(self, safe):
        """safe: bytes object."""
        self.safe = _ALWAYS_SAFE.union(safe)

    def __repr__(self):
        # Without this, will just display as a defaultdict
        return "<Quoter %r>" % dict(self)

    def __missing__(self, b):
        # Handle a cache miss. Store quoted string in cache and return.
        res = chr(b) if b in self.safe else '%{:02X}'.format(b)
        self[b] = res
        return res


def clear_cache():
    """Clear the quoters cache."""
    _safe_quoters.clear()


def quote(string, safe='/', encoding=None, errors=None):
    """quote('abc def') -> 'abc%20def'

    Each part of a URL, e.g. the path info, the query, etc., has a
    different set of reserved characters that must be quoted.

    RFC 2396 Uniform Resource Identifiers (URI): Generic Syntax lists
    the following reserved characters.

    reserved    = ";" | "/" | "?" | ":" | "@" | "&" | "=" | "+" |
                  "$" | ","

    Each of these characters is reserved in some component of a URL,
    but not necessarily in all of them.

    By default, the quote function is intended for quoting the path
    section of a URL.  Thus, it will not encode '/'.  This character
    is reserved, but in typical usage the quote function is being
    called on a path where the existing slash characters are used as
    reserved characters.

    string and safe may be either str or bytes objects. encoding must
    not be specified if string is a str.

    The optional encoding and errors parameters specify how to deal with
    non-ASCII characters, as accepted by the str.encode method.
    By default, encoding='utf-8' (characters are encoded with UTF-8), and
    errors='strict' (unsupported characters raise a UnicodeEncodeError).
    """
    if isinstance(string, str):
        if not string:
            return string
        if encoding is None:
            encoding = 'utf-8'
        if errors is None:
            errors = 'strict'
        string = string.encode(encoding, errors)
    else:
        if encoding is not None:
            raise TypeError("quote() doesn't support 'encoding' for bytes")
        if errors is not None:
            raise TypeError("quote() doesn't support 'errors' for bytes")

    return quote_from_bytes(string, safe)


def quote_plus(string, safe='', encoding=None, errors=None):
    """Like quote(), but also replace ' ' with '+', as required for quoting
    HTML form values. Plus signs in the original string are escaped unless
    they are included in safe. It also does not have safe default to '/'.
    """
    # Check if ' ' in string, where string may either be a str or bytes.  If
    # there are no spaces, the regular quote will produce the right answer.
    if ((isinstance(string, str) and ' ' not in string) or
            (isinstance(string, bytes) and b' ' not in string)):
        return quote(string, safe, encoding, errors)

    if isinstance(safe, str):
        space = ' '
    else:
        space = b' '

    string = quote(string, safe + space, encoding, errors)
    return string.replace(' ', '+')


def quote_from_bytes(bs, safe='/'):
    """Like quote(), but accepts a bytes object rather than a str, and does
    not perform string-to-bytes encoding.  It always returns an ASCII string.
    quote_from_bytes(b'abc def\x3f') -> 'abc%20def%3f'
    """
    if not isinstance(bs, (bytes, bytearray)):
        raise TypeError("quote_from_bytes() expected bytes")

    if not bs:
        return ''

    if isinstance(safe, str):
        # Normalize 'safe' by converting to bytes and removing non-ASCII chars
        safe = safe.encode('ascii', 'ignore')
    else:
        safe = bytes([c for c in safe if c < 128])

    if not bs.rstrip(_ALWAYS_SAFE_BYTES + safe):
        return bs.decode()

    try:
        quoter = _safe_quoters[safe]
    except KeyError:
        _safe_quoters[safe] = quoter = Quoter(safe).__getitem__

    return ''.join([quoter(char) for char in bs])


def urlencode(query, doseq=False, safe='', encoding=None, errors=None):
    """Encode a dict or sequence of two-element tuples into a URL query string.

    If any values in the query arg are sequences and doseq is true, each
    sequence element is converted to a separate parameter.

    If the query arg is a sequence of two-element tuples, the order of the
    parameters in the output will match the order of parameters in the
    input.

    The components of a query arg may each be either a string or a bytes type.
    When a component is a string, the safe, encoding and error parameters are
    sent to the quote_plus function for encoding.
    """

    if hasattr(query, "items"):
        query = query.items()
    else:
        # It's a bother at times that strings and string-like objects are
        # sequences.
        try:
            # non-sequence items should not work with len()
            # non-empty strings will fail this
            if len(query) and not isinstance(query[0], tuple):
                raise TypeError
            # Zero-length sequences of all types will get here and succeed,
            # but that's a minor nit.  Since the original implementation
            # allowed empty dicts that type of behavior probably should be
            # preserved for consistency
        except TypeError:
            # ty, va, tb = sys.exc_info()
            raise TypeError("not a valid non-string sequence "
                            "or mapping object")  # .with_traceback(tb)

    l = []
    if not doseq:
        for k, v in query:
            if isinstance(k, bytes):
                k = quote_plus(k, safe)
            else:
                k = quote_plus(str(k), safe, encoding, errors)

            if isinstance(v, bytes):
                v = quote_plus(v, safe)
            else:
                v = quote_plus(str(v), safe, encoding, errors)

            l.append(k + '=' + v)
    else:
        for k, v in query:
            if isinstance(k, bytes):
                k = quote_plus(k, safe)
            else:
                k = quote_plus(str(k), safe, encoding, errors)

            if isinstance(v, bytes):
                v = quote_plus(v, safe)
                l.append(k + '=' + v)
            elif isinstance(v, str):
                v = quote_plus(v, safe, encoding, errors)
                l.append(k + '=' + v)
            else:
                try:
                    # Is this a sufficient test for sequence-ness?
                    _ = len(v)  # noqa
                except TypeError:
                    # not a sequence
                    v = quote_plus(str(v), safe, encoding, errors)
                    l.append(k + '=' + v)
                else:
                    # loop over the sequence
                    for elt in v:
                        if isinstance(elt, bytes):
                            elt = quote_plus(elt, safe)
                        else:
                            elt = quote_plus(str(elt), safe, encoding, errors)

                        l.append(k + '=' + elt)

    return '&'.join(l)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


from bs4 import BeautifulSoup

html_str = "<p>Hello World!</p>"
soup = BeautifulSoup(html_str, "lxml")
print(soup)

print("------------------------------------------------------------")  # 60個

import requests
from bs4 import BeautifulSoup

r = requests.get("https://fchart.github.io/ML/Surveys.html")
r.encoding = "utf8"
soup = BeautifulSoup(r.text, "lxml")
print(soup)

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
    print(soup)

tags = soup("a")
tag = tags[1]
print("標籤名稱: ", tag.name)
print("標籤內容: ", tag.text)
print("標籤內容: ", tag.string)
print("標籤內容: ", tag.b.string)
print("URL網址: ", tag.get("href", None))
print("target屬性: ", tag["target"])

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")

tags = soup("img")
tag = tags[0]
print("圖片網址: ", tag.get("src", None))
print("alt屬性: ", tag["alt"])
print("屬性: ", tag.attrs)

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

# 走訪下一層HTML標籤
print(soup.html.body.div.div.p.a.text)
print("----------------------")
# 走訪上一層HTML標籤
tag_div = soup.select_one("#q1") # 找到第1題的<div>標籤
tag_li = tag_div.ul.li    # 走訪到之下的<ul>
print(tag_li.text)
# 使用parent屬性取得父標籤
print(tag_li.parent.parent.p.a.text)
print("----------------------")
tag_div = soup.select_one("#q2") # 找到第2題的<div>標籤
print(tag_div.find_previous_sibling().p.a.text)
print(tag_div.find_next_sibling().p.a.text)

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")

#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

# 搜尋<a>標籤
tag_a = soup.find("a") 
print(tag_a.text)
# 呼叫多次find()方法
tag_p = soup.find(name="p")
tag_a = tag_p.find(name="a")
print(tag_p.a.text)
print(tag_a.text)

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

# 使用id屬性搜尋<div>標籤
tag_div = soup.find(id="q2")
tag_a = tag_div.find("a") 
print(tag_a.text)

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  
    
# 使用class屬性搜尋<span>標籤
tag_span = soup.find(attrs={"class": "score"})
print(tag_span.text)
# 搜尋第2題的第1個<span>標籤
tag_div = soup.find(id="q2")
tag_span = tag_div.find(class_="score")
print(tag_span.text)

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

# 使用HTML5的data-屬性搜尋<div>標籤
tag_div = soup.find(attrs={"data-custom": "important"})
print(tag_div.text)

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")

# 使用文字內容來搜尋標籤
tag_str = soup.find(text="請問你的")
print(tag_str)
tag_str = soup.find(text="10")
print(tag_str)
print(type(tag_str))        # NavigableString型態
print(tag_str.parent.name)  # 父標籤名稱
tag_str = soup.find(text="男 - ")
print(tag_str)

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")   
    
# 測試取出<li>標籤的內容
tag_str = soup.find(text="女 - ")
print(tag_str)
tag_li = soup.find(class_="response")
print(tag_li.text)
print(tag_li.string)
print(tag_li.span.string)

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")      
    
# 使用多條件來搜尋HTML標籤
tag_div = soup.find("div", class_="question")
print(tag_div.prettify())
tag_p = soup.find("p", class_="question")
print(tag_p.prettify())

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  
    
# 使用函數建立搜尋條件
def is_secondary_question(tag):
    return tag.has_attr("href") and \
           tag.get("href") == "http://example.com/q2"

tag_a = soup.find(is_secondary_question)
print(tag_a.prettify())

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")      
    
# 找出所有問卷的題目串列
tag_list = soup.find_all("p", class_="question")
print(tag_list[0].prettify())

for question in tag_list:
    print(question.a.text)

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")     
    
# 找出前2個問卷的題目串列
tag_list = soup.find_all("p", class_="question", limit=2)
print(len(tag_list))

for question in tag_list:
    print(question.a.text)

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

tag_div = soup.find("div", id="q2")
# 找出所有標籤串列
tag_all = tag_div.find_all(True)
for tag in tag_all:
    print(tag.name)

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

tag_div = soup.find("div", id="q2")
# 找出所有文字內容串列
tag_str_list = tag_div.find_all(text=True)
print(tag_str_list)
# 找出指定的文字內容串列
tag_str_list = tag_div.find_all(text=["20", "40"])
print(tag_str_list)

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

tag_div = soup.find("div", id="q2")
# 找出所有<p>和<span>標籤
tag_list = tag_div.find_all(["p", "span"])
for tag in tag_list:
    print(tag.name, tag.text.replace("\n", ""))
print("-------------")
# 找出class屬性值question或selected的所有標籤
tag_list = tag_div.find_all(class_=["question", "selected"])
for tag in tag_list:
    print(tag.name, tag.text.replace("\n", ""))

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

tag_div = soup.find("div", id="q2")
# 找出所有<li>子孫標籤
tag_list = tag_div.find_all("li")
for tag in tag_list:
    print(tag.text.replace("\n", ""))
# 沒有使用遞迴來找出所有<li>標籤
tag_list = tag_div.find_all("li", recursive=False)
print(tag_list)

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

# 搜尋<title>標籤和第3個<div>標籤
tag_title = soup.select("title")
print(tag_title[0].text)
tag_first_div = soup.find("div")
tag_div = tag_first_div.select("div:nth-of-type(3)")
print(tag_div[0].prettify())

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

# 搜尋class和id屬性值的標籤
tag_div = soup.select("#q1")
print(tag_div[0].p.a.text)
tag_span = soup.select("span#email")
print(tag_span[0].text)
tag_div = soup.select("#q1, #q2")  # 多個id屬性
for item in tag_div:
    print(item.p.a.text)
print("-----------")
tag_div = soup.find("div")  # 第1個<div>標籤
tag_p = tag_div.select(".question")   
for item in tag_p:
    print(item.a["href"])
tag_span = soup.select("[class~=selected]")
for item in tag_span:
    print(item.text)

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

# 搜尋特定屬性值的標籤
def print_a(tag_a):
    for tag in tag_a:
        print(tag["href"])
    print("-----------")    
tag_a = soup.select("a[href]")
print_a(tag_a)
tag_a = soup.select("a[href='http://example.com/q2']")
print_a(tag_a)
tag_a = soup.select("a[href^='http://example.com']")
print_a(tag_a)
tag_a = soup.select("a[href$='q3']")
print_a(tag_a)
tag_a = soup.select("a[href*='q']")
print_a(tag_a)

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

# 搜尋<title>標籤, 和<div>標籤下的所有<a>標籤
tag_title = soup.select("html head title")
print(tag_title[0].text)    
tag_a = soup.select("body div a")
for tag in tag_a:
    print(tag["href"])

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

# 搜尋指定標籤下的直接子標籤
tag_a = soup.select("p > a")
for tag in tag_a:
    print(tag["href"])
tag_li = soup.select("ul > li:nth-of-type(2)")
for tag in tag_li:
    print(tag.text.replace("\n", ""))
tag_span = soup.select("div > #email")
for tag in tag_span:
    print(tag.prettify())  

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

# 搜尋兄弟標籤
tag_div = soup.find(id="q1")
print(tag_div.p.a.text)
print("-----------")
tag_div = soup.select("#q1 ~ .survey")
for item in tag_div:            
    print(item.p.a.text)  
print("-----------")
tag_div = soup.select("#q1 + .survey")
for item in tag_div:            
    print(item.p.a.text)   

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

# 使用select_one()方法搜尋標籤
tag_a = soup.select_one("a[href]")
print(tag_a.prettify())

print("------------------------------------------------------------")  # 60個

import re
from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

# 使用正規表達式搜尋文字內容
tag_str = soup.find(text="男 -")
print(tag_str)
regexp = re.compile("男 -")
tag_str = soup.find(text=regexp)
print(tag_str)
print("---------------------")
regexp = re.compile("\w+ -")
tag_list = soup.find_all(text=regexp)
print(tag_list)

print("------------------------------------------------------------")  # 60個

import re
from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

# 使用正規表達式搜尋電子郵件地址
email_regexp = re.compile("\w+@\w+\.\w+")
tag_str = soup.find(text=email_regexp)
print(tag_str)
print("---------------------")
tag_list = soup.find_all(text=email_regexp)
print(tag_list)

print("------------------------------------------------------------")  # 60個

import re
from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

# 使用正規表達式搜尋URL網址
url_regexp = re.compile("^http:")
tag = soup.find(href=url_regexp)
print(tag["href"], tag.text)
print("---------------------")
tag_list = soup.find_all(href=url_regexp)
for tag in tag_list:
    print(tag["href"], tag.text)

print("------------------------------------------------------------")  # 60個


"""webdriver skip

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/ML/Example.html")
print(driver.title)
soup = BeautifulSoup(driver.page_source, "lxml")
tag_ol = soup.find("ol", {"id":"list"})
tags_li = tag_ol.find_all("li", class_="line")
for tag in tags_li:
    print(tag.text)
driver.quit()

print("------------------------------------------------------------")  # 60個

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from bs4 import BeautifulSoup

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/ML/Example.html")
print(driver.title)
soup = BeautifulSoup(driver.page_source, "lxml")
tag_ol = soup.find("ol", {"id":"list"})
tags_li = tag_ol.find_all("li", class_="line")
for tag in tags_li:
    print(tag.text)
driver.quit()

print("------------------------------------------------------------")  # 60個

from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/Example.html")
tag_ol = driver.find_element_by_xpath('//*[@id="list"]')
print(tag_ol.tag_name)
tags_li = tag_ol.find_elements_by_xpath('//li')
for tag in tags_li:
    print(tag.text, tag.get_attribute("class"))
driver.quit()

print("------------------------------------------------------------")  # 60個

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/ML/Example.html")
tag_ol = driver.find_element(By.XPATH, '/html/body/ol')
print(tag_ol.tag_name)
tags_li = tag_ol.find_elements(By.XPATH, '//li')
for tag in tags_li:
    print(tag.text, tag.get_attribute("class"))
driver.quit()

print("------------------------------------------------------------")  # 60個

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/ML/Example.html")
tag_ol = driver.find_element(By.XPATH, '/html/body/ol')
print(tag_ol.tag_name)
tags_li = tag_ol.find_elements(By.XPATH, '//li')
for tag in tags_li:
    print(tag.text, tag.get_attribute("class"))
driver.quit()

print("------------------------------------------------------------")  # 60個

from selenium import webdriver

driver = webdriver.Edge("./msedgedriver")
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/Example.html")
tag_ol = driver.find_element_by_xpath('/html/body/ol')
print(tag_ol.tag_name)
tags_li = tag_ol.find_elements_by_xpath('//li')
for tag in tags_li:
    print(tag.text, tag.get_attribute("class"))
driver.quit()

print("------------------------------------------------------------")  # 60個

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/ML/Example.html")
tag_ol = driver.find_element(By.XPATH, '//*[@id="list"]')
print(tag_ol.tag_name)
print(tag_ol.get_attribute('innerHTML'))
soup = BeautifulSoup(tag_ol.get_attribute('innerHTML'), "lxml")
tags_li = soup.find_all("li", class_="line")
for tag in tags_li:
    print(tag.text)
driver.quit()

print("------------------------------------------------------------")  # 60個

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from bs4 import BeautifulSoup

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/ML/Example.html")
tag_ol = driver.find_element(By.XPATH, '//*[@id="list"]')
print(tag_ol.tag_name)
print(tag_ol.get_attribute('innerHTML'))
soup = BeautifulSoup(tag_ol.get_attribute('innerHTML'), "lxml")
tags_li = soup.find_all("li", class_="line")
for tag in tags_li:
    print(tag.text)
driver.quit()
"""

print("------------------------------------------------------------")  # 60個

import sys
import json 
import requests

print("------------------------------------------------------------")  # 60個

url = "https://www.googleapis.com/books/v1/volumes?maxResults=5&q=Python&projection=lite"
jsonfilename = "tmp_GoogleBooks.json"
r = requests.get(url)
r.encoding = "utf8"
json_data = json.loads(r.text)
with open(jsonfilename, 'w') as fp:
    json.dump(json_data, fp)
    print('json 存檔完成, 檔案 :', jsonfilename)

print("------------------------------------------------------------")  # 60個

import requests

""" momo 網站 無 headers, 不可抓取
URL = "https://www.momoshop.com.tw/search/"

r = requests.get(URL+"searchShop.jsp?keyword=NBA")
if r.status_code == requests.codes.ok:
    r.encoding = "big5"
    print(r.text)        
else:
    print("HTTP請求錯誤..." + URL)

"""
print("------------------------------------------------------------")  # 60個

import requests

print('使用 headers 抓取 momo 網站')

URL="https://www.momoshop.com.tw/search/"

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
           'AppleWebKit/537.36 (KHTML, like Gecko)'
           'Chrome/63.0.3239.132 Safari/537.36'}
r = requests.get(URL+"searchShop.jsp?keyword=NBA", headers=headers)
if r.status_code == requests.codes.ok:
    r.encoding = "big5"    
    print(r.text)        
else:
    print("HTTP請求錯誤..." + URL)

print("------------------------------------------------------------")  # 60個

""" webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

URL="https://www.momoshop.com.tw/search/"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get(URL+"searchShop.jsp?keyword=NBA")
print("-----------------------------")
print(driver.title)
html = driver.page_source
fp = open("tmp_NBA.html", "w", encoding="utf8")
fp.write(html)
print("寫入檔案tmp_NBA.html...")
fp.close()
driver.quit()
"""
print("------------------------------------------------------------")  # 60個

""" wait long
import time
import requests

URL = "http://www.majortests.com/word-lists/word-list-0{0}.html"

for i in range(1, 10):
    url = URL.format(i) 
    r = requests.get(url)
    print(r.status_code)
    print("等待5秒鐘... i = ", i)
    time.sleep(5) 
"""

print("------------------------------------------------------------")  # 60個

import requests
from bs4 import BeautifulSoup

URL = "https://www.ptt.cc/bbs/NBA/index6503.html"
DELETED = BeautifulSoup("<a href='Deleted'>本文已刪除</a>", "lxml").a

r = requests.get(URL)
if r.status_code == requests.codes.ok:
    r.encoding = "utf8"
    soup = BeautifulSoup(r.text, "lxml")
    tag_divs = soup.find_all("div", class_="r-ent")
    for tag in tag_divs:
        tag_a = tag.find("a") or DELETED
        print(tag_a["href"])
        print(tag_a.text)
        print(tag.find("div", class_="author").string)
else:
    print("HTTP請求錯誤..." + URL)

print("------------------------------------------------------------")  # 60個

import requests
from bs4 import BeautifulSoup

URL = "https://www.ptt.cc/bbs/Gossiping/index.html"

r = requests.get(URL, cookies={"over18": "1"})
if r.status_code == requests.codes.ok:
    r.encoding = "utf8"
    soup = BeautifulSoup(r.text, "lxml")
    tag_divs = soup.find_all("div", class_="r-ent")
    for tag in tag_divs:
        if tag.find('a'): # 是否有<a>標籤
            tag_a = tag.find("a")
            print(tag_a["href"])
            print(tag_a.text)
            print(tag.find("div", class_="author").string)
else:
    print("HTTP請求錯誤..." + URL)

print("------------------------------------------------------------")  # 60個

from urllib.parse import urljoin

URL = "http://www.majortests.com/word-lists/word-list-01.html"
PTT = "https://wwww.ptt.cc/bbs/movie/index.html"

catalog = ["movie", "NBA", "Gossiping"]

for i in range(1, 5):
    url = urljoin(URL, "world-list-0{0}.html".format(i)) 
    print(url)
print("-----------------")
for item in catalog:
    url = urljoin(PTT, "../{0}/index.html".format(item))
    print(url)

print("------------------------------------------------------------")  # 60個

import requests
from bs4 import BeautifulSoup
import csv, re

URL = "https://movies.yahoo.com.tw/movie_intheaters.html"
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
           "AppleWebKit/537.36 (KHTML, like Gecko)"
           "Chrome/63.0.3239.132 Safari/537.36"}

def format_date(date):  # 取出上映日期
    if not date: return "N/A"
    pattern = '\d+-\d+-\d+'
    match = re.search(pattern, date.text)
    if match is None:
        return date.text
    else:
        return match.group(0)    

def get_text(tag):
    if tag:
        return tag.text.strip()
    else:
        return "N/A"
 
def get_attrib(tag, attrib):
    if tag:
        return tag[attrib].strip()
    else:
        return "N/A"

""" fail    
movies = [["中文片名","英文片名","期待度","海報圖片","上映日"]]
r = requests.get(URL, headers=headers)
if r.status_code == requests.codes.ok:
    soup = BeautifulSoup(r.text, 'lxml')
    tag_ul = soup.find("ul", class_="release_list")
    rows = tag_ul.find_all("li")
    for row in rows:
        name_div = row.find("div",class_="release_movie_name")
        cht_n = get_text(name_div.find("a"))
        eng_n = get_text(name_div.find("div",class_="en").find("a"))
        expect = get_text(row.find("div",class_="leveltext").find("span"))
        photo_div = row.find("div",class_="release_foto")
        poster_url = get_attrib(photo_div.find("img"),"data-src")
        date = row.find('div',class_='release_movie_time')
        release_date = format_date(date)
        movie= [cht_n,eng_n,expect,poster_url,release_date]
        movies.append(movie)
else:
   print("HTTP請求錯誤...")

with open("tmp_movies.csv", "w+",newline="",encoding="utf-8") as fp:
    writer = csv.writer(fp)
    for item in movies:
        writer.writerow(item)
"""
print("------------------------------------------------------------")  # 60個

""" webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import json

URL = "https://fchart.github.io/Ashion/"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get(URL)

soup = BeautifulSoup(driver.page_source, "lxml")
sec = soup.find("section", class_="product spad")
items = sec.find_all("div", class_="product__item")
print(len(items))
products=[]
for item in items:
    tag = item.find("h6").find("a")
    title = tag.text.strip() if tag else "N/A"
    tag = item.find("div", class_="product__item__pic")
    img = tag["data-setbg"].strip() if tag else "N/A"
    tag = item.find("div", class_="product__price")
    price = tag.text.strip() if tag else "N/A"
    print(title)
    products.append({
        "title": title,
        "image": URL+img,
        "price": price
    })
driver.quit()
with open("tmp_products.json", "w", encoding="utf-8") as fp: # 寫入JSON檔案
    json.dump(products,fp,indent=2,
              sort_keys=True,
              ensure_ascii=False)
"""

print("------------------------------------------------------------")  # 60個

import requests 
from bs4 import BeautifulSoup
import csv

url = "https://rate.bot.com.tw/xrt?Lang=zh-TW"
csvfile = "tmp_xrt.csv"
r = requests.get(url)
r.encoding = "utf8"
soup = BeautifulSoup(r.text, "lxml")
tag_table = soup.select_one("#ie11andabove > div > table")
rows = tag_table.find_all("tr")
with open(csvfile,'w+',newline='',encoding="big5") as fp:
    writer = csv.writer(fp)
    for row in rows:
        lst = []
        for cell in row.find_all(["td", "th"]):
            lst.append(cell.text.replace("\n","").
                       replace("\r","").
                       strip())
        writer.writerow(lst)

print("------------------------------------------------------------")  # 60個

import requests
from bs4 import BeautifulSoup
import csv, re, time

URL = "https://movies.yahoo.com.tw/movie_intheaters.html/?page={0}"
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
           "AppleWebKit/537.36 (KHTML, like Gecko)"
           "Chrome/63.0.3239.132 Safari/537.36"}
 
def format_date(date):  # 取出上映日期
    if not date: return "N/A"
    pattern = '\d+-\d+-\d+'
    match = re.search(pattern, date.text)
    if match is None:
        return date.text
    else:
        return match.group(0)    

def get_text(tag):
    if tag:
        return tag.text.strip()
    else:
        return "N/A"
 
def get_attrib(tag, attrib):
    if tag:
        return tag[attrib].strip()
    else:
        return "N/A"   
""" fail
all_movies = [["中文片名","英文片名","期待度","海報圖片","上映日"]]
for page in range(1, 11):
    url = URL.format(page)
    print("抓取: 第" + str(page) + "頁 網路資料中...")
    r = requests.get(url, headers=headers)
    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text, 'lxml')
        movies = []
        tag_ul = soup.find("ul", class_="release_list")
        rows = tag_ul.find_all("li")
        for row in rows:
            name_div = row.find("div",class_="release_movie_name")
            cht_n = get_text(name_div.find("a"))
            eng_n = get_text(name_div.find("div",class_="en").find("a"))
            expect = get_text(row.find("div",class_="leveltext").find("span"))
            photo_div = row.find("div",class_="release_foto")
            poster_url = get_attrib(photo_div.find("img"),"data-src")
            date = row.find('div',class_='release_movie_time')
            release_date = format_date(date)
            movie= [cht_n,eng_n,expect,poster_url,release_date]
            movies.append(movie)
        all_movies = all_movies + movies
        if soup.find("li", class_="nexttxt disabled"):
            break   # 已經沒有下一頁
        print("等待5秒鐘...")   
        time.sleep(5) 
    else:
        print("HTTP請求錯誤...")

with open("all_movies.csv", "w+",newline="",encoding="utf-8") as fp:
    writer = csv.writer(fp)
    for item in all_movies:
        writer.writerow(item)
"""

print("------------------------------------------------------------")  # 60個

import requests
from bs4 import BeautifulSoup
import csv, re, time

URL = "https://movies.yahoo.com.tw/movie_intheaters.html/?page=1"
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
           "AppleWebKit/537.36 (KHTML, like Gecko)"
           "Chrome/63.0.3239.132 Safari/537.36"}
 
def format_date(date):  # 取出上映日期
    if not date: return "N/A"
    pattern = '\d+-\d+-\d+'
    match = re.search(pattern, date.text)
    if match is None:
        return date.text
    else:
        return match.group(0)    

def get_text(tag):
    if tag:
        return tag.text.strip()
    else:
        return "N/A"
 
def get_attrib(tag, attrib):
    if tag:
        return tag[attrib].strip()
    else:
        return "N/A"  

""" fail
all_movies = [["中文片名","英文片名","期待度","海報圖片","上映日"]]
page = 1
while True:
    print("抓取: 第" + str(page) + "頁 網路資料中...")
    page = page + 1
    r = requests.get(URL, headers=headers)
    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text, 'lxml')
        movies = []
        tag_ul = soup.find("ul", class_="release_list")
        rows = tag_ul.find_all("li")
        for row in rows:
            name_div = row.find("div",class_="release_movie_name")
            cht_n = get_text(name_div.find("a"))
            eng_n = get_text(name_div.find("div",class_="en").find("a"))
            expect = get_text(row.find("div",class_="leveltext").find("span"))
            photo_div = row.find("div",class_="release_foto")
            poster_url = get_attrib(photo_div.find("img"),"data-src")
            date = row.find('div',class_='release_movie_time')
            release_date = format_date(date)
            movie= [cht_n,eng_n,expect,poster_url,release_date]
            movies.append(movie)
        all_movies = all_movies + movies
        if soup.find("li", class_="nexttxt disabled"):
            break   # 已經沒有下一頁
        nextPage = soup.find("li", class_="nexttxt")   
        if nextPage:
            URL = nextPage.find("a")["href"] 
            print("等待5秒鐘...")          
            time.sleep(5)
        else:
            break
    else:
        print("HTTP請求錯誤...")

with open("tmp_all_movies2.csv", "w+",newline="",encoding="utf-8") as fp:
    writer = csv.writer(fp)
    for item in all_movies:
        writer.writerow(item)
"""
print("------------------------------------------------------------")  # 60個

""" webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time, csv

URL="https://fchart.github.io/ML/nba_items.html"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get(URL)
pages_remaining = True
page_num = 1
while pages_remaining:
    soup = BeautifulSoup(driver.page_source, "lxml")
    tag_table = soup.select_one("#our-table")
    rows = tag_table.find_all("tr")
    csvfile = "tmp_NBA_Products" + str(page_num) + ".csv"
    with open(csvfile, 'w+', newline='', encoding="utf8") as fp:
        writer = csv.writer(fp)
        for row in rows:
            lst = []
            for cell in row.find_all(["td", "th"]):
                lst.append(cell.text.replace("\n","").
                           replace("\r","").
                           strip())
            writer.writerow(lst)
    print("儲存頁面:", page_num)
    try:   
        next_link = driver.find_element(By.CLASS_NAME, "nextbtn")
        if next_link:
            next_link.click()
            time.sleep(5)
            page_num = page_num + 1
        else:
            pages_remaining = False
    except Exception:
        pages_remaining = False        
driver.close()
"""
print("------------------------------------------------------------")  # 60個

import time
import requests
import json
from bs4 import BeautifulSoup

# 目標URL網址
URL = "https://www.ptt.cc"
MAX_PUSH = 50
# TOPIC = "Gossiping"
TOPIC = "NBA" 

def get_resource(url):
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
               "AppleWebKit/537.36 (KHTML, like Gecko)"
               "Chrome/63.0.3239.132 Safari/537.36"}
    return requests.get(url, headers=headers, cookies={"over18":"1"})

def parse_html(r):
    if r.status_code == requests.codes.ok:
        r.encoding = "utf8"
        soup = BeautifulSoup(r.text, "lxml")        
    else:
        print("HTTP請求錯誤..." + url)
        soup = None
    
    return soup    

def get_articles(soup, date):
    articles = []  
    # 取得上一頁的超連結
    paging_div = soup.find("div", class_="btn-group btn-group-paging")
    paging_a = paging_div.find_all("a", class_="btn")
    prev_url = paging_a[1]["href"]

    tag_divs = soup.find_all("div", class_="r-ent")
    for tag in tag_divs:
        # 判斷文章的日期
        if tag.find("div",class_="date").text.strip() == date:
            push_count = 0    # 取得推文數
            push_str = tag.find("div", class_="nrec").text
            if push_str:
                try:
                    push_count = int(push_str)  # 轉換成數字
                except ValueError:  # 轉換失敗，可能是'爆'或 'X1','X2'
                    if push_str == '爆':
                        push_count = 99
                    elif push_str.startswith('X'):
                        push_count = -10
            # 取得貼章的超連結和標題文字
            if tag.find("a"):  # 有超連結，表示文章存在
                href = tag.find("a")["href"]
                title = tag.find("a").text
                author = tag.find("div", class_="author").string 
                articles.append({
                    "title": title,
                    "href": href,
                    "push_count": push_count,
                    "author": author
                })
    
    return articles, prev_url

def save_to_json(articles, file):
    print("今天總共有: " + str(len(articles)) + " 篇文章")
    threshold = MAX_PUSH
    print("熱門文章(> %d 推): " % (threshold))
    for item in articles:   # 顯示熱門文章清單
        if int(item["push_count"]) > threshold:
            print(item["title"], item["href"], item["author"])    
    with open(file, "w", encoding="utf-8") as fp: # 寫入JSON檔案
        json.dump(articles,fp,indent=2,sort_keys=True,ensure_ascii=False)

def web_scraping_bot(url):
    articles = []
    print("抓取網路資料中...")
    soup = parse_html(get_resource(url))
    if soup:
        # 取得今天日期, 去掉開頭'0'符合PTT的日期格式
        today = time.strftime("%m/%d").lstrip('0') 
        # 取得目前頁面的今日文章清單
        current_articles, prev_url = get_articles(soup, today) 
        while current_articles: 
            articles += current_articles
            print("等待2秒鐘...")
            time.sleep(2) 
             # 剖析上一頁繼續尋找是否有今日的文章
            soup = parse_html(get_resource(URL + prev_url))
            current_articles, prev_url = get_articles(soup, today)

    return articles

if __name__ == '__main__':
    url = URL + "/bbs/" + TOPIC + "/index.html"
    print(url)
    articles = web_scraping_bot(url)
    for item in articles:
        print(item)
    save_to_json(articles, "tmp_articles.json")
 

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



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

# 尋找指定標籤find()、find_all()

# find_all()定位符合標籤的全部節點，回傳的是一個列表。
# select()其實就是使用CSS選擇器語法的find_all()



print("------------------------------------------------------------")  # 60個
"""
print("BeautifulSoup 測試 4")

url = "https://oldsiao.neocities.org/"
soup = get_soup_from_url(url)

print("尋找標籤「<div>」")
print(soup.find("div"))

print("尋找標籤「<title>」")
print(soup.find_all("title"))

"""

