print('------------------------------------------------------------')	#60個


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

print("------------------------------------------------------------")  # 60個

import string

str1 = "#$%^Python -is- *a* $%programming_ language.$"

print(string.punctuation)
list1 = str1.split(" ")
for item in list1:
    print(item.strip(string.punctuation))

print("------------------------------------------------------------")  # 60個

baseUrl = "http://example.com"
list1 = ["http://www.example.com/test", "http://example.com/word",
         "media/ex.jpg", "http://www.example.com/index.html"]

def getUrl(baseUrl, source):
    if source.startswith("http://www."):
        url = "http://" + source[11:]
    elif source.startswith("http://"):
        url = source
    elif source.startswith("www"):
        url = source[4:]
        url = "http://" + source
    else:
        url = baseUrl + "/" + source
        
    if baseUrl not in url:
        return None
    return url

for item in list1:
    print(getUrl(baseUrl, item))

print("------------------------------------------------------------")  # 60個

import re

str1 = "  Python, is   a, \nprogramming, \n\nlanguage.\n\r   "

list1 = str1.split(",")
for item in list1:
    item = re.sub(r"\n+", "", item)
    item = re.sub(r" +", " ", item)
    item = item.strip()
    print("'" + item + "'")
    

print("------------------------------------------------------------")  # 60個

import re

list1 = ["", "/", "path/", "/path", "/path/", "//path/", "/path///"]

def getPath(path):
    if path:
        if path[0] != "/":
            path = "/" + path
        if path[-1] != "/":
            path = path + "/"
        path = re.sub(r"/{2,}", "/", path)
    else:
        path = "/"
        
    return path

for item in list1:
    item = getPath(item)
    print(item)

print("------------------------------------------------------------")  # 60個

import requests
from bs4 import BeautifulSoup
import csv

url = "https://fchart.github.io/ML/table.html"
csvfile = "tmp_CompanySales.csv"
r = requests.get(url)
r.encoding = "utf8"
soup = BeautifulSoup(r.text, "lxml")
tag_table = soup.find(class_="tt")  # 找到<table>
rows = tag_table.findAll("tr")   # 找出所有<tr>
# 開啟CSV檔案寫入截取的資料
with open(csvfile, 'w+', newline='', encoding="utf-8") as fp:
    writer = csv.writer(fp)
    for row in rows:
        rowList = []
        for cell in row.findAll(["td", "th"]):
            rowList.append(cell.get_text().replace("\n", "").replace("\r", ""))
        writer.writerow(rowList)

print("------------------------------------------------------------")  # 60個

import requests

url = "https://fchart.github.io/img/fchart03.png"
path = "tmp_fchart03.png"
response = requests.get(url, stream=True)
if response.status_code == 200:
    with open(path, 'wb') as fp:
        for chunk in response:
            fp.write(chunk)
    print("圖檔已經下載")        
else:
    print("錯誤! HTTP請求失敗...")
    

print("------------------------------------------------------------")  # 60個

import urllib.request

url = "https://fchart.github.io/img/fchart03.png"
response = urllib.request.urlopen(url)
fp = open("tmp_fchart04.png", "wb")
size = 0
while True:
    info = response.read(10000)
    if len(info) < 1:
        break
    size = size + len(info)
    fp.write(info)    
print(size, "個字元下載...")
fp.close()
response.close()

print("------------------------------------------------------------")  # 60個

import re
import requests
from bs4 import BeautifulSoup

url = "http://www.google.com.tw"
path = "tmp_logo.png"
r = requests.get(url)
r.encoding = "utf8"
soup = BeautifulSoup(r.text, "lxml")
tag_img = soup.find("img")
# 取出Logo圖片的正規運算式
match = re.search(r"(/[^/#?]+)+\.(?:jpg|gif|png)", str(tag_img))
print(match.group())
url = url + str(match.group())
response = requests.get(url, stream=True)
if response.status_code == 200:
    with open(path, 'wb') as fp:
        for chunk in response:
            fp.write(chunk)
    print("圖檔logo.png已經下載")        
else:
    print("錯誤! HTTP請求失敗...")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個




print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個






print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

