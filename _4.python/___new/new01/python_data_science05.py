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

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
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

import sqlite3

# 建立資料庫連接
conn = sqlite3.connect("data/Books.sqlite")
# 執行SQL指令SELECT
cursor = conn.execute("SELECT * FROM Books")
# 取出查詢結果的每一筆記錄
for row in cursor:
    print(row[0], row[1])
conn.close()  # 關閉資料庫連接

print("------------------------------------------------------------")  # 60個

import sqlite3

book = "D0002,MySQL資料庫系統,600"
f = book.split(",")

# 建立資料庫連接
conn = sqlite3.connect("data/Books.sqlite")
# 建立SQL指令INSERT字串
sql = "INSERT INTO Books (id, title, price) VALUES ('{0}','{1}',{2})"
sql = sql.format(f[0], f[1], f[2])
print(sql)
cursor = conn.execute(sql)   # 執行SQL指令
print(cursor.rowcount)
conn.commit() # 確認交易
conn.close()  # 關閉資料庫連接


print("------------------------------------------------------------")  # 60個

import sqlite3

d = {
   "id": "D0003",
   "title": "MongoDB資料庫系統",
   "price": 650
}

# 建立資料庫連接
conn = sqlite3.connect("data/Books.sqlite")
# 建立SQL指令INSERT字串
sql = "INSERT INTO Books (id, title, price) VALUES ('{0}','{1}',{2})"
sql = sql.format(d['id'], d['title'], d['price'])
print(sql)
cursor = conn.execute(sql)   # 執行SQL指令
print(cursor.rowcount)
conn.commit() # 確認交易
conn.close()  # 關閉資料庫連接

print("------------------------------------------------------------")  # 60個

import sqlite3

# 建立資料庫連接
conn = sqlite3.connect("data/Books.sqlite")
cursor = conn.cursor()
sql = """UPDATE Books SET price=650 
         WHERE id='D0002' """
sql2 = """UPDATE Books SET price=700 
         WHERE id='D0003' """
try:
    cursor.execute(sql) 
    cursor.execute(sql2)
    conn.commit()
    print("更新 2 筆記錄...")
except:
    conn.rollback()
    print("更新記錄失敗...")
conn.close() 

print("------------------------------------------------------------")  # 60個

import sqlite3

# 建立資料庫連接
conn = sqlite3.connect("data/Books.sqlite")
cursor = conn.cursor()
sql = "DELETE FROM Books WHERE id='D0002'"
sql2 = "DELETE FROM Books WHERE id='D0003'"
try:
    cursor.execute(sql) 
    cursor.execute(sql2)
    conn.commit()
    print("刪除 2 筆記錄...")
except:
    conn.rollback()
    print("刪除記錄失敗...")
conn.close() 


print("------------------------------------------------------------")  # 60個

""" 無 pymysql

import pymysql 

db = pymysql.connect(host="localhost",user="root",password="",database="mybook",charset="utf8")
cursor = db.cursor() 
cursor.execute("SELECT * FROM book")
row = cursor.fetchone()
print(row[0], row[1])
print("-------------------------")      
data = cursor.fetchall()
for row in data:
    print(row[0], row[1])
db.close()
"""
print("------------------------------------------------------------")  # 60個

'''
import pymysql

book = "P0004,Node.js程式設計,陳會安,550,程式設計,2020-01-01"
f = book.split(",")

db = pymysql.connect(host="localhost",user="root",password="",database="mybook",charset="utf8")
cursor = db.cursor()
sql = """INSERT INTO book (id,title,author,price,category,pubdate)
         VALUES ('{0}','{1}','{2}',{3},'{4}','{5}')"""
sql = sql.format(f[0], f[1], f[2], f[3], f[4], f[5])
print(sql)
try:
    cursor.execute(sql)
    db.commit()
    print("新增一筆記錄...")
except:
    db.rollback() 
    print("新增記錄失敗...")
db.close()


print("------------------------------------------------------------")  # 60個

import pymysql

d = {
   "id": "P0005",
   "title": "Android程式設計",
   "author": "陳會安",
   "price": 650,
   "cat": "程式設計",
   "date": "2019-02-01"
}

db = pymysql.connect(host="localhost",user="root",password="",database="mybook",charset="utf8")
cursor = db.cursor()
sql = """INSERT INTO book (id,title,author,price,category,pubdate)
         VALUES ('{0}','{1}','{2}',{3},'{4}','{5}')"""
sql = sql.format(d['id'],d['title'],d['author'],d['price'],d['cat'],d['date'])
print(sql)
try:
    cursor.execute(sql) 
    db.commit()
    print("新增一筆記錄...")
except:
    db.rollback()
    print("新增記錄失敗...")
db.close() 

print("------------------------------------------------------------")  # 60個

import pymysql

db = pymysql.connect(host="localhost",user="root",password="",database="mybook",charset="utf8")
cursor = db.cursor()
sql = """UPDATE book SET price=500, 
         pubdate='2020/02/01'
         WHERE id='P0004' """
sql2 = """UPDATE book SET price=600, 
         pubdate='2019/03/01'
         WHERE id='P0005' """
try:
    cursor.execute(sql) 
    cursor.execute(sql2)
    db.commit()
    print("更新 2 筆記錄...")
except:
    db.rollback()
    print("更新記錄失敗...")
db.close() 

print("------------------------------------------------------------")  # 60個

import pymysql

db = pymysql.connect(host="localhost",user="root",password="",database="mybook",charset="utf8")
cursor = db.cursor()
sql = "DELETE FROM book WHERE id='P0004'"
sql2 = "DELETE FROM book WHERE id='P0005'"
try:
    cursor.execute(sql) 
    cursor.execute(sql2)
    db.commit()
    print("刪除 2 筆記錄...")
except:
    db.rollback()
    print("刪除記錄失敗...")
db.close() 


print("------------------------------------------------------------")  # 60個

import pymongo

client = pymongo.MongoClient("localhost", 27017)
db = client.mydb          # 選擇mydb資料庫
collection = db.students  # 選擇students
std = collection.find_one({"name": 'joe chen'})
print(std)
print("------------")
for item in collection.find({"gender":"f"}):
    print(item)

print("------------------------------------------------------------")  # 60個

import pymongo

client = pymongo.MongoClient("localhost", 27017)
db = client.mydb          # 選擇mydb資料庫
collection = db.students  # 選擇students

std = {
    'name': 'mary wang',
    'dob': '11/05/1978',
    'gender': 'f',
    'favorite_color': 'red',
    'nationality': 'taiwan'
}

result = collection.insert_one(std)
print("新增1筆: {0}".format(result.inserted_id))

print("------------------------------------------------------------")  # 60個

import pymongo

client = pymongo.MongoClient("localhost", 27017)
db = client.mydb          # 選擇mydb資料庫
collection = db.students  # 選擇students

std1 = {
    'name': 'tom wang',
    'dob': '11/01/1988',
    'gender': 'm',
    'favorite_color': 'black',
    'nationality': 'taiwan'
}

std2 = {
    'name': 'john chen',
    'dob': '22/01/1989',
    'gender': 'm',
    'favorite_color': 'blue',
    'nationality': 'taiwan'
}
result = collection.insert_many([std1, std2])
print("新增2筆: {0}".format(result.inserted_ids))
'''
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

