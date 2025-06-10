import re
import csv
import json
import requests
from bs4 import BeautifulSoup

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

print("------------------------------------------------------------")  # 60個


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# get.py

url = "http://www.ehappy.tw/demo.htm"
html = requests.get(url)
# 檢查HTTP回應碼是否為200(requests.code.ok)
if html.status_code == requests.codes.ok:
    print(html.text)

print("------------------------------------------------------------")  # 60個

# get_headers.py

url = "https://irs.thsrc.com.tw/IMINT/"
# 自訂表頭
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
}
# 將自訂表頭加入 GET 請求中
html = requests.get(url, headers=headers)
print(html)

print("------------------------------------------------------------")  # 60個

# get_cookie.py

url = "https://www.ptt.cc/bbs/Gossiping/index.html"
# 設定cookies的值
cookies = {"over18": "1"}
r = requests.get(url, cookies=cookies)
print(r.text)

print("------------------------------------------------------------")  # 60個

# bs1.py

url = "http://ehappy.tw/bsdemo1.htm"
html = requests.get(url)
html.encoding = "UTF-8"
sp = BeautifulSoup(html.text, "lxml")

print(sp.title)
print(sp.title.text)
print(sp.h1)
print(sp.p)

print("------------------------------------------------------------")  # 60個

# bs2.py

html = """
<html>
  <head><meta charset="UTF-8"><title>我是網頁標題</title></head>
  <body>
      <p id="p1">我是段落一</p>
      <p id="p2" class='red'>我是段落二</p>
  </body>
</html>
"""
sp = BeautifulSoup(html, "lxml")
print(sp.find("p"))
print(sp.find_all("p"))
print(sp.find("p", {"id": "p2", "class": "red"}))
print(sp.find("p", id="p2", class_="red"))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# bs3.py

html = """
<html>
  <head><meta charset="UTF-8"><title>我是網頁標題</title></head>
  <body>
      <p id="p1">我是段落一</p>
      <p id="p2" class='red'>我是段落二</p>
  </body>
</html>
"""
sp = BeautifulSoup(html, "lxml")
print(sp.select("title"))
print(sp.select("p"))
print(sp.select("#p1"))
print(sp.select(".red"))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# bs4.py

html = """
<html>
  <head><meta charset="UTF-8"><title>我是網頁標題</title></head>
  <body>
      <img src="http://www.ehappy.tw/python.png">
      <a href="http://www.e-happy.com.tw">超連結</a>
  </body>
</html>
"""
sp = BeautifulSoup(html, "lxml")
print(sp.select("img")[0].get("src"))
print(sp.select("a")[0].get("href"))
print(sp.select("img")[0]["src"])
print(sp.select("a")[0]["href"])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# taiwanlottery.py

url = "https://www.taiwanlottery.com.tw/"
r = requests.get(url)
sp = BeautifulSoup(r.text, "lxml")
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

# re_match.py

m = re.match(r"[a-z]+", "abc123xyz")
print(m)
if m != None:
    print(m.group())  # abc
    print(m.start())  # 0
    print(m.end())  # 3
    print(m.span())  # (0, 3)

print("------------------------------------------------------------")  # 60個

# re_search.py

m = re.search(r"[a-z]+", "abc123xyz")
print(m)  # <re.Match object; span=(0, 3), match='abc'>
if m != None:
    print(m.group())  # abc
    print(m.start())  # 0
    print(m.end())  # 3
    print(m.span())  # (0,3)

print("------------------------------------------------------------")  # 60個

# re_findall.py

m = re.findall(r"[a-z]+", "abc123xyz")
print(m)  # ['abc', 'xyz']

print("------------------------------------------------------------")  # 60個

# re_sub.py

result = re.sub(r"\d+", "*", "Password:1234,ID:5678")
print(result)  # Password:*,ID:*

print("------------------------------------------------------------")  # 60個

# regex.py
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


# twhrtimetable.py
from selenium import webdriver

# 高鐵時刻表查詢網站
url = "http://www.thsrc.com.tw/tw/TimeTable/SearchResult"
ss = "台中站"  # 出發站
es = "台北站"  # 到達站
dd = "2020/03/26"  # 日期
dt = "09:00"  # 時間
# 建立瀏覽器物件開啟網站
driver = webdriver.Chrome()
driver.get(url)
# 輸入出發站
driver.find_element_by_id("StartStation").send_keys(ss)
# 輸入到達站
driver.find_element_by_id("EndStation").send_keys(es)
# 輸入日期
driver.find_element_by_id("DepartueSearchDate").click()
driver.find_element_by_id("DepartueSearchDate").send_keys(dd)
# 輸入時間
driver.find_element_by_id("DepartueSearchTime").click()
driver.find_element_by_id("DepartueSearchTime").send_keys(dt)
driver.find_element_by_id("SearchButton").click()  # 按查詢鈕

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# twhrtimetable.py
from selenium import webdriver

# 高鐵時刻表查詢網站
url = "http://www.thsrc.com.tw/tw/TimeTable/SearchResult"
ss = "台中站"  # 出發站
es = "台北站"  # 到達站

# 建立瀏覽器物件開啟網站
driver = webdriver.Chrome()
driver.get(url)
# 按我同意
driver.find_element_by_xpath("//button[@class='swal2-confirm swal2-styled']").click()
# 輸入出發站
driver.find_element_by_id("select_location01").send_keys(ss)
# #輸入到達站
driver.find_element_by_id("select_location02").send_keys(es)
# 輸入日期
driver.find_element_by_id("Departdate03").click()
driver.find_element_by_xpath(
    "//div[@id='tot-1']/div/div/ul/li/div/div/table/tbody/tr[2]/td[1]"
).click()
# #輸入時間
driver.find_element_by_id("outWardTime").click()
driver.find_element_by_xpath(
    "//div[@id='tot-1']/div[2]/div/ul/li[2]/div/div/table/tr[3]/td[3]/a/i"
).click()
driver.find_element_by_id("start-search").click()  # 按查詢鈕

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# iplookup.py

# 設定查詢目前IP的api網址
url = "https://api.ipify.org"
r = requests.get(url)

print("我目前的IP是：", r.text)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# loginFacebook.py

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

print("------------------------------------------------------------")  # 60個

# phone_check.py


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
print("------------------------------------------------------------")  # 60個

# timetable.py

from selenium import webdriver

# 高鐵時刻表查詢網站
url = "http://www.thsrc.com.tw/tw/TimeTable/SearchResult"
ss = "台中站"  # 出發站
es = "台北站"  # 到達站
dd = "2020/03/26"  # 日期
dt = "09:00"  # 時間
# 建立瀏覽器物件
driver = webdriver.Chrome()
## 最大化視窗後開啟facebook網站
# driver.maximize_window()
driver.get(url)
# 執行自動登入動作
driver.find_element_by_id("StartStation").send_keys(ss)  # 輸入郵件
driver.find_element_by_id("EndStation").send_keys(es)  # 輸入密碼密碼
driver.find_element_by_id("DepartueSearchDate").click()
driver.find_element_by_id("DepartueSearchDate").send_keys(dd)  # 輸入
driver.find_element_by_id("DepartueSearchTime").click()
driver.find_element_by_id("DepartueSearchTime").send_keys(dt)  # 輸入密碼
driver.find_element_by_id("SearchButton").click()  # 按登入鈕

#
# driver.find_element_by_id("StartStation").click()
# Select(driver.find_element_by_id("StartStation")).select_by_visible_text(u"台中站")
# driver.find_element_by_id("StartStation").click()
# driver.find_element_by_id("EndStation").click()
# Select(driver.find_element_by_id("EndStation")).select_by_visible_text(u"台北站")
# driver.find_element_by_id("EndStation").click()
# driver.find_element_by_id("DepartueSearchDate").click()
# driver.find_element_by_link_text("26").click()
# driver.find_element_by_id("DepartueSearchTime").click()
# Select(driver.find_element_by_id("DepartueSearchTime")).select_by_visible_text("09:00")
# driver.find_element_by_id("DepartueSearchTime").click()
# driver.find_element_by_id("SearchButton").click()

# url = 'http://www.thsrc.com.tw/tw/TimeTable/Search'
#
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)                         Chrome/73.0.3683.86 Safari/537.36'
# }
#
# form_data = {
#    'StartStationName':'南港站',
#    'EndStationName':'台南站',
#    'SearchType':'S',
#    'StartStation':'2f940836-cedc-41ef-8e28-c2336ac8fe68',
#    'EndStation':'9c5ac6ca-ec89-48f8-aab0-41b738cb1814',
#    'DepartueSearchDate':'2019/04/02',
#    'DepartueSearchTime':'09:00',
#    'DepartueTrainCode':'',
#    'DestinationSearchDate':'',
#    'DestinationSearchTime':'',
#    'DiscountType':''
# }
#
# res = requests.post(url, headers=headers, data=form_data)
#
# jsdata = res.json()
#
##print(jsdata['data'])
# jsdata

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# lineimage.py

url = "https://store.line.me/stickershop/product/8991459/zh-Hant"
url = "https://store.line.me/stickershop/product/10571593/zh-Hant"
html = requests.get(url)
soup = BeautifulSoup(html.text, "html.parser")

# 建立目錄儲存圖片
images_dir = "line_image/"
if not os.path.exists(images_dir):
    os.mkdir(images_dir)

# 下載貼圖
datas = soup.find_all("li", {"class": "mdCMN09Li FnStickerPreviewItem"})
for data in datas:
    # 將字串資料轉換為字典
    imginfo = json.loads(data.get("data-preview"))
    id = imginfo["id"]
    imgfile = requests.get(imginfo["staticUrl"])  # 載入圖片

    full_path = os.path.join(images_dir, id)  # 儲存的路徑和主檔名
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
images_dir = "line_image2/"
if not os.path.exists(images_dir):
    os.mkdir(images_dir)

# 下載貼圖
datas = soup.find_all("a", {"class": "FnRelatedStickerLink"})
for data in datas:
    imginfo = data.find("img")
    id = re.findall(r"[\d]+", data["href"])[0]
    imgfile = requests.get(imginfo["src"])  # 載入圖片

    full_path = os.path.join(images_dir, id)  # 儲存的路徑和主檔名
    # 儲存圖片
    with open(full_path + ".png", "wb") as f:
        f.write(imgfile.content)
    print(full_path + ".png")  # 顯示儲存的路徑和檔名

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "https://store.line.me/stickershop/product/8991459/zh-Hant"

html = requests.get(url)

sp = BeautifulSoup(html.text, "html.parser")
datas = sp.find_all("li", {"class": "mdCMN09Li FnStickerPreviewItem"})

# 建立目錄儲存圖片
images_dir = "line_image/"
if not os.path.exists(images_dir):
    os.mkdir(images_dir)

for data in datas:
    imginfo = json.loads(data.get("data-preview"))
    id = imginfo["id"]
    imgfile = requests.get(imginfo["staticUrl"])
    full_path = images_dir + id + ".png"

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
title = soup.find("h1", {"class": "album-title flex-1"}).text.strip()

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
images_dir = title + "/"
if not os.path.exists(images_dir):
    os.mkdir(images_dir)

# 處理所有 <img> 標籤
photos = soup.select(".photo_img")
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
            with open(os.path.join(images_dir, filename), "wb") as f:
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
title = soup.find("h1", {"class": "album-title flex-1"}).text.strip() + "_全部相片"

url = "https://running.biji.co/index.php?pop=ajax&func=album&fename=load_more_photos_in_listing_computer"

# 在回應頁面中找出所有照片連結
soup = BeautifulSoup(html.text, "html.parser")

# 以標題建立目錄儲存圖片
images_dir = title + "/"
if not os.path.exists(images_dir):
    os.mkdir(images_dir)

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
    photos = soup.select(".photo_img")
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
                with open(os.path.join(images_dir, filename), "wb") as f:
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


# yearurl.py
def twodigit(n):  # 將數值轉為二位數字串
    if n < 10:
        retstr = "0" + str(n)
    else:
        retstr = str(n)
    return retstr


urlbase = (
    "http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=2019"  # 網址前半
)
urltail = "01&stockNo=2317&_=1521363562193"  # 網址後半
for i in range(1, 13):  # 取1到12數字
    url_twse = urlbase + twodigit(i) + urltail  # 組合網址
    print(url_twse)


# stockmonth.py
def convertDate(date):  # 轉捔民國日期為西元:108/01/01->20190101
    str1 = str(date)
    yearstr = str1[:3]  # 取出民國年
    realyear = str(int(yearstr) + 1911)  # 轉為西元年
    realdate = realyear + str1[4:6] + str1[7:9]  # 組合日期
    return realdate


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

plt.rcParams["font.sans-serif"] = "mingliu"  # 設定中文字型
plt.rcParams["axes.unicode_minus"] = False

pd.options.mode.chained_assignment = None  # 取消顯示pandas資料重設警告

filepath = "stockmonth01.csv"

if not os.path.isfile(filepath):  # 如果檔案不存在就建立檔案
    url_twse = "http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20190101&stockNo=2317&_=1521363562193"
    res = requests.get(url_twse)  # 回傳為json資料
    jdata = json.loads(res.text)  # json解析

    outputfile = open(filepath, "w", newline="", encoding="utf-8")  # 開啟儲存檔案
    outputwriter = csv.writer(outputfile)  # 以csv格式寫入檔案
    outputwriter.writerow(jdata["fields"])
    for dataline in jdata["data"]:  # 寫入資料
        outputwriter.writerow(dataline)
    outputfile.close()  # 關閉檔案

pdstock = pd.read_csv(filepath, encoding="utf-8")  # 以pandas讀取檔案
for i in range(len(pdstock["日期"])):  # 轉換日期式為西元年格
    pdstock["日期"][i] = convertDate(pdstock["日期"][i])
pdstock["日期"] = pd.to_datetime(pdstock["日期"])  # 轉換日期欄位為日期格式
pdstock.plot(kind="line", figsize=(12, 6), x="日期", y=["收盤價", "最低價", "最高價"])  # 繪製統計圖


# stockyear.py
def twodigit(n):  # 將數值轉為二位數字串
    if n < 10:
        retstr = "0" + str(n)
    else:
        retstr = str(n)
    return retstr


def convertDate(date):  # 轉捔民國日期為西元:108/01/01->20190101
    str1 = str(date)
    yearstr = str1[:3]  # 取出民國年
    realyear = str(int(yearstr) + 1911)  # 轉為西元年
    realdate = realyear + str1[4:6] + str1[7:9]  # 組合日期
    return realdate


plt.rcParams["font.sans-serif"] = "mingliu"  # 設定中文字型
plt.rcParams["axes.unicode_minus"] = False

pd.options.mode.chained_assignment = None  # 取消顯示pandas資料重設警告

urlbase = (
    "http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=2019"  # 網址前半
)
urltail = "01&stockNo=2317&_=1521363562193"  # 網址後半
filepath = "stockyear2019.csv"

if not os.path.isfile(filepath):  # 如果檔案不存在就建立檔案
    for i in range(1, 13):  # 取1到12數字
        url_twse = urlbase + twodigit(i) + urltail  # 組合網址
        res = requests.get(url_twse)  # 回傳為json資料
        jdata = json.loads(res.text)  # json解析

        outputfile = open(filepath, "a", newline="", encoding="utf-8")  # 開啟儲存檔案
        outputwriter = csv.writer(outputfile)  # 以csv格式寫入檔案
        if i == 1:  # 若是1月就寫入欄位名稱
            outputwriter.writerow(jdata["fields"])
        for dataline in jdata["data"]:  # 逐月寫入資料
            outputwriter.writerow(dataline)
        time.sleep(0.5)  # 延遲0.5秒,否則有時會有錯誤
    outputfile.close()  # 關閉檔案

pdstock = pd.read_csv(filepath, encoding="utf-8")  # 以pandas讀取檔案
for i in range(len(pdstock["日期"])):  # 轉換日期式為西元年格式
    pdstock["日期"][i] = convertDate(pdstock["日期"][i])
pdstock["日期"] = pd.to_datetime(pdstock["日期"])  # 轉換日期欄位為日期格式
pdstock.plot(kind="line", figsize=(12, 6), x="日期", y=["收盤價", "最低價", "最高價"])  # 繪製統計圖


# stockyear_plotly.py
def twodigit(n):  # 將數值轉為二位數字串
    if n < 10:
        retstr = "0" + str(n)
    else:
        retstr = str(n)
    return retstr


def convertDate(date):  # 轉捔民國日期為西元:106/03/02->20170302
    str1 = str(date)
    yearstr = str1[:3]  # 取出民國年
    realyear = str(int(yearstr) + 1911)  # 轉為西元年
    realdate = realyear + str1[4:6] + str1[7:9]  # 組合日期
    return realdate


from plotly.graph_objs import Scatter, Layout
from plotly.offline import plot

pd.options.mode.chained_assignment = None  # 取消顯示pandas資料重設警告

urlbase = (
    "http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=2019"  # 網址前半
)
urltail = "01&stockNo=2317&_=1521363562193"  # 網址後半
filepath = "stockyear2019.csv"

if not os.path.isfile(filepath):  # 如果檔案不存在就建立檔案
    for i in range(1, 13):  # 取1到12數字
        url_twse = urlbase + twodigit(i) + urltail  # 組合網址
        res = requests.get(url_twse)  # 回傳為json資料
        jdata = json.loads(res.text)  # json解析

        outputfile = open(filepath, "a", newline="", encoding="utf-8")  # 開啟儲存檔案
        outputwriter = csv.writer(outputfile)  # 以csv格式寫入檔案
        if i == 1:  # 若是1月就寫入欄位名稱
            outputwriter.writerow(jdata["fields"])
        for dataline in jdata["data"]:  # 逐月寫入資料
            outputwriter.writerow(dataline)
        time.sleep(0.5)  # 延遲0.5秒,否則有時會有錯誤
    outputfile.close()  # 關閉檔案

pdstock = pd.read_csv(filepath, encoding="utf-8")  # 以pandas讀取檔案
for i in range(len(pdstock["日期"])):  # 轉換日期式為西元年格式
    pdstock["日期"][i] = convertDate(pdstock["日期"][i])
pdstock["日期"] = pd.to_datetime(pdstock["日期"])  # 轉換日期欄位為日期格式
data = [
    Scatter(x=pdstock["日期"], y=pdstock["收盤價"], name="收盤價"),
    Scatter(x=pdstock["日期"], y=pdstock["最低價"], name="最低價"),
    Scatter(x=pdstock["日期"], y=pdstock["最高價"], name="最高價"),
]
plot({"data": data, "layout": Layout(title="2019年個股統計圖")}, auto_open=True)

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


# books.py
def showkind(url, kind):
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, "lxml")
    try:
        pages = int(soup.select(".cnt_page span")[0].text)  # 該分類共有多少頁
        print("共有", pages, "頁")
        for page in range(1, pages + 1):
            pageurl = url + "&page=" + str(page).strip()
            print("第", page, "頁", pageurl)
            # showpage(pageurl,kind)
    except:  # 沒有分頁的處理
        showpage(url, kind)


def showpage(url, kind):
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, "lxml")
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


def twobyte(kindno):
    if kindno < 10:
        kindnostr = "0" + str(kindno)
    else:
        kindnostr = str(kindno)
    return kindnostr

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

kindno = 1  # 要下載的分類，預設為第1分類：文學小說
homeurl = "http://www.books.com.tw/web/books_nbtopm_01/?o=5&v=1"
mode = "?o=5&v=1"  # 顯示模式：直式  排序依：暢銷度
url = "http://www.books.com.tw/web/books_nbtopm_"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
}
html = requests.get(homeurl, headers=headers).text
soup = BeautifulSoup(html, "lxml")

# 中文書新書分類，取得分類資訊
res = soup.find("div", class_="mod_b type02_l001-1 clearfix")
hrefs = res.select("a")

kindno = int(input("請輸入要下載的分類："))
if 0 < kindno <= len(hrefs):
    kind = hrefs[kindno - 1].text  # 分類名稱
    print("下載的分類編號：{}   分類名稱：{}".format(kindno, kind))
    # 下載指定的分類
    kindurl = url + twobyte(kindno) + mode  # 分類網址
    print(kindurl)
    showkind(kindurl, kind)  # 顯示該分類所有書籍
else:
    print("分類不存在!")


# books_GoogleSheet.py
def showkind(url, kind):
    html = requests.get(url, headers=headers).text
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
    html = requests.get(url, headers=headers).text
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
        # 將資料加入 list1 串列中
        listdata = [kind, title, imgurl, author, publish, date, onsale, content]
        list1.append(listdata)
        n += 1
        print("n=", n)


def twobyte(kindno):
    if kindno < 10:
        kindnostr = "0" + str(kindno)
    else:
        kindnostr = str(kindno)
    return kindnostr


def auth_gss_client(path, scopes):  # 建立憑證
    credentials = ServiceAccountCredentials.from_json_keyfile_name(path, scopes)
    return gspread.authorize(credentials)


import gspread
from oauth2client.service_account import ServiceAccountCredentials
from time import sleep

auth_json_path = "C:/_git/vcs/_1.data/______test_files1/_key/PythonUpload.json"
gss_scopes = ["https://spreadsheets.google.com/feeds"]
gss_client = auth_gss_client(auth_json_path, gss_scopes)  # 連線

spreadsheet_key = "您自己的key"
sheet = gss_client.open_by_key(spreadsheet_key).sheet1  # 開啟工作表
sheet.clear()  # 清除工作表內容

list1 = []
kindno = 1  # 要下載的分類，預設為第 1分類：文學小說
homeurl = "http://www.books.com.tw/web/books_nbtopm_01/?o=5&v=1"
mode = "?o=5&v=1"  # 顯示模式：直式  排序依：暢銷度
url = "https://www.books.com.tw/web/books_nbtopm_"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
}
html = requests.get(homeurl, headers=headers).text
soup = BeautifulSoup(html, "html.parser")
# 中文書新書分類，取得分類資訊
res = soup.find("div", {"class": "mod_b type02_l001-1 clearfix"})
hrefs = res.select("a")
kindno = int(input("請輸入要下載的分類："))
if 0 < kindno <= len(hrefs):
    kind = hrefs[kindno - 1].text  # 分類名稱
    print("下載的分類編號：{}   分類名稱：{}".format(kindno, kind))
    # 下載指定的分類
    kindurl = url + twobyte(kindno) + mode  # 分類網址
    showkind(kindurl, kind)  # 顯示該分類所有書籍
    # 儲存 Google 試算表
    print("資料寫入雲端 Google 試算表中，請等侯幾分鐘!")
    listtitle = ["分類", "書名", "圖片網址", "作者", "出版社", "出版日期", "優惠價", "內容"]
    sheet.append_row(listtitle)  # 標題
    for item1 in list1:  # 資料
        sheet.append_row(item1)
        sleep(1)  # 必須加上適當的 delay
else:
    print("分類不存在!")
print("資料儲存完畢!")

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
    job = soup.select(".jbInfoin")  # 取class=jbInfoin內容
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
    job = soup.select(".it-md")  # 取class=jbInfoin內容
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

# filewrite1.py
content = """Hello Python
中文字測試
Welcome"""
f = open("tmp_file1.txt", "w", encoding="utf-8", newline="")
f.write(content)
f.close()

print("------------------------------------------------------------")  # 60個

# filewrite2.py
content = """Hello Python
中文字測試
Welcome"""
with open("tmp_file2.txt", "w", encoding="utf-8", newline="") as f:
    f.write(content)

print("------------------------------------------------------------")  # 60個

# fileread1.py
with open("tmp_file1.txt", "r", encoding="utf-8") as f:
    output_str = f.read(5)
    print(output_str)  # Hello

# fileread2.py
with open("tmp_file1.txt", "r", encoding="UTF-8") as f:
    print(f.readline())
    print(f.readline(3))

# fileread3.py
with open("tmp_file1.txt", "r", encoding="utf-8") as f:
    content = f.readlines()
    print(type(content))
    print(content)
# fileread4.py
with open("tmp_file2.txt", "r", encoding="UTF-8") as f:
    print(f.readlines())

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# csv_read.py

# 開啟 csv 檔案
with open("data/school.csv", newline="") as csvfile:
    # 讀取 csv 檔案內容
    rows = csv.reader(csvfile)
    # 以迴圈顯示每一列
    for row in rows:
        print(row)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 開啟 csv 檔案
with open("data/school.csv", newline="") as csvfile:
    # 讀取 csv 檔案內容
    rows = csv.reader(csvfile)
    # 以迴圈顯示每一列
    for row in rows:
        print(row)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# csv_read_dict.py

# 開啟 csv 檔案
with open("data/school.csv", newline="") as csvfile:
    # 讀取 csv 檔內容，將每一列轉成 dictionary
    rows = csv.DictReader(csvfile)
    # 以迴圈顯示每一列
    for row in rows:
        print(row["座號"], row["姓名"], row["國文"], row["英文"], row["數學"])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# csv_write_list1.py

with open("tmp_test1.csv", "w", newline="") as f:
    # 建立 csv 檔寫入物件
    writer = csv.writer(f)
    # 寫入欄位及資料
    writer.writerow(["座號", "姓名", "國文", "英文", "數學"])
    writer.writerow([1, "葉大雄", 65, 62, 40])
    writer.writerow([2, "陳靜香", 85, 90, 87])
    writer.writerow([3, "王聰明", 92, 90, 95])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# csv_write_list2.py

# 建立csv二維串列資料
csvtable = [
    ["座號", "姓名", "國文", "英文", "數學"],
    [1, "葉大雄", 65, 62, 40],
    [2, "陳靜香", 85, 90, 87],
    [3, "王聰明", 92, 90, 95],
]
# 寫入csv檔案
with open("tmp_test2.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(csvtable)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# csv_write_dict.py

with open("tmp_test3.csv", "w", newline="") as csvfile:
    # 定義欄位
    fieldnames = ["座號", "姓名", "國文", "英文", "數學"]
    # 將 dictionary 寫入 csv 檔
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    # 寫入欄位名稱
    writer.writeheader()
    # 寫入資料
    writer.writerow({"座號": 1, "姓名": "葉大雄", "國文": 65, "英文": 62, "數學": 40})
    writer.writerow({"座號": 2, "姓名": "陳靜香", "國文": 85, "英文": 90, "數學": 87})
    writer.writerow({"座號": 3, "姓名": "王聰明", "國文": 92, "英文": 90, "數學": 95})

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# jsonload1.py

class_str = """
{
  "一年甲班": [
    {
      "座號": 1,
      "姓名": "葉大雄",
      "國文": 65,
      "英文": 62,
      "數學": 40
    },
    {
      "座號": 2,
      "姓名": "陳靜香",
      "國文": 85,
      "英文": 90,
      "數學": 87
    },
    {
      "座號": 3,
      "姓名": "王聰明",
      "國文": 92,
      "英文": 90,
      "數學": 95
    }
  ]
}
"""
datas = json.loads(class_str)
print(type(datas))
for data in datas["一年甲班"]:
    print(data, data["姓名"])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# jsonload2.py

with open("data/class_str.json", "r", encoding="utf-8") as f:
    datas = json.load(f)
    print(type(datas))
    for data in datas["一年甲班"]:
        print(data, data["姓名"])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# jsondump1.py

with open("data/class_str.json", "r", encoding="utf-8") as f:
    datas = json.load(f)
print(datas, type(datas))
dumpdata = json.dumps(datas, ensure_ascii=False)
print(dumpdata, type(dumpdata))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# jsondump2.py

with open("data/class_str.json", "r", encoding="utf-8") as f:
    datas = json.load(f)
with open("tmp_class_str.json", "w", encoding="utf-8") as f:
    dumpdata = json.dump(datas, f, ensure_ascii=False)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
""" NG
# LinkGoogleSheet.py

import gspread
from oauth2client.service_account import ServiceAccountCredentials as sac

# 設定金鑰檔路徑及驗證範圍
auth_json = "data/PythonConnectGsheet1-6a6086d149c5.json"
gs_scopes = ["https://spreadsheets.google.com/feeds"]
# 連線資料表
cr = sac.from_json_keyfile_name(auth_json, gs_scopes)
gc = gspread.authorize(cr)
# 開啟資料表
spreadsheet_key = "1OihpM657yWo1lc3RjskRfZ8m75dCPwL1IPwoDXSvyzI"
sheet = gc.open_by_key(spreadsheet_key)
# 開啟工作簿
wks = sheet.sheet1
# 清除所有內容
wks.clear()
# 新增列
listtitle = ["座號", "姓名", "國文", "英文", "數學"]
wks.append_row(listtitle)  # 標題
listdatas = [[1, "葉大雄", 65, 62, 40], [2, "陳靜香", 85, 90, 87], [3, "王聰明", 92, 90, 95]]
for listdata in listdatas:
    wks.append_row(listdata)  # 資料內容
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# csv_read_dict.py

# 開啟 csv 檔案
with open("data/school.csv", newline="") as csvfile:
    # 讀取 csv 檔內容，將每一列轉成 dictionary
    rows = csv.DictReader(csvfile)
    # 以迴圈顯示每一列
    for row in rows:
        print(row["座號"], row["姓名"], row["國文"], row["英文"], row["數學"])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# csv_write_dict.py

with open("tmp_test3aa.csv", "w", newline="") as csvfile:
    # 定義欄位
    fieldnames = ["座號", "姓名", "國文", "英文", "數學"]
    # 將 dictionary 寫入 csv 檔
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    # 寫入欄位名稱
    writer.writeheader()
    # 寫入資料
    writer.writerow({"座號": 1, "姓名": "葉大雄", "國文": 65, "英文": 62, "數學": 40})
    writer.writerow({"座號": 2, "姓名": "陳靜香", "國文": 85, "英文": 90, "數學": 87})
    writer.writerow({"座號": 3, "姓名": "王聰明", "國文": 92, "英文": 90, "數學": 95})

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# csv_write_list1.py

with open("tmp_test1aaaa.csv", "w", newline="") as f:
    # 建立 csv 檔寫入物件
    writer = csv.writer(f)
    # 寫入欄位及資料
    writer.writerow(["座號", "姓名", "國文", "英文", "數學"])
    writer.writerow([1, "葉大雄", 65, 62, 40])
    writer.writerow([2, "陳靜香", 85, 90, 87])
    writer.writerow([3, "王聰明", 92, 90, 95])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# csv_write_list2.py

# 建立csv二維串列資料
csvtable = [
    ["座號", "姓名", "國文", "英文", "數學"],
    [1, "葉大雄", 65, 62, 40],
    [2, "陳靜香", 85, 90, 87],
    [3, "王聰明", 92, 90, 95],
]
# 寫入csv檔案
with open("tmp_test2aaaa.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(csvtable)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# fileread1.py

with open("tmp_file1.txt", "r", encoding="utf-8") as f:
    output_str = f.read(5)
    print(output_str)  # Hello

print("------------------------------------------------------------")  # 60個

# fileread2.py

with open("tmp_file1.txt", "r", encoding="UTF-8") as f:
    print(f.readline())
    print(f.readline(3))

print("------------------------------------------------------------")  # 60個

# fileread3.py

with open("tmp_file1.txt", "r", encoding="utf-8") as f:
    content = f.readlines()
    print(type(content))
    print(content)

print("------------------------------------------------------------")  # 60個

# fileread4.py

with open("tmp_file2.txt", "r", encoding="UTF-8") as f:
    print(f.readlines())

print("------------------------------------------------------------")  # 60個

# fileread5.py

with open("tmp_file2.txt", "r", encoding="UTF-8-sig") as f:
    print(f.readlines())

print("------------------------------------------------------------")  # 60個

# filewrite1.py

content = """Hello Python
中文字測試
Welcome"""
f = open("tmp_file1cccc.txt", "w", encoding="utf-8", newline="")
f.write(content)
f.close()

print("------------------------------------------------------------")  # 60個

# filewrite2.py

content = """Hello Python
中文字測試
Welcome"""
with open("tmp_file1ccccd.txt", "w", encoding="utf-8", newline="") as f:
    f.write(content)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# jsondump1.py

with open("data/class_str.json", "r", encoding="utf-8") as f:
    datas = json.load(f)
print(datas, type(datas))
dumpdata = json.dumps(datas, ensure_ascii=False)
print(dumpdata, type(dumpdata))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# jsondump2.py

with open("data/class_str.json", "r", encoding="utf-8") as f:
    datas = json.load(f)
with open("tmp_class_str2.json", "w", encoding="utf-8") as f:
    dumpdata = json.dump(datas, f, ensure_ascii=False)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# jsonload1.py

class_str = """
{
  "一年甲班": [
    {
      "座號": 1,
      "姓名": "葉大雄",
      "國文": 65,
      "英文": 62,
      "數學": 40
    },
    {
      "座號": 2,
      "姓名": "陳靜香",
      "國文": 85,
      "英文": 90,
      "數學": 87
    },
    {
      "座號": 3,
      "姓名": "王聰明",
      "國文": 92,
      "英文": 90,
      "數學": 95
    }
  ]
}
"""
datas = json.loads(class_str)
print(type(datas))
for data in datas["一年甲班"]:
    print(data, data["姓名"])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# jsonload2.py

with open("data/class_str.json", "r", encoding="utf-8") as f:
    datas = json.load(f)
    print(type(datas))
    for data in datas["一年甲班"]:
        print(data, data["姓名"])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
""" NG
#LinkGoogleSheet.py

import gspread
from oauth2client.service_account import ServiceAccountCredentials as sac

# 設定金鑰檔路徑及驗證範圍
auth_json = "data/PythonConnectGsheet1-6a6086d149c5.json"
gs_scopes = ["https://spreadsheets.google.com/feeds"]
# 連線資料表
cr = sac.from_json_keyfile_name(auth_json, gs_scopes)
gc = gspread.authorize(cr)
# 開啟資料表
spreadsheet_key = "1OihpM657yWo1lc3RjskRfZ8m75dCPwL1IPwoDXSvyzI"
sheet = gc.open_by_key(spreadsheet_key)
# 開啟工作簿
wks = sheet.sheet1
# 清除所有內容
wks.clear()
# 新增列
listtitle = ["座號", "姓名", "國文", "英文", "數學"]
wks.append_row(listtitle)  # 標題
listdatas = [[1, "葉大雄", 65, 62, 40], [2, "陳靜香", 85, 90, 87], [3, "王聰明", 92, 90, 95]]
for listdata in listdatas:
    wks.append_row(listdata)  # 資料內容
"""
print("------------------------------------------------------------")  # 60個
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


print("------------------------------------------------------------")  # 60個
