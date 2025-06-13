"""
Python自學聖經(第二版)

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
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
'''
print("姓名   座號  國文  數學  英文")
print("%3s  %2d   %3d   %3d  %3d" % ("林大明", 1, 100, 87, 79))
print("%3s  %2d   %3d   %3d  %3d" % ("陳阿中", 2, 74, 88, 100))
print("%3s  %2d   %3d   %3d  %3d" % ("張小英", 11, 82, 65, 8))

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

# print("本班總成績：%d 分，平均成績：%5.2f 分" % (total, average))

print("------------------------------------------------------------")  # 60個

for i in range(1, 10):
    for j in range(1, 10):
        product = i * j
        print("%d*%d=%-2d   " % (i, j, product), end="")
    print()

print("------------------------------------------------------------")  # 60個

# print("本班總成績：%d 分，平均成績：%5.2f 分" % (total, average))

print("------------------------------------------------------------")  # 60個


listname = ["林大明", "陳阿中", "張小英"]
listchinese = [100, 74, 82]
listmath = [87, 88, 65]
listenglish = [79, 100, 8]
print("姓名     座號  國文  數學  英文")
for i in range(0, 3):
    print(
        listname[i].ljust(5),
        str(i + 1).rjust(3),
        str(listchinese[i]).rjust(5),
        str(listmath[i]).rjust(5),
        str(listenglish[i]).rjust(5),
    )

print("------------------------------------------------------------")  # 60個

import time as t

week = [" 一", " 二", " 三", " 四", " 五", " 六", " 日"]
dst = [" 無日光節約時間", " 有日光節約時間"]
time1 = t.localtime()
show = " 現在時刻：中華民國 " + str(int(time1.tm_year) - 1911) + " 年 "
show += str(time1.tm_mon) + " 月 " + str(time1.tm_mday) + " 日 "
show += str(time1.tm_hour) + " 點 " + str(time1.tm_min) + " 分 "
show += str(time1.tm_sec) + " 秒 星期" + week[time1.tm_wday] + "\n"
show += " 今天是今年的第 " + str(time1.tm_yday) + " 天，此地" + dst[time1.tm_isdst]
print(show)

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

# ch05\spenttime.py

import time

start = time.time()  # 開始執行時間
print("開始時間：{}".format(start))
for i in range(100):
    time.sleep(0.001)
end = time.time()  # 結束執行時間
print("結束時間：{}".format(end))
print("使用時間：%7.3f 秒" % (end - start))

print("------------------------------------------------------------")  # 60個

import msvcrt


def pwd_input():
    chars = []
    while True:
        try:
            newChar = msvcrt.getch().decode(encoding="utf-8")
        except:
            return input("請在cmd命令行下執行，否則密碼輸入將無法隱藏:")
        if newChar in "\r\n":  # 如果是換行，结束輸入
            break
        elif newChar == "\b":  # 如果是退格，删除密碼末尾一位並且删除一個星號
            if chars:
                del chars[-1]
                msvcrt.putch("\b".encode(encoding="utf-8"))  # 游標退回一格
                msvcrt.putch(" ".encode(encoding="utf-8"))  # 输出一個空格覆蓋原來的星號
                msvcrt.putch("\b".encode(encoding="utf-8"))  # 游標退回一格準備接受新的输入
        else:
            chars.append(newChar)
            msvcrt.putch("*".encode(encoding="utf-8"))  # 顯示 * 號
    return "".join(chars)

# pwd_input()


print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

# ch08\bracket.py

import re

pat = r"[0-9+]+"
s = "Amy was 18 year old,she likes Python and C++."
m = re.findall(pat, s)
print(m)  # ['18', '++']

print("------------------------------------------------------------")  # 60個

# ch08\compile.py

import re

reobj = re.compile(r"[a-z]+")
m = reobj.findall("3tem12po")
print(m)  # ['tem', 'po']

print("------------------------------------------------------------")  # 60個

# ch08\dotall.py

import re

pat = r".*"
s = "Do your best,\nGo Go Go!"
m = re.search(pat, s)
print(m.group())  # Do your best,
m2 = re.search(r".*", s, re.DOTALL)
print(m2.group())  # Do your best,\nGo Go Go!

print("------------------------------------------------------------")  # 60個

# ch08\findall.py

import re

pat = re.compile("[a-z]+")
m = pat.findall("tem12po")
print(m)  # ['tem', 'po']

print("------------------------------------------------------------")  # 60個

# ch08\ignore.py

import re

pat = r"PYTHON|ANDROID"
s = "I like Python and Android!"
m = re.findall(pat, s, re.I)
print(m)  # ['Python', 'Android']

print("------------------------------------------------------------")  # 60個

# ch08\match.py

import re

pat = re.compile(r"[a-z]+")

m = pat.match("tem12po")
print(m)  # <re.Match object; span=(0, 3), match='tem'>
if not m == None:
    print(m.group())  # tem
    print(m.start())  # 0
    print(m.end())  # 3
    print(m.span())  # (0,3)

print("------------------------------------------------------------")  # 60個

# ch08\not1.py

import re

pat = r"[^a-z. ]+"
s = "John was 18 year old."
m = re.findall(pat, s)
print(m)  # ['J', '18']

print("------------------------------------------------------------")  # 60個

# ch08\not2.py

import re

pat = r"^\d+"
s = "2020 is coming soon"
m = re.findall(pat, s)
print(m)  # ['2020']
m2 = re.findall(r"\w+$", s)
print(m2)  # ['soon']

print("------------------------------------------------------------")  # 60個

# ch08\phone_check.py


def isTaiwanPhone(str):
    if len(str) != 11:  # 如果長度不是11
        return False  # 傳回非手機號碼格式
    # 檢查11個字元是否符合手機號碼格式
    for i in range(0, 11):
        if i == 4:
            if str[4] != "-":  # 如果第5個字元不是'-'字元
                return False  # 傳回非手機號碼格式
        else:  # 如果前4個字或最後6個字出現非數字字元
            if str[i].isdecimal() == False:
                return False  # 傳回非手機號碼格式
    return True  # 傳回是正確手機號碼格式


print("0937-123456 是台灣手機號碼：", isTaiwanPhone("0937-123456"))
print("02-12345678 是台灣手機號碼：", isTaiwanPhone("02-12345678"))

print("------------------------------------------------------------")  # 60個

# ch08\phone1.py

import re

numStr = "tel:04-12345678"
pat = r"(\d{2})-(\d{8})"

phone = re.search(pat, numStr)
if not phone == None:
    print(phone.group())  # 04-12345678
    print(phone.group(0))  # 04-12345678
    print(phone.group(1))  # 04
    print(phone.group(2))  # 12345678

print("------------------------------------------------------------")  # 60個

# ch08\phone2.py

import re

numStr = "tel:(04)12345678"
pat = r"(\(\d{2}\))(\d{8})"

phone = re.search(pat, numStr)
if not phone == None:
    print(phone.group())  # (04)12345678
    print(phone.group(1))  # (04)
    print(phone.group(2))  # 12345678

print("------------------------------------------------------------")  # 60個

# ch08\phone3.py

import re

phoneList = ["(04)12345678", "(04)-12345678"]
pat = r"(\(\d{2}\))-?(\d{8})"

for phone in phoneList:
    phoneNum = re.search(pat, phone)
    if not phoneNum == None:
        print(phoneNum.group())

print("------------------------------------------------------------")  # 60個

# ch08\phone4.py

import re

phoneList = [
    "0412345678",
    "(04)12345678",
    "(04)-12345678",
    "(049)2987654",
    "0937-998877",
]
pat = r"\(\d{2,4}\)-?\d{6,8}|\d{9,10}|\d{4}-\d{6,8}"
for phone in phoneList:
    phoneNum = re.search(pat, phone)
    if not phoneNum == None:
        print(phoneNum.group())

print("------------------------------------------------------------")  # 60個

# ch08\plus.py

import re

pat = re.compile(r"[aeiou]+")
s = "John is my best friend."
m = re.findall(pat, s)
print(m)  # ['o', 'i', 'e', 'ie']

print("------------------------------------------------------------")  # 60個

# ch08\re_findall.py

import re

m = re.findall(r"[a-z]+", "tem12po")
print(m)  # ['tem', 'po']

print("------------------------------------------------------------")  # 60個

# ch08\re_match.py

import re

pat = r"[a-z]+"
m = re.match(pat, "tem12po")
print(m)  # <re.Match object; span=(0, 3), match='tem'>

print("------------------------------------------------------------")  # 60個

# ch08\re_search.py

import re

pat = "[a-z]+"
m = re.search(pat, "3tem12po")
print(m)  # <re.Match object; span=(1, 4), match='tem'>

print("------------------------------------------------------------")  # 60個

# ch08\re_verbose.py

import re

phoneList = [
    "0412345678",
    "(04)12345678",
    "(04)-12345678",
    "(049)2987654",
    "0937-998877",
]
pat = r"""
 \(\d{2,4}\)-?\d{6,8} #(04)12345678、(04)-12345678、(049)2987654 等電話格式
|\d{9,10}             #0412345678 等含 9~10 位數字
|\d{4}-\d{6,8}        #0937-998877 等手機格式
"""

for phone in phoneList:
    phoneNum = re.search(pat, phone, re.VERBOSE)
    if not phoneNum == None:
        print(phoneNum.group())

print("------------------------------------------------------------")  # 60個

# ch08\regex.py

html = """
<div class="content">
    E-Mail：<a href="mailto:mail@test.com.tw">mail</a><br>
    E-Mail2：<a href="mailto:mail2@test.com.tw">mail2</a><br>
    <ul class="price">定價：360元 </ul>
    <img src="http://test.com.tw/p1.jpg">
    <img src="http://test.com.tw/p2.jpg">
    <img src="http://test.com.tw/p3.png">
    電話：(04)-76543210、0937-123456
</div>
"""

import re

emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", html)
for email in emails:  # 顯示 email
    print(email)

price = re.findall(r"[\d]+元", html)[0].split("元")[0]  # 價格
print(price)  # 顯示定價金額

imglist = re.findall(r"[http://]+[a-zA-Z0-9-/.]+\.[jpgpng]+", html)
for img in imglist:  #
    print(img)  # 顯示圖片網址

phonelist = re.findall(r"\(?\d{2,4}\)?\-\d{6,8}", html)
for phone in phonelist:
    print(phone)  # 顯示電話號碼

print("------------------------------------------------------------")  # 60個

# ch08\search.py

import re

pat = re.compile("[a-z]+")

m = pat.search("3tem12po")
print(m)  # <re.Match object; span=(1, 4), match='tem'>
if not m == None:
    print(m.group())  # tem
    print(m.start())  # 1
    print(m.end())  # 4
    print(m.span())  # (1,4)

print("------------------------------------------------------------")  # 60個

# ch08\star.py

import re

pat = re.compile(r"[aeiou]*")
s = "John is my best friend."
m = re.findall(pat, s)
print(m)

print("------------------------------------------------------------")  # 60個

# ch08\sub1.py

import re

pat = r"\d+"
substr = "*"
s = "Password:1234,ID:5678"
result = re.sub(pat, substr, s)
print(result)  # Password:*,ID:*

print("------------------------------------------------------------")  # 60個

# ch08\sub2.py

import re


def multiply(m):
    v = int(m.group())
    return str(v * 2)


result = re.sub("\d+", multiply, "10 20 30 40 50", 3)
print(result)  # 20 40 60 40 50

print("------------------------------------------------------------")  # 60個

# ch08\wild.py

import re

pat = r".o"
s = "Do your best!"
m = re.findall(pat, s)
print(m)  # ['Do', 'yo']
m2 = re.findall(r".*o", s)
print(m2)  # ['Do yo']

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


'''

print("------------------------------------------------------------")  # 60個

# ch11\bs1.py

import requests
from bs4 import BeautifulSoup

url = "http://www.ehappy.tw/bsdemo1.htm"
html = requests.get(url)
html.encoding = "UTF-8"
sp = BeautifulSoup(html.text, "html.parser")

print(sp.title)
print(sp.title.text)
print(sp.h1)
print(sp.p)

print("------------------------------------------------------------")  # 60個

# ch11\bs2.py

from bs4 import BeautifulSoup

html = """
<html>
  <head><meta charset="UTF-8"><title>我是網頁標題</title></head>
  <body>
      <p id="p1">我是段落一</p>
      <p id="p2" class='red'>我是段落二</p>
  </body>
</html>
"""
sp = BeautifulSoup(html, "html.parser")
print(sp.find("p"))
print(sp.find_all("p"))
print(sp.find("p", {"id": "p2", "class": "red"}))
print(sp.find("p", id="p2", class_="red"))

print("------------------------------------------------------------")  # 60個

# ch11\bs3.py

from bs4 import BeautifulSoup

html = """
<html>
  <head><meta charset="UTF-8"><title>我是網頁標題</title></head>
  <body>
      <p id="p1">我是段落一</p>
      <p id="p2" class='red'>我是段落二</p>
  </body>
</html>
"""
sp = BeautifulSoup(html, "html.parser")
print(sp.select("title"))
print(sp.select("p"))
print(sp.select("#p1"))
print(sp.select(".red"))

print("------------------------------------------------------------")  # 60個

# ch11\bs4.py

from bs4 import BeautifulSoup

html = """
<html>
  <head><meta charset="UTF-8"><title>我是網頁標題</title></head>
  <body>
      <img src="http://www.ehappy.tw/python.png">
      <a href="http://www.e-happy.com.tw">超連結</a>
  </body>
</html>
"""
sp = BeautifulSoup(html, "html.parser")
print(sp.select("img")[0].get("src"))
print(sp.select("a")[0].get("href"))
print(sp.select("img")[0]["src"])
print(sp.select("a")[0]["href"])

print("------------------------------------------------------------")  # 60個

# ch11\bs5.py

html = """
<html><head><title>網頁標題</title></head>
<h1>文件標題</h1>
<div class="content">
    <div class="item1">
        <a href="http://example.com/one" class="red" id="link1">First</a>
        <a href="http://example.com/two" class="red" id="link2">Second</a>
    </div>
    <a href="http://example.com/three" class="blue" id="link3">
        <img src="http://example.com/three.jpg">Third
    </a>
</div>
"""

from bs4 import BeautifulSoup

sp = BeautifulSoup(html, "html.parser")

print(sp.title)  # <title>網頁標題</title>

print(sp.find("h1"))  # <h1>文件標題</h1>

print(sp.find_all("a"))
print(sp.find_all("a", {"class": "red"}))

data1 = sp.find("a", {"href": "http://example.com/one"})
print(data1.text)  # First

data2 = sp.select("#link1")
print(data2[0].text)  # First
print(data2[0].get("href"))  # http://example.com/one
print(data2[0]["href"])  # http://example.com/one

print(sp.find_all(["title", "h1"]))  # [<title>網頁標題</title>, <h1>文件標題</h1>]

print(sp.select("div img")[0]["src"])  # http://example.com/three.jpg


print("------------------------------------------------------------")  # 60個

# ch11\get.py

import requests

url = "http://www.ehappy.tw/demo.htm"
r = requests.get(url)
# 檢查HTTP回應碼是否為200(requests.code.ok)
if r.status_code == requests.codes.ok:
    print(r.text)

print("------------------------------------------------------------")  # 60個

# ch11\get_cookie.py

import requests

url = "https://www.ptt.cc/bbs/Gossiping/index.html"
# 設定cookies的值
cookies = {"over18": "1"}
r = requests.get(url, cookies=cookies)
print(r.text)

print("------------------------------------------------------------")  # 60個

# ch11\get_headers.py

import requests

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
r = requests.get(url, headers=headers)
print(r)

print("------------------------------------------------------------")  # 60個

# ch11\iplookup.py

import requests

# 設定查詢目前IP的api網址
url = "https://api.ipify.org"
r = requests.get(url)

print("我目前的IP是：", r.text)

print("------------------------------------------------------------")  # 60個

# ch11\loginFacebook.py

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

print("------------------------------------------------------------")  # 60個

# ch11\loginFacebook2.py

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

print("------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt

listx = [1, 2, 3, 4, 5]

listy1 = [15, 50, 80, 40, 70]
plt.axes([0.1, 0, 0.8, 0.8])
plt.ylim(0, 100)
plt.plot(listx, listy1, "r-s")

listy2 = [80, 20, 60, 50, 20]
plt.axes([1, 0, 0.8, 0.8])
plt.ylim(0, 100)
plt.plot(listx, listy2, "g--o")

plt.axes([0.1, 1, 0.8, 0.8])
plt.ylim(0, 100)
plt.plot(listx, listy1, "r-s")

plt.axes([1, 1, 0.8, 0.8])
plt.ylim(0, 100)
plt.plot(listx, listy2, "g--o")

plt.show()

# plt.rcParams['figure.figsize'] = [10, 10]
# plt.rcParams['figure.dpi'] = 72
# plt.rcParams.keys

print("------------------------------------------------------------")  # 60個

# ch13\subplot1.py

import matplotlib.pyplot as plt

plt.figure(figsize=[8, 8])
plt.subplot(211)
plt.title(label="Chart 1")
plt.plot([1, 2, 3], "r:o")

plt.subplot(212)
plt.title(label="Chart 2")
plt.plot([1, 2, 3], "g--o")

plt.show()

print("------------------------------------------------------------")  # 60個

# ch13\subplot2.py

import matplotlib.pyplot as plt

plt.figure(figsize=[8, 8])
plt.subplot(121)
plt.title(label="Chart 1")
plt.plot([1, 2, 3], "r:o")

plt.subplot(122)
plt.title(label="Chart 2")
plt.plot([1, 2, 3], "g--o")

plt.show()

print("------------------------------------------------------------")  # 60個

# ch13\subplot3.py

import matplotlib.pyplot as plt

plt.figure(figsize=[8, 8])
plt.subplot(221)
plt.title(label="Chart 1")
plt.plot([1, 2, 3], "r:o")

plt.subplot(222)
plt.title(label="Chart 2")
plt.plot([1, 2, 3], "g--o")

plt.subplot(223)
plt.title(label="Chart 3")
plt.plot([1, 2, 3], "b:o")

plt.subplot(224)
plt.title(label="Chart 4")
plt.plot([1, 2, 3], "y--o")

plt.show()

print("------------------------------------------------------------")  # 60個

# ch13\subplot4.py

import matplotlib.pyplot as plt

plt.figure(figsize=[8, 4])
plt.axes([0, 0, 0.4, 1])
plt.title(label="Chart 1")
plt.plot([1, 2, 3], "r:o")

plt.axes([0.5, 0, 0.4, 1])
plt.title(label="Chart 2")
plt.plot([1, 2, 3], "g--o")

plt.show()

print("------------------------------------------------------------")  # 60個

# ch13\subplot5.py

import matplotlib.pyplot as plt

plt.figure(figsize=[8, 4])
plt.axes([0, 0, 0.8, 1])
plt.title(label="Chart 1")
plt.plot([1, 2, 3], "r:o")

plt.axes([0.55, 0.1, 0.2, 0.2])
plt.title(label="Chart 2")
plt.plot([1, 2, 3], "g--o")

plt.show()

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
sys.exit()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
