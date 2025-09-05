"""
sqlite基本範例 一個 基本款

增刪查改（英語：CRUD），全稱
增加（CREATE，意為「建立」）、
刪除（DELETE）、
查詢（Read，意為「讀取」）、
改正（UPDATE，意為「更新」），
在電腦程式語言中是一連串常見的動作行為，

簡易建立資料庫

增加(13)

刪除資料(1)
讀取全部資料
搜尋資料

刪除資料庫

原始資料 9 筆
	id_num	ename	cname	weight
第1筆 : 5	horse	馬	36
第2筆 : 1	mouse	鼠	3
第3筆 : 4	elephant象	100	(此筆資料錯誤, 應刪除)

第4筆 : 9	ox		48
第5筆 : 2	sheep		66	(此筆資料錯誤, 應為goat 29)

第6筆 : 8	snake		16	(詢問是否刪除此筆資料)
第7筆 : 3	tiger		33

第8筆 : 7	rabbit		8

第9筆 : 6	tiger		240

1. 建立資料庫
2. 新增資料 9筆
3. 修改2號的name
4. 刪除4號
5. 詢問是否刪除8號資料
6. 搜尋

sqlite基本範例 一個

原始資料 9 筆
	id_num	ename	cname	weight
第1筆 : 5	horse	馬	36
第2筆 : 1	mouse	鼠	3
第3筆 : 4	elephant象	100	(此筆資料錯誤, 應刪除)

第4筆 : 9	ox		48
第5筆 : 2	sheep		66	(此筆資料錯誤, 應為goat 29)

第6筆 : 8	snake		16	(詢問是否刪除此筆資料)
第7筆 : 3	tiger		33

第8筆 : 7	rabbit		8

第9筆 : 6	tiger		240

1. 建立資料庫
2. 新增資料 9筆
3. 修改2號的name
4. 刪除4號
5. 詢問是否刪除8號資料
6. 搜尋
7. 各種排序顯示資料庫內容

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


def show():
    return
    plt.tight_layout()  # 緊密排列，並填滿原圖大小
    plt.show()


print("------------------------------------------------------------")  # 60個

import csv
import shutil
import datetime
import sqlite3

print("準備工作")

db_filename_books_old = "data/Books.sqlite"
db_filename_books = "tmp_Books.sqlite"
db_filename_python02_old = "data/python02.sqlite"
db_filename_python02 = "tmp_python02.sqlite"
db_filename_myInfo1_old = "data/myInfo.db"
db_filename_myInfo2_old = "data/myInfo2.db"
db_filename_myInfo1 = "tmp_myInfo.db"
db_filename_myInfo2 = "tmp_myInfo2.db"

if not os.path.exists(db_filename_books):
    shutil.copy(db_filename_books_old, db_filename_books)
    print(db_filename_books)

if not os.path.exists(db_filename_python02):
    shutil.copy(db_filename_python02_old, db_filename_python02)
    print(db_filename_python02)

if not os.path.exists(db_filename_myInfo1):
    shutil.copy(db_filename_myInfo1_old, db_filename_myInfo1)
    print(db_filename_myInfo1)

if not os.path.exists(db_filename_myInfo2):
    shutil.copy(db_filename_myInfo2_old, db_filename_myInfo2)
    print(db_filename_myInfo2)


def show_data_base_contents(db_filename, table_name, length):
    conn = sqlite3.connect(db_filename)  # 建立資料庫連線
    sqlstr = "SELECT * FROM {};".format(table_name)  # same
    sqlstr = "SELECT * FROM %s" % table_name
    cursor = conn.execute(sqlstr)

    n = 0
    for row in cursor:
        print(row)
        n = n + 1
        # 讀取 N 筆資料, 即跳出
        if n == length:
            break
    conn.close()  # 關閉資料庫連線


def show_data_base_contents_all(db_filename, table_name):
    conn = sqlite3.connect(db_filename)  # 建立資料庫連線
    # SELECT * : 取得所有資料
    sqlstr = "SELECT * FROM {};".format(table_name)  # same
    sqlstr = "SELECT * FROM %s" % table_name
    rows = str(conn.execute(sqlstr).fetchall())  # 讀取全部資料成元組串列
    print(rows)
    conn.close()  # 關閉資料庫連線


def do_fetchall(cursor):
    rows = cursor.fetchall()  # 讀取全部資料成元組串列
    length = len(rows)
    print("共有", length, "筆資料")
    for i in range(length):
        print("第" + str(i + 1) + "筆資料 : ", rows[i])
        if i > 10:
            break


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("建立資料庫 + 加入資料 + 讀取資料")

db_filename = "tmp_db01_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".sqlite"
print("建立資料庫連線, 資料庫 :", db_filename)

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

sqlstr = """
CREATE TABLE IF NOT EXISTS table01(
idx    INTEGER PRIMARY KEY AUTOINCREMENT,
id_num INTEGER NOT NULL,
ename  TEXT NOT NULL,
cname  TEXT,
weight INTEGER NOT NULL CHECK(weight > 0) -- 預設錯誤時會顯示
)
"""

cursor.execute(sqlstr)
conn.commit()  # 更新

print("新增資料 2 筆 寫法三, 有些欄位可以不寫, 序號自動遞增")

sqlstr = (
    "INSERT INTO table01 (id_num, ename, cname, weight) VALUES (5, 'horse', '馬', 48)"
)
cursor.execute(sqlstr)
sqlstr = (
    "INSERT INTO table01 (id_num, ename, cname, weight) VALUES (1, 'mouse', '鼠', 66)"
)
cursor.execute(sqlstr)
sqlstr = (
    "INSERT INTO table01 (id_num, ename, cname, weight) VALUES (4, 'elephant', '象', 48)"
)
cursor.execute(sqlstr)
sqlstr = "INSERT INTO table01 (id_num, ename, weight) VALUES (9, 'ox', 48)"
cursor.execute(sqlstr)
sqlstr = "INSERT INTO table01 (id_num, ename, weight) VALUES (2, 'sheep', 66)"
cursor.execute(sqlstr)
sqlstr = "INSERT INTO table01 (id_num, ename, weight) VALUES (8, 'snake', 16)"
cursor.execute(sqlstr)
sqlstr = "INSERT INTO table01 (id_num, ename, weight) VALUES (3, 'tiger', 33)"
cursor.execute(sqlstr)
sqlstr = "INSERT INTO table01 (id_num, ename, weight) VALUES (7, 'rabbit', 8)"
cursor.execute(sqlstr)
sqlstr = "INSERT INTO table01 (id_num, ename, weight) VALUES (6, 'tiger', 240)"
cursor.execute(sqlstr)

conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

# UPDATE 更新
print("更新資料, 修改2號的資料")
print("建立資料庫連線, 資料庫 :", db_filename)
conn = sqlite3.connect(db_filename)  # 建立資料庫連線
sqlstr = "UPDATE table01 SET ename = '{}'  WHERE id_num = {}".format("goat", 2)
conn.execute(sqlstr)  # 修改2號的資料, 要先確保已經有2號的資料, 才可以修改
sqlstr = "UPDATE table01 SET weight = '{}' WHERE id_num = {}".format(29, 2)
conn.execute(sqlstr)  # 修改2號的資料, 要先確保已經有2號的資料, 才可以修改
conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

# DELETE 刪除
print("刪除資料, 刪除4號的資料")
print("建立資料庫連線, 資料庫 :", db_filename)
conn = sqlite3.connect(db_filename)  # 建立資料庫連線
sqlstr = "DELETE FROM table01 WHERE id_num = {}".format(4)
conn.execute(sqlstr)
conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

print("用fetchall()讀取 全部資料")
print("建立資料庫連線, 資料庫 :", db_filename)
conn = sqlite3.connect(db_filename)  # 建立資料庫連線
sqlstr = "SELECT * FROM table01"  # SELECT * : 取得所有資料
cursor = conn.execute(sqlstr)

do_fetchall(cursor)

conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

"""
print("刪除資料庫中的表單")
print("建立資料庫連線, 資料庫 :", db_filename)
conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.execute("DROP TABLE table01")
conn.commit()  # 更新
conn.close()  # 關閉資料庫連線
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

db_filename = "tmp_db02_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".sqlite"
print("建立資料庫連線, 資料庫 :", db_filename)

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

print("建立一個表單")

# id_num不可重複
sqlstr = """
CREATE TABLE IF NOT EXISTS table01(
id_num       CHAR(5),
subjectId    CHAR(4) NOT NULL,
animalNumber INTEGER,
title        VARCHAR(50) NOT NULL,
PRIMARY KEY (id_num)
)
"""

# id_num可重複
sqlstr = """
CREATE TABLE IF NOT EXISTS table01(
id_num       CHAR(5),
subjectId    CHAR(4) NOT NULL,
animalNumber INTEGER,
title        VARCHAR(50) NOT NULL
)
"""

# id_num可重複, 若資料庫已存在 則不用重新建立
sqlstr = """
CREATE TABLE IF NOT EXISTS table01(
id_num       CHAR(5),
subjectId    CHAR(4) NOT NULL,
animalNumber INTEGER,
title        VARCHAR(50) NOT NULL
)
"""

# PRIMARY KEY (id_num), id_num不可重複
sqlstr = """
CREATE TABLE IF NOT EXISTS table01(
id_num INTEGER PRIMARY KEY NOT NULL,
ename  TEXT NOT NULL,
weight INTEGER NOT NULL
)
"""

# 多了檢查條件
# 序號 自動遞增 不可重複
sqlstr = """
CREATE TABLE IF NOT EXISTS table01(
idx    INTEGER PRIMARY KEY AUTOINCREMENT,
id_num INTEGER NOT NULL,
ename  TEXT NOT NULL,
cname  TEXT,
weight INTEGER NOT NULL CHECK(weight > 0) -- 預設錯誤時會顯示
)
"""

# 有寫NOT NULL表示一定要填寫, 若無此條件, 則可以不寫

cursor.execute(sqlstr)
conn.commit()  # 更新

# INSERT 新增資料
print("新增資料 2 筆 寫法一, 必須要寫滿所有欄位")
# id_num不可重複
sqlstr = 'INSERT INTO table01 VALUES (20, 5, "horse", "馬", 36)'
cursor.execute(sqlstr)
sqlstr = 'INSERT INTO table01 VALUES (50, 1, "mouse", "鼠", 3)'
cursor.execute(sqlstr)

print("新增資料 1 筆 寫法二, 有些欄位可以不寫, 使用tuple")
sqlstr = "INSERT INTO table01 (id_num, ename, cname, weight) VALUES (?, ?, ?, ?)"
data_insert_tuple = (4, "elephant", "象", 100)
cursor.execute(sqlstr, data_insert_tuple)

print("新增資料 2 筆 寫法三, 有些欄位可以不寫, 序號自動遞增")
cursor.execute("INSERT INTO table01 (id_num, ename, weight) VALUES (9, 'ox', 48)")
# id_num不重複 但name weight 重複
cursor.execute("INSERT INTO table01 (id_num, ename, weight) VALUES (2, 'sheep', 66)")

print("新增資料 2 筆 寫法四, 有些欄位可以不寫, 序號自動遞增")
# 定義資料串列
datas = [[8, "snake", 16], [3, "tiger", 33]]

for data in datas:
    # 新增資料
    sqlstr = (
        "INSERT INTO table01 (id_num, ename, weight) VALUES ({}, '{}', '{}')".format(
            data[0], data[1], data[2]
        )
    )
    cursor.execute(sqlstr)
conn.commit()  # 更新


print("新增資料 1 筆 寫法五, 必須要寫滿所有欄位")
index = 70
number = 7
ename = "rabbit"
cname = ""
weight = 8
sqlstr = "INSERT INTO table01 VALUES ({},{},'{}','{}','{}');".format(
    index, number, ename, cname, weight
)
cursor.execute(sqlstr)

print("新增資料 1 筆 寫法六, 必須要寫滿所有欄位")
data = (80, 6, "tiger", "", 240)
cursor.execute("INSERT INTO table01 VALUES (?, ?, ?, ?, ?)", data)

conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

# UPDATE 更新
print("更新資料, 修改2號的資料")
print("建立資料庫連線, 資料庫 :", db_filename)
conn = sqlite3.connect(db_filename)  # 建立資料庫連線
sqlstr = "UPDATE table01 SET ename = '{}'  WHERE id_num = {}".format("goat", 2)
conn.execute(sqlstr)  # 修改2號的資料, 要先確保已經有2號的資料, 才可以修改
sqlstr = "UPDATE table01 SET weight = '{}' WHERE id_num = {}".format(29, 2)
conn.execute(sqlstr)  # 修改2號的資料, 要先確保已經有2號的資料, 才可以修改
conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

# DELETE 刪除
print("刪除資料, 刪除4號的資料")
print("建立資料庫連線, 資料庫 :", db_filename)
conn = sqlite3.connect(db_filename)  # 建立資料庫連線
sqlstr = "DELETE FROM table01 WHERE id_num = {}".format(4)
conn.execute(sqlstr)
conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個
# SELECT 取得
print("讀取資料庫資料, 全部1")
show_data_base_contents_all(db_filename, "table01")

print("------------------------------------------------------------")  # 60個
print("讀取資料庫資料, 全部2")
print("建立資料庫連線, 資料庫 :", db_filename)
conn = sqlite3.connect(db_filename)  # 建立資料庫連線
sqlstr = "SELECT * FROM table01"  # SELECT * : 取得所有資料
cursor = conn.execute(sqlstr)
do_fetchall(cursor)

conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個
# SELECT 取得
print("建立資料庫連線, 資料庫 :", db_filename)
conn = sqlite3.connect(db_filename)  # 建立資料庫連線
print("指明抓一筆資料, 9號")
number = 9
sqlstr = "SELECT * FROM table01 WHERE id_num = " + str(number)  # 條件
cursor = conn.execute(sqlstr)
row = cursor.fetchone()  # 讀取一筆資料
if not row == None:
    print("{}\t{}\t{}\t{}".format(row[0], row[1], row[2], row[3], row[4]))
else:
    print("找不到" + str(number) + "號資料")

print("------------------------------------------------------------")  # 60個
print("指明抓一筆資料, 15號")
number = 15
sqlstr = "SELECT * FROM table01 WHERE id_num = " + str(number)  # 條件
cursor = conn.execute(sqlstr)
row = cursor.fetchone()  # 讀取一筆資料
if not row == None:
    print("{}\t{}\t{}\t{}".format(row[0], row[1], row[2], row[3], row[4]))
else:
    print("找不到" + str(number) + "號資料")

print("------------------------------------------------------------")  # 60個
print("指明抓名字有bb的資料")
data = ("%bb%",)  # bb在中間 前後要有%
# sqlstr =
cursor = conn.execute("SELECT * FROM table01 WHERE ename LIKE ?", data)  # 條件
do_fetchall(cursor)

conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個
print("尋找資料")
print("建立資料庫連線, 資料庫 :", db_filename)
conn = sqlite3.connect(db_filename)  # 建立資料庫連線
number = 8
sqlstr = "SELECT * FROM table01 WHERE id_num = {};".format(number)  # 條件
cursor = conn.execute(sqlstr)
rows = cursor.fetchall()  # 讀取全部資料成元組串列
length = len(rows)
print("共有", length, "筆資料")
for i in range(length):
    print("第" + str(i + 1) + "筆資料 : ", rows[i])

if len(rows) > 0:
    print("找到資料 {}\t{}\t{}\t{}".format(rows[0][0], rows[0][1], rows[0][2], rows[0][3]))
    """
    # 刪除資料
    sqlstr = "DELETE FROM table01 WHERE id_num = {};".format(number)
    conn.execute(sqlstr)
    conn.commit()  # 更新
    print("已刪除指定的資料")
    """

print("------------------------------------------------------------")  # 60個

print("不是用fetchall()讀取 全部資料")
print("建立資料庫連線, 資料庫 :", db_filename)
conn = sqlite3.connect(db_filename)  # 建立資料庫連線
sqlstr
cursor = conn.execute("SELECT * FROM table01")  # SELECT * : 取得所有資料
i = 0
for row in cursor:
    # print(type(rows[i]))
    print("第" + str(i + 1) + "筆資料 :", end="")
    # print(rows[i])
    print("{}\t{}\t{}\t{}".format(row[0], row[1], row[2], row[3], row[4]))
    i = i + 1
conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個
print("用fetchall()讀取 全部資料")
print("建立資料庫連線, 資料庫 :", db_filename)
conn = sqlite3.connect(db_filename)  # 建立資料庫連線
sqlstr = "SELECT * FROM table01"  # SELECT * : 取得所有資料
cursor = conn.execute(sqlstr)
do_fetchall(cursor)

conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個

print("用fetchall()讀取 全部資料 預設排序(依第1項升冪排序)")
print("建立資料庫連線, 資料庫 :", db_filename)
conn = sqlite3.connect(db_filename)  # 建立資料庫連線
sqlstr = "SELECT * FROM table01"  # SELECT * : 取得所有資料
cursor = conn.execute(sqlstr)
do_fetchall(cursor)

conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個

print("用fetchall()讀取 全部資料 依 ename 排序, 升冪")
print("建立資料庫連線, 資料庫 :", db_filename)
conn = sqlite3.connect(db_filename)  # 建立資料庫連線
sqlstr = "SELECT * FROM table01 ORDER BY ename;"  # 由小到大, 升冪
cursor = conn.execute(sqlstr)
# cursor = conn.execute("SELECT * FROM table01 ORDER BY ename DESC;")  #由小到大 + 反相 = 由大到小, 降冪
do_fetchall(cursor)

conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個
print("用fetchall()讀取 全部資料 依 weight 排序, 降冪")
print("建立資料庫連線, 資料庫 :", db_filename)
conn = sqlite3.connect(db_filename)  # 建立資料庫連線
# cursor = conn.execute("SELECT * FROM table01 ORDER BY weight;")  #由小到大, 升冪
cursor = conn.execute(
    "SELECT * FROM table01 ORDER BY weight DESC;"
)  # 由小到大 + 反相 = 由大到小, 降冪
do_fetchall(cursor)

conn.close()  # 關閉資料庫連線
"""
print("------------------------------------------------------------")	#60個
print("刪除資料庫中的表單")
print("建立資料庫連線, 資料庫 :", db_filename)
conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.execute("DROP TABLE table01")
conn.commit()  # 更新
conn.close()  # 關閉資料庫連線
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 讀取資料庫大全

"""
讀出一個完整的資料庫大全
1. 一個資料庫內  多個表單 能找出所有表單
2. 依序開啟每個表單 讀出所有資料
搜尋排序.....
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# 取得一個資料庫內所有表單的名稱, list格式
def get_table_names(conn):
    table_names = []
    tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
    for table in tables.fetchall():
        table_names.append(table[0])
    return table_names


# 取得一個表單內所有欄位的名稱, list格式
def get_column_names(conn, table_name):
    column_names = []
    columns = conn.execute(f"PRAGMA table_info('{table_name}');").fetchall()
    for col in columns:
        column_names.append(col[1])
    return column_names


db_filename = "ims_sql/db_ims.sqlite"
db_filename = "data/gasoline.sqlite"
db_filename = "data/example.db"
db_filename = "data/populations.db"
db_filename = "data/singMatch.db"

print("建立資料庫連線, 資料庫 :", db_filename)
conn = sqlite3.connect(db_filename)  # 建立資料庫連線

print("讀取此資料庫內的所有表單")
table_names = get_table_names(conn)

print("裡面有 :", len(table_names), "個表單 :", table_names)

print("讀取每個表單的所有欄位")
# table_dicts = [] # 將資料存在字典裡
for table_name in table_names:
    print("表單 :", table_name, end="\t")
    column_names = get_column_names(conn, table_name)
    # table_dicts.append({"table_name": table_name, "column_names": column_names})
    print("裡面有 :", len(column_names), "個欄位 :", column_names)
# print(type(table_dicts))
# print(table_dicts)


print("讀取每個表單的所有內容")
for table_name in table_names:
    print("表單 :", table_name, end="\t")
    cursor = conn.execute("SELECT * FROM %s" % table_name)
    rows = cursor.fetchall()  # 讀取全部資料成元組串列
    length = len(rows)
    print("共有", length, "筆資料")
    for i in range(length):
        print("第" + str(i + 1) + "筆資料 : ", rows[i])

conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 各種讀取資料庫範例

print("------------------------------------------------------------")  # 60個

db_filename = "data/gasoline.sqlite"


def disp_menu():
    print("中油歷年油價查詢系統")
    print("------------")
    print("1.顯示歷年油價資訊")
    print("2.最近10週油價資訊")
    print("0.結束")
    print("------------")


def disp_alldata():
    print("建立資料庫連線, 資料庫 :", db_filename)
    conn = sqlite3.connect(db_filename)  # 建立資料庫連線

    print("要事先能知道表單的名稱 prices 與 各欄位的名稱 gdate")

    sqlstr = "SELECT * FROM prices ORDER BY gdate DESC;"
    cursor = conn.execute(sqlstr)

    # 不是用fetchall()讀取全部資料
    n = 0
    for row in cursor:
        print("日期：{}，92無鉛：{}，95無鉛：{}，98無鉛：{}".format(row[0], row[1], row[2], row[3]))
        n = n + 1
        """
        if n == 20:  # 一次顯示20筆
            x = input("請按Enter鍵繼續...(Q:回主選單)")
            if x == "Q" or x == "q": break
            n = 0
        """
    conn.close()  # 關閉資料庫連線


def disp_10data_a():
    print("建立資料庫連線, 資料庫 :", db_filename)
    conn = sqlite3.connect(db_filename)  # 建立資料庫連線

    print("要事先能知道表單的名稱 prices 與 各欄位的名稱 gdate")
    sqlstr = "SELECT * FROM prices ORDER BY gdate DESC;"
    cursor = conn.execute(sqlstr)

    n = 0
    for row in cursor:
        print(row)
        print("日期：{}，92無鉛：{}，95無鉛：{}，98無鉛：{}".format(row[0], row[1], row[2], row[3]))
        n = n + 1
        # 讀取10筆資料, 即跳出
        if n == 10:
            break
    conn.close()  # 關閉資料庫連線


def disp_10data_b():
    print("建立資料庫連線, 資料庫 :", db_filename)
    conn = sqlite3.connect(db_filename)  # 建立資料庫連線

    print("要事先能知道表單的名稱 prices 與 各欄位的名稱 gdate")
    sqlstr = "SELECT * FROM prices ORDER BY gdate DESC;"
    cursor = conn.execute(sqlstr)
    """ 一次抓5筆資料 抓到完
    dataclip = []
    temp = cursor.fetchmany(5)
    print(temp)
    while temp:
        dataclip.extend(temp)
        temp = cursor.fetchmany(5)
        #print(temp) many
    """

    # 一次抓完
    rows = cursor.fetchall()  # 讀取全部資料成元組串列
    # print(rows)
    dataclip = [(str(i[0]), str(i[1]), str(i[2]), str(i[3])) for i in rows]
    print(dataclip)

    conn.close()  # 關閉資料庫連線


print("中油歷年油價查詢系統")

print("1.顯示歷年油價資訊")
# disp_alldata()
print("2.最近10週油價資訊")
disp_10data_b()

print("------------------------------------------------------------")  # 60個

print("讀取資料庫範例")

db_filename = "data/DataBasePM25.sqlite"

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

# 建立一個表單
sqlstr = """
CREATE TABLE IF NOT EXISTS TablePM25(
no       INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
SiteName TEXT NOT NULL,
PM25     INTEGER
)
"""
cursor.execute(sqlstr)

print("從資料庫讀取資料...")
sqlstr = "SELECT * FROM TablePM25"
cursor = conn.execute(sqlstr)
rows = cursor.fetchall()  # 讀取全部資料成元組串列
length = len(rows)
print("共有", length, "筆資料")
for i in range(length):
    print("第" + str(i + 1) + "筆資料 : ", rows[i])

i = 0
for row in rows:
    print("站名:{}   PM2.5={}".format(row[1], row[2]))
    i += 1
    if i > 10:
        break

conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("從資料庫讀出一筆資料")

db_filename = "data/python01.sqlite"

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
sqlstr = "SELECT * FROM table01 WHERE num = 1"
cursor = conn.execute(sqlstr)
row = cursor.fetchone()

if not row == None:
    print("{}\t{}".format(row[0], row[1]))

conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個

print("從資料庫讀出全部資料")

db_filename = "data/python01.sqlite"

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
sqlstr = "SELECT * FROM table01"
cursor = conn.execute(sqlstr)
do_fetchall(cursor)

conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個

print("從資料庫讀出全部資料")

db_filename = "data/headlines.sqlite"

conn = sqlite3.connect(db_filename)  # 建立資料庫連線

print("讀取全部, 只顯示前10筆")
sqlstr = "SELECT * FROM titles"
cursor = conn.execute(sqlstr)
rows = cursor.fetchall()  # 讀取全部資料成元組串列
length = len(rows)
print("共有", length, "筆資料")
for i in range(length):
    print("第" + str(i + 1) + "筆資料 : ", rows[i])
    if i == 10:
        break

print("只讀前10筆")
sqlstr = "SELECT * FROM titles LIMIT 10"
cursor = conn.execute(sqlstr)
rows = cursor.fetchall()  # 讀取全部資料成元組串列
length = len(rows)
print("共有", length, "筆資料")
for i in range(length):
    print("第" + str(i + 1) + "筆資料 : ", rows[i])

print("從第3筆開始讀5筆資料(從0起算)")
sqlstr = "SELECT * FROM titles LIMIT 3, 5"
cursor = conn.execute(sqlstr)
rows = cursor.fetchall()  # 讀取全部資料成元組串列
length = len(rows)
print("共有", length, "筆資料")
for i in range(length):
    print("第" + str(i + 1) + "筆資料 : ", rows[i])

print("讀5筆資料出來, 從第3筆開始讀 (從0起算)")
sqlstr = "SELECT * FROM titles LIMIT 5 OFFSET 3"
cursor = conn.execute(sqlstr)
rows = cursor.fetchall()  # 讀取全部資料成元組串列
length = len(rows)
print("共有", length, "筆資料")
for i in range(length):
    print("第" + str(i + 1) + "筆資料 : ", rows[i])

conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# sqlite基本範例 其他
# 同一個資料庫內 可以放多個table table名稱不同即可

"""
MySQL將每個資料庫稱為schema

MySQL主要DataType
BOOLEAN
INT
TYNYINT         -128 ~ 127
CHAR(字數)      字串
VARCHAR(字數)   字串
TEXT            字串
NUMERIC         數值
DOUBLE
FLOAT
DECIMAL
SERIAL          序列
DATE
TIME
TIMESTAMP       時間戳
DATETIME
INTERVAL        間隔
GEOMETRY        經緯度

關鍵字        用全大寫
自定義的變數  用小寫加底線

TableName
表格名稱

ColumnName    DataType
欄名      

SQL之資料一定要"方正" ???    不一定
sqlite試用一下輸入NULL 或是用'' ""即可  不一定
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

db_filename = "tmp_db03_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".sqlite"
print("建立資料庫連線, 資料庫 :", db_filename)

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

print("建立表單")

sqlstr = """
CREATE TABLE IF NOT EXISTS table01(
filename VARCHAR(32),
filesize VARCHAR(32)
)
"""
cursor.execute(sqlstr)

print("INSERT")
cursor.execute(
    "INSERT INTO table01" "  (filename, filesize)" "  VALUES" "  (?, ?)",
    ("aaaa.mp4", "12345"),
)

print("SELECT")
# sqlstr =
cursor.execute("SELECT * FROM table01 WHERE filename = ?", ("aaaa.mp4",))

print("Fetchall")
do_fetchall(cursor)

filename = "aaaa.mp4"
cursor.execute("DELETE FROM table01 WHERE filename = ?", (filename,))
conn.commit()  # 更新

print("SELECT")
# sqlstr =
cursor.execute("SELECT * FROM table01 WHERE filename = ?", (filename,))
rows = cursor.fetchall()  # 讀取全部資料成元組串列
length = len(rows)
print("共有", length, "筆資料")
for i in range(length):
    print("第" + str(i + 1) + "筆資料 : ", rows[i])

print("DELETE")
cursor.execute("DELETE FROM table01 WHERE filename = ?", ("aaaa.mp4",))

conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


def disp_data():
    return
    print("顯示所有資料")
    sqlstr = "SELECT * FROM password"
    cursor = conn.execute(sqlstr)
    print("帳號\t密碼")
    print("================")
    for row in cursor:
        print("{}\t{}".format(row[0], row[1]))


conn = sqlite3.connect(db_filename_python02)  # 建立資料庫連線

disp_data()

print("新增資料")

new_name = "John"
# 無 LIKE, 一定要符合大小寫
sqlstr = "SELECT * FROM password WHERE name = '{}'".format(new_name)
# 有 LIKE, 大小寫皆可
sqlstr = "SELECT * FROM password WHERE name LIKE '{}'".format(new_name)

cursor = conn.execute(sqlstr)
row = cursor.fetchone()

if not row == None:
    print("{} 帳號已存在!".format(new_name), "無法再新增")
else:
    new_password = "12345678"
    sqlstr = "INSERT INTO password VALUES('{}', '{}');".format(new_name, new_password)
    conn.execute(sqlstr)
    conn.commit()  # 更新
    print("資料 {} 已儲存完畢".format(new_name))

disp_data()

print("修改資料")

old_name = "David"
sqlstr = "SELECT * FROM password WHERE name = '{}'".format(old_name)
cursor = conn.execute(sqlstr)
row = cursor.fetchone()
# print(row)
if row == None:
    print("{} 帳號不存在!".format(old_name), "無法修改資料")
else:
    print("原來密碼為：{}".format(row[1]))
    new_password = "abcdefg"
    sqlstr = "UPDATE password SET pass = '{}' WHERE name = '{}'".format(
        new_password, old_name
    )
    conn.execute(sqlstr)
    conn.commit()  # 更新
    print("資料 {} 已修改完成".format(old_name))

disp_data()

print("刪除資料")
name = "John"
sqlstr = "SELECT * FROM password WHERE name = '{}'".format(name)
cursor = conn.execute(sqlstr)
row = cursor.fetchone()
if row == None:
    print("{} 帳號不存在!".format(name), "無法刪除資料")
else:
    sqlstr = "DELETE FROM password WHERE name = '{}'".format(name)
    conn.execute(sqlstr)
    conn.commit()  # 更新
    print("刪除{}的資料!：".format(name), "已完成")

disp_data()

conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("測試 例外 的寫法")

conn = sqlite3.connect(":memory:")  # 建立資料庫連線, 記憶體

sqlstr = """
CREATE TABLE IF NOT EXISTS table01(
id   INTEGER PRIMARY KEY,
name VARCHAR UNIQUE
)
"""
conn.execute(sqlstr)

with conn:
    conn.execute("INSERT INTO table01(name) VALUES (?)", ("David",))
    conn.execute("INSERT INTO table01(name) VALUES (?)", ("Lion",))
    conn.execute("INSERT INTO table01(name) VALUES (?)", ("Mouse",))

try:
    with conn:
        conn.execute("INSERT INTO table01(name) VALUES (?)", ("Lion",))
except sqlite3.IntegrityError:
    print("無法重複輸入相同的資料")

sqlstr = "SELECT * FROM table01"  # SELECT * : 取得所有資料
cursor = conn.execute(sqlstr)
do_fetchall(cursor)

conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("測試 TIMESTAMP")

conn = sqlite3.connect(":memory:")  # 建立資料庫連線, 記憶體
cursor = conn.cursor()  # 建立 cursor 物件

sqlstr = """
CREATE TABLE IF NOT EXISTS table01(
my_date      DATE,
my_timestamp TIMESTAMP
)
"""
cursor.execute(sqlstr)

today = datetime.date.today()
now = datetime.datetime.now()

cursor.execute("INSERT INTO table01(my_date, my_timestamp) VALUES (?, ?)", (today, now))
cursor.execute("SELECT my_date, my_timestamp FROM table01")
row = cursor.fetchone()
print(today, "=>", row[0], type(row[0]))
print(now, "=>", row[1], type(row[1]))

cursor.execute(
    'SELECT current_date as "my_date [date]", current_timestamp as "my_timestamp [timestamp]"'
)
row = cursor.fetchone()
print("current_date", row[0], type(row[0]))
print("current_timestamp", row[1], type(row[1]))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("測試 executemany NG")

persons = [("Hugo", "Boss"), ("Calvin", "Klein")]

conn = sqlite3.connect(":memory:")  # 建立資料庫連線, 記憶體

sqlstr = """
CREATE TABLE IF NOT EXISTS person(
firstname,
lastname
)
"""
conn.execute(sqlstr)

"""
# Fill the table
sqlstr = "INSERT INTO person(firstname, lastname) VALUES (?, ?)", persons
conn.executemany(sqlstr)

# Print the table contents
for row in conn.execute("SELECT firstname, lastname FROM person"):
    print(row)

print("I just deleted", conn.execute("DELETE FROM person").rowcount, "rows")
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("測試 序號自動遞增")

db_filename = "tmp_db04_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".sqlite"
print("建立資料庫連線, 資料庫 :", db_filename)

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

print("建立表單")

sqlstr = """
CREATE TABLE IF NOT EXISTS table01(
id      INTEGER PRIMARY KEY AUTOINCREMENT,
name    TEXT NOT NULL,
age     INT NOT NULL,
address CHAR(50),
salary  REAL
)
"""
cursor.execute(sqlstr)

cursor.execute(
    "INSERT INTO table01 (name, age, address, salary) VALUES (?, ?, ?, ?)",
    ("Paul", 32, "California", 20000.00),
)
cursor.execute(
    "INSERT INTO table01 (name, age, address, salary) VALUES (?, ?, ?, ?)",
    ("Allen", 25, "Texas", 15000.00),
)
cursor.execute(
    "INSERT INTO table01 (name, age, address, salary) VALUES (?, ?, ?, ?)",
    ("Teddy", 23, "Norway", 20000.00),
)
cursor.execute(
    "INSERT INTO table01 (name, age, address, salary) VALUES (?, ?, ?, ?)",
    ("Mark", 25, "Rich-Mond ", 65000.00),
)
cursor.execute(
    "INSERT INTO table01 (name, age, address, salary) VALUES (?, ?, ?, ?)",
    ("David", 27, "Texas", 85000.00),
)
cursor.execute(
    "INSERT INTO table01 (name, age, address, salary) VALUES (?, ?, ?, ?)",
    ("Kim", 22, "South-Hall", 45000.00),
)
cursor.execute(
    "INSERT INTO table01 (name, age, address, salary) VALUES (?, ?, ?, ?)",
    ("James", 24, "Houston", 10000.00),
)

conn.commit()  # 更新

conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個

print("讀取資料庫資料, 全部")
print("建立資料庫連線, 資料庫 :", db_filename)
conn = sqlite3.connect(db_filename)  # 建立資料庫連線
sqlstr = "SELECT * FROM table01"  # SELECT * : 取得所有資料
cursor = conn.execute(sqlstr)
do_fetchall(cursor)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
sqlite基本範例 一個 基本款

簡易建立資料庫

增加(13)

刪除資料(1)
讀取全部資料
搜尋資料

刪除資料庫


原始資料 9 筆
	id_num	ename	cname	weight
第1筆 : 5	horse	馬	36
第2筆 : 1	mouse	鼠	3
第3筆 : 4	elephant象	100	(此筆資料錯誤, 應刪除)

第4筆 : 9	ox		48
第5筆 : 2	sheep		66	(此筆資料錯誤, 應為goat 29)

第6筆 : 8	snake		16	(詢問是否刪除此筆資料)
第7筆 : 3	tiger		33

第8筆 : 7	rabbit		8

第9筆 : 6	tiger		240

1. 建立資料庫
2. 新增資料 9筆
3. 修改2號的name
4. 刪除4號
5. 詢問是否刪除8號資料
6. 搜尋

"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

db_filename = "tmp_db05_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".sqlite"
print("建立資料庫連線, 資料庫 :", db_filename)

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

print("建立一個表單")

# PRIMARY KEY 主鍵
# 序號 自動遞增 不可重複
sqlstr = """
CREATE TABLE IF NOT EXISTS table01(
idx    INTEGER PRIMARY KEY AUTOINCREMENT,
id_num INTEGER NOT NULL,
ename  TEXT NOT NULL,
cname  TEXT,
weight INTEGER NOT NULL CHECK(weight > 0) -- 預設錯誤時會顯示
)
"""

cursor.execute(sqlstr)
conn.commit()  # 更新

print("新增資料 2 筆 寫法三, 有些欄位可以不寫, 序號自動遞增")

cursor.execute(
    "INSERT INTO table01 (id_num, ename, cname, weight) VALUES (5, 'horse', '馬', 48)"
)
cursor.execute(
    "INSERT INTO table01 (id_num, ename, cname, weight) VALUES (1, 'mouse', '鼠', 66)"
)
cursor.execute(
    "INSERT INTO table01 (id_num, ename, cname, weight) VALUES (4, 'elephant', '象', 48)"
)

cursor.execute("INSERT INTO table01 (id_num, ename, weight) VALUES (9, 'ox', 48)")
cursor.execute("INSERT INTO table01 (id_num, ename, weight) VALUES (2, 'sheep', 66)")
cursor.execute("INSERT INTO table01 (id_num, ename, weight) VALUES (8, 'snake', 16)")
cursor.execute("INSERT INTO table01 (id_num, ename, weight) VALUES (3, 'tiger', 33)")
cursor.execute("INSERT INTO table01 (id_num, ename, weight) VALUES (7, 'rabbit', 8)")
cursor.execute("INSERT INTO table01 (id_num, ename, weight) VALUES (6, 'tiger', 240)")

for _ in range(123456):
    cursor.execute(
        "INSERT INTO table01 (id_num, ename, weight) VALUES (6, 'tiger', 240)"
    )

conn.commit()  # 更新

conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個

print("用fetchall()讀取 全部資料")
print("建立資料庫連線, 資料庫 :", db_filename)
conn = sqlite3.connect(db_filename)  # 建立資料庫連線
sqlstr = "SELECT * FROM table01"  # SELECT * : 取得所有資料
cursor = conn.execute(sqlstr)
do_fetchall(cursor)

conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("新進測試")

db_filename = "ims_sql/db_ims.sqlite"
db_filename = "data/gasoline.sqlite"
# db_filename = "db_20230703_113217.sqlite"

print("建立資料庫連線, 資料庫 :", db_filename)

conn = sqlite3.connect(db_filename)  # 建立資料庫連線

print("要事先能知道表單的名稱 prices 與 各欄位的名稱 gdate")

sqlstr = "SELECT * FROM prices ORDER BY gdate DESC;"
cursor = conn.execute(sqlstr)

n = 0
for row in cursor:
    print(row)
    print("日期：{}，92無鉛：{}，95無鉛：{}，98無鉛：{}".format(row[0], row[1], row[2], row[3]))
    n = n + 1
    # 讀取10筆資料, 即跳出
    if n == 5:
        break

conn.close()  # 關閉資料庫連線

print("-------------------")
table_name = "prices"
length = 5
show_data_base_contents(db_filename, table_name, length)
print("-------------------")
show_data_base_contents_all(db_filename, table_name)

# ----------------------------------------------------------------

"""

新進測試
測試 SERIAL 測不出效果

測試 TIMESTAMP
測試 DATE
測試 CHECK

測試部分填入資料

"""

print("------------------------------------------------------------")  # 60個
print("新進測試")

db_filename = "tmp_db06_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".sqlite"
print("建立資料庫連線, 資料庫 :", db_filename)

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

# 建立一個表單 table01 + PRIMARY KEY
sqlstr = """
CREATE TABLE IF NOT EXISTS table01(
--id SERIAL PRIMARY KEY,   無效
id_num      INTEGER,
name        VARCHAR(50),
birthday    DATE CHECK(birthday > "1900-01-01"),
work_time   DATE CHECK(work_time > birthday),
money       INTEGER CHECK(money > 0), -- 預設錯誤時會顯示
update_time TIMESTAMP
)
"""

cursor.execute(sqlstr)
conn.commit()  # 更新

id_num = 3
name = "David"
birthday = "2006-03-11"
work_time = "2023-07-11"
money = 2345
update_time = datetime.datetime.now()

sql = "INSERT INTO table01 (id_num, name, birthday, work_time, money, update_time) VALUES ({}, '{}', '{}', '{}', {}, '{}')"
sqlstr = sql.format(id_num, name, birthday, work_time, money, update_time)

# 或者直接寫
# sqlstr = "INSERT INTO table01 (id_num, name, birthday, work_time, money) VALUES (5, 'David', 'xxxx', 'xxxx', 1234, 'xxxx');"

cursor.execute(sqlstr)

print("資料不足時, 部分填入資料")
id_num = 5
name = "Eric"
update_time = datetime.datetime.now()

sql = "INSERT INTO table01 (id_num, name, update_time) VALUES ({}, '{}', '{}')"
sqlstr = sql.format(id_num, name, update_time)
cursor.execute(sqlstr)

conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

conn = sqlite3.connect(db_filename)  # 建立資料庫連線

sqlstr = "SELECT * FROM table01"
cursor = conn.execute(sqlstr)

n = 0
for row in cursor:
    print(row)
    n = n + 1
    # 讀取10筆資料, 即跳出

conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("一次寫入多行的語法 executescript")

db_filename = "tmp_db07_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".sqlite"
print("建立資料庫連線, 資料庫 :", db_filename)

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

conn.execute("CREATE virtual TABLE IF NOT EXISTS table01 using fts3(name, ingredients)")

# 要同質性
conn.executescript(
    """
INSERT INTO table01 (name, ingredients) VALUES ('broccoli stew', 'broccoli peppers cheese tomatoes');
INSERT INTO table01 (name, ingredients) VALUES ('pumpkin stew', 'pumpkin onions garlic celery');
INSERT INTO table01 (name, ingredients) VALUES ('broccoli pie', 'broccoli cheese onions flour');
INSERT INTO table01 (name, ingredients) VALUES ('pumpkin pie', 'pumpkin sugar flour butter');
"""
)

for row in conn.execute(
    "SELECT rowid, name, ingredients FROM table01 WHERE name MATCH 'pie'"
):
    print(row)

# conn.commit()  # 更新

table_name = "table01"
show_data_base_contents_all(db_filename, table_name)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("一次寫入多行的語法 executescript")

conn = sqlite3.connect(":memory:")  # 建立資料庫連線, 記憶體
cursor = conn.cursor()  # 建立 cursor 物件

conn.execute("CREATE TABLE IF NOT EXISTS person(firstname,lastname,age)")
conn.execute("CREATE TABLE IF NOT EXISTS book(title,author,published)")

# 要同質性
conn.executescript(
    """
INSERT INTO book(title, author, published)VALUES ('Dirk Gently''s Holistic Detective Agency','Douglas Adams',1987)
"""
)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

conn = sqlite3.connect(":memory:")  # 建立資料庫連線, 記憶體
cursor = conn.cursor()  # 建立 cursor 物件

sqlstr = """
CREATE TABLE IF NOT EXISTS people(
name_last,
age
)
"""
cursor.execute(sqlstr)

who = "David"
age = 18

cursor.execute("INSERT INTO people VALUES (?, ?)", (who, age))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

db_filename_disk = (
    "tmp_db08_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + "_disk.sqlite"
)

mem_conn = sqlite3.connect(":memory:")  # 建立資料庫連線, 記憶體
disk_conn = sqlite3.connect(db_filename_disk)  # 建立資料庫連線, 磁碟

cursor = mem_conn.cursor()  # 建立 cursor 物件

sqlstr = """
CREATE TABLE IF NOT EXISTS table01(
name_last,
age
)
"""
cursor.execute(sqlstr)

print("目前共有修改資料次數 : ", mem_conn.total_changes)

who = "David"
age = 18

cursor.execute("INSERT INTO table01 VALUES (?, ?)", (who, age))

print("目前共有修改資料次數 : ", mem_conn.total_changes)

cursor.execute("INSERT INTO table01 VALUES (?, ?)", (who, age))
cursor.execute("INSERT INTO table01 VALUES (?, ?)", (who, age))
cursor.execute("INSERT INTO table01 VALUES (?, ?)", (who, age))
print("目前共有修改資料次數 : ", mem_conn.total_changes)

sqlstr = """
CREATE TABLE IF NOT EXISTS stocks(
date   TEXT,
trans  TEXT,
symbol TEXT,
qty    REAL,
price  REAL
)
"""
cursor.execute(sqlstr)

cursor.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

mem_conn.commit()

sqlstr = "SELECT * FROM table01"
cursor.execute(sqlstr)

do_fetchall(cursor)

# 使用 backup 命令将内存数据库备份到磁盘数据库。

# 备份内存数据库到磁盘数据库
mem_conn.backup(disk_conn)

"""
backup 覆蓋
attach 附加
"""

"""
# 将磁盘数据库附加到内存数据库中
mem_conn.execute("ATTACH DATABASE db_filename_disk AS disk_db")

# 执行插入命令将数据插入到磁盘数据库中
mem_conn.execute("INSERT INTO disk_db.example_table VALUES (1, 'example')")
"""

# 关闭数据库连接对象
mem_conn.close()  # 關閉資料庫連線
disk_conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個

db_filename = db_filename_disk
table_name = "table01"
show_data_base_contents_all(db_filename, table_name)

table_name = "stocks"
show_data_base_contents_all(db_filename, table_name)

print("------------------------------------------------------------")  # 60個
print("測 executemany")

stocks = [
    ("2006-01-05", "BUY", "RHAT", 100, 35.14),
    ("2006-03-28", "BUY", "IBM", 1000, 45.0),
    ("2006-04-06", "SELL", "IBM", 500, 53.0),
    ("2006-04-05", "BUY", "MSFT", 1000, 72.0),
]
conn = sqlite3.connect(":memory:")  # 建立資料庫連線, 記憶體

sqlstr = """
CREATE TABLE IF NOT EXISTS stocks(
date    TEXT,
buysell TEXT,
symb    TEXT,
amount  INTEGER,
price   REAL
)
"""
conn.execute(sqlstr)

conn.executemany("INSERT INTO stocks values (?, ?, ?, ?, ?)", stocks)

cursor = conn.cursor()  # 建立 cursor 物件

sqlstr = "SELECT * FROM stocks ORDER BY price"
for row in cursor.execute(sqlstr):
    print(row)

# Output:
# ("2006-01-05", "BUY", "RHAT", 100, 35.14)
# ("2006-03-28", "BUY", "IBM", 1000, 45.0)
# ("2006-04-06", "SELL", "IBM", 500, 53.0)
# ("2006-04-05", "BUY", "MSFT", 1000, 72.0)

sqlstr = "SELECT * FROM stocks ORDER BY price"
cursor.execute(sqlstr)

one_row_data = cursor.fetchone()
print("fetchone", one_row_data)

while one_row_data:
    one_row_data = cursor.fetchone()
    print("fetchone", one_row_data)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

try:
    # 嘗試連接到資料庫
    conn = sqlite3.connect(db_filename_disk)  # 建立資料庫連線
    cursor = conn.cursor()  # 建立 cursor 物件
    # 嘗試執行查詢，可能會引發異常
    sqlstr = "SELECT * FROM non_existent_table"
    cursor.execute(sqlstr)
except sqlite3.Error as e:
    # 捕獲並處理 SQLite 特定的異常
    print(f"Database error: {e}")
except Exception as e:
    # 捕獲並處理其他所有異常
    print(f"Exception occurred: {e}")
finally:
    # 確保資料庫連接被關閉
    conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("測試各種fetch")
"""
fetchone()	#抓一行 tuple
fetchmany(size=cursor.arraysize)	#抓n行 list
fetchall()  # 讀取全部資料成元組串列	#抓取剩下的全部 list

"""

db_filename = "ims_sql/db_ims.sqlite"
db_filename = "data/gasoline.sqlite"
# db_filename  = "db_20230703_113217.sqlite"

print("建立資料庫連線, 資料庫 :", db_filename)

conn = sqlite3.connect(db_filename)  # 建立資料庫連線

sqlstr = "SELECT * FROM prices;"
cursor = conn.execute(sqlstr)

cc = cursor.fetchone()
print(type(cc))
print(cc)

cc = cursor.fetchone()
print(type(cc))
print(cc)

cc = cursor.fetchmany(3)
print(type(cc))
print(cc)

do_fetchall(cursor)

conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個
print("xxxxx new 0717")

conn = sqlite3.connect(":memory:")  # 建立資料庫連線, 記憶體
cursor = conn.cursor()  # 建立 cursor 物件

# 建立一個表單 table01 + PRIMARY KEY

sqlstr = """
CREATE TABLE IF NOT EXISTS table01(
key  INTEGER PRIMARY KEY,
task TEXT
)
"""
cursor.execute(sqlstr)

tasks = (
    "give food to fish",
    "prepare group meeting",
    "fight with a zebra",
)

for task in tasks:
    cursor.execute("INSERT INTO table01 VALUES(NULL, ?)", (task,))

sqlstr = "SELECT * FROM table01"
cursor.execute(sqlstr)

do_fetchall(cursor)

# 更新資料
cursor.execute("UPDATE table01 SET task = 'learn italian' WHERE key = 1")

sqlstr = "SELECT * FROM table01"
cursor.execute(sqlstr)
print(cursor.fetchall())  # 讀取全部資料成元組串列


key_id = 2
# sqlstr =
cursor.execute("SELECT * FROM table01 WHERE key=?", (str(key_id),))
key, task = cursor.fetchone()

print(key)
print(task)

print("程式執行完畢！")

"""
注意：不要使用%s 將字串插入 SQL 命令，
因為它可能使你的程式容易受到 SQL 注入攻擊（請參閱 SQL 注入 ）。
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
新進測試
建立多個表單 要分開寫
"""
print("------------------------------------------------------------")  # 60個

db_filename = "tmp_db09_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".sqlite"
print("建立資料庫連線, 資料庫 :", db_filename)

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

# 建立一個表單 table01 + PRIMARY KEY
sqlstr = """
CREATE TABLE IF NOT EXISTS table01(
id      INTEGER PRIMARY KEY AUTOINCREMENT,
name    TEXT NOT NULL,
age     INT NOT NULL,
address CHAR(50),
salary  REAL
)
"""
cursor.execute(sqlstr)

# conn.commit()  # 更新
# conn.close()  # 關閉資料庫連線

# 刪除三個表單

sqlstr = "DROP TABLE IF EXISTS table01"
cursor.execute(sqlstr)

sqlstr = "DROP TABLE IF EXISTS table02"
cursor.execute(sqlstr)

sqlstr = "DROP TABLE IF EXISTS table03"
cursor.execute(sqlstr)

# 建立一個表單 table01 + PRIMARY KEY
sqlstr = """
CREATE TABLE IF NOT EXISTS table01(
id serial                 NOT NULL,
uid character varying(50) NOT NULL,
PRIMARY KEY (id))
"""
cursor.execute(sqlstr)

# 建立一個表單 table02 + PRIMARY KEY
sqlstr = """
CREATE TABLE IF NOT EXISTS table02(
id serial NOT NULL,
uid character varying(50) NOT NULL,
PRIMARY KEY (id))
"""
cursor.execute(sqlstr)

# 建立一個表單 table03 + PRIMARY KEY
sqlstr = """
CREATE TABLE IF NOT EXISTS table03(
id serial NOT NULL,
bid character varying(50) NOT NULL,
roomtype character varying(20) NOT NULL,
roomamount character varying(5) NOT NULL,
datein character varying(20) NOT NULL,
dateout character varying(20) NOT NULL,
PRIMARY KEY (id)
)
"""
cursor.execute(sqlstr)

# 建立一個表單 table04 + PRIMARY KEY
sqlstr = """
CREATE TABLE IF NOT EXISTS table04(
sid serial NOT NULL,
name character varying(50) NOT NULL,
tel character varying(50),
addr character varying(200),
email character varying(100),
PRIMARY KEY (sid))
"""
cursor.execute(sqlstr)

# 建立一個表單 users1 + PRIMARY KEY
sqlstr = """
CREATE TABLE IF NOT EXISTS users1(
id serial NOT NULL,
uid character varying(50) NOT NULL,
question character varying(250) NOT NULL,
PRIMARY KEY (id))
"""
cursor.execute(sqlstr)

# 建立一個表單 login + PRIMARY KEY
sqlstr = """
CREATE TABLE IF NOT EXISTS login(
id serial NOT NULL,
uid character varying(50) NOT NULL,
state character varying(10) NOT NULL,
PRIMARY KEY (id))
"""
cursor.execute(sqlstr)

# 建立一個表單 users2 + PRIMARY KEY
sqlstr = """
CREATE TABLE IF NOT EXISTS users2(
id serial NOT NULL,
uid character varying(50) NOT NULL,
state character varying(10) NOT NULL,
digit3 character varying(10) NOT NULL,
PRIMARY KEY (id))
"""
cursor.execute(sqlstr)

# 建立一個表單 setting + PRIMARY KEY
sqlstr = """
CREATE TABLE IF NOT EXISTS setting(
id serial NOT NULL,
uid character varying(50) NOT NULL,
lang character varying(10) NOT NULL,
sound character varying(10) NOT NULL,
PRIMARY KEY (id))
"""
cursor.execute(sqlstr)

conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# CREATE + PK
# 建立一個表單 student2 + PRIMARY KEY
sqlstr = """
CREATE TABLE IF NOT EXISTS student2(
id     INTEGER PRIMARY KEY AUTOINCREMENT,
name   TEXT,
gender TEXT
)
"""

# INSERT

conn = sqlite3.connect(db_filename_myInfo1)  # 建立資料庫連線

print("新增資料 INSERT INTO")

new_id = 123
new_name = "david"
new_gender = "M"
x = (new_id, new_name, new_gender)
sqlstr = """INSERT INTO students values(?,?,?)"""
conn.execute(sqlstr, x)
conn.commit()  # 更新

conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

conn = sqlite3.connect(db_filename_myInfo2)  # 建立資料庫連線

print("新增資料 INSERT INTO")

new_name = "david"
new_gender = "M"
x = (new_name, new_gender)
sqlstr = """INSERT INTO student2(name, gender) values(?,?)"""
conn.execute(sqlstr, x)
conn.commit()  # 更新

conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

print("讀取資料 SELECT *")

conn = sqlite3.connect(db_filename_myInfo1)  # 建立資料庫連線
sqlstr = "SELECT * FROM students"
cursor = conn.execute(sqlstr)
for row in cursor:
    print("id = ", row[0])
    print("name = ", row[1])
    print("gender = ", row[2])
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

print("讀取資料 SELECT *")

conn = sqlite3.connect(db_filename_myInfo2)  # 建立資料庫連線
sqlstr = "SELECT * FROM student2"
cursor = conn.execute(sqlstr)
for row in cursor:
    print("id = ", row[0])
    print("name = ", row[1])
    print("gender = ", row[2])
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

print("讀取資料 SELECT *")

conn = sqlite3.connect(db_filename_myInfo1)  # 建立資料庫連線
sqlstr = "SELECT * FROM students"
cursor = conn.execute(sqlstr)

do_fetchall(cursor)

conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

print("讀取資料 SELECT *")

conn = sqlite3.connect(db_filename_myInfo1)  # 建立資料庫連線
cursor = conn.execute("SELECT name FROM students")

do_fetchall(cursor)

conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

print("讀取資料 SELECT *")

conn = sqlite3.connect(db_filename_myInfo1)  # 建立資料庫連線
sqlstr = """
SELECT name, gender FROM students where gender = "F"
"""
cursor = conn.execute(sqlstr)

do_fetchall(cursor)

conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

print("更新資料 UPDATE *")

conn = sqlite3.connect(db_filename_myInfo1)  # 建立資料庫連線
sqlstr = """
UPDATE students
set name = "Tomy"
where id = 1
"""
cursor = conn.execute(sqlstr)
conn.commit()  # 更新
cursor = conn.execute("SELECT name FROM students")

do_fetchall(cursor)

conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

print("刪除資料 DELETE *")

conn = sqlite3.connect(db_filename_myInfo1)  # 建立資料庫連線
sqlstr = "DELETE FROM students where id = 2"
cursor = conn.execute(sqlstr)
conn.commit()  # 更新
cursor = conn.execute("SELECT name FROM students")

do_fetchall(cursor)

conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

db_filename = "tmp_db10_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".sqlite"

conn = sqlite3.connect(db_filename)  # 建立資料庫連線

sqlstr = """
CREATE TABLE IF NOT EXISTS population(
area   TEXT,
male   INTEGER,
female INTEGER,
total  INTEGER
)
"""
conn.execute(sqlstr)

fn = "data/Taipei_Population.csv"
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
        sqlstr = """INSERT INTO population values(?,?,?,?)"""
        conn.execute(sqlstr, x)
        conn.commit()

sqlstr = "SELECT * FROM population"
cursor = conn.execute(sqlstr)
for row in cursor:
    print("區域       = ", row[0])
    print("男性人口數 = ", row[1])
    print("女性人口數 = ", row[2])
    print("總計人口數 = ", row[3])

conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
sqlstr = "SELECT * FROM population"
cursor = conn.execute(sqlstr)

area, male, female, total = [], [], [], []
for row in cursor:  # 將人口資料放入串列
    area.append(row[0])
    male.append(row[1])
    female.append(row[2])
    total.append(row[3])
conn.close()  # 關閉資料庫連線

seq = area
(linemale,) = plt.plot(seq, male, "-*", label="男性人口數")
(linefemale,) = plt.plot(seq, female, "-o", label="女性人口數")
(linetotal,) = plt.plot(seq, total, "-^", label="總計人口數")

plt.legend(handles=[linemale, linefemale, linetotal], loc="best")
plt.title("台北市", fontsize=24)
plt.xlabel("2019年", fontsize=14)
plt.ylabel("人口數", fontsize=14)
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
""" no db
conn = sqlite3.connect("python.sqlite")  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

cursor.execute("INSERT INTO people (name,age,sex) values ('Jee',21,'F')")
r = cursor.execute("DELETE FROM people where age=20")
conn.commit()  # 更新
sqlstr = "SELECT * FROM people"
cursor.execute(sqlstr)

do_fetchall(cursor)

cursor.close()  # 關閉游標
conn.close()  # 關閉資料庫連線
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("讀取資料庫的所有資料")

conn = sqlite3.connect("data/singMatch.db")  # 建立資料庫連線

print("編號\t姓名\t音色50\t技巧30\t儀態20\t總分")
sqlstr = "SELECT 參賽者.編號,參賽者.姓名,音色.音色50, \
       技巧.技巧30,儀態.儀態20 FROM 參賽者 \
       INNER JOIN 音色 ON 音色.編號 = 參賽者.編號 \
       INNER JOIN 技巧 ON 技巧.編號 = 參賽者.編號 \
       INNER JOIN 儀態 ON 儀態.編號 = 參賽者.編號"

rows = conn.execute(sqlstr)
for row in rows:
    tot = row[2] + row[3] + row[4]
    print("%d\t%s\t%d\t%d\t%d\t%d" % (row[0], row[1], row[2], row[3], row[4], tot))

conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

"""
#delete.py

conn = sqlite3.connect("data/singMatch.db")  # 建立資料庫連線

selId = int(input("請輸入要移除的 編號 : "))
sqlstr = "DELETE FROM 參賽者 WHERE 編號 = {0}".format(selId)
conn.execute(sqlstr)
print("編號 = {0} 的記錄 已經刪除....".format(selId))
conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

#insert01.py

conn = sqlite3.connect("data/singMatch.db")  # 建立資料庫連線

print ("請輸入「參賽者」表單的記錄資料")
again = "y"
while again.lower() == "y":
    newId = int(input("編號 : "))
    newName = input("姓名 : ")
    newSex = input("性別 : ")
    newTel = input("電話 : ")
    row = (newId, newName, newSex, newTel)
    sqlstr = "INSERT INTO 參賽者 VALUES(?,?,?,?)"
    conn.execute(sqlstr, row)
    conn.commit()  # 更新
    again = input("是否繼續輸入資料 ? ")
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

#insert02.py

conn = sqlite3.connect("data/singMatch.db")  # 建立資料庫連線

# 建立一個表單 音色
sql1 = "CREATE TABLE IF NOT EXISTS 音色( \
        編號 INTEGER UNIQUE NOT NULL, \
        音色50 INTEGER)"
conn.execute(sql1)

print ("請輸入「音色」表單的記錄資料")
again = "y"
while again.lower() == "y":
    newId = int(input("編號 : "))
    newScore = int(input("音色50 : "))
    row = (newId, newScore)
    sql2 = "INSERT INTO 音色 VALUES(?,?)"
    conn.execute(sql2, row)
    conn.commit()
    again = input("是否繼續輸入資料 ? ")
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

#insert03.py

conn = sqlite3.connect("data/singMatch.db")  # 建立資料庫連線

# 建立一個表單 技巧
sql1 = "CREATE TABLE IF NOT EXISTS 技巧( \
         編號 INTEGER UNIQUE NOT NULL, \
         技巧30 INTEGER)"
conn.execute(sql1)

print ("請輸入「技巧」表單的記錄資料")
again = "y"
while again.lower() == "y":
    newId = int(input("編號 : "))
    newScore = int(input("技巧30 : "))
    row = (newId, newScore)
    sql2 = "INSERT INTO 技巧 VALUES(?,?)"
    conn.execute(sql2, row)
    conn.commit()
    again = input("是否繼續輸入資料 ? ")
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

#insert04.py

conn = sqlite3.connect("data/singMatch.db")  # 建立資料庫連線

# 建立一個表單 儀態
sql1 = "CREATE TABLE IF NOT EXISTS 儀態( \
         編號 INTEGER UNIQUE NOT NULL, \
         儀態20 INTEGER)"
conn.execute(sql1)

print ("請輸入「儀態」表單的記錄資料")
again = "y"
while again.lower() == "y":
    newId = int(input("編號 : "))
    newScore = int(input("儀態20 : "))
    row = (newId, newScore)
    sql2 = "INSERT INTO 儀態 VALUES(?,?)"
    conn.execute(sql2, row)
    conn.commit()
    again = input("是否繼續輸入資料 ? ")
conn.close()  # 關閉資料庫連線
"""
print("------------------------------")  # 30個

# match.py


def fnCreateTable():
    # 建立一個表單 參賽者
    sql1 = "CREATE TABLE IF NOT EXISTS 參賽者( \
            編號 INTEGER UNIQUE NOT NULL, \
            姓名 TEXT, \
            性別 TEXT, \
            電話 TEXT)"
    conn.execute(sql1)

    # 建立一個表單 音色
    sql2 = "CREATE TABLE IF NOT EXISTS 音色( \
            編號 INTEGER UNIQUE NOT NULL, \
            音色50 INTEGER)"
    conn.execute(sql2)

    # 建立一個表單 技巧
    sql3 = "CREATE TABLE IF NOT EXISTS 技巧( \
            編號 INTEGER UNIQUE NOT NULL, \
            技巧30 INTEGER)"
    conn.execute(sql3)

    # 建立一個表單 儀態
    sql4 = "CREATE TABLE IF NOT EXISTS 儀態( \
            編號 INTEGER UNIQUE NOT NULL, \
            儀態20 INTEGER)"
    conn.execute(sql4)

    anykey = input("請按 <enter>鍵 繼續...")


def fnInsert01():
    print("\n請輸入「參賽者」表單的記錄資料")
    again = "y"
    while again.lower() == "y":
        newId = int(input("編號 : "))
        newName = input("姓名 : ")
        newSex = input("性別 : ")
        newTel = input("電話 : ")
        row = (newId, newName, newSex, newTel)
        sqlstr = "INSERT INTO 參賽者 VALUES(?,?,?,?)"
        conn.execute(sqlstr, row)
        conn.commit()
        again = input("是否繼續輸入資料 ? ")


def fnSelect01():
    sqlstr = "SELECT * FROM 參賽者"
    data = conn.execute(sqlstr)
    print("編號\t姓名\t性別\t電話")
    for rec in data:
        print("%d\t%s\t%s\t%s" % (rec[0], rec[1], rec[2], rec[3]))
    anykey = input("請按 <enter>鍵 繼續...")


def fnDelect01():
    delId = int(input("請輸入要刪除的參賽者編號: "))
    sqlstr = "DELETE FROM 參賽者 WHERE 編號 = {0}".format(delId)
    conn.execute(sqlstr)
    conn.commit()
    anykey = input("請按 <enter>鍵 繼續...")


def fnInsert02():
    print("\n請輸入「音色」表單的記錄資料")
    again = "y"
    while again.lower() == "y":
        newId = int(input("編號 : "))
        newScore = int(input("音色50 : "))
        row = (newId, newScore)
        sqlstr = "INSERT INTO 音色 VALUES(?,?)"
        conn.execute(sqlstr, row)
        conn.commit()
        again = input("是否繼續輸入資料 ? ")


def fnSelect02():
    sqlstr = "SELECT * FROM 音色"
    data = conn.execute(sqlstr)
    print("編號\t音色50")
    for rec in data:
        print("%d\t%d" % (rec[0], rec[1]))
    anykey = input("請按 <enter>鍵 繼續...")


def fnDelect02():
    delId = int(input("請輸入要刪除的音色編號: "))
    sqlstr = "DELETE FROM 音色 WHERE 編號 = {0}".format(delId)
    conn.execute(sqlstr)
    conn.commit()
    anykey = input("請按 <enter>鍵 繼續...")


def fnInsert03():
    print("\n請輸入「技巧」表單的記錄資料")
    again = "y"
    while again.lower() == "y":
        newId = int(input("編號 : "))
        newScore = int(input("技巧30 : "))
        row = (newId, newScore)
        sqlstr = "INSERT INTO 技巧 VALUES(?,?)"
        conn.execute(sqlstr, row)
        conn.commit()
        again = input("是否繼續輸入資料 ? ")


def fnSelect03():
    sqlstr = "SELECT * FROM 技巧"
    data = conn.execute(sqlstr)
    print("編號\t技巧30")
    for rec in data:
        print("%d\t%d" % (rec[0], rec[1]))
    anykey = input("請按 <enter>鍵 繼續...")


def fnDelect03():
    delId = int(input("請輸入要刪除的技巧編號: "))
    sqlstr = "DELETE FROM 技巧 WHERE 編號 = {0}".format(delId)
    conn.execute(sqlstr)
    conn.commit()
    anykey = input("請按 <enter>鍵 繼續...")


def fnInsert04():
    print("\n請輸入「儀態」表單的記錄資料")
    again = "y"
    while again.lower() == "y":
        newId = int(input("編號 : "))
        newScore = int(input("儀態20 : "))
        row = (newId, newScore)
        sqlstr = "INSERT INTO 儀態 VALUES(?,?)"
        conn.execute(sqlstr, row)
        conn.commit()
        again = input("是否繼續輸入資料 ? ")


def fnSelect04():
    sqlstr = "SELECT * FROM 儀態"
    data = conn.execute(sqlstr)
    print("編號\t儀態20")
    for rec in data:
        print("%d\t%d" % (rec[0], rec[1]))
    anykey = input("請按 <enter>鍵 繼續...")


def fnDelect04():
    delId = int(input("請輸入要刪除的儀態編號: "))
    sqlstr = "DELETE FROM 儀態 WHERE 編號 = {0}".format(delId)
    conn.execute(sqlstr)
    conn.commit()
    anykey = input("請按 <enter>鍵 繼續...")


def fnRelation():
    print("編號\t姓名\t音色50\t技巧30\t儀態20\t總分")
    sqlstr = "SELECT 參賽者.編號,參賽者.姓名,音色.音色50, \
           技巧.技巧30,儀態.儀態20 FROM 參賽者 \
           INNER JOIN 音色 ON 音色.編號 = 參賽者.編號 \
           INNER JOIN 技巧 ON 技巧.編號 = 參賽者.編號 \
           INNER JOIN 儀態 ON 儀態.編號 = 參賽者.編號"
    rows = conn.execute(sqlstr)
    for row in rows:
        tot = row[2] + row[3] + row[4]
        print("%d\t%s\t%d\t%d\t%d\t%d" % (row[0], row[1], row[2], row[3], row[4], tot))
    anykey = input("請按 <enter>鍵 繼續...")


#####  主程式  #####
conn = sqlite3.connect("data/singMatch.db")  # 建立資料庫連線
while True:
    print("\n*** 博碩歌唱比賽評分管理系統 ***")
    print("    1. 建立表單")
    print("    2. 管理 參賽者 表單")
    print("    3. 管理 音色 表單")
    print("    4. 管理 技巧 表單")
    print("    5. 管理 儀態 表單")
    print("    6. 顯示 比賽總成績")
    print("    7. 離開系統")
    print("===========================")
    n = input("請選擇操作項目: ")

    if n == "1":
        fnCreateTable()
    elif n == "2":
        while True:
            print("\n** 管理 參賽者 表單 **")
            print("   1. 新增記錄")
            print("   2. 查詢記錄")
            print("   3. 刪除記錄")
            print("   4. 回上一層操作")
            print("-------------------------")
            n2 = int(input("請選擇管理項目: "))
            if n2 == 1:
                fnInsert01()
            elif n2 == 2:
                fnSelect01()
            elif n2 == 3:
                fnDelect01()
            elif n2 == 4:
                break
    elif n == "3":
        while True:
            print("\n** 管理 音色 表單 **")
            print("   1. 新增記錄")
            print("   2. 查詢記錄")
            print("   3. 刪除記錄")
            print("   4. 回上一層操作")
            print("-------------------------")
            n3 = int(input("請選擇管理項目: "))
            if n3 == 1:
                fnInsert02()
            elif n3 == 2:
                fnSelect02()
            elif n3 == 3:
                fnDelect02()
            elif n3 == 4:
                break
    elif n == "4":
        while True:
            print("\n** 管理 技巧 表單 **")
            print("   1. 新增記錄")
            print("   2. 查詢記錄")
            print("   3. 刪除記錄")
            print("   4. 回上一層操作")
            print("-------------------------")
            n4 = int(input("請選擇管理項目: "))
            if n4 == 1:
                fnInsert03()
            elif n4 == 2:
                fnSelect03()
            elif n4 == 3:
                fnDelect03()
            elif n4 == 4:
                break
    elif n == "5":
        while True:
            print("\n** 管理 儀態 表單 **")
            print("   1. 新增記錄")
            print("   2. 查詢記錄")
            print("   3. 刪除記錄")
            print("   4. 回上一層操作")
            print("-------------------------")
            n5 = int(input("請選擇管理項目: "))
            if n5 == 1:
                fnInsert04()
            elif n5 == 2:
                fnSelect04()
            elif n5 == 3:
                fnDelect04()
            elif n5 == 4:
                break
    elif n == "6":
        fnRelation()
    elif n == "7":
        break

conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

# relation.py

conn = sqlite3.connect("data/singMatch.db")  # 建立資料庫連線

print("編號\t姓名\t音色50\t技巧30\t儀態20\t總分")
sqlstr = "SELECT 參賽者.編號,參賽者.姓名,音色.音色50, \
       技巧.技巧30,儀態.儀態20 FROM 參賽者 \
       INNER JOIN 音色 ON 音色.編號 = 參賽者.編號 \
       INNER JOIN 技巧 ON 技巧.編號 = 參賽者.編號 \
       INNER JOIN 儀態 ON 儀態.編號 = 參賽者.編號"
rows = conn.execute(sqlstr)
for row in rows:
    tot = row[2] + row[3] + row[4]
    print("%d\t%s\t%d\t%d\t%d\t%d" % (row[0], row[1], row[2], row[3], row[4], tot))
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

# select01.py

conn = sqlite3.connect("data/singMatch.db")  # 建立資料庫連線
sqlstr = "SELECT * FROM 參賽者"
data = conn.execute(sqlstr)  # 執行SQL指令,傳回記錄資料
print("編號\t姓名\t性別\t電話")
for rec in data:
    print("%d\t%s\t%s\t%s" % (rec[0], rec[1], rec[2], rec[3]))
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

# select02.py

conn = sqlite3.connect("data/singMatch.db")  # 建立資料庫連線
sqlstr = "SELECT 姓名,電話 FROM 參賽者"
data = conn.execute(sqlstr)  # 執行SQL指令,傳回記錄資料
print("姓名\t電話")
for rec in data:
    print("%s\t%s" % (rec[0], rec[1]))
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

# select03.py

conn = sqlite3.connect("data/singMatch.db")  # 建立資料庫連線
selId = int(input("請輸入要查詢的 編號 : "))
sqlstr = "SELECT * FROM 參賽者 WHERE 編號 = {0}".format(selId)
data = conn.execute(sqlstr)  # 執行SQL指令,傳回記錄資料
print("編號\t姓名\t性別\t電話")
for rec in data:
    print("%d\t%s\t%s\t%s" % (rec[0], rec[1], rec[2], rec[3]))
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

# select04.py

conn = sqlite3.connect("data/singMatch.db")  # 建立資料庫連線
selName = input("請輸入要查詢的 姓名 : ")
sqlstr = 'SELECT * FROM 參賽者 WHERE 姓名 = "{0}"'.format(selName)
data = conn.execute(sqlstr)  # 執行SQL指令,傳回記錄資料
print("編號\t姓名\t性別\t電話")
for rec in data:
    print("%d\t%s\t%s\t%s" % (rec[0], rec[1], rec[2], rec[3]))
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

# table.py

conn = sqlite3.connect("data/singMatch.db")  # 建立資料庫連線

# 建立一個表單 參賽者
sqlstr = """
CREATE TABLE IF NOT EXISTS 參賽者(
編號 INTEGER UNIQUE NOT NULL,
姓名 TEXT,
性別 TEXT,
電話 TEXT
)
"""
conn.execute(sqlstr)
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

# update.py

conn = sqlite3.connect("data/singMatch.db")  # 建立資料庫連線
selId = int(input("請輸入要異動的 編號 : "))
print("\n選擇要異動的欄位名稱...")
field = input("1.姓名  2.性別  3.電話 ..... ? ")
if field == "1":
    newName = input("姓名 :")
    sqlstr = 'UPDATE 參賽者 \
           SET 姓名 = "{0}" \
           WHERE 編號 = {1}'.format(
        newName, selId
    )
elif field == "2":
    newSex = input("性別 :")
    sqlstr = 'UPDATE 參賽者 \
           SET 性別 = "{0}" \
           WHERE 編號 = {1}'.format(
        newSex, selId
    )
elif field == "3":
    newTel = input("電話 :")
    sqlstr = 'UPDATE 參賽者 \
           SET 電話 = "{0}" \
           WHERE 編號 = {1}'.format(
        newTel, selId
    )

conn.execute(sqlstr)
conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

db_filename_tips = (
    "tmp_db11_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + "_tips.sqlite"
)

conn = sqlite3.connect(db_filename_tips)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

# 建立一個表單 table_tips

sqlstr = """
CREATE TABLE IF NOT EXISTS table_tips(
NAME    TEXT NOT NULL,
ADDRESS CHAR(50),
BILL    REAL
)
"""
cursor.execute(sqlstr)

cursor.execute(
    "INSERT INTO table_tips (NAME,ADDRESS,BILL) \
      VALUES ('Zhang', 'Beijing', 1004.00 )"
)
# 向表中輸入數據

sqlstr = "SELECT * FROM table_tips"
cursors = cursor.execute(sqlstr)
for row in cursors:
    print(row)
conn.commit()
conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("查詢資料庫")
conn = sqlite3.connect(db_filename_books)  # 建立資料庫連線

# 執行SQL指令SELECT
sqlstr = "SELECT * FROM Books"
cursor = conn.execute(sqlstr)
# 取出查詢結果的每一筆記錄
print("ID\tTitle\t\t\tPrice")
for row in cursor:
    print(row[0], "\t", row[1], "\t", row[2])
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

print("加入資料庫")

conn = sqlite3.connect(db_filename_books)  # 建立資料庫連線

new_id = "D0002d"
new_title = "MySQL資料庫系統333"
new_price = "600"

# 建立SQL指令INSERT字串
sql = "INSERT INTO Books (id, title, price) VALUES ('{0}','{1}',{2})"
sqlstr = sql.format(new_id, new_title, new_price)
print(sqlstr)

cursor = conn.execute(sqlstr)
print(cursor.rowcount)

conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

print("加入資料庫 字典")

d = {"id": "D0003", "title": "MongoDB資料庫系統", "price": 650}  # 字典

conn = sqlite3.connect(db_filename_books)  # 建立資料庫連線

# 建立SQL指令INSERT字串
sql = "INSERT INTO Books (id, title, price) VALUES ('{0}','{1}',{2})"
sqlstr = sql.format(d["id"], d["title"], d["price"])
print(sqlstr)

cursor = conn.execute(sqlstr)
print(cursor.rowcount)

conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

print("更新資料庫")

conn = sqlite3.connect(db_filename_books)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

sqlstr1 = """UPDATE Books SET price=650 WHERE id='D0002' """
sqlstr2 = """UPDATE Books SET price=700 WHERE id='D0003' """
try:
    cursor.execute(sqlstr1)
    cursor.execute(sqlstr2)
    conn.commit()  # 更新
    print("更新 2 筆記錄...")
except:
    conn.rollback()
    print("更新記錄失敗...")
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

conn = sqlite3.connect(db_filename_books)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

sqlstr1 = "DELETE FROM Books WHERE id='D0002'"
sqlstr2 = "DELETE FROM Books WHERE id='D0003'"
try:
    cursor.execute(sqlstr1)
    cursor.execute(sqlstr2)
    conn.commit()  # 更新
    print("刪除 2 筆記錄...")
except:
    conn.rollback()
    print("刪除記錄失敗...")
conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

db_filename_school = (
    "tmp_db12_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + "_school.sqlite"
)

print("新建資料庫")

conn = sqlite3.connect(db_filename_school)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

# 建立一個表單 scores + PRIMARY KEY
sqlstr = """
CREATE TABLE IF NOT EXISTS scores(
id      INTEGER PRIMARY KEY NOT NULL,
name    TEXT NOT NULL,
chinese INTEGER NOT NULL,
english INTEGER NOT NULL,
math    INTEGER NOT NULL
)
"""
cursor.execute(sqlstr)

print("加入資料庫")
cursor.execute('INSERT INTO scores values(1, "葉大雄", 65, 62, 40)')
cursor.execute('INSERT INTO scores values(2, "陳靜香", 85, 90, 87)')
cursor.execute('INSERT INTO scores values(3, "王聰明", 92, 90, 95)')
conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

print("加入資料庫")

conn = sqlite3.connect(db_filename_school)  # 建立資料庫連線

# 定義資料串列
datas = [[11, "葉大雄", 65, 62, 40], [12, "陳靜香", 85, 90, 87], [13, "王聰明", 92, 90, 95]]

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

print("------------------------------")  # 30個

print("更新資料庫")

conn = sqlite3.connect(db_filename_school)  # 建立資料庫連線

# 更新資料
conn.execute("UPDATE scores SET name='{}' WHERE id={}".format("林胖虎", 1))
conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

print("刪除資料庫")

conn = sqlite3.connect(db_filename_school)  # 建立資料庫連線

# 刪除資料
conn.execute("DELETE FROM scores WHERE id={}".format(1))
conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

print("查詢資料庫")

conn = sqlite3.connect(db_filename_school)  # 建立資料庫連線

sqlstr = "SELECT * FROM scores"
cursor = conn.execute(sqlstr)
do_fetchall(cursor)

conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

print("查詢資料庫")

# fetchone.py

conn = sqlite3.connect(db_filename_school)  # 建立資料庫連線

sqlstr = "SELECT * FROM scores"
cursor = conn.execute(sqlstr)
row = cursor.fetchone()
print(row[0], row[1])
conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

db_filename_mydb = (
    "tmp_db13_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + "_mydb.sqlite"
)

print("建立資料庫")

name = "david"
conn = sqlite3.connect(db_filename_mydb)  # 建立資料庫連線

# 建立一個表單 mytable
sqlstr = """
CREATE TABLE IF NOT EXISTS mytable(
姓名     TEXT,
打卡時間 TEXT
)
"""
conn.execute(sqlstr)

print("加入資料庫")
# 取得現在時間
save_time = datetime.datetime.now().strftime("%Y-%m-%d %H.%M.%S")

# 新增一筆資料的 SQL 語法
sqlstr = f'INSERT INTO mytable values("{name}", "{save_time}")'
conn.execute(sqlstr)

conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

print("讀取資料庫")

conn = sqlite3.connect(db_filename_mydb)  # 建立資料庫連線

sqlstr = "SELECT * FROM mytable"  # 選取表單中所有資料的 SQL 語法
cursor = conn.execute(sqlstr)  # 執行 SQL 語法得到 cursor 物件

do_fetchall(cursor)

conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

db_filename_contact = (
    "tmp_db14_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + "_contact.sqlite"
)

conn = sqlite3.connect(db_filename_contact)  # 建立資料庫連線

# 建立一個表單 + PRIMARY KEY
sqlstr = """
CREATE TABLE IF NOT EXISTS contact(
id   INTEGER PRIMARY KEY NOT NULL,
name TEXT NOT NULL,
tel  TEXT NOT NULL
)
"""
conn.execute(sqlstr)
conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

conn = sqlite3.connect(db_filename_contact)  # 建立資料庫連線

sqlstr = "SELECT * FROM contact"
cursor = conn.execute(sqlstr)
do_fetchall(cursor)

conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

# fetchone.py

conn = sqlite3.connect("data/test_bbb.sqlite")  # 建立資料庫連線

sqlstr = "SELECT * FROM contact"
cursor = conn.execute(sqlstr)
row = cursor.fetchone()
print(row[0], row[1])

conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

# sqlite_crud2.py

conn = sqlite3.connect(db_filename_contact)  # 建立資料庫連線

# 定義資料串列
datas = [
    [1, "David", "02-123456789"],
    [2, "Lily", "02-987654321"],
]
for data in datas:
    # 新增資料
    conn.execute(
        "INSERT INTO contact (id, name, tel) VALUES \
                 ({}, '{}', '{}')".format(
            data[0], data[1], data[2]
        )
    )
conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

# sqlite_crud3.py

conn = sqlite3.connect(db_filename_contact)  # 建立資料庫連線

# 更新資料
conn.execute("UPDATE contact SET name='{}' WHERE id={}".format("Ken", 1))
conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

# sqlite_crud4.py

conn = sqlite3.connect(db_filename_contact)  # 建立資料庫連線

# 刪除資料
conn.execute("DELETE FROM contact WHERE id={}".format(1))
conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

# sqlite_cursor.py

conn = sqlite3.connect(db_filename_contact)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

# 建立一個表單 table01 + PRIMARY KEY
sqlstr = """
CREATE TABLE IF NOT EXISTS table01(
id   INTEGER PRIMARY KEY NOT NULL,
name TEXT NOT NULL,
tel  TEXT NOT NULL
)
"""
cursor.execute(sqlstr)

# 新增一筆記錄
sqlstr = 'INSERT INTO table01 values(1, "David", "02-1234567")'
cursor.execute(sqlstr)
conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

db_filename = "tmp_db15_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".sqlite"

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

sqlstr = """
CREATE TABLE IF NOT EXISTS table01(
symbol TEXT,
shares INTEGER,
price  REAL
)
"""

cursor.execute(sqlstr)
conn.commit()  # 更新

stocks = [
    ("GOOG", 100, 490.1),
    ("AAPL", 50, 545.75),
    ("FB", 150, 7.45),
    ("HPQ", 75, 33.2),
]
cursor.executemany("INSERT INTO table01 values (?,?,?)", stocks)
conn.commit()  # 更新

sqlstr = "SELECT * FROM table01"
for row in conn.execute(sqlstr):
    print(row)

min_price = 12
# sqlstr =
for row in conn.execute("SELECT * FROM table01 where price >= ?", (min_price,)):
    print(row)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

db_filename = "tmp_db16_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".sqlite"

print("新建資料庫")

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件  # 獲得資料庫游標

# 建立一個表單 table01
sqlstr = """
CREATE TABLE IF NOT EXISTS table01(
title        TEXT,
username     TEXT,
email        TEXT,
message_text TEXT,
date         TEXT
)
"""
conn.execute(sqlstr)

print("加入資料庫")

name = "david"
mail = "david@lion.mouse"
site = "MacOS"
message = "delicious"
time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
cursor.execute(
    "INSERT INTO table01 VALUES(?,?,?,?,?)", (name, mail, site, message, time)
)

print("加入資料庫")

title = "AAAA"
username = "BBBB"
email = "CCCC"
message_text = "DDDD"
conn.execute(
    "INSERT INTO table01 (title, username, email, message_text, date) VALUES (?, ?, ?, ?, DATETIME('now'))",
    (title, username, email, message_text),
)

sqlstr = "SELECT * FROM table01"
cursor.execute(sqlstr)

do_fetchall(cursor)

cursor.close()  # 關閉游標
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

print("讀取資料庫")

conn = sqlite3.connect(db_filename)  # 建立資料庫連線

# 建立一個表單 table01
sqlstr = """
CREATE TABLE IF NOT EXISTS table01(
title        TEXT,
username     TEXT,
email        TEXT,
message_text TEXT,
date         TEXT
)
"""
conn.execute(sqlstr)

sqlstr = "SELECT * FROM table01"
cursor = conn.execute(sqlstr)

do_fetchall(cursor)

conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

print("讀取資料庫")

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
# 建立一個表單 table01
sqlstr = 'CREATE TABLE IF NOT EXISTS table01("title" TEXT, "username" TEXT, "email" TEXT, "message_text" TEXT, "date" TEXT)'
conn.execute(sqlstr)
sqlstr = "SELECT * FROM table01"
cursor = conn.execute(sqlstr)

do_fetchall(cursor)

conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import numpy as np

db_filename = "data/gasoline.sqlite"

print("油價走勢圖")

print("建立資料庫連線, 資料庫 : " + db_filename)
conn = sqlite3.connect(db_filename)  # 建立資料庫連線
sqlstr = "SELECT * FROM prices ORDER BY gdate;"
cursor = conn.execute(sqlstr)

data = []
cnt = 0
for row in cursor:
    data.append(list(row))
    cnt = cnt + 1
    """
    if cnt == 20:
        break
    """
x = np.arange(0, len(data))
dataset = [list(), list(), list()]
for i in range(0, len(data)):
    for j in range(0, 3):
        dataset[j].append(data[i][j + 1])

w = np.array(dataset[0])  # 92
y = np.array(dataset[1])  # 95
z = np.array(dataset[2])  # 98

plt.ylabel("NTD$")
plt.xlabel("Weeks ( {} --- {} )".format(data[0][0], data[len(data) - 1][0]))
plt.plot(x, w, color="blue", label="92")
plt.plot(x, y, color="red", label="95")
plt.plot(x, z, color="green", label="98")
plt.xlim(0, len(data))
plt.ylim(10, 40)
plt.title("台灣油價走勢圖")
plt.legend()
show()

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

"""
sql能否做到部分填滿? 可以

SQL
資料 計畫 問題

AQI 之 sqlit應加入更新時間(update_time)一欄

print("------------------------------------------------------------")  # 60個

DB Browser for SQLite
https://sqlitebrowser.org/

def fetch_data():
    url = 'http://new.cpc.com.tw/division/mb/oil-more4.aspx'

    html = requests.get(url).text
    sp = BeautifulSoup(html, 'html.parser')
    data = sp.find_all('span', {'id':'Showtd'})
    rows = data[0].find_all('tr')

    prices = list()
    for row in rows:
        cols = row.find_all('td')
        if len(cols[1].text) > 0:
            item = [cols[0].text, cols[1].text, \
                    cols[2].text, cols[3].text]
            prices.append(item)
    for p in prices:
        sqlstr = "select * from prices where gdate='{}';".format(p[0])
        cursor = conn.execute(sqlstr)
        if len(cursor.fetchall()) == 0:
            g92 = 0 if p[1]=='' else float(p[1])
            g95 = 0 if p[2]=='' else float(p[2])
            g98 = 0 if p[3]=='' else float(p[3])
            sqlstr = "insert into prices values('{}', {}, {}, {});". \
                format(p[0], g92, g95, g98)
            print(sqlstr)
            conn.execute(sqlstr)
            conn.commit()

return "CREATE TABLE %s (%s PRIMARY KEY %s)" % (self.name, fields, keys)

    v = db.OpenView("SELECT * FROM `%s`" % table)
    v = db.OpenView("INSERT INTO _Streams (Name, Data) VALUES ('%s', ?)" % name)

# 修改 id 為 1 的資料
conn.execute("UPDATE scores SET name='{}' WHERE id={}".format('林胖虎', 1))

# 刪除資料 id 為 1 之資料
conn.execute("DELETE FROM scores WHERE id={}".format(1))

# 新增記錄
cursor.execute('insert into scores values(1, "葉大雄", 65, 62, 40)')
cursor.execute('insert into scores values(2, "陳靜香", 85, 90, 87)')
cursor.execute('insert into scores values(3, "王聰明", 92, 90, 95)')


# 定義資料串列
datas = [[7,'葉大雄',65,62,40],
        [8,'陳靜香',85,90,87],
        [9,'王聰明',92,90,95]]

# 新增資料
for data in datas:
    conn.execute("INSERT INTO scores (id, name, chinese, english, math) VALUES \
                 ({}, '{}', {}, {}, {})".format(data[0], data[1], data[2], data[3], data[4]))

----------------------------------------------------------------

dbfile = "applenews.db"
conn = sqlite3.connect(dbfile)

sql_str = "select count(*) from news;"
result = conn.execute(sql_str)
count = result.fetchone()[0]
print(count)

    sql_str = "select count(*) from news where url='{}';".format(content_url)
    result = conn.execute(sql_str)
    count = result.fetchone()[0]

        sql_str = "insert into news(url, title, content) values('{}','{}','{}');".format(content_url, title, data)
        conn.execute(sql_str)

----------------------------------------------------------------

db = sqlite3.connect("db")

cursor = db.cursor()

cursor.execute("create table Course ( " +
               "courseId char(5), subjectId char(4) not null, " +
               "courseNumber integer, title varchar(50) not null, " +
               "numOfCredits integer, primary key (courseId))")

cursor.execute("insert into Course (courseId, subjectId, " + 
               " courseNumber, title, numOfCredits) " + 
               "values ('11113', 'CSCI', '3720', 'Database Systems', 3)")

cursor.execute("insert into Course (courseId, subjectId, " + 
               " courseNumber, title, numOfCredits) " + 
               "values ('11111', 'CSCI', '1301', 'Introduction to Programming', 3)")
db.commit()

cursor.execute("select * from Course")

rows = cursor.fetchall()

print(rows)

db.close()

----------------------------------------------------------------

CREATE TABLE IF NOT EXISTS "Orders"
(
  "Id" INTEGER PRIMARY KEY, 
  "CustomerId" VARCHAR(8000) NULL, 
  "EmployeesId" INTEGER NOT NULL, 
  "orderdate" VARCHAR(8000) NULL, 
  "RequiredDate" VARCHAR(8000) NULL, 
  "ShippedDate" VARCHAR(8000) NULL, 
  "ShipVia" INTEGER NULL, 
  "Freight" DECIMAL NOT NULL, 
  "ShipName" VARCHAR(8000) NULL, 
  "ShipAddress" VARCHAR(8000) NULL, 
  "ShipCity" VARCHAR(8000) NULL, 
  "ShipRegion" VARCHAR(8000) NULL, 
  "ShipPostalCode" VARCHAR(8000) NULL, 
  "ShipCountry" VARCHAR(8000) NULL 
)

CREATE TABLE IF NOT EXISTS "Orders"
(
  "Id" INTEGER PRIMARY KEY, 
  "CustomerId" VARCHAR(8000) NULL, 
  "EmployeesId" INTEGER NOT NULL, 
  "orderdate" VARCHAR(8000) NULL, 
  "RequiredDate" VARCHAR(8000) NULL, 
  "ShippedDate" VARCHAR(8000) NULL, 
  "ShipVia" INTEGER NULL, 
  "Freight" DECIMAL NOT NULL, 
  "ShipName" VARCHAR(8000) NULL, 
  "ShipAddress" VARCHAR(8000) NULL, 
  "ShipCity" VARCHAR(8000) NULL, 
  "ShipRegion" VARCHAR(8000) NULL, 
  "ShipPostalCode" VARCHAR(8000) NULL, 
  "ShipCountry" VARCHAR(8000) NULL 
)

CREATE TABLE IF NOT EXISTS "OrderDetails"
(
  "Id" VARCHAR(8000) PRIMARY KEY, 
  "OrderId" INTEGER NOT NULL, 
  "ProductId" INTEGER NOT NULL, 
  "UnitPrice" DECIMAL NOT NULL, 
  "Quantity" INTEGER NOT NULL, 
  "Discount" DOUBLE NOT NULL 
)

CREATE TABLE IF NOT EXISTS "Customers"
(
  "Id" VARCHAR(8000) PRIMARY KEY, 
  "CompanyName" VARCHAR(8000) NULL, 
  "ContactName" VARCHAR(8000) NULL, 
  "ContactTitle" VARCHAR(8000) NULL, 
  "Address" VARCHAR(8000) NULL, 
  "City" VARCHAR(8000) NULL, 
  "Region" VARCHAR(8000) NULL, 
  "PostalCode" VARCHAR(8000) NULL, 
  "Country" VARCHAR(8000) NULL, 
  "Phone" VARCHAR(8000) NULL, 
  "Fax" VARCHAR(8000) NULL 
)
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
db : 資料庫 db
table : 表單 資料表(x)

print("建立一個表單")

# 固定指令用全大寫

# AUTOINCREMENT 自動遞增
SQLite Autoincrement（自動遞增）
SQLite 的 AUTOINCREMENT 是一個關鍵字，用于表中的字段值自動遞增。
我們可以在創建表時在特定的列名稱上使用 AUTOINCREMENT 關鍵字實現該字段值的自動增加。
關鍵字 AUTOINCREMENT 只能用于整型（INTEGER）字段。

# CREATE 建立
CREATE TABLE IF NOT EXISTS table01
# PRIMARY KEY 主鍵
# 序號
# AUTOINCREMENT 自動遞增
# UNIQUE 不可重複
# NOT NULL 不可不填
# CHECK(age >= 18) 條件檢查

UNIQUE
編號 INTEGER UNIQUE NOT NULL

建立表單 CREATE TABLE
1. CREATE TABLE table01 # 建立表單table01, 若已存在，則失敗
2. CREATE TABLE IF NOT EXISTS table01 # 建立表單table01, 若已存在，則沿用, 如果尚未建立的話
3. CREATE virtual TABLE table01

# 新增資料
INSERT INTO 表單

# 取得所有資料
SELECT

SELECT 陳述式 FROM 陳述式

取得
SELECT * FROM 哪裏;   取得所有資料

      A,B,C,D
SELECT 什麼 FROM 哪裏;
       欄名      表格名稱


SELECT 什麼 FROM 哪裏 WHERE 條件; (可用邏輯運算子做組合條件)
       欄名      表格名稱


SELECT * FROM customer WHERE birthday < "1990-01-01";

SELECT 什麼 FROM 哪裏 ORDER BY 什麼 ASC;
      欄名      表格名稱       欄名,排列方法
以升冪排序 ASC(預設)
以降冪排序 DESC

限制讀取個數
SELECT 什麼 FROM 哪裏 LIMIT 10         #只讀前10筆
SELECT * FROM titles LIMIT 3, 5        #從第3筆開始讀5筆資料(從0起算)
SELECT * FROM titles LIMIT 5 OFFSET 3  #讀5筆資料出來, 從第3筆開始讀 (從0起算)

# DELETE 刪除

sqlite指令整理
1. CREATE TABLE
2. INSERT INTO
3. SELECT * FROM table01

4.
cursor.execute("UPDATE table01 SET task = 'learn italian' WHERE key = 1")
conn.execute("UPDATE scores SET name='{}' WHERE id={}".format("林胖虎", 1))
conn.execute("UPDATE contact SET name='{}' WHERE id={}".format("Ken", 1))
5.
cursor.execute("DELETE FROM table01 WHERE filename = ?", (filename,))
cursor.execute("DELETE FROM table01 WHERE filename = ?", ("aaaa.mp4",))
cursor.execute("DELETE FROM people where age=20")
conn.execute("DELETE FROM scores WHERE id={}".format(1))
conn.execute("DELETE FROM contact WHERE id={}".format(1))

其他
cursor = conn.execute("DROP TABLE table01")
columns = conn.execute(f"PRAGMA table_info('{table_name}');").fetchall()
"""

"""
新進測試
建立多個表單 要分開寫
"""

# 3030
print("------------------------------")  # 30個

do_fetchall(cursor)
"""
rows = cursor.fetchall()  # 讀取全部資料成元組串列
length = len(rows)
print("共有", length, "筆資料")
for i in range(length):
    print("第" + str(i + 1) + "筆資料 : ", rows[i])
"""

"""
# 語法:
INSERT INTO archive_orders SELECT * from orders WHERE order_date < "2016-01-01",
DELETE from orders WHERE order_date < "2016-01-01",

"""

sqlstr = """
CREATE TABLE IF NOT EXISTS scores(
id      INTEGER PRIMARY KEY NOT NULL,
name    TEXT NOT NULL,
chinese INTEGER NOT NULL,
english INTEGER NOT NULL,
math    INTEGER NOT NULL
)
"""

sqlstr = """CREATE TABLE IF NOT EXISTS scores(
id      INTEGER PRIMARY KEY NOT NULL,
name    TEXT NOT NULL,
chinese INTEGER NOT NULL,
english INTEGER NOT NULL,
math    INTEGER NOT NULL
)
"""
