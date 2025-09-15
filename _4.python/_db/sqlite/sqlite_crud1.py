"""
sqlite基本範例 一個 基本款

增刪查改（英語：CRUD），全稱
增加（CREATE）
刪除（DELETE）
查詢（READ）
改正（UPDATE）
在電腦程式語言中是一連串常見的動作行為

	 idx	英文名	中文名	體重
第 1筆 :  1	mouse	米老鼠	3
第 2筆 :  2	ox	班尼牛	48
第 3筆 :  3	tiger	跳跳虎	33
第 4筆 :  4	rabbit	彼得兔	8
第 5筆 :  5	dragon	逗逗龍	38
第 6筆 :  6	snake	貪吃蛇	16
第 7筆 :  7	horse	草泥馬	31
第 8筆 :  8	goat	喜羊羊	29
第 9筆 :  9	monkey	山道猴	22
第10筆 : 10	chicken	肯德雞	5
第11筆 : 11	dog	貴賓狗	17
第12筆 : 12	pig	佩佩豬	42

# sqlite基本範例 其他
# 同一個資料庫內 可以放多個table table名稱不同即可

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
表單名稱

ColumnName    DataType
欄名      

SQL之資料一定要"方正" ???    不一定
sqlite試用一下輸入NULL 或是用'' ""即可  不一定

# 各種fetch
fetchone()  # 讀取一筆資料	        # 抓一行 tuple
fetchall()  # 讀取全部資料成元組串列	# 抓取剩下的全部 list

fetchmany(size=cursor.arraysize)	# 抓n行 list
fetchmany(100)
fetchmany(size=100)
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
    # return
    plt.tight_layout()  # 緊密排列，並填滿原圖大小
    plt.show()


print("------------------------------------------------------------")  # 60個

import csv
import shutil
import datetime
import sqlite3


def show_data_base_contents0(conn, table_name):
    # SELECT * : 取得所有資料
    sqlstr = "SELECT * FROM {};".format(table_name)  # same
    sqlstr = "SELECT * FROM %s" % table_name
    cursor = conn.execute(sqlstr)
    # 使用fetchall()
    rows = cursor.fetchall()  # 讀取全部資料成元組串列
    length = len(rows)
    print("共有", length, "筆資料")
    for i in range(length):
        print("第" + str(i + 1) + "筆資料 : ", rows[i])
        if i > 10:
            break
    """
    # 不使用fetchall()
    i = 0
    for row in cursor:  # 不是用fetchall()讀取全部資料
        print("第" + str(i + 1) + "筆資料 : ", row)
        i += 1
        if i > 10:
            break
    """


def show_data_base_contents(db_filename, table_name):
    conn = sqlite3.connect(db_filename)  # 建立資料庫連線
    show_data_base_contents0(conn, table_name)
    conn.close()  # 關閉資料庫連線


current_time = datetime.datetime.now().strftime("%Y/%m/%d %a %H:%M:%S")
print("現在時間 :", current_time)

version = sqlite3.sqlite_version_info
print("目前 sqlite3 版本 :", version)

print("------------------------------------------------------------")  # 60個

print("建立資料庫 + INSERT INTO 加入資料 + 讀取資料 + DROP")

db_filename = "tmp_db01_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".sqlite"

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

# 建立表單
# PRIMARY KEY 主鍵 不可重複
# 序號 自動遞增 不會重複
sqlstr = """
CREATE TABLE IF NOT EXISTS table01(
idx    INTEGER PRIMARY KEY AUTOINCREMENT, -- 序號(idx)整數自動遞增, 可填可不填
英文名 TEXT NOT NULL,
中文名 TEXT,
體重   INTEGER NOT NULL CHECK(體重 > 0) -- 預設錯誤時會顯示
)
"""
cursor.execute(sqlstr)
conn.commit()  # 更新

# INSERT INTO 新增資料, 有些欄位可以不寫, 序號(idx)自動遞增

# 資料寫2項 有填序號
sqlstr = "INSERT INTO table01 (idx, 英文名, 中文名, 體重) VALUES (?, ?, ?, ?)"

x = (1, "mouse", "米老鼠", 3)  # tuple格式
cursor.execute(sqlstr, x)
x = (2, "ox", "班尼牛", 48)  # tuple格式
cursor.execute(sqlstr, x)

# 資料寫5項 沒有填序號
sqlstr = "INSERT INTO table01 (英文名, 體重) VALUES (?, ?)"
x = ("tiger", 33)  # tuple格式
cursor.execute(sqlstr, x)
x = ("rabbit", 8)  # tuple格式
cursor.execute(sqlstr, x)
x = ("dragon", 38)  # tuple格式
cursor.execute(sqlstr, x)
x = ("snake", 16)  # tuple格式
cursor.execute(sqlstr, x)
x = ("horse", 31)  # tuple格式
cursor.execute(sqlstr, x)

# DROP TABLE 刪除表單 如果存在的話
# sqlstr = "DROP TABLE IF EXISTS table01"
# cursor = conn.execute(sqlstr)

conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

print("讀取資料庫")
table_name = "table01"
show_data_base_contents(db_filename, table_name)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("建立資料庫 + INSERT INTO 加入串列資料 + SELECT + UPDATE + DELETE")

db_filename = "tmp_db02_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".sqlite"

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

# 建立表單
# PRIMARY KEY 主鍵 不可重複
# 序號 自動遞增 不會重複
sqlstr = """
CREATE TABLE IF NOT EXISTS table01(
idx    INTEGER PRIMARY KEY AUTOINCREMENT, -- 序號(idx)整數自動遞增, 可填可不填
英文名 TEXT NOT NULL,
中文名 TEXT,
體重   INTEGER NOT NULL CHECK(體重 > 0) -- 預設錯誤時會顯示
)
"""
cursor.execute(sqlstr)
conn.commit()  # 更新

# INSERT INTO 新增資料 多筆, 使用串列
sqlstr = "INSERT INTO table01 (英文名, 體重, 中文名) VALUES (?, ?, ?)"

# 元組串列
animals = [
    ("mouse", 3, "米老鼠"),
    ("ox", 48, "班尼牛"),
    ("tiger", 33, "跳跳虎"),
    ("rabbit", 8, "彼得兔"),
    ("dragon", 38, "逗逗龍"),
    ("snake", 16, "貪吃蛇"),
    ("horse", 31, "草泥馬"),
    ("goat", 29, "喜羊羊"),
    ("monkey", 22, "山道猴"),
    ("chicken", 5, "肯德雞"),
    ("dog", 17, "貴賓狗"),
    ("pig", 42, "佩佩豬"),
]

print("測試 executemany, 一次執行多個指令")

# 一次執行多個指令
cursor = conn.executemany(sqlstr, animals)  # 一次執行多個指令
print("新增資料行數 :", cursor.rowcount)

# SELECT 顯示表單資料 只看2欄
for row in conn.execute("SELECT 英文名, 體重 FROM table01"):
    print(row)

# 刪除表單 全部
# cursor = conn.execute("DELETE FROM table01")
# print("刪除資料行數 :", cursor.rowcount)

conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("讀取資料庫")
table_name = "table01"
show_data_base_contents(db_filename, table_name)

print("------------------------------")  # 30個

print("測試 SELECT 用法")

# 加各種搜尋資料在此 SELECT

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

# idx, 英文名, 中文名, 體重

# SELECT * FROM 表單           : 取得資料
# SELECT * FROM 表單 WHERE 條件: 取得資料 + 條件

print("------------------------------")  # 30個

print("無條件搜尋 + 抓資料方法")

# 要事先知道表單的欄位

print("查詢資料庫 fetchone() 讀取一筆資料")
print("從資料庫讀出一筆資料")

print("讀取資料庫")
print("用 SELECT * FROM 表單 # SELECT * : 取得所有資料")

print("------------------------------")  # 30個

print("查詢資料庫 fetchone() 讀取一筆資料")
sqlstr = "SELECT * FROM table01"  # SELECT * : 取得所有資料
cursor = conn.execute(sqlstr)
row = cursor.fetchone()  # 讀取一筆資料
print(row)

print("------------------------------")  # 30個

# SELECT 取得 指定欄位 1欄

print("讀取一欄資料全部")
cursor = conn.execute("SELECT 英文名 FROM table01")
row = cursor.fetchall()  # 讀取一筆資料
print(row)

print("------------------------------")  # 30個

# SELECT 取得 指定欄位 2欄

print("讀取二欄資料全部")
cursor = conn.execute("SELECT 中文名, 體重 FROM table01")
row = cursor.fetchall()  # 讀取一筆資料
print(row)

print("------------------------------")  # 30個

print("SELECT + WHERE 取得資料 + 條件1")

sqlstr = "SELECT * FROM table01 WHERE 中文名 = ?"
name = ("跳跳虎",)  # tuple格式
cursor.execute(sqlstr, name)
print("讀取一筆資料")
row = cursor.fetchone()  # 讀取一筆資料
print(row)

print("------------------------------")  # 30個

print("SELECT + WHERE 取得資料 + 條件2")

# SELECT * : 取得所有資料 + 條件
sqlstr = "SELECT * FROM table01 WHERE 體重 > ?"
min_weight = (30,)  # tuple格式
cursor = conn.execute(sqlstr, min_weight)
# 不是用fetchall()讀取全部資料
for row in cursor:  # 不是用fetchall()讀取全部資料
    print(row)

# 同條件再搜尋一次
cursor = conn.execute(sqlstr, min_weight)

print("讀取一筆資料")
row = cursor.fetchone()  # 讀取一筆資料
if not row == None:
    print(row)

print("讀取一筆資料")
row = cursor.fetchone()  # 讀取一筆資料
if not row == None:
    print(row)

print("讀取3筆資料")
rows = cursor.fetchmany(3)
print(rows)

print("fetchall()  # 讀取全部資料")
rows = cursor.fetchall()  # 讀取全部資料成元組串列
if not rows == None:
    print(rows)

print("------------------------------")  # 30個

# SELECT * WHERE : 取得所有資料 + 條件
index = 2
cursor = conn.execute("SELECT * FROM table01 WHERE idx=?", (str(index),))
rows = cursor.fetchall()  # 讀取全部資料成元組串列
print(rows)

print("------------------------------")  # 30個

new_name = "DRAGON"

# 無 LIKE, 一定要符合大小寫
sqlstr = "SELECT * FROM table01 WHERE 英文名 = '{}'".format(new_name)
# 有 LIKE, 大小寫皆可
sqlstr = "SELECT * FROM table01 WHERE 英文名 LIKE '{}'".format(new_name)

cursor = conn.execute(sqlstr)

print("讀取一筆資料")
row = cursor.fetchone()  # 讀取一筆資料

if not row == None:
    print("取得資料 :", row)
else:
    print("找不到資料")

print("------------------------------")  # 30個

old_name = "snake"
sqlstr = "SELECT * FROM table01 WHERE 英文名 = '{}'".format(old_name)
cursor = conn.execute(sqlstr)

print("讀取一筆資料")
row = cursor.fetchone()  # 讀取一筆資料
print(row)

name = "snake"
sqlstr = "SELECT * FROM table01 WHERE 英文名 = '{}'".format(name)
cursor = conn.execute(sqlstr)

print("讀取一筆資料")
row = cursor.fetchone()  # 讀取一筆資料

print("------------------------------")  # 30個

print("SELECT + WHERE 取得資料 + 條件3")

cursor.execute("SELECT * FROM table01 WHERE 英文名 = ?", ("rabbit",))

rows = cursor.fetchall()  # 讀取全部資料成元組串列
length = len(rows)
print("共有", length, "筆資料")
for i in range(length):
    print("第" + str(i + 1) + "筆資料 : ", rows[i])

# SELECT * WHERE : 取得所有資料 + 條件
name = "rabbit"
cursor.execute("SELECT * FROM table01 WHERE 英文名 = ?", (name,))
rows = cursor.fetchall()  # 讀取全部資料成元組串列
length = len(rows)
print("共有", length, "筆資料")
for i in range(length):
    print("第" + str(i + 1) + "筆資料 : ", rows[i])

"""
print("DELETE + 條件")

cursor.execute("DELETE FROM table01 WHERE 中文名 = ?", ("貴賓狗",))

name = "rabbit"
cursor.execute("DELETE FROM table01 WHERE 英文名 = ?", (name,))

cursor.execute("DELETE FROM table01 WHERE idx = ?", (8,))

cursor.execute("DELETE FROM table01 WHERE 體重 = 38")

print("DELETE 刪除資料 條件")
name = "monkey"
sqlstr = "DELETE FROM table01 WHERE 英文名 = '{}'".format(name)
conn.execute(sqlstr)

print("DELETE 刪除資料, 刪除7號的資料")
sqlstr = "DELETE FROM table01 WHERE idx = {}".format(7)
conn.execute(sqlstr)

sqlstr = "DELETE FROM table01 WHERE idx = 2"
cursor = conn.execute(sqlstr)

print("DELETE 刪除資料 條件 1筆, 刪除11號")
# DELETE 刪除資料 條件 id 為 11 之資料
conn.execute("DELETE FROM table01 WHERE idx = {}".format(11))
"""
print("------------------------------")  # 30個
print("------------------------------")  # 30個
"""
print('SELECT + LIMIT 取得資料 + 讀取個數')

print("只讀前5筆")
sqlstr = "SELECT * FROM table01 LIMIT 5"  # SELECT * : 取得所有資料, 限制10筆
cursor = conn.execute(sqlstr)
rows = cursor.fetchall()  # 讀取全部資料成元組串列
length = len(rows)
print("共有", length, "筆資料")
for i in range(length):
    print("第" + str(i + 1) + "筆資料 : ", rows[i])

print("從第3筆開始讀5筆資料(從0起算)")
sqlstr = "SELECT * FROM table01 LIMIT 3, 5"
cursor = conn.execute(sqlstr)
rows = cursor.fetchall()  # 讀取全部資料成元組串列
length = len(rows)
print("共有", length, "筆資料")
for i in range(length):
    print("第" + str(i + 1) + "筆資料 : ", rows[i])

print("讀5筆資料出來, 從第3筆開始讀 (從0起算)")
sqlstr = "SELECT * FROM table01 LIMIT 5 OFFSET 3"
cursor = conn.execute(sqlstr)
rows = cursor.fetchall()  # 讀取全部資料成元組串列
length = len(rows)
print("共有", length, "筆資料")
for i in range(length):
    print("第" + str(i + 1) + "筆資料 : ", rows[i])

print("------------------------------")  # 30個

cursor = conn.execute("SELECT * FROM table01 WHERE 中文名 LIKE :name", {"name": "跳跳虎"})
rows = cursor.fetchall()  # 讀取全部資料成元組串列
print(rows)
"""
print("------------------------------")  # 30個
print("------------------------------")  # 30個

print("SELECT + ORDER 取得資料 + 排序")

# SELECT * : 取得資料 排列 依 體重 升冪
sqlstr = "SELECT * FROM table01 ORDER BY 體重"
cursor = conn.execute(sqlstr)
for row in cursor:
    print(row)

# SELECT * : 取得資料 排列 依 體重 升冪
sqlstr = "SELECT * FROM table01 ORDER BY 體重"
cursor.execute(sqlstr)

print("讀取一筆資料")
row = cursor.fetchone()  # 讀取一筆資料
print("a讀取一筆資料", row)

while row:
    print("讀取一筆資料")
    row = cursor.fetchone()  # 讀取一筆資料
    print("b讀取一筆資料", row)

print("------------------------------")  # 30個

print("用fetchall()讀取 全部資料 依 體重 排序, 降冪")

conn = sqlite3.connect(db_filename)  # 建立資料庫連線

# SELECT * : 取得資料 排列 依 體重 升冪
# cursor = conn.execute("SELECT * FROM table01 ORDER BY 體重;")  #由小到大, 升冪

# SELECT * : 取得資料 排列 依 體重 降冪
cursor = conn.execute("SELECT * FROM table01 ORDER BY 體重 DESC;")  # 由小到大 + 反相 = 由大到小, 降冪

print("取得所有資料 搜尋")
for row in cursor:  # 不是用fetchall()讀取全部資料
    print(row)

print("------------------------------")  # 30個

print("用fetchall()讀取 全部資料 依 英文名 排序, 升冪")

conn = sqlite3.connect(db_filename)  # 建立資料庫連線

# SELECT * : 取得資料 排列 依 英文名 升冪
sqlstr = "SELECT * FROM table01 ORDER BY 英文名;"  # 由小到大, 升冪

# SELECT * : 取得資料 排列 依 英文名 降冪
# cursor = conn.execute("SELECT * FROM table01 ORDER BY 英文名 DESC;")  #由小到大 + 反相 = 由大到小, 降冪

cursor = conn.execute(sqlstr)

print("取得所有資料 搜尋")
for row in cursor:  # 不是用fetchall()讀取全部資料
    print(row)

print("------------------------------")  # 30個
print("------------------------------")  # 30個
"""
print("UPDATE 更新資料 修改資料")

# UPDATE 更新資料, 修改表單 table01 內, 修改 中文名 = "虎" 的資料的 體重 內容, 改為 123
cursor.execute("UPDATE table01 SET 體重=? WHERE 中文名 = ?", (123, "虎"))

# UPDATE 更新資料, 修改表單 table01 內, 修改 英文名 = 'snake' 的資料的 中文名 內容, 改為 '小龍'
cursor.execute("UPDATE table01 SET 中文名 = '小龍' WHERE 英文名 = 'snake'")

# UPDATE 更新資料, 修改表單 table01 內, 修改 idx = 6 的資料的 中文名 內容, 改為 '小龍'
cursor.execute("UPDATE table01 SET 中文名 = '小龍' WHERE idx = 6")

# UPDATE 更新資料, 修改表單 table01 內, 修改 idx = 2 的資料的 體重 內容, 改為 53
sqlstr = "UPDATE table01 SET 體重 = '{}' WHERE idx = {}".format(53, 2)
conn.execute(sqlstr)  # 修改2號的資料, 要先確保已經有2號的資料, 才可以修改

# UPDATE 更新資料, 修改表單 table01 內, 修改 英文名 = 'tiger' 的資料的 中文名 內容, 改為 '大蛇'
sqlstr = "UPDATE table01 SET 中文名 = '{}' WHERE 英文名 = '{}'".format("大蛇", "snake")
conn.execute(sqlstr)

# UPDATE 更新資料, 修改表單 table01 內, 修改 idx = 1 的資料的 中文名 內容, 改為 "傑利鼠"
sqlstr = "UPDATE table01 SET 中文名 = '傑利鼠' WHERE idx = 1"
conn.execute(sqlstr)

# UPDATE 更新資料, 修改表單 table01 內, 修改 idx = 8 的資料的 英文名 內容, 改為 sheep
sqlstr = "UPDATE table01 SET 英文名 = '{}' WHERE idx = {}".format("sheep", 8)
conn.execute(sqlstr)  # 修改8號的資料, 要先確保已經有8號的資料, 才可以修改
"""
conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

print("讀取資料庫")
table_name = "table01"
show_data_base_contents(db_filename, table_name)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

db_filename = "tmp_db03_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".sqlite"

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

# 建立表單
# 多了檢查條件
# 序號 自動遞增 不可重複
sqlstr = """
CREATE TABLE IF NOT EXISTS table01(
idx    INTEGER PRIMARY KEY AUTOINCREMENT, -- 序號(idx)整數自動遞增, 可填可不填
id_num INTEGER NOT NULL,
英文名 TEXT NOT NULL,
中文名 TEXT,
體重   INTEGER NOT NULL CHECK(體重 > 0) -- 預設錯誤時會顯示
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
sqlstr = "INSERT INTO table01 (id_num, 英文名, 中文名, 體重) VALUES (?, ?, ?, ?)"
x = (4, "elephant", "象", 100)  # tuple格式
cursor.execute(sqlstr, x)

print("INSERT INTO 新增資料 2 筆 寫法三, 有些欄位可以不寫, 序號自動遞增")

sqlstr = "INSERT INTO table01 (id_num, 英文名, 體重) VALUES (?, ?, ?)"
x = (9, "ox", 48)  # tuple格式
cursor.execute(sqlstr, x)

# id_num不重複 但name 體重 重複
sqlstr = "INSERT INTO table01 (id_num, 英文名, 體重) VALUES (?, ?, ?)"
x = (2, "sheep", 66)  # tuple格式
cursor.execute(sqlstr, x)

print("INSERT INTO 新增資料 2 筆 寫法四, 有些欄位可以不寫, 序號自動遞增")
# 定義資料串列
datas = [[8, "snake", 16], [3, "tiger", 33]]

for data in datas:
    print(data)
    sqlstr = "INSERT INTO table01 (id_num, 英文名, 體重) VALUES (?, ?, ?)"
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

print("查詢資料庫 fetchone() 讀取一筆資料")

# SELECT 取得
conn = sqlite3.connect(db_filename)  # 建立資料庫連線

# SELECT * WHERE : 取得所有資料 + 條件
print("指明抓一筆資料, 9號")
number = 9
sqlstr = "SELECT * FROM table01 WHERE id_num = " + str(number)  # 條件
cursor = conn.execute(sqlstr)

print("讀取一筆資料")
row = cursor.fetchone()  # 讀取一筆資料
if not row == None:
    print(row)
else:
    print("找不到" + str(number) + "號資料")

print("------------------------------")  # 30個

# SELECT * WHERE : 取得所有資料 + 條件
print("指明抓一筆資料, 15號")
number = 15
sqlstr = "SELECT * FROM table01 WHERE id_num = " + str(number)  # 條件
cursor = conn.execute(sqlstr)

print("讀取一筆資料")
row = cursor.fetchone()  # 讀取一筆資料
if not row == None:
    print(row)
else:
    print("找不到" + str(number) + "號資料")

print("------------------------------")  # 30個

# SELECT * WHERE : 取得所有資料 + 條件
print("指明抓名字有bb的資料")
data = ("%bb%",)  # bb在中間 前後要有%
# sqlstr =
cursor = conn.execute("SELECT * FROM table01 WHERE 英文名 LIKE ?", data)  # 條件
rows = cursor.fetchall()  # 讀取全部資料成元組串列
length = len(rows)
print("共有", length, "筆資料")
for i in range(length):
    print("第" + str(i + 1) + "筆資料 : ", rows[i])

conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

print("尋找資料")

conn = sqlite3.connect(db_filename)  # 建立資料庫連線

# SELECT * WHERE : 取得所有資料 + 條件
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

print("------------------------------")  # 30個

print("不是用fetchall()讀取 全部資料")

conn = sqlite3.connect(db_filename)  # 建立資料庫連線

table_name = "table01"
show_data_base_contents0(conn, table_name)

conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

print("用fetchall()讀取 全部資料")

print("讀取資料庫")
print("用fetchall()讀取 全部資料 預設排序(依第1項升冪排序)")
table_name = "table01"
show_data_base_contents(db_filename, table_name)

conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("測試 序號自動遞增")

db_filename = "tmp_db04_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".sqlite"

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

# 建立表單
sqlstr = """
CREATE TABLE IF NOT EXISTS table01(
idx    INTEGER PRIMARY KEY AUTOINCREMENT, -- 序號(idx)整數自動遞增, 可填可不填
中文名 TEXT NOT NULL,
體重   INTEGER NOT NULL
)
"""
cursor.execute(sqlstr)

print("有設定序號 123")
sqlstr = "INSERT INTO table01 (idx, 中文名, 體重) VALUES (?, ?, ?)"
x = (123, "喜羊羊", 29)  # tuple格式
cursor.execute(sqlstr, x)

print("沒有設定序號, 系統自動遞增")
sqlstr = "INSERT INTO table01 (中文名, 體重) VALUES (?, ?)"

x = ("山道猴", 22)  # tuple格式
cursor.execute(sqlstr, x)

x = ("肯德雞", 5)  # tuple格式
cursor.execute(sqlstr, x)

conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("讀取資料庫")
table_name = "table01"
show_data_base_contents(db_filename, table_name)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("測試 DATE/TIMESTAMP 時間戳")

"""
print('製作 DATE/TIMESTAMP 時間戳')
dd = datetime.date.today()
tt = time.time()
tt = datetime.datetime.now()
tt = datetime.datetime.now().strftime("%Y/%m/%d %a %H:%M:%S")
"""

db_filename = "tmp_db05_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".sqlite"

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

sqlstr = """
CREATE TABLE IF NOT EXISTS table01(
login_name TEXT,
login_date DATE,
login_time TIMESTAMP
)
"""
conn.execute(sqlstr)

# INSERT INTO 新增資料
sqlstr = "INSERT INTO table01 (login_name, login_date, login_time) VALUES (?, ?, ?)"

nn = "肯德雞"
dd = datetime.date.today()
tt = datetime.datetime.now().strftime("%Y/%m/%d %a %H:%M:%S")
x = (nn, dd, tt)  # tuple格式
conn.execute(sqlstr, x)

time.sleep(0.3456)  # 過了一段時間

nn = "貴賓狗"
dd = datetime.date.today()
tt = datetime.datetime.now().strftime("%Y/%m/%d %a %H:%M:%S")
x = (nn, dd, tt)  # tuple格式
conn.execute(sqlstr, x)

conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("讀取資料庫")
table_name = "table01"
show_data_base_contents(db_filename, table_name)

print("------------------------------------------------------------")  # 60個
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
db_filename = "data/populations.db"
db_filename = "data/singMatch.db"

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

"""
SELECT name FROM table01  WHERE type IN ('table','view') AND name NOT LIKE 'sqlite_%' ORDER BY 1
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("測試 例外 的寫法 資料重複")

db_filename = "tmp_db06_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".sqlite"

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

sqlstr = """
CREATE TABLE IF NOT EXISTS table01(
id   INTEGER PRIMARY KEY,
name VARCHAR UNIQUE
)
"""
cursor = conn.execute(sqlstr)

conn.execute("INSERT INTO table01(name) VALUES (?)", ("David",))
conn.execute("INSERT INTO table01(name) VALUES (?)", ("Lion",))
conn.execute("INSERT INTO table01(name) VALUES (?)", ("Mouse",))

print("顯示所有資料")
sqlstr = "SELECT * FROM table01"  # SELECT * : 取得所有資料
cursor = conn.execute(sqlstr)

table_name = "table01"
show_data_base_contents0(conn, table_name)

try:
    conn.execute("INSERT INTO table01(name) VALUES (?)", ("Lion",))
except sqlite3.IntegrityError:
    print("無法重複輸入相同的資料")

print("顯示所有資料")
sqlstr = "SELECT * FROM table01"  # SELECT * : 取得所有資料
cursor = conn.execute(sqlstr)

table_name = "table01"
show_data_base_contents0(conn, table_name)

conn.close()  # 關閉資料庫連線

# 改成關閉資料庫連線後 再重新顯示資料

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("一次寫入多行的語法 executescript")

db_filename = "tmp_db07_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".sqlite"

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

conn.executescript(
    """
CREATE TABLE IF NOT EXISTS table01(title,author,published);
INSERT INTO table01(title, author, published) VALUES ('TTT1','AAA1', 2001);
INSERT INTO table01(title, author, published) VALUES ('TTT2','AAA2', 2002);
INSERT INTO table01(title, author, published) VALUES ('TTT3','AAA3', 2003);
INSERT INTO table01(title, author, published) VALUES ('TTT4','AAA4', 2004);
INSERT INTO table01(title, author, published) VALUES ('TTT5','AAA5', 2005);
"""
)

print("顯示所有資料")
sqlstr = "SELECT * FROM table01"  # SELECT * : 取得所有資料
cursor = conn.execute(sqlstr)

table_name = "table01"
show_data_base_contents0(conn, table_name)

conn.close()  # 關閉資料庫連線

# 改成關閉資料庫連線後 再重新顯示資料

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("一次寫入多行的語法 executescript")

db_filename = "tmp_db09_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".sqlite"

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

conn.execute("CREATE virtual TABLE IF NOT EXISTS table01 using fts3(name, ingredients)")

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
for row in cursor:  # 不是用fetchall()讀取全部資料
    print(row)

conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("讀取資料庫")
table_name = "table01"
show_data_base_contents(db_filename, table_name)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

db_filename_disk = (
    "tmp_db08_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + "_disk.sqlite"
)

mem_conn = sqlite3.connect(":memory:")  # 建立資料庫連線, 記憶體
cursor = mem_conn.cursor()  # 建立 cursor 物件

disk_conn = sqlite3.connect(db_filename_disk)  # 建立資料庫連線, 磁碟
# xxxxx cursor = disk_conn.cursor()  # 建立 cursor 物件

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

mem_conn.commit()  # 更新

sqlstr = "SELECT * FROM table01"  # SELECT * : 取得所有資料
cursor.execute(sqlstr)

rows = cursor.fetchall()  # 讀取全部資料成元組串列
length = len(rows)
print("共有", length, "筆資料")
for i in range(length):
    print("第" + str(i + 1) + "筆資料 : ", rows[i])

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
show_data_base_contents(db_filename, table_name)

print("讀取資料庫")
table_name = "stocks"
show_data_base_contents(db_filename, table_name)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

try:
    # 嘗試連接到資料庫
    conn = sqlite3.connect(db_filename)  # 建立資料庫連線
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
print("------------------------------------------------------------")  # 60個

print("資料庫 轉 df")

db_filename_animals = "data/animals.sqlite"

print("讀取資料庫")
table_name = "animals"
show_data_base_contents(db_filename_animals, table_name)

conn = sqlite3.connect(db_filename_animals)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

# 查詢資料
cursor = conn.execute("SELECT * FROM animals")
rows = cursor.fetchall()
print(rows)

# cursor.description 包含 欄位資訊
print("cursor.description")
print(cursor.description)

print("資料庫轉df")  # 用資料庫的資料建立 DataFrame
df = pd.DataFrame(rows, columns=[f[0] for f in cursor.description])
print("df")
print(df)

print("讀取資料轉df, 讀取全部資料")
df = pd.read_sql("SELECT * FROM animals", conn)
print("df")
print(df)

conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("csv 轉 sqlite")

csv_filename = "D:/_git/vcs/_4.python/write_read_file/_3.csv/data/animals.csv"
db_filename = (
    "tmp_db10_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + "_csv.sqlite"
)

df = pd.read_csv(csv_filename)
df.columns = df.columns.str.strip()

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
df.to_sql("animals", conn, if_exists="replace")
# df.to_sql("animals", conn)
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

print("讀取資料轉df")

conn = sqlite3.connect(db_filename)  # 建立資料庫連線

print("讀取資料轉df 1, 讀取3筆資料")
df = pd.read_sql("SELECT * FROM animals LIMIT 3", conn)
print(df)

print("讀取資料轉df 2, 讀取3筆資料, 依體重排序(預設升冪)")
df = pd.read_sql("SELECT * FROM animals ORDER BY 體重 LIMIT 3", conn)
print(df)

print("讀取資料轉df 3, 讀取3筆資料")
df = pd.read_sql("SELECT * FROM animals LIMIT 3", conn, index_col="index")
print(df)

print("讀取資料轉df 4")
df = pd.read_sql("SELECT * FROM animals LIMIT 3", conn, index_col=["index", "英文名"])
print(df)

print("讀取資料轉df 5")
df = pd.read_sql_query("SELECT * FROM animals;", conn)
print(df.head())

print("讀取資料轉df 6")
df = pd.read_sql_query("SELECT * FROM animals WHERE 體重>25;", conn)
print(df)

print("讀取資料轉df 7")
df = pd.read_sql_query('SELECT * FROM animals WHERE 中文名="跳跳虎";', conn)
print(df)

conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

print("讀取資料庫")
table_name = "animals"
show_data_base_contents(db_filename, table_name)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("讀取資料庫的所有資料")

db_filename_singMatch = "data/singMatch.db"

print("------------------------------")  # 30個

print("讀取資料庫")
table_name = "參賽者"
print(table_name)
show_data_base_contents(db_filename_singMatch, table_name)

table_name = "音色"
print(table_name)
show_data_base_contents(db_filename_singMatch, table_name)

table_name = "技巧"
print(table_name)
show_data_base_contents(db_filename_singMatch, table_name)

table_name = "儀態"
print(table_name)
show_data_base_contents(db_filename_singMatch, table_name)

print("------------------------------")  # 30個

conn = sqlite3.connect(db_filename_singMatch)  # 建立資料庫連線

print("編號\t姓名\t音色50\t技巧30\t儀態20\t總分")

sqlstr = "SELECT 參賽者.編號, 參賽者.姓名, 音色.音色50, 技巧.技巧30, 儀態.儀態20 FROM 參賽者 INNER JOIN 音色 ON 音色.編號 = 參賽者.編號 INNER JOIN 技巧 ON 技巧.編號 = 參賽者.編號 INNER JOIN 儀態 ON 儀態.編號 = 參賽者.編號"

rows = conn.execute(sqlstr)

for row in rows:
    tot = row[2] + row[3] + row[4]
    print("%d\t%s\t%d\t%d\t%d\t%d" % (row[0], row[1], row[2], row[3], row[4], tot))

conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

# sqlstr = "SELECT * FROM prices WHERE gdate='{}';".format(p[0])

print("------------------------------------------------------------")  # 60個

cursor.execute("DELETE FROM ")
# 一次執行多個指令
cursor.executemany("INSERT INTO test(i) VALUES (?)", [(10,), (20,), (30,)])
cursor.execute("SELECT mysum(i) FROM test")

self.conn.execute("SELECT c2 FROM t2")

# SELECT * : 取得資料 排列 依 gdate 降冪
sqlstr = "SELECT * FROM prices ORDER BY gdate DESC;"

# SELECT * : 取得資料 排列 依 gdate 降冪
sqlstr = "SELECT * FROM prices ORDER BY gdate DESC;"

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

# self.con.execute("insert into test (value) values (?)", ("a\x00b",))# 一項的tuple寫法

# ------------------------------------------------------------

sqlstr = "select {} from {} where {} like '{}.%'".format(
    TXApi.K_DB_TABLE_SN, TXApi.K_DB_TABLE_NAME, TXApi.K_DB_TABLE_SN, symbol
)

sqlstr = "select stockCode from {} where pinyin='{}'".format(
    TXApi.K_DB_TABLE_NAME, pinyin
)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

d = sqlite3.Date(2004, 2, 14)
print(d)

ts = sqlite3.Timestamp(2004, 2, 14, 7, 15, 0)
ts = sqlite3.Timestamp(2004, 2, 14, 7, 15, 0, 500000)
ts = sqlite3.Timestamp(2004, 2, 14, 7, 15, 0, 510241)
print(ts)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
""" 資料整理 ST

sql能否做到部分填滿? 可以

SQL
資料 計畫 問題

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

DB Browser for SQLite
https://sqlitebrowser.org/

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

db : 資料庫 db
table : 表單 資料表(x)

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

建立表單 CREATE TABLE
1. CREATE TABLE table01 # 建立表單table01, 若已存在，則失敗
2. CREATE TABLE IF NOT EXISTS table01 # 建立表單table01, 若已存在，則沿用, 如果尚未建立的話
3. CREATE virtual TABLE table01

print("------------------------------------------------------------")  # 60個
print("SELECT")
print("------------------------------------------------------------")  # 60個

# SELECT
# SELECT 什麼 FROM 表單 陳述式
# SELECT 什麼 FROM 表單 WHERE 條件; (可用邏輯運算子做組合條件)

1.
SELECT * : 取得所有資料
SELECT * FROM table01 # 取得所有資料
SELECT * FROM 表單;   取得所有資料
SELECT 什麼 FROM 表單;
       欄名      表單

2.
SELECT * FROM 表單    WHERE 條件 # 取得所有資料 + 條件
SELECT * FROM table01 WHERE id_num = 5  # 條件
SELECT * FROM customer WHERE birthday < "1990-01-01";
SELECT 什麼 FROM 表單 ORDER BY 什麼 ASC;
       欄名      表單       欄名,排列方法
以升冪排序 ASC(預設)
以降冪排序 DESC

限制讀取個數
SELECT 什麼 FROM 表單 LIMIT 10         #只讀前10筆
SELECT * FROM table01 LIMIT 3, 5        #從第3筆開始讀5筆資料(從0起算)
SELECT * FROM table01 LIMIT 5 OFFSET 3  #讀5筆資料出來, 從第3筆開始讀 (從0起算)

# DELETE 刪除

sqlite指令整理
1. CREATE TABLE
2. INSERT INTO
3. SELECT
4. UPDATE
5.

其他
columns = conn.execute(f"PRAGMA table_info('{table_name}');").fetchall()

新進測試
建立多個表單 要分開寫

# 語法:
INSERT INTO archive_orders SELECT * FROM orders WHERE order_date < "2016-01-01",
DELETE FROM orders WHERE order_date < "2016-01-01",

注意：不要使用%s 將字串插入 SQL 命令，
因為它可能使你的程式容易受到 SQL 注入攻擊（請參閱 SQL 注入 ）。

寫法比較

# INSERT INTO 比較好的寫法 用 tuple

sqlstr = "INSERT INTO table01 (idx, 英文名, 體重) VALUES (?, ?, ?)"
x = (2, 'sheep', 66)  # tuple格式
cursor.execute(sqlstr, x)

# 用.format 比較不好 用 format
sqlstr = ("INSERT INTO table01 (idx, 英文名, 體重) VALUES ({}, '{}', '{}')".format(data[0], data[1], data[2])

相同
.connect = .Connection
conn = sqlite3.connect(db_filename)  # 建立資料庫連線
conn = sqlite3.Connection(db_filename)  # 建立資料庫連線

資料整理 SP"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 修改後 INSERT INTO / xxx / xxxx 之後要  conn.commit()  # 更新  ???
# INSERT INTO
# UPDATE
# DELETE
# DROP
# CREATE TABLE?

# 似乎 INSERT INTO 新增資料 沒有 commit也可以

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
新進測試
測試 SERIAL 測不出效果, 應該像是整數的東西

測試 CHECK
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

sqlstr = "SELECT count(*) FROM news WHERE url='{}';".format(content_url)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 3030
print("------------------------------")  # 30個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 各種fetch
# SELECT + FETCHX

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# CREATE TABLE 各種參數測試

# 只有 CREATE  + INSERT 與 show_data_base_contents

print("一次寫入多行的語法 executescript")

db_filename = "tmp_db11_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".sqlite"

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

# 暫時

"""結論

REAL = FLOAT        小數
INTEGER = INT       整數
TEXT/VARCHAR(n)     字串
NULL
無用 BLOB
"""

"""
CREATE TABLE IF NOT EXISTS table01(
no        INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
id_num    INTEGER PRIMARY KEY NOT NULL,
"""

sqlstr = "INSERT INTO table01 VALUES (?, ?)"
sqlstr = "INSERT INTO table01 VALUES (?, ?, ?, ?)"
# sqlstr = "INSERT INTO table01 VALUES (?, ?, ?)"

id_num, title, author, published = 10, "TTT1", "AAA1", 2001
x = (id_num, title, author, published)  # tuple格式
cursor.execute(sqlstr, x)
conn.commit()  # 更新

conn.close()  # 關閉資料庫連線

print("讀取資料庫")
table_name = "table01"
show_data_base_contents(db_filename, table_name)

# 讀取資料庫大全

"""
讀出一個完整的資料庫大全
1. 一個資料庫內  多個表單 能找出所有表單
2. 依序開啟每個表單 讀出所有資料
搜尋排序.....
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

sqlstr = """
CREATE TABLE IF NOT EXISTS table01(
filename VARCHAR(32),
filesize VARCHAR(32)
)
"""

# conn.rollback()

# 或許rollback是用在操作失敗後要做的動作～～～～～
try:
    cursor.execute(sqlstr1)
    cursor.execute(sqlstr2)
    conn.commit()  # 更新
    print("更新 2 筆記錄...")
except:
    conn.rollback()
    print("更新記錄失敗...")

"CREATE TABLE IF NOT EXISTS table01(idx)"
"vacuum"
"pragma count_changes=1"
"replace into table01(idx) VALUES (6)"
"SELECT idx FROM table01"

"CREATE TABLE IF NOT EXISTS table01(x)"
"INSERT INTO table01(x) VALUES (5)"
"SELECT 1 union SELECT 2 union SELECT 3"

# dddddddddd 可刪除檔案 與 準備刪除的code ST


# dddddddddd 可刪除檔案 與 準備刪除的code SP


# SELECT * : 取得資料 排列 依 gdate 升冪
sqlstr = "SELECT * FROM prices ORDER BY gdate;"

# SELECT * : 取得資料 排列 依 gdate 降冪
sqlstr = "SELECT * FROM prices ORDER BY gdate DESC;"

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

sqlstr = """
CREATE TABLE IF NOT EXISTS 參賽者(
編號 INTEGER UNIQUE NOT NULL,
)
"""

"""
sqlstr = "INSERT INTO 音色 VALUES (?, ?)"
row = (newId, newScore)  # tuple格式
conn.execute(sqlstr, row)

sqlstr = "SELECT * FROM 音色"  # SELECT * : 取得所有資料
data = conn.execute(sqlstr)

selId = 1
sqlstr = "DELETE FROM 參賽者 WHERE 編號 = {0}".format(selId)

delId = 123
sqlstr = "DELETE FROM 音色 WHERE 編號 = {0}".format(delId)

sqlstr = "SELECT * FROM 參賽者"  # SELECT * : 取得所有資料

sqlstr = "SELECT 姓名,電話 FROM 參賽者"

selId = 1
sqlstr = "SELECT * FROM 參賽者 WHERE 編號 = {0}".format(selId)

selName = "a"
sqlstr = 'SELECT * FROM 參賽者 WHERE 姓名 = "{0}"'.format(selName)

newName = input("姓名 :")sqlstr = 'UPDATE 參賽者 \SET 姓名 = "{0}" \WHERE 編號 = {1}'.format(newName, selId)
newSex = input("性別 :")sqlstr = 'UPDATE 參賽者 \SET 性別 = "{0}" \WHERE 編號 = {1}'.format(newSex, selId)
sqlstr = 'UPDATE 參賽者 \SET 電話 = "{0}" \WHERE 編號 = {1}'.format(newTel, selId)
"""

print("INSERT INTO 新增資料 字典方法")
d = {"id": "D0003", "title": "MongoDB資料庫系統", "price": 650}  # 字典
sqlstr = "INSERT INTO Books (id, title, price) VALUES (?, ?, ?)"
x = (d["id"], d["title"], d["price"])  # tuple格式
cursor = conn.execute(sqlstr, x)
print("新增資料行數 :", cursor.rowcount)

# CREATE + PK
# 建立表單 + PRIMARY KEY 序號 自動遞增 不可重複
sqlstr = """
CREATE TABLE IF NOT EXISTS table01(
id     INTEGER PRIMARY KEY AUTOINCREMENT, -- 序號(id)整數自動遞增, 可填可不填
name   TEXT,
gender TEXT
)
"""
print("INSERT INTO 新增資料 3個欄位 指定id")
print("INSERT INTO 新增資料 2個欄位 不指定id 會自動遞增")
sqlstr = "INSERT INTO table01 VALUES (?, ?, ?)"
sqlstr = "INSERT INTO table01 (name, gender) VALUES (?, ?)"

print("讀取資料 SELECT 僅一欄 name")
sqlstr = "SELECT name FROM table01"  # SELECT name : 取得一欄資料

sqlstr = 'SELECT name, gender FROM table01 WHERE gender = "F"'

print("建立暫存檔案的方法")

db_filename_books_old = "data/Books.sqlite"
db_filename_books = (
    "tmp_Books_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".sqlite"
)

if not os.path.exists(db_filename_books):
    shutil.copy(db_filename_books_old, db_filename_books)
    print(db_filename_books)


"""
address CHAR(50),
salary  REAL -- REAL:小數
"""

"""
CHECK  的寫法
birthday    DATE CHECK(birthday > "1900-01-01"),
work_time   DATE CHECK(work_time > birthday),
money       INTEGER CHECK(money > 0) -- 預設錯誤時會顯示

birthday = "2006-03-11"
work_time = "2023-07-11"
money = 2345
"""

# 建立表單 table01 + PRIMARY KEY
sqlstr = """
CREATE TABLE IF NOT EXISTS table01(
-- id SERIAL PRIMARY KEY,   無效
id_num      INTEGER,
name        VARCHAR(50)
)
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


sqlstr = """
CREATE TABLE table01(
aaaa VARCHAR(20),
)
"""

cc = [x for x in range(6)]
print(cc)
