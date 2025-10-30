"""
Python 測試 BeautifulSoup
解讀 本地 / 遠端 網頁資料, 都是使用 html.parser 解析器

以BeautifulSoup套件進行網頁解析
1. 展開的html text成string
2. 本地html檔案
3. 網頁資料

共同抽出
print(soup.prettify())  # prettify()這個函數可以將DOM tree以比較美觀的方式印出。
print(soup.prettify())  # 把排版後的 html 印出來
print("列印BeautifulSoup物件資料型態 ", type(soup))
print("取得網頁內容 :", soup.text)

# 尋找指定標籤find()、find_all()
# find_all()定位符合標籤的全部節點，回傳的是一個列表。
# select()其實就是使用CSS選擇器語法的find_all()

# 用.取
# 用find找
# 用select選
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

font_filename = "D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個
print("準備工作")
print("------------------------------------------------------------")  # 60個

import re
import csv
import ssl
import json
import requests
import urllib
import urllib.parse
from bs4 import BeautifulSoup
from bs4.element import NavigableString
from datetime import datetime
from urllib.request import urlopen


def get_html_data1(url):
    # print("取得網頁資料 :", url)
    resp = requests.get(url)  # 用 requests 的 get 方法把網頁抓下來

    # 檢查 HTTP 回應碼是否為 requests.codes.ok(200)
    if resp.status_code != requests.codes.ok:
        print("讀取網頁資料錯誤, url :", resp.url)
        return None
    else:
        return resp


def get_soup_from_url(url):
    html_data = get_html_data1(url)
    if html_data == None:
        print("無法取得網頁資料")
        sys.exit()  # 立刻退出程式

    html_data.encoding = "UTF-8"  # 或是 unicode 也可, 指定編碼方式
    soup = BeautifulSoup(html_data.text, "html.parser")  # 解析原始碼
    # soup = BeautifulSoup(html_data.text, "lxml") # 指定 lxml 作為解析器
    # pprint.pprint(html_data.text)
    # print("取得網頁標題 :", soup.title)  # 印出整行資料 # <title>網頁標題</title>
    return soup


def save_html_file(url):
    html_data = requests.get(url)  # 使用 GET 對檔案連結發出請求
    print("取出路徑中的檔案名稱 :", os.path.basename(url))
    filename = "tmp_" + os.path.basename(url)
    filename = filename + ".html"
    with open(filename, "wb") as f:
        f.write(html_data.content)  # 將response.content二進位內容寫入檔案
    print("存檔檔案 :", filename)


headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
}

cookies = {"over18": "1"}
'''
print("------------------------------------------------------------")  # 60個
print("讀取本地html ST")
print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 讀取本地 html 1")

string_html_data = """
<html>
    <head><meta charset="big-5"><title>網頁標題1</title></head>
    <body>
        <div class="section" id="main">
            <img alt="台北火車站" src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/TRA_Taipei_Station_and_Zhongxiao_West_Road_at_night_20210115.jpg/500px-TRA_Taipei_Station_and_Zhongxiao_West_Road_at_night_20210115.jpg" width="320" alt="台北車站"/>
            <p>車站選擇</p>
            <button id="station1"><h4 class="bk">台北</h4></button>
            <button id="station2"><h4 class="pk">台中</h4></button>
            <button id="station3"><h4 class="pk">台南</h4></button>
            <button id="station4"><h4 class="pk">高雄</h4></button>
        </div>
        <div class="section" id="footer">
            <p>臺北市中正區黎明里北平西路3號</p>
        </div>

        <h3>網站連結</h3>
        <img src="https://assets.raspberrypi.com/static/d8c8df845f270ad324962846437aa55c/69a47/hero.webp" width="320" alt="樹梅派"/><br>
        <a href="https://tw.yahoo.com/" target="_blank">連線到<b>奇摩</b></a><br>
        <a href="https://www.google.com/" target="_blank">連線到<b>Google</b></a><br>
        <a href="https://www.youtube.com/" target="_blank">連線到<b>Youtube</b></a><br>

        <h3>段落</h3>
        <p id="p1">我是段落一</p>
        <p id="p2" class="red">我是段落二</p>

        <h3>分區</h3>
        <div class="content">
            <div class="item1">
                <a href="https://www.youtube.com/" class="red" id="link1">Youtube</a><br>
                <a href="https://www.google.com/" class="red" id="link2">Google</a>
            </div>
            <a href="https://tw.yahoo.com/" class="blue" id="link3"><br><img src="https://s.yimg.com/cv/apiv2/twfrontpage/logo/Yahoo-TW-desktop-homepage@2x-new.png">奇摩</a>
        </div>
        <p class="title1"><b>The test1</b></p>
        <p class="title2"><b>The test2</b></p>
        <p class="title3"><b>The test3</b></p>
        <a class="redcolor" href="http://powenko.com/1.html" id="link1">test1</a>
        <a class="bluecolor" href="http://powenko.com/2.html" id="link2">test2</a>
        <a class="redcolor" id="link3" href="http://powenko.com/3.html" id="link3">test3</a>

        <h3 class="blueText">優質好書</h3>
        <ul>
          <li><a href="https://www.google.com111">AAAA</a></li>
          <li><a href="https://www.google.com222">BBBB</a></li>
          <li><a href="https://www.google.com333">CCCC</a></li>
        </ul>
        <p><a href="https://www.google.com444" id="linkDtc" target="_blank">DDDD</a></p>

    <p class="title"><b>文件標題</b></p>
    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>
    <p class="story">...</p>

    <div class="content">
        E-Mail：<a href="mailto:mail@test.com.tw">mail</a><br>
        E-Mail2：<a href="mailto:mail2@test.com.tw">mail2</a><br>
        <ul class="price">定價：360元 </ul>
        <img src="http://test.com.tw/p1.jpg">
        <img src="http://test.com.tw/p2.jpg">
        <img src="http://test.com.tw/p3.png">
    </div>

    </body>
</html>
"""
soup = BeautifulSoup(string_html_data, "html.parser")
# soup = BeautifulSoup(string_html_data, "lxml")

print("------------------------------")  # 30個

print("第1個超連結：")
print(soup.find("a", {"href": "https://tw.yahoo.com/"}))
print("第2個超連結：")
print(soup.find("a", {"href": "https://www.google.com/"}))

print("------------------------------")  # 30個

# 用find找

print("找下一個粗體<b>")
cc = soup.find("b")  # 找下一個粗體<b>
print(cc)  # 全部
print(cc.text)  # 內容
print(cc.string)  # 內容

print("找全部的超連結<a>")

print(soup.find_all("a"))

print("找全部的超連結<a> +  條件")
cc = soup.find_all("a", {"class": "sister"})
print(cc)

print("找下一個超連結<a> + 條件")
cc = soup.find("a", {"href": "http://example.com/elsie"})
print(cc.text)  # Elsie

print("找下一個超連結<a> + 條件")
cc = soup.find("a", {"id": "link2"})
print(cc.text)  # Lacie

# 用select選
cc = soup.select("#link3")
print(cc)  # 全部
print(cc[0].text)  # 內容  # Tillie

print("找下一個超連結<a> + 條件")
cc = soup.find("a", {"id": "link1"})
print(cc.get("href"))  # http://example.com/elsie
print(cc["href"])  # http://example.com/elsie

print("------------------------------")  # 30個

print("用 re 搭配搜尋")
print("搜尋網頁中的 e-mail")
emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", string_html_data)
for email in emails:
    print(email)

print("搜尋網頁中的 價格")
price = re.findall(r"[\d]+", soup.select(".price")[0].text)[0]  # 價格  # 尋找class是price
print(price)

print("搜尋網頁中的 jpg圖片連結")
regex = re.compile(".*\.jpg")

print("找全部的影像<img> + 條件")
imglist = soup.find_all("img", {"src": regex})
for img in imglist:
    print(img["src"])

print("------------------------------")  # 30個

print("---------------h3")  # 15個
print(soup.find("h3"))
print(soup.find("h3").text)
print("---------------blueText")  # 15個
print(soup.select(".blueText"))  # 尋找class是blueText
print(soup.select(".blueText")[0].text)  # 尋找class是blueText
print("---------------a")  # 15個
print(soup.find("a", {"target": "_blank"}))
print(soup.find("a", {"target": "_blank"}).text)
print("---------------linkDtc")  # 15個
print(soup.select("#linkDtc"))
print(soup.select("#linkDtc")[0].text)
print("---------------a")  # 15個
link1 = soup.find_all("a")
for n in range(0, len(link1)):
    print(link1[n].text)
print("---------------ul")  # 15個
data = soup.find("ul")
link2 = data.find_all("a")
for n in range(0, len(link2)):
    print(link2[n].text)

print("------------------------------")  # 30個

# 用.取
print("找下一個超連結<a>")
print(soup.a)
print(soup.a.text)
print(soup.a.get("href"))
print(soup.a["href"])

# 用.取
print("找下一個標題<h1>")
print(soup.h1)

print("找下一個段落<p>")
print(soup.p)

print("找下一個超連結<a>")
print(soup.a)

print("取得網頁標題 :", soup.title)  # 印出整行資料 # <title>網頁標題4</title>
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

# 用.取
# print("整個html檔案 :\n", soup.html)  # 整個html檔案
print("整個head標籤 :", soup.html.head)  # 整個head標籤
print("取得網頁標題(內容) :", soup.html.head.title)  # title
print("取得網頁標題(內容) :", soup.html.head.title.string)
print("取得網頁標題(全部) :", soup.title)  # 印出整行資料 # <title>網頁標題1</title>
print("取得網頁標題(內容) :", soup.title.string)  # 印出內容資料 # 網頁標題1
print("取得網頁標題(內容) :", soup.meta["charset"])  # 印出內容資料 # 網頁標題1
print("head.meta :", soup.html.head.meta["charset"])

print("------------------------------")  # 30個

print("找全部的超連結<a>")
all_links = soup.find_all("a")  # 取得 全部 <a></a>
for link in all_links:
    href = link.get("href")  # 讀取 href 屬性內容
    # 判斷內容是否為非 None，並且開頭文字是 https://
    if href != None and href.startswith("https://"):
        print(href)

print("------------------------------")  # 30個

print("搜尋網頁中的 jpg圖片連結")
regex = re.compile(".*\.jpg")
imglist = soup.find_all("img", {"src": regex})
for img in imglist:
    print(img["src"])

print("------------------------------")  # 30個

# 用find找

# print("網頁html語法區塊：\n", soup.find("html"))  # <html>標籤
print("---------------")  # 15個
print("網頁表頭範圍 :", soup.find("head"))  # <head>標籤
print("---------------")  # 15個
# print("網頁身體範圍：", soup.find("body"))  # <body>標籤
print("---------------")  # 15個

print(soup.find("title"))  # 傳回網頁含<title>~</title>
print(soup.find("title").text)  # 傳回網頁<title>標籤內的資料

print("------------------------------")  # 30個

# 用find找
print("找下一個標題<h4>")
print(soup.find("h4"))

print("找下一個標題<h4> + 條件")
print(soup.find("h4", {"class": "pk"}))

print(soup.find("h4").text)

print("找全部的標題<h4>")
print(soup.find_all("h4"))

print("找全部的標題<h4> + 條件")
print(soup.find_all("h4", {"class": "pk"}))

print("多重取得")
cc = soup.find_all(["title", "p"])  # 多重取得, 找全部的 超標題<title> 和 段落<p>
print("共 :", len(cc), "個, 分別是 :")
for _ in cc:
    print(_)
print("直接取出第2項的內容 :")
print(soup.find_all(["title", "p"])[2].text)

# 用select選
print("h4:", soup.select("h4"))  # 選全部的h4標籤
print("#station2:", soup.select("#station2"))  # ←查詢所有 id 為 "station2" 的標籤
print(".pk:", soup.select(".pk"))  # ←查詢所有 class 為 "pk" 的標籤,  # 尋找class是pk
print("h4.bk", soup.select("h4.bk"))  # ←查詢所有 class 為 "bk" 的 h4 標籤

print(soup.select("#main button .pk"))

print(soup.select("#main button .pk")[1].text)
# print(soup.select("#footer a")[0]["href"])

# 用find找
# 1. 找下一個 + 條件
# 2. 找全部的 + 條件

print("找全部的")
cc = soup.find_all("title")  # 找全部的標題<title>
cc = soup.find_all("a")  # 找全部的超連結<a>
cc = soup.find_all("p")  # 找全部的段落<p>

print("共 :", len(cc), "個, 分別是 :")
for _ in cc:
    print(_)

cc = soup.find_all("a", {"class": "red"})  # 找全部的超連結<a> +  條件
print("共 :", len(cc), "個, 分別是 :")
for _ in cc:
    print(_)

print("多重取得")
cc = soup.find_all(["a", "p"])  # 多重取得, 找全部的 超連結<a> 和 段落<p>
print("共 :", len(cc), "個, 分別是 :")
for _ in cc:
    print(_)

print("找下一個段落<p>")
print(soup.find("p"))

print("找下一個段落<p> + 條件")
cc = soup.find("p", {"id": "p2", "class": "red"})
print(cc)

print("找下一個段落<p> + 條件")
cc = soup.find("p", id="p2", class_="red")
print(cc)

print("------------------------------")  # 30個

# 用select選
print("select() title")

print("選<title>")
cc = soup.select("title")  # 選全部的標題<title>
print(cc)

print("選<p>")
cc = soup.select("p")  # 選全部的段落<p>
print(cc)

print("選<#p1>")
cc = soup.select("#p1")
print(cc)

print("選<.red>")
cc = soup.select(".red")  # 尋找class是red
print(cc)

print("------------------------------")  # 30個

# 用select選
print("取得網頁中圖片的位址")
print(soup.select("img")[0].get("src"))
print(soup.select("img")[0]["src"])

print("取得網頁中的超連結")
print(soup.select("a")[0].get("href"))
print(soup.select("a")[0]["href"])

print("------------------------------")  # 30個

# 用find找

print("找下一個標題<h3>")
print(soup.find("h3"))  # <h3>標題</h3>

print("找下一個超連結<a> + 條件")
cc = soup.find("a", {"href": "https://www.youtube.com/"})
print(cc.text)  # First

print("------------------------------")  # 30個

# 用select選
data2 = soup.select("#link1")
print(data2[0].text)  # First
print(data2[0].get("href"))  # https://www.youtube.com/
print(data2[0]["href"])  # https://www.youtube.com/

print(soup.select("div img")[0]["src"])  # http://example.com/three.jpg

print("------------------------------")  # 30個

# 用.取
print("找下一個段落<p>")
print(soup.p.text)

print("找下一個段落<p> + 條件")
# print(soup.p["class"])

print("找下一個超連結<a>")
print(soup.a.text)

print("找下一個超連結<a>")
print(soup.a.text)

print("------------------------------")  # 30個

# 用find找
print("一一列出連結")
print("找全部的超連結<a>")
for link in soup.find_all("a"):  # 取得 全部 <a></a>
    print(link.get("href"))

print("------------------------------")  # 30個

# 用select選
for link in soup.select("a"):  # 選全部的超連結<a>
    print(link)  # 全部
    print(link.string)  # 內容
print("---------------")  # 15個
print(soup.select(".redcolor"))  # class="redcolor"  # 尋找class是redcolor
print("---------------")  # 15個
print(soup.select("#link3"))  # id="link3"
print("---------------")  # 15個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 讀取本地 html 3")

string_html_data = """
<html>
<body>
    <a href="https://www.google.com111/">超連結1</a><br>
    <a href="https://www.google.com222/">超連結2</a><br>
    <a href="https://www.google.com333/">超連結3</a><br>
    <a href="https://www.google.com444/">超連結4</a><br>
    <a href="https://www.google.com555/">超連結5</a><br>

    <p id="p1">段落1</p>
    <p id="p2" class="red">段落2 p2</p>
    <p id="p2" class="red">段落3 p3</p>
    <p id="p1">段落4</p>
    <p id="p1">段落5</p>

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
    <div>
    <p>我是段落</p>
    <img src="https://www.w3.org/html/logo/downloads/HTML5_Logo_256.png" alt="我是圖片">
    <a href="http://www.e-happy.com.tw">我是超連結</a>
    </div>
</body>
</html>
"""

soup = BeautifulSoup(string_html_data, "html.parser")
# soup = BeautifulSoup(string_html_data, "lxml")

print("------------------------------")  # 30個

# 用find找
print("找下一個超連結<a> + 條件")
cc = soup.find("a", {"href": "https://www.google.com333/"})
print(cc)
print(cc.text)

print("找全部的超連結<a>")
print(soup.find_all("a"))

print("找全部的超連結<a> +  條件")
print(soup.find_all("a", {"class": "red"}))

print("------------------------------")  # 30個

# 用find找
print("find 段落<p>")

print("找下一個段落<p>")
print(soup.find("p"))

print("找下一個段落<p>")
print(soup.find("p"))

print("找下一個段落<p>")
print(soup.find("p"))

print("找下一個段落<p> + 條件")
print(soup.find("p", {"id": "p2", "class": "red"}))

print("找下一個段落<p> + 條件")
print(soup.find("p", id="p2", class_="red"))

print("------------------------------")  # 30個

# 用select選
print("select() 全部 p")
print(soup.select("p"))  # 選全部的段落<p>
print("select() 全部 #p1")
print(soup.select("#p1"))
print("select() 全部 .red")
print(soup.select(".red"))  # 尋找class是red

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
print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 讀取本地 html 6")

string_html_data = """
<html>
  <head><meta charset="big5"><title>網頁標題9</title></head>
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
    <p id="p2" class="red">p2 : 第八章 : 更多關於正規表示式</p>
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

print("------------------------------")  # 30個

# 用find找

print("找下一個標題<h1>")
print(soup.find("h1"))  # 印出整行資料
print(soup.find("h1").text)  # 只印出text部分

print("找全部的超連結<a>")
print(soup.find_all("a"))

print("有3個, 需要縮小範圍")
print("找全部的超連結<a> +  條件")
print(soup.find_all("a", {"class": "red"}))

print("有2個, 需要縮小範圍")

print("找下一個超連結<a> + 條件")
cc = soup.find("a", {"href": "https://easun.org/perl/perl-toc/ch05.html"})
print("取得a 指明 href :", cc)  # 印出整行資料
print("取得a 指明 href :", cc.text)  # 只印出text部分

print("------------------------------")  # 30個

# 用select選
print("取得超連結")
cc = soup.select("#link1")
print("取得link1 :", cc)  # 印出整行資料
print("取得link1 text :", cc[0].text)  # 只印出text部分
print("取得link1 get :", cc[0].get("href"))  # https://easun.org/perl/perl-toc/ch01.html
print("取得link1 href :", cc[0]["href"])  # https://easun.org/perl/perl-toc/ch01.html

print("取得圖片超連結")
print(
    "取得div img :", soup.select("div img")[0]["src"]
)  # https://easun.org/perl/perl-toc/index_2.png

print("------------------------------")  # 30個

# 用find找
print("find 段落<p>")

print("找下一個段落<p>")
print(soup.find("p"))

print("找下一個段落<p> + 條件")
print("取得 p, p2 class red", soup.find("p", {"id": "p2", "class": "red"}))

print("找下一個段落<p> + 條件")
print("取得 p, p2 class red", soup.find("p", id="p2", class_="red"))

print("------------------------------")  # 30個

# 用select選
print("select() title")

print("select p", soup.select("p"))  # 選全部的段落<p>
print("select #p1", soup.select("#p1"))
print("select .red", soup.select(".red"))  # 尋找class是red

# 用select
print("取得圖片超連結 取得 img src", soup.select("img")[0].get("src"))
print("取得網頁超連結 取得 a href", soup.select("a")[0].get("href"))
print("取得圖片超連結 取得 img src", soup.select("img")[0]["src"])
print("取得網頁超連結 取得 a href", soup.select("a")[0]["href"])

print("多重條件選擇")
data = soup.select("div div p")  # 尋找 div 標籤裡面的 div 標籤裡面的 p 標籤 三者都要符合的抓出來
print("符合條件的資料", len(data), "筆")
print(data)

print("------------------------------")  # 30個

# 用find找
print("找下一個標題<h1>")
h1 = soup.find("h1")
print(h1)  # 印出整行資料
print(h1.text)  # 只印出text部分

print("尋找符合標籤的第一個節點 find by class")
# 使用class屬性定位，但因為在Python中已經有class保留字了，所以改用class_

print("找下一個內容分區元素<div> + 條件")
container = soup.find("div", class_="container")
print("取得div container :", container)  # 印出整行資料
print("取得div container :", container.text)  # 只印出text部分

print("尋找符合標籤的第一個節點 find by id")
# 用id屬性定位。
print("找下一個標題<h2> + 條件")
this = soup.find("h2", id="this")
print("取得h2 this :", this)  # 印出整行資料
print("取得h2 this :", this.text)  # 只印出text部分

print("找全部的標題<h2>")
h2s = soup.find_all("h2")  # 取得 全部 <h2></h2>
length = len(h2s)
print("共找到", length, "筆資料")
for nn in range(length):
    print(h2s[nn].text)  # 使用索引值, 只印出text部分
# print("取得全部 h2 :", h2s)        #印出全部資料, 一個list

# 定位多個標籤，則將標籤打包成一個列表就好了。limit屬性則可以限制數量。
print("多重取得 + 條件")
h1_h2s = soup.find_all(["h1", "h2"], limit=3)  # 多重取得, 找全部的 標題1<h1> 和 標題2<h2>
length = len(h1_h2s)
print("共找到", length, "筆資料")
for nn in range(length):
    print(h1_h2s[nn].text)  # 使用索引值, 只印出text部分
# print("取得全部 h1 h2 :", h1_h2s)        #印出全部資料, 一個list

# 用select_one
# select_one()使用CSS選擇器的語法來定位節點
h1 = soup.select_one("h1")
print(h1)
print("取得<h1>??</h1> :", h1)  # 印出整行資料
print("取得<h1>??</h1> :", h1.text)  # 只印出text部分

h2s = soup.select("h2")  # 選全部的h2標籤
length = len(h2s)
print("共找到", length, "筆資料")
for nn in range(length):
    print(h2s[nn].text)  # 使用索引值, 只印出text部分
# print("取得全部 h2 :", h2s)        #印出全部資料, 一個list

# 用select_one by class
# class 定位
p = soup.select_one("div.container")
print("取得div.container :", p)  # 印出整行資料
print("取得div.container :", p.text)  # 只印出text部分

# 用select_one by id
# id定位
this = soup.select_one("h2#this")
print("h2#this :", this)  # 印出整行資料
print("h2#this :", this.text)  # 只印出text部分

# 尋找parent和sibling

print("找下一個標題<h2> + 條件")
# this = soup.find("h2", id="this")
# print(this)
# print(this.find_previous_sibling())
# print(this.find_next_sibling())
# print(this.find_parent())

# 取得文字
# 定位到指定的節點後，可以使用text或string取得文字，或者也可以用getText()
print("找下一個標題<h1>")
h1 = soup.find("h1")
print("h1 getText() :", h1.getText())
print("h1 text :", h1.text)
print("h1 strint :", h1.string)
print("取得<h1>??</h1> :", h1)  # 印出整行資料
print("取得<h1>??</h1> :", h1.text)  # 只印出text部分

print("------------------------------")  # 30個

# 取得屬性值
# 對於有屬性值的節點，就用get("屬性")或類似字典的方式["屬性"]取得屬性值。
# 取得<img>標籤中的src屬性值：
img = soup.find("img")
print("取得圖片超連結 取得 img src", img["src"])
print("取得圖片超連結 取得 img src", img.get("src"))

print("下載圖片 另存新檔")
filename = img["src"].split("/")[-1]  # 取得圖檔名
filename2 = "tmp_" + filename
img = requests.get(img["src"])
with open(filename2, "wb") as file:
    file.write(img.content)
print("圖片下載完成, 檔案 : " + filename2)

print("------------------------------")  # 30個

print("下載網頁中的所有圖片")

# 以標題建立目錄儲存圖片
title = soup.title.text
download_image_dir = "下載圖片_" + title + "/"
if not os.path.exists(download_image_dir):
    os.mkdir(download_image_dir)

# 用find找
print("找全部的影像<img>")
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
            with open(os.path.join(download_image_dir, filename), "wb") as f:
                f.write(image.read())  
            n+=1
            if n>=1000: # 最多下載 1000 張
                break
            """
        except:
            print("{} 無法讀取!".format(filename))

print("共下載", n, "張圖片")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 讀取本地 html 7")

string_html_data = """
<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <title>網頁標題10</title>
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
    <h1 id="author">朱冶蕙</h1>
    <img src="picture1.jpg" width="100">
    
    <section>
       <h1 id="content">第一本書</h1>
       <p>這是<strong>朱冶蕙</strong>老師寫的第二本書</p>
       <img src="picture2.jpg" width="150"
    </section>
    
    <section>
       <h1 id="content">第二本書</h1>
       <p>這是朱冶蕙老師寫的第二本書</p>
       <img src="picture3.jpg" width="200">
    </section>
    
</body>
</html>
"""

soup = BeautifulSoup(string_html_data, "lxml")

print("------------------------------")  # 30個

# 用find找

print("找下一個標題<h1>")
cc = soup.find("h1")
print("資料型態       = ", type(cc))
print("列印Tag        = ", cc)
print("Text屬性內容   = ", cc.text)
print("String屬性內容 = ", cc.string)

print("找全部的標題<h1> + 條件")
cc = soup.find_all("h1", limit=2)  # 取得 全部 <h1></h1>
for c in cc:  # 列印串列元素內容
    print(c.text)

print("找全部的標題<h1>")
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

# 用find找
cc = soup.find(id="author")
print(cc)
print(cc.text)

print("------------------------------")  # 30個

# 用find找

print("找全部的標題<h4> + 條件")  # ???
cc = soup.find_all(id="content")
for c in cc:
    print(c)
    print(c.text)

print("------------------------------")  # 30個

# 用select選
cc = soup.select("#author")
print("資料型態     = ", type(cc))  # 列印資料型態
print("串列長度     = ", len(cc))  # 列印串列長度
print("元素資料型態 = ", type(cc[0]))  # 列印元素資料型態
print("元素內容     = ", cc[0].getText())  # 列印元素內容

print("------------------------------")  # 30個

# 用select選
cc = soup.select("#author")
print("列出串列元素的資料型態    = ", type(cc[0]))
print(cc[0])
print("列出str()轉換過的資料型態 = ", type(str(cc[0])))
print(str(cc[0]))

print("------------------------------")  # 30個

# 用select選
cc = soup.select("#author")
print(str(cc[0].attrs))

print("------------------------------")  # 30個

# 用select選
cc = soup.select("p")  # 選全部的段落<p>

print("含<p>標籤的串列長度 = ", len(cc))
for c in cc:
    print(str(cc))  # 內部有子標籤<strong>字串
    print(c.getText())  # 沒有子標籤
    print(c.text)  # 沒有子標籤

print("------------------------------")  # 30個

tags = soup("img")  # 找全部的影像<img>
print("全部的影像<img>, 共 :", len(tags), "個")
print(tags)
for tag in tags:
    print(tag)
    print("圖片網址 :", tag.get("src", None))
    # print("alt屬性 :", tag["alt"])
    print("屬性 :", tag.attrs)

print("------------------------------")  # 30個

# 用select選
cc = soup.select("img")  # 選全部的圖片<img>
print("全部的影像<img>, 共 :", len(cc), "個")
for c in cc:
    print("列印標籤串列 = ", c)
    print("列印圖檔     = ", c.get("src"))
    print("列印圖檔     = ", c["src"])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 讀取本地 html 1")

# 讀取遠端檔案
# html_data = requests.get("https://fchart.github.io/ML/Surveys.html")
# html_data.encoding = "utf8"
# soup = BeautifulSoup(html_data.text, "lxml")

# 讀取本地檔案
with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
    # print("整個網頁資料 :", soup)

print("------------------------------")  # 30個

# 搜尋<a>標籤
print("找下一個超連結<a>")
tag_a = soup.find("a")
print(tag_a)
print(tag_a.text)

print("找下一個段落<p>")
print(soup.find("p"))

# 呼叫多次find()方法

print("段落<p>內有連結<a>")
tag_p = soup.find("p")
print(tag_p)

print("段落<p>內找連結<a>")
tag_a = tag_p.find("a")
print(tag_a)
print(tag_p.a.text)
print(tag_a.text)

print("------------------------------")  # 30個

# 走訪下一層HTML標籤
print(soup.html.body.div.div.p.a.text)

print("------------------------------")  # 30個

# 走訪上一層HTML標籤
tag_div = soup.select_one("#q1")  # 找到第1題的<div>標籤
tag_li = tag_div.ul.li  # 走訪到之下的<ul>
print(tag_li.text)
# 使用parent屬性取得父標籤
print(tag_li.parent.parent.p.a.text)

print("------------------------------")  # 30個

tag_div = soup.select_one("#q2")  # 找到第2題的<div>標籤
print(tag_div.find_previous_sibling().p.a.text)
print(tag_div.find_next_sibling().p.a.text)

print("------------------------------")  # 30個

# 使用id屬性搜尋<div>標籤
tag_div = soup.find(id="q2")

print("找下一個超連結<a>")
tag_a = tag_div.find("a")
print(tag_a.text)

print("------------------------------")  # 30個

# 使用class屬性搜尋<span>標籤
tag_span = soup.find(attrs={"class": "score"})
print(tag_span.text)

# 搜尋第2題的第1個<span>標籤
tag_div = soup.find(id="q2")
tag_span = tag_div.find(class_="score")
print(tag_span.text)

print("------------------------------")  # 30個

# 使用HTML5的data-屬性搜尋<div>標籤
tag_div = soup.find(attrs={"data-custom": "important"})
print(tag_div.text)

print("------------------------------")  # 30個

# 使用文字內容來搜尋標籤
tag_str = soup.find(text="請問你的")
print(tag_str)
tag_str = soup.find(text="10")
print(tag_str)
print(type(tag_str))  # NavigableString型態
print(tag_str.parent.name)  # 父標籤名稱
tag_str = soup.find(text="男 - ")
print(tag_str)

print("------------------------------")  # 30個

# 測試取出<li>標籤的內容
tag_str = soup.find(text="女 - ")
print(tag_str)
tag_li = soup.find(class_="response")
print(tag_li.text)
print(tag_li.string)
print(tag_li.span.string)

print("------------------------------")  # 30個

# 使用多條件來搜尋HTML標籤
print("找下一個內容分區元素<div> + 條件")
tag_div = soup.find("div", class_="question")
print(tag_div.prettify())  # pretty打印

print("找下一個段落<p> + 條件")
tag_p = soup.find("p", class_="question")
print(tag_p.prettify())  # pretty打印

print("------------------------------")  # 30個


# 使用函數建立搜尋條件
def is_secondary_question(tag):
    return tag.has_attr("href") and tag.get("href") == "http://example.com/q2"


tag_a = soup.find(is_secondary_question)
print(tag_a.prettify())  # pretty打印

print("------------------------------")  # 30個

# 找出所有問卷的題目串列
print("找全部的段落<p> + 條件")
tag_list = soup.find_all("p", class_="question")
print(tag_list[0].prettify())  # pretty打印

for question in tag_list:
    print(question.a.text)

print("------------------------------")  # 30個

# 找出前2個問卷的題目串列
print("找全部的段落<p> + 條件")
tag_list = soup.find_all("p", class_="question", limit=2)
print(len(tag_list))

for question in tag_list:
    print(question.a.text)

print("------------------------------")  # 30個

print("找下一個內容分區元素<div> + 條件")
tag_div = soup.find("div", id="q2")

# 找出所有標籤串列
tag_all = tag_div.find_all(True)
for tag in tag_all:
    print(tag.name)

print("------------------------------")  # 30個

print("找下一個內容分區元素<div> + 條件")
tag_div = soup.find("div", id="q2")

# 找出所有文字內容串列
tag_str_list = tag_div.find_all(text=True)
print(tag_str_list)

# 找出指定的文字內容串列
tag_str_list = tag_div.find_all(text=["20", "40"])
print(tag_str_list)

print("------------------------------")  # 30個

print("找下一個內容分區元素<div> + 條件")
tag_div = soup.find("div", id="q2")

print("多重取得, 找出所有<p>和<span>標籤")
tag_list = tag_div.find_all(["p", "span"])  # 多重取得, 找全部的 段落<p> 和 xx<span>
for tag in tag_list:
    print(tag.name, tag.text.replace("\n", ""))

print("------------------------------")  # 30個

# 找出class屬性值question或selected的所有標籤
tag_list = tag_div.find_all(class_=["question", "selected"])
for tag in tag_list:
    print(tag.name, tag.text.replace("\n", ""))

print("------------------------------")  # 30個

print("找下一個內容分區元素<div> + 條件")
tag_div = soup.find("div", id="q2")
# 找出所有<li>子孫標籤
tag_list = tag_div.find_all("li")
for tag in tag_list:
    print(tag.text.replace("\n", ""))

# 沒有使用遞迴來找出所有<li>標籤
tag_list = tag_div.find_all("li", recursive=False)
print(tag_list)

print("------------------------------")  # 30個

# 搜尋<title>標籤和第3個<div>標籤
tag_title = soup.select("title")  # 選全部的標題<title>
print(tag_title[0].text)

print("找下一個內容分區元素<div> + 條件")
tag_first_div = soup.find("div")

tag_div = tag_first_div.select("div:nth-of-type(3)")
print(tag_div[0].prettify())  # pretty打印

print("------------------------------")  # 30個

# 搜尋class和id屬性值的標籤
tag_div = soup.select("#q1")
print(tag_div[0].p.a.text)

tag_span = soup.select("span#email")
print(tag_span[0].text)

tag_div = soup.select("#q1, #q2")  # 多個id屬性
for item in tag_div:
    print(item.p.a.text)

print("------------------------------")  # 30個

print("找下一個內容分區元素<div> + 條件")
tag_div = soup.find("div")  # 第1個<div>標籤

tag_p = tag_div.select(".question")  # 尋找class是question
for item in tag_p:
    print(item.a["href"])

tag_span = soup.select("[class~=selected]")
for item in tag_span:
    print(item.text)

print("------------------------------")  # 30個


# 搜尋特定屬性值的標籤
def print_a(tag_a):
    for tag in tag_a:
        print(tag["href"])
    print("---------------")  # 15個


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

print("------------------------------")  # 30個

# 搜尋<title>標籤, 和<div>標籤下的所有<a>標籤
tag_title = soup.select("html head title")  # 選全部的<html><head><title>
print(tag_title[0].text)
tag_a = soup.select("body div a")
for tag in tag_a:
    print(tag["href"])

print("------------------------------")  # 30個

# 搜尋指定標籤下的直接子標籤
tag_a = soup.select("p > a")
for tag in tag_a:
    print(tag["href"])
tag_li = soup.select("ul > li:nth-of-type(2)")
for tag in tag_li:
    print(tag.text.replace("\n", ""))
tag_span = soup.select("div > #email")
for tag in tag_span:
    print(tag.prettify())  # pretty打印

print("------------------------------")  # 30個

# 搜尋兄弟標籤
tag_div = soup.find(id="q1")
print(tag_div.p.a.text)

print("---------------")  # 15個

tag_div = soup.select("#q1 ~ .survey")
for item in tag_div:
    print(item.p.a.text)

print("---------------")  # 15個

tag_div = soup.select("#q1 + .survey")
for item in tag_div:
    print(item.p.a.text)

print("------------------------------")  # 30個

# 使用select_one()方法搜尋標籤
tag_a = soup.select_one("a[href]")
print(tag_a.prettify())  # pretty打印

print("------------------------------")  # 30個

# 使用正規表達式搜尋文字內容
tag_str = soup.find(text="男 -")
print(tag_str)
regexp = re.compile("男 -")
tag_str = soup.find(text=regexp)
print(tag_str)

print("---------------")  # 15個

regexp = re.compile("\w+ -")
tag_list = soup.find_all(text=regexp)
print(tag_list)

print("------------------------------")  # 30個

# 使用正規表達式搜尋電子郵件地址
email_regexp = re.compile("\w+@\w+\.\w+")
tag_str = soup.find(text=email_regexp)
print(tag_str)

print("---------------")  # 15個

tag_list = soup.find_all(text=email_regexp)
print(tag_list)

print("------------------------------")  # 30個

# 使用正規表達式搜尋URL網址
url_regexp = re.compile("^http:")
tag = soup.find(href=url_regexp)
print(tag["href"], tag.text)

print("---------------")  # 15個

tag_list = soup.find_all(href=url_regexp)
for tag in tag_list:
    print(tag["href"], tag.text)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

fp = open("data/Example.html", "r", encoding="utf8")
string_html_data = fp.read()
print("檔案內容:")
print(string_html_data)

print("------------------------------")  # 30個

# 搜尋HTML標籤
soup = BeautifulSoup(string_html_data, "lxml")
tag_a = soup.find("a")
print(tag_a.string)

# 搜尋HTML標籤的id屬性
tag_div = soup.find(id="q2")
tag_a = tag_div.find("a")
print(tag_a.string)

# class樣式屬性
tag_li = soup.find(attrs={"class": "response"})
tag_span = tag_li.find("span")
print(tag_span.string)

print("------------------------------")  # 30個

# 搜尋HTML標籤
tag_div = soup.find(attrs={"data-custom": "important"})
print(tag_div.string)

print("------------------------------")  # 30個

# 搜尋HTML標籤
tag_div = soup.find(attrs={"id": "email"})
print(tag_div.string)

print("------------------------------")  # 30個

tag_div = soup.find("div", class_="question")
print(tag_div)
print(tag_div.string)

print("------------------------------")  # 30個

tag_p = soup.find("p", class_="question")
print(tag_p)

# tag_p = soup.find("p", class_="question")
# tag_a = tag_p.find("a")
# print(tag_a.string)


# Python函數定義搜尋條件
def is_secondary_question(tag):
    return tag.has_attr("href") and tag.get("href") == "http://example.com/q2"


tag_a = soup.find(is_secondary_question)
print(tag_a)

# 找出所有問卷的題目字串
tag_list = soup.find_all("p", class_="question")
print(tag_list)
for question in tag_list:
    print(question.a.string)

print("------------------------------")  # 30個

# 使用limit參數限制搜尋數量
tag_list = soup.find_all("p", class_="question", limit=1)
print(tag_list)
for question in tag_list:
    print(question.a.string)

print("------------------------------")  # 30個

# 搜尋所有標籤
tag_div = soup.find("div", id="q2")
# 找出所有標籤清單
tag_all = tag_div.find_all(True)
print(tag_all)

print("------------------------------")  # 30個

# 搜尋所有文字內容
tag_div = soup.find("div", id="q2")
# 找出所有文字內容清單
tag_str_list = tag_div.find_all(text=True)
print(tag_str_list)

print("------------------------------")  # 30個

# 找出指定的文字內容清單
tag_str_list = tag_div.find_all(text=["20", "40"])
print(tag_str_list)

# 清單指定搜尋條件
tag_div = soup.find("div", id="q2")
# 找出所有<p>和<span>標籤
tag_list = tag_div.find_all(["p", "span"])
print(tag_list)

print("------------------------------")  # 30個

# 找出class屬性值question或selected的所有標籤
tag_list = tag_div.find_all(class_=["question", "selected"])
print(tag_list)

# 沒有使用遞迴來執行搜尋
tag_div = soup.find("div", id="q2")
# 找出所有<li>子孫標籤
tag_list = tag_div.find_all("li")
print(tag_list)

print("------------------------------")  # 30個

# 沒有使用遞迴來找出所有<li>標籤
tag_list = tag_div.find_all("li", recursive=False)
print(tag_list)

# 正規表達式搜尋文字內容
regexp = re.compile("男-")
tag_str = soup.find(text=regexp)
print(tag_str)
regexp = re.compile("\w+-")  # 字元+-
tag_list = soup.find_all(text=regexp)
print(tag_list)

# 使用正規表達式搜尋電子郵件地址
email_regexp = re.compile("\w+@\w+\.\w+")
tag_str = soup.find(text=email_regexp)
print(tag_str)
print("---------------")  # 15個
tag_list = soup.find_all(text=email_regexp)
print(tag_list)

# 使用正規表達式搜尋URL網址
url_regexp = re.compile("^http:")
tag_href = soup.find(href=url_regexp)
print(tag_href)
print("---------------")  # 15個
tag_list = soup.find_all(href=url_regexp)
print(tag_list)
print("---------------")  # 15個
print(tag_list[0].string)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

with open("data/Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")

# 使用childen屬性取得子標籤
tag_div = soup.select("#q2")  # 找到第2題
tag_ul = tag_div[0].ul  # 走訪到之下的<ul>
for child in tag_ul.children:
    print(type(child))

print("------------------------------")  # 30個

# 使用childen屬性取得子標籤
tag_div = soup.select("#q2")  # 找到第2題
tag_ul = tag_div[0].ul  # 走訪到之下的<ul>
for child in tag_ul.children:
    if not isinstance(child, NavigableString):
        print(child.name)

print("------------------------------")  # 30個

# 使用屬性向下走訪
print(soup.html.head.meta["charset"])
# 使用div屬性取得第1個<div>標籤
print(soup.html.body.div.div.p.a.string)

print("------------------------------")  # 30個

# 使用屬性取得所有子標籤
tag_div = soup.select("#q2")  # 找到第2題
tag_ul = tag_div[0].ul  # 走訪到之下的<ul>
for child in tag_ul.contents:
    if not isinstance(child, NavigableString):
        print(child.span.string)

print("------------------------------")  # 30個

# 使用屬性取得所有子標籤
tag_div = soup.select("#q2")  # 找到第2題
tag_ul = tag_div[0].ul  # 走訪到之下的<ul>
for child in tag_ul.children:
    if not isinstance(child, NavigableString):
        print(child.name)
        for tag in child:
            if not isinstance(tag, NavigableString):
                print(tag.name, tag.string)
            else:
                print(tag.replace("\n", ""))

print("------------------------------")  # 30個

# 使用屬性取得所有子孫標籤
tag_div = soup.select("#q2")  # 找到第2題
tag_ul = tag_div[0].ul  # 走訪到之下的<ul>
for child in tag_ul.descendants:
    if not isinstance(child, NavigableString):
        print(child.name)

print("------------------------------")  # 30個

# 使用屬性取得所有子孫的文字內容
tag_div = soup.select("#q2")  # 找到第2題
tag_ul = tag_div[0].ul  # 走訪到之下的<ul>
for string in tag_ul.strings:
    print(string.replace("\n", ""))

print("------------------------------")  # 30個

tag_div = soup.select("#q2")  # 找到第2題
tag_ul = tag_div[0].ul  # 走訪到之下的<ul>
# 使用屬性取得父標籤
print(tag_ul.parent.name)
# 使用函數取得父標籤
print(tag_ul.find_parent().name)

print("------------------------------")  # 30個

tag_div = soup.select("#q2")  # 找到第2題
tag_ul = tag_div[0].ul  # 走訪到之下的<ul>
# 使用屬性取得所有祖先標籤
for tag in tag_ul.parents:
    print(tag.name)
# 使用函數取得所有祖先標籤
for tag in tag_ul.find_parents():
    print(tag.name)

print("------------------------------")  # 30個

tag_div = soup.select("#q2")  # 找到第2題
first_li = tag_div[0].ul.li  # 第1個<li>
print(first_li)
# 使用next_sibling屬性取得下一個兄弟標籤
second_li = first_li.next_sibling.next_sibling
print(second_li)
# 呼叫next_sibling()函數取得下一個兄弟標籤
third_li = second_li.find_next_sibling()
print(third_li)

print("------------------------------")  # 30個

# 呼叫next_siblings()函數取得所有兄弟標籤
for tag in first_li.find_next_siblings():
    print(tag.name, tag.span.string)

print("------------------------------")  # 30個

tag_div = soup.select("#q2")  # 找到第2題
tag_li = tag_div[0].ul.li  # 第1個<li>
third_li = tag_li.find_next_sibling().find_next_sibling()
print(third_li)
# 使用previous_sibling屬性取得前一個兄弟標籤
second_li = third_li.previous_sibling.previous_sibling
print(second_li)
# 呼叫previous_sibling()函數取得前一個兄弟標籤
first_li = second_li.find_previous_sibling()
print(first_li)

print("------------------------------")  # 30個

# 呼叫previous_siblings()函數取得所有兄弟標籤
for tag in third_li.find_previous_siblings():
    print(tag.name, tag.span.string)

print("------------------------------")  # 30個

tag_html = soup.html  # 找到第<html>標籤
print(type(tag_html), tag_html.name)

tag_next = tag_html.next_element.next_element
print(type(tag_next), tag_next.name)

tag_title = soup.title  # 找到第<title>標籤
print(type(tag_title), tag_title.name)

tag_previous = tag_title.previous_element.previous_element
print(type(tag_previous), tag_previous.name)

print("------------------------------")  # 30個

tag_div = soup.find(id="emails")
for element in tag_div.next_elements:
    if not isinstance(element, NavigableString):
        print(element.name)

print("------------------------------")  # 30個

tag_div = soup.find(id="q1")
for element in tag_div.previous_elements:
    if not isinstance(element, NavigableString):
        print(element.name)

print("------------------------------------------------------------")  # 60個
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
<h1 style="color:rgb(255, 199, 125);">優質大學推薦</h1>
<h1 style="color:rgb(126, 168, 168);">優質高中推薦</h1>
<h3 style="background-color:green; color:yellow; font-family:Segoe Script; border:3px #000000 solid;">勵志名句</h1>
一分努力~~ 一分收獲~~
金誠所至~~ 金石為開~~
</body>
</html>
"""
print("------------------------------------------------------------")  # 60個
print("讀取本地html SP")
print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 01 抓取一個網頁的所有圖片檔")

# 文淵閣工作室官網
url = "http://www.e-happy.com.tw"

domain = "{}://{}".format(
    urllib.parse.urlparse(url).scheme, urllib.parse.urlparse(url).hostname
)
print("domain :", domain)

html_data = get_html_data1(url)
soup = BeautifulSoup(html_data.text, "html.parser")

print("多重取得")
all_links = soup.find_all(["a", "img"])  # 多重取得, 找全部的 超連結<a> 和 影像<img>

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
                print("A遠端檔案 :", full_path)
            else:
                full_path = domain + t
                print("B遠端檔案 :", full_path)
            download_image_dir = url.split("/")[-1]
            download_image_dir = "tmp_image_dir"
            if not os.path.exists(download_image_dir):
                os.mkdir(download_image_dir)
            filename = full_path.split("/")[-1]
            ext = filename.split(".")[-1]
            filename = filename.split(".")[-2]
            if "jpg" in ext:
                filename = filename + ".jpg"
            else:
                filename = filename + ".png"

            print(filename)
            image = urlopen(full_path)
            cc = os.path.join(download_image_dir, filename)
            print(cc)
            print("------------------------------")  # 30個
            fp = open(os.path.join(download_image_dir, filename), "wb")
            fp.write(image.read())
            fp.close()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 02")

url = "https://tw.news.yahoo.com/rss/technology"
soup = get_soup_from_url(url)

# 用find找
cc = soup.findAll("item")
print("取得Yahoo奇摩新聞-科技新聞-標題")
for news in cc:
    print(news.title)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 06")

url = "https://newcar.u-car.com.tw/newcar"
soup = get_soup_from_url(url)

print("抓出 下拉式選單 的項目")

# 用select選
makes = soup.select("#makeselect > option")
makers = dict()
for make in makes:
    if make["value"] != "0":
        makers[int(make["value"])] = make.text
print(makers)

# 用select選
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
print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 09a udn news")

# 聯合新聞網
url = "https://udn.com/news/breaknews/1"
soup = get_soup_from_url(url)

# 用find找
print("找全部的標題<h2> + 條件")
target = soup.find_all("h2", {"class": "breaking-news"})
# print(target)

print("聯合新聞網 快訊")
for news in target:
    print(news.a["title"])

print("------------------------------")  # 30個

# 用find找
# print("找全部的超連結<a> + 條件")?????
all_links = soup.find_all(class_="story-list__text")
# print(all_links)

headlines = list()  # 串列, 裡面放字典

for link in all_links:
    title = link.find("h2")
    try:
        # print(title.a["title"])
        # print(title.a["href"])
        item = dict()  # 字典
        item["title"] = title.a["title"]
        if not title.a["href"].startswith("http"):
            item["link"] = "https://udn.com{}".format(title.a["href"])
        else:
            item["link"] = title.a["href"]
        headlines.append(item)
    except:
        pass

"""
print(len(headlines))
print(headlines)
print(type(headlines))
print(type(headlines[0]))
"""
print("看5筆資料")
for i in range(5):
    print(headlines[i])

print("------------------------------------------------------------")  # 60個

url = "https://udn.com/news/breaknews/1"  # 聯合新聞網

domain = "{}://{}".format(
    urllib.parse.urlparse(url).scheme, urllib.parse.urlparse(url).hostname
)
print("domain :", domain)

soup = get_soup_from_url(url)
print(soup)

# 用find找
print("多重取得")
all_links = soup.find_all(["a", "img"])  # 多重取得, 找全部的 超連結<a> 和 影像<img>
# print(all_links)

cnt = 0
for link in all_links:
    src = link.get("src")
    href = link.get("href")
    targets = [src, href]
    # print(targets)
    for t in targets:
        if t != None and (".jpg" in t or ".png" in t):
            if t.startswith("https"):
                print("aa")
                full_path = t
            else:
                print("bbxxxxxxx")
                full_path = domain + t
            print(full_path)
            cnt += 1
            if cnt > 5:
                break

            download_image_dir = url.split("/")[-1]
            if not os.path.exists(download_image_dir):
                os.mkdir(download_image_dir)
            filename = full_path.split("/")[-1]
            ext = filename.split(".")[-1]
            filename = filename.split(".")[-2]
            if "jpg" in ext:
                filename = filename + ".jpg"
            else:
                filename = filename + ".png"
            image = urlopen(full_path)
            fp = open(os.path.join(download_image_dir, filename), "wb")
            fp.write(image.read())
            fp.close()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 12")

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
print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 13")

url = "https://www.mvdis.gov.tw/m3-emv-plate/webpickno/queryPickNo#"
# html_data = requests.get(url)
# soup = BeautifulSoup(html_data.text, "html.parser")
soup = get_soup_from_url(url)

# 用find找
captcha_image = soup.find("img", id="pickimg")["src"]

# print("找全部的超連結<a> + 條件")????
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

print("找全部的超連結<a> +  條件")
plate_numbers = soup.find_all("a", "number")
print(plate_numbers)

for plate_number in plate_numbers:
    print("aaaaaaaaaaaaaa")
    print(plate_number.text)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 14")

# Python 測試 BeautifulSoup Yahoo電影 台北票房榜

from urllib import request
from urllib import parse

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
    html_data = html_data.decode("utf-8")
    print(html_data)
    soup = BeautifulSoup(html_data, "html.parser")
    print("找全部的內容分區元素<div> + 條件")
    rows = soup.find_all("div", class_ = "tr")

    colname = list(rows.pop(0).stripped_strings)
    contents = []
    for row in rows:
        thisweek_rank = row.find_next("div" , attrs={"class" : "td"})
        updown = thisweek_rank.find_next("div")
        lastweek_rank = updown.find_next("div")

        if thisweek_rank.string == str(1):
            movie_title = lastweek_rank.find_next("h2")
        else:
            movie_title = lastweek_rank.find_next("div" , attrs={"class" : "rank_txt"})

        release_date = movie_title.find_next("div" , attrs={"class" : "td"})
        trailer = release_date.find_next("div" , attrs={"class" : "td"})

        if trailer.find("a") is None:
            trailer_address = ""
        else:
            trailer_address = trailer.find("a")["href"]

        starts = row.find("h6" , attrs={"class" : "count"})
        lastweek_rank = lastweek_rank.string if lastweek_rank.string else ""

        c = [thisweek_rank.string , lastweek_rank , movie_title.string , release_date.string , trailer_address , starts.string]
        print("加入: ", c)
        contents.append(c)

print(contents)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 15 KKBOX")

# KKBOX華語新歌日榜
# 舊版 OK
url = "https://kma.kkbox.com/charts/api/v1/daily?category=390&lang=tc&limit=50&terr=tw&type=newrelease"
# 新版NG
# url = "https://kma.kkbox.com/charts/daily/newrelease?cate=390&lang=tc&terr=tw"

# 取得歌曲資訊json檔
html_data = requests.get(url)
# print(html_data.status_code)
# print(html_data.text)

# 將json字串轉為Python的字典型態
data = json.loads(html_data.text)
song_list = data["data"]["charts"]["newrelease"]

# 印10筆資料就好
cnt = 0
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

    # 從歌曲連結取得歌詞
    # html_data = requests.get(song_url)
    # soup = BeautifulSoup(html_data.text, "html.parser")
    # print("找下一個內容分區元素<div> + 條件")
    # lyric = soup.find("div", class_="lyrics").text
    # print("歌詞:", lyric)
    print("------------------------------")  # 30個
    cnt += 1
    if cnt == 10:
        break

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 16 好樂迪")

# Python 測試 BeautifulSoup 好樂迪 K歌排行

from urllib import request
from urllib import parse

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
	resp = res_obj.read().decode("utf-8")
        # 使用 html.parser
	soup = BeautifulSoup(resp , "html.parser")
        # 用 find 找到 id 為 ctl00_ContentPlaceHolder1_dgSong 的 table 標籤，並回傳 table 內全部的 tr 內容
	rank_table = soup.find("table", id="ctl00_ContentPlaceHolder1_dgSong").find_all("tr")

        #由於要避開 table 的第一列 tr 資料以及最後一列 tr 資料，所以取 [1:-2] 
	for rt in rank_table[1:-2]:
               # 找到全部的 td 並取得第 5 個 td(index 是 4)
		song_name = rt.find_all("td")[4]
               # 找到第一個 a 這個標籤，因為只有歌手的資料被 a tag 包住
		singer = rt.find("a")
        # 把歌曲跟歌手的資料轉成 string 並去前後空白塞到一個 song_list
	song_list.append([song_name.string.strip(), singer.string.strip()])

# 把 song_list 使用 pandas 模組轉成 dataframe 用於後面資料分析
df = pd.DataFrame(song_list,columns=["song", "singer"])
print(df)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 博碩文化新書網頁
url = "http://www.drmaster.com.tw/Publish_Newbook.asp"
html_data = requests.get(url)
html_data.encoding = "utf-8"

print("網址：%s" % (html_data.url))
print("狀態：%s" % (html_data.status_code))
print("表頭：%s" % (html_data.headers))
print("網頁程式碼：%s" % (html_data.text))

"""
Response屬性
content 取得二進位資料 例如可以取得網路圖檔
encoding 取得或設定網頁的編碼模式
headers 取得網頁的表頭資訊
text 取得網頁的所有程式碼
status_code 取得網頁的連線狀態
    200: 請求成功
    400 伺服器無法理解請求
    404伺服器找不到請求資源, 可能是連接的url錯誤
url 取得網頁的網址
"""
print("------------------------------------------------------------")  # 60個

# 博碩文化新書網頁
url = "http://www.drmaster.com.tw/Publish_Newbook.asp"
html_data = requests.get(url)
html_data.encoding = "utf-8"
soup = BeautifulSoup(html_data.text, "html.parser")
# soup = get_soup_from_url(url)

listBookName = soup.select(".style2")  # 尋找class是style2
count = len(listBookName)
print("共 %d 筆新書記錄" % (count))  # 顯示 "共 20 筆新書記錄"

print("顯示網頁新書書名")
for book in listBookName:
    print(book.text)

print("------------------------------")  # 30個

listImageUrl = soup.select("td a img")

for link in listImageUrl:
    # if("http" in link.get("src")):
    print(link.get("src"))

print("------------------------------------------------------------")  # 60個

# htmlparse06.py   http讀圖部分還沒好

import shutil

# 若程式的路徑有images資料即刪除，否則即建立images
download_image_dir = "images"
if os.path.exists(download_image_dir):
    shutil.rmtree(download_image_dir)
os.mkdir(download_image_dir)

# 博碩文化新書網頁
url = "http://www.drmaster.com.tw/Publish_Newbook.asp"
html_data = requests.get(url)
html_data.encoding = "utf-8"
soup = BeautifulSoup(html_data.text, "html.parser")
# soup = get_soup_from_url(url)

listImageUrl = soup.select("td a img")
# 逐一取得博碩新書圖檔並放入images資料夾下
n = 0
for link in listImageUrl:
    print(link.get("src"))
    imgUrl = link.get("src")
    if "http" in imgUrl:
        imgName = imgUrl.split("/")[-1]
        html_data = requests.get(imgUrl)
        f = open(download_image_dir + "/" + imgName, "wb")  # 指定開啟檔案路徑
        # 將response.content二進位內容寫入指定的圖檔名稱
        f.write(html_data.content)
        f.close()
        print("%s 下載完成" % (imgName))
        n += 1
print("共下載 %d 張圖檔" % (n))

print("------------------------------------------------------------")  # 60個

home = "https://www.drmaster.com.tw/"

import shutil

# 若程式的路徑有images資料即刪除，否則即建立images
download_image_dir = "images"
if os.path.exists(download_image_dir):
    shutil.rmtree(download_image_dir)
os.mkdir(download_image_dir)
pageName = "newbook.html"
if os.path.exists(pageName):
    os.remove(pageName)

# 博碩文化新書網頁
url = "http://www.drmaster.com.tw/Publish_Newbook.asp"
html_data = requests.get(url)
html_data.encoding = "utf-8"
soup = BeautifulSoup(html_data.text, "html.parser")
# soup = get_soup_from_url(url)

listImageUrl = soup.select("td a img")
listImageUrlOk = []
listBookName = soup.select(".style2")  # 尋找class是style2

# 逐一取得博碩新書圖檔並放入images資料夾下
for link in listImageUrl:
    imgUrl = link.get("src")
    imgUrl = home + imgUrl
    print("url :", imgUrl)
    if "http" in imgUrl:
        imgName = imgUrl.split("/")[-1]
        print(imgName)
        listImageUrlOk.append(imgName)
        html_data = requests.get(imgUrl)
        f = open(download_image_dir + "/" + imgName, "wb")  # 指定開啟檔案路徑
        # 將response.content二進位內容寫入指定的圖檔名稱
        f.write(html_data.content)
        f.close()
        print("%s 下載完成" % (imgName))

f = open(pageName, "w", encoding="utf-8")
f.write("<html>\n")
f.write("<meta charset='utf-8'>\n")
f.write("<body>\n")
f.write("<table border>\n")
f.write("<tr><td>書號</td><td>圖</td><td>書名</td></tr>\n")

print("---------------")  # 15個
print(len(listBookName))
print(listBookName)
print("---------------")  # 15個
print(len(listImageUrlOk))
print(listImageUrlOk)
print("---------------")  # 15個

for n in range(len(listBookName)):
    f.write("<tr>\n")
    f.write("<td>%s</td>\n" % (listImageUrlOk[n].split(".")[0]))
    f.write('<td><img src="images/%s" width="100"></td>\n' % (listImageUrlOk[n]))
    f.write("<td>%s</td>\n" % (listBookName[n].text))
    f.write("</tr>\n")
f.write("</table>\n")
f.write("</body>\n")
f.write("</html>\n")
f.close()

# 開啟 os.system(pageName)

print("%s 網頁建置成功" % (pageName))

print("------------------------------------------------------------")  # 60個

# 博碩文化新書網頁
url = "http://www.drmaster.com.tw/Publish_Newbook.asp"

responseObj = requests.get(url)
responseObj.encoding = "utf-8"
soup = BeautifulSoup(responseObj.text, "html.parser")

data = soup.select(".style2")  # 尋找class是style2
count = len(data)
print("共 %d 筆新書記錄" % (count))

for book in data:
    print(book.text)

print("------------------------------------------------------------")  # 60個

# 博碩文化新書網頁
url = "http://www.drmaster.com.tw/Publish_Newbook.asp"

responseObj = requests.get(url)
responseObj.encoding = "utf-8"
soup = BeautifulSoup(responseObj.text, "html.parser")

data = soup.select("td a img")

for book in data:
    if "http" in book.get("src"):
        print(book.get("src"))

print("------------------------------------------------------------")  # 60個

# 指定圖片網址
imgUrl = "http://www.drmaster.com.tw/Cover/MP22030.png"
imgName = imgUrl.split("/")[-1]
html_data = requests.get(imgUrl)
f = open(imgName, "wb")  # 指定開啟檔案路徑
# 將response.content二進位內容寫入為MP22030.png
f.write(html_data.content)
print("%s 下載完畢" % (imgName))
f.close()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 22")

# 某圖庫網站
url = "https://www.dreamstime.com/free-images_pg1"

html = requests.get(url)
html.encoding = "utf-8"

soup = BeautifulSoup(html.text, "html.parser")

# 建立 images 目錄儲存圖片
download_image_dir = "images/"
if not os.path.exists(download_image_dir):
    os.mkdir(download_image_dir)

print("多重取得")
all_links = soup.find_all(["a", "img"])  # 多重取得, 找全部的 超連結<a> 和 影像<img>

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
                f = open(os.path.join(download_image_dir, filename), "wb")
                f.write(image.read())
                f.close()
            except:
                print("{} 無法讀取!".format(filename))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 23 應該要改用cookie")

print("台灣英文新聞網")

news_title = ""
news_content = "contain"
filename = "tmp_engnews.txt"

url = "https://www.taiwannews.com.tw/news/3610689"
url = "https://www.taiwannews.com.tw/news/4966193"
html = requests.get(url).text
print(html)

soup = BeautifulSoup(html, "html.parser")  # 解析原始碼

print("找下一個標題<h1> + 條件")
title = soup.find("h1", class_="article-title")
news_title = title.text

article = soup.find("article", class_="container-fluid article")
news_content = article.text

with open(filename, "w", encoding="utf-8") as f:
    f.write(news_title + "\n")
    f.write(news_content)

print("標題")
print(news_title)
print("內容")
print(news_content)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 24 中央通訊社新聞")

from fake_useragent import UserAgent

ua = UserAgent()

headers = {"user-agent": ua.random}

news_title = ""
news_content = ""
filename = "tmp_cna_news.txt"

url = "https://www.cna.com.tw/news/aopl/201901050192.aspx"  # 加州保齡球館爆槍擊案 警方：3死4傷
url = "https://www.cna.com.tw/news/ait/202308280292.aspx"  # 繼探月成功後 印度又將發射太陽探測器

html = requests.get(url, headers=headers).text

soup = BeautifulSoup(html, "html.parser")  # 解析原始碼

print("找下一個內容分區元素<div> + 條件")
article = soup.find("div", class_="paragraph")
news_title = title.text.strip()  # strip()用來刪除文字前面和後面多餘的空白
print(news_title)

news_content = article.text

with open(filename, "w", encoding="utf-8") as f:
    f.write(news_title + "\n")
    f.write(news_content)

print("標題")
print(news_title)
print("內容")
print(news_content)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 25")

# 正妹指南／正妹筆記本
# (更新)郭雪芙／DreamGirls 32D美食天后 (100P+影)
url = "https://aiworker2000.pixnet.net/blog/post/16062839"

soup = get_soup_from_url(url)

# print("整個網頁資料 :", soup)
print(dir(soup))

print("------------------------------")  # 30個

download_image_dir = "tmp_download_files"
if not os.path.exists(download_image_dir):
    os.mkdir(download_image_dir)

# 用find找
print("找全部的影像<img>")
images = soup.find_all("img")  # 取得 全部 <img></img>
for image in images:
    image_url = image["src"]
    print(image_url)
    """ NG
    if ".jpg" in image_url:
        image_filename = os.path.basename(image_url)
        with open(os.path.join(download_image_dir, image_filename), "wb") as fp:
            image_data = urllib.request.urlopen(image_url).read()
            fp.write(image_data)
        print(image_url)
        print(image_filename)
    """

print("------------------------------")  # 30個

print("抓取網頁 分析 10")

import dominate
from dominate.tags import *
from dominate.util import raw

url = "http://aiworker2000.pixnet.net/blog/post/16062839"
index_html = dominate.document(title="圖形檔案索引")

download_image_dir = "tmp_download_files"
if not os.path.exists(download_image_dir):
    os.mkdir(download_image_dir)

with index_html.head:
    meta(charset="utf-8")

with index_html:
    h1("圖形檔案索引")
    hr()
    # html = requests.get(url).text
    # soup = BeautifulSoup(html, "lxml")
    soup = get_soup_from_url(url)
    # 用find找
    print("找全部的影像<img>")
    images = soup.find_all("img")  # 取得 全部 <img></img>
    for image in images:
        image_url = image["src"]
        """
        if ".jpg" in image_url:
            image_filename = os.path.basename(image_url)
            image_link = a(href=image_filename)
            image_link += img(src=image_filename, width=200)
            with open(os.path.join(download_image_dir, image_filename), "wb") as fp:
                image_data = urllib.request.urlopen(image_url).read()
                fp.write(image_data)
        """

with open(os.path.join(download_image_dir, "index.html"), "wt", encoding="utf-8") as fp:
    fp.write(str(index_html))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("抓取網頁 分析 9")

# 教育部全球資訊網-即時新聞
url = "https://www.edu.tw/News.aspx?n=9E7AC85F1954DDA8&sms=169B8E91BB75571F"
soup = get_soup_from_url(url)

table = soup.find("table")

cnt = 0
print("找全部的xx<tr>")
print("---------------")  # 15個
for row in soup.find_all("tr"):  # 取得 全部 <tr></tr>
    # print("找全部的xx<td>")
    cells = row.find_all("td")  # 取得 全部 <td></td>
    for cell in cells:
        a = cell.find("a")
        if a is not None and a.text != "下一頁":
            print(a.text)
            print("---------------")  # 15個
    cnt += 1
    if cnt > 5:
        break

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 26")

url = "https://www.mobile01.com/topiclist.php?f=751"

# 不使用headers, 無法抓資料
html_data = requests.get(url)

# 使用headers
html_data = requests.get(url, headers=headers)

soup = BeautifulSoup(html_data.text, "html.parser")  # 解析原始碼

print("找全部的超連結<a> + 條件")
pages = soup.find_all("a", class_="c-pagination")

print("本討論區的最後一頁是：", end="")
print(pages[-1].text)

print("找全部的內容分區元素<div> + 條件")
titles = soup.find_all("div", class_="c-listTableTd__title")
print(len(titles))

cnt = 0
for title in titles:
    print("------------------------------")  # 30個
    print(title)
    print("---------------")  # 15個
    print(title.a.text)
    print("---------------")  # 15個
    print(title.a["href"])
    print("---------------")  # 15個
    cnt += 1
    if cnt > 5:
        break

print("------------------------------------------------------------")  # 60個

print("找全部的超連結<a> +  條件")
pages = soup.find_all("a", class_="c-pagination")
last_page = int(pages[-1].text)
print("共有 :", last_page, " 頁")
url_pattern = "https://www.mobile01.com/topiclist.php?f=751&p={}"

last_page = 1

for page in range(1, last_page + 1):
    current_url = url_pattern.format(page)
    html_data = requests.get(current_url, headers=headers)
    soup = BeautifulSoup(html_data.text, "html.parser")
    print("找全部的內容分區元素<div> + 條件")
    titles = soup.find_all("div", class_="c-listTableTd__title")
    cnt = 0
    for title in titles:
        print("------------------------------")  # 30個
        print(title.a.text)
        print("---------------")  # 15個
        print(title.a["href"])
        print("---------------")  # 15個
        cnt += 1
        if cnt > 5:
            break
    time.sleep(3)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 31 飛比價格 搜尋 raspberry pi 3")

url = "https://feebee.com.tw/s/?q=raspberry+pi+3"
html_data = requests.get(url)
soup = BeautifulSoup(html_data.text.encode("utf-8"), "html.parser")

cnt = 0
for line in soup.select(".items"):  # 尋找class是items
    print(line.select(".large")[0].text)  # 尋找class是large
    print(line.select(".ellipsis")[0].text)  # 尋找class是ellipsis
    print(line.select("a")[0].get("href"))
    cnt += 1
    if cnt > 3:
        break

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 32 中時新聞網 焦點新聞\n")

url = "https://www.chinatimes.com/?chdtv"
html_data = requests.get(url)
soup = BeautifulSoup(html_data.text.encode("utf-8"), "html.parser")

cnt = 0
for lines in soup.select(".focus-news"):  # 尋找class是focus-news 焦點新聞
    for line in lines.select(".title"):  # 尋找class是title
        print("---------------")  # 15個
        print("全部 :", line)  # 整個class的資料
        print("文字 :", line.select("a")[0].text)  # 取出Text
        # print(line.select("a"))
        # print(line.select("a")[0])
        # print("取得網頁中的超連結")
        # print(line.select("a")[0].get("href")) # same
        print("超連結 :", line.select("a")[0]["href"])
        cnt += 1
        if cnt > 3:
            break

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 中時新聞網 文字雲 目前無法抓網頁

urls = []
url = "https://www.chinatimes.com/realtimenews/?chdtv"  # 中時新聞網

# html_data = requests.get(url)  # same
html_data = requests.get(url, headers=headers)  # same

soup = BeautifulSoup(html_data.text.encode("utf-8"), "html.parser")
print(soup)

cc = soup.select(".article-list a")  # 尋找class是article-list a
for d in cc:  # 取得新聞連結
    url = "https://www.chinatimes.com" + d.get("href")
    if (len(url) > 58) and (url not in urls):
        urls.append("https://www.chinatimes.com" + d.get("href"))

text = ""
i = 1
for url in urls:  # 逐一取得新聞
    print(url)
    html_data = requests.get(url)
    soup = BeautifulSoup(html_data.text, "html.parser")
    # <h1 class="article-title">陸93閱兵後民調變了！近6成支持交流避戰、僅4成信美軍會出兵</h1>
    print("找全部的標題<h1>")
    all_links = soup.find_all("h1")  # 取得 全部 <a></a>
    for link in all_links:
        print(link)
        href = link.get("href")  # 讀取 href 屬性內容
        print(href)
        # 判斷內容是否為非 None，並且開頭文字是 https://
        if href != None and href.startswith("https://"):
            print(href)

    cc = soup.select(".article-body p")  # 新聞內容  # 尋找class是article-body p
    print(cc)
    # print("處理第 {} 則新聞".format(i))
    for d in cc:
        if d.text != "":  # 有新聞內容
            text += d.text
            print(d.text)
    i += 1
    if i > 3:
        break

text = text.replace("中時", "").replace("新聞網", "")
print("text :", text)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 35 抓圖片範例 合併根目錄位址")

# 星座屋
url = "http://www.xzw.com/fortune/"

soup = get_soup_from_url(url)
print(soup)

print("找下一個內容分區元素<div> + 條件")
constellation = soup.find("div", id="list")
cons = constellation.find("div", "alb").find_all("div")  # 取得 全部 <div></div>
print(len(cons))

pict_url = "http://www.xzw.com"
photos = []
for con in cons:
    print("---------------")  # 15個
    # print(con)
    print("星座 :", con.strong.text)
    print("整體運勢 :", soup.find("p").text)
    pict = con.a.img["src"]
    print("圖片位址 :", pict)
    photos.append(pict_url + pict)

print(len(photos))
for photo in photos:
    print(photo)

download_image_dir = "tmp_xzw_picture"
if os.path.exists(download_image_dir) == False:  # 如果沒有此資料夾就建立
    os.mkdir(download_image_dir)

print("搜尋到的圖片數量 = ", len(photos))  # 列出搜尋到的圖片數量
for photo in photos:  # 迴圈下載圖片與儲存
    picture = requests.get(photo)  # 下載圖片
    picture.raise_for_status()  # 如果發生錯誤的話, 會丟出 exception
    print("%s 圖片下載成功" % photo)
    # 先開啟檔案, 再儲存圖片
    pictFile = open(os.path.join(download_image_dir, os.path.basename(photo)), "wb")
    for diskStorage in picture.iter_content(10240):
        pictFile.write(diskStorage)
    pictFile.close()  # 關閉檔案

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 37")
url = "https://fchart.github.io/Elements.html"
soup = get_soup_from_url(url)

tag = soup.select_one("h2")
print("h2 :", tag.text)

tags = soup.select("b")
print("b :", tags[0].text)

tag = soup.select_one("#q2")
tag2 = tag.select_one("b")
print("b :", tag2.text)

tags = soup.select(".response")  # 尋找class是response
print("li :", tags[0].text)
print("li :", tags[1].text)

print("------------------------------")  # 30個

print("找下一個標題<h2>")
tag = soup.find("h2")
print("h2 :", tag.text)

tag = soup.find("b")  # 找下一個粗體<b>
print("b :", tag.text)

print("找全部的xx<b>")
tags = soup.find_all("b")  # 取得 全部 <b></b>
print("b :", tags[0].text)

tag = soup.find("li", {"id": "q2"})
tag_q = tag.find("b")  # 找下一個粗體<b>
print("Question :", tag_q.text)

tags_a = tag.find_all("li", {"class": "response"})
for tag in tags_a:
    print("Ans :", tag.text)

tags_a = tag.find_all("li", class_="response")
for tag in tags_a:
    print("Ans :", tag.text)

print("------------------------------")  # 30個

print("找全部的xx<li> + 條件")
tags_li = soup.find_all("li", class_="response", limit=3)
print(tags_li)

print("------------------------------")  # 30個

tag_ans1 = soup.find("li", class_="response")
print(tag_ans1.text)

tag_ans2 = tag_ans1.find_next()
print(tag_ans2.text)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 42")

print("臺灣證交所本國上市證券")
# 查詢台灣證交所本國上市證券國際證券辨識號碼一覽表

df = pd.read_html(
    "https://isin.twse.com.tw/isin/C_public.jsp?strMode=2",
    header=0,
)

newdf = df[0][df[0]["產業別"] > "0"]  # 產業別資料大於0
# del newdf["國際證券辨識號碼(ISIN Code)"],newdf["CFICode"],newdf["備註"]
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

filename = "tmp_stock_.xlsx"
newdf.to_excel(filename, sheet_name="Sheet1", index=False)  # 存入excel

print("已存檔到 :", filename)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 43")
print("將網頁上的資料存成csv檔")

print("新北市不動產仲介經紀商業同業公會網站")

csv_filename = "tmp_新北市仲介.csv"
f = open(csv_filename, "w", encoding="utf-8-sig")
w = csv.writer(f)

httphead = "https://www.tcr.org.tw/a/table_blogs/index/21654"

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
    # soup = BeautifulSoup(html, "lxml")
    print(htmlname)
    soup = get_soup_from_url(htmlname)
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
print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 36 巴哈姆特 + headers")

# 獲取網頁內容 巴哈姆特 必須使用headers
url = "https://acg.gamer.com.tw/billboard.php?t=2&p=Android"

html_data = requests.get(url, headers=headers)
html_data.encoding = "UTF-8"

soup = BeautifulSoup(html_data.text, "html.parser")
print(soup)

soup.find(class_="ACG-mainbox1").find(class_="ACG-maintitle").find("a").string

for game in soup.findAll(class_="ACG-mainbox1"):
    print("---------------")  # 15個
    # print(game)
    print("名次 :", game.find(class_="ACG-mainumber").string)
    print("名稱 :", game.find(class_="ACG-maintitle").find("a").string)

print("------------------------------------------------------------")  # 60個

# 獲取網頁內容 巴哈姆特 必須使用headers
url = "https://acg.gamer.com.tw/billboard.php?t=2&p=iOS"
html_data = requests.get(url, headers=headers)

soup = BeautifulSoup(html_data.text, "html.parser")
print(soup)

# 找到所有遊戲排名標題的標籤
print("找全部的內容分區元素<div> + 條件")
games = soup.find_all("div", {"class": "ACG-mainbox2"})

print("---------------")  # 15個

# 顯示遊戲排名標題
for game in games:
    print("---------------")  # 15個
    # print(game)
    print("名次 :", game.find(class_="ACG-mainumber").string)
    print("名稱 :", game.find(class_="ACG-maintitle").find("a").string)
    print("全部 :", game.text.strip())  # strip()用來刪除文字前面和後面多餘的空白

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 加了 headers 也無法讀取

print("BeautifulSoup 測試 46 NG")
# 指定url變數為「Dcard熱門文章」網頁的網址
url = "https://www.dcard.tw/f"
# html_data = requests.get(url)
html_data = requests.get(url, headers=headers)

soup = BeautifulSoup(html_data.text, "lxml")  # 取得物件
# soup = get_soup_from_url(url)
print(soup)

# 取得所有文章程式碼
print("找全部的xx<article>")
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
print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 47")
url = "https://www.iana.org/domains/"
soup = get_soup_from_url(url)

print("------------------------------")  # 30個

print("找全部的超連結<a>")
print(soup.find_all("a"))  # 找全部的超連結<a>
print(soup("a"))  # 找全部的超連結<a>

print("找全部的超連結<a> +  條件")
print(soup.find_all("a", string="Domains"))  # 找出內容字串為 Domains 的 a tag

print(soup("a", limit=2))  # 找全部的超連結<a> + 條件

print("------------------------------")  # 30個

print(soup.find("a").get_text())  # 輸出第一個 a tag 的內容
print(soup.find("a")["href"])  # 輸出第一個 a tag 的 href 屬性內容

print("------------------------------")  # 30個

print(soup.select("#logo"))  # 搜尋 id 為 logo 的 tag 內容

print("------------------------------")  # 30個

print("找全部的內容分區元素<div> + 條件")
print(soup.find_all("div", id="logo"))  # 搜尋所有 id 為 logo 的 div

print("------------------------------")  # 30個

print("找全部的內容分區元素<div>")
divs = soup.find_all("div")  # 取得 全部 <div></div>
print(divs[1])  # 取得搜尋到的第二個項目 ( 第一個為 divs[0] )

print("------------------------------")  # 30個

# 從搜尋到的項目裡，尋找父節點裡全部的 li
print(divs[1].find_parent().find_all("li"))  # 取得 全部 <li></li>

print("------------------------------")  # 30個

# 從搜尋到的項目裡，尋找父節點裡所有 li 的第三個項目，找到他後方同層的所有 li
print(divs[1].find_parent().find_all("li")[2].find_next_siblings())

print("------------------------------")  # 30個

# 從搜尋到的項目裡，尋找父節點裡所有 li 的第三個項目，找到他前方同層的所有 li
print(divs[1].find_parent().find_all("li")[2].find_previous_siblings())

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("抓取網頁 分析 13")

url = "https://www.ptt.cc/bbs/Gossiping/index.html"

# 不使用  cookies 也可以抓網頁
# html_data = requests.get(url=url, cookies=cookies)
html_data = requests.get(url=url)

soup = BeautifulSoup(html_data.text, "lxml")
print(soup)

print("找全部的內容分區元素<div> + 條件")
titles = soup.find_all("div", class_="title")  # 取得 class 為 title 的 div 內容
for title in titles:
    print(title.a.text)

print("------------------------------------------------------------")  # 60個

url = "https://www.ptt.cc/bbs/Gossiping/index.html"

# 不使用  cookies 也可以抓網頁
# html_data = requests.get(url=url, cookies=cookies)
html_data = requests.get(url=url)

soup = BeautifulSoup(html_data.text, "html.parser")

print("找全部的內容分區元素<div> + 條件")
titles = soup.find_all("div", class_="title")  # 取得 class 為 title 的 div 內容
for i in titles:
    if i.find("a") != None:  # 判斷如果不為 None
        print(i.find("a").get_text())  # 取得 div 裡 a 的內容，使用 get_text() 取得文字
        print(url + i.find("a")["href"], end="\n\n")  # 使用 ["href"] 取得 href 的屬性

print("------------------------------------------------------------")  # 60個

url = "https://www.ptt.cc/bbs/Gossiping/index.html"

# 不使用  cookies 也可以抓網頁
# html_data = requests.get(url=url, cookies=cookies)
html_data = requests.get(url=url)
html_data.encoding = "utf-8"  # 避免中文亂碼

soup = BeautifulSoup(html_data.text, "html.parser")

print("找全部的內容分區元素<div> + 條件")
titles = soup.find_all("div", class_="title")  # 取得 class 為 title 的 div 內容
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

url = "https://www.ptt.cc/bbs/NBA/index6503.html"

DELETED = BeautifulSoup("<a href='Deleted'>本文已刪除</a>", "lxml").a

html_data = requests.get(url)
if html_data.status_code == requests.codes.ok:
    html_data.encoding = "utf8"
    soup = BeautifulSoup(html_data.text, "lxml")
    print("找全部的內容分區元素<div> + 條件")
    tag_divs = soup.find_all("div", class_="r-ent")
    for tag in tag_divs:
        tag_a = tag.find("a") or DELETED
        print(tag_a["href"])
        print(tag_a.text)
        print(tag.find("div", class_="author").string)
else:
    print("HTTP請求錯誤..." + url)

print("------------------------------------------------------------")  # 60個

url = "https://www.ptt.cc/bbs/Gossiping/index.html"

# 不使用  cookies 也可以抓網頁
html_data = requests.get(url, cookies=cookies)

if html_data.status_code == requests.codes.ok:
    html_data.encoding = "utf8"
    soup = BeautifulSoup(html_data.text, "lxml")
    print("找全部的內容分區元素<div> + 條件")
    tag_divs = soup.find_all("div", class_="r-ent")
    for tag in tag_divs:
        if tag.find("a"):  # 是否有<a>標籤
            tag_a = tag.find("a")
            print(tag_a["href"])
            print(tag_a.text)
            print(tag.find("div", class_="author").string)
else:
    print("HTTP請求錯誤..." + url)

print("------------------------------------------------------------")  # 60個

from urllib.parse import urljoin

url = "http://www.majortests.com/word-lists/word-list-01.html"
PTT = "https://wwww.ptt.cc/bbs/movie/index.html"

catalog = ["movie", "NBA", "Gossiping"]

for i in range(1, 5):
    url = urljoin(url, "world-list-0{0}.html".format(i))
    print(url)
print("---------------")  # 15個
for item in catalog:
    url = urljoin(PTT, "../{0}/index.html".format(item))
    print(url)

print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 53")

url = "https://www.ptt.cc/bbs/Beauty/M.1638380033.A.7C7.html"

# 不使用  cookies 也可以抓網頁
# html_data = requests.get(url=url, cookies=cookies)
html_data = requests.get(url=url)

soup = BeautifulSoup(html_data.text, "html.parser")

# 用find找
print("找全部的影像<img>")
imgs = soup.find_all("img")  # 取得 全部 <img></img>
name = 0  #  設定圖片編號
for i in imgs:
    print(i["src"])  # 印出 src 的屬性
    jpg = requests.get(i["src"])  # 使用 requests 讀取圖片網址，取得圖片編碼
    f = open(f"tmp_test_{name}.jpg", "wb")  # 使用 open 設定以二進位格式寫入圖片檔案
    f.write(jpg.content)  # 寫入圖片的 content
    f.close()  # 寫入完成後關閉圖片檔案
    name = name + 1  # 編號增加 1

print("------------------------------------------------------------")  # 60個

url = "https://www.ptt.cc/bbs/Beauty/M.1638380033.A.7C7.html"

# 不使用  cookies 也可以抓網頁
# html_data = requests.get(url=url, cookies=cookies)
html_data = requests.get(url=url)

soup = BeautifulSoup(html_data.text, "html.parser")

# 用find找
print("找全部的影像<img>")
imgs = soup.find_all("img")  # 取得 全部 <img></img>
name = 0
urls = []  # 根據爬取的資料，建立一個圖片名稱與網址的空串列
for i in imgs:  # 修改 for 迴圈內容
    urls.append([i["src"], name])  # 將圖片網址與編號加入串列中
    name = name + 1  # 編號增加 1

print(urls)
print()  # 印出網址
jpg = requests.get(urls[0])  # 使用 requests.get 取得圖片資訊
f = open(f"download/test_{urls[1]}.jpg", "wb")  # 將圖片開啟為二進位格式 ( 請自行修改存取路徑 )
f.write(jpg.content)  # 存取圖片
f.close()

print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 04")

# PTT C_Chat板每篇文章的標題

url = "https://www.ptt.cc/bbs/C_Chat/index.html"

domain = "{}://{}".format(
    urllib.parse.urlparse(url).scheme, urllib.parse.urlparse(url).hostname
)
print("domain :", domain)

soup = get_soup_from_url(url)

# 發現全部的文章標題都在class="title"的div中
print("找全部的內容分區元素<div> + 條件")
all_links = soup.find_all("div", class_="title")  # 文章標題
for link in all_links:
    print(link.text.strip())  # strip()用來刪除文字前面和後面多餘的空白

print("------------------------------------------------------------")  # 60個

# 參考 https://ithelp.ithome.com.tw/articles/10186119

print("BeautifulSoup 測試 17 PTT NBA 板")

url = "https://www.ptt.cc/bbs/NBA/index.html"  # PTT NBA 板
html_data = requests.get(url)  # 用 requests 的 get 方法把網頁抓下來

soup = BeautifulSoup(html_data.text, "lxml")  # 指定 lxml 作為解析器

print("一些 BeautifulSoup 的屬性或方法")

# Beautiful Soup 幫我們將 html 檔案轉換為 bs4 的物件，像是標籤（Tag），
# 標籤中的內容（NavigableString）與 BeautifulSoup 物件本身。

# 用.取
print(type(soup.a))
print("---------------")  # 15個
print(soup.a.name)  # 抓標籤名 a
print("---------------")  # 15個
print(soup.a["id"])  # 抓<a></a>的 id 名稱
print("------------------------------")  # 30個
print("標籤中的內容（NavigableString）")
print(type(soup.a.string))
print(soup.a.string)
print("------------------------------")  # 30個
print("爬樹")

# DOM（Document Object Model）的樹狀結構觀念在使用 BeautifulSoup 扮演至關重要的角色，所以我們也要練習爬樹。
print("往下爬")
# 從標籤中回傳更多資訊。

print(soup.body.a.contents)
print(list(soup.body.a.children))
print(soup.body.a.string)

print("往上爬")
# 回傳上一階層的標籤。

print("往旁邊爬")
# 回傳同一階層的標籤。

first_a_tag = soup.body.a
next_to_first_a_tag = first_a_tag.next_sibling
print(first_a_tag)
print("---------------")  # 15個
print(next_to_first_a_tag)
print("---------------")  # 15個
print(next_to_first_a_tag.previous_sibling)

print("------------------------------")  # 30個

print("搜尋")
# 這是我們主要使用 BeautifulSoup 套件來做網站解析的方法。
# find() 方法
# find_all() 方法

print("可以在第二個參數 class_= 加入 CSS 的類別。")

print("找下一個內容分區元素<div> + 條件")
print(soup.find("div", class_="r-ent"))

print("------------------------------")  # 30個

# BeautifulSoup 牛刀小試

"""
大略照著官方文件練習了前面的內容之後，
我們參考Tutorial of PTT crawler來應用 BeautifulSoup
把 PTT NBA 版首頁資訊包含推文數，作者 id，文章標題與發文日期搜集下來。
我們需要的資訊都放在 CSS 類別為 r-ent 的 <div></div> 中。
"""

print("找全部的內容分區元素<div> + 條件")
posts = soup.find_all("div", class_="r-ent")
print(posts)
type(posts)

# 注意這個 posts 物件是一個 ResultSet，一般我們使用迴圈將裡面的每一個元素再抓出來，先練習一下作者 id。

print("------------------------------")  # 30個

author_ids = []  # 建立一個空的 list 來放置作者 id
print("找全部的內容分區元素<div> + 條件")
posts = soup.find_all("div", class_="r-ent")
for post in posts:
    author_ids.extend(post.find("div", class_="author"))

print(author_ids)

print("------------------------------")  # 30個

print("接下來我們把推文數，文章標題與發文日期一起寫進去。")

author_ids = []  # 建立一個空的 list 來放作者 id
recommends = []  # 建立一個空的 list 來放推文數
post_titles = []  # 建立一個空的 list 來放文章標題
post_dates = []  # 建立一個空的 list 來放發文日期

print("找全部的超連結<a> + 條件")
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
print("找全部的內容分區元素<div> + 條件")
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

print("------------------------------")  # 30個

# 檢查結果都沒有問題之後，那我們就可以把這幾個 list 放進 dictionary 接著轉換成 data frame 了。

author_ids = []  # 建立一個空的 list 來放作者 id
recommends = []  # 建立一個空的 list 來放推文數
post_titles = []  # 建立一個空的 list 來放文章標題
post_dates = []  # 建立一個空的 list 來放發文日期

print("找全部的內容分區元素<div> + 條件")
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
print("找全部的內容分區元素<div> + 條件")
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

'''
print("------------------------------------------------------------")  # 60個
print("統一發票")
print("------------------------------------------------------------")  # 60個

## 取得發票號碼
# pip insall invoiceTW

from invoiceTW import invoice

""" NG
cc = invoice.get_current()
print(cc)
"""
# {'title': '109年11月、12月', '特別獎': '77815838', '特獎': '39993297', '頭獎': '59028801、02813820、06896234', '增開六獎': '011、427'}

print("------------------------------")  # 30個

print("BeautifulSoup 測試 57")

url = "https://invoice.etax.nat.gov.tw/index.html"

html_data = requests.get(url)  # 取得網頁內容
html_data.encoding = "utf-8"  # 因為該網頁編碼為 utf-8，加上 .encoding 避免亂碼

soup = BeautifulSoup(html_data.text, "html.parser")  # 轉換成標籤樹

td = soup.select(".container-fluid")[0].select(
    ".etw-tbiggest"
)  # 取出中獎號碼的位置  # 尋找class是container-fluid
ns = td[0].getText()  # 特別獎
n1 = td[1].getText()  # 特獎
# 頭獎，因為存入串列會出現 /n 換行符，使用 [-8:] 取出最後八碼
n2 = [td[2].getText()[-8:], td[3].getText()[-8:], td[4].getText()[-8:]]
print("特別獎 :", ns)
print("特獎 :", n1)
print("頭獎 :", n2)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 60")
# 馬丁路德 I have a dream
url = "http://www.analytictech.com/mb021/mlk.htm"
page = requests.get(url)
page.raise_for_status()  # 如果發生錯誤的話, 會丟出 exception
soup = BeautifulSoup(page.text, "html.parser")
p_elems = [element.text for element in soup.find_all("p")]

speech = " ".join(p_elems)  # 將段落內容串在一起

# 修正錯字、刪除多餘的空格、移除非字母內容
speech = speech.replace(")mowing", "knowing")
speech = re.sub("\s+", " ", speech)
speech_edit = re.sub("[^a-zA-Z]", " ", speech)
speech_edit = re.sub("\s+", " ", speech_edit)

print(speech_edit)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 61")
exist_url = []
g_writecount = 0

full_url = "https://zh.wikipedia.org/wiki/%E6%8B%BF%E7%A0%B4%E4%BB%91%E4%B8%80%E4%B8%96"  # 填写你要爬取的网页


def scrappy(url, depth=1):
    global g_writecount
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
        }
        html_data = requests.get(full_url, headers=headers)
        html = html_data.text
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


# 效果：给一个网页，返回一个chinese_txt文件，
# 里面有爬回这个网页内全部的文字，
# 以及网页内全部的链接内的网页文字也会被爬到。

start = time.time()

scrappy(full_url)
stop = time.time()
print("所用时间：", stop - start)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("專項")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
# 台灣水庫即時水情 water.taiwanstat.com
print("------------------------------------------------------------")  # 60個

print("台灣水庫即時水情")
url = "https://water.taiwanstat.com/"  # 台灣水庫即時水情

html_data = requests.get(url)  # 取得網頁內容
html_data.encoding = "utf-8"  # 網頁編碼模式  # 因為該網頁編碼為 utf-8，加上 .encoding 避免亂碼

print(html_data.text)  # HTML網頁內容

# NG print(html_data.json())  # response轉成json格式

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 台灣水庫即時水情
url = "https://water.taiwanstat.com/"
html_data = requests.get(url)  # 取得網頁內容

# soup = BeautifulSoup(html_data.text, "html.parser")  # 使用 html.parser 解析器
# soup = BeautifulSoup(html_data.text, "html5lib")  # 使用 html5lib 解析器
soup = BeautifulSoup(html_data.text, "html.parser")

reservoir = soup.select(
    ".reservoir"
)  # 取得所有 class 為 reservoir 的 tag   # 取出中獎號碼的位置  # 尋找class是reservoir
for i in reservoir:
    print(
        i.find("div", class_="name").get_text(), end=" "
    )  # 取得內容的 class 為 name 的 div 文字
    print(i.find("h5").get_text(), end=" ")  # 取得內容 h5 tag 的文字
    print("---------------")  # 15個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
# www.books.com.tw
print("------------------------------------------------------------")  # 60個

url = "https://www.books.com.tw/"  # 博客來
soup = get_soup_from_url(url)

print(soup.find("title"))  # 傳回網頁含<title>~</title>
print(soup.find("title").text)  # 傳回網頁<title>標籤內的資料

# 用find找
print("找全部的標題<h2>")
h2s = soup.find_all("h2")  # 取得 全部 <h2></h2>
# print("取得全部 h2 :", h2s)        #印出全部資料, 一個list

length = len(h2s)
print("共找到", length, "筆資料")
for nn in range(length):
    print(h2s[nn].text)  # 使用索引值, 只印出text部分

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 博客來-中文書>暢銷榜
url = "https://www.books.com.tw/web/sys_saletopb/books/19/?loc=P_0002_020"
soup = get_soup_from_url(url)

# 用find找
print("找全部的影像<img>")
cnt = 0
images = soup.find_all("img")  # 取得 全部 <img></img>
for image in images:
    if ".jpg" in image["src"] or ".png" in image["src"]:
        print(image["src"])
        cnt += 1
        if cnt > 10:
            break

print("------------------------------")  # 30個

print("找全部的超連結<a>")
cnt = 0
all_links = soup.find_all("a")  # 取得 全部 <a></a>
for link in all_links:
    if "http" in link["href"]:
        print(link["href"])
        cnt += 1
        if cnt > 10:
            break

print("------------------------------")  # 30個

print("找全部的影像<img> + 條件")
cnt = 0
titles = soup.find_all("img", {"class": "cover"})
for i, title in enumerate(titles):
    print("第{}名：{}".format(i + 1, title["alt"]))
    cnt += 1
    if cnt > 10:
        break

print("------------------------------")  # 30個

print("找全部的xx<li>")
books = soup.find_all("li", {"class": "item"})
print(len(books))
# print(books)

for i, book in enumerate(books):
    # print(i, book)
    if i > 22 and i < 30:
        print("第{}名：".format(i - 22), end="")
        print(book.find("img")["alt"])
        for info in book.find("ul").find_all("li"):  # 取得 全部 <li></li>
            print(info.text)
        print("---------------")  # 15個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 博客來寵物電子書
url = "https://www.books.com.tw/web/sys_cebbotm/cebook/1003/?loc=P_0001_2_003"
soup = get_soup_from_url(url)

print("找全部的內容分區元素<div> + 條件")
listAll = soup.find_all("div", class_="item")  # 取得<div class="item">標籤的內容
for book in listAll:  # 將資料利用迴圈依序解析
    listClass = book.get("class")  # 傳回目前標籤的類別資訊
    if len(listClass) == 2:  # ["item", "clearfix"]總數為2，即目前有兩個類別
        if listClass[1] == "clearfix":  # 遇到clearfix類別時，跳出本次迴圈
            continue
    print((book.find("h4").find("a").text))  # 搜尋第一個<h4>內的第一個<a>標籤，即書名

print("------------------------------")  # 30個

listName = soup.select("div.item>div.msg>h4>a")  # 根據路徑擷取<a>標籤，並指定給listName串列
listPrice = soup.select("li.set2")  # 取得套用set2類別的<li>標籤，並指定給listPrice串列
for i in range(0, len(listName)):  # 使用迴圈逐一印出書名與書價
    print("%s  %s" % (listName[i].text, listPrice[i].text))

print("------------------------------")  # 30個

# 分別取的商品名稱以及價格標籤，並指定給對應串列
listName = soup.select("div.item>div.msg>h4>a")
listPress = soup.select("li.info>span>a")
listPrice = soup.select("li.set2")

print("---------------")  # 15個
print(len(listName))
print("---------------")  # 15個
print(type(listName))
print("---------------")  # 15個
print(listName)
print("---------------")  # 15個

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

print("------------------------------")  # 30個

print("下載網站圖片")

Img = soup.select("div.item>a>img")  # 擷取有圖片網址的<img>標籤

print("共找到有圖片網址的連結 :", len(Img), "個")

cnt = 0
for link in Img:
    print("圖片連結 :", link)
    # 使用split()方法解析網址
    src = link.get("src")
    ImgUrl = src.split("=")[1].split("&")[0]
    # 網址用"/"分隔取最後一筆資料 => *.jpg
    filename = ImgUrl.split("/")[-1]
    print("圖片網址 :", ImgUrl)
    print("圖片檔名 :", filename)

    try:  # 下載圖片
        html_data = requests.get(ImgUrl)  # 建立下載圖片的Response物件 html_data
        f = open((filename), "wb")  # 開啟圖片檔案
        f.write(html_data.content)  # 下載圖片
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
print("------------------------------------------------------------")  # 60個


def showpage(url, kind):
    print("showpage, url  :", url)
    print("showpage, kind :", kind)
    soup = get_soup_from_url(url)
    # 近期新書、在 class="mod type02_m012 clearfix" 中
    res = soup.find_all("div", {"class": "mod type02_m012 clearfix"})[0]
    items = res.select(".item")  # 所有 item  # 尋找class是item
    n = 0  # 計算該分頁共有多少本書
    print(len(items))
    for item in items:
        print(item)
        msg = item.select(".msg")[0]  # 尋找class是msg
        # src = item.select("a img")[0]["src"]
        title = msg.select("a")[0].text  # 書名
        # imgurl = src.split("?i=")[-1].split("&")[0]  # 圖片網址
        author = msg.select("a")[1].text  # 作者
        publish = msg.select("a")[2].text  # 出版社
        date = msg.find("span").text.split("：")[-1]  # 出版日期
        onsale = item.select(".price .set2")[0].text  # 優惠價  # 尋找class是price .set2
        content = (
            item.select(".txt_cont")[0].text.replace(" ", "").strip()
        )  # 內容  # 尋找class是txt_cont
        # 將資料加入 list1 串列中
        # listdata = [kind, title, imgurl, author, publish, date, onsale, content]
        # list1.append(listdata)
        print("\n分類：" + kind)
        print("書名：" + title)
        # print("圖片網址：" + imgurl)
        print("作者：" + author)
        print("出版社：" + publish)
        print("出版日期：" + date)
        print(onsale)  # 優惠價
        print("內容：" + content)
        n += 1
        print("n=", n)
        if n > 2:
            break


def twobyte(kindno):
    if kindno < 10:
        kindnostr = "0" + str(kindno)
    else:
        kindnostr = str(kindno)
    return kindnostr


print("------------------------------")  # 30個

list1 = []
kindno = 1  # 要下載的分類，預設為第1分類：文學小說
homeurl = "https://www.books.com.tw/web/books_nbtopm_01/?o=5&v=1"
mode = "?o=5&v=1"  # 顯示模式：直式  排序依：暢銷度
url = "https://www.books.com.tw/web/books_nbtopm_"

soup = get_soup_from_url(homeurl)

# 中文書新書分類，取得分類資訊
# res = soup.find("div", {"class": "mod_b type02_l001-1 clearfix"})  # same
res = soup.find("div", class_="mod_b type02_l001-1 clearfix")
hrefs = res.select("a")  # 選全部的超連結<a>

# kindno = int(input("請輸入要下載的分類："))
kindno = 1  # 要下載的分類，預設為第1分類：文學小說

if 0 < kindno <= len(hrefs):
    kind = hrefs[kindno - 1].text  # 分類名稱
    print("下載的分類編號：{}   分類名稱：{}".format(kindno, kind))
    # 下載指定的分類
    kindurl = url + twobyte(kindno) + mode  # 分類網址
    print(kindurl)
    print("showkind, url  :", kindurl)
    print("showkind, kind :", kind)
    soup = get_soup_from_url(kindurl)
    try:
        pages = int(
            soup.select(".cnt_page span")[0].text
        )  # 該分類共有多少頁  # 尋找class是cnt_page span
        print("共有", pages, "頁")
        for page in range(1, pages + 1):
            pageurl = kindurl + "&page=" + str(page).strip()  # strip()用來刪除文字前面和後面多餘的空白
            print("第", page, "頁", pageurl)
            if page == 1:  # 只看第1頁
                showpage(pageurl, kind)
    except:  # 沒有分頁的處理
        print("XXXXXXX 沒有分頁的處理")
        # showpage(kindurl, kind)

    listtitle = ["分類", "書名", "圖片網址", "作者", "出版社", "出版日期", "優惠價", "內容"]
    print(listtitle)
    for item1 in list1:  # 資料
        print(item1)
else:
    print("分類不存在!")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" webdriver skip
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/test.html")

print("------------------------------")  # 30個

print(driver.title)
html = driver.page_source
print(html)
driver.quit()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/test.html")

print("------------------------------")  # 30個

print(driver.title)
html = driver.page_source
print(html)
driver.quit()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
cookies = {"name": "over18", "value": "1"}
driver.get("https://www.ptt.cc/bbs/Gossiping/index.html")
driver.add_cookie(cookies)

print("------------------------------")  # 30個

print(driver.title)
driver.quit()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
driver.implicitly_wait(10)
cookies = {"name": "over18", "value": "1"}
driver.get("https://www.ptt.cc/bbs/Gossiping/index.html")
driver.add_cookie(cookies)

print("------------------------------")  # 30個

print(driver.title)
driver.quit()
"""
print("------------------------------------------------------------")  # 60個
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

print("------------------------------")  # 30個

print(driver.title)
html = driver.page_source
print(html)
driver.quit()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""webdriver skip

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

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
print("------------------------------------------------------------")  # 60個

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

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
print("------------------------------------------------------------")  # 60個

from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/Example.html")
tag_ol = driver.find_element_by_xpath('//*[@id="list"]')
print(tag_ol.tag_name)
tags_li = tag_ol.find_elements_by_xpath("//li")
for tag in tags_li:
    print(tag.text, tag.get_attribute("class"))
driver.quit()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/ML/Example.html")

tag_ol = driver.find_element(By.XPATH, "/html/body/ol")
print(tag_ol.tag_name)
tags_li = tag_ol.find_elements(By.XPATH, "//li")
for tag in tags_li:
    print(tag.text, tag.get_attribute("class"))
driver.quit()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/ML/Example.html")

tag_ol = driver.find_element(By.XPATH, "/html/body/ol")
print(tag_ol.tag_name)
tags_li = tag_ol.find_elements(By.XPATH, "//li")
for tag in tags_li:
    print(tag.text, tag.get_attribute("class"))
driver.quit()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from selenium import webdriver

driver = webdriver.Edge("./msedgedriver")
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/Example.html")

tag_ol = driver.find_element_by_xpath("/html/body/ol")
print(tag_ol.tag_name)
tags_li = tag_ol.find_elements_by_xpath("//li")
for tag in tags_li:
    print(tag.text, tag.get_attribute("class"))
driver.quit()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/ML/Example.html")

tag_ol = driver.find_element(By.XPATH, '//*[@id="list"]')
print(tag_ol.tag_name)
print(tag_ol.get_attribute("innerHTML"))
soup = BeautifulSoup(tag_ol.get_attribute("innerHTML"), "lxml")

print("找全部的xx<li> + 條件")
tags_li = soup.find_all("li", class_="line")
for tag in tags_li:
    print(tag.text)
driver.quit()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/ML/Example.html")
tag_ol = driver.find_element(By.XPATH, '//*[@id="list"]')
print(tag_ol.tag_name)
print(tag_ol.get_attribute("innerHTML"))
soup = BeautifulSoup(tag_ol.get_attribute("innerHTML"), "lxml")

print("找全部的xx<li> + 條件")
tags_li = soup.find_all("li", class_="line")
for tag in tags_li:
    print(tag.text)
driver.quit()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = (
    "https://www.googleapis.com/books/v1/volumes?maxResults=5&q=Python&projection=lite"
)
html_data = requests.get(url)
html_data.encoding = "utf8"
json_data = json.loads(html_data.text)

jsonfilename = "tmp_GoogleBooks.json"
with open(jsonfilename, "w") as fp:
    json.dump(json_data, fp)
    print("json 存檔完成, 檔案 :", jsonfilename)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("比較使用 headers 抓取網站資料")

#  momo 網站 無 headers, 不可抓取

url = "https://www.momoshop.com.tw/search/"

url_new = url + "searchShop.jsp?keyword=NBA"
print(url_new)

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    "AppleWebKit/537.36 (KHTML, like Gecko)"
    "Chrome/63.0.3239.132 Safari/537.36"
}

print("------------------------------")  # 30個

print("無 headers, 抓取 momo 網站")
html_data = requests.get(url_new)

if html_data.status_code == requests.codes.ok:
    html_data.encoding = "utf-8"
    print(html_data.text)
else:
    print("HTTP請求錯誤..." + url)

print("------------------------------")  # 30個

print("使用 headers, 抓取 momo 網站")

html_data = requests.get(url_new, headers=headers)

if html_data.status_code == requests.codes.ok:
    html_data.encoding = "utf-8"
    print(html_data.text)
else:
    print("HTTP請求錯誤..." + url)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
""" webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

url="https://www.momoshop.com.tw/search/"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get(url+"searchShop.jsp?keyword=NBA")

print("------------------------------")  # 30個

print(driver.title)
html = driver.page_source
fp = open("tmp_NBA.html", "w", encoding="utf8")
fp.write(html)
print("寫入檔案tmp_NBA.html...")
fp.close()
driver.quit()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
""" 久
url = "http://www.majortests.com/word-lists/word-list-0{0}.html"

for i in range(1, 10):
    url = url.format(i) 
    html_data = requests.get(url)
    print(html_data.status_code)
    print("等待5秒鐘... i = ", i)
    time.sleep(5) 
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

url = "https://fchart.github.io/Ashion/"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get(url)

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
        "image": url+img,
        "price": price
    })
driver.quit()
with open("tmp_products.json", "w", encoding="utf-8") as fp: # 寫入JSON檔案
    json.dump(products,fp,indent=2,
              sort_keys=True,
              ensure_ascii=False)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

url="https://fchart.github.io/ML/nba_items.html"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get(url)
pages_remaining = True
page_num = 1
while pages_remaining:
    soup = BeautifulSoup(driver.page_source, "lxml")
    tag_table = soup.select_one("#our-table")
    rows = tag_table.find_all("tr")
    csvfile = "tmp_NBA_Products" + str(page_num) + ".csv"
    with open(csvfile, "w+", newline="", encoding="utf8") as fp:
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
print("------------------------------------------------------------")  # 60個

# 目標url網址
url = "https://www.ptt.cc"
MAX_PUSH = 50
TOPIC = "Gossiping"
# TOPIC = "NBA"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    "AppleWebKit/537.36 (KHTML, like Gecko)"
    "Chrome/63.0.3239.132 Safari/537.36"
}

# 這兩個網站, 沒有用headers和cookies, 看起來也OK


def parse_html(html_data):
    if html_data.status_code == requests.codes.ok:
        html_data.encoding = "utf8"
        print("aaaa")
        print(html_data.text)
        print("bbbb")
        soup = BeautifulSoup(html_data.text, "lxml")
    else:
        print("HTTP請求錯誤..." + url)
        soup = None
    return soup


def get_articles(soup, date):
    articles = []
    # 取得上一頁的超連結
    print("找下一個內容分區元素<div> + 條件")
    paging_div = soup.find("div", class_="btn-group btn-group-paging")
    print("找全部的超連結<a> +  條件")
    paging_a = paging_div.find_all("a", class_="btn")
    prev_url = paging_a[1]["href"]

    print("找全部的內容分區元素<div> + 條件")
    tag_divs = soup.find_all("div", class_="r-ent")
    print(tag_divs)
    for tag in tag_divs:
        print(tag)
        # 判斷文章的日期
        if tag.find("div", class_="date").text.strip() == date:
            push_count = 0  # 取得推文數
            push_str = tag.find("div", class_="nrec").text
            if push_str:
                try:
                    push_count = int(push_str)  # 轉換成數字
                except ValueError:  # 轉換失敗，可能是"爆"或 "X1","X2"
                    if push_str == "爆":
                        push_count = 99
                    elif push_str.startswith("X"):
                        push_count = -10
            # 取得貼章的超連結和標題文字
            if tag.find("a"):  # 有超連結，表示文章存在
                href = tag.find("a")["href"]
                title = tag.find("a").text
                author = tag.find("div", class_="author").string
                articles.append(
                    {
                        "title": title,
                        "href": href,
                        "push_count": push_count,
                        "author": author,
                    }
                )
    return articles, prev_url


def save_to_json(articles, file):
    print("今天總共有: " + str(len(articles)) + " 篇文章")
    threshold = MAX_PUSH
    print("熱門文章(> %d 推): " % (threshold))
    for item in articles:  # 顯示熱門文章清單
        if int(item["push_count"]) > threshold:
            print(item["title"], item["href"], item["author"])
    with open(file, "w", encoding="utf-8") as fp:  # 寫入JSON檔案
        json.dump(articles, fp, indent=2, sort_keys=True, ensure_ascii=False)


def web_scraping_bot(url):
    articles = []
    print("抓取網路資料中...")
    cc = requests.get(url, headers=headers, cookies=cookies)
    soup = parse_html(cc)
    if soup:
        # 取得今天日期, 去掉開頭"0"符合PTT的日期格式
        today = time.strftime("%m/%d").lstrip("0")
        # 取得目前頁面的今日文章清單
        current_articles, prev_url = get_articles(soup, today)
        print("current_articles :", current_articles)
        articles += current_articles
        """ NG
        while current_articles:
            articles += current_articles
            print("等待2秒鐘...")
            time.sleep(2)
            # 剖析上一頁繼續尋找是否有今日的文章
            cc = requests.get(url + prev_url, headers=headers, cookies=cookies)
            soup = parse_html(cc)
            current_articles, prev_url = get_articles(soup, today)
        """
    return articles


url = url + "/bbs/" + TOPIC + "/index.html"
print(url)
articles = web_scraping_bot(url)
for item in articles:
    print(item)
save_to_json(articles, "tmp_articles.json")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
""" NG
url = "https://irs.thsrc.com.tw/IMINT/"

# 自訂表頭
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
}
# 自訂表頭
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
}

# 將自訂表頭加入 GET 請求中
html_data = requests.get(url, headers=headers)
print(html_data)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# webdriver
print("------------------------------------------------------------")  # 60個
""" NG
from selenium import webdriver

# 設定facebook登入資訊
url = "https://www.facebook.com/"
email = "你的faceook電子郵件"
password = "你的faceook密碼"
# 建立瀏覽器物件
driver = webdriver.Chrome()
# 最大化視窗後開啟facebook網站
driver.maximize_window()
driver.get(url)
# 執行自動登入動作
driver.find_element_by_id("email").send_keys(email)  # 輸入郵件
driver.find_element_by_id("pass").send_keys(password)  # 輸入密碼
driver.find_element_by_id("loginbutton").click()  # 按登入鈕
driver.find_element_by_name("login").click()  # 按登入鈕
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
""" NG
from selenium import webdriver

# 設定facebook登入資訊
url = "https://www.facebook.com/"
email = "你的faceook電子郵件"
password = "你的faceook密碼"

# 取消 Alert
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)

# 建立瀏覽器物件
driver = webdriver.Chrome(chrome_options=chrome_options)
# 最大化視窗後開啟facebook網站
driver.maximize_window()
driver.get(url)

# 執行自動登入動作
driver.find_element_by_id("email").send_keys(email)  # 輸入郵件
driver.find_element_by_id("pass").send_keys(password)  # 輸入密碼
driver.find_element_by_name("login").click()  # 按登入鈕
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# product.py

url = "https://data.coa.gov.tw/Service/OpenData/FromM/FarmTransData.aspx?FOTT=Xml"

import urllib.request as ur

with ur.urlopen(url) as response:
    get_xml = response.read()

data = BeautifulSoup(get_xml, "xml")

field1 = data.find_all("交易日期")
field2 = data.find_all("種類代碼")
field3 = data.find_all("作物代號")
field4 = data.find_all("作物名稱")
field5 = data.find_all("市場代號")
field6 = data.find_all("市場名稱")
field7 = data.find_all("上價")
field8 = data.find_all("中價")
field9 = data.find_all("下價")
fieldA = data.find_all("平均價")
fieldB = data.find_all("交易量")

csv_str = ""
for i in range(0, len(field1)):
    csv_str += "{},{},{},{},{},{},{},{},{},{},{}\n".format(
        field1[i].get_text(),
        field2[i].get_text(),
        field3[i].get_text(),
        field4[i].get_text(),
        field5[i].get_text(),
        field6[i].get_text(),
        field7[i].get_text(),
        field8[i].get_text(),
        field9[i].get_text(),
        fieldA[i].get_text(),
        fieldB[i].get_text(),
    )

with open("product.csv", "w") as f:
    result = f.write(csv_str)  # 寫入檔案

print("資料已寫入product.csv")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# xml_parse.py

"""
政府資料開放平臺 XML格式資料擷取與應用

"""
url = "https://apiservice.mol.gov.tw/OdService/download/A17000000J-000007-yrg"

import urllib.request as ur

with ur.urlopen(url) as response:
    get_xml = response.read()

data = BeautifulSoup(get_xml, "xml")
HandlingUnit = data.find_all("辦理單位")
ContactPerson = data.find_all("聯絡人")
DuringTraining = data.find_all("訓練期間")
ContactNumber = data.find_all("聯絡電話")
CourseTitle = data.find_all("課程名稱")


csv_str = ""
for i in range(0, len(HandlingUnit)):
    csv_str += "{},{},{},{},{}\n".format(
        HandlingUnit[i].get_text(),
        ContactPerson[i].get_text(),
        ContactNumber[i].get_text(),
        DuringTraining[i].get_text(),
        CourseTitle[i].get_text(),
    )

with open("course_xml.csv", "w") as f:
    story = f.write(csv_str)  # 寫入檔案

print("XML格式資料擷取與應用,已將資料寫入course_xml.csv")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# 目標URL網址
URL = "http://www.majortests.com/word-lists/word-list-0{0}.html"


def generate_urls(url, start_page, end_page):
    urls = []
    for page in range(start_page, end_page + 1):
        urls.append(url.format(page))
    return urls


def get_resource(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        "AppleWebKit/537.36 (KHTML, like Gecko)"
        "Chrome/63.0.3239.132 Safari/537.36"
    }
    return requests.get(url, headers=headers)


def parse_html(html_str):
    return BeautifulSoup(html_str, "lxml")


def get_words(soup, file):
    words = []
    count = 0

    for wordlist_table in soup.find_all(class_="wordlist"):
        count += 1
        for word_entry in wordlist_table.find_all("tr"):
            new_word = []
            new_word.append(file)
            new_word.append(str(count))
            new_word.append(word_entry.th.text)
            new_word.append(word_entry.td.text)
            words.append(new_word)

    return words


def save_to_csv(words, file):
    with open(file, "w+", newline="", encoding="utf-8") as fp:
        writer = csv.writer(fp)
        for word in words:
            writer.writerow(word)


def web_scraping_bot(urls):
    eng_words = []

    for url in urls:
        print("抓取: " + url + " 網路資料中...")
        file = url.split("/")[-1]
        # print("抓取: " + file + " 網路資料中...")
        html_data = get_resource(url)
        if html_data.status_code == requests.codes.ok:
            soup = parse_html(html_data.text)
            words = get_words(soup, file)
            eng_words = eng_words + words
            print("等待5秒鐘...")
            time.sleep(5)
        else:
            print("HTTP請求錯誤...")

    return eng_words


urls = generate_urls(URL, 1, 3)
print(urls)

print("---------------")  # 15個

eng_words = web_scraping_bot(urls)

print("---------------")  # 15個

"""
for item in eng_words:
    print(item)
"""
print("---------------")  # 15個

save_to_csv(eng_words, "tmp_words.csv")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


def showsite(siteurl):
    html = requests.get(siteurl).text
    soup = BeautifulSoup(html, "html.parser")
    kind = soup.select(".content-header-desc__detail")[
        1
    ].text.strip()  # 分類  # strip()用來刪除文字前面和後面多餘的空白
    area = soup.select(".content-header-desc__detail")[
        2
    ].text.strip()  # 區  # strip()用來刪除文字前面和後面多餘的空白
    item_desc = soup.select(".location-item .location-item__desc")  # 店名、地址
    name = item_desc[0].select("p")[0].text  # 店名
    imgurl = (
        soup.find("div", {"class": "images-featured-big-slider"})
        .get("style")
        .split("'")[1]
    )  # 圖片名稱
    lat = soup.select("#js-location-map")[0]["data-lat"]  # 緯度
    lng = soup.select("#js-location-map")[0]["data-lon"]  # 經度
    tel = soup.select(".location-item .location-item__desc")[
        2
    ].text.strip()  # 電話  # strip()用來刪除文字前面和後面多餘的空白
    addr = (
        item_desc[0]
        .select("p")[1]
        .text.replace(" ", "")
        .replace("\n", "")
        .strip()  # strip()用來刪除文字前面和後面多餘的空白
    )  # 地址
    desc = soup.select(".restaurant-desc")[
        0
    ].text.strip()  # 說明  # strip()用來刪除文字前面和後面多餘的空白
    working_hours = soup.select(".location-item .location-item__desc")[
        1
    ].text.strip()  # 營業時間  # strip()用來刪除文字前面和後面多餘的空白
    print("分類:", kind)  # 分類
    print("地區:", area)  # 地區
    print("店名:", name)  # 店名
    print("網址:", siteurl)  # 網址
    print("圖片名稱:", imgurl)  # 圖片名稱
    print("緯度:", lat)  # 緯度
    print("經度:", lng)  # 經度
    print("電話:", tel)  # 電話
    print("地址:", addr)  # 地址
    print("說明:", desc)  # 說明
    print("營業時間:", working_hours + "\n")  # 營業時間


def getpageurl(page, url):
    global n, totpages
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    items = soup.select(".grid-restaurants__item__inner")
    print("第" + str(page) + "頁,共有" + str(len(items)) + "間")
    for item in items:
        n += 1
        print("n=", n)
        itemurl = item.select(".resto-inner-title a")[0]["href"]  # 網址
        siteurl = rooturl + itemurl  # 組成完整網址
        showsite(siteurl)  # 顯示該店資訊
        if n == 1:
            totpages = int(
                soup.find("input", {"class": "form-control"})["data-max_page"]
            )  # 總頁數


# 主程式
n = 0  # 計算總共有多少家店
homeurl = "https://guide.michelin.com/tw/taipei/restaurants?max=30&sort=relevance"
rooturl = "https://guide.michelin.com"
getpageurl(1, homeurl)  # 首頁

for page in range(2, totpages + 1):  # 第 2~totpages頁
    html = requests.get(homeurl).text
    soup = BeautifulSoup(html, "html.parser")
    path = soup.find("a", {"class": "page-arrow"})  # 「>」 下一頁按鈕
    fullurl = path["href"]  # 讀取 href 內容
    # 以「?」分割，刪除前面字串中的最後一個字元，再加上 page 後，組成完整的路徑
    url = rooturl + fullurl.split("?")[0][:-1] + str(page) + "?" + fullurl.split("?")[1]
    getpageurl(page, url)

print("\n總共有", n, "間")

print("------------------------------------------------------------")  # 60個
print("使用 key ST")
print("------------------------------------------------------------")  # 60個

"""
會用到 KEY 的
氣象署 / 環境部

"""

import sys


def get_html_data1(url):
    print("取得網頁資料: ", url)
    resp = requests.get(url)
    # 檢查 HTTP 回應碼是否為 requests.codes.ok(200)
    if resp.status_code != requests.codes.ok:
        print("讀取網頁資料錯誤, url: ", resp.url)
        return None
    else:
        return resp


print("#抓中央氣象局的衛星雲圖")

url = "https://www.cwa.gov.tw/V8/C/W/OBS_Sat.html"

# TBD

"""
html_data = get_html_data1(url)
if html_data:
        soup = BeautifulSoup(html_data.text, 'html.parser')
        print("取得網頁標題", soup.title)
        print('搜尋網頁中的 jpg圖片連結')
        
        regex = re.compile('.*\.jpg')
        imglist = soup.find_all("img", {"src":regex})
        for img in imglist:
            print(img["src"])
        
else:
        print('無法取得網頁資料')
"""

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("使用 key SP")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("example ST")
print("------------------------------------------------------------")  # 60個

# class_ 的"_"符號是因為class是保留字，所以加上_符號作區別

import urllib.parse
import html5lib


# 無參數
def get_html_data1(url):
    print("取得網頁資料: ", url)
    resp = requests.get(url)
    # 檢查 HTTP 回應碼是否為 requests.codes.ok(200)
    if resp.status_code != requests.codes.ok:
        print("讀取網頁資料錯誤, url: ", resp.url)
        return None
    else:
        return resp


# Yahoo字典 ST
def searchdic(search_word):
    result = ""

    # yahoo字典的網址，可修改網址查詢想要的單字，網址當中的%s為格式化字串
    url = "https://tw.dictionary.search.yahoo.com/search?p=%s" % (search_word)
    html_data = get_html_data1(url)
    """ same
    payload = {'p': search_word}
    html_data = requests.get('https://tw.dictionary.search.yahoo.com/search?', params = payload)
    #相當於寫了 : https://tw.dictionary.search.yahoo.com/search?p=search_word
    """

    if html_data:
        result += "擷取網頁資料 OK\n"
        # print(html_data.text)
    else:
        print("無法取得網頁資料")
        return None

    soup = BeautifulSoup(html_data.text, "html.parser")
    # soup = BeautifulSoup(html_data.text, 'html5lib')   #也可
    # soup = BeautifulSoup(html_data.text, 'lxml')   # 指定 lxml 作為解析器
    print(soup.prettify())  # 把排版後的 html 印出來

    sorry_word = soup.find_all("div", class_="w-100p fz-16 va-mid ta-c")
    for sw in sorry_word:
        # print(type(sorry_word))
        # print(len(sorry_word))
        for di in sw:
            # print(di.text)
            # result += di.text.replace("\n", "") + "\n"
            if "很抱歉" in di.text:
                return None

    """
    # 一些屬性或方法, BeautifulSoup的用法
    print('---title---')
    print(soup.title) # 把 tag 抓出來
    print('---title.name---')
    print(soup.title.name) # 把 title 的 tag 名稱抓出來
    print('---title.string---')
    print(soup.title.string) # 把 title tag 的內容抓出來
    print('---title.parent.name---')
    print(soup.title.parent.name) # title tag 的上一層 tag
    print('---a---')
    print(soup.a) # 把第一個 <a></a> 抓出來
    print('---all a---')
    print(soup.find_all('a')) # 把所有的 <a></a> 抓出來
    print('---all div---')
    print(soup.find_all('div')) # 把所有的 <a></a> 抓出來
    """

    result += "上框\n"
    result += "上框 搜尋英文字 :\n"
    search_word = soup.find_all("span", class_="fz-24 fw-500 c-black lh-24")
    for sw in search_word:
        for di in sw:
            result += di.text.replace("\n", "") + "\n"

    result += "上框 音標 :\n"

    # 音標
    pronunciation = soup.find_all("span", class_="fz-14")
    result += "000" + pronunciation[0].text + "\n"  # 第0個是KK音標
    result += "111" + pronunciation[1].text + "\n"  # 第1個是DJ音標

    result += "上框 詞性 :\n"
    divs = soup.find_all("div", "compList mb-25 p-rel")  # 如此可以框選較大範圍之資料 找到較大的區塊包含所有資料

    # print(divs)
    for div in divs:
        # print(div)
        for di in div:
            for tt in di.find_all("li"):
                cc = tt.find("div", "pos_button fz-14 fl-l mr-12")
                if cc != None:  # 如果標題包含資料, 印出來
                    result += "詞性\n"
                    result += cc.text.replace("\n", "") + "\n"  # 只是刪除換行符號, 或許不一定有

                dd = tt.find("div", "fz-16 fl-l dictionaryExplanation")
                if dd != None:  # 如果標題包含資料, 印出來
                    result += "解釋\n"
                    result += dd.text.replace("\n", "") + "\n"  # 只是刪除換行符號, 或許不一定有

    result += "中框\n"
    result += "中框 釋義 :\n"

    divs = soup.find_all(
        "div",
        class_="grp grp-tab-content-explanation tabsContent-s tab-content-explanation pt-24 tabActived",
    )  # 如此可以框選較大範圍之資料 找到較大的區塊包含所有資料
    # print(divs)

    if divs == []:
        return result

    div1 = divs[0].find_all("div", "compTitle lh-25")
    length = len(div1)
    # print('a共找到', length, '筆資料')

    div2 = divs[0].find_all("div", "compTextList ml-50")
    length = len(div2)
    # print('b共找到', length, '筆資料')

    # 依照詞性數量的區塊做迴圈，將一個一個區塊作處理
    for nn in range(length):
        """debug
        print(nn)
        print('--------------------')
        print(div1[nn])   # 使用索引值, 只印出text部分
        print('--------------------')
        print(div2[nn])   # 使用索引值, 只印出text部分
        print('--------------------')
        """
        result += "詞性\n"
        result += (
            div1[nn].find("span", "pos_button fz-14").text.replace("\n", "")
        )  # 只是刪除換行符號, 或許不一定有
        result += (
            div1[nn].find("span", "fz-14 va-mid lh-22 ml-5").text.replace("\n", "")
            + "\n"
        )  # 只是刪除換行符號, 或許不一定有

        result += "解釋:\n"
        nnn2 = div2[nn].find_all("span")
        # print(nnn)
        # 這個迴圈將詞性區塊裡的單字意思一個一個抓出來顯示
        # 而每個單字意思及例句都是使用li標籤所包起來，所以將每個li標籤抓出來顯示他的單字意思及例句
        for n in nnn2:
            # print(n)
            for di in n:
                result += di.text.replace("\n", "")
            result += "\n"
    return result


# Yahoo字典 SP

"""test
print('------------------------------')
print('Yahoo字典')
search_word = 'coordinate'
#search_word = '英國'
result = searchdic(search_word)
print(result)
print('------------------------------')
print('Yahoo字典')
search_word = 'oat'
result = searchdic(search_word)
print(result)
print('------------------------------')
search_word = '英國'
result = searchdic(search_word)
print(result)
print('------------------------------')
"""

while True:
    print()
    search_word = input("請輸入查詢單字 : ")
    if search_word == "":
        continue
    if search_word == "q":
        break

    result = searchdic(search_word)
    if result == None:
        print("找不到 :", search_word)
    else:
        print(result)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 有參數 之 requests.get

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/77.0.3865.120 Safari/537.36"
}

url = "https://www.books.com.tw/web/sys_saletopb/books/19/?loc=P_0002_020"  # old
url = "https://www.books.com.tw/web/sys_saletopb/books/19/?loc=P_0002_021"

html_data = requests.get(url, headers=headers)

soup = BeautifulSoup(html_data.text, "html.parser")
# print(soup.prettify())  #prettify()這個函數可以將DOM tree以比較美觀的方式印出。

sel = "li.item"
ranking = soup.select(sel)

# print(ranking)

print()
print()
print()

cnt = 0
for rank, book in enumerate(ranking, 1):
    print(book)
    """
    title = book.h4.a.text
    detail = book.find_all("li")
    author = detail[0].text
    price = detail[1].text
    print(rank, title, author, price)

    print("第{}名".format(rank))
    print(book.h4.a.text)
    detail = book.find_all('a')
    print(detail[0].text)
    print(detail[1].text)
    """
    print("----")
    cnt += 1
    if cnt == 10:
        break

print("Done")


print("------------------------------------------------------------")  # 60個


def showbook(url, kind):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    try:
        pages = int(soup.select(".cnt_page span")[0].text)  # 該分類共有多少頁
        print("共有", pages, "頁")
        for page in range(1, pages + 1):
            pageurl = url + "&page=" + str(page).strip()
            print("第", page, "頁", pageurl)
            showpage(pageurl, kind)
    except:  # 沒有分頁的處理
        showpage(url, kind)


def showpage(url, kind):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    # 近期新書、在 class="mod type02_m012 clearfix" 中
    res = soup.find_all("div", {"class": "mod type02_m012 clearfix"})[0]
    items = res.select(".item")  # 所有 item
    n = 0  # 計算該分頁共有多少本書
    for item in items:
        msg = item.select(".msg")[0]
        src = item.select("a img")[0]["src"]
        title = msg.select("a")[0].text  # 書名
        imgurl = src.split("?i=")[-1].split("&")[0]  # 圖片網址
        author = msg.select("a")[1].text  # 作者
        publish = msg.select("a")[2].text  # 出版社
        date = msg.find("span").text.split("：")[-1]  # 出版日期
        onsale = item.select(".price .set2")[0].text  # 優惠價
        content = item.select(".txt_cont")[0].text.replace(" ", "").strip()  # 內容
        print("\n分類：" + kind)
        print("書名：" + title)
        print("圖片網址：" + imgurl)
        print("作者：" + author)
        print("出版社：" + publish)
        print("出版日期：" + date)
        print(onsale)  # 優惠價
        print("內容：" + content)
        n += 1
        print("n=", n)


#
#        if n==2: break  # 開發階段


def twobyte(kindno):
    if kindno < 10:
        kindnostr = "0" + str(kindno)
    else:
        kindnostr = str(kindno)
    return kindnostr


# 主程式
kindno = 1  # 計算共有多少分類
homeurl = "http://www.books.com.tw/web/books_nbtopm_01/?o=5&v=1"
mode = "?o=5&v=1"  # 顯示模式：直式  排序依：暢銷度
url = "http://www.books.com.tw/web/books_nbtopm_"
html = requests.get(homeurl).text
soup = BeautifulSoup(html, "html.parser")
# 中文書新書分類，算出共有多少分類
res = soup.find("div", {"class": "mod_b type02_l001-1 clearfix"})
hrefs = res.select("a")
for href in hrefs:
    kindurl = url + twobyte(kindno) + mode  # 分類網址
    print("\nkindno=", kindno)
    kind = href.text  # 分類
    showbook(kindurl, kind)  # 顯示該分類所有書籍
    kindno += 1
#    if kindno==2: break  # 開發階段


print("------------------------------------------------------------")  # 60個


def showbook(url, kind):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    try:
        pages = int(soup.select(".cnt_page span")[0].text)  # 該分類共有多少頁
        print("共有", pages, "頁")
        for page in range(1, pages + 1):
            pageurl = url + "&page = " + str(page).strip()
            print("第", page, "頁", pageurl)
            showpage(pageurl, kind)
    except:  # 沒有分頁的處理
        showpage(url, kind)


def showpage(url, kind):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    # 近期新書、在 class = "mod type02_m012 clearfix" 中
    res = soup.find_all("div", {"class": "mod type02_m012 clearfix"})[0]
    items = res.select(".item")  # 所有 item
    n = 0  # 計算該分頁共有多少本書
    for item in items:
        msg = item.select(".msg")[0]
        src = item.select("a img")[0]["src"]
        title = msg.select("a")[0].text  # 書名
        imgurl = src.split("?i = ")[-1].split("&")[0]  # 圖片網址
        author = msg.select("a")[1].text  # 作者
        publish = msg.select("a")[2].text  # 出版社
        date = msg.find("span").text.split("：")[-1]  # 出版日期
        onsale = item.select(".price .set2")[0].text  # 優惠價
        content = item.select(".txt_cont")[0].text.replace(" ", "").strip()  # 內容
        # 將資料加入 list1 串列中
        listdata = [kind, title, imgurl, author, publish, date, onsale, content]
        list1.append(listdata)
        n += 1
        print("n = ", n)


def twobyte(kindno):
    if kindno < 10:
        kindnostr = "0" + str(kindno)
    else:
        kindnostr = str(kindno)
    return kindnostr


# 主程式
list1 = []
kindno = 1  # 計算共有多少分類
homeurl = "http://www.books.com.tw/web/books_nbtopm_01/?o=5&v=1"
mode = "?o=5&v=1"  # 顯示模式：直式  排序依：暢銷度
url = "http://www.books.com.tw/web/books_nbtopm_"
html = requests.get(homeurl).text
soup = BeautifulSoup(html, "html.parser")
# 中文書新書分類，算出共有多少分類
res = soup.find("div", {"class": "mod_b type02_l001-1 clearfix"})
hrefs = res.select("a")
for href in hrefs:
    kindurl = url + twobyte(kindno) + mode  # 分類網址
    print("\nkindno = ", kindno)
    kind = href.text  # 分類
    showbook(kindurl, kind)  # 顯示該分類所有書籍
    kindno += 1

# excel 資料
listtitle = ["分類", "書名", "圖片網址", "作者", "出版社", "出版日期", "優惠價", "內容"]
print(listtitle)  # 標題

for _ in list1:  # 資料
    print(_)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "http://www.daxi-hro.tycg.gov.tw/home.jsp?id=25&parentpath=0,21,22"
content = requests.get(url).text
soup = BeautifulSoup(content, "html.parser")

# 人口統計
person_data = list()  # 人口統計資料
data1 = soup.find("tbody")
# print(data1)

rows = data1.find_all("tr")
for row in rows:
    cols = row.find_all("td")
    if len(cols) > 0:
        if cols[1].text != "─":
            person_data.append(
                (
                    (int)(cols[0].text.strip()[:-1]),
                    (int)(cols[1].text),
                    (int)(cols[2].text),
                    (int)(cols[3].text),
                )
            )
        else:
            print("xxxxxx1111")
    else:
        print("xxxxxx2222")

person_data.reverse()  # 反相
length = len(person_data)
year1 = []
person1 = []
person2 = []
person3 = []
for i in range(0, length):
    year1.append(person_data[i][0])
    person1.append(person_data[i][1])
    person2.append(person_data[i][2])
    person3.append(person_data[i][3])

# 戶數統計
house_data = list()  # 戶數統計資料
data1 = soup.select("table[summary^='歷年戶數統計列表排版用']")[0]
# print(data1)

rows = data1.find_all("tr")
for row in rows:
    cols = row.find_all("td")
    if len(cols) > 0:
        if cols[1].text != "─":
            house_data.append(((int)(cols[0].text.strip()[:-1]), (int)(cols[1].text)))
        else:
            print("xxxxxx1111")
    else:
        print("xxxxxx2222")

house_data.reverse()  # 反相
length = len(house_data)
year2 = []
house = []
for i in range(0, length):
    year2.append(house_data[i][0])
    house.append(house_data[i][1])

"""
print('person_data')
print(person_data)
print('house_data')
print(house_data)
print('year1')
print(year1)
print('person1')
print(person1)
print('person2')
print(person2)
print('person3')
print(person3)
print('year2')
print(year2)
print('house')
print(house)
"""

print("------------------------------------------------------------")  # 60個

# 開始畫圖

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

#          編號                          圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(
    num="plot 集合 1 函數曲線",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示

# 第一張圖
plt.subplot(211)

plt.plot(year1, person1, linewidth=2.0, label="男")
plt.plot(year1, person2, linewidth=2.0, label="女")
plt.title("桃園市大溪區歷年人口數")
plt.xlabel("年度")
plt.ylabel("人口數")
plt.legend()

# 第二張圖
plt.subplot(212)

plt.plot(year2, house, linewidth=2.0)
plt.title("桃園市大溪區歷年戶數")
plt.xlabel("年度")
plt.ylabel("戶數")

plt.show()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


"""
url = 'https://siluo.household.yunlin.gov.tw/popul05/List.aspx?Parser=99,5,47,,,,,,,,,,,,,,,,,,,,,4'
content = requests.get(url).text
soup = BeautifulSoup(content, "html.parser")

#print(soup)

links = soup.find_all("li", class_="list_date")    # 文章標題
for link in links:
    print(link.text.strip()) # strip()用來刪除文字前面和後面多餘的空白
    dddd = link.find_all("span", role="gridcell")    # 文章標題
    for ddd in dddd:
        print(ddd.text.strip())
    print()


"""

"""

#人口統計
person_data = list()    #人口統計資料
data1 = soup.find("tbody")
#print(data1)


<li class="list_date">


rows = data1.find_all("tr")
for row in rows:
    cols = row.find_all("td")
    if(len(cols) > 0):
        if cols[1].text != "─":
            person_data.append(((int)(cols[0].text.strip()[:-1]), (int)(cols[1].text), (int)(cols[2].text), (int)(cols[3].text)))
        else:
            print('xxxxxx1111')
    else:
        print('xxxxxx2222')

person_data.reverse()   #反相
length = len(person_data)
year1 = []
person1 = []
person2 = []
person3 = []
for i in range(0, length): 
    year1.append(person_data[i][0])
    person1.append(person_data[i][1])
    person2.append(person_data[i][2])
    person3.append(person_data[i][3])
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("有無 cookies 之比較")

# gossiping
url = "https://www.ptt.cc/bbs/Gossiping/index.html"  # 八卦板的網址

print("無 cookies")
html_data = requests.get(url)
# print(html_data.text)
soup = BeautifulSoup(html_data.text, "html.parser")
print(soup.prettify())

print("有 cookies")
cookies = {"over18": "1"}
html_data = requests.get(url, cookies=cookies)
# print(html_data.text)
soup = BeautifulSoup(html_data.text, "html.parser")
print(soup.prettify())

print("BeautifulSoup 測試 1a 使用 cookie")

url = "https://www.ptt.cc/bbs/Gossiping/index.html"  # 八卦板的網址

my_headers = {"cookie": "over18=1"}  # cookie設定

response = requests.get(url, headers=my_headers)  # 放在headers欄位中傳送
soup = BeautifulSoup(response.text, "html.parser")  # 解析原始碼
# print(soup.prettify())
links = soup.find_all("div", class_="title")  # 文章標題
# print(links)
for link in links:
    print(link.text.strip())  # strip()用來刪除文字前面和後面多餘的空白

print("BeautifulSoup 測試 1b 使用 session")

# post要傳的資料
payload = {"from": "/bbs/Gossiping/index.html", "yes": "yes"}

rs = requests.session()  # 用session紀錄此次使用的cookie
response = rs.post("https://www.ptt.cc/ask/over18", data=payload)  # post傳遞資料
response = rs.get(url)  # 再get一次PTT八卦板首頁
print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")
links = soup.find_all("div", class_="title")  # 文章標題
for link in links:
    print(link.text.strip())  # strip()用來刪除文字前面和後面多餘的空白

print("BeautifulSoup 測試 1c")

url = "https://www.ptt.cc/bbs/Gossiping/index.html"  # 八卦板的網址

payload = {"from": url, "yes": "yes"}
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
}
rs = requests.Session()
rs.post("https://www.ptt.cc/ask/over18", data=payload, headers=headers)
res = rs.get(url, headers=headers)

soup = BeautifulSoup(res.text, "html.parser")
items = soup.select(".r-ent")
for item in items:
    print(
        item.select(".date")[0].text,
        item.select(".author")[0].text,
        item.select(".title")[0].text,
    )

print("------------------------------")  # 30個

# post要傳的資料
payload = {"from": "/bbs/Gossiping/index.html", "yes": "yes"}

# 用session紀錄此次使用的cookie
rs = requests.session()
# post傳遞資料
response = rs.post("https://www.ptt.cc/ask/over18", data=payload)
# 再get一次PTT八卦板首頁
response = rs.get("https://www.ptt.cc/bbs/Gossiping/index.html")
print(response.status_code)

root = BeautifulSoup(response.text, "html.parser")
links = root.find_all("div", class_="title")  # 文章標題
for link in links:
    page_url = "https://www.ptt.cc" + link.a["href"]
    print(page_url)
    response = rs.get(page_url)
    result = BeautifulSoup(response.text, "html.parser")
    main_content = result.find("div", id="main-content")
    article_info = main_content.find_all("span", class_="article-meta-value")
    if len(article_info) != 0:
        author = article_info[0].string  # 作者
        title = article_info[2].string  # 標題
        time = article_info[3].string  # 時間
    else:  # 避免有沒有資訊的狀況
        author = "無"  # 作者
        title = "無"  # 標題
        time = "無"  # 時間
    # print(author + ' ' + title + ' ' + time)
    # 將整段文字內容抓出來
    all_text = main_content.text
    # 以--切割，抓最後一個--前的所有內容
    pre_texts = all_text.split("--")[:-1]
    # 將前面的所有內容合併成一個
    one_text = "--".join(pre_texts)
    # 以\n切割，第一行標題不要
    texts = one_text.split("\n")[1:]
    # 將每一行合併
    content = "\n".join(texts)
    print(content)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# PTT八卦版爬蟲

# 基本參數
url = "https://www.ptt.cc/bbs/Gossiping/index.html"
payload = {"from": "/bbs/Gossiping/index.html", "yes": "yes"}
data = []  # 全部文章的資料
num = 0

# 用session紀錄此次使用的cookie
rs = requests.session()
response = rs.post("https://www.ptt.cc/ask/over18", data=payload)

# 爬取兩頁
for i in range(2):
    # get取得頁面的HTML
    # print(url)
    response = rs.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup.prettify())

    # 找出每篇文章的連結
    links = soup.find_all("div", class_="title")
    for link in links:
        # 如果文章已被刪除，連結為None
        if link.a != None:
            article_data = {}  # 單篇文章的資料
            page_url = "https://www.ptt.cc/" + link.a["href"]

            # 進入文章頁面
            response = rs.get(page_url)
            result = BeautifulSoup(response.text, "html.parser")
            # print(soup.prettify())

            # 找出作者、標題、時間、留言
            main_content = result.find("div", id="main-content")
            article_info = main_content.find_all("span", class_="article-meta-value")

            if len(article_info) != 0:
                author = article_info[0].string  # 作者
                title = article_info[2].string  # 標題
                time = article_info[3].string  # 時間
            else:
                author = "無"  # 作者
                title = "無"  # 標題
                time = "無"  # 時間

            # print(author)
            # print(title)
            # print(time)

            article_data["author"] = author
            article_data["title"] = title
            article_data["time"] = time

            # 將整段文字內容抓出來
            all_text = main_content.text
            # 以--切割，抓最後一個--前的所有內容
            pre_texts = all_text.split("--")[:-1]
            # 將前面的所有內容合併成一個
            one_text = "--".join(pre_texts)
            # 以\n切割，第一行標題不要
            texts = one_text.split("\n")[1:]
            # 將每一行合併
            content = "\n".join(texts)

            # print(content)
            article_data["content"] = content

            # 一種留言一個列表
            comment_dic = {}
            push_dic = []
            arrow_dic = []
            shu_dic = []

            # 抓出所有留言
            comments = main_content.find_all("div", class_="push")
            for comment in comments:
                push_tag = comment.find("span", class_="push-tag").string  # 分類標籤
                push_userid = comment.find("span", class_="push-userid").string  # 使用者ID
                push_content = comment.find(
                    "span", class_="push-content"
                ).string  # 留言內容
                push_time = comment.find(
                    "span", class_="push-ipdatetime"
                ).string  # 留言時間

                # print(push_tag, push_userid, push_content, push_time)

                dict1 = {
                    "push_userid": push_userid,
                    "push_content": push_content,
                    "push_time": push_time,
                }
                if push_tag == "推 ":
                    push_dic.append(dict1)
                if push_tag == "→ ":
                    arrow_dic.append(dict1)
                if push_tag == "噓 ":
                    shu_dic.append(dict1)

            # print(push_dic)
            # print(arrow_dic)
            # print(shu_dic)
            # print("--------")

            comment_dic["推"] = push_dic
            comment_dic["→"] = arrow_dic
            comment_dic["噓"] = shu_dic
            article_data["comment"] = comment_dic

            # print(article_data)
            data.append(article_data)
            num += 1
            print("第 " + str(num) + " 篇文章完成!")

    # 找到上頁的網址，並更新url
    url = "https://www.ptt.cc/" + soup.find("a", string="‹ 上頁")["href"]

# print(data)
# 輸出JSON檔案
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "https://www.ptt.cc/bbs/Gossiping/index.html"

session = requests.Session()
payload = {"from": "/bbs/Gossiping/index.html", "yes": "yes"}
session.post(
    "https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html", payload
)

# html_data = requests.get(url)  #直接抓, 抓不到資料, 因為有擋
html_data = session.get(url)

soup = BeautifulSoup(html_data.text, "html.parser")

titles = soup.select(".title")

for title in titles:
    print(title.a.text)
    print(title.a["href"])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "http://blog.castman.net/web-crawler-tutorial/ch1/connect.html"

try:
    resp = requests.get(url)
except:
    resp = None

if resp and resp.status_code == 200:
    print(resp.status_code)
    print(resp.text)
    soup = BeautifulSoup(resp.text, "html.parser")
    print(soup)
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

print("------------------------------")  # 30個


def get_header_text(url, header_tag):
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, "html.parser")
            return soup.find(header_tag).text
    except Exception as exception:
        return None


print("------------------------------")  # 30個

url = "http://blog.castman.net/web-crawler-tutorial/ch1/connect.html"

h1 = get_header_text(url, "h1")
if h1:
    print("h1: " + h1)

h2 = get_header_text(url, "h2")
if h2:
    print("h2: " + h2)

p = get_header_text(url, "p")
if p:
    print("p: " + p)

print("------------------------------")  # 30個

# PTT八卦版今日熱門文章

PTT_URL = "https://www.ptt.cc"


def get_web_page(url):
    resp = requests.get(url=url, cookies={"over18": "1"})
    if resp.status_code != 200:
        print("Invalid url:", resp.url)
        return None
    else:
        return resp.text


def get_articles(dom, date):
    soup = BeautifulSoup(dom, "html5lib")
    # Retrieve the link of previous page
    paging_div = soup.find("div", "btn-group btn-group-paging")
    prev_url = paging_div.find_all("a")[1]["href"]

    articles = []
    divs = soup.find_all("div", "r-ent")
    for d in divs:
        # If post date matched:
        if d.find("div", "date").text.strip() == date:
            # To retrieve the push count:
            push_count = 0
            push_str = d.find("div", "nrec").text
            if push_str:
                try:
                    push_count = int(push_str)
                except ValueError:
                    # If transform failed, it might be '爆', 'X1', 'X2', etc.
                    if push_str == "爆":
                        push_count = 99
                    elif push_str.startswith("X"):
                        push_count = -10

            # To retrieve title and href of the article:
            if d.find("a"):
                href = d.find("a")["href"]
                title = d.find("a").text
                author = d.find("div", "author").text if d.find("div", "author") else ""
                articles.append(
                    {
                        "title": title,
                        "href": href,
                        "push_count": push_count,
                        "author": author,
                    }
                )

    return articles, prev_url


def get_author_ids(posts, pattern):
    ids = set()
    for post in posts:
        if pattern in post["author"]:
            ids.add(post["author"])
    return ids


def main():
    current_page = get_web_page(PTT_URL + "/bbs/Gossiping/index.html")
    if current_page:
        # To keep all of today's articles.
        articles = []
        # Today's date, here we remove the 0 at the head to match the format of PTT date.
        # API doc for strftime: https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
        # API doc for lstrip: https://www.tutorialspoint.com/python/string_lstrip.htm
        today = time.strftime("%m/%d").lstrip("0")
        current_articles, prev_url = get_articles(current_page, today)

        while current_articles:
            articles += current_articles
            current_page = get_web_page(PTT_URL + prev_url)
            current_articles, prev_url = get_articles(current_page, today)

        print("Today's 5566:")
        print(get_author_ids(articles, "5566"))

        print("\nThere are ", len(articles), " posts today.")
        threshold = 50
        print("Hot post(≥ %d push): " % threshold)
        for article in articles:
            if int(article["push_count"]) > threshold:
                print(article)
        # with as: https://openhome.cc/Gossip/Python/WithAs.html
        # json.dump: http://python3-cookbook.readthedocs.io/zh_CN/latest/c06/p02_read-write_json_data.html
        with open("gossiping.json", "w", encoding="UTF-8") as file:
            json.dump(articles, file, indent=2, sort_keys=True, ensure_ascii=False)


if __name__ == "__main__":
    main()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

PTT_URL = "https://www.ptt.cc"
FREEGEOIP_API = "http://freegeoip.net/json/"


def get_web_page(url):
    resp = requests.get(url=url, cookies={"over18": "1"})
    if resp.status_code != 200:
        print("Invalid url: ", resp.url)
        return None
    else:
        return resp.text


def get_articles(dom, date):
    soup = BeautifulSoup(dom, "html5lib")
    # Retrieve the link of previous page
    paging_div = soup.find("div", "btn-group btn-group-paging")
    prev_url = paging_div.find_all("a")[1]["href"]

    articles = []
    divs = soup.find_all("div", "r-ent")
    for d in divs:
        # If post date matched:
        if d.find("div", "date").text.strip() == date:
            # To retrieve the push count:
            push_count = 0
            push_str = d.find("div", "nrec").text
            if push_str:
                try:
                    push_count = int(push_str)
                except ValueError:
                    # If transform failed, it might be '爆', 'X1', 'X2', etc.
                    if push_str == "爆":
                        push_count = 99
                    elif push_str.startswith("X"):
                        push_count = -10

            # To retrieve title and href of the article:
            if d.find("a"):
                href = d.find("a")["href"]
                title = d.find("a").text
                author = d.find("div", "author").text if d.find("div", "author") else ""
                articles.append(
                    {
                        "title": title,
                        "href": href,
                        "push_count": push_count,
                        "author": author,
                    }
                )

    return articles, prev_url


def get_ip(dom):
    # e.g., ※ 發信站: 批踢踢實業坊(ptt.cc), 來自: 27.52.6.175
    pattern = "來自: \d+\.\d+\.\d+\.\d+"
    match = re.search(pattern, dom)
    if match:
        return match.group(0).replace("來自: ", "")
    else:
        return None


def main():
    print("取得今日文章列表:")
    current_page = get_web_page(PTT_URL + "/bbs/Gossiping/index.html")
    if current_page:
        articles = []
        today = time.strftime("%m/%d").lstrip("0")
        current_articles, prev_url = get_articles(current_page, today)
        while current_articles:
            articles += current_articles
            current_page = get_web_page(PTT_URL + prev_url)
            current_articles, prev_url = get_articles(current_page, today)

        length = len(articles)
        print("共 %d 篇文章" % length)

        for i in range(0, 10):
            print(articles[i])

        print()
        print()
        print("取得前10篇文章的資料")
        for article in articles[:10]:
            print(article["title"])

        print("取得前10篇文章的IP:")
        country_to_count = dict()
        for article in articles[:10]:
            print("查詢 IP:", article["title"])
            print("111")
            page = get_web_page(PTT_URL + article["href"])
            print("222")
            if page:
                ip = get_ip(page)
                print(ip)


if __name__ == "__main__":
    main()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "https://www.taiwanlottery.com.tw/"
r = requests.get(url)
# sp = BeautifulSoup(r.text, 'lxml')
sp = BeautifulSoup(r.text, "html.parser")
# 找到威力彩的區塊
datas = sp.find("div", class_="contents_box02")
# 開獎期數
title = datas.find("span", "font_black15").text
print("威力彩期數：", title)
# 開獎號碼
nums = datas.find_all("div", class_="ball_tx ball_green")
# 開出順序
print("開出順序：", end=" ")
for i in range(0, 6):
    print(nums[i].text, end=" ")
# 大小順序
print("\n大小順序：", end=" ")
for i in range(6, 12):
    print(nums[i].text, end=" ")
# 第二區
num = datas.find("div", class_="ball_red").text
print("\n第二區：", num)


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("example SP")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

# 1515
print("---------------")  # 15個

# 3030
print("------------------------------")  # 30個

"""
# 基本

<html>：HTML 文件/根元素
<head>
HTML 中的 <head> 元素包含有關文件的機器可讀信息（後設資料），例如 標題、腳本、樣式表。

<body>：文件主體元素

<title>
HTML <title> 元素定義了顯示在瀏覽器標題欄或頁面標籤上的文件標題。它僅包含文本，元素內的標籤會被忽略。

<a>：超連結元素
<p>：段落元素
<img>: The Image Embed element
<b>: The Bring Attention To element
<meta>: The metadata element
<h1>–<h6>: The HTML Section Heading elements

<br>: The Line Break element

<script>: The Script element
<style>: The Style Information element

# 表格 list/table

<tr>: The Table Row element

<div>: The Content Division element

<ul>: The Unordered List element
<li>: The List Item element
<link>: The External Resource Link element
<section>: The Generic Section element
<strong>: The Strong Importance element
<center>: The Centered Text element
<ol>: The Ordered List element
<span>: The Content Span element
<td>: The Table Data Cell element
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 用find找
print("找全部的影像<img>")
all_imgs = soup.find_all("img")  # 取得 全部 <img></img>
print(all_imgs)

# 用find找
print("找全部的影像<img>")
all_imgs = soup.find_all("img")  # 取得 全部 <img></img>
for photo in all_imgs:
    if photo["src"].startswith("http"):
        print(photo["src"])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("抓取網頁 分析 12")

url = "https://tw.appledaily.com/new/realtime/"
html_data = requests.get(url)
soup = BeautifulSoup(html_data.text, "lxml")
# soup = get_soup_from_url(url)

headlines = soup.find("ul", {"class": "rtddd slvl"})
items = headlines.find_all("li")  # 取得 全部 <li></li>
for item in items:
    print(item.find("h1").text)
    time.sleep(random.randint(0, 2))
    content_url = item.find("a")["href"]
    print(content_url)
    html_data = requests.get(content_url)
    soup = BeautifulSoup(html_data.text, "lxml")
    # soup = get_soup_from_url(url)
    print("找下一個標題<h1>")
    title = soup.find("h1")
    print(title.text)
    article = soup.find("article", {"class": "ndArticle_content clearmen"})
    print(article.find("p").text)

print("------------------------------")  # 30個

cc = soup.find(name="p")
# 等同於
cc = soup.find("p")

print("------------------------------")  # 30個

url = "http://www.google.com.tw"
path = "tmp_logo.png"
html_data = requests.get(url)
html_data.encoding = "utf8"
soup = BeautifulSoup(html_data.text, "lxml")
tag_img = soup.find("img")
# 取出Logo圖片的正規運算式
match = re.search(r"(/[^/#?]+)+\.(?:jpg|gif|png)", str(tag_img))
print(match.group())
url = url + str(match.group())
html_data = requests.get(url, stream=True)
if html_data.status_code == 200:
    with open(path, "wb") as fp:
        for chunk in html_data:
            fp.write(chunk)
    print("圖檔logo.png已經下載")
else:
    print("錯誤! HTTP請求失敗...")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "https://fchart.github.io/ML/table.html"
csvfile = "tmp_CompanySales.csv"
html_data = requests.get(url)
html_data.encoding = "utf8"
soup = BeautifulSoup(html_data.text, "lxml")

tag_table = soup.find(class_="tt")  # 找到<table>
rows = tag_table.findAll("tr")  # 找出所有<tr>

# 開啟CSV檔案寫入截取的資料
with open(csvfile, "w+", newline="", encoding="utf-8") as fp:
    writer = csv.writer(fp)
    for row in rows:
        rowList = []
        for cell in row.findAll(["td", "th"]):
            rowList.append(cell.get_text().replace("\n", "").replace("\r", ""))
        writer.writerow(rowList)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# taiwanlottery.py

url = "https://www.taiwanlottery.com.tw/"
html_data = requests.get(url)
soup = BeautifulSoup(html_data.text, "lxml")

# 找到威力彩的區塊
datas = soup.find("div", class_="contents_box02")
# 開獎期數
title = datas.find("span", "font_black15").text
print("威力彩期數：", title)
# 開獎號碼
nums = datas.find_all("div", class_="ball_tx ball_green")
# 開出順序
print("開出順序：", end=" ")
for i in range(0, 6):
    print(nums[i].text, end=" ")
# 大小順序
print("\n大小順序：", end=" ")
for i in range(6, 12):
    print(nums[i].text, end=" ")
# 第二區
num = datas.find("div", class_="ball_red").text
print("\n第二區：", num)


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# lineimage.py

url = "https://store.line.me/stickershop/product/8991459/zh-Hant"
url = "https://store.line.me/stickershop/product/10571593/zh-Hant"
html = requests.get(url)
soup = BeautifulSoup(html.text, "html.parser")

# 建立目錄儲存圖片
download_image_dir = "tmp_line_image/"
if not os.path.exists(download_image_dir):
    os.mkdir(download_image_dir)

# 下載貼圖
datas = soup.find_all("li", {"class": "mdCMN09Li FnStickerPreviewItem"})
for data in datas:
    # 將字串資料轉換為字典
    imginfo = json.loads(data.get("data-preview"))
    id = imginfo["id"]
    imgfile = requests.get(imginfo["staticUrl"])  # 載入圖片

    full_path = os.path.join(download_image_dir, id)  # 儲存的路徑和主檔名
    # 儲存圖片
    with open(full_path + ".png", "wb") as f:
        f.write(imgfile.content)
    print(full_path + ".png")  # 顯示儲存的路徑和檔名
#    break  # 測試用

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# lineimage_adv.py

url = "https://store.line.me/stickershop/product/8991459/zh-Hant"
url = "https://store.line.me/stickershop/product/10571593/zh-Hant"
html = requests.get(url)
soup = BeautifulSoup(html.text, "html.parser")

# 建立目錄儲存圖片
download_image_dir = "tmp_line_image2/"
if not os.path.exists(download_image_dir):
    os.mkdir(download_image_dir)

# 下載貼圖
datas = soup.find_all("a", {"class": "FnRelatedStickerLink"})
for data in datas:
    imginfo = data.find("img")
    id = re.findall(r"[\d]+", data["href"])[0]
    imgfile = requests.get(imginfo["src"])  # 載入圖片

    full_path = os.path.join(download_image_dir, id)  # 儲存的路徑和主檔名
    # 儲存圖片
    with open(full_path + ".png", "wb") as f:
        f.write(imgfile.content)
    print(full_path + ".png")  # 顯示儲存的路徑和檔名

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "https://store.line.me/stickershop/product/8991459/zh-Hant"

html = requests.get(url)

soup = BeautifulSoup(html.text, "html.parser")
datas = soup.find_all("li", {"class": "mdCMN09Li FnStickerPreviewItem"})

# 建立目錄儲存圖片
download_image_dir = "tmp_line_image3/"
if not os.path.exists(download_image_dir):
    os.mkdir(download_image_dir)

for data in datas:
    imginfo = json.loads(data.get("data-preview"))
    id = imginfo["id"]
    imgfile = requests.get(imginfo["staticUrl"])
    full_path = download_image_dir + id + ".png"

    with open(full_path, "wb") as f:
        f.write(imgfile.content)
        print(full_path)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# load_url_images.py
from urllib.request import urlopen

# 第3屆埔里跑 Puli Power 山城派對馬拉松  向善橋(約34K)
url = "http://tw.running.biji.co/index.php?q=album&act=photo_list&album_id=30668&cid=5791&type=album&subtitle=第3屆埔里跑 Puli Power 山城派對馬拉松-向善橋(約34K)"
html = requests.get(url)

soup = BeautifulSoup(html.text, "html.parser")
title = soup.find(
    "h1", {"class": "album-title flex-1"}
).text.strip()  # strip()用來刪除文字前面和後面多餘的空白

url = "https://running.biji.co/index.php?pop=ajax&func=album&fename=load_more_photos_in_listing_computer"

payload = {
    "type": "album",
    "rows": "0",
    "need_rows": "20",
    "cid": "5791",
    "album_id": "30668",
}
html = requests.post(url, data=payload)
# 在回應頁面中找出所有照片連結
soup = BeautifulSoup(html.text, "html.parser")

# 以標題建立目錄儲存圖片
download_image_dir = title + "/"
if not os.path.exists(download_image_dir):
    os.mkdir(download_image_dir)

# 處理所有 <img> 標籤
photos = soup.select(".photo_img")  # 尋找class是photo_img
n = 0
for photo in photos:
    # 讀取 src 屬性內容
    src = photo["src"]
    # 讀取 .jpg 檔
    if src != None and (".jpg" in src):
        # 設定圖檔完整路徑
        full_path = src
        filename = full_path.split("/")[-1]  # 取得圖檔名
        print(full_path)
        # 儲存圖片
        try:
            image = urlopen(full_path)
            with open(os.path.join(download_image_dir, filename), "wb") as f:
                f.write(image.read())
            n += 1
        except:
            print("{} 無法讀取!".format(filename))

print("共下載", n, "張圖片")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# load_url_images_adv.py
from urllib.request import urlopen

# 第3屆埔里跑 Puli Power 山城派對馬拉松  向善橋(約34K)
url = "http://tw.running.biji.co/index.php?q=album&act=photo_list&album_id=30668&cid=5791&type=album&subtitle=第3屆埔里跑 Puli Power 山城派對馬拉松-向善橋(約34K)"
html = requests.get(url)

soup = BeautifulSoup(html.text, "html.parser")
title = (
    soup.find("h1", {"class": "album-title flex-1"}).text.strip() + "_全部相片"
)  # strip()用來刪除文字前面和後面多餘的空白

url = "https://running.biji.co/index.php?pop=ajax&func=album&fename=load_more_photos_in_listing_computer"

# 在回應頁面中找出所有照片連結
soup = BeautifulSoup(html.text, "html.parser")

# 以標題建立目錄儲存圖片
download_image_dir = title + "/"
if not os.path.exists(download_image_dir):
    os.mkdir(download_image_dir)

n = 0
for i in range(200):
    payload = {
        "type": "album",
        "rows": str(i * 20),
        "need_rows": "20",
        "cid": "5791",
        "album_id": "30668",
    }
    html = requests.post(url, data=payload)
    soup = BeautifulSoup(html.text, "html.parser")
    # 處理所有 <img> 標籤
    photos = soup.select(".photo_img")  # 尋找class是photo_img
    for photo in photos:
        # 讀取 src 屬性內容
        src = photo["src"]
        # 讀取 .jpg 檔
        if src != None and (".jpg" in src):
            # 設定圖檔完整路徑
            full_path = src
            filename = full_path.split("/")[-1]  # 取得圖檔名
            print(full_path)
            # 儲存圖片
            try:
                image = urlopen(full_path)
                with open(os.path.join(download_image_dir, filename), "wb") as f:
                    f.write(image.read())
                n += 1
                if n >= 1000:  # 最多下載 1000 張
                    break  # 離開內部 for 迴圈
            except:
                print("{} 無法讀取!".format(filename))
    if n >= 1000:  # 最多下載 1000 張
        break  # 離開外部 for 迴圈

print("共下載", n, "張圖片")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# compare1.py

# 1111data.py

df = []
baseurl = (
    "https://www.1111.com.tw/job-bank/job-index.asp?si=1&ks=電腦&ss=s&ps=100&page="  # 電腦
)

# 取得總頁數
html = requests.get(baseurl + "1")
soup = BeautifulSoup(html.text, "lxml")
tem = soup.find("span", class_="Nexup").text
page = int(tem.replace("1 / ", ""))
if page > 15:  # 最多取15頁資料
    page = 15
# 逐頁讀取資料
for i in range(page):
    url = baseurl + str(i + 1)
    html = requests.get(url)
    soup = BeautifulSoup(html.text, "lxml")
    job = soup.select(".jbInfoin")  # 取class=jbInfoin內容  # 尋找class是jbInfoin
    for j in range(len(job)):
        work = job[j].h3.a.text  # 職務名稱
        work = work.replace("【誠徵】", "").replace("【急徵】", "").replace("誠徵", "")
        site = "https:" + job[j].h3.a.get("href")  # 工作網址
        company = job[j].h4.a.text  # 公司名稱
        companysort = job[j].find("div", class_="csort").a.text  # 公司類別
        area = job[j].find("span", class_="location").a.text  # 工作地點
        tem = job[j].find("div", class_="needs").text
        temlist = tem.split("|")
        salary = temlist[0]  # 薪資
        experiment = temlist[1]  # 工作經驗
        school = temlist[2]  # 學歷
        tem = job[j].find("div", class_="jbInfoTxt")
        temlist = tem.find_all("p")
        content = ""  # 工作內容
        for k in range(len(temlist)):
            content = content + temlist[k].text

        dfmono = pd.DataFrame(
            [
                {
                    "職務名稱": work,
                    "工作網址": site,
                    "公司名稱": company,
                    "公司類別": companysort,
                    "工作地點": area,
                    "薪資": salary,
                    "工作經驗": experiment,
                    "學歷": school,
                    "工作內容": content,
                }
            ],
        )
        df.append(dfmono)
    print("處理第 " + str(i + 1) + " 頁完畢！")
df = pd.concat(df, ignore_index=True)
df.to_excel("tmp_1111data1.xlsx", index=0)  # 存為excel檔

print("------------------------------------------------------------")  # 60個

# compare2.py

# 1111data.py

df = []
baseurl = (
    "https://www.1111.com.tw/job-bank/job-index.asp?si=1&ks=電腦&ss=s&ps=100&page="  # 電腦
)

# 取得總頁數
html = requests.get(baseurl + "1")
soup = BeautifulSoup(html.text, "lxml")
tem = soup.find("select", class_="custom-select").text
page = int(tem.replace("1 / ", ""))
if page > 15:  # 最多取15頁資料
    page = 15
# 逐頁讀取資料
for i in range(page):
    url = baseurl + str(i + 1)
    html = requests.get(url)
    soup = BeautifulSoup(html.text, "lxml")
    job = soup.select(".it-md")  # 取class=jbInfoin內容  # 尋找class是it-md
    for j in range(len(job)):
        work = job[j].find("div", class_="position0").a.text  # 職務名稱
        work = work.replace("【誠徵】", "").replace("【急徵】", "").replace("誠徵", "")
        site = "https://www.1111.com.tw" + job[j].find("div", class_="position0").a.get(
            "href"
        )  # 工作網址
        company = job[j].find("div", class_="d-none d-md-flex jb-organ").a.text  # 公司名稱
        companysort = (
            job[j].find("span", class_="d-none d-md-block").text.replace("｜", "")
        )  # 公司類別
        tem = job[j].find("div", class_="text-truncate needs").select("span")
        area = tem[0].text  # 工作地點
        salary = tem[1].text  # 薪資
        experiment = tem[2].text  # 工作經驗
        school = tem[3].text  # 學歷
        tem = job[j].find("div", class_="col-12 jbInfoTxt UnExtension").select("p")
        content = ""  # 工作內容
        for k in range(len(tem)):
            content = content + tem[k].text

        dfmono = pd.DataFrame(
            [
                {
                    "職務名稱": work,
                    "工作網址": site,
                    "公司名稱": company,
                    "公司類別": companysort,
                    "工作地點": area,
                    "薪資": salary,
                    "工作經驗": experiment,
                    "學歷": school,
                    "工作內容": content,
                }
            ],
        )
        df.append(dfmono)
    print("處理第 " + str(i + 1) + " 頁完畢！")
df = pd.concat(df, ignore_index=True)
df.to_excel("tmp_1111data2.xlsx", index=0)  # 存為excel檔

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" wait long
print("requests 1")

html_data = requests.get("https://tw.yahoo.com/")
print(html_data.text)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

base_url = "https://zipcloud.ibsnet.co.jp/api/search"

query_parameter = "?zipcode="

zipcode = "1600021"

request_url = base_url + query_parameter + zipcode

request_url

requests.get(request_url).json()


# 有這樣的 API 啊，網址是：https://zipcloud.ibsnet.co.jp/doc/api，請幫我寫出來

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 郵遞區號
zipcode = "1000001"

# API 端點
api_endpoint = f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}"

# 進行查詢
html_data = requests.get(api_endpoint)

# 檢查回應狀態
if html_data.status_code == 200:
    # 解析回應內容
    data = html_data.json()

    # 驗證 API 回應狀態
    if data["status"] == 200:
        # 取出第一筆地址資訊
        address_info = data["results"][0]

        # 印出完整郵遞區域
        print(f"{address_info['address1']} {address_info['address2']} {address_info['address3']}")
    else:
        print("API 回應錯誤，訊息：", data["message"])
else:
    print("API 查詢失敗，狀態碼：", html_data.status_code)


"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" fail
# 郵遞區號
zipcode = "100-0001"

# API 端點
api_endpoint = "http://your_api_endpoint"

# 你的 API 金鑰
api_key = "your_api_key"

# 設定查詢參數
params = {
    "apikey": api_key,
    "zipcode": zipcode,
}

# 進行查詢
html_data = requests.get(api_endpoint, params=params)

# 檢查回應狀態
if html_data.status_code == 200:
    # 解析回應內容
    data = html_data.json()

    # 印出郵遞區域
    print(data["area"])
else:
    print("API 查詢失敗，狀態碼：", html_data.status_code)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
api_url = "https://collectionapi.metmuseum.org/public/collection/v1/objects"
html_data = requests.get(api_url)
response_dict = html_data.json()

response_dict.keys()
response_dict["total"]

get_object_url = (
    "https://collectionapi.metmuseum.org/public/collection/v1/objects/435864"
)

object_response = requests.get(get_object_url)

object_response.json()["objectURL"]

object_response.json()["title"]

object_response.json()["primaryImageSmall"]
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
tags = soup("a")  # 找全部的超連結<a>
print(len(tags))
print(tags)
tag = tags[1]
print("標籤名稱 :", tag.name)
print("標籤內容 :", tag)
print("標籤內容 :", tag.text)
print("標籤內容 :", tag.string)
print("標籤內容 :", tag.b.string)
print("URL網址 :", tag.get("href", None))
print("target屬性 :", tag["target"])

print("------------------------------")  # 30個

# 用find找

print("找下一個標題<h1>")
h1 = soup.find("h1")
print(soup.find("h1"))
print(soup.find("h1").text)

print("找下一個超連結<a>")
print(soup.a)  # 把第一個 <a></a> 抓出來

print("找全部的超連結<a>")
print(soup.find_all("a"))  # 把全部的 <a></a> 抓出來

print("找下一個段落<p>")
print(soup.p)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("找全部的超連結<a>")
all_links = soup.find_all("a")  # 取得 全部 <a></a>
# print(all_links)
for link in all_links:
    href = link.get("href")
    # print(href)
    if href != None and href.startswith("https://"):
        print("取得資料")
        print(href)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("找全部的超連結<a>")
all_links = soup.find_all("a")  # 取得 全部 <a></a>
# print(all_links)
for link in all_links:
    print("aa :", link)
    href = link.get("href")
    # print(href)
    # print("aaaaa")
    if href != None:
        print("bb :", link["href"])
        if ".jpg" in link["href"]:
            print("cc :", link["href"])
            target = link["href"]
            photos.append(target)
            # for item in re.findall(regex, target):
            # photos.append(item)


# 抓圖部分

photos = list()

print(photos)

for link in photos:
    item = urllib.parse.urlparse(link)
    q = urllib.parse.parse_qs(item.query)
    target = urllib.parse.urlparse(q["u"][0])
    filename = os.path.basename(target.path)
    urllib.request.urlretrieve(link, os.path.join("images", filename))
    print("Storing " + filename)
    time.sleep(3)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 片段html

string_html_data = "<p>Hello World!</p>"
soup = BeautifulSoup(string_html_data, "lxml")

soup = BeautifulSoup("<b class='score'>Joe</b>", "lxml")

# 用.取
tag = soup.b
tag.name = "p"
tag["class"] = "question"
tag["id"] = "name"
print(tag)
del tag["class"]
print(tag)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

soup = BeautifulSoup("<b class='score'>Joe</b>", "lxml")

# 用.取
tag = soup.b
tag.string = "Mary"
print(tag)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Tag物件
# NavigableString物件
# navigable 可航行的；可操縱的，可駕駛的

string_html_data = "<div id='msg' class='body strikeout'>Hello World!</div>"
soup = BeautifulSoup(string_html_data, "lxml")

# 用.取
tag = soup.div
print(type(tag))
print(tag)
print(tag.string)  # 標籤內容
print(type(tag.string))  # NavigableString型態

print("------------------------------")  # 30個

# BeautifulSoup物件
string_html_data = "<div id='msg'>Hello World!</div>"
soup = BeautifulSoup(string_html_data, "lxml")

# 用.取
tag = soup.div
print(soup.name)
print(type(soup))  # BeautifulSoup型態

print("------------------------------")  # 30個

# Comment物件
string_html_data = "<p><!-- 註解文字 --></p>"
soup = BeautifulSoup(string_html_data, "lxml")

# 用.取
comment = soup.p.string
print(comment)
print(type(comment))  # Comment型態

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

soup = BeautifulSoup("<b></b>", "lxml")

# 用.取
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
print("------------------------------------------------------------")  # 60個

soup = BeautifulSoup("<p><b>One</b></p>", "lxml")

# 用.取
tag = soup.b
new_tag = soup.new_tag("i")
new_tag.string = "Two"
tag.insert_before(new_tag)

print("找下一個段落<p>")
print(soup.p)

new_string = soup.new_string("Three")
tag.insert_after(new_string)

print("找下一個段落<p>")
print(soup.p)

tag.clear()

print("找下一個段落<p>")
print(soup.p)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

soup = BeautifulSoup("<p><b>One</b></p>", "lxml")

# 用.取
tag = soup.b
new_tag = soup.new_tag("i")
new_tag.string = "Two"
tag.replace_with(new_tag)

print("找下一個段落<p>")
print(soup.p)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# useful
def get_text(tag):
    if tag:
        return tag.text.strip()  # strip()用來刪除文字前面和後面多餘的空白
    else:
        return "N/A"


url = "https://movies.yahoo.com.tw/movie_intheaters.html"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    "AppleWebKit/537.36 (KHTML, like Gecko)"
    "Chrome/63.0.3239.132 Safari/537.36"
}

url = "https://movies.yahoo.com.tw/movie_intheaters.html/?page={0}"
for page in range(1, 11):
    url = url.format(page)
    print("抓取: 第" + str(page) + "頁 網路資料中...")

url = "https://movies.yahoo.com.tw/movie_intheaters.html/?page=1"


# 固定換法
html_data = requests.get(url)
soup = BeautifulSoup(html_data.text, "lxml")  # 傳回soup物件可解析網頁
# 換成
soup = get_soup_from_url(url)

"""
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
}
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("抓取一個網頁的所有連結網址")

# html使用<a>標籤來製作連結
# 抓取網頁所有的 <a href="XXXXXXXXXXXXX">YYYYYYYYYY</a> 之XXXXXXXXXXXXX部分 即網頁連結

url = "https://hispark.hccg.gov.tw/"  # 新竹市路邊停車收費網
html_data = requests.get(url)

soup = BeautifulSoup(html_data.text, "lxml")

print("------------------------------")  # 30個

print("找所有連結a")
tags = soup("a")
print("共找到", len(tags), "個連結")
for tag in tags:
    print(tag.get("href", None))

print("看第12個連結")
tag = tags[12]
print("URL網址: ", tag.get("href", None))
print("標籤內容: ", tag.text)
print("target屬性: ", tag["target"])

print("------------------------------")  # 30個

# html使用<img>來顯示圖片
# <img src="https://hispark.hccg.gov.tw/uploadfile/images/relatedlink/relatedlink_2.jpg" width="170" height="67" border="0" />

print("抓取一個網頁的所有圖片連結網址")
print("找所有圖片img")
tags = soup("img")
print("共找到", len(tags), "個圖片")
for tag in tags:
    print(tag.get("src", None))

print("看第0個圖片")
tag = tags[0]
print("圖片網址: ", tag.get("src", None))
print("alt屬性: ", tag["alt"])
print("屬性: ", tag.attrs)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/Example.html")
print(driver.title)

soup = BeautifulSoup(driver.page_source, "lxml")
tag_ol = soup.find("ol", {"id": "list"})
tags_li = tag_ol.find_all("li", class_="line")
for tag in tags_li:
    print(tag.text)
driver.quit()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/Example.html")
tag_ol = driver.find_element_by_xpath('//*[@id="list"]')
print(tag_ol.tag_name)
tags_li = tag_ol.find_elements_by_xpath("//li")
for tag in tags_li:
    print(tag.text, tag.get_attribute("class"))
driver.quit()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/Example.html")
tag_ol = driver.find_element_by_xpath("/html/body/ol")
print(tag_ol.tag_name)
tags_li = tag_ol.find_elements_by_xpath("//li")
for tag in tags_li:
    print(tag.text, tag.get_attribute("class"))
driver.quit()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/Example.html")
tag_ol = driver.find_element_by_xpath('//*[@id="list"]')
print(tag_ol.tag_name)
print(tag_ol.get_attribute("innerHTML"))

soup = BeautifulSoup(tag_ol.get_attribute("innerHTML"), "lxml")
tags_li = soup.find_all("li", class_="line")
for tag in tags_li:
    print(tag.text)
driver.quit()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from selenium import webdriver

email_address = "<電子郵件地址>"
password = "<密碼>"

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
url = "https://www.facebook.com/"
driver.get(url)

email = driver.find_element_by_css_selector("#email")
email.send_keys(email_address)

time.sleep(0.5)

passwd = driver.find_element_by_css_selector("#pass")
passwd.send_keys(password)

time.sleep(0.5)

button = driver.find_element_by_css_selector("#loginbutton")
button.click()

time.sleep(5)

soup = BeautifulSoup(driver.page_source, "lxml")
tag_title = soup.find("title")
print(tag_title.text)
driver.quit()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("使用UserAgent")

print("使用 fake user agent")
from fake_useragent import UserAgent

ua = UserAgent()

print(ua.ie)
print(ua.google)
print(ua.firefox)
print(ua.safari)
print(ua.random)

print("------------------------------")  # 30個

# 不使用 UserAgent 連接 momo 購物網

url = "https://www.momoshop.com.tw/main/Main.jsp"
html_data = requests.get(url)
print(html_data.status_code)
print(html_data.text)

print("---------------")  # 15個

# 使用 UserAgent 連接 momo 購物網

from fake_useragent import UserAgent

ua = UserAgent()
headers = {"user-agent": ua.random}

url = "https://www.momoshop.com.tw/main/Main.jsp"
html_data = requests.get(url, headers=headers)
print(html_data.status_code)
print(html_data.text)

print("------------------------------")  # 30個

from fake_useragent import UserAgent

ua = UserAgent()


def proxyGenerator():
    headers = {"user-agent": ua.random}
    res = requests.get("https://free-proxy-list.net/", headers=headers)
    soup = BeautifulSoup(res.text, "lxml")
    proxies_table = soup.find(id="proxylisttable")
    proxies = []
    for row in proxies_table.tbody.find_all("tr"):
        proxies.append(
            {
                "http": "http://"
                + row.find_all("td")[0].string
                + ":"
                + row.find_all("td")[1].string,
                "https": "https://"
                + row.find_all("td")[0].string
                + ":"
                + row.find_all("td")[1].string,
            }
        )
    return random.choice(proxies)


for n in range(5):
    proxy = proxyGenerator()
    print(proxy)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 58")
url = "https://tw.stock.yahoo.com/quote/2330"  # 台積電 Yahoo 股市網址
html_data = requests.get(url)  # 取得網頁內容

soup = BeautifulSoup(html_data.text, "html.parser")  # 轉換內容

print("找下一個標題<h1>")
title = soup.find("h1")  # 找到 h1 的內容

a = soup.select(".Fz(32px)")[0]  # 找到第一個 class 為 Fz(32px) 的內容  # 尋找class是Fz(32px)
b = soup.select(".Fz(20px)")[0]  # 找到第一個 class 為 Fz(20px) 的內容  # 尋找class是Fz(20px)
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
print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 59")

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
    html_data = requests.get(url)
    soup = BeautifulSoup(html_data.text, "html.parser")
    print("找下一個標題<h1>")
    title = soup.find("h1")
    a = soup.select(".Fz(32px)")[0]  # 尋找class是Fz(32px)
    b = soup.select(".Fz(20px)")[0]  # 尋找class是Fz(20px)
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
print("------------------------------------------------------------")  # 60個

url = "https://tw.stock.yahoo.com/s/list.php?\
c=%A8%E4%A5%A6%B9q%A4l&rr=0.84235400%201556957344"

# 取得網頁原始程式碼
res = requests.get(url).text

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

print("BeautifulSoup 測試 44")
# 讀取網頁中的表格

url = "https://tw.stock.yahoo.com/s/list.php?\
c=%A8%E4%A5%A6%B9q%A4l&rr=0.84235400%201556957344"

# 取得網頁原始程式碼
res = requests.get(url).text

# 以html.parser解析程式解析程式碼
soup = BeautifulSoup(res, "html.parser")

# 以<tr>並配合屬性取得表格中每列內容

print("找全部的xx<tr> + 條件")
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
        print("---------------")  # 15個

print("------------------------------------------------------------")  # 60個

# foreign.py

url = "https://tw.stock.yahoo.com/d/i/fgbuy_tse.html"

res = requests.get(url).text
print(res)

soup = BeautifulSoup(res, "html.parser")

# 以<tr>並配合屬性取得表格中每列內容
rows = soup.find_all("tr", {"bgcolor": "#FFFFFF"})

# 印出要查詢資料各欄位名稱
print("名 次 股票代號/名稱  成交價  漲　跌  買超張數  外資持股張數  外資持股比率")

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
print("------------------------------------------------------------")  # 60個

soup = BeautifulSoup(html_data.text.encode("utf-8"), "html.parser")

from concurrent.futures import ThreadPoolExecutor


def thread1(my_list):  # 編輯下載函式
    print(my_list)  # 印出網址
    for _ in ragne(5):
        print("1")
        time.sleep(0.5)
    print("a")


my_list = [1, 2, 3, 4, 5]
executor = ThreadPoolExecutor()  # 建立非同步的多執行緒的啟動器
with ThreadPoolExecutor() as executor:
    executor.map(thread1, my_list)  # 同時下載圖片

# url = "https://data.kcg.gov.tw/dataset/6f29f6f4-2549-4473-aa90-bf60d10895dc/resource/30dfc2cf-17b5-4a40-8bb7-c511ea166bd3/download/lightrailtraffic.json"

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
