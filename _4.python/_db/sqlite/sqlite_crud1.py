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


# 盡量用此
def show_data_base_contents_all(db_filename, table_name):
    print("show_data_base_contents_all")
    conn = sqlite3.connect(db_filename)  # 建立資料庫連線
    # SELECT * : 取得所有資料
    sqlstr = "SELECT * FROM {};".format(table_name)  # same
    sqlstr = "SELECT * FROM %s" % table_name
    cursor = conn.execute(sqlstr)
    rows = cursor.fetchall()  # 讀取全部資料成元組串列
    length = len(rows)
    print("共有", length, "筆資料")
    for i in range(length):
        print("第" + str(i + 1) + "筆資料 : ", rows[i])
        if i > 10:
            break
    cursor.close()  # 關閉游標
    conn.close()  # 關閉資料庫連線


# 準備廢棄
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


# 準備廢棄
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

db_filename = "tmp_db01_20250908_164536.sqlite"

print("讀取資料庫")
table_name = "table01"
show_data_base_contents_all(db_filename, table_name)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("建立資料庫 + 加入資料 + 讀取資料")

db_filename = "tmp_db01_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".sqlite"
print("建立資料庫連線, 資料庫 :", db_filename)

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

print("建立表單")

# PRIMARY KEY 主鍵
# 序號 自動遞增 不可重複

sqlstr = """
CREATE TABLE IF NOT EXISTS table01(
idx    INTEGER PRIMARY KEY AUTOINCREMENT, -- 序號(idx)整數自動遞增, 可填可不填
id_num INTEGER NOT NULL,
ename  TEXT NOT NULL,
cname  TEXT,
weight INTEGER NOT NULL CHECK(weight > 0) -- 預設錯誤時會顯示
)
"""

cursor.execute(sqlstr)
conn.commit()  # 更新

# INSERT INTO 新增資料, 有些欄位可以不寫, 序號(idx)自動遞增

# 資料寫4項
sqlstr = "INSERT INTO table01 (id_num, ename, cname, weight) VALUES (?, ?, ?, ?)"

x = (5, "horse", "馬", 48)  # tuple格式
cursor.execute(sqlstr, x)
x = (1, "mouse", "鼠", 66)  # tuple格式
cursor.execute(sqlstr, x)
x = (4, "elephant", "象", 48)  # tuple格式
cursor.execute(sqlstr, x)

# 資料寫3項
sqlstr = "INSERT INTO table01 (id_num, ename, weight) VALUES (?, ?, ?)"
x = (9, "ox", 48)  # tuple格式
cursor.execute(sqlstr, x)
x = (2, "sheep", 66)  # tuple格式
cursor.execute(sqlstr, x)
x = (8, "snake", 16)  # tuple格式
cursor.execute(sqlstr, x)
x = (3, "tiger", 33)  # tuple格式
cursor.execute(sqlstr, x)
x = (7, "rabbit", 8)  # tuple格式
cursor.execute(sqlstr, x)
x = (6, "tiger", 240)  # tuple格式
cursor.execute(sqlstr, x)

for _ in range(10):
    sqlstr = "INSERT INTO table01 (id_num, ename, weight) VALUES (?, ?, ?)"
    x = (6, "tiger", 240)  # tuple格式
    cursor.execute(sqlstr, x)

conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

# UPDATE 更新資料
print("UPDATE 更新資料, 修改2號的資料")
print("建立資料庫連線, 資料庫 :", db_filename)
conn = sqlite3.connect(db_filename)  # 建立資料庫連線

sqlstr = "UPDATE table01 SET ename = '{}'  WHERE id_num = {}".format("goat", 2)
conn.execute(sqlstr)  # 修改2號的資料, 要先確保已經有2號的資料, 才可以修改

sqlstr = "UPDATE table01 SET weight = '{}' WHERE id_num = {}".format(29, 2)
conn.execute(sqlstr)  # 修改2號的資料, 要先確保已經有2號的資料, 才可以修改

conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

# DELETE 刪除資料 條件
print("DELETE 刪除資料, 刪除4號的資料")
print("建立資料庫連線, 資料庫 :", db_filename)
conn = sqlite3.connect(db_filename)  # 建立資料庫連線

sqlstr = "DELETE FROM table01 WHERE id_num = {}".format(4)
conn.execute(sqlstr)

conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

print("用fetchall()讀取 全部資料")

print("讀取資料庫")
table_name = "table01"
show_data_base_contents_all(db_filename, table_name)

print("------------------------------")  # 30個
"""
print("建立資料庫連線, 資料庫 :", db_filename)
conn = sqlite3.connect(db_filename)  # 建立資料庫連線

# DROP TABLE 刪除表單
sqlstr = "DROP TABLE IF EXISTS table01"
cursor = conn.execute(sqlstr)

conn.commit()  # 更新
conn.close()  # 關閉資料庫連線
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

db_filename = "tmp_db02_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".sqlite"
print("建立資料庫連線, 資料庫 :", db_filename)

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

print("建立表單")

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
idx    INTEGER PRIMARY KEY AUTOINCREMENT, -- 序號(idx)整數自動遞增, 可填可不填
id_num INTEGER NOT NULL,
ename  TEXT NOT NULL,
cname  TEXT,
weight INTEGER NOT NULL CHECK(weight > 0) -- 預設錯誤時會顯示
)
"""

# 有寫NOT NULL表示一定要填寫, 若無此條件, 則可以不寫

cursor.execute(sqlstr)
conn.commit()  # 更新

# INSERT INTO 新增資料

print("INSERT INTO 新增資料 2 筆 寫法一, 必須要寫滿所有欄位")
# id_num不可重複
sqlstr = "INSERT INTO table01 VALUES (?, ?, ?, ?, ?)"
x = (20, 5, "horse", "馬", 36)  # tuple格式
cursor.execute(sqlstr, x)

sqlstr = "INSERT INTO table01 VALUES (?, ?, ?, ?, ?)"
x = (50, 1, "mouse", "鼠", 3)  # tuple格式
cursor.execute(sqlstr, x)

print("INSERT INTO 新增資料 1 筆 寫法二, 有些欄位可以不寫, 使用tuple")
sqlstr = "INSERT INTO table01 (id_num, ename, cname, weight) VALUES (?, ?, ?, ?)"
x = (4, "elephant", "象", 100)  # tuple格式
cursor.execute(sqlstr, x)

print("INSERT INTO 新增資料 2 筆 寫法三, 有些欄位可以不寫, 序號自動遞增")

sqlstr = "INSERT INTO table01 (id_num, ename, weight) VALUES (?, ?, ?)"
x = (9, "ox", 48)  # tuple格式
cursor.execute(sqlstr, x)

# id_num不重複 但name weight 重複
sqlstr = "INSERT INTO table01 (id_num, ename, weight) VALUES (?, ?, ?)"
x = (2, "sheep", 66)  # tuple格式
cursor.execute(sqlstr, x)

print("INSERT INTO 新增資料 2 筆 寫法四, 有些欄位可以不寫, 序號自動遞增")
# 定義資料串列
datas = [[8, "snake", 16], [3, "tiger", 33]]

for data in datas:
    print(data)
    sqlstr = "INSERT INTO table01 (id_num, ename, weight) VALUES (?, ?, ?)"
    x = (data[0], data[1], data[2])  # tuple格式
    cursor.execute(sqlstr, x)
conn.commit()  # 更新

print("INSERT INTO 新增資料 1 筆 寫法五, 必須要寫滿所有欄位")

sqlstr = "INSERT INTO table01 VALUES (?, ?, ?, ?, ?)"
index, number, ename, cname, weight = 70, 7, "rabbit", "", 8
x = (index, number, ename, cname, weight)  # tuple格式
cursor.execute(sqlstr, x)

print("INSERT INTO 新增資料 1 筆 寫法六, 必須要寫滿所有欄位")
sqlstr = "INSERT INTO table01 VALUES (?, ?, ?, ?, ?)"
data = (80, 6, "tiger", "", 240)
cursor.execute(sqlstr, data)

conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

# UPDATE 更新資料
print("UPDATE 更新資料, 修改2號的資料")

conn = sqlite3.connect(db_filename)  # 建立資料庫連線

sqlstr = "UPDATE table01 SET ename = '{}'  WHERE id_num = {}".format("goat", 2)
conn.execute(sqlstr)  # 修改2號的資料, 要先確保已經有2號的資料, 才可以修改

sqlstr = "UPDATE table01 SET weight = '{}' WHERE id_num = {}".format(29, 2)
conn.execute(sqlstr)  # 修改2號的資料, 要先確保已經有2號的資料, 才可以修改

conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

# DELETE 刪除資料 條件
print("DELETE 刪除資料, 刪除4號的資料")

conn = sqlite3.connect(db_filename)  # 建立資料庫連線

sqlstr = "DELETE FROM table01 WHERE id_num = {}".format(4)
conn.execute(sqlstr)

conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

# SELECT 取得
print("讀取資料庫")
table_name = "table01"
show_data_base_contents_all(db_filename, table_name)

print("------------------------------")  # 30個

print("查詢資料庫 fetchone() 讀取一筆資料")

# SELECT 取得
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

print("------------------------------")  # 30個

print("指明抓一筆資料, 15號")
number = 15
sqlstr = "SELECT * FROM table01 WHERE id_num = " + str(number)  # 條件
cursor = conn.execute(sqlstr)
row = cursor.fetchone()  # 讀取一筆資料
if not row == None:
    print("{}\t{}\t{}\t{}".format(row[0], row[1], row[2], row[3], row[4]))
else:
    print("找不到" + str(number) + "號資料")

print("------------------------------")  # 30個

print("指明抓名字有bb的資料")
data = ("%bb%",)  # bb在中間 前後要有%
# sqlstr =
cursor = conn.execute("SELECT * FROM table01 WHERE ename LIKE ?", data)  # 條件
# xxxx do_fetchall(cursor)

conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

print("尋找資料")

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
    # DELETE 刪除資料 條件
    sqlstr = "DELETE FROM table01 WHERE id_num = {};".format(number)
    conn.execute(sqlstr)
    conn.commit()  # 更新
    print("已刪除指定的資料")
    """

print("------------------------------")  # 30個

print("不是用fetchall()讀取 全部資料")

conn = sqlite3.connect(db_filename)  # 建立資料庫連線

# sqlstr
cursor = conn.execute("SELECT * FROM table01")  # SELECT * : 取得所有資料
i = 0
for row in cursor:
    # print(type(rows[i]))
    print("第" + str(i + 1) + "筆資料 :", end="")
    # print(rows[i])
    print("{}\t{}\t{}\t{}".format(row[0], row[1], row[2], row[3], row[4]))
    i = i + 1
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

print("用fetchall()讀取 全部資料")

print("讀取資料庫")
print("用fetchall()讀取 全部資料 預設排序(依第1項升冪排序)")
table_name = "table01"
show_data_base_contents_all(db_filename, table_name)

print("------------------------------")  # 30個

print("用fetchall()讀取 全部資料 依 ename 排序, 升冪")

conn = sqlite3.connect(db_filename)  # 建立資料庫連線

# SELECT * : 取得資料 排列 依 ename 升冪
sqlstr = "SELECT * FROM table01 ORDER BY ename;"  # 由小到大, 升冪
cursor = conn.execute(sqlstr)

# SELECT * : 取得資料 排列 依 ename 降冪
# cursor = conn.execute("SELECT * FROM table01 ORDER BY ename DESC;")  #由小到大 + 反相 = 由大到小, 降冪
# xxxx do_fetchall(cursor)

conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

print("用fetchall()讀取 全部資料 依 weight 排序, 降冪")

conn = sqlite3.connect(db_filename)  # 建立資料庫連線

# SELECT * : 取得資料 排列 依 weight 升冪
# cursor = conn.execute("SELECT * FROM table01 ORDER BY weight;")  #由小到大, 升冪

# SELECT * : 取得資料 排列 依 weight 降冪
cursor = conn.execute(
    "SELECT * FROM table01 ORDER BY weight DESC;"
)  # 由小到大 + 反相 = 由大到小, 降冪

# xxxx do_fetchall(cursor)

conn.close()  # 關閉資料庫連線
"""
print("------------------------------")  # 30個

conn = sqlite3.connect(db_filename)  # 建立資料庫連線

# DROP TABLE 刪除表單
sqlstr = "DROP TABLE IF EXISTS table01"
cursor = conn.execute(sqlstr)

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
    cursor = conn.execute("SELECT * FROM %s" % table_name)  # SELECT * : 取得所有資料
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
    print("------------------------------")  # 30個
    print("1.顯示歷年油價資訊")
    print("2.最近10週油價資訊")
    print("0.結束")
    print("------------------------------")  # 30個


def disp_alldata():
    print("建立資料庫連線, 資料庫 :", db_filename)
    conn = sqlite3.connect(db_filename)  # 建立資料庫連線

    print("要事先能知道表單的名稱 prices 與 各欄位的名稱 gdate")

    # SELECT * : 取得資料 排列 依 gdate 降冪
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
    # SELECT * : 取得資料 排列 依 gdate 降冪
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
    # SELECT * : 取得資料 排列 依 gdate 降冪
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
print("建立資料庫連線, 資料庫 :", db_filename)

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

# 建立表單
sqlstr = """
CREATE TABLE IF NOT EXISTS TablePM25(
no       INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
SiteName TEXT NOT NULL,
PM25     INTEGER
)
"""
cursor.execute(sqlstr)

print("從資料庫讀取資料...")
sqlstr = "SELECT * FROM TablePM25"  # SELECT * : 取得所有資料
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

print("查詢資料庫 fetchone() 讀取一筆資料")
print("從資料庫讀出一筆資料")

db_filename = "data/python01.sqlite"
print("建立資料庫連線, 資料庫 :", db_filename)

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
sqlstr = "SELECT * FROM table01 WHERE num = 1"
cursor = conn.execute(sqlstr)
row = cursor.fetchone()  # 讀取一筆資料

if not row == None:
    print("{}\t{}".format(row[0], row[1]))

conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個

print("從資料庫讀出全部資料")

db_filename = "data/python01.sqlite"
print("建立資料庫連線, 資料庫 :", db_filename)

print("讀取資料庫")
table_name = "table01"
show_data_base_contents_all(db_filename, table_name)

print("------------------------------------------------------------")  # 60個

print("從資料庫讀出全部資料")

db_filename = "data/headlines.sqlite"
print("建立資料庫連線, 資料庫 :", db_filename)

conn = sqlite3.connect(db_filename)  # 建立資料庫連線

print("讀取全部, 只顯示前10筆")
sqlstr = "SELECT * FROM titles"  # SELECT * : 取得所有資料
cursor = conn.execute(sqlstr)
rows = cursor.fetchall()  # 讀取全部資料成元組串列
length = len(rows)
print("共有", length, "筆資料")
for i in range(length):
    print("第" + str(i + 1) + "筆資料 : ", rows[i])
    if i == 10:
        break

print("只讀前10筆")
sqlstr = "SELECT * FROM titles LIMIT 10"  # SELECT * : 取得所有資料, 限制10筆
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
SERIAL          序列  測不出效果
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

print("INSERT INTO 新增資料")

sqlstr = "INSERT INTO table01 (filename, filesize) VALUES (?, ?)"
x = ("aaaa.mp4", "12345")  # tuple格式
cursor.execute(sqlstr, x)

print("SELECT")
# sqlstr =
cursor.execute("SELECT * FROM table01 WHERE filename = ?", ("aaaa.mp4",))

print("Fetchall")
# xxxx do_fetchall(cursor)

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
    sqlstr = "SELECT * FROM password"  # SELECT * : 取得所有資料
    cursor = conn.execute(sqlstr)
    for row in cursor:
        print("帳號 : {}\t密碼 : {}".format(row[0], row[1]))


db_filename = "tmp_db04_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".sqlite"
print("建立資料庫連線, 資料庫 :", db_filename)


conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

sqlstr = """
CREATE TABLE IF NOT EXISTS password(
name TEXT NOT NULL,
pass TEXT NOT NULL
)
"""
cursor.execute(sqlstr)

# INSERT INTO 新增資料
sqlstr = "INSERT INTO password (name, pass) VALUES (?, ?)"

new_name = "Apple"
new_pass = "123456"
x = (new_name, new_pass)  # tuple格式
cursor.execute(sqlstr, x)

new_name = "Bravo"
new_pass = "abcdefg"
x = (new_name, new_pass)  # tuple格式
cursor.execute(sqlstr, x)

new_name = "Charlie"
new_pass = "ccccc"
x = (new_name, new_pass)  # tuple格式
cursor.execute(sqlstr, x)

print("顯示所有資料")
disp_data()

print("------------------------------")  # 30個

# INSERT INTO 新增資料

new_name = "Delta"
new_password = "12345678"

sqlstr = "INSERT INTO password (name, pass) VALUES (?, ?)"
x = (new_name, new_password)  # tuple格式
conn.execute(sqlstr, x)
conn.commit()  # 更新
print("資料 {} 已儲存完畢".format(new_name))

print("顯示所有資料")
disp_data()

print("------------------------------")  # 30個

print("查詢 CHARLIE")

new_name = "CHARLIE"

# 無 LIKE, 一定要符合大小寫
sqlstr = "SELECT * FROM password WHERE name = '{}'".format(new_name)
# 有 LIKE, 大小寫皆可
sqlstr = "SELECT * FROM password WHERE name LIKE '{}'".format(new_name)

cursor = conn.execute(sqlstr)
row = cursor.fetchone()  # 讀取一筆資料

if not row == None:
    print("{} 帳號已存在!".format(new_name))
else:
    print("{} 帳號不存在!".format(new_name))

print("查詢 ELEPHANT")

new_name = "ELEPHANT"

# 無 LIKE, 一定要符合大小寫
sqlstr = "SELECT * FROM password WHERE name = '{}'".format(new_name)
# 有 LIKE, 大小寫皆可
sqlstr = "SELECT * FROM password WHERE name LIKE '{}'".format(new_name)

cursor = conn.execute(sqlstr)
row = cursor.fetchone()  # 讀取一筆資料

if not row == None:
    print("{} 帳號已存在!".format(new_name))
else:
    print("{} 帳號不存在!".format(new_name))

print("------------------------------")  # 30個

print("修改資料")

old_name = "Charlie"
sqlstr = "SELECT * FROM password WHERE name = '{}'".format(old_name)
cursor = conn.execute(sqlstr)
row = cursor.fetchone()  # 讀取一筆資料
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

print("顯示所有資料")
disp_data()

print("------------------------------")  # 30個

print("DELETE 刪除資料 條件")

name = "Delta"
sqlstr = "SELECT * FROM password WHERE name = '{}'".format(name)
cursor = conn.execute(sqlstr)

row = cursor.fetchone()  # 讀取一筆資料

if row == None:
    print("{} 帳號不存在!".format(name), "無法刪除資料")
else:
    sqlstr = "DELETE FROM password WHERE name = '{}'".format(name)
    conn.execute(sqlstr)
    conn.commit()  # 更新
    print("刪除{}的資料!：".format(name), "已完成")


print("顯示所有資料")
disp_data()

conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("測試 例外 的寫法")

conn = sqlite3.connect(":memory:")  # 建立資料庫連線, 記憶體
cursor = conn.cursor()  # 建立 cursor 物件

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

conn.close()  # 關閉資料庫連線

# print("讀取資料庫")
# table_name = "table01"
# show_data_base_contents_all(db_filename, table_name)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("測試 TIMESTAMP 時間戳")

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
print("製作資料 today :", today)
print("製作資料 now :", now)

# INSERT INTO 新增資料

sqlstr = "INSERT INTO table01(my_date, my_timestamp) VALUES (?, ?)"
x = (today, now)  # tuple格式
cursor.execute(sqlstr, x)

# SELECT 取得
cursor.execute("SELECT my_date, my_timestamp FROM table01")
row = cursor.fetchone()  # 讀取一筆資料
print(row)
print(row[0])
print(row[1])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("測試 executemany NG")
print("測試 executemany, 一次執行多個指令")

persons = [("Hugo", "Boss"), ("Calvin", "Klein")]

conn = sqlite3.connect(":memory:")  # 建立資料庫連線, 記憶體
cursor = conn.cursor()  # 建立 cursor 物件

sqlstr = """
CREATE TABLE IF NOT EXISTS person(
firstname,
lastname
)
"""
conn.execute(sqlstr)

"""
# INSERT INTO 新增資料
sqlstr = "INSERT INTO person(firstname, lastname) VALUES (?, ?)", persons
conn.executemany(sqlstr)

# SELECT 顯示表單資料
for row in conn.execute("SELECT firstname, lastname FROM person"):
    print(row)

print("I just deleted", conn.execute("DELETE FROM person").rowcount, "rows")
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("測試 序號自動遞增")

db_filename = "tmp_db05_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".sqlite"
print("建立資料庫連線, 資料庫 :", db_filename)

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

print("建立表單")

sqlstr = """
CREATE TABLE IF NOT EXISTS table01(
id      INTEGER PRIMARY KEY AUTOINCREMENT, -- 序號(id)整數自動遞增, 可填可不填
name    TEXT NOT NULL,
age     INTEGER NOT NULL,
address CHAR(50),
salary  REAL -- REAL:小數
)
"""
cursor.execute(sqlstr)

print("有設定序號 123")
sqlstr = "INSERT INTO table01 (id, name, age, address, salary) VALUES (?, ?, ?, ?, ?)"
x = (123, "Paul", 32, "California", 20000.00)  # tuple格式
cursor.execute(sqlstr, x)

print("沒有設定序號, 系統自動遞增")
sqlstr = "INSERT INTO table01 (name, age, address, salary) VALUES (?, ?, ?, ?)"

x = ("Allen", 25, "Texas", 15000.00)  # tuple格式
cursor.execute(sqlstr, x)

x = ("Teddy", 23, "Norway", 20000.00)  # tuple格式
cursor.execute(sqlstr, x)

conn.commit()  # 更新

conn.close()  # 關閉資料庫連線

print("讀取資料庫")
table_name = "table01"
show_data_base_contents_all(db_filename, table_name)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("新進測試")

db_filename = "ims_sql/db_ims.sqlite"
db_filename = "data/gasoline.sqlite"
# db_filename = "db_20230703_113217.sqlite"
print("建立資料庫連線, 資料庫 :", db_filename)

conn = sqlite3.connect(db_filename)  # 建立資料庫連線

print("要事先能知道表單的名稱 prices 與 各欄位的名稱 gdate")

# SELECT * : 取得資料 排列 依 gdate 降冪
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

print("------------------------------")  # 30個

print("讀取資料庫")
table_name = "prices"
show_data_base_contents_all(db_filename, table_name)

print("------------------------------")  # 30個

"""
新進測試
測試 SERIAL 測不出效果

測試 TIMESTAMP
測試 DATE
測試 CHECK

測試部分填入資料

"""

print("------------------------------------------------------------")  # 60個

db_filename = "tmp_db06_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".sqlite"
print("建立資料庫連線, 資料庫 :", db_filename)

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

# 建立表單 table01 + PRIMARY KEY
sqlstr = """
CREATE TABLE IF NOT EXISTS table01(
-- id SERIAL PRIMARY KEY,   無效
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

# INSERT INTO 新增資料 完整
id_num = 3
name = "David"
birthday = "2006-03-11"
work_time = "2023-07-11"
money = 2345
update_time = datetime.datetime.now()
sqlstr = "INSERT INTO table01 (id_num, name, birthday, work_time, money, update_time) VALUES (?, ?, ?, ?, ?, ?)"
x = (id_num, name, birthday, work_time, money, update_time)  # tuple格式
cursor.execute(sqlstr, x)

# INSERT INTO 新增資料 部分
id_num = 5
name = "Eric"
update_time = datetime.datetime.now()
sqlstr = "INSERT INTO table01 (id_num, name, update_time) VALUES (?, ?, ?)"
x = (id_num, name, update_time)  # tuple格式
cursor.execute(sqlstr, x)

conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("讀取資料庫")
table_name = "table01"
show_data_base_contents_all(db_filename, table_name)

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

cursor = conn.execute(
    "SELECT rowid, name, ingredients FROM table01 WHERE name MATCH 'pie'"
)  # 條件
for row in cursor:
    print(row)

# conn.commit()  # 更新

print("讀取資料庫")
table_name = "table01"
show_data_base_contents_all(db_filename, table_name)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("一次寫入多行的語法 executescript")

conn = sqlite3.connect(":memory:")  # 建立資料庫連線, 記憶體
cursor = conn.cursor()  # 建立 cursor 物件

conn.execute("CREATE TABLE IF NOT EXISTS book(title, author, published)")

# 要同質性
conn.executescript(
    """
INSERT INTO book(title, author, published) VALUES ('Dirk Gently''s Holistic Detective Agency','Douglas Adams',1987)
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

sqlstr = "INSERT INTO people VALUES (?, ?)"
name, age = "David", 18
x = (name, age)  # tuple格式
cursor.execute(sqlstr, x)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

db_filename_disk = (
    "tmp_db08_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + "_disk.sqlite"
)

mem_conn = sqlite3.connect(":memory:")  # 建立資料庫連線, 記憶體
cursor = conn.cursor()  # 建立 cursor 物件

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

sqlstr = "INSERT INTO table01 VALUES (?, ?)"
name, age = "David", 18
x = (name, age)  # tuple格式
cursor.execute(sqlstr, x)

print("目前共有修改資料次數 : ", mem_conn.total_changes)

cursor.execute(sqlstr, x)
cursor.execute(sqlstr, x)
cursor.execute(sqlstr, x)

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

sqlstr = "INSERT INTO stocks VALUES (?, ?, ?, ?, ?)"
x = ("2006-01-05", "BUY", "RHAT", 100, 35.14)  # tuple格式
cursor.execute(sqlstr, x)

mem_conn.commit()

sqlstr = "SELECT * FROM table01"  # SELECT * : 取得所有資料
cursor.execute(sqlstr)

# xxxx do_fetchall(cursor)

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

print("------------------------------")  # 30個

db_filename = db_filename_disk

print("讀取資料庫")
table_name = "table01"
show_data_base_contents_all(db_filename, table_name)

print("讀取資料庫")
table_name = "stocks"
show_data_base_contents_all(db_filename, table_name)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("測試 executemany, 一次執行多個指令")

conn = sqlite3.connect(":memory:")  # 建立資料庫連線, 記憶體
cursor = conn.cursor()  # 建立 cursor 物件

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

# INSERT INTO 新增資料 多筆, 使用串列
stocks = [
    # 日期         買/買   代號   數量  價格
    ("2006-01-05", "BUY", "RHAT", 100, 35.14),
    ("2006-03-28", "BUY", "IBM", 1000, 45.0),
    ("2006-04-06", "SELL", "IBM", 500, 53.0),
    ("2006-04-05", "BUY", "MSFT", 1000, 72.0),
]
conn.executemany("INSERT INTO stocks values (?, ?, ?, ?, ?)", stocks)

cursor = conn.cursor()  # 建立 cursor 物件

# SELECT * : 取得資料 排列 依 ename 升冪
sqlstr = "SELECT * FROM stocks ORDER BY price"
for row in cursor.execute(sqlstr):
    print(row)

# Output:
# ("2006-01-05", "BUY", "RHAT", 100, 35.14)
# ("2006-03-28", "BUY", "IBM", 1000, 45.0)
# ("2006-04-06", "SELL", "IBM", 500, 53.0)
# ("2006-04-05", "BUY", "MSFT", 1000, 72.0)

# SELECT * : 取得資料 排列 依 ename 升冪
sqlstr = "SELECT * FROM stocks ORDER BY price"
cursor.execute(sqlstr)

one_row_data = cursor.fetchone()  # 讀取一筆資料
print("a讀取一筆資料", one_row_data)

while one_row_data:
    one_row_data = cursor.fetchone()  # 讀取一筆資料
    print("b讀取一筆資料", one_row_data)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

try:
    # 嘗試連接到資料庫
    conn = sqlite3.connect(db_filename_disk)  # 建立資料庫連線
    cursor = conn.cursor()  # 建立 cursor 物件
    # 嘗試執行查詢，可能會引發異常
    sqlstr = "SELECT * FROM non_existent_table"  # SELECT * : 取得所有資料
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
fetchone()  # 讀取一筆資料	#抓一行 tuple
fetchmany(size=cursor.arraysize)	#抓n行 list
fetchall()  # 讀取全部資料成元組串列	#抓取剩下的全部 list
"""

db_filename = "ims_sql/db_ims.sqlite"
db_filename = "data/gasoline.sqlite"
# db_filename  = "db_20230703_113217.sqlite"
print("建立資料庫連線, 資料庫 :", db_filename)

conn = sqlite3.connect(db_filename)  # 建立資料庫連線

sqlstr = "SELECT * FROM prices;"  # SELECT * : 取得所有資料
cursor = conn.execute(sqlstr)

print("讀取1筆資料")
cc = cursor.fetchone()
print(cc)

print("讀取1筆資料")
cc = cursor.fetchone()
print(cc)

print("讀取3筆資料")
cc = cursor.fetchmany(3)
print(cc)

print("讀取全部資料")
# xxxx do_fetchall(cursor)

conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

conn = sqlite3.connect(":memory:")  # 建立資料庫連線, 記憶體
cursor = conn.cursor()  # 建立 cursor 物件

# 建立表單 table01 + PRIMARY KEY

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

print(tasks[0])
print(tasks[1])
print(tasks[2])

cursor.execute("INSERT INTO table01 VALUES (NULL, ?)", (tasks[0],))
cursor.execute("INSERT INTO table01 VALUES (NULL, ?)", (tasks[1],))
cursor.execute("INSERT INTO table01 VALUES (NULL, ?)", (tasks[2],))

# UPDATE 更新資料
cursor.execute("UPDATE table01 SET task = 'learn italian' WHERE key = 1")

key_id = 2
# sqlstr =
cursor.execute("SELECT * FROM table01 WHERE key=?", (str(key_id),))
key, task = cursor.fetchone()  # 讀取一筆資料

print(key)
print(task)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

db_filename = "tmp_db09_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".sqlite"
print("建立資料庫連線, 資料庫 :", db_filename)

conn = sqlite3.connect(db_filename)  # 建立資料庫連線

# CREATE + PK
# 建立表單 students + PRIMARY KEY 序號 自動遞增 不可重複
sqlstr = """
CREATE TABLE IF NOT EXISTS students(
id     INTEGER PRIMARY KEY AUTOINCREMENT, -- 序號(id)整數自動遞增, 可填可不填
name   TEXT,
gender TEXT
)
"""
conn.execute(sqlstr)

print("INSERT INTO 新增資料 3個欄位 指定id")

sqlstr = "INSERT INTO students VALUES (?, ?, ?)"

new_id, new_name, new_gender = 1, "Tomy", "M"
x = (new_id, new_name, new_gender)  # tuple格式
conn.execute(sqlstr, x)

new_id, new_name, new_gender = 3, "Kathy", "F"
x = (new_id, new_name, new_gender)  # tuple格式
conn.execute(sqlstr, x)

new_id, new_name, new_gender = 123, "david", "M"
x = (new_id, new_name, new_gender)  # tuple格式
conn.execute(sqlstr, x)

conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

conn = sqlite3.connect(db_filename)  # 建立資料庫連線

print("INSERT INTO 新增資料 2個欄位 不指定id")

new_name = "elephant"
new_gender = "F"
x = (new_name, new_gender)  # tuple格式
sqlstr = "INSERT INTO students(name, gender) VALUES (?, ?)"
conn.execute(sqlstr, x)

conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

print("讀取資料 SELECT *")

conn = sqlite3.connect(db_filename)  # 建立資料庫連線

sqlstr = "SELECT * FROM students"  # SELECT * : 取得所有資料
cursor = conn.execute(sqlstr)

print("取得所有資料")
i = 0
for row in cursor:
    print("第" + str(i + 1) + "筆資料 : ", row)
    i = i + 1
    print("id =", row[0], ", name =", row[1], ", gender =", row[2])

conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

print("讀取資料 SELECT * 所有資料")

conn = sqlite3.connect(db_filename)  # 建立資料庫連線

sqlstr = "SELECT * FROM students"  # SELECT * : 取得所有資料
cursor = conn.execute(sqlstr)

# xxxx do_fetchall(cursor)

conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

print("讀取資料 SELECT 僅一欄 name")

conn = sqlite3.connect(db_filename)  # 建立資料庫連線

sqlstr = "SELECT name FROM students"  # SELECT name : 取得一欄資料
cursor = conn.execute(sqlstr)

# xxxx do_fetchall(cursor)

conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

print("讀取資料 SELECT 加條件")

conn = sqlite3.connect(db_filename)  # 建立資料庫連線

sqlstr = 'SELECT name, gender FROM students WHERE gender = "F"'
cursor = conn.execute(sqlstr)

# xxxx do_fetchall(cursor)

conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

print("UPDATE 更新資料")

conn = sqlite3.connect(db_filename)  # 建立資料庫連線

sqlstr = 'UPDATE students set name = "Tomy" WHERE id = 1'
cursor = conn.execute(sqlstr)

conn.commit()  # 更新

cursor = conn.execute("SELECT name FROM students")

# xxxx do_fetchall(cursor)

conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

print("# DELETE 刪除資料 條件")

conn = sqlite3.connect(db_filename)  # 建立資料庫連線

sqlstr = "DELETE FROM students WHERE id = 2"
cursor = conn.execute(sqlstr)

conn.commit()  # 更新

cursor = conn.execute("SELECT name FROM students")

# xxxx do_fetchall(cursor)

conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

db_filename = "tmp_db10_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".sqlite"
print("建立資料庫連線, 資料庫 :", db_filename)

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
        sqlstr = "INSERT INTO population VALUES (?, ?, ?, ?)"
        x = (area, male, female, total)  # tuple格式
        conn.execute(sqlstr, x)
        conn.commit()

sqlstr = "SELECT * FROM population"  # SELECT * : 取得所有資料
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

sqlstr = "SELECT * FROM population"  # SELECT * : 取得所有資料
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
print("建立資料庫連線, 資料庫 :", db_filename)

cursor = conn.cursor()  # 建立 cursor 物件

sqlstr = "INSERT INTO people (name,age,sex) values (?, ?, ?)"
x = ('Jee', 21, 'F')  # tuple格式
cursor.execute(sqlstr, x)

r = cursor.execute("DELETE FROM people WHERE age=20")
conn.commit()  # 更新

sqlstr = "SELECT * FROM people"  # SELECT * : 取得所有資料
cursor.execute(sqlstr)

# xxxx do_fetchall(cursor)

cursor.close()  # 關閉游標
conn.close()  # 關閉資料庫連線
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

db_filename = "tmp_db11_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".sqlite"
print("建立資料庫連線, 資料庫 :", db_filename)

print("新建資料庫")

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

# 建立表單 table01 + PRIMARY KEY
sqlstr = """
CREATE TABLE IF NOT EXISTS table01(
id      INTEGER PRIMARY KEY NOT NULL,
name    TEXT NOT NULL,
chinese INTEGER NOT NULL,
english INTEGER NOT NULL,
math    INTEGER NOT NULL
)
"""
cursor.execute(sqlstr)

print("------------------------------")  # 30個

print("INSERT INTO 新增資料")
sqlstr = "INSERT INTO table01 VALUES (?, ?, ?, ?, ?)"

x = (1, "葉大雄", 65, 62, 40)  # tuple格式
cursor.execute(sqlstr, x)
x = (2, "陳靜香", 85, 90, 87)  # tuple格式
cursor.execute(sqlstr, x)
x = (3, "王聰明", 92, 90, 95)  # tuple格式
cursor.execute(sqlstr, x)

# 定義資料串列
datas = [[11, "葉大雄", 65, 62, 40], [12, "陳靜香", 85, 90, 87], [13, "王聰明", 92, 90, 95]]

for data in datas:
    x = (data[0], data[1], data[2], data[3], data[4])  # tuple格式
    conn.execute(sqlstr, x)

conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

print("UPDATE 更新資料")

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

# UPDATE 更新資料 # 修改 id 為 1 的資料
conn.execute("UPDATE table01 SET name='{}' WHERE id={}".format("林胖虎", 1))

conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

print("DELETE 刪除資料 條件")

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

# DELETE 刪除資料 條件 id 為 1 之資料
conn.execute("DELETE FROM table01 WHERE id={}".format(1))

conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

print("讀取資料庫")
table_name = "table01"
show_data_base_contents_all(db_filename, table_name)

print("------------------------------")  # 30個

print("查詢資料庫 fetchone() 讀取一筆資料")

# fetchone.py

conn = sqlite3.connect(db_filename)  # 建立資料庫連線

sqlstr = "SELECT * FROM table01"  # SELECT * : 取得所有資料
cursor = conn.execute(sqlstr)

row = cursor.fetchone()  # 讀取一筆資料
print(row[0], row[1])
conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

db_filename = "tmp_db12_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".sqlite"
print("建立資料庫連線, 資料庫 :", db_filename)

conn = sqlite3.connect(db_filename)  # 建立資料庫連線

# 建立表單 table01
sqlstr = """
CREATE TABLE IF NOT EXISTS table01(
姓名     TEXT,
打卡時間 TEXT
)
"""
conn.execute(sqlstr)

print("INSERT INTO 新增資料")

name = "david"
# 取得現在時間
save_time = datetime.datetime.now().strftime("%Y-%m-%d %H.%M.%S")

# 新增一筆資料的 SQL 語法
sqlstr = "INSERT INTO table01 VALUES (?, ?)"
x = (name, save_time)  # tuple格式
conn.execute(sqlstr, x)

conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

print("讀取資料庫")
table_name = "table01"
show_data_base_contents_all(db_filename, table_name)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

db_filename = "tmp_db13_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".sqlite"
print("建立資料庫連線, 資料庫 :", db_filename)

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

# 建立表單 table01 + PRIMARY KEY
sqlstr = """
CREATE TABLE IF NOT EXISTS table01(
id   INTEGER PRIMARY KEY NOT NULL,
name TEXT NOT NULL,
tel  TEXT NOT NULL
)
"""
cursor.execute(sqlstr)

conn.commit()  # 更新

conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

# sqlite_crud2.py

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

# 定義資料串列
datas = [
    [1, "David", "02-123456789"],
    [2, "Lily", "02-987654321"],
]

# INSERT INTO 新增資料
sqlstr = "INSERT INTO table01 (id, name, tel) VALUES (?, ?, ?)"
for data in datas:
    x = (data[0], data[1], data[2])  # tuple格式
    conn.execute(sqlstr, x)

conn.commit()  # 更新

conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

print("查詢資料庫 fetchone() 讀取一筆資料")

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

sqlstr = "SELECT * FROM table01"  # SELECT * : 取得所有資料
cursor = conn.execute(sqlstr)

row = cursor.fetchone()  # 讀取一筆資料
print(row)

conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

print("UPDATE 更新資料")

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

# UPDATE 更新資料 # 修改 id 為 1 的資料
conn.execute("UPDATE table01 SET name='{}' WHERE id={}".format("Ken", 1))

conn.commit()  # 更新

conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

print("DELETE 刪除資料 條件")

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

# DELETE 刪除資料 條件 id 為 1 之資料
conn.execute("DELETE FROM table01 WHERE id={}".format(1))

conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

# sqlite_cursor.py

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

# 新增一筆記錄
sqlstr = "INSERT INTO table01 VALUES (?, ?, ?)"
x = (1, "David", "02-1234567")  # tuple格式
cursor.execute(sqlstr, x)

conn.commit()  # 更新

conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

print("讀取資料庫")
table_name = "table01"
show_data_base_contents_all(db_filename, table_name)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("測試 executemany, 一次執行多個指令")

db_filename = "tmp_db14_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".sqlite"
print("建立資料庫連線, 資料庫 :", db_filename)

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
cursor.executemany("INSERT INTO table01 values (?, ?, ?)", stocks)

conn.commit()  # 更新

# SELECT * : 取得所有資料
print("SELECT * : 取得所有資料")
sqlstr = "SELECT * FROM table01"  # SELECT * : 取得所有資料
cursor = conn.execute(sqlstr)

# xxxx do_fetchall(cursor)

# SELECT * : 條件取得資料
print("SELECT * : 條件取得資料")
min_price = 12
# sqlstr = NG
for row in conn.execute("SELECT * FROM table01 WHERE price >= ?", (min_price,)):
    print(row)

conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

db_filename = "tmp_db15_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".sqlite"
print("建立資料庫連線, 資料庫 :", db_filename)

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件  # 獲得資料庫游標

# 建立表單 table01
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

print("INSERT INTO 新增資料")

title = "david"
username = "wang"
email = "david@lion.mouse"
message = "delicious"
t = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

sqlstr = "INSERT INTO table01 VALUES (?, ?, ?, ?, ?)"
x = (title, username, email, message, t)  # tuple格式
cursor.execute(sqlstr, x)

print("INSERT INTO 新增資料")

title = "AAAA"
username = "BBBB"
email = "CCCC"
message = "DDDD"
t = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

sqlstr = "INSERT INTO table01 (title, username, email, message_text, date) VALUES (?, ?, ?, ?, ?)"
x = (title, username, email, message, t)  # tuple格式
conn.execute(sqlstr, x)

cursor.close()  # 關閉游標
conn.close()  # 關閉資料庫連線

print("讀取資料庫")
table_name = "table01"
show_data_base_contents_all(db_filename, table_name)

print("------------------------------")  # 30個

print("讀取資料庫")
table_name = "table01"
show_data_base_contents_all(db_filename, table_name)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

db_filename = "data/gasoline.sqlite"
print("建立資料庫連線, 資料庫 :", db_filename)

print("油價走勢圖")

print("建立資料庫連線, 資料庫 : " + db_filename)
conn = sqlite3.connect(db_filename)  # 建立資料庫連線

# SELECT * : 取得資料 排列 依 gdate 升冪
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
"""
# csv 轉 sqlite

csv_filename = "D:/_git/vcs/_4.python/write_read_file/_3.csv/data/animals.csv"
db_filename = (
    "tmp_db16_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + "_csv.sqlite"
)

df = pd.read_csv(csv_filename)
df.columns = df.columns.str.strip()

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
df.to_sql("animals", conn, if_exists="replace")

conn.close()  # 關閉資料庫連線
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("較完整")
print("------------------------------------------------------------")  # 60個

print("準備工作")


db_filename_books_old = "data/Books.sqlite"
db_filename_books = (
    "tmp_Books_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".sqlite"
)

db_filename_singMatch_old = "data/singMatch.db"
db_filename_singMatch = (
    "tmp_singMatch_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".sqlite"
)

if not os.path.exists(db_filename_books):
    shutil.copy(db_filename_books_old, db_filename_books)
    print(db_filename_books)


if not os.path.exists(db_filename_singMatch):
    shutil.copy(db_filename_singMatch_old, db_filename_singMatch)
    print(db_filename_singMatch)


def show_books_data():
    print("查詢資料庫")
    conn = sqlite3.connect(db_filename_books)  # 建立資料庫連線

    # SELECT * : 取得所有資料
    sqlstr = "SELECT * FROM Books"  # SELECT * : 取得所有資料
    cursor = conn.execute(sqlstr)

    # 取出查詢結果的每一筆記錄
    print("ID\tTitle\t\t\tPrice")
    for row in cursor:
        print(row[0], "\t", row[1], "\t", row[2])

    conn.close()  # 關閉資料庫連線


show_books_data()

print("原始資料 4 筆")

print("------------------------------")  # 30個

print("INSERT INTO 新增資料")

conn = sqlite3.connect(db_filename_books)  # 建立資料庫連線

new_id = "D0002"
new_title = "MySQL資料庫系統333"
new_price = "600"

# INSERT INTO 新增資料
sqlstr = "INSERT INTO Books (id, title, price) VALUES (?, ?, ?)"
x = (new_id, new_title, new_price)  # tuple格式
conn.execute(sqlstr, x)

print("加入 :", x)

conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

show_books_data()

print("------------------------------")  # 30個

print("INSERT INTO 新增資料 字典")

conn = sqlite3.connect(db_filename_books)  # 建立資料庫連線

d = {"id": "D0003", "title": "MongoDB資料庫系統", "price": 650}  # 字典

# INSERT INTO 新增資料
sqlstr = "INSERT INTO Books (id, title, price) VALUES (?, ?, ?)"
x = (d["id"], d["title"], d["price"])  # tuple格式

cursor = conn.execute(sqlstr, x)
print(cursor.rowcount)

print("加入 :", x)

conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

show_books_data()

print("------------------------------")  # 30個

print("UPDATE 更新資料 D0002 價格改 650")
print("UPDATE 更新資料 D0003 價格改 700")

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

show_books_data()

print("------------------------------")  # 30個

print("刪除資料庫 D0002")
print("刪除資料庫 D0003")

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

show_books_data()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("讀取資料庫的所有資料")

conn = sqlite3.connect(db_filename_singMatch)  # 建立資料庫連線

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

# delete.py

conn = sqlite3.connect(db_filename_singMatch)  # 建立資料庫連線

# selId = int(input("請輸入要移除的 編號 : "))
selId = 1

sqlstr = "DELETE FROM 參賽者 WHERE 編號 = {0}".format(selId)
conn.execute(sqlstr)
print("編號 = {0} 的記錄 已經刪除....".format(selId))

conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

# insert01.py

conn = sqlite3.connect(db_filename_singMatch)  # 建立資料庫連線

newId = 123
newName = "david"
newSex = "M"
newTel = "0912345678"
sqlstr = "INSERT INTO 參賽者 VALUES (?, ?, ?, ?)"
row = (newId, newName, newSex, newTel)  # tuple格式
conn.execute(sqlstr, row)

conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

# insert02.py

conn = sqlite3.connect(db_filename_singMatch)  # 建立資料庫連線

# 建立表單 音色
sql1 = "CREATE TABLE IF NOT EXISTS 音色( \
        編號 INTEGER UNIQUE NOT NULL, \
        音色50 INTEGER)"
conn.execute(sql1)

newId = 124
newScore = 100
row = (newId, newScore)
sql2 = "INSERT INTO 音色 VALUES (?, ?)"
conn.execute(sql2, row)

conn.commit()
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

# insert03.py

conn = sqlite3.connect(db_filename_singMatch)  # 建立資料庫連線

# 建立表單 技巧
sql1 = "CREATE TABLE IF NOT EXISTS 技巧( \
         編號 INTEGER UNIQUE NOT NULL, \
         技巧30 INTEGER)"
conn.execute(sql1)

print("請輸入「技巧」表單的記錄資料")

newId = 125
newScore = 87
row = (newId, newScore)
sql2 = "INSERT INTO 技巧 VALUES (?, ?)"
conn.execute(sql2, row)

conn.commit()
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

# insert04.py

conn = sqlite3.connect(db_filename_singMatch)  # 建立資料庫連線

# 建立表單 儀態
sql1 = "CREATE TABLE IF NOT EXISTS 儀態( \
         編號 INTEGER UNIQUE NOT NULL, \
         儀態20 INTEGER)"
conn.execute(sql1)

newId = 123
newScore = 77
row = (newId, newScore)
sql2 = "INSERT INTO 儀態 VALUES (?, ?)"
conn.execute(sql2, row)

conn.commit()
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

# match.py


def fnCreateTable():
    # 建立表單 參賽者
    sql1 = "CREATE TABLE IF NOT EXISTS 參賽者( \
            編號 INTEGER UNIQUE NOT NULL, \
            姓名 TEXT, \
            性別 TEXT, \
            電話 TEXT)"
    conn.execute(sql1)

    # 建立表單 音色
    sql2 = "CREATE TABLE IF NOT EXISTS 音色( \
            編號 INTEGER UNIQUE NOT NULL, \
            音色50 INTEGER)"
    conn.execute(sql2)

    # 建立表單 技巧
    sql3 = "CREATE TABLE IF NOT EXISTS 技巧( \
            編號 INTEGER UNIQUE NOT NULL, \
            技巧30 INTEGER)"
    conn.execute(sql3)

    # 建立表單 儀態
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
        sqlstr = "INSERT INTO 參賽者 VALUES (?, ?, ?, ?)"
        row = (newId, newName, newSex, newTel)  # tuple格式
        conn.execute(sqlstr, row)
        conn.commit()
        again = input("是否繼續輸入資料 ? ")


def fnSelect01():
    sqlstr = "SELECT * FROM 參賽者"  # SELECT * : 取得所有資料
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
        sqlstr = "INSERT INTO 音色 VALUES (?, ?)"
        row = (newId, newScore)  # tuple格式
        conn.execute(sqlstr, row)
        conn.commit()
        again = input("是否繼續輸入資料 ? ")


def fnSelect02():
    sqlstr = "SELECT * FROM 音色"  # SELECT * : 取得所有資料
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
        sqlstr = "INSERT INTO 技巧 VALUES (?, ?)"
        row = (newId, newScore)  # tuple格式
        conn.execute(sqlstr, row)
        conn.commit()
        again = input("是否繼續輸入資料 ? ")


def fnSelect03():
    sqlstr = "SELECT * FROM 技巧"  # SELECT * : 取得所有資料
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
        sqlstr = "INSERT INTO 儀態 VALUES (?, ?)"
        row = (newId, newScore)  # tuple格式
        conn.execute(sqlstr, row)
        conn.commit()
        again = input("是否繼續輸入資料 ? ")


def fnSelect04():
    sqlstr = "SELECT * FROM 儀態"  # SELECT * : 取得所有資料
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
conn = sqlite3.connect(db_filename_singMatch)  # 建立資料庫連線
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

    # n = input("請選擇操作項目: ")
    n = "7"  # 跳開

    if n == "1":
        fnCreateTable()
    elif n == "2":
        while True:
            print("\n** 管理 參賽者 表單 **")
            print("   1. 新增記錄")
            print("   2. 查詢記錄")
            print("   3. 刪除記錄")
            print("   4. 回上一層操作")
            print("------------------------------")  # 30個
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
            print("------------------------------")  # 30個
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
            print("------------------------------")  # 30個
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
            print("------------------------------")  # 30個
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

conn = sqlite3.connect(db_filename_singMatch)  # 建立資料庫連線

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

conn = sqlite3.connect(db_filename_singMatch)  # 建立資料庫連線

sqlstr = "SELECT * FROM 參賽者"  # SELECT * : 取得所有資料
data = conn.execute(sqlstr)

print("編號\t姓名\t性別\t電話")
for rec in data:
    print("%d\t%s\t%s\t%s" % (rec[0], rec[1], rec[2], rec[3]))
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

# select02.py

conn = sqlite3.connect(db_filename_singMatch)  # 建立資料庫連線

sqlstr = "SELECT 姓名,電話 FROM 參賽者"
data = conn.execute(sqlstr)

print("姓名\t電話")
for rec in data:
    print("%s\t%s" % (rec[0], rec[1]))
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

# select03.py

conn = sqlite3.connect(db_filename_singMatch)  # 建立資料庫連線
# selId = int(input("請輸入要查詢的 編號 : "))
selId = 1
sqlstr = "SELECT * FROM 參賽者 WHERE 編號 = {0}".format(selId)
data = conn.execute(sqlstr)

print("編號\t姓名\t性別\t電話")
for rec in data:
    print("%d\t%s\t%s\t%s" % (rec[0], rec[1], rec[2], rec[3]))
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

# select04.py

conn = sqlite3.connect(db_filename_singMatch)  # 建立資料庫連線
# selName = input("請輸入要查詢的 姓名 : ")
selName = "a"

sqlstr = 'SELECT * FROM 參賽者 WHERE 姓名 = "{0}"'.format(selName)
data = conn.execute(sqlstr)

print("編號\t姓名\t性別\t電話")
for rec in data:
    print("%d\t%s\t%s\t%s" % (rec[0], rec[1], rec[2], rec[3]))
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

# table.py

conn = sqlite3.connect(db_filename_singMatch)  # 建立資料庫連線

# 建立表單 參賽者
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

conn = sqlite3.connect(db_filename_singMatch)  # 建立資料庫連線
# selId = int(input("請輸入要異動的 編號 : "))
selId = 1

print("\n選擇要異動的欄位名稱...")
# field = input("1.姓名  2.性別  3.電話 ..... ? ")
field = 1
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
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

d = sqlite3.Date(2004, 2, 14)
print(d)

ts = sqlite3.Timestamp(2004, 2, 14, 7, 15, 0)
ts = sqlite3.Timestamp(2004, 2, 14, 7, 15, 0, 500000)
ts = sqlite3.Timestamp(2004, 2, 14, 7, 15, 0, 510241)
print(ts)

now = datetime.datetime.now()
print(now)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
''' 資料整理 ST

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
        sqlstr = "SELECT * FROM prices WHERE gdate='{}';".format(p[0])
        cursor = conn.execute(sqlstr)
        if len(cursor.fetchall()) == 0:
            g92 = 0 if p[1]=='' else float(p[1])
            g95 = 0 if p[2]=='' else float(p[2])
            g98 = 0 if p[3]=='' else float(p[3])
            sqlstr = "INSERT INTO prices VALUES (?, ?, ?, ?)"
            x = (p[0], g92, g95, g98)  # tuple格式
            conn.execute(sqlstr, x)
            conn.commit()

return "CREATE TABLE %s (%s PRIMARY KEY %s)" % (self.name, fields, keys)

    v = db.OpenView("SELECT * FROM `%s`" % table)
    v = db.OpenView("INSERT INTO _Streams (Name, Data) VALUES ('%s', ?)" % name)

print("------------------------------------------------------------")  # 60個

print("查詢資料庫 fetchone() 讀取一筆資料")

db_filename = "applenews.db"
print("建立資料庫連線, 資料庫 :", db_filename)

conn = sqlite3.connect(db_filename)  # 建立資料庫連線

sqlstr = "SELECT count(*) FROM news;"
result = conn.execute(sqlstr)
count = result.fetchone()[0]  # 讀取一筆資料
print(count)

sqlstr = "SELECT count(*) FROM news WHERE url='{}';".format(content_url)
result = conn.execute(sqlstr)
count = result.fetchone()[0]  # 讀取一筆資料

sqlstr = "INSERT INTO news (url, title, content) VALUES (?, ?, ?)"
x = (content_url, title, data)  # tuple格式
conn.execute(sqlstr, x)

print("------------------------------------------------------------")  # 60個

conn = sqlite3.connect(db_filename)  # 建立資料庫連線

cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS Course ( " +
               "courseId char(5), subjectId char(4) not null, " +
               "courseNumber integer, title varchar(50) not null, " +
               "numOfCredits integer, primary key (courseId))")

cursor.execute("INSERT INTO Course (courseId, subjectId, " + 
               " courseNumber, title, numOfCredits) " + 
               "values ('11113', 'CSCI', '3720', 'Database Systems', 3)")

cursor.execute("INSERT INTO Course (courseId, subjectId, " + 
               " courseNumber, title, numOfCredits) " + 
               "values ('11111', 'CSCI', '1301', 'Introduction to Programming', 3)")
conn.commit()

cursor.execute("SELECT * FROM Course")  # SELECT * : 取得所有資料

rows = cursor.fetchall()

print(rows)

conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個

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

db : 資料庫 db
table : 表單 資料表(x)

print("建立表單")

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

# INSERT INTO 新增資料
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
5.
cursor.execute("DELETE FROM table01 WHERE filename = ?", (filename,))
cursor.execute("DELETE FROM table01 WHERE filename = ?", ("aaaa.mp4",))
cursor.execute("DELETE FROM people WHERE age=20")

其他
# DROP TABLE 刪除表單
sqlstr = "DROP TABLE IF EXISTS table01"
cursor = conn.execute(sqlstr)

columns = conn.execute(f"PRAGMA table_info('{table_name}');").fetchall()


新進測試
建立多個表單 要分開寫

# xxxx do_fetchall(cursor)

rows = cursor.fetchall()  # 讀取全部資料成元組串列
length = len(rows)
print("共有", length, "筆資料")
for i in range(length):
    print("第" + str(i + 1) + "筆資料 : ", rows[i])


# 語法:
INSERT INTO archive_orders SELECT * FROM orders WHERE order_date < "2016-01-01",
DELETE FROM orders WHERE order_date < "2016-01-01",

sqlstr = """
CREATE TABLE IF NOT EXISTS table01(
id      INTEGER PRIMARY KEY NOT NULL,
name    TEXT NOT NULL,
chinese INTEGER NOT NULL,
english INTEGER NOT NULL,
math    INTEGER NOT NULL
)
"""

sqlstr = """
CREATE TABLE IF NOT EXISTS table01(
id      INTEGER PRIMARY KEY NOT NULL,
name    TEXT NOT NULL,
chinese INTEGER NOT NULL,
english INTEGER NOT NULL,
math    INTEGER NOT NULL
)
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

注意：不要使用%s 將字串插入 SQL 命令，
因為它可能使你的程式容易受到 SQL 注入攻擊（請參閱 SQL 注入 ）。

# DROP TABLE 刪除表單
sqlstr = "DROP TABLE IF EXISTS table01"
cursor.execute(sqlstr)



# 建立表單 範例

# 建立表單 table01 + PRIMARY KEY
sqlstr = """
CREATE TABLE IF NOT EXISTS table01(
id      INTEGER PRIMARY KEY AUTOINCREMENT, -- 序號(id)整數自動遞增, 可填可不填
name    TEXT NOT NULL,
age     INTEGER NOT NULL,
address CHAR(50),
salary  REAL
)
"""
# 建立表單 table01 + PRIMARY KEY
sqlstr = """
CREATE TABLE IF NOT EXISTS table01(
id serial                 NOT NULL,
uid character varying(50) NOT NULL,
PRIMARY KEY (id))
"""
# 建立表單 table02 + PRIMARY KEY
sqlstr = """
CREATE TABLE IF NOT EXISTS table02(
id serial NOT NULL,
uid character varying(50) NOT NULL,
PRIMARY KEY (id))
"""
# 建立表單 table03 + PRIMARY KEY
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
# 建立表單 table04 + PRIMARY KEY
sqlstr = """
CREATE TABLE IF NOT EXISTS table04(
sid serial NOT NULL,
name character varying(50) NOT NULL,
tel character varying(50),
addr character varying(200),
email character varying(100),
PRIMARY KEY (sid))
"""
# 建立表單 users1 + PRIMARY KEY
sqlstr = """
CREATE TABLE IF NOT EXISTS users1(
id serial NOT NULL,
uid character varying(50) NOT NULL,
question character varying(250) NOT NULL,
PRIMARY KEY (id))
"""
# 建立表單 login + PRIMARY KEY
sqlstr = """
CREATE TABLE IF NOT EXISTS login(
id serial NOT NULL,
uid character varying(50) NOT NULL,
state character varying(10) NOT NULL,
PRIMARY KEY (id))
"""
# 建立表單 users2 + PRIMARY KEY
sqlstr = """
CREATE TABLE IF NOT EXISTS users2(
id serial NOT NULL,
uid character varying(50) NOT NULL,
state character varying(10) NOT NULL,
digit3 character varying(10) NOT NULL,
PRIMARY KEY (id))
"""
# 建立表單 setting + PRIMARY KEY
sqlstr = """
CREATE TABLE IF NOT EXISTS setting(
id serial NOT NULL,
uid character varying(50) NOT NULL,
lang character varying(10) NOT NULL,
sound character varying(10) NOT NULL,
PRIMARY KEY (id))
"""

sqlstr = """
CREATE TABLE IF NOT EXISTS table01(
NAME    TEXT NOT NULL,
ADDRESS CHAR(50),
BILL    REAL
)
"""

create_weather = """
CREATE TABLE weather(
id      text NOT NULL,
year    integer NOT NULL,
month   integer NOT NULL,
element text NOT NULL,
max     real,
min     real,
mean    real,
count   integer
)
"""

# dddddddddd 可刪除檔案 與 準備刪除的code ST




# dddddddddd 可刪除檔案 與 準備刪除的code SP

# 3030
print("------------------------------")  # 30個

寫法比較

# INSERT INTO 比較好的寫法

sqlstr = "INSERT INTO table01 (id_num, ename, weight) VALUES (?, ?, ?)"
x = (2, 'sheep', 66)  # tuple格式
cursor.execute(sqlstr, x)

# 用.format 比較不好
sqlstr = ("INSERT INTO table01 (id_num, ename, weight) VALUES ({}, '{}', '{}')".format(data[0], data[1], data[2])

相同
.connect = .Connection
conn = sqlite3.connect(db_filename)  # 建立資料庫連線
conn = sqlite3.Connection(db_filename)  # 建立資料庫連線

資料整理 SP'''

# INSERT INTO 之後要  conn.commit()  ???

''' tmp code ST
class FunctionTests(unittest.TestCase):
    def setUp(self):
        self.con = sqlite.connect(":memory:")
        val = cur.fetchone()[0]

    def CheckAggrCheckAggrSum(self):
        cur = self.con.cursor()
        cur.execute("delete from test")
        cur.executemany("insert into test(i) values (?)", [(10,), (20,), (30,)])
        cur.execute("select mysum(i) from test")
        val = cur.fetchone()[0]
        self.assertEqual(val, 60)

class AuthorizerTests(unittest.TestCase):
    @staticmethod
    def authorizer_cb(action, arg1, arg2, dbname, source):
        if action != sqlite.SQLITE_SELECT:
            return sqlite.SQLITE_DENY
        if arg2 == 'c2' or arg1 == 't2':
            return sqlite.SQLITE_DENY
        return sqlite.SQLITE_OK

    def setUp(self):
        self.con = sqlite.connect(":memory:")
        self.con.executescript("""
            create table t1 (c1, c2);
            create table t2 (c1, c2);
            insert into t1 (c1, c2) values (1, 2);
            insert into t2 (c1, c2) values (4, 5);
            """)

        # For our security test:
        self.con.execute("select c2 from t2")

        self.con.set_authorizer(self.authorizer_cb)

tmp code ST'''

# self.cur.execute("create table test(d date, ts timestamp)")
# self.cur.execute("create table test(i int, s str, f float, b bool, u unicode, foo foo, bin blob, n1 number, n2 number(5))")
# self.cur.execute("create table test(i integer, s varchar, f number, b blob)")

print("------------------------------------------------------------")  # 60個

conn = sqlite3.connect("datafilecccc.db")

cursor = conn.cursor()

# cursor

cursor.execute("create table people (id integer primary key, name text, count integer)")

cursor.execute("insert into people (name, count) values ('Bob', 1)")
cursor.execute("insert into people (name, count) values (?, ?)", ("Jill", 15))

conn.commit()

cursor.execute(
    "insert into people (name, count) values (:username, :usercount)",
    {"username": "Joe", "usercount": 10},
)


result = cursor.execute("select * from people")
print(result.fetchall())

# [(1, 'Bob', 1), (2, 'Jill', 15), (3, 'Joe', 10)]

result = cursor.execute("select * from people where name like :name", {"name": "bob"})

print(result.fetchall())
# [(1, 'Bob', 1)]

cursor.execute("update people set count=? where name=?", (20, "Jill"))

result = cursor.execute("select * from people")

print(result.fetchall())
# [(1, 'Bob', 1), (2, 'Jill', 20), (3, 'Joe', 10)]


result = cursor.execute("select * from people")

for row in result:
    print(row)

# (1, 'Bob', 1)
# (2, 'Jill', 20)
# (3, 'Joe', 10)


cursor.execute("update people set count=? where name=?", (20, "Jill"))
conn.commit()
conn.close()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# SQL (SQLite)

db_filename = "tmp_salary_table.db"

conn = sqlite3.connect(db_filename)

##############################################################################
salary = pd.read_csv("data/salary_table.csv")
print(salary.head())

salary.to_sql("salary", conn, if_exists="replace")

##############################################################################
# Push modifications

cur = conn.cursor()
values = (100, 14000, 5, "Bachelor", "N")
cur.execute("insert into salary values (?, ?, ?, ?, ?)", values)
conn.commit()

##############################################################################
# Reading results into a pandas DataFrame

salary_sql = pd.read_sql_query("select * from salary;", conn)
print(salary_sql.head())

pd.read_sql_query("select * from salary;", conn).tail()
pd.read_sql_query("select * from salary where salary>25000;", conn)
pd.read_sql_query("select * from salary where experience=16;", conn)
pd.read_sql_query('select * from salary where education="Master";', conn)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "youtube_trends_selenium.sqlite"

print("title:", title.encode(sys.getfilesystemencoding()))
print("link:", link.encode(sys.getfilesystemencoding()))
print("autor_name:", autor_name.encode(sys.getfilesystemencoding()))
print("autor_link:", autor_link.encode(sys.getfilesystemencoding()))
print("watch:", watch.encode(sys.getfilesystemencoding()))
print("=======================")

# 連接資料庫
print("ssss")
conn = sqlite3.connect(filename)
with conn:
    cursor = conn.cursor()
    sql = (
        "CREATE TABLE IF NOT EXISTS "
        + table
        + "(Id INTEGER PRIMARY key autoincrement, title TEXT, link TEXT, autor_name TEXT, autor_link TEXT, views TEXT )"
    )
    cursor.execute(sql)
    # INSERT INTO table VALUES(NULL,'title','link','autor_name','autor_link','watch')
    sql = (
        "INSERT INTO "
        + table
        + " VALUES(NULL,'"
        + title
        + "','"
        + link
        + "','"
        + autor_name
        + "','"
        + autor_link
        + "','"
        + watch
        + "')"
    )
    try:
        cursor.execute(sql)
    except:
        print("Write SQLite error:", sql.encode(sys.getfilesystemencoding()))


# 如果資料庫已經存在則移除
if os.path.exists(filename):
    os.remove(filename)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
# Writing to a SQLite database

weather_df = pd.read_csv("data/weather_2012.csv")
con = sqlite3.connect("tmp_test_db.sqlite")
con.execute("DROP TABLE IF EXISTS weather_2012")
weather_df.to_sql("weather_2012", con)

con = sqlite3.connect("tmp_test_db.sqlite")
df = pd.read_sql("SELECT * from weather_2012 LIMIT 3", con)
print(df)

con = sqlite3.connect("tmp_test_db.sqlite")
df = pd.read_sql("SELECT * from weather_2012 ORDER BY Weather LIMIT 3", con)
print(df)

print("------------------------------------------------------------")  # 60個

con = sqlite3.connect("data/weather_2012.sqlite")
df = pd.read_sql("SELECT * from weather_2012 LIMIT 3", con)
print(df)

print("------------------------------")  # 30個

df = pd.read_sql("SELECT * from weather_2012 LIMIT 3", con, index_col="id")
print(df)

print("------------------------------")  # 30個

df = pd.read_sql(
    "SELECT * from weather_2012 LIMIT 3", con, index_col=["id", "date_time"]
)
print(df)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("使用數據庫")

# 使用 SQLite3

# 連接資料庫
con = sqlite3.connect(":memory:")

# 建立資料表
query = """
CREATE TABLE test
(a VARCHAR(20), b VARCHAR(20), c REAL, d INTEGER);
"""
con.execute(query)
con.commit()

# 插入資料
data = [
    ("Atlanta", "Georgia", 1.25, 6),
    ("Tallahassee", "Florida", 2.6, 3),
    ("Sacramento", "California", 1.7, 5),
]
stmt = "INSERT INTO test VALUES(?, ?, ?, ?)"
con.executemany(stmt, data)
con.commit()


# 查詢資料
cursor = con.execute("select * from test")
rows = cursor.fetchall()
print(rows)

"""
[('Atlanta', 'Georgia', 1.25, 6),
 ('Tallahassee', 'Florida', 2.6, 3),
 ('Sacramento', 'California', 1.7, 5)]
"""

# 看起來沒內容
# cursor.description 包含 欄位資訊
print(cursor.description)


# 用資料庫的資料建立 DataFrame
df = pd.DataFrame(rows, columns=[f[0] for f in cursor.description])
print(df)

# 使用 pandas.io.sql 來讀取資料庫資料並創建 DataFrame

import pandas.io.sql as sql

df = sql.read_sql("select * from test", con)
print(df)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
