"""
Python自學聖經(第二版) 01~22

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




print("------------------------------------------------------------")  # 60個



# 保留 bs4 本地讀取 html

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




print("------------------------------------------------------------")  # 60個

# 自訂表頭

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






print("------------------------------------------------------------")  # 60個
# webdriver
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



print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

a = np.genfromtxt("scores.csv", delimiter=",", skip_header=1)
print(a.shape)

print("------------------------------------------------------------")  # 60個

a = np.arange(1, 10).reshape(3, 3)
print("陣列的內容：\n", a)
print("1.最小值與最大值：\n", np.min(a), np.max(a))
print("2.每一直行最小值與最大值：\n", np.min(a, axis=0), np.max(a, axis=0))
print("3.每一橫列最小值與最大值：\n", np.min(a, axis=1), np.max(a, axis=1))
print("4.加總、乘積及平均值：\n", np.sum(a), np.prod(a), np.mean(a))
print("5.每一直行加總、乘積與平均值：\n", np.sum(a, axis=0), np.prod(a, axis=0), np.mean(a, axis=0))
print("6.每一橫列加總、乘積與平均值：\n", np.sum(a, axis=1), np.prod(a, axis=1), np.mean(a, axis=1))

print("------------------------------------------------------------")  # 60個

na = np.genfromtxt("scores.csv", delimiter=",", skip_header=1)
print("國文最高分數：", na[:, 1].max())
print("英文最低分數：", na[:, 2].min())
print("數學平均分數：", na[:, 3].mean())
total1 = na[:, 1] + na[:, 2] + na[:, 3]
print(total1)
print("全班最高總分：", total1.max())

total2 = na[:, 1:4].sum(axis=1)
print(total2)
print("全班最高總分：", total2.max())

print("------------------------------------------------------------")  # 60個

a = np.random.randint(100, size=50)
print("陣列的內容：", a)
print("1.標準差：", np.std(a))
print("2.變異數：", np.var(a))
print("3.中位數：", np.median(a))
print("4.百分比值：", np.percentile(a, 80))
print("5.最大最小差值：", np.ptp(a))

print("------------------------------------------------------------")  # 60個

a = np.random.choice(50, size=10, replace=False)
print("排序前的陣列：", a)
print("排序後的陣列：", np.sort(a))
print("排序後的索引：", np.argsort(a))
# 用索引到陣列取值
for i in np.argsort(a):
    print(a[i], end=",")

print("------------------------------------------------------------")  # 60個

a = np.random.randint(0, 10, (3, 5))
print("原陣列內容：")
print(a)
print("將每一直行進行排序：")
print(np.sort(a, axis=0))
print("將每一橫列進行排序：")
print(np.sort(a, axis=1))

print("------------------------------------------------------------")  # 60個

listdata = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
na = np.array(listdata)
print(na)
print("維度", na.ndim)
print("形狀", na.shape)
print("數量", na.size)

print("------------------------------------------------------------")  # 60個

# 同一df畫出3圖
df = pd.DataFrame(
    [[250, 320, 300, 312, 280], [280, 300, 280, 290, 310], [220, 280, 250, 305, 250]],
    index=["北部", "中部", "南部"],
    columns=[2015, 2016, 2017, 2018, 2019],
)
g1 = df.plot(kind="bar", title="長條圖", figsize=[10, 5])
g2 = df.plot(kind="barh", title="橫條圖", figsize=[10, 5])
g3 = df.plot(kind="bar", stacked=True, title="堆疊圖", figsize=[10, 5])

show()

print("------------------------------------------------------------")  # 60個

# 同一df將三筆資料畫在一圖

df = pd.DataFrame(
    [[250, 320, 300, 312, 280], [280, 300, 280, 290, 310], [220, 280, 250, 305, 250]],
    index=["北部", "中部", "南部"],
    columns=[2015, 2016, 2017, 2018, 2019],
)
g1 = df.iloc[0].plot(
    kind="line",
    legend=True,
    xticks=range(2015, 2020),
    title="公司分區年度銷售表",
    figsize=[10, 5],
)
g1 = df.iloc[1].plot(kind="line", legend=True, xticks=range(2015, 2020))
g1 = df.iloc[2].plot(kind="line", legend=True, xticks=range(2015, 2020))

show()

print("------------------------------------------------------------")  # 60個

df = pd.DataFrame(
    [[250, 320, 300, 312, 280], [280, 300, 280, 290, 310], [220, 280, 250, 305, 250]],
    index=["北部", "中部", "南部"],
    columns=[2015, 2016, 2017, 2018, 2019],
)
df.plot(kind="pie", subplots=True, figsize=[16, 6])

show()

print("------------------------------------------------------------")  # 60個

url = "https://www.tiobe.com/tiobe-index/"
tables = pd.read_html(url, header=0, keep_default_na=False)
print(tables[0])

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

# ch14\to_cvs.py

scores = {
    "國文": {"王小明": 65, "李小美": 90, "陳大同": 81, "林小玉": 79},
    "英文": {"王小明": 92, "李小美": 72, "陳大同": 85, "林小玉": 53},
    "數學": {"王小明": 78, "李小美": 76, "陳大同": 91, "林小玉": 47},
    "自然": {"王小明": 83, "李小美": 93, "陳大同": 89, "林小玉": 94},
    "社會": {"王小明": 70, "李小美": 56, "陳大同": 94, "林小玉": 80},
}
df = pd.DataFrame(scores)
df.to_csv("tmp_scores3.csv", encoding="utf-8-sig")

print("------------------------------------------------------------")  # 60個

# ch15\create_data.py

def c_item(x):
    if x < 2:
        return "筆電"
    elif x < 7:
        return "冰箱"
    else:
        return "電視"


def s_item(x):
    if x < 5:
        return "張三安"
    elif x < 7:
        return "李四友"
    else:
        return "王五信"


df = pd.DataFrame(
    {
        "業務員": np.random.randint(0, 10, size=100),
        "商品": np.random.randint(0, 10, size=100),
        "數量": np.random.randint(30, 300, size=100),
        "價格": np.random.randint(100, 200, size=100),
    }
)
df["商品"] = df["商品"].map(c_item)
df["業務員"] = df["業務員"].map(s_item)
df["價格"] = df["價格"].map(lambda x: x * 100)

df.to_csv("tmp_sale.csv", index=False)

print("------------------------------------------------------------")  # 60個

# ch15\create_score.py

tem = []
for i in range(3):
    tem.append(i + 1)
df = pd.DataFrame(np.random.randint(40, 101, size=(3, 3)), columns=["英文", "社會", "公民"])
# df = pd.DataFrame(np.random.randint(40,101,size=(3,4)), columns=['國文','數學','自然','社會'])
df.insert(0, "座號", tem)
df.to_csv("tmp_score2_6.csv", index=False)

print("------------------------------------------------------------")  # 60個

# ch15\split_data.py

df1 = pd.read_csv("data/titanic.csv")

df2 = df1[["row.names", "pclass", "survived", "name", "age", "embarked"]]
df2.to_csv("tmp_titanic1.csv", index=False)

df3 = df1[["row.names", "home.dest", "room", "ticket", "boat", "sex"]]
df3.to_csv("tmp_titanic2.csv", index=False)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

def twodigit(n):  #將數值轉為二位數字串
    if(n < 10):
        retstr = '0' + str(n)
    else:
        retstr = str(n)
    return retstr

def convertDate(date):  #轉捔民國日期為西元:106/03/02->20170302
    str1 = str(date)
    yearstr = str1[:3]  #取出民國年
    realyear = str(int(yearstr) + 1911)  #轉為西元年
    realdate = realyear + str1[4:6] + str1[7:9]  #組合日期
    return realdate

import requests
import json, csv
import pandas as pd
import os
import time

pd.options.mode.chained_assignment = None  #取消顯示pandas資料重設警告

urlbase = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=2017'  #網址前半
urltail = '01&stockNo=2317&_=1521363562193'  #網址後半
filepath = 'stockyear2017.csv'

if not os.path.isfile(filepath):  #如果檔案不存在就建立檔案
    for i in range(1, 13):  #取1到12數字
        url_twse = urlbase + twodigit(i) + urltail  #組合網址
        res = requests.get(url_twse)  #回傳為json資料
        jdata = json.loads(res.text)  #json解析
        
        outputfile = open(filepath, 'a', newline='', encoding='utf-8')  #開啟儲存檔案
        outputwriter = csv.writer(outputfile)  #以csv格式寫入檔案
        if i==1:  #若是1月就寫入欄位名稱
            outputwriter.writerow(jdata['fields'])
        for dataline in (jdata['data']):  #逐月寫入資料
            outputwriter.writerow(dataline)
        time.sleep(0.5)  #延遲0.5秒,否則有時會有錯誤
    outputfile.close()  #關閉檔案

pdstock = pd.read_csv(filepath, encoding='utf-8')  #以pandas讀取檔案
for i in range(len(pdstock['日期'])):  #轉換日期式為西元年格式
    pdstock['日期'][i] = convertDate(pdstock['日期'][i])
pdstock['日期'] = pd.to_datetime(pdstock['日期'])  #轉換日期欄位為日期格式

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


""" 統一發票


# ch22\tree1.py

import requests

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

content = requests.get("http://invoice.etax.nat.gov.tw/invoice.xml")
tree = ET.fromstring(content.text)

print("根目錄標籤：" + tree.tag)
print("根目錄屬性：" + str(tree.attrib))
print("根目錄值：" + str(tree.text))

print("------------------------------------------------------------")  # 60個

# ch22\tree2.py

import requests

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

content = requests.get("http://invoice.etax.nat.gov.tw/invoice.xml")
tree = ET.fromstring(content.text)

item = tree[0].find("item")
print("find 方法：" + item[0].text)

items = tree[0].findall("item")
print("findall 方法：" + items[0][0].text)

items = list(tree.iter(tag="item"))
print("iter 方法：" + items[0][0].text)



print("------------------------------------------------------------")  # 60個

import requests

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET



        try:
            content = requests.get("http://invoice.etax.nat.gov.tw/invoice.xml")
            tree = ET.fromstring(content.text)
            items = list(tree.iter(tag="item"))  # 取得item標籤內容
            ptext = items[0][2].text  # 中獎號碼
            ptext = ptext.replace("<p>", "").replace("</p>", "")
            temlist = ptext.split("：")
            prizelist = []  # 特別獎或特獎後三碼
            prizelist.append(temlist[1][5:8])
            prizelist.append(temlist[2][5:8])
            for i in range(3):  # 頭獎後三碼
                prizelist.append(temlist[3][9 * i + 5 : 9 * i + 8])
            sixlist = temlist[4].split("、")  # 增開六獎
            for i in range(len(sixlist)):
                prizelist.append(sixlist[i])
            if mtext in prizelist:
                message = "符合某獎項後三碼，請自行核對發票前五碼！\n\n"
                message += monoNum(0)
            else:
                message = "很可惜，未中獎。請輸入下一張發票最後三碼。"
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))
        except:
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text="讀取發票號碼發生錯誤！")
            )



def monoNum(n):
    content = requests.get("http://invoice.etax.nat.gov.tw/invoice.xml")
    tree = ET.fromstring(content.text)  # 解析XML
    items = list(tree.iter(tag="item"))  # 取得item標籤內容
    title = items[n][0].text  # 期別
    ptext = items[n][2].text  # 中獎號碼
    ptext = ptext.replace("<p>", "").replace("</p>", "\n")
    return title + "月\n" + ptext[:-1]  # ptext[:-1]為移除最後一個\n

"""

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

