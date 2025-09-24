"""
sqlite基本範例 一個 基本款

增查改刪（英語：CRUD）
增加（CREATE）
查詢（READ, SELECT）
改正（UPDATE）
刪除（DELETE）

* : 全部欄位 cf 指定欄位

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
fetchone()  # 讀取一筆資料	     # 抓一行 tuple
fetchall()  # 讀取全部資料成元組串列 # 抓取剩下的全部 list

fetchmany(size=cursor.arraysize)     # 讀取N筆資料成元組串列
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
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 打卡程式

import sqlite3
import datetime


def show_data_base_contents(db_filename, table_name, reverse=0):
    conn = sqlite3.connect(db_filename)  # 建立資料庫連線
    cursor = conn.cursor()  # 建立 cursor 物件
    # SELECT * : 取得所有資料
    sqlstr = "SELECT * FROM {};".format(table_name)  # same
    sqlstr = "SELECT * FROM %s" % table_name
    cursor.execute(sqlstr)
    # 使用fetchall()
    # print("用fetchall()讀取 全部資料 預設排序(依第1項升冪排序)")
    rows = cursor.fetchall()  # 讀取全部資料成元組串列
    length = len(rows)
    print("共有", length, "筆資料")
    if reverse==1:
        rows = sorted(rows, reverse=True)
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
    conn.close()  # 關閉資料庫連線


def checkin(name, option=0):
    db_filename = "D:/_git/vcs/_4.python/_db/sqlite/data/checkin.sqlite"
    if option == 1:
        print("讀取資料庫")
        table_name = "table01"
        show_data_base_contents(db_filename, table_name, 1)
    else:
        conn = sqlite3.connect(db_filename)  # 建立資料庫連線
        cursor = conn.cursor()  # 建立 cursor 物件
        sqlstr = """
        CREATE TABLE IF NOT EXISTS table01(
        idx INTEGER PRIMARY KEY AUTOINCREMENT, -- 序號(idx)整數自動遞增, 可填可不填
        登入姓名 TEXT NOT NULL,
        登入日期 DATE,
        登入時間 TIMESTAMP
        )
        """
        cursor.execute(sqlstr)
        conn.commit()  # 更新
        sqlstr = "INSERT INTO table01 (登入姓名, 登入日期, 登入時間) VALUES (?, ?, ?)"
        dd = datetime.date.today()
        tt = datetime.datetime.now().strftime("%Y/%m/%d %a %H:%M:%S")
        x = (name, dd, tt)  # tuple格式
        cursor.execute(sqlstr, x)
        conn.commit()  # 更新
        conn.close()  # 關閉資料庫連線


# checkin("mouse", 1)
checkin("mouse")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import shutil
import datetime
import sqlite3


def show_data_base_contents(db_filename, table_name, reverse=0):
    conn = sqlite3.connect(db_filename)  # 建立資料庫連線
    cursor = conn.cursor()  # 建立 cursor 物件
    # SELECT * : 取得所有資料
    sqlstr = "SELECT * FROM {};".format(table_name)  # same
    sqlstr = "SELECT * FROM %s" % table_name
    cursor.execute(sqlstr)
    # 使用fetchall()
    # print("用fetchall()讀取 全部資料 預設排序(依第1項升冪排序)")
    rows = cursor.fetchall()  # 讀取全部資料成元組串列
    length = len(rows)
    print("共有", length, "筆資料")
    if reverse==1:
        rows = sorted(rows, reverse=True)
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
    conn.close()  # 關閉資料庫連線


def show_result():
    rows = cursor.fetchall()  # 讀取全部資料成元組串列
    length = len(rows)
    # print("共有", length, "筆資料")
    print(rows)
    return
    for i in range(length):
        print("第" + str(i + 1) + "筆資料 : ", rows[i])


db_filename_animals_old = "data/animals.sqlite"
db_filename_animals = (
    "tmp_animals_" + time.strftime("%H%M%S", time.localtime()) + ".sqlite"
)

if not os.path.exists(db_filename_animals):
    shutil.copy(db_filename_animals_old, db_filename_animals)
    # print(db_filename_animals)

current_time = datetime.datetime.now().strftime("%Y/%m/%d %a %H:%M:%S")
print("現在時間 :", current_time)

version = sqlite3.sqlite_version_info
print("目前 sqlite3 版本 :", version)

"""
print('製作 DATE/TIMESTAMP 時間戳')
dd = datetime.date.today()
tt = time.time()
tt = datetime.datetime.now()
tt = datetime.datetime.now().strftime("%Y/%m/%d %a %H:%M:%S")
"""
print("------------------------------------------------------------")  # 60個
print("INSERT INTO 新增資料 大全 + CREATE + DROP")
print("------------------------------------------------------------")  # 60個

db_filename = "tmp_db01_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".sqlite"

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

# 建立表單
# PK : PRIMARY KEY 主鍵, 不可重複
# PRIMARY KEY (xxxxx), 指名某項不可重複
# NN : NOT NULL 不得為空
# 序號 自動遞增 不可重複
# UNIQUE 表示不可重複
# CHECK 多了檢查條件
sqlstr = """
CREATE TABLE IF NOT EXISTS table01(
idx INTEGER PRIMARY KEY AUTOINCREMENT, -- 序號(idx)整數自動遞增, 可填可不填
英文名 TEXT NOT NULL,
中文名 TEXT UNIQUE,
體重 INTEGER NOT NULL CHECK(體重 > 0), -- 預設錯誤時會顯示
登入日期 DATE,
登入時間 TIMESTAMP
)
"""
cursor.execute(sqlstr)
conn.commit()  # 更新

print("------------------------------")  # 30個

# INSERT INTO 新增資料, 有些欄位可以不寫, 序號(idx)自動遞增

print("INSERT INTO 新增資料, 有填序號")

sqlstr = "INSERT INTO table01 (idx, 英文名, 中文名, 體重) VALUES (?, ?, ?, ?)"
x = (1, "mouse", "米老鼠", 3)  # tuple格式
cursor.execute(sqlstr, x)
x = (2, "ox", "班尼牛", 48)  # tuple格式
cursor.execute(sqlstr, x)

# 未指明欄位，則必須全寫
sqlstr = "INSERT INTO table01 VALUES (?, ?, ?, ?, ?, ?)"
dd = datetime.date.today()
tt = datetime.datetime.now().strftime("%Y/%m/%d %a %H:%M:%S")
x = (3, "tiger", "", 33, dd, tt)  # tuple格式
cursor.execute(sqlstr, x)

print("------------------------------")  # 30個

print("INSERT INTO 新增資料, 沒有填序號, 系統自動遞增")

# INSERT INTO 用 tuple
sqlstr = "INSERT INTO table01 (英文名, 體重) VALUES (?, ?)"
x = ("rabbit", 8)  # tuple格式
cursor.execute(sqlstr, x)

# INSERT INTO 用 format
sqlstr = "INSERT INTO table01 (英文名, 體重) VALUES ('{}', '{}')".format("dragon", 38)
cursor.execute(sqlstr)

print("------------------------------")  # 30個

print("INSERT INTO 新增資料, 使用字典")

d = {"英文名": "snake", "中文名": "貪吃蛇", "體重": 16}  # 字典
sqlstr = "INSERT INTO table01 (英文名, 中文名, 體重) VALUES (?, ?, ?)"
x = (d["英文名"], d["中文名"], d["體重"])  # tuple格式
cursor.execute(sqlstr, x)
print("新增資料行數 :", cursor.rowcount)

print("------------------------------")  # 30個

print("INSERT INTO 新增資料, 使用DATE/TIMESTAMP 時間戳")

sqlstr = "INSERT INTO table01 (英文名, 體重, 登入日期, 登入時間) VALUES (?, ?, ?, ?)"

nn = "horse"
ww = 31
dd = datetime.date.today()
tt = datetime.datetime.now().strftime("%Y/%m/%d %a %H:%M:%S")
x = (nn, ww, dd, tt)  # tuple格式
cursor.execute(sqlstr, x)

time.sleep(0.3456)  # 過了一段時間

nn = "goat"
ww = 29
dd = datetime.date.today()
tt = datetime.datetime.now().strftime("%Y/%m/%d %a %H:%M:%S")
x = (nn, ww, dd, tt)  # tuple格式
cursor.execute(sqlstr, x)

print("------------------------------")  # 30個

print("INSERT INTO 新增資料, 使用元組串列, 使用executemany")

sqlstr = "INSERT INTO table01 (英文名, 體重, 中文名) VALUES (?, ?, ?)"

# 元組串列
animals = [
    ("monkey", 22, "山道猴"),
    ("chicken", 5, "肯德雞"),
    ("dog", 17, "貴賓狗"),
    ("pig", 42, "佩佩豬"),
]
print("測試 executemany, 一次執行多個指令")
# 一次執行多個指令
cursor.executemany(sqlstr, animals)  # 一次執行多個指令
print("新增資料行數 :", cursor.rowcount)

print("------------------------------")  # 30個
"""
print("測試 例外 的寫法 資料重複")

# 測試 PK, 不能使用相同的PK
try:
    sqlstr = "INSERT INTO table01 (idx, 英文名, 中文名, 體重) VALUES (?, ?, ?, ?)"
    x = (2, "ox", "班尼牛", 48)  # tuple格式
    cursor.execute(sqlstr, x)
except sqlite3.IntegrityError:
    print("無法重複輸入相同的資料1")

# 資料無UNIQUE可以重複
try:
    sqlstr = "INSERT INTO table01 (英文名, 體重) VALUES (?, ?)"
    x = ("tiger", 33)  # tuple格式
    cursor.execute(sqlstr, x)
    print("可以重複輸入相同的資料2")
except sqlite3.IntegrityError:
    print("無法重複輸入相同的資料2")

# 資料有UNIQUE不可以重複
try:
    sqlstr = "INSERT INTO table01 (中文名, 體重) VALUES (?, ?)"
    x = ("班尼牛", 48)  # tuple格式
    cursor.execute(sqlstr, x)
except sqlite3.IntegrityError:
    print("無法重複輸入相同的資料3")
"""
print("------------------------------")  # 30個

# DROP TABLE 刪除表單 如果存在的話
# sqlstr = "DROP TABLE IF EXISTS table01"
# cursor.execute(sqlstr)

# 刪除表單 全部
# cursor.execute("DELETE FROM table01")
# print("刪除資料行數 :", cursor.rowcount)

print("------------------------------")  # 30個

conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

print("讀取資料庫")
table_name = "table01"
show_data_base_contents(db_filename, table_name)

print("------------------------------------------------------------")  # 60個
print("SELECT 取得資料 大全")
print("------------------------------------------------------------")  # 60個

# SELECT * FROM table01           : 取得所有資料
# SELECT * FROM table01 WHERE 條件: 取得所有資料 + 條件, WHERE目標條件式

db_filename = db_filename_animals
print("讀取資料庫")
table_name = "table01"
show_data_base_contents(db_filename, table_name)

print("------------------------------")  # 30個

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

print("------------------------------")  # 30個

print("SELECT * FROM table01, 取得所有資料")

sqlstr = "SELECT * FROM table01"  # SELECT * : 取得所有資料
cursor.execute(sqlstr)

print("先 fetchone() 讀取一筆資料")
row = cursor.fetchone()  # 讀取一筆資料
print(row)

print("再 fetchone() 讀取一筆資料")
row = cursor.fetchone()  # 讀取一筆資料
print(row)

print("再 fetchone() 讀取一筆資料")
row = cursor.fetchone()  # 讀取一筆資料
print(row)

print("再 fetchmany() 讀取3筆資料")
rows = cursor.fetchmany(3)  # 讀取N筆資料成元組串列
print(rows)

print("再 fetchall() 讀取全部資料")
rows = cursor.fetchall()  # 讀取全部資料成元組串列
print(rows)

print("------------------------------")  # 30個

print("SELECT 取得資料 指定欄位 1欄")

sqlstr = "SELECT 英文名 FROM table01"  # SELECT 英文名 : 取得一欄資料
cursor.execute(sqlstr)  # 取得一欄資料
show_result()

print("------------------------------")  # 30個

print("SELECT 取得資料 指定欄位 2欄")

sqlstr = "SELECT 中文名, 體重 FROM table01"  # SELECT 中文名, 體重 : 取得二欄資料
cursor.execute(sqlstr)  # 取得二欄資料
show_result()

print("------------------------------")  # 30個
print("------------------------------")  # 30個

print("SELECT + WHERE 取得資料 + 條件, 名字完全符合")

# name = "貪吃蛇"
# sqlstr = 'SELECT * FROM table01 WHERE 中文名 = "{0}"'.format(name) # same
sqlstr = "SELECT * FROM table01 WHERE 中文名 = ?"
name = ("貪吃蛇",)  # tuple格式, 一項的tuple寫法
cursor.execute(sqlstr, name)
print("中文名=", name[0], "的 :")
show_result()

print("------------------------------")  # 30個

print("SELECT + WHERE 取得資料 + 條件, 體重 > 30")

# min_weight = 30
# sqlstr = "SELECT * FROM table01 WHERE 體重 = {0}".format(min_weight)  # same
sqlstr = "SELECT * FROM table01 WHERE 體重 > ?"
min_weight = (30,)  # tuple格式, 一項的tuple寫法
cursor.execute(sqlstr, min_weight)
show_result()

print("------------------------------")  # 30個

print("SELECT + WHERE 取得資料 + 條件, 名字部分符合")

search_name = "rabbit"
# 無 LIKE, 一定要符合大小寫
sqlstr = "SELECT * FROM table01 WHERE 英文名 = '{}'".format(search_name)
# 有 LIKE, 大小寫皆可
sqlstr = "SELECT * FROM table01 WHERE 英文名 LIKE '{}'".format(search_name)

cursor.execute(sqlstr)
show_result()

# 部分相符
print("指明抓名字有bb的資料")
search_name = ("%bb%",)  # bb在中間 前後要有%, 代表部分, 若無%, 要全部相符
cursor.execute("SELECT * FROM table01 WHERE 英文名 LIKE ?", search_name)
show_result()

# 部分相符
print("指明抓名字有bb的資料")
sqlstr = "SELECT * FROM table01 WHERE 英文名 LIKE '{}'".format("%bb%")
cursor.execute(sqlstr)
show_result()

print("------------------------------")  # 30個

cursor.execute("SELECT * FROM table01 WHERE 中文名 LIKE :name", {"name": "跳跳虎"})
show_result()

print("------------------------------")  # 30個

print("SELECT + WHERE 取得資料 + 條件")

cursor.execute("SELECT * FROM table01 WHERE 英文名 = ?", ("rabbit",))
show_result()

name = "rabbit"
cursor.execute("SELECT * FROM table01 WHERE 英文名 = ?", (name,))
show_result()

print("指明抓一筆資料, 9號")
idx = 9
sqlstr = "SELECT * FROM table01 WHERE idx = " + str(idx)
cursor.execute(sqlstr)

print("idx=9的 :")
show_result()

# 其他寫法
# cursor.execute("SELECT * FROM table01 WHERE idx=?", (str(idx),))
# sqlstr = "SELECT * FROM table01 WHERE idx = {};".format(idx)

print("------------------------------")  # 30個

# 看二欄資料全部
cursor.execute("SELECT 中文名, 體重 FROM table01")  # 取得二欄資料
show_result()

print("------------------------------")  # 30個

# 看二欄資料 + 條件
sqlstr = "SELECT 中文名, 體重 FROM table01 WHERE 體重 >= 30"
cursor.execute(sqlstr)
print("體重>=30的 :")
show_result()

print("------------------------------")  # 30個

print("英文名 有A且有B的")
cursor.execute("SELECT * FROM table01 WHERE 英文名 LIKE '%a%' AND 英文名 LIKE '%b%'")
show_result()

print("英文名 有A或有B的")
cursor.execute("SELECT * FROM table01 WHERE 英文名 LIKE '%a%' OR 英文名 LIKE '%b%'")
show_result()

print("英文名 有A無B的")
cursor.execute("SELECT * FROM table01 WHERE 英文名 LIKE '%a%' AND 英文名 NOT LIKE '%b%'")
show_result()


print("------------------------------")  # 30個
print("------------------------------")  # 30個

print("SELECT + LIMIT 取得資料 + 讀取個數")
# 限制讀取個數
# SELECT 什麼 FROM 表單 LIMIT 5          # SELECT * : 取得所有資料, 限制數量
# SELECT * FROM table01 LIMIT 5          # SELECT * : 取得所有資料, 限制數量
# SELECT * FROM table01 LIMIT 3, 5       # 從第3筆開始讀5筆資料(從0起算)
# SELECT * FROM table01 LIMIT 5 OFFSET 3 # 讀5筆資料出來, 從第3筆開始讀 (從0起算)

offset = 3
limit = 5
print("只讀前5筆")
sqlstr = "SELECT * FROM table01 LIMIT {:d}".format(limit)  # SELECT * : 取得所有資料, 限制數量
cursor.execute(sqlstr)
show_result()

print("從第3筆開始讀5筆資料(從0起算)")
sqlstr = "SELECT * FROM table01 LIMIT {:d}, {:d}".format(offset, limit)
cursor.execute(sqlstr)
show_result()

print("讀5筆資料出來, 從第3筆開始讀 (從0起算)")
sqlstr = "SELECT * FROM table01 LIMIT {:d} OFFSET {:d}".format(limit, offset)
cursor.execute(sqlstr)
show_result()

print("------------------------------")  # 30個
print("------------------------------")  # 30個

print("SELECT + ORDER BY 取得資料 + 排序 升冪 ASC")

print("依 體重 升冪 ASC")
# SELECT * : 取得資料 排列 依 體重 升冪
sqlstr = "SELECT * FROM table01 ORDER BY 體重"
cursor.execute(sqlstr)
show_result()

print("------------------------------")  # 30個

print("SELECT + ORDER BY 取得資料 + 排序 降冪 DESC")
print("依 體重 降冪 DESC")

# SELECT * : 取得資料 排列 依 體重 升冪
# cursor.execute("SELECT * FROM table01 ORDER BY 體重;")  #由小到大, 升冪

# SELECT * : 取得資料 排列 依 體重 降冪
# cursor.execute("SELECT * FROM table01 ORDER BY 體重 DESC;")  # 由小到大 + 反相 = 由大到小, 降冪
sqlstr = "SELECT * FROM table01 ORDER BY 體重 DESC;"
cursor.execute(sqlstr)
show_result()

print("------------------------------")  # 30個

print("用fetchall()讀取 全部資料 依 英文名 排序, 升冪")

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

# SELECT * : 取得資料 排列 依 英文名 升冪
sqlstr = "SELECT * FROM table01 ORDER BY 英文名;"  # 由小到大, 升冪

# SELECT * : 取得資料 排列 依 英文名 降冪
# cursor.execute("SELECT * FROM table01 ORDER BY 英文名 DESC;")  #由小到大 + 反相 = 由大到小, 降冪

cursor.execute(sqlstr)
show_result()

print("------------------------------")  # 30個

conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個
print("UPDATE 更新資料 大全")
print("------------------------------------------------------------")  # 60個

db_filename = db_filename_animals
print("讀取資料庫")
table_name = "table01"
show_data_base_contents(db_filename, table_name)

print("------------------------------")  # 30個

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

print("------------------------------")  # 30個

print("UPDATE 更新資料 修改資料")

# UPDATE 更新資料, 修改表單 table01 內, 修改 中文名 = "虎" 的資料的 體重 內容, 改為 123
cursor.execute("UPDATE table01 SET 體重=? WHERE 中文名 = ?", (123, "虎"))

# UPDATE 更新資料, 修改表單 table01 內, 修改 英文名 = 'snake' 的資料的 中文名 內容, 改為 '小龍'
cursor.execute("UPDATE table01 SET 中文名 = '小龍' WHERE 英文名 = 'snake'")

# UPDATE 更新資料, 修改表單 table01 內, 修改 idx = 6 的資料的 中文名 內容, 改為 '小龍'
cursor.execute("UPDATE table01 SET 中文名 = '小龍' WHERE idx = 6")

# UPDATE 更新資料, 修改表單 table01 內, 修改 idx = 2 的資料的 體重 內容, 改為 53
sqlstr = "UPDATE table01 SET 體重 = '{}' WHERE idx = {}".format(53, 2)
cursor.execute(sqlstr)  # 修改2號的資料, 要先確保已經有2號的資料, 才可以修改

# UPDATE 更新資料, 修改表單 table01 內, 修改 英文名 = 'tiger' 的資料的 中文名 內容, 改為 '大蛇'
sqlstr = "UPDATE table01 SET 中文名 = '{}' WHERE 英文名 = '{}'".format("大蛇", "snake")
cursor.execute(sqlstr)

# UPDATE 更新資料, 修改表單 table01 內, 修改 idx = 1 的資料的 中文名 內容, 改為 "傑利鼠"
sqlstr = "UPDATE table01 SET 中文名 = '傑利鼠' WHERE idx = 1"
cursor.execute(sqlstr)

# UPDATE 更新資料, 修改表單 table01 內, 修改 idx = 8 的資料的 英文名 內容, 改為 sheep
sqlstr = "UPDATE table01 SET 英文名 = '{}' WHERE idx = {}".format("sheep", 8)
cursor.execute(sqlstr)  # 修改8號的資料, 要先確保已經有8號的資料, 才可以修改

idx = 1
newName = "jerry"
newWeight = 5
sqlstr = 'UPDATE table01 SET 英文名 = "{0}" WHERE idx = {1}'.format(newName, idx)
cursor.execute(sqlstr)
sqlstr = "UPDATE table01 SET 體重 = {0} WHERE idx = {1}".format(newWeight, idx)
cursor.execute(sqlstr)

print("------------------------------------------------------------")  # 60個
print("DELETE 刪除資料 大全")
print("------------------------------------------------------------")  # 60個

print("DELETE 刪除資料 + 條件")

idx = 8
cursor.execute("DELETE FROM table01 WHERE idx = ?", (idx,))

idx = 7
sqlstr = "DELETE FROM table01 WHERE idx = {}".format(idx)
# sqlstr = "DELETE FROM table01 WHERE idx = {0}".format(idx) 比較一下
cursor.execute(sqlstr)

print("DELETE 刪除資料 條件 1筆, 刪除11號")
# DELETE 刪除資料 條件 id 為 11 之資料
cursor.execute("DELETE FROM table01 WHERE idx = {}".format(11))

sqlstr = "DELETE FROM table01 WHERE idx = 2"
cursor.execute(sqlstr)

name = "rabbit"
cursor.execute("DELETE FROM table01 WHERE 英文名 = ?", (name,))

name = "貴賓狗"
cursor.execute("DELETE FROM table01 WHERE 中文名 = ?", (name,))

cursor.execute("DELETE FROM table01 WHERE 體重 = 38")

name = "monkey"
sqlstr = "DELETE FROM table01 WHERE 英文名 = '{}'".format(name)
cursor.execute(sqlstr)

print("------------------------------")  # 30個

conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

print("讀取資料庫")
table_name = "table01"
show_data_base_contents(db_filename, table_name)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("一次寫入多行的語法 executescript, 其實就是多行指令寫在一起")

db_filename = "tmp_db03_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".sqlite"

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

conn.executescript(
    """
CREATE TABLE IF NOT EXISTS table01(ename, cname, weight);
INSERT INTO table01(ename, cname, weight) VALUES ('mouse','米老鼠', 3);
INSERT INTO table01(ename, cname, weight) VALUES ('ox','班尼牛', 48);
INSERT INTO table01(ename, cname, weight) VALUES ('tiger','跳跳虎', 33);
"""
)
# 用executescript, 沒有commit也可以

conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("使用記憶體資料庫 轉 磁碟資料庫")

mem_conn = sqlite3.connect(":memory:")  # 建立資料庫連線, 記憶體
cursor = mem_conn.cursor()  # 建立 cursor 物件

sqlstr = """
CREATE TABLE IF NOT EXISTS table01(
name TEXT,
age INT
)
"""
cursor.execute(sqlstr)
print("目前共有修改資料次數 : ", mem_conn.total_changes)

sqlstr = "INSERT INTO table01 VALUES (?, ?)"
x = ("David", 18)  # tuple格式
cursor.execute(sqlstr, x)
print("目前共有修改資料次數 : ", mem_conn.total_changes)

cursor.execute(sqlstr, x)
cursor.execute(sqlstr, x)
cursor.execute(sqlstr, x)
print("目前共有修改資料次數 : ", mem_conn.total_changes)

mem_conn.commit()  # 更新

# 以上把資料存進 記憶體資料庫

# 以下要把 記憶體資料庫 轉 磁碟資料庫

# 建立磁碟資料庫連線
db_filename_disk = (
    "tmp_db05_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + "_disk.sqlite"
)

disk_conn = sqlite3.connect(db_filename_disk)  # 建立資料庫連線, 磁碟

# 使用 backup 命令将内存数据库备份到磁盘数据库。

# 記憶體資料庫 轉 磁碟資料庫
mem_conn.backup(disk_conn)

# backup 覆蓋, attach 附加

"""
# 将磁盘数据库附加到内存数据库中
mem_conn.execute("ATTACH DATABASE db_filename_disk AS disk_db")

# 执行插入命令将数据插入到磁盘数据库中
mem_conn.execute("INSERT INTO disk_db.example_table VALUES (1, 'example')")
"""

mem_conn.close()  # 關閉記憶體資料庫連線
disk_conn.close()  # 關閉磁碟資料庫連線

print("------------------------------")  # 30個

db_filename = db_filename_disk

print("讀取資料庫")
table_name = "table01"
show_data_base_contents(db_filename, table_name)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("取得欄位名稱範例")

db_filename = "D:/_git/vcs/_4.python/_db/sqlite/data/checkin.sqlite"

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
conn.row_factory = sqlite3.Row  # 設定成 Row 物件
sqlstr = "SELECT * FROM table01"
cursor = conn.execute(sqlstr)
rows = cursor.fetchall()  # 讀取全部資料成元組串列
col0 = rows[0].keys()[0]  # 取得第0筆資料的第0個欄位名稱
col1 = rows[0].keys()[1]  # 取得第0筆資料的第1個欄位名稱
col2 = rows[0].keys()[2]  # 取得第0筆資料的第2個欄位名稱
col3 = rows[0].keys()[3]  # 取得第0筆資料的第3個欄位名稱
print("取得col0 :", col0)
print("取得col1 :", col1)
print("取得col2 :", col2)
print("取得col3 :", col3)
print(f"{col1}\t{col2}\t{col3}")
print("----\t  ----\t  ----")
i = 0
for row in rows:
    print(f"{row[1]}\t{row[2]}\t{row[3]}")
    i += 1
    if i > 5:
        break
conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("PRAGMA 編譯指令")

db_filename = "D:/_git/vcs/_4.python/_db/sqlite/data/checkin.sqlite"

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

# 取值
cursor.execute("pragma user_version")  # user_version 用戶自定義版號
rows = cursor.fetchall()  # 讀取全部資料成元組串列
print("用戶自定義版號 :", rows)

cursor.execute("pragma schema_version")  # 當前資料庫模式版本號
rows = cursor.fetchall()  # 讀取全部資料成元組串列
print("當前資料庫模式版本號 :", rows)

cursor.execute("pragma page_size")
rows = cursor.fetchall()  # 讀取全部資料成元組串列
print("Page Size :", rows)

cursor.execute("pragma cache_size")
rows = cursor.fetchall()  # 讀取全部資料成元組串列
print("Cache Size :", rows)

"""設定值
cursor.execute("pragma user_version = 3")# user_version 用戶自定義版號
cursor.execute("pragma schema_version = 7")# 當前資料庫模式版本號
PRAGMA cache_size = 2000;    -- 设置缓存大小为 2000 KB
"""

"""
功能：获取或设置当前数据库的模式版本号。
PRAGMA schema_version;       -- 获取当前模式版本
PRAGMA schema_version = 2;   -- 设置模式版本为 2
"""

print('取得表單資訊 table_info')

table_name = "table01"
cursor.execute('PRAGMA table_info("{0}")'.format(table_name))

table_info = cursor.fetchall()  # 讀取全部資料成元組串列
# print("table_info :", table_info)
length = len(table_info)
print("共有", length, "個欄位")
for i in range(length):
    print("------------------------------")  # 30個
    print("第" + str(i + 1) + "個欄位 : ", table_info[i])
    ii = table_info[i][0]
    nn = table_info[i][1]
    tt = table_info[i][2]
    t1 = table_info[i][3]
    t2 = table_info[i][4]
    t3 = table_info[i][5]
    print("序號 :", ii)
    print("欄名 :", nn)
    print("型態 :", tt)
    print("資料1 :", t1)
    print("資料2 :", t2)
    print("資料3 :", t3)

print("------------------------------")  # 30個

conn.close()  # 關閉資料庫連線

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
    # 編譯指令 PRAGMA
    columns = conn.execute(f"PRAGMA table_info('{table_name}');").fetchall()
    for col in columns:
        column_names.append(col[1])
    return column_names


db_filename = "data/singMatch.db"

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

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
    cursor.execute("SELECT * FROM %s" % table_name)  # SELECT * : 取得所有資料
    rows = cursor.fetchall()  # 讀取全部資料成元組串列
    length = len(rows)
    print("共有", length, "筆資料")
    for i in range(length):
        print("第" + str(i + 1) + "筆資料 : ", rows[i])

conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("讀取資料庫的所有資料")

db_filename_singMatch = "data/singMatch.db"

conn = sqlite3.connect(db_filename_singMatch)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

"""
print("測試UNION ST")
sqlstr = "SELECT * FROM 參賽者"
rows = conn.execute(sqlstr)
for _ in rows:
    print(_)

sqlstr = "SELECT * FROM 音色"
rows = conn.execute(sqlstr)
for _ in rows:
    print(_)

print("測試UNION")

# 直排
# "SELECT 1 UNION SELECT 2 UNION SELECT 3"
sqlstr = "SELECT * FROM 技巧 UNION SELECT * FROM 音色"
rows = conn.execute(sqlstr)
for _ in rows:
    print(_)

conn.close()  # 關閉資料庫連線

print("測試UNION SP")
"""
print("讀取資料庫")
table_name = "參賽者"
print(table_name)
show_data_base_contents(db_filename_singMatch, table_name)
""" 雷同
table_name = "音色"
print(table_name)
show_data_base_contents(db_filename_singMatch, table_name)

table_name = "技巧"
print(table_name)
show_data_base_contents(db_filename_singMatch, table_name)

table_name = "儀態"
print(table_name)
show_data_base_contents(db_filename_singMatch, table_name)
"""
print("------------------------------")  # 30個

conn = sqlite3.connect(db_filename_singMatch)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

print("編號\t姓名\t音色50\t技巧30\t儀態20\t總分")

sqlstr = "SELECT 參賽者.編號, 參賽者.姓名, 音色.音色50, 技巧.技巧30, 儀態.儀態20 FROM 參賽者 INNER JOIN 音色 ON 音色.編號 = 參賽者.編號 INNER JOIN 技巧 ON 技巧.編號 = 參賽者.編號 INNER JOIN 儀態 ON 儀態.編號 = 參賽者.編號"

rows = conn.execute(sqlstr)

for row in rows:
    tot = row[2] + row[3] + row[4]
    print("%d\t%s\t%d\t%d\t%d\t%d" % (row[0], row[1], row[2], row[3], row[4], tot))

conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

db_filename = "data/animals.sqlite"

print("測試讀取不存在的表單觸發異常")

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

print("SQLite FTS3 and FTS4 Extensions 擴展")

db_filename = "tmp_db04_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".sqlite"

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

# ingredient （混合物的）組成部分；（烹調的）原料；（構成）要素，因素

cursor.execute(
    "CREATE VIRTUAL TABLE IF NOT EXISTS table01 USING FTS3(name, ingredients)"
)

sqlstr = "INSERT INTO table01 (name, ingredients) VALUES ('broccoli stew', 'broccoli peppers cheese tomatoes')"
cursor.execute(sqlstr)
sqlstr = "INSERT INTO table01 (name, ingredients) VALUES ('pumpkin stew', 'pumpkin onions garlic celery')"
cursor.execute(sqlstr)
sqlstr = "INSERT INTO table01 (name, ingredients) VALUES ('broccoli pie', 'broccoli cheese onions flour')"
cursor.execute(sqlstr)
sqlstr = "INSERT INTO table01 (name, ingredients) VALUES ('pumpkin pie', 'pumpkin sugar flour butter')"
cursor.execute(sqlstr)

cursor.execute("SELECT rowid, name, ingredients FROM table01 WHERE name MATCH 'pie'")
for row in cursor:  # 不是用fetchall()讀取全部資料
    print(row)

conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("讀取資料庫")
table_name = "table01"
show_data_base_contents(db_filename, table_name)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# """ 資料很多 保留給 fts3 用

# 4個欄位 id / url / title / content
db_filename = "data/applenews.db"

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

sqlstr = "SELECT * FROM news;"

cursor.execute(sqlstr)
rows = cursor.fetchall()  # 讀取全部資料成元組串列
length = len(rows)
print("共有", length, "筆資料")
for i in range(length):
    idx = rows[i][0]
    url = rows[i][1]
    title = rows[i][2]
    content = rows[i][3]
    if i == 0:
        # print("第" + str(i + 1) + "筆資料 : ", rows[i])
        print('id :', idx)
        print('url :', url)
        print('title :', title)
        print('content :', content)
        

""" 把所有的content合併在一起
rows = conn.execute(sqlstr)
cloud_text = ""
for row in rows:
    cloud_text += row[3]
print(cloud_text)
"""
conn.close()  # 關閉資料庫連線

"""
print("讀取資料庫")
table_name = "news"
show_data_base_contents(db_filename, table_name)
"""


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

d = sqlite3.Date(2004, 2, 14)
print(d)

ts = sqlite3.Timestamp(2004, 2, 14, 7, 15, 0)
ts = sqlite3.Timestamp(2004, 2, 14, 7, 15, 0, 500000)
ts = sqlite3.Timestamp(2004, 2, 14, 7, 15, 0, 510241)
print(ts)

# Date
d = sqlite3.Date(2004, 10, 28)
# Time
t = sqlite3.Time(12, 39, 35)
# Timestamp
ts = sqlite3.Timestamp(2004, 10, 28, 12, 39, 35)
# DateFromTicks
d = sqlite3.DateFromTicks(42)
# TimeFromTicks
t = sqlite3.TimeFromTicks(42)
# TimestampFromTicks
ts = sqlite3.TimestampFromTicks(42)
# Binary
b = sqlite3.Binary(b"\0'")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
""" 資料整理 ST

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
# NOT NULL 不得為空
# CHECK(age >= 18) 條件檢查

建立表單 CREATE TABLE
1. CREATE TABLE table01 # 建立表單table01, 若已存在，則失敗
2. CREATE TABLE IF NOT EXISTS table01 # 建立表單table01, 若已存在，則沿用, 如果尚未建立的話

print("------------------------------------------------------------")  # 60個
print("SELECT")
print("------------------------------------------------------------")  # 60個

# SELECT
# SELECT 什麼 FROM 表單 陳述式
# SELECT 什麼 FROM 表單 WHERE 條件; (可用邏輯運算子做組合條件)

1.
SELECT * : 取得所有資料
SELECT * FROM table01 # 取得所有資料
SELECT 什麼 FROM 表單;
       欄名      表單

2.
SELECT * FROM table01 WHERE 條件 # 取得所有資料 + 條件
SELECT * FROM table01 WHERE id_num = 5
SELECT * FROM table01 WHERE birthday < "1990-01-01";
SELECT 什麼 FROM 表單 ORDER BY 什麼 ASC;
       欄名      表單       欄名,排列方法
以升冪排序 ASC(預設)
以降冪排序 DESC

新進測試
建立多個表單 要分開寫

# 語法:
INSERT INTO table01
SELECT * FROM table01 WHERE order_date < "2016-01-01",
DELETE FROM table01   WHERE order_date < "2016-01-01",

注意：不要使用%s 將字串插入 SQL 命令，
因為它可能使你的程式容易受到 SQL 注入攻擊（請參閱 SQL 注入 ）。

寫法比較

相同
.connect = .Connection
conn = sqlite3.connect(db_filename)  # 建立資料庫連線
conn = sqlite3.Connection(db_filename)  # 建立資料庫連線

資料整理 SP"""

"""
新進測試
測試 SERIAL 測不出效果, 應該像是整數的東西

測試 CHECK
"""

# 3030
print("------------------------------")  # 30個

# CREATE TABLE 各種參數測試

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

"""
# 讀取資料庫大全
讀出一個完整的資料庫大全
1. 一個資料庫內  多個表單 能找出所有表單
2. 依序開啟每個表單 讀出所有資料
搜尋排序.....
"""
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

"CREATE TABLE IF NOT EXISTS table01(x)"

sqlstr = """
CREATE TABLE IF NOT EXISTS 參賽者(
編號 INTEGER UNIQUE NOT NULL,
)
"""

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

sqlstr = """
CREATE TABLE IF NOT EXISTS table01(
id   INTEGER PRIMARY KEY,
name VARCHAR UNIQUE
)
"""

print("------------------------------------------------------------")  # 60個

sqlstr = """
CREATE TABLE table01(
aaaa VARCHAR(20),
)
"""

cc = [x for x in range(6)]
print(cc)


print("讀取一筆資料")
row = cursor.fetchone()  # 讀取一筆資料
print("a讀取一筆資料", row)

while row:
    print("讀取一筆資料")
    row = cursor.fetchone()  # 讀取一筆資料
    print("b讀取一筆資料", row)


""" 一次抓5筆資料 抓到完
dataclip = []
rows = cursor.fetchmany(5)# 讀取N筆資料成元組串列
print(rows)
while rows:
    dataclip.extend(rows)
    rows = cursor.fetchmany(5)# 讀取N筆資料成元組串列
    #print(rows) many
"""

# 字串替代法:
fullstring = "I am {} and {} and {}".format("aaaa", "bbbb", "cccc")
print(fullstring)

name = "david"
save_time = xxxxxx
sqlstr = f'INSERT INTO table01 VALUES ("{name}", "{save_time}")'
cursor.execute(sqlstr)
