"""
Python網路爬蟲_大數據擷取、清洗、儲存與分析：王者歸來
ch06~ch15
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

font_filename = "D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
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


# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch6\ch6_1.py

# ch6_1.py
import hashlib

data = hashlib.md5()  # 建立data物件
data.update(b"Ming-Chi Institute of Technology")  # 更新data物件內容

print("Hash Value         = ", data.digest())
print("Hash Value(16進位) = ", data.hexdigest())
print(type(data))  # 列出data資料型態
print(type(data.hexdigest()))  # 列出哈希值資料型態


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch6\ch6_2.py

# ch6_2.py
import hashlib

data = hashlib.md5()  # 建立data物件
school = "明志科技大學"  # 中文字串
data.update(school.encode("utf-8"))  # 更新data物件內容

print("Hash Value         = ", data.digest())
print("Hash Value(16進位) = ", data.hexdigest())
print(type(data))  # 列出data資料型態
print(type(data.hexdigest()))  # 列出哈希值資料型態


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch6\ch6_3.py

# ch6_3.py
import hashlib

data = hashlib.md5()  # 建立data物件
filename = "data6_3.txt"

with open(filename, "rb") as fn:  # 以二進位方式讀取檔案
    btxt = fn.read()
    data.update(btxt)

print("Hash Value         = ", data.digest())
print("Hash Value(16進位) = ", data.hexdigest())
print(type(data))  # 列出data資料型態
print(type(data.hexdigest()))  # 列出哈希值資料型態


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch6\ch6_4.py

# ch6_4.py
import hashlib

data = hashlib.sha1()  # 建立data物件
data.update(b"Ming-Chi Institute of Technology")  # 更新data物件內容

print("Hash Value         = ", data.digest())
print("Hash Value(16進位) = ", data.hexdigest())
print(type(data))  # 列出data資料型態
print(type(data.hexdigest()))  # 列出哈希值資料型態


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch6\ch6_5.py

# ch6_5.py
import hashlib

print(hashlib.algorithms_available)  # 列出此平台可使用的哈希演算法


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch6\ch6_6.py

# ch6_6.py
import hashlib

print(hashlib.algorithms_guaranteed)  # 列出跨平台可使用的哈希演算法


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch6\ch6_7.py

# ch6_7.py
import requests
import json

url = "http://opendata.epa.gov.tw/webapi/Data/REWIQA/?$orderby=SiteName&$\
skip=0&$top=1000&format=json"
try:
    aqijsons = requests.get(url)  # 將檔案下載至aqijsons
    print("下載成功")
except Exception as err:
    print("下載失敗")

print(aqijsons.text)  # 列印所下載的json檔案

fn = "aqi.json"  # 建立欲儲存的json檔案
with open(fn, "w") as f:
    json.dump(aqijsons.json(), f)  # 寫入json檔案至aqi.json


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch6\ch6_8.py

# ch6_8.py
import json

fn = "aqi.json"
with open(fn) as fnObj:
    getDatas = json.load(fnObj)  # 讀json檔案

for getData in getDatas:
    county = getData["County"]  # 城市名稱
    sitename = getData["SiteName"]  # 站台名稱
    siteid = getData["SiteId"]  # 站台ID
    pm25 = getData["PM2.5"]  # PM2.5值
    print(
        "城市名稱 =%4s  站台ID =%3s  PM2.5值 =%3s  站台名稱 = %s "
        % (county, siteid, pm25, sitename)
    )


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch6\ch6_9.py

# ch6_9.py
import json

fn = "aqi.json"
with open(fn) as fnObj:
    getDatas = json.load(fnObj)  # 讀json檔案

for getData in getDatas:
    if getData["County"] == "臺北市":
        sitename = getData["SiteName"]  # 站台名稱
        siteid = getData["SiteId"]  # 站台ID
        pm25 = getData["PM2.5"]  # PM2.5值
        print("站台ID =%3s  PM2.5值 =%3s  站台名稱 = %s " % (siteid, pm25, sitename))


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch6\ch6_10.py

# ch6_10.py
import requests
import hashlib
import json

url = "http://opendata.epa.gov.tw/webapi/Data/REWIQA/?$orderby=SiteName&$\
skip=0&$top=1000&format=json"
try:
    aqijsons = requests.get(url)  # 將檔案下載至htmlfile
    print("下載成功")
except Exception as err:
    print("下載失敗")

data = hashlib.md5()
data.update(aqijsons.text.encode("utf-8"))
hashdata = data.hexdigest()
print("環保署PM2.5的哈希值 = ", hashdata)

fn = "out6_10.txt"
with open(fn, "w") as fileobj:
    fileobj.write(hashdata)


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch6\ch6_11.py

# ch6_11.py
import requests
import os
import json
import hashlib


def save_newaqi():
    """儲存newaqi.json"""
    with open(fn, "w") as f:
        json.dump(aqijsons.json(), f)  # 寫入json檔案至newaqi.json


def save_hashvalue():
    """儲存哈希值至hashvalue.txt"""
    with open(fn_hash, "w") as fileobj:
        fileobj.write(newhash)  # 寫入哈希值至hashvalue.txt


def cal_hashvalue():
    """計算hash value"""
    data = hashlib.md5()
    data.update(aqijsons.text.encode("utf-8"))
    hashdata = data.hexdigest()
    return hashdata  # 傳回哈希值


url = "http://opendata.epa.gov.tw/webapi/Data/REWIQA/?$orderby=SiteName&$\
skip=0&$top=1000&format=json"
try:
    aqijsons = requests.get(url)  # 將檔案下載至aqijsons
    print("下載成功")
except Exception as err:
    print("下載失敗")

fn = "newaqi.json"
fn_hash = "hashvalue.txt"  # 檔案名稱
if os.path.exists(fn_hash):  # 如果hashvalue.txt存在
    newhash = cal_hashvalue()  # 計算新的哈希值hashvalue
    print("newhash = ", newhash)
    # 開啟hashvalue.txt檔案
    with open(fn_hash, "r") as fnObj:  # 讀取舊的哈希值
        oldhash = fnObj.read()
        print("oldhash = ", oldhash)
    if newhash == oldhash:  # 比對新舊哈希值
        print("環保署空氣品質資料未更新")
    else:
        print("環保署空氣品質資料已經更新")
        save_newaqi()  # 儲存newaqi.son
        save_hashvalue()  # 儲存哈希值至hashvalue.txt
else:  # 如果hashvalue.txt不存在
    print("第一次啟動此程式")
    newhvalue = cal_hashvalue()
    print("哈希值 = ", newvalue)
    save_hashvalue()  # 儲存哈希值至hashvalue.txt
    save_newaqi()  # 儲存newaqi.son


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch6\ch6_12.py

# ch6_12.py
import csv

infn = "AQI_20190814010150.csv"  # 來源檔案
outfn = "out6_12.csv"  # 目的檔案
with open(infn) as csvRFile:  # 開啟csv檔案供讀取
    csvReader = csv.reader(csvRFile)  # 讀檔案建立Reader物件
    listReport = list(csvReader)  # 將資料轉成串列

newListReport = []  # 空串列
tmpList = []
for row in listReport:  # 使用迴圈取新的欄位
    tmpList = [row[1], row[23], row[11], row[0]]
    newListReport.append(tmpList)

with open(outfn, "w", newline="") as csvOFile:  # 開啟csv檔案供寫入
    csvWriter = csv.writer(csvOFile)  # 建立Writer物件
    for row in newListReport:  # 將串列寫入和列印
        csvWriter.writerow(row)  # 寫入檔案
        if row[0] != "County":  # 不是標題
            print(
                "城市名稱 =%4s  站台ID =%3s  PM2.5值 =%3s  站台名稱 = %s "
                % (row[0], row[1], row[2], row[3])
            )


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch6\ch6_13.py

# ch6_13.py
import csv

infn = "out6_12.csv"  # 來源檔案
with open(infn) as csvRFile:  # 開啟csv檔案供讀取
    csvReader = csv.reader(csvRFile)  # 讀檔案建立Reader物件
    listReport = list(csvReader)  # 將資料轉成串列

for row in listReport:  # 使用迴圈取新的欄位
    if row[0] == "臺北市":
        print("站台ID =%3s  PM2.5值 =%3s  站台名稱 = %s " % (row[1], row[2], row[3]))


print("------------------------------------------------------------")  # 60個


# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch7\ch7_1.py

# ch7_1.py
from selenium import webdriver

browser = webdriver.Firefox()
print(type(browser))


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch7\ch7_2.py

# ch7_2.py
from selenium import webdriver

driverPath = "D:\geckodriver\geckodriver.exe"
browser = webdriver.Firefox(executable_path=driverPath)
print(type(browser))


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch7\ch7_3.py

# ch7_3.py
from selenium import webdriver

dirverPath = "D:\geckodriver\chromedriver.exe"
browser = webdriver.Chrome(dirverPath)
print(type(browser))


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch7\ch7_4.py

# ch7_4.py
from selenium import webdriver

driverPath = "D:\geckodriver\geckodriver.exe"
browser = webdriver.Firefox(executable_path=driverPath)
url = "http://aaa.24ht.com.tw"
browser.get(url)  # 網頁下載至瀏覽器


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch7\ch7_4_1.py

# ch7_4_1.py
from selenium import webdriver

driverPath = "D:\geckodriver\geckodriver.exe"
browser = webdriver.Firefox(executable_path=driverPath)
url = "http://aaa.24ht.com.tw"
browser.get(url)  # 網頁下載至瀏覽器
print(browser.page_source)  # 列印網頁原始碼


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch7\ch7_4_2.py

# ch7_4_2.py
from selenium import webdriver

driverPath = "D:\geckodriver\geckodriver.exe"
browser = webdriver.Firefox(executable_path=driverPath)
url = "http://aaa.24ht.com.tw"
browser.get(url)  # 網頁下載至瀏覽器
print("瀏覽器名稱 = ", browser.name)  # 列印瀏覽器名稱
print("網頁url    = ", browser.current_url)  # 列印網頁url
print("網頁連線id = ", browser.session_id)  # 網頁連線id
print("瀏覽器功能 = \n", browser.capabilities)  # 瀏覽器功能設定訊息


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch7\ch7_4_3.py

# ch7_4_3.py
from selenium import webdriver
import time

urls = [
    "http://aaa.24ht.com.tw",
    "http://www.mcut.edu.tw",
    "http://www.siliconstone.com",
]

driverPath = "D:\geckodriver\geckodriver.exe"
browser = webdriver.Firefox(executable_path=driverPath)

for url in urls:
    browser.get(url)  # 網頁下載至瀏覽器
    time.sleep(5)

browser.quit()


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch7\ch7_5.py

# ch7_5.py
from selenium import webdriver

driverPath = "D:\geckodriver\geckodriver.exe"
browser = webdriver.Firefox(executable_path=driverPath)
url = "http://aaa.24ht.com.tw"
browser.get(url)  # 網頁下載至瀏覽器

tag = browser.find_element_by_id("main")
print(tag.tag_name)


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch7\ch7_6.py

# ch7_6.py
from selenium import webdriver

driverPath = "D:\geckodriver\geckodriver.exe"
browser = webdriver.Firefox(executable_path=driverPath)
url = "http://aaa.24ht.com.tw"
browser.get(url)  # 網頁下載至瀏覽器

try:
    tag = browser.find_element_by_id("main")
    print(tag.tag_name)
except:
    print("沒有找到相符的元素")


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch7\ch7_7.py

# ch7_7.py
from selenium import webdriver

driverPath = "D:\geckodriver\geckodriver.exe"
browser = webdriver.Firefox(executable_path=driverPath)
url = "http://aaa.24ht.com.tw"
browser.get(url)  # 網頁下載至瀏覽器

print("網頁標題內容是 = ", browser.title)

tag2 = browser.find_element_by_id("author")  # 傳回<h1>
print("\n標籤名稱 = %s, 內容是 = %s " % (tag2.tag_name, tag2.text))

print()
tag3 = browser.find_elements_by_id("content")  # 傳回<h1>
for t3 in tag3:
    print("標籤名稱 = %s, 內容是 = %s " % (t3.tag_name, t3.text))

print()
tag4 = browser.find_elements_by_tag_name("p")  # 傳回<p>
for t4 in tag4:
    print("標籤名稱 = %s, 內容是 = %s " % (t4.tag_name, t4.text))

print()
tag5 = browser.find_elements_by_tag_name("img")  # 傳回<img>
for t5 in tag5:
    print("標籤名稱 = %s, 內容是 = %s " % (t5.tag_name, t5.get_attribute("src")))

print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch7\ch7_7_1.py

# ch7_7_1.py
from selenium import webdriver

driverPath = "D:\geckodriver\chromedriver.exe"
browser = webdriver.Chrome(executable_path=driverPath)
url = "d:\Web_Crawler\ch7\h7_1.html"
browser.get(url)  # 網頁下載至瀏覽器

n1 = browser.find_element_by_xpath("//h4")
print(n1.text)
n2 = browser.find_element_by_xpath("//body/section/h4")
print(n2.text)
n3 = browser.find_element_by_xpath("//section/h4")
print(n3.text)
n4 = browser.find_element_by_xpath("//body/*/h4")
print(n4.text)


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch7\ch7_7_2.py

# ch7_7_2.py
from selenium import webdriver

driverPath = "D:\geckodriver\chromedriver.exe"
browser = webdriver.Chrome(executable_path=driverPath)
url = "d:\Web_Crawler\ch7\h7_1.html"
browser.get(url)  # 網頁下載至瀏覽器

n1 = browser.find_element_by_xpath("//p")
print(n1.text)


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch7\ch7_7_3.py

# ch7_7_3.py
from selenium import webdriver

driverPath = "D:\geckodriver\chromedriver.exe"
browser = webdriver.Chrome(executable_path=driverPath)
url = "d:\Web_Crawler\ch7\h7_1.html"
browser.get(url)  # 網頁下載至瀏覽器

n1 = browser.find_element_by_xpath("//section/p[1]")
print(n1.text)
n2 = browser.find_element_by_xpath("//section/p[2]")
print(n1.text)

print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch7\ch7_7_4.py

# ch7_7_4.py
from selenium import webdriver

driverPath = "D:\geckodriver\chromedriver.exe"
browser = webdriver.Chrome(executable_path=driverPath)
url = "d:\Web_Crawler\ch7\h7_1.html"
browser.get(url)  # 網頁下載至瀏覽器

n1 = browser.find_element_by_xpath("//section/p[@class='year']")
print(n1.text)
n1 = browser.find_element_by_xpath("//section/p[@class='price']")
print(n1.text)

print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch7\ch7_7_5.py

# ch7_7_5.py
from selenium import webdriver

driverPath = "D:\geckodriver\chromedriver.exe"
browser = webdriver.Chrome(executable_path=driverPath)
url = "d:\Web_Crawler\ch7\h7_2.html"
browser.get(url)  # 網頁下載至瀏覽器

pict = browser.find_element_by_xpath("//section/img")
print(pict.get_attribute("src"))


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch7\ch7_7_6.py

# ch7_7_6.py
from selenium import webdriver

driverPath = "D:\geckodriver\chromedriver.exe"
browser = webdriver.Chrome(executable_path=driverPath)
url = "d:\Web_Crawler\ch7\h7_3.html"
browser.get(url)  # 網頁下載至瀏覽器

n1 = browser.find_element_by_xpath("//h1/em")
print("em          : ", n1.text)
n2 = browser.find_element_by_xpath("//h1")
print("h1          : ", n2.text)
n3 = browser.find_element_by_xpath("//h1")
print("textContent : ", n3.get_attribute("textContent"))
n4 = browser.find_element_by_xpath("//h1")
print("innerHTML : ", n4.get_attribute("innerHTML"))
n5 = browser.find_element_by_xpath("//h1")
print("outerHTML : ", n5.get_attribute("outerHTML"))

print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch7\ch7_7_7.py

# ch7_7_7.py
from selenium import webdriver

driverPath = "D:\geckodriver\chromedriver.exe"
browser = webdriver.Chrome(executable_path=driverPath)
url = "d:\Web_Crawler\ch7\h7_4.html"
browser.get(url)  # 網頁下載至瀏覽器

n = browser.find_element_by_xpath("//div[@id='Traveling']//a[contains(text(),'深石')]")
print(n.get_attribute("outerHTML"))
print(n.get_attribute("href"))


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch7\ch7_7_8.py

# ch7_7_8.py
from selenium import webdriver

driverPath = "D:\geckodriver\chromedriver.exe"
headless = webdriver.ChromeOptions()
headless.add_argument("headless")  # 隱藏參數
browser = webdriver.Chrome(executable_path=driverPath, options=headless)
url = "d:\Web_Crawler\ch7\h7_4.html"
browser.implicitly_wait(5)  # 等待網頁載入
browser.get(url)  # 網頁下載至瀏覽器

n = browser.find_element_by_xpath("//div[@id='Traveling']//a[contains(text(),'深石')]")
print(n.get_attribute("outerHTML"))
print(n.get_attribute("href"))


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch7\ch7_8.py

# ch7_8.py
from selenium import webdriver
import time

driverPath = "D:\geckodriver\geckodriver.exe"
browser = webdriver.Firefox(executable_path=driverPath)
url = "http://www.deepmind.com.tw"
browser.get(url)  # 網頁下載至瀏覽器

eleLink = browser.find_element_by_link_text("深智數位緣起")
print(type(eleLink))  # 列印eleLink資料類別
time.sleep(5)  # 暫停5秒
eleLink.click()


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch7\ch7_9.py

# ch7_9.py
from selenium import webdriver
import time

driverPath = "D:\geckodriver\geckodriver.exe"
browser = webdriver.Firefox(executable_path=driverPath)
url = "http://www.mcut.edu.tw/?Lang=en"
browser.get(url)  # 網頁下載至瀏覽器

txtBox = browser.find_element_by_id("hdSchKey")
txtBox.send_keys("王永慶")  # 輸入表單資料
time.sleep(5)  # 暫停5秒
txtBox.submit()  # 送出表單


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch7\ch7_9_1.py

# ch7_9_1.py
from selenium import webdriver
import time

driverPath = "D:\geckodriver\geckodriver.exe"
browser = webdriver.Firefox(executable_path=driverPath)
url = "http://www.mcut.edu.tw/?Lang=en"
browser.get(url)  # 網頁下載至瀏覽器

txtBox = browser.find_element_by_name("SchKey")
txtBox.send_keys("王永慶")  # 輸入表單資料
time.sleep(5)  # 暫停5秒
txtBox.submit()  # 送出表單


print("------------------------------------------------------------")  # 60個


# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch7\ch7_10.py

# ch7_10.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driverPath = "D:\geckodriver\geckodriver.exe"
browser = webdriver.Firefox(executable_path=driverPath)
url = "http://www.mcut.edu.tw"
browser.get(url)  # 網頁下載至瀏覽器

ele = browser.find_element_by_tag_name("body")
time.sleep(3)
ele.send_keys(Keys.PAGE_DOWN)  # 網頁捲動到下一頁
time.sleep(3)
ele.send_keys(Keys.END)  # 網頁捲動到最底端
time.sleep(3)
ele.send_keys(Keys.PAGE_UP)  # 網頁捲動到上一頁
time.sleep(3)
ele.send_keys(Keys.HOME)  # 網頁捲動到最上端


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch7\ch7_11.py

# ch7_11.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driverPath = "D:\geckodriver\geckodriver.exe"
browser = webdriver.Firefox(executable_path=driverPath)
url = "http://www.deepmind.com.tw"
browser.get(url)  # 網頁下載至瀏覽器

time.sleep(3)
browser.refresh()  # 更新網頁
time.sleep(3)
browser.quit()  # 關閉網頁


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch7\ch7_12.py

# ch7_12.py
from selenium import webdriver
import time

url = "https://www.google.com"
email = input("請輸入你的Google Email的帳號 : ")
pwd = input("請輸入你的Google Email的密碼 : ")

driverPath = "D:\geckodriver\geckodriver.exe"
browser = webdriver.Firefox(executable_path=driverPath)
browser.get(url)  # 網頁下載至瀏覽器

browser.find_element_by_id("gb_70").click()


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch7\ch7_13.py

# ch7_13.py
from selenium import webdriver
import time

url = "https://www.google.com"
email = input("請輸入你的Google Email的帳號 : ")
pwd = input("請輸入你的Google Email的密碼 : ")

driverPath = "D:\geckodriver\geckodriver.exe"
browser = webdriver.Firefox(executable_path=driverPath)
browser.get(url)  # 網頁下載至瀏覽器

browser.find_element_by_id("gb_70").click()  # 按登入鈕
browser.find_element_by_id("identifierId").send_keys(email)  # 輸入帳號
time.sleep(3)


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch7\ch7_14.py

# ch7_14.py
from selenium import webdriver
import time

url = "https://www.google.com"
email = input("請輸入你的Google Email的帳號 : ")
pwd = input("請輸入你的Google Email的密碼 : ")

driverPath = "D:\geckodriver\geckodriver.exe"
browser = webdriver.Firefox(executable_path=driverPath)
browser.get(url)  # 網頁下載至瀏覽器

browser.find_element_by_id("gb_70").click()  # 按登入鈕
browser.find_element_by_id("identifierId").send_keys(email)  # 輸入帳號
time.sleep(3)

# 按繼續鈕
browser.find_element_by_xpath("//span[@class='RveJvd snByac']").click()
time.sleep(3)


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch7\ch7_15.py

# ch7_15.py
from selenium import webdriver
import time

url = "https://www.google.com"
email = input("請輸入你的Google Email的帳號 : ")
pwd = input("請輸入你的Google Email的密碼 : ")

driverPath = "D:\geckodriver\geckodriver.exe"
browser = webdriver.Firefox(executable_path=driverPath)
browser.get(url)  # 網頁下載至瀏覽器

browser.find_element_by_id("gb_70").click()  # 按登入鈕
browser.find_element_by_id("identifierId").send_keys(email)  # 輸入帳號
time.sleep(3)

# 按繼續鈕
browser.find_element_by_xpath("//span[@class='RveJvd snByac']").click()
time.sleep(3)

# 輸入密碼
browser.find_element_by_xpath("//input[@type='password']").send_keys(pwd)
time.sleep(3)


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch7\ch7_16.py

# ch7_16.py
from selenium import webdriver
import time

url = "https://www.google.com"
email = input("請輸入你的Google Email的帳號 : ")
pwd = input("請輸入你的Google Email的密碼 : ")

driverPath = "D:\geckodriver\geckodriver.exe"
browser = webdriver.Firefox(executable_path=driverPath)
browser.get(url)  # 網頁下載至瀏覽器

browser.find_element_by_id("gb_70").click()  # 按登入鈕
browser.find_element_by_id("identifierId").send_keys(email)  # 輸入帳號
time.sleep(3)

# 按繼續鈕
browser.find_element_by_xpath("//span[@class='RveJvd snByac']").click()
time.sleep(3)

# 輸入密碼
browser.find_element_by_xpath("//input[@type='password']").send_keys(pwd)
time.sleep(3)

# 按繼續鈕
browser.find_element_by_xpath("//span[@class='RveJvd snByac']").click()
time.sleep(3)


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch7\ch7_17.py

# ch7_17.py
from selenium import webdriver
import time

url = "https://opendata.epa.gov.tw/data/contents/aqi/"

driverPath = "D:\geckodriver\chromedriver.exe"
browser = webdriver.Chrome(executable_path=driverPath)
browser.get(url)  # 網頁下載至瀏覽器

browser.find_element_by_link_text("JSON").click()  # 按JSON鈕
time.sleep(3)

browser.find_element_by_link_text("XML").click()  # 按XML鈕
time.sleep(3)

browser.find_element_by_link_text("CSV").click()  # 按CSV鈕
time.sleep(3)


print("------------------------------------------------------------")  # 60個


# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch8\ch8_1.py

# ch8_1.py
import requests, bs4

url = "https://www.ptt.cc/bbs/Gossiping/index.html"
ptthtml = requests.get(url, cookies={"over18": "1"})
objSoup = bs4.BeautifulSoup(ptthtml.text, "lxml")
print("列印BeautifulSoup物件資料型態 ", type(objSoup))


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch8\ch8_2.py

# ch8_2.py
import requests, bs4

url = "https://www.ptt.cc/bbs/Gossiping/index.html"
ptthtml = requests.get(url, cookies={"over18": "1"})
objSoup = bs4.BeautifulSoup(ptthtml.text, "lxml")

articles = 0  # 本頁面文章數量
pttdivs = objSoup.find_all("div", "r-ent")
for p in pttdivs:
    if p.find("a"):
        articles += 1
print("本頁的文章數量 = ", articles)


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch8\ch8_3.py

# ch8_3.py
import requests, bs4

url = "https://www.ptt.cc/bbs/Gossiping/index.html"
ptthtml = requests.get(url, cookies={"over18": "1"})
objSoup = bs4.BeautifulSoup(ptthtml.text, "lxml")

articles = []  # 本頁面文章
pttdivs = objSoup.find_all("div", "r-ent")
for p in pttdivs:
    if p.find("a"):
        title = p.find("a").text
        author = p.find("div", "author").text
        href = p.find("a")["href"]
        articles.append(
            {
                "title": title,  # 文章標題
                "author": author,  # 文章作者
                "href": href,  # 文章超連結
            }
        )
print("本頁的文章數量 = ", len(articles))
count = 0  # 文章編號計數器
for article in articles:
    count += 1
    print("文章編號 : ", count)
    print("文章標題 : ", article["title"])
    print("文章作者 : ", article["author"])
    print("文章連結 : ", article["href"], "\n")


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch8\ch8_4.py

# ch8_4.py
import requests, bs4

url = "https://www.ptt.cc/bbs/Gossiping/index.html"
ptthtml = requests.get(url, cookies={"over18": "1"})
objSoup = bs4.BeautifulSoup(ptthtml.text, "lxml")

articles = []  # 本頁面文章
pttdivs = objSoup.find_all("div", "r-ent")
for p in pttdivs:
    if p.find("a"):
        title = p.find("a").text
        author = p.find("div", "author").text
        href = p.find("a")["href"]
        push_num = p.find("div", "nrec").text
        articles.append(
            {
                "title": title,  # 文章標題
                "author": author,  # 文章作者
                "href": href,  # 文章超連結
                "push_num": push_num,  # 推文數
            }
        )
print("本頁的文章數量 = ", len(articles))
count = 0  # 文章編號計數器
for article in articles:
    count += 1
    print("文章編號 : ", count)
    print("文章標題 : ", article["title"])
    print("文章作者 : ", article["author"])
    print("文章連結 : ", article["href"])
    print("推文數量 : ", article["push_num"], "\n")


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch8\ch8_5.py

# ch8_5.py
import requests, bs4

url = "https://www.ptt.cc/bbs/Gossiping/index.html"
ptthtml = requests.get(url, cookies={"over18": "1"})
objSoup = bs4.BeautifulSoup(ptthtml.text, "lxml")

articles = []  # 本頁面文章
pttdivs = objSoup.find_all("div", "r-ent")
for p in pttdivs:
    if p.find("a"):
        title = p.find("a").text
        author = p.find("div", "author").text
        href = p.find("a")["href"]
        push_num = p.find("div", "nrec").text
        if push_num.startswith("X"):  # 表示推文被噓超過10次
            push_num = "0"
        if push_num == "爆":  # 表示推文超過100次
            push_num = "100"
        articles.append(
            {
                "title": title,  # 文章標題
                "author": author,  # 文章作者
                "href": href,  # 文章超連結
                "push_num": push_num,  # 推文數
            }
        )
print("本頁的文章數量 = ", len(articles))
count = 0  # 文章編號計數器
pushcounts = 20  # 最低推文數
print("下列是推文數大於20的文章", "\n")
for article in articles:
    count += 1
    if article["push_num"] != "":  # 測試是否空的
        push_min = int(article["push_num"])  # 不是空的,直接獲得推文數
    else:
        push_min = 0  # 是空的,推文數是0
    if push_min > pushcounts:  # 如果推文數大於最低推文數
        print("文章編號 : ", count)
        print("文章標題 : ", article["title"])
        print("文章作者 : ", article["author"])
        print("文章連結 : ", article["href"])
        print("推文數量 : ", article["push_num"], "\n")


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch8\ch8_6.py

# ch8_6.py
import requests, bs4

url = "https://www.ptt.cc/bbs/Gossiping/index.html"
ptthtml = requests.get(url, cookies={"over18": "1"})
objSoup = bs4.BeautifulSoup(ptthtml.text, "lxml")

articles = []  # 本頁面文章
pttdivs = objSoup.find_all("div", "r-ent")
for p in pttdivs:
    if p.find("a"):
        title = p.find("a").text
        author = p.find("div", "author").text
        href = p.find("a")["href"]
        push_num = p.find("div", "nrec").text
        if push_num.startswith("X"):  # 表示推文被噓超過10次
            push_num = "0"
        if push_num == "爆":  # 表示推文超過100次
            push_num = "100"
        publish_time = p.find("div", "date").text
        articles.append(
            {
                "title": title,  # 文章標題
                "publish_time": publish_time,  # 發表時間
                "author": author,  # 文章作者
                "href": href,  # 文章超連結
                "push_num": push_num,  # 推文數
            }
        )
print("本頁的文章數量 = ", len(articles))
count = 0  # 文章編號計數器
pushcounts = 20  # 最低推文數
print("下列是推文數大於20的文章", "\n")
for article in articles:
    count += 1
    if article["push_num"] != "":  # 測試是否空的
        push_min = int(article["push_num"])  # 不是空的,直接獲得推文數
    else:
        push_min = 0  # 是空的,推文數是0
    if push_min > pushcounts:  # 如果推文數大於最低推文數
        print("文章編號 : ", count)
        print("文章標題 : ", article["title"])
        print("發表時間 : ", article["publish_time"])
        print("文章作者 : ", article["author"])
        print("文章連結 : ", article["href"])
        print("推文數量 : ", article["push_num"], "\n")


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch8\ch8_7.py

# ch8_7.py
import requests, bs4
import json

url = "https://www.ptt.cc/bbs/Gossiping/index.html"
ptthtml = requests.get(url, cookies={"over18": "1"})
objSoup = bs4.BeautifulSoup(ptthtml.text, "lxml")

articles = []  # 本頁面文章
pttdivs = objSoup.find_all("div", "r-ent")
for p in pttdivs:
    if p.find("a"):
        title = p.find("a").text
        author = p.find("div", "author").text
        href = p.find("a")["href"]
        push_num = p.find("div", "nrec").text
        if push_num.startswith("X"):  # 表示推文被噓超過10次
            push_num = "0"
        if push_num == "爆":  # 表示推文超過100次
            push_num = "100"
        publish_time = p.find("div", "date").text
        articles.append(
            {
                "title": title,  # 文章標題
                "publish_time": publish_time,  # 發表時間
                "author": author,  # 文章作者
                "href": href,  # 文章超連結
                "push_num": push_num,  # 推文數
            }
        )

fn = "out8_7.json"
with open(fn, "w", encoding="utf-8") as fnObj:
    json.dump(articles, fnObj, ensure_ascii=False, indent=2)


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch8\ch8_8.py

# ch8_8.py
import requests, bs4

url = "https://www.ptt.cc/bbs/Gossiping/index.html"
ptthtml = requests.get(url, cookies={"over18": "1"})
objSoup = bs4.BeautifulSoup(ptthtml.text, "lxml")

div_page = objSoup.find("div", "btn-group btn-group-paging")
print(type(div_page))
print(div_page)


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch8\ch8_8_1.py

# ch8_8_1.py
import requests, bs4

url = "https://www.ptt.cc/bbs/Gossiping/index.html"
ptthtml = requests.get(url, cookies={"over18": "1"})
objSoup = bs4.BeautifulSoup(ptthtml.text, "lxml")

div_page = objSoup.find("div", "btn-group-paging")
print(type(div_page))
print(div_page)


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch8\ch8_9.py

# ch8_9.py
import requests, bs4

url = "https://www.ptt.cc/bbs/Gossiping/index.html"
ptthtml = requests.get(url, cookies={"over18": "1"})
objSoup = bs4.BeautifulSoup(ptthtml.text, "lxml")

div_page = objSoup.find("div", "btn-group-paging")
last_page = div_page.find_all("a")
print(type(last_page))  # 列出last_page資料型態
print(last_page)  # 列出last_page


print("------------------------------------------------------------")  # 60個


# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch8\ch8_10.py

# ch8_10.py
import requests, bs4

url = "https://www.ptt.cc/bbs/Gossiping/index.html"
ptthtml = requests.get(url, cookies={"over18": "1"})
objSoup = bs4.BeautifulSoup(ptthtml.text, "lxml")

div_page = objSoup.find("div", "btn-group-paging")
last_page = div_page.find_all("a")[1]
print(type(last_page))  # 列出last_page資料型態
print(last_page)  # 列出last_page


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch8\ch8_11.py

# ch8_11.py
import requests, bs4

url = "https://www.ptt.cc/bbs/Gossiping/index.html"
ptthtml = requests.get(url, cookies={"over18": "1"})
objSoup = bs4.BeautifulSoup(ptthtml.text, "lxml")

div_page = objSoup.find("div", "btn-group-paging")
last_page = div_page.find_all("a")[1]["href"]
print(type(last_page))  # 列出last_page資料型態
print(last_page)  # 列出last_page


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch8\ch8_12.py

# ch8_12.py
import requests, bs4

ptturl = "https://www.ptt.cc"
page = "/bbs/Gossiping/index.html"
ptthtml = requests.get(ptturl + page, cookies={"over18": "1"})
objSoup = bs4.BeautifulSoup(ptthtml.text, "lxml")  # 目前頁

div_page = objSoup.find("div", "btn-group-paging")
last_page = div_page.find_all("a")[1]["href"]  # 前一頁超連結

ptthtml = requests.get(ptturl + last_page, cookies={"over18": "1"})  # 前一頁
objSoup = bs4.BeautifulSoup(ptthtml.text, "lxml")  # 前一頁

articles = []  # 本頁面文章
pttdivs = objSoup.find_all("div", "r-ent")
for p in pttdivs:
    if p.find("a"):
        title = p.find("a").text
        author = p.find("div", "author").text
        href = p.find("a")["href"]
        push_num = p.find("div", "nrec").text
        publish_time = p.find("div", "date").text
        articles.append(
            {
                "title": title,  # 文章標題
                "publish_time": publish_time,  # 發表時間
                "author": author,  # 文章作者
                "href": href,  # 文章超連結
                "push_num": push_num,  # 推文數
            }
        )
print("本頁的文章數量 = ", len(articles))
count = 0  # 文章編號計數器
for article in articles:
    count += 1
    print("文章編號 : ", count)
    print("文章標題 : ", article["title"])
    print("發表時間 : ", article["publish_time"])
    print("文章作者 : ", article["author"])
    print("文章連結 : ", article["href"])
    print("推文數量 : ", article["push_num"], "\n")


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch8\ch8_13.py

# ch8_13.py
import requests, bs4

url = "https://www.ptt.cc/bbs/beauty/index.html"
ptthtml = requests.get(url, cookies={"over18": "1"})
objSoup = bs4.BeautifulSoup(ptthtml.text, "lxml")

articles = 0  # 本頁面文章數量
pttdivs = objSoup.find_all("div", "r-ent")
for p in pttdivs:
    if p.find("a"):
        articles += 1
print("本頁的文章數量 = ", articles)


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch8\ch8_14.py

# ch8_14.py
import requests, bs4

url = "https://www.ptt.cc/bbs/beauty/index.html"
ptthtml = requests.get(url, cookies={"over18": "1"})
objSoup = bs4.BeautifulSoup(ptthtml.text, "lxml")

articles = []  # 本頁面文章
pttdivs = objSoup.find_all("div", "r-ent")
for p in pttdivs:
    if p.find("a"):
        title = p.find("a").text
        author = p.find("div", "author").text
        href = p.find("a")["href"]
        push_num = p.find("div", "nrec").text
        ptime = p.find("div", "date").text
        articles.append(
            {
                "title": title,  # 文章標題
                "author": author,  # 文章作者
                "href": href,  # 文章超連結
                "ptime": ptime,  # 貼文時間
                "push_num": push_num,  # 推文數
            }
        )
print("本頁的文章數量 = ", len(articles))
count = 0  # 文章編號計數器
for article in articles:
    count += 1
    print("文章編號 : ", count)
    print("貼文時間 : ", article["ptime"])
    print("文章作者 : ", article["author"])
    print("文章標題 : ", article["title"])
    print("文章連結 : ", article["href"])
    print("推文數量 : ", article["push_num"], "\n")


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch8\ch8_15.py

# ch8_15.py
import requests, bs4

url_ppt = "https://www.ptt.cc"
beauty = "/bbs/beauty/index.html"

ptthtml = requests.get(url_ppt + beauty, cookies={"over18": "1"})
objSoup = bs4.BeautifulSoup(ptthtml.text, "lxml")

pttdivs = objSoup.find_all("div", "r-ent")
href = pttdivs[0].find("a")["href"]  # 文章超連結

print("目前連線網址 : ", url_ppt + href)
beauty_html = requests.get(url_ppt + href, cookies={"over18": "1"})  # 進入超連結
beauty_soup = bs4.BeautifulSoup(beauty_html.text, "lxml")

beauty_divs = beauty_soup.find("div", id="main-content")
items = beauty_divs.find_all("div", "article-metaline")

for item in items:  # 列印標題
    field = item.find("span", "article-meta-tag")
    print(field.text, end=" : ")
    field_data = item.find("span", "article-meta-value")
    print(field_data.text)

mylist = list(beauty_divs)  # 轉成串列
print("內文 : ", mylist[4].strip())  # 列印本文


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch8\ch8_16.py

# ch8_16.py
import requests, bs4

url_ppt = "https://www.ptt.cc"
beauty = "/bbs/beauty/index.html"

ptthtml = requests.get(url_ppt + beauty, cookies={"over18": "1"})
objSoup = bs4.BeautifulSoup(ptthtml.text, "lxml")

pttdivs = objSoup.find_all("div", "r-ent")
href = pttdivs[0].find("a")["href"]  # 文章超連結

print("目前連線網址 : ", url_ppt + href)
beauty_html = requests.get(url_ppt + href, cookies={"over18": "1"})  # 進入超連結
beauty_soup = bs4.BeautifulSoup(beauty_html.text, "lxml")

beauty_divs = beauty_soup.find("div", id="main-content")
items = beauty_divs.find_all("div", "push")
print("評論如下:")
for item in items:
    topiclist = list(item)
    push = topiclist[0]
    push_id = topiclist[1]
    push_content = topiclist[2]
    push_time = topiclist[3]
    print("推      :", push.text)
    print("作者    :", push_id.text)
    print("內文   ", push_content.text)
    print("時間    :", push_time.text.strip())


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch8\ch8_17.py

# ch8_17.py
import requests, bs4, os

url_ppt = "https://www.ptt.cc"
beauty = "/bbs/beauty/index.html"

ptthtml = requests.get(url_ppt + beauty, cookies={"over18": "1"})
objSoup = bs4.BeautifulSoup(ptthtml.text, "lxml")

pttdivs = objSoup.find_all("div", "r-ent")
href = pttdivs[0].find("a")["href"]  # 文章超連結

print("目前連線網址 : ", url_ppt + href)
beauty_html = requests.get(url_ppt + href, cookies={"over18": "1"})  # 進入超連結
beauty_soup = bs4.BeautifulSoup(beauty_html.text, "lxml")

beauty_divs = beauty_soup.find("div", id="main-content")
photos = []  # 圖片網址
url_photos = beauty_divs.find_all("a")  # 找尋所有圖片
for photo in url_photos:
    href_photo = photo["href"]
    if href_photo.startswith("https://i.imgur"):  # 判斷圖片網址
        photos.append(href_photo)

for photo in photos:  # 列印圖片網址
    print(photo)

destDir = "out8_17"
if os.path.exists(destDir) == False:  # 如果沒有此資料夾就建立
    os.mkdir(destDir)
print("搜尋到的圖片數量 = ", len(photos))  # 列出搜尋到的圖片數量
for photo in photos:  # 迴圈下載圖片與儲存
    picture = requests.get(photo)  # 下載圖片
    print("%s 圖片下載成功" % photo)
    # 先開啟檔案, 再儲存圖片
    pictFile = open(os.path.join(destDir, os.path.basename(photo)), "wb")
    for diskStorage in picture.iter_content(10240):
        pictFile.write(diskStorage)
    pictFile.close()  # 關閉檔案


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch8\ch8_18.py

# ch8_18.py
import requests

url = "http://api.ipstack.com/www.mcut.edu.tw?access_key=Your API Key"
urlfile = requests.get(url)
ip_info = urlfile.json()
print("資料型態 ", type(ip_info))

print("IP地址 : ", ip_info["ip"])
print("洲名   : ", ip_info["continent_name"])
print("國名   : ", ip_info["country_name"])
print("城市名 : ", ip_info["city"])
print("緯度   : ", ip_info["latitude"])
print("經度   : ", ip_info["longitude"])


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch8\ch8_19.py

# ch8_19.py
import requests

url_head = "http://api.ipstack.com/"
url_tail = "?access_key=Your API Key"
getip = input("請輸入網域或IP : ")
url = url_head + getip + url_tail
urlfile = requests.get(url.strip())
ip_info = urlfile.json()

print("IP地址 : ", ip_info["ip"])
print("洲名   : ", ip_info["continent_name"])
print("國名   : ", ip_info["country_name"])
print("城市名 : ", ip_info["city"])
print("緯度   : ", ip_info["latitude"])
print("經度   : ", ip_info["longitude"])


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch8\ch8_20.py

# ch8_20.py
import requests, bs4, re


def get_ip(ipstr):
    """由字串回傳IP地址"""
    pattern = r"\d+.\d+.\d+.\d+"
    addr = re.search(pattern, ipstr)
    return addr


def get_city(ptturl):
    """由IP地址回傳城市名稱"""
    url_head = "http://api.ipstack.com/"
    url_tail = "?access_key=Your API Key"
    url = url_head + ptturl + url_tail
    urlfile = requests.get(url.strip())
    ip_info = urlfile.json()
    return ip_info["city"]


url_ptt = "https://www.ptt.cc"
gossiping = "/bbs/gossiping/index.html"

ptthtml = requests.get(url_ptt + gossiping, cookies={"over18": "1"})
objSoup = bs4.BeautifulSoup(ptthtml.text, "lxml")

pttdivs = objSoup.find_all("div", "r-ent")
href = pttdivs[0].find("a")["href"]  # 文章超連結
title = pttdivs[0].find("a").text

print("目前連線網址 : ", url_ptt + href)
print("目前文章標題 : ", title)
gossiping_html = requests.get(url_ptt + href, cookies={"over18": "1"})  # 進入超連結
gossiping_soup = bs4.BeautifulSoup(gossiping_html.text, "lxml")

gossiping_span = gossiping_soup.find("span", "f2")  # 爬取文章來源
if gossiping_span:
    print("文章來源 :")
    print(gossiping_span.text)
    ip_addr = get_ip(gossiping_span.text)
    print("IP地址 : ", ip_addr.group())
    ip_city = get_city(ip_addr.group())
    print("IP城市 : ", ip_city)
else:
    print("可能是廣告信件沒有發文IP")


print("------------------------------------------------------------")  # 60個


# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch9\ch9_1.py

# ch9_1.py
import requests, bs4

url = "https://movies.yahoo.com.tw/movie_thisweek.html"  # 本周新片的網址
moviehtml = requests.get(url)
objSoup = bs4.BeautifulSoup(moviehtml.text, "lxml")  # 取得新片網址的HTML

movieNum = 0
items = objSoup.find_all("div", "release_info")  # 新片在此資料區間
for item in items:
    cName = item.find("div", "release_movie_name").a.text.strip()  # 中文片名
    eName = item.find("div", "en").a.text.strip()  # 英文片名
    movieNum += 1
    print("新片編號 : ", movieNum)
    print("中文片名 : ", cName)
    print("英文片名 : ", eName)
    print()


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch9\ch9_2.py

# ch9_2.py
import requests, bs4

url = "https://movies.yahoo.com.tw/movie_thisweek.html"  # 本周新片的網址
moviehtml = requests.get(url)
objSoup = bs4.BeautifulSoup(moviehtml.text, "lxml")  # 取得新片網址的HTML

movieNum = 0
items = objSoup.find_all("div", "release_info")  # 新片在此資料區間
for item in items:
    cName = item.find("div", "release_movie_name").a.text.strip()  # 中文片名
    eName = item.find("div", "en").a.text.strip()  # 英文片名
    rTime = item.find("div", "release_movie_time")  # 上映日期
    movieNum += 1
    print("新片編號 : ", movieNum)
    print("中文片名 : ", cName)
    print("英文片名 : ", eName)
    print(rTime.text)  # 列印上映日期
    print()


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch9\ch9_3.py

# ch9_3.py
import requests, bs4

url = "https://movies.yahoo.com.tw/movie_thisweek.html"  # 本周新片的網址
moviehtml = requests.get(url)
objSoup = bs4.BeautifulSoup(moviehtml.text, "lxml")  # 取得新片網址的HTML

movieNum = 0
items = objSoup.find_all("div", "release_info")  # 新片在此資料區間
for item in items:
    cName = item.find("div", "release_movie_name").a.text.strip()  # 中文片名
    eName = item.find("div", "en").a.text.strip()  # 英文片名
    rTime = item.find("div", "release_movie_time")  # 上映日期
    level = item.find("div", "leveltext").span.text.strip()  # 期待度
    movieNum += 1
    print("新片編號 : ", movieNum)
    print("中文片名 : ", cName)
    print("英文片名 : ", eName)
    print(rTime.text)  # 列印上映日期
    print("期待度   : ", level)
    print()


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch9\ch9_4.py

# ch9_4.py
import requests, bs4

url = "https://movies.yahoo.com.tw/movie_thisweek.html"  # 本周新片的網址
moviehtml = requests.get(url)
objSoup = bs4.BeautifulSoup(moviehtml.text, "lxml")  # 取得新片網址的HTML

movieNum = 0
items = objSoup.find_all("div", "release_info")  # 新片在此資料區間
for item in items:
    cName = item.find("div", "release_movie_name").a.text.strip()  # 中文片名
    eName = item.find("div", "en").a.text.strip()  # 英文片名
    rTime = item.find("div", "release_movie_time")  # 上映日期
    level = item.find("div", "leveltext").span.text.strip()  # 期待度
    txt = item.find("div", "release_text").text.strip()  # 內容摘要
    movieNum += 1
    print("新片編號 : ", movieNum)
    print("中文片名 : ", cName)
    print("英文片名 : ", eName)
    print(rTime.text)  # 列印上映日期
    print("期待度   : ", level)
    print("內容摘要 : ", txt)
    print()


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch9\ch9_5.py

# ch9_5.py
import requests, bs4, os

url = "https://movies.yahoo.com.tw/movie_thisweek.html"  # 本周新片的網址
moviehtml = requests.get(url)
objSoup = bs4.BeautifulSoup(moviehtml.text, "lxml")  # 取得新片網址的HTML

photos = []  # 放置劇照串列
items = objSoup.find_all("div", "release_foto")
for item in items:
    photo = item.a.img["src"]  # 取得劇照網址
    photos.append(photo)

destDir = "out9_5"
if os.path.exists(destDir) == False:  # 如果沒有此資料夾就建立
    os.mkdir(destDir)
print("搜尋到的圖片數量 = ", len(photos))  # 列出搜尋到的圖片數量
for photo in photos:  # 迴圈下載圖片與儲存
    picture = requests.get(photo)  # 下載圖片
    picture.raise_for_status()  # 驗證圖片是否下載成功
    print("%s 圖片下載成功" % photo)
    # 先開啟檔案, 再儲存圖片
    pictFile = open(os.path.join(destDir, os.path.basename(photo)), "wb")
    for diskStorage in picture.iter_content(10240):
        pictFile.write(diskStorage)
    pictFile.close()  # 關閉檔案


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch9\ch9_6.py

# ch9_6.py
import requests, bs4

url = "https://movies.yahoo.com.tw/movie_thisweek.html"  # 本周新片的網址
moviehtml = requests.get(url)
objSoup = bs4.BeautifulSoup(moviehtml.text, "lxml")  # 取得新片網址的HTML

movieNum = 0
items = objSoup.find_all("div", "release_info")  # 新片在此資料區間
for item in items:
    cName = item.find("div", "release_movie_name").a.text.strip()  # 中文片名
    eName = item.find("div", "en").a.text.strip()  # 英文片名
    photo = item.find_previous_sibling("div", "release_foto").a.img["src"]
    movieNum += 1
    print("新片編號 : ", movieNum)
    print("中文片名 : ", cName)
    print("英文片名 : ", eName)
    print("海報網址 : ", photo)
    print()


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch9\ch9_7.py

# ch9_7.py
import requests, bs4

url = "https://movies.yahoo.com.tw/movie_thisweek.html"  # 本周新片的網址
moviehtml = requests.get(url)
objSoup = bs4.BeautifulSoup(moviehtml.text, "lxml")  # 取得新片網址的HTML

movieNum = 0
items = objSoup.find_all("div", "release_info")  # 新片在此資料區間
for item in items:
    cName = item.find("div", "release_movie_name").a.text.strip()  # 中文片名
    eName = item.find("div", "en").a.text.strip()  # 英文片名
    photo = item.find_previous_sibling("div", "release_foto").a.img["src"]
    video = item.find("div", "release_btn color_btnbox").find_all("a")[1]
    if "href" in video.attrs:  # 檢查預告片是否存在
        video = video["href"]
    else:
        video = ""

    movieNum += 1
    print("新片編號 : ", movieNum)
    print("中文片名 : ", cName)
    print("英文片名 : ", eName)
    print("海報網址 : ", photo)
    print("預告片   : ", video)
    print()


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch9\ch9_8.py

# ch9_8.py
import requests, bs4

url = "https://movies.yahoo.com.tw/chart.html"  # 本周排行榜的網址
moviehtml = requests.get(url)
objSoup = bs4.BeautifulSoup(moviehtml.text, "lxml")  # 取得排行榜的HTML

itemsobj = objSoup.find("ul", "ranking_list_r")  # 排行榜在此資料區間
items = itemsobj.find_all("li")
print("台北本週票房排行榜\n")
for item in items:
    name = item.span.text
    rank = item.find("div", "num")
    print("片名 : ", name)
    print("名次 : ", rank.text)
    print()


print("------------------------------------------------------------")  # 60個


# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch10\ch10_1.py

# ch10_1.py
import requests, bs4

url = "https://tw.appledaily.com/hot/daily"
applehtml = requests.get(url)
objSoup = bs4.BeautifulSoup(applehtml.text, "lxml")  # 取得HTML

items = objSoup.find("ul", "all").find_all("li")
for item in items:
    if item.find("div", "aht_title_num atopred"):  # 前10條是紅色
        num = item.find("div", "aht_title_num atopred").text
    else:
        num = item.find("div", "aht_title_num").text  # 其它則黑色色
    txt = item.find("div", "aht_title").text
    print("新聞編號 : ", num)
    print(txt)


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch10\ch10_2.py

# ch10_2.py
import requests, bs4

url = "https://udn.com/news/cate/2/7225"  # 全球頭條新聞
newshtml = requests.get(url)
objSoup = bs4.BeautifulSoup(newshtml.text, "lxml")  # 取得HTML
items = objSoup.find("div", "area")
print(type(items))
print(items)


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch10\ch10_3.py

# ch10_3.py
import requests, bs4

url = "https://udn.com/news/cate/2/7225"  # 全球頭條新聞
newshtml = requests.get(url)
objSoup = bs4.BeautifulSoup(newshtml.text, "lxml")  # 取得HTML
items = objSoup.find("div", "area")
items = items.find_all("div", "ms-info")
for item in items:
    txt = item.h1.text
    print(txt)
    print()


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch10\ch10_4.py

# ch10_4.py
import requests, bs4

url = "https://money.udn.com/money/cate/5591"  # 經濟日報新聞
newshtml = requests.get(url)
objSoup = bs4.BeautifulSoup(newshtml.text, "lxml")  # 取得HTML
itemobj = objSoup.find("div", "category_box_list author")
items = itemobj.find_all("dt", "more_5612")
for item in items:
    txt = item.a.text.strip()
    print(txt)


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch10\ch10_5.py

# ch10_5.py
import requests, bs4

url = "https://www.chinatimes.com/world/?chdtv"
newshtml = requests.get(url)  # 中國時報新聞
objSoup = bs4.BeautifulSoup(newshtml.text, "lxml")  # 取得HTML
itemobj = objSoup.find("section", "hot-news")
itemobj = itemobj.find("ol", "vertical-list")
items = itemobj.find_all("li")
for item in items:
    txt = item.h4.text
    print(txt)


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch10\ch10_6.py

# ch10_6.py
import requests, bs4

url = "https://www.chinatimes.com/newspapers/2602?chdtv"
newshtml = requests.get(url)  # 工商時報熱門新聞
objSoup = bs4.BeautifulSoup(newshtml.text, "lxml")  # 取得HTML
itemobj = objSoup.find("section", "hot-news")
print(itemobj.h4.text, "\n")  # 熱門新聞標題
itemobj = itemobj.find("ol", "vertical-list")
items = itemobj.find_all("li")
for item in items:
    txt = item.h4.text
    print(txt)


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch11\ch11_1.py

# ch11_1.py
import sqlite3

conn = sqlite3.connect("myData.db")
conn.close()


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch11\ch11_2.py

# ch11_2.py
import sqlite3

conn = sqlite3.connect("data11_2.db")  # 資料庫連線
cursor = conn.cursor()
sql = """Create table students(  
        id int,
        name text,
        gender text)"""
cursor.execute(sql)  # 執行SQL指令
cursor.close()  # 關閉
conn.close()  # 關閉資料庫連線


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch11\ch11_3.py

# ch11_3.py
import sqlite3

conn = sqlite3.connect("myInfo.db")  # 資料庫連線
sql = """Create table students(  
        id int,
        name text,
        gender text)"""
conn.execute(sql)  # 執行SQL指令
conn.close()  # 關閉資料庫連線


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch11\ch11_3_1.py

# ch11_3_1.py
import sqlite3

conn = sqlite3.connect("myInfo2.db")  # 資料庫連線
sql = """Create table student2(  
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        gender TEXT)"""
conn.execute(sql)  # 執行SQL指令
conn.close()  # 關閉資料庫連線


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch11\ch11_4.py

# ch11_4.py
import sqlite3

conn = sqlite3.connect("myInfo.db")  # 資料庫連線
print("請輸入myInfo資料庫students表單資料")
while True:
    new_id = int(input("請輸入id : "))  # 轉成整數
    new_name = input("請輸入name : ")
    new_gender = input("請輸入gender : ")
    x = (new_id, new_name, new_gender)
    sql = """insert into students values(?,?,?)"""
    conn.execute(sql, x)
    conn.commit()  # 更新資料庫
    again = input("繼續(y/n)? ")
    if again[0].lower() == "n":
        break
conn.close()  # 關閉資料庫連線


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch11\ch11_4_1.py

# ch11_4_1.py
import sqlite3

conn = sqlite3.connect("myInfo2.db")  # 資料庫連線
print("請輸入myInfo資料庫student2表單資料")
while True:
    n_name = input("請輸入name : ")
    n_gender = input("請輸入gender : ")
    x = (n_name, n_gender)
    sql = """insert into student2(name, gender) values(?,?)"""
    conn.execute(sql, x)
    conn.commit()  # 更新資料庫
    again = input("繼續(y/n)? ")
    if again[0].lower() == "n":
        break
conn.close()  # 關閉資料庫連線


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch11\ch11_5.py

# ch11_5.py
import sqlite3

conn = sqlite3.connect("myInfo.db")  # 資料庫連線
results = conn.execute("SELECT * from students")
for record in results:
    print("id = ", record[0])
    print("name = ", record[1])
    print("gender = ", record[2])
conn.close()  # 關閉資料庫連線


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch11\ch11_5_1.py

# ch11_5_1.py
import sqlite3

conn = sqlite3.connect("myInfo2.db")  # 資料庫連線
results = conn.execute("SELECT * from student2")
for record in results:
    print("id = ", record[0])
    print("name = ", record[1])
    print("gender = ", record[2])
conn.close()  # 關閉資料庫連線


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch11\ch11_6.py

# ch11_6.py
import sqlite3

conn = sqlite3.connect("myInfo.db")  # 資料庫連線
results = conn.execute("SELECT * from students")
allstudents = results.fetchall()  # 結果轉成元素是元組的串列
for student in allstudents:
    print(student)
conn.close()  # 關閉資料庫連線


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch11\ch11_7.py

# ch11_7.py
import sqlite3

conn = sqlite3.connect("myInfo.db")  # 資料庫連線
results = conn.execute("SELECT name from students")
allstudents = results.fetchall()  # 結果轉成元素是元組的串列
for student in allstudents:
    print(student)
conn.close()  # 關閉資料庫連線


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch11\ch11_8.py

# ch11_8.py
import sqlite3

conn = sqlite3.connect("myInfo.db")  # 資料庫連線
sql = '''SELECT name, gender
        from students
        where gender = "F"'''
results = conn.execute(sql)
allstudents = results.fetchall()  # 結果轉成元素是元組的串列
for student in allstudents:
    print(student)
conn.close()  # 關閉資料庫連線


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch11\ch11_9.py

# ch11_9.py
import sqlite3

conn = sqlite3.connect("myInfo.db")  # 資料庫連線
sql = """UPDATE students
        set name = "Tomy"
        where id = 1"""
results = conn.execute(sql)
conn.commit()  # 更新資料庫
results = conn.execute("SELECT name from students")
allstudents = results.fetchall()  # 結果轉成元素是元組的串列
for student in allstudents:
    print(student)
conn.close()  # 關閉資料庫連線


print("------------------------------------------------------------")  # 60個


# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch11\ch11_10.py

# ch11_10.py
import sqlite3

conn = sqlite3.connect("myInfo.db")  # 資料庫連線
sql = """DELETE
        from students
        where id = 2"""
results = conn.execute(sql)
conn.commit()  # 更新資料庫
results = conn.execute("SELECT name from students")
allstudents = results.fetchall()  # 結果轉成元素是元組的串列
for student in allstudents:
    print(student)
conn.close()  # 關閉資料庫連線


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch11\ch11_11.py

# ch11_11.py
import sqlite3
import csv
import matplotlib.pyplot as plt

conn = sqlite3.connect("populations.db")  # 資料庫連線
sql = """Create table population( 
        area TEXT,
        male int,                     
        female int,
        total int)"""
conn.execute(sql)  # 執行SQL指令

fn = "Taipei_Population.csv"
with open(fn) as csvFile:  # 儲存在SQLite
    csvReader = csv.reader(csvFile)
    listCsv = list(csvReader)  # 轉成串列
    csvData = listCsv[4:]  # 切片刪除前4 rows
    for row in csvData:
        area = row[0]  # 區名稱
        male = int(row[7])  # 男性人數
        female = int(row[8])  # 女性人數
        total = int(row[6])  # 總人數
        x = (area, male, female, total)
        sql = """insert into population values(?,?,?,?)"""
        conn.execute(sql, x)
        conn.commit()

results = conn.execute("SELECT * from population")
for record in results:
    print("區域       = ", record[0])
    print("男性人口數 = ", record[1])
    print("女性人口數 = ", record[2])
    print("總計人口數 = ", record[3])

conn.close()  # 關閉資料庫連線


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch11\ch11_12.py

# ch11_12.py
import sqlite3
import matplotlib.pyplot as plt
from pylab import mpl

conn = sqlite3.connect("populations.db")  # 資料庫連線
results = conn.execute("SELECT * from population")

area, male, female, total = [], [], [], []
for record in results:  # 將人口資料放入串列
    area.append(record[0])
    male.append(record[1])
    female.append(record[2])
    total.append(record[3])
conn.close()  # 關閉資料庫連線

mpl.rcParams["font.sans-serif"] = ["SimHei"]  # 使用黑體
seq = area
(linemale,) = plt.plot(seq, male, "-*", label="男性人口數")
(linefemale,) = plt.plot(seq, female, "-o", label="女性人口數")
(linetotal,) = plt.plot(seq, total, "-^", label="總計人口數")

plt.legend(handles=[linemale, linefemale, linetotal], loc="best")
plt.title("台北市", fontsize=24)
plt.xlabel("2019年", fontsize=14)
plt.ylabel("人口數", fontsize=14)
plt.show()


print("------------------------------------------------------------")  # 60個


# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch12\ch12_1.py

# ch12_1.py
import csv
import matplotlib.pyplot as plt
from datetime import datetime

fn = "ST43_3083_201907.csv"
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    listCsv = list(csvReader)  # 轉成串列
    csvData = listCsv[5:-1]  # 切片刪除非成交資訊
    dates, highs, lows, prices = [], [], [], []  # 設定空串列
    for row in csvData:
        try:
            datestr = row[0].replace("108", "2019")
            currentDate = datetime.strptime(datestr, "%Y/%m/%d")
            high = float(row[4])  # 設定最高價
            low = float(row[5])  # 設定最低價
            price = float(row[6])  # 設定收盤價
        except Exception:
            print("有缺值")
        else:
            highs.append(high)  # 儲存最高價
            lows.append(low)  # 儲存最低價
            prices.append(price)  # 儲存收盤價
            dates.append(currentDate)  # 儲存日期

fig = plt.figure(dpi=80, figsize=(12, 8))  # 設定繪圖區大小
plt.plot(dates, highs, "-*", label="High")  # 繪製最高價
plt.plot(dates, lows, "-o", label="Low")  # 繪製最低價
plt.plot(dates, prices, "-^", label="Price")  # 繪製收盤價
plt.legend(loc="best")
fig.autofmt_xdate()  # 日期旋轉
plt.title("Stock 3083, July 2019", fontsize=24)
plt.xlabel("", fontsize=14)
plt.ylabel("Price", fontsize=14)
plt.tick_params(axis="both", labelsize=12, color="red")
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch12\ch12_2.py

# ch12_2.py
import csv
import matplotlib.pyplot as plt
from datetime import datetime

fn = "FMNPTK.csv"
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    listCsv = list(csvReader)  # 轉成串列
    csvData = listCsv[2:-5]  # 切片刪除非成交資訊
    years, highs, lows, prices = [], [], [], []  # 設定空串列
    for row in csvData:
        try:
            year = int(row[0]) + 1911
            high = float(row[4])  # 設定最高價
            low = float(row[6])  # 設定最低價
            price = float(row[8])  # 設定收盤平均價
        except Exception:
            print("有缺值")
        else:
            highs.append(high)  # 儲存最高價
            lows.append(low)  # 儲存最低價
            prices.append(price)  # 儲存收盤平均價
            years.append(year)  # 儲存日期

fig = plt.figure(dpi=80, figsize=(12, 8))  # 設定繪圖區大小
plt.plot(years, highs, "-*", label="High")  # 繪製最高價
plt.plot(years, lows, "-o", label="Low")  # 繪製最低價
plt.plot(years, prices, "-^", label="Price")  # 繪製收盤平均價
plt.legend(loc="best")
fig.autofmt_xdate()  # 日期旋轉
plt.title("Taiwan Cement Company", fontsize=24)
plt.xlabel("", fontsize=14)
plt.ylabel("Price", fontsize=14)
plt.tick_params(axis="both", labelsize=12, color="red")
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch12\ch12_3.py

# ch12_3.py
import csv

fn = "MI_5MINS.csv"  # 台灣證劵交易所資料
out = "MI_30MINS.csv"  # 每30分鐘資料
with open(out, "w", newline="") as csvOut:
    csvWriter = csv.writer(csvOut)
    csvWriter.writerow(["時間", "累積成交數"])
    with open(fn) as csvFile:
        csvReader = csv.reader(csvFile)
        listCsv = list(csvReader)  # 轉成串列
        csvData = listCsv[2:-8]  # 切片刪除非成交資訊
        for row in csvData:
            xmin = row[0][3:5]  # 分
            xsec = row[0][6:]  # 秒
            if xmin == "00" or xmin == "30":  # 每30分鐘
                if xsec == "00":  # True時寫入時間和累積成交數
                    csvWriter.writerow([row[0], row[6]])


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch12\ch12_4.py

# ch12_4.py
import csv
import matplotlib.pyplot as plt
from datetime import datetime

fn = "MI_30MINS.csv"
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    listCsv = list(csvReader)  # 轉成串列
    csvData = listCsv[1:]  # 切片刪除非成交資訊
    times, items = [], []  # 設定空串列
    for row in csvData:
        try:
            time = row[0]  # 時間
            item = row[1]  # 累積成交數
        except Exception:
            print("有缺值")
        else:
            times.append(time)  # 儲存時間
            items.append(item)  # 儲存累積成交數

fig = plt.figure(dpi=80, figsize=(12, 8))  # 設定繪圖區大小
plt.plot(times, items, "-*")  # 繪製累積成交數
fig.autofmt_xdate()  # 時間旋轉
plt.title("Accumulated deal every 30 minutes", fontsize=24)
plt.xlabel("", fontsize=14)
plt.ylabel("Accumulated deal", fontsize=14)
plt.tick_params(axis="both", labelsize=12, color="red")
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch12\ch12_5.py

# ch12_5.py
import requests, bs4

url = "https://www.google.com/search?q=TPE:1101"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
            Safari/537.36",
}
newshtml = requests.get(url, headers=headers)  # 台灣水泥
objSoup = bs4.BeautifulSoup(newshtml.text, "lxml")  # 取得HTML
gcards = objSoup.find_all("g-card-section")
company = gcards[1].div
company = company.find("div", "oPhL2e")  # 取得公司名稱
print(company.text)
spans = gcards[1].find_all("div", recursive=False)[1]  # False只搜尋第一層
info = spans.find_all("span", recursive=False)  # False只搜尋第一層
price = info[0].text
change = info[1].text
print("收盤價 = ", price)
print("帳跌   = ", change)
for table in gcards[3].find_all("table"):
    for row in table.find_all("tr")[:3]:
        key = row.find_all("td")[0].text
        value = row.find_all("td")[1].text
        print(key, "=", value)


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch12\ch12_6.py

# ch12_6.py
import requests, bs4

url = "https://tw.stock.yahoo.com/q/q?s=2330"

newshtml = requests.get(url)  # 台積電
objSoup = bs4.BeautifulSoup(newshtml.text, "lxml")  # 取得HTML

tables = objSoup.find_all("table")
table1 = tables[1].find_all("th")  # 表頭
for t_head in table1:
    print(t_head.text)
table2 = tables[2].find_all("td")  # 表格值
print("------------------------------")
for t_info in table2:
    print(t_info.text)


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch12\ch12_7.py

# ch12_7.py
import twstock

stock2330 = twstock.Stock("2330")

print("股票代號   : ", stock2330.sid)
print("股票收盤價 : ", stock2330.price)


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch12\ch12_8.py

# ch12_8.py
import matplotlib.pyplot as plt
from pylab import mpl
import twstock

mpl.rcParams["font.sans-serif"] = ["SimHei"]  # 使用黑體

stock2330 = twstock.Stock("2330")
plt.title("台積電", fontsize=24)
plt.plot(stock2330.price)
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch12\ch12_9.py

# ch12_9.py
import matplotlib.pyplot as plt
from pylab import mpl
import twstock

mpl.rcParams["font.sans-serif"] = ["SimHei"]  # 使用黑體

stock2330 = twstock.Stock("2330")
stock2330.fetch_from(2018, 1)
plt.title("台積電", fontsize=24)
plt.xlabel("2018年1月以來的交易天數", fontsize=14)
plt.ylabel("價格", fontsize=14)
plt.plot(stock2330.price)
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch12\ch12_10.py

# ch12_10.py
import pandas as pd
import twstock

stock2330 = twstock.realtime.get("2330")
buyPrice = stock2330["realtime"]["best_bid_price"]
buyNum = stock2330["realtime"]["best_bid_volume"]

selPrice = stock2330["realtime"]["best_ask_price"]
selNum = stock2330["realtime"]["best_ask_volume"]

dict2330 = {"BVolumn": buyNum, "Buy": buyPrice, "Sell": selPrice, "SVolumn": selNum}

df2330 = pd.DataFrame(dict2330, index=range(1, 6))
print("台積電最佳五檔價量表")
print(df2330)


print("------------------------------------------------------------")  # 60個


# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch13\ch13_1.py

# ch13_1.py
import requests

url = "http://www.taiwanrate.com/"
htmlfile = requests.get(url)
print("HTML編碼方式 : ", htmlfile.encoding)
print("列印網頁內容 \n", htmlfile.text)


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch13\ch13_2.py

# ch13_2.py
import requests

url = "http://www.taiwanrate.com/"
htmlfile = requests.get(url)
print("HTML編碼方式 : ", htmlfile.encoding)
htmlfile.encoding = "utf-8"  # 編碼改為utf-8
print("更改編碼")
print("HTML編碼方式 : ", htmlfile.encoding)
print("列印網頁內容 \n", htmlfile.text)


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch13\ch13_3.py

# ch13_3.py
import requests, bs4

url = "http://www.taiwanrate.com/"
htmlfile = requests.get(url)
htmlfile.encoding = "utf-8"  # 轉成utf-8
objSoup = bs4.BeautifulSoup(htmlfile.text, "lxml")  # 取得物件
ratetable = objSoup.find_all("table")
# 列印表格欄位名稱
lefttop = ratetable[4].find("tr").find("tr").find("td")  # 第4個表格
print(lefttop.text, end=" ")  # 左上角內容
ratehead = ratetable[4].find("tr").find_all("a", "bodytablehead")
for head in ratehead:
    print(head.text, end=" ")  # 列出其它欄位名稱
# 以上是列印表格欄位名稱
print()
# 以下是列印各銀行利率, 先找出第一個class='bodytabletr1'
ratetd = ratetable[4].find("tr", "bodytabletr1")
print(ratetd.text)  # 列出第一家銀行
while ratetd.find_next_sibling("tr"):
    ratetd = ratetd.find_next_sibling("tr")
    print(ratetd.text)  # 列出其它家銀行


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch13\ch13_4.py

# ch13_4.py
import requests, bs4
import csv

fn = "out13_4.csv"
tablelist = []  # 利率表串列
headlist = []
ratelist = []
url = "http://www.taiwanrate.com/"
htmlfile = requests.get(url)
htmlfile.encoding = "utf-8"  # 轉成utf-8
objSoup = bs4.BeautifulSoup(htmlfile.text, "lxml")  # 取得物件
ratetable = objSoup.find_all("table")
# 列印表格欄位名稱
lefttop = ratetable[4].find("tr").find("tr").find("td")  # 第4個表格
headlist.append(lefttop.text)  # 加入欄位名稱串列
ratehead = ratetable[4].find("tr").find_all("a", "bodytablehead")
for head in ratehead:
    headlist.append(head.text)  # 加入欄位名稱串列
tablelist.append(headlist)  #
# 以上是列印表格欄位名稱
# 以下是列印各銀行利率, 先找出第一個class='bodytabletr1'
ratetd = ratetable[4].find("tr", "bodytabletr1")  # 找出第一筆利率
for row in ratetd:
    ratelist.append(row.text)
tablelist.append(ratelist)  # 將第一筆銀行利率加入
while ratetd.find_next_sibling("tr"):  # 找出其他銀行利率
    ratetd = ratetd.find_next_sibling("tr")
    ratelist = []
    for row in ratetd:
        ratelist.append(row.text)
    tablelist.append(ratelist)  # 加入其它家銀行利率

with open(fn, "w", newline="") as csvFile:  # 寫入out13_4.csv
    csvWriter = csv.writer(csvFile)
    for row in tablelist:
        csvWriter.writerow(row)  # 一次寫一筆


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch13\ch13_5.py

# ch13_5.py
import csv
import pandas as pd

fn = "out13_4.csv"
with open(fn) as csvFile:  # 開啟csv檔案
    csvReader = csv.reader(csvFile)  # 讀檔案建立Reader物件
    listReport = list(csvReader)  # 將資料轉成串列

for row in listReport:  # 將'-'改為'0'
    while "-" in row:
        i = row.index("-")
        row[i] = "0"

time_period = listReport[0]  # 將第一個串列改為columns
time_period = time_period[1:]

listReport = listReport[1:]  # 切片

bank = []
newReport = []
for row in listReport:  # 取得index
    bank.append(row[0])
    newReport.append(row[1:])  # 建立新利率串列

df = pd.DataFrame(newReport, columns=time_period, index=bank)

print(df)


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch13\ch13_6.py

# ch13_6.py
import requests, bs4

url = "https://www.moneydj.com/funddj/ya/YP401000.djhtm"
htmlfile = requests.get(url)
objSoup = bs4.BeautifulSoup(htmlfile.text, "lxml")  # 取得物件
fundtable = objSoup.find("table", id="oMainTable")
# 抓標題
objhead = fundtable.find("tr", id="oScrollMenu")
heads = objhead.find_all("th")
for head in heads:
    print(head.text.strip())


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch13\ch13_7.py

# ch13_7.py
import requests, bs4

url = "https://www.moneydj.com/funddj/ya/YP401000.djhtm"
htmlfile = requests.get(url)
objSoup = bs4.BeautifulSoup(htmlfile.text, "lxml")  # 取得物件
fundtable = objSoup.find("table", id="oMainTable")
# 抓標題
objhead = fundtable.find("tr", id="oScrollMenu")
heads = objhead.find_all("th")
for head in heads:  # 輸出基金表格標題
    print(head.text.strip(), " ", end="")
print()
# 抓基金表格資料
objtable = fundtable.find("tbody")
tables = objtable.find_all("tr")
for table in tables:  # 輸出各基金績效
    rowtext = table.text.strip()
    txt = rowtext.split("\n")  # 將字串轉成串列
    print(txt)


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch13\ch13_8.py

# ch13_8.py
import requests, bs4
import csv

fn = "out13_8.csv"
tablelist = []
headlist = []
url = "https://www.moneydj.com/funddj/ya/YP401000.djhtm"
htmlfile = requests.get(url)
objSoup = bs4.BeautifulSoup(htmlfile.text, "lxml")  # 取得物件
fundtable = objSoup.find("table", id="oMainTable")
# 抓標題
objhead = fundtable.find("tr", id="oScrollMenu")
heads = objhead.find_all("th")
for head in heads:  # 輸出基金表格標題
    headlist.append(head.text)
tablelist.append(headlist)
# 抓基金表格資料
objtable = fundtable.find("tbody")
tables = objtable.find_all("tr")
for table in tables:  # 輸出各基金績效
    rowtext = table.text.strip()
    txt = rowtext.split("\n")  # 將字串轉成串列
    tablelist.append(txt)
# 寫入csv
with open(fn, "w", newline="") as csvFile:  # 寫入out13_8.csv
    csvWriter = csv.writer(csvFile)
    for row in tablelist:
        csvWriter.writerow(row)  # 一次寫一筆


print("------------------------------------------------------------")  # 60個


# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch14\ch14_1.py

# ch14_1.py
import requests, bs4

# url = 'https://www.dcard.tw/f?latest=false'                # 這個URL也可以
url = "https://www.dcard.tw/f"
htmlfile = requests.get(url)
objSoup = bs4.BeautifulSoup(htmlfile.text, "lxml")  # 取得物件
items = objSoup.find_all("div", "PostList_entry_1rq5Lf")
print(items[0].h3.text)  # 列出第1篇貼文標題
print(items[1].h3.text)  # 列出第3篇貼文標題


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch14\ch14_2.py

# ch14_2.py
import requests, bs4

# url = 'https://www.dcard.tw/f?latest=false'                # 這個URL也可以
url = "https://www.dcard.tw/f"
htmlfile = requests.get(url)
objSoup = bs4.BeautifulSoup(htmlfile.text, "lxml")  # 取得物件
items = objSoup.find_all("div", "PostList_entry_1rq5Lf")
print(items[0].h3.text)  # 列出第1篇貼文標題
print(items[1].h3.text)  # 列出第2篇貼文標題


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch14\ch14_3.py

# ch14_3.py
import requests, bs4

# url = 'https://www.dcard.tw/f?latest=false'                # 這個URL也可以
url = "https://www.dcard.tw/f"
htmlfile = requests.get(url)
objSoup = bs4.BeautifulSoup(htmlfile.text, "lxml")  # 取得物件
items = objSoup.find_all("div", "PostList_entry_1rq5Lf")
try:
    print(items[0].h3.text)  # 列出第1篇貼文標題
    print(items[1].h3.text)  # 列出第2篇貼文標題
except UnicodeEncodeError:
    print("UnicodeEncodeError")


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch14\ch14_4.py

# ch14_4.py
import requests, bs4

# url = 'https://www.dcard.tw/f?latest=false'                # 這個URL也可以
url = "https://www.dcard.tw/f"
htmlfile = requests.get(url)
objSoup = bs4.BeautifulSoup(htmlfile.text, "lxml")  # 取得物件
try:
    items = objSoup.find_all("div", "PostList_entry_1rq5Lf")
    header = items[0].find("span", "bOzcuu")
    print("貼文論壇 : ", header.text)
    author = items[0].find("span", "PostAuthor_root_3vAJfe")
    print("貼文學校 : ", author.text)
    time = items[0].find("span", "MDszy")
    print("貼文時間 : ", time.text)
    print("貼文標題 : ", items[0].h3.text)
except UnicodeEncodeError:
    print("UnicodeEncodeError")


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch14\ch14_5.py

# ch14_5.py
import requests, bs4

# url = 'https://www.dcard.tw/f?latest=false'                # 這個URL也可以
url = "https://www.dcard.tw/f"
htmlfile = requests.get(url)
objSoup = bs4.BeautifulSoup(htmlfile.text, "lxml")  # 取得物件
try:
    items = objSoup.find_all("div", "PostList_entry_1rq5Lf")
    header = items[0].find("span", "bOzcuu")
    print("貼文論壇 : ", header.text)
    author = items[0].find("span", "PostAuthor_root_3vAJfe")
    print("貼文學校 : ", author.text)
    time = items[0].find("span", "MDszy")
    print("貼文時間 : ", time.text)
    print("貼文標題 : ", items[0].h3.text)
    print("貼文內容 : ", items[0].text)
    bookmark = items[0].find("div", "cGEHtj")
    print("按讚人數 : ", bookmark.text)
    spanmark = items[0].find("span", "hkpJwJ")
    print("貼文回應 : ", spanmark.text)
    link = items[0].find("a")["href"]
    print("貼文連結 : ", link)
except UnicodeEncodeError:
    print("UnicodeEncodeError")


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch14\ch14_6.py

# ch14_6.py
import requests, bs4

# url = 'https://www.dcard.tw/f?latest=false'                # 這個URL也可以
url = "https://www.dcard.tw/f"
htmlfile = requests.get(url)
objSoup = bs4.BeautifulSoup(htmlfile.text, "lxml")  # 取得物件
items = objSoup.find_all("div", "PostList_entry_1rq5Lf")
print("取得文章數量 = ", len(items))
for item in items:
    try:
        header = item.find("span", "bOzcuu")
        print(header.text, "  ", end="")
        author = item.find("span", "PostAuthor_root_3vAJfe")
        print(author.text, "", end="")
        time = item.find("span", "MDszy")
        print(time.text)
        print(item.h3.text)
        print(item.text)
        bookmark = item.find("div", "cGEHtj")
        print(bookmark.text)
        spanmark = item.find("span", "hkpJwJ")
        print(spanmark.text)
        link = item.find("a")["href"]
        print(link)
    except UnicodeEncodeError:
        print("UnicodeEncodeError")
    print()


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch14\ch14_7.py

# ch14_7.py
import requests, bs4, json

url = "https://www.dcard.tw/"
api = "_api/posts?popular=true"
url_popular = url + api
posts = list(requests.get(url_popular).json())
try:
    print("id   : ", posts[0]["id"])
    print("標題 : ", posts[0]["title"])
    print("內文 : ", posts[0]["excerpt"])
    print("按讚 : ", posts[0]["likeCount"])
    print("回應 : ", posts[0]["commentCount"])
except UnicodeEncodeError:
    print("UnicodeEncodeError")


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch14\ch14_8.py

# ch14_8.py
import requests, bs4, json

url = "https://www.dcard.tw/"
api = "_api/posts?popular=true"
url_popular = url + api
posts = list(requests.get(url_popular).json())
print(len(posts))
for post in posts:
    try:
        print("id   : ", post["id"])
        print("標題 : ", post["title"])
        print("內文 : ", post["excerpt"])
        print("按讚 : ", post["likeCount"])
        print("回應 : ", post["commentCount"])
    except UnicodeEncodeError:
        print("UnicodeEncodeError")


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch14\ch14_9.py

# ch14_9.py
import requests, bs4, json


def printing():  # 列印熱門貼文
    global counter
    for post in posts:
        try:
            counter += 1
            print("貼文熱門編號 : ", counter)
            print("id           : ", post["id"])
            print("標題         : ", post["title"])
            print("內文         : ", post["excerpt"])
            print("按讚         : ", post["likeCount"])
            print("回應         : ", post["commentCount"])
        except UnicodeEncodeError:
            print("UnicodeEncodeError")


url = "https://www.dcard.tw/"
api = "_api/posts?popular=true"
url_popular = url + api
posts = list(requests.get(url_popular).json())
counter = 0
printing()  # 印第1組前30熱門
last_id = posts[-1]["id"]  # 第1組最後一筆熱門id
num_page = 2
for i in range(num_page):  # 印第2-3組前30熱門
    posts = list(requests.get(url_popular + "&before=" + str(last_id)).json())
    printing()
    last_id = posts[-1]["id"]  # 最後一筆熱門的id


print("------------------------------------------------------------")  # 60個


# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch15\ch15_1.py

# ch15_1.py
import requests, bs4

url = "http://www.xzw.com/fortune/"
htmlfile = requests.get(url)
objSoup = bs4.BeautifulSoup(htmlfile.text, "lxml")  # 取得物件
constellation = objSoup.find("div", id="list")
print(constellation.find("h1").text)  # 標題
con = constellation.find("dd").find("strong")  # 星座
print(con.text)
dateofbirth = constellation.find("dd").find("small")  # 出生日期
print(dateofbirth.text)
fortune = constellation.find("dd").find("span")  # 整體運勢
print(fortune.text)
txt = constellation.find("dd").find("p")  # 簡略說明
print(txt.text)


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch15\ch15_2.py

# ch15_2.py
import requests, bs4

url = "http://www.xzw.com/fortune/"
htmlfile = requests.get(url)
objSoup = bs4.BeautifulSoup(htmlfile.text, "lxml")  # 取得物件
constellation = objSoup.find("div", id="list")
print(constellation.find("h1").text)  # 標題
cons = constellation.find("div", "alb").find_all("div")
for con in cons:
    c = con.find("dd").find("strong")  # 星座
    print(c.text)
    dateofbirth = con.find("dd").find("small")  # 出生日期
    print(dateofbirth.text)
    forturn = con.find("dd").find("span")  # 整體運勢
    print(forturn.text)
    txt = con.find("dd").find("p")  # 簡略說明
    print(txt.text)


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python網路爬蟲_王者歸來\ch15\ch15_3.py

# ch15_3.py
import requests, bs4, os

url = "http://www.xzw.com/fortune/"
htmlfile = requests.get(url)
objSoup = bs4.BeautifulSoup(htmlfile.text, "lxml")  # 取得物件
constellation = objSoup.find("div", id="list")
cons = constellation.find("div", "alb").find_all("div")

pict_url = "http://www.xzw.com"
photos = []
for con in cons:
    pict = con.a.img["src"]
    photos.append(pict_url + pict)

destDir = "out15_3"
if os.path.exists(destDir) == False:  # 如果沒有此資料夾就建立
    os.mkdir(destDir)
print("搜尋到的圖片數量 = ", len(photos))  # 列出搜尋到的圖片數量
for photo in photos:  # 迴圈下載圖片與儲存
    picture = requests.get(photo)  # 下載圖片
    picture.raise_for_status()  # 驗證圖片是否下載成功
    print("%s 圖片下載成功" % photo)
    # 先開啟檔案, 再儲存圖片
    pictFile = open(os.path.join(destDir, os.path.basename(photo)), "wb")
    for diskStorage in picture.iter_content(10240):
        pictFile.write(diskStorage)
    pictFile.close()  # 關閉檔案


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
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
