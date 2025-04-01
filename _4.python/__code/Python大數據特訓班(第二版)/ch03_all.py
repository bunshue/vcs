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

# csv_read.py
import csv

# 開啟 csv 檔案
with open("data/school.csv", newline="") as csvfile:
    # 讀取 csv 檔案內容
    rows = csv.reader(csvfile)
    # 以迴圈顯示每一列
    for row in rows:
        print(row)

print("------------------------------------------------------------")  # 60個

import csv

# 開啟 csv 檔案
with open("data/school.csv", newline="") as csvfile:
    # 讀取 csv 檔案內容
    rows = csv.reader(csvfile)
    # 以迴圈顯示每一列
    for row in rows:
        print(row)

print("------------------------------------------------------------")  # 60個

# csv_read_dict.py
import csv

# 開啟 csv 檔案
with open("data/school.csv", newline="") as csvfile:
    # 讀取 csv 檔內容，將每一列轉成 dictionary
    rows = csv.DictReader(csvfile)
    # 以迴圈顯示每一列
    for row in rows:
        print(row["座號"], row["姓名"], row["國文"], row["英文"], row["數學"])

# csv_write_list1.py
import csv

with open("tmp_test1.csv", "w", newline="") as f:
    # 建立 csv 檔寫入物件
    writer = csv.writer(f)
    # 寫入欄位及資料
    writer.writerow(["座號", "姓名", "國文", "英文", "數學"])
    writer.writerow([1, "葉大雄", 65, 62, 40])
    writer.writerow([2, "陳靜香", 85, 90, 87])
    writer.writerow([3, "王聰明", 92, 90, 95])

# csv_write_list2.py
import csv

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

# csv_write_dict.py
import csv

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

# jsonload1.py
import json

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

# jsonload2.py
import json

with open("data/class_str.json", "r", encoding="utf-8") as f:
    datas = json.load(f)
    print(type(datas))
    for data in datas["一年甲班"]:
        print(data, data["姓名"])


print("------------------------------------------------------------")  # 60個

# jsondump1.py
import json

with open("data/class_str.json", "r", encoding="utf-8") as f:
    datas = json.load(f)
print(datas, type(datas))
dumpdata = json.dumps(datas, ensure_ascii=False)
print(dumpdata, type(dumpdata))

print("------------------------------------------------------------")  # 60個


# jsondump2.py
import json

with open("data/class_str.json", "r", encoding="utf-8") as f:
    datas = json.load(f)
with open("tmp_class_str.json", "w", encoding="utf-8") as f:
    dumpdata = json.dump(datas, f, ensure_ascii=False)

print("------------------------------------------------------------")  # 60個
'''
# sqlite_cursor.py
import sqlite3

conn = sqlite3.connect("school.db")  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件
# 建立一個資料表
sqlstr = """CREATE TABLE IF NOT EXISTS scores \
("id"  INTEGER PRIMARY KEY NOT NULL,
 "name"  TEXT NOT NULL,
 "chinese"  INTEGER NOT NULL,
 "english"  INTEGER NOT NULL,
 "math"  INTEGER NOT NULL
 )
"""
cursor.execute(sqlstr)

# 新增記錄
cursor.execute('insert into scores values(1, "葉大雄", 65, 62, 40)')
cursor.execute('insert into scores values(2, "陳靜香", 85, 90, 87)')
cursor.execute('insert into scores values(3, "王聰明", 92, 90, 95)')
conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個


# sqlite_crud1.py
import sqlite3

conn = sqlite3.connect("school.db")  # 建立資料庫連線
# 建立一個資料表
sqlstr = """CREATE TABLE IF NOT EXISTS scores \
("id"  INTEGER PRIMARY KEY NOT NULL,
 "name"  TEXT NOT NULL,
 "chinese"  INTEGER NOT NULL,
 "english"  INTEGER NOT NULL,
 "math"  INTEGER NOT NULL
 )
"""
conn.execute(sqlstr)
conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

# sqlite_crud2.py
import sqlite3

conn = sqlite3.connect("data/school.db")  # 建立資料庫連線
# 定義資料串列
datas = [[1, "葉大雄", 65, 62, 40], [2, "陳靜香", 85, 90, 87], [3, "王聰明", 92, 90, 95]]

# 新增資料
for data in datas:
    conn.execute(
        "INSERT INTO scores (id, name, chinese, english, math) VALUES \
                 ({}, '{}', {}, {}, {})".format(
            data[0], data[1], data[2], data[3], data[4]
        )
    )
conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個

# sqlite_crud3.py
import sqlite3

conn = sqlite3.connect("school.db")  # 建立資料庫連線
# 更新資料
conn.execute("UPDATE scores SET name='{}' WHERE id={}".format("林胖虎", 1))
conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個

# sqlite_crud4.py
import sqlite3

conn = sqlite3.connect("school.db")  # 建立資料庫連線
# 刪除資料
conn.execute("DELETE FROM scores WHERE id={}".format(1))
conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

# fetchall.py
import sqlite3

conn = sqlite3.connect("school.db")  # 建立資料庫連線
cursor = conn.execute("select * from scores")
rows = cursor.fetchall()
# 顯示原始資料
print(rows)
# 逐筆顯示資料
for row in rows:
    print(row[0], row[1])
conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個

# fetchone.py
import sqlite3

conn = sqlite3.connect("school.db")  # 建立資料庫連線
cursor = conn.execute("select * from scores")
row = cursor.fetchone()
print(row[0], row[1])
conn.close()  # 關閉資料庫連線
'''
print("------------------------------------------------------------")  # 60個
''' pymysql
# mysqltable.py
import pymysql

conn = pymysql.connect(
    "localhost", port=3306, user="root", passwd="1234", charset="utf8", db="pythondb"
)  # 連結資料庫

with conn.cursor() as cursor:
    sql = """
    CREATE TABLE IF NOT EXISTS Scores (
      ID int NOT NULL AUTO_INCREMENT PRIMARY KEY,
      Name varchar(20),
      Chinese int(3),
      English int(3),
      Math int(3)
    );
    """
    cursor.execute(sql)  # 執行SQL指令
    conn.commit()  # 提交資料庫
conn.close()

print("------------------------------------------------------------")  # 60個


# mysqlinsert.py
import pymysql

conn = pymysql.connect(
    "localhost", port=3306, user="root", passwd="1234", charset="utf8", db="pythondb"
)  # 連結資料庫

with conn.cursor() as cursor:
    sql = """
    insert into scores (Name, Chinese, English, Math) values 
    ('葉大雄',65,62,40),
    ('陳靜香',85,90,87),
    ('王聰明',92,90,95)
    """
    cursor.execute(sql)
    conn.commit()  # 提交資料庫
conn.close()

print("------------------------------------------------------------")  # 60個


# mysqlquery.py
import pymysql

conn = pymysql.connect(
    "localhost", port=3306, user="root", passwd="1234", charset="utf8", db="pythondb"
)  # 連結資料庫

with conn.cursor() as cursor:
    sql = "select * from scores"
    cursor.execute(sql)
    datas = cursor.fetchall()  # 取出所有資料
    print(datas)
    print("-" * 30)  # 畫分隔線
    sql = "select * from scores"
    cursor.execute(sql)
    data = cursor.fetchone()  # 取出第一筆資料
    print(data)

conn.close()

print("------------------------------------------------------------")  # 60個


# mysqlupdate.py
import pymysql

conn = pymysql.connect(
    "localhost", port=3306, user="root", passwd="1234", charset="utf8", db="pythondb"
)  # 連結資料庫

with conn.cursor() as cursor:
    sql = "update scores set Chinese = 98 where ID = 3"
    cursor.execute(sql)
    conn.commit()
    sql = "select * from scores where ID = 3"
    cursor.execute(sql)
    data = cursor.fetchone()
    print(data)

conn.close()

# mysqldelete.py
import pymysql

conn = pymysql.connect(
    "localhost", port=3306, user="root", passwd="1234", charset="utf8", db="pythondb"
)  # 連結資料庫

with conn.cursor() as cursor:
    sql = "delete from scores where ID = 3"
    cursor.execute(sql)
    conn.commit()
    sql = "select * from scores"
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)

conn.close()
'''
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

# csv_read_dict.py

import csv

# 開啟 csv 檔案
with open("data/school.csv", newline="") as csvfile:
    # 讀取 csv 檔內容，將每一列轉成 dictionary
    rows = csv.DictReader(csvfile)
    # 以迴圈顯示每一列
    for row in rows:
        print(row["座號"], row["姓名"], row["國文"], row["英文"], row["數學"])

print("------------------------------------------------------------")  # 60個

# csv_write_dict.py

import csv

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

# csv_write_list1.py

import csv

with open("tmp_test1aaaa.csv", "w", newline="") as f:
    # 建立 csv 檔寫入物件
    writer = csv.writer(f)
    # 寫入欄位及資料
    writer.writerow(["座號", "姓名", "國文", "英文", "數學"])
    writer.writerow([1, "葉大雄", 65, 62, 40])
    writer.writerow([2, "陳靜香", 85, 90, 87])
    writer.writerow([3, "王聰明", 92, 90, 95])

print("------------------------------------------------------------")  # 60個

# csv_write_list2.py

import csv

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

# jsondump1.py

import json

with open("data/class_str.json", "r", encoding="utf-8") as f:
    datas = json.load(f)
print(datas, type(datas))
dumpdata = json.dumps(datas, ensure_ascii=False)
print(dumpdata, type(dumpdata))

print("------------------------------------------------------------")  # 60個

# jsondump2.py

import json

with open("data/class_str.json", "r", encoding="utf-8") as f:
    datas = json.load(f)
with open("tmp_class_str2.json", "w", encoding="utf-8") as f:
    dumpdata = json.dump(datas, f, ensure_ascii=False)

print("------------------------------------------------------------")  # 60個

# jsonload1.py

import json

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

# jsonload2.py

import json

with open("data/class_str.json", "r", encoding="utf-8") as f:
    datas = json.load(f)
    print(type(datas))
    for data in datas["一年甲班"]:
        print(data, data["姓名"])

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


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
