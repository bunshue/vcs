"""
各種讀取資料庫範例
"""

# ----------------------------------------------------------------

print("讀取資料庫範例")

import sqlite3

db_filename = "C:/_git/vcs/_1.data/______test_files1/_db/gasoline.sqlite"


def disp_menu():
    print("中油歷年油價查詢系統")
    print("------------")
    print("1.顯示歷年油價資訊")
    print("2.最近10週油價資訊")
    print("0.結束")
    print("------------")


def disp_alldata():
    print("建立資料庫連線, 資料庫 : " + db_filename)
    conn = sqlite3.connect(db_filename)  # 建立資料庫連線

    print("要事先能知道表單的名稱 prices 與 各欄位的名稱 gdate")

    cursor = conn.execute("SELECT * FROM prices ORDER BY gdate DESC;")

    # 不是用fetchall()讀取全部資料
    n = 0
    for row in cursor:
        print("日期：{}，92無鉛：{}，95無鉛：{}，98無鉛：{}".format(row[0], row[1], row[2], row[3]))
        n = n + 1
        """
        if n == 20:  # 一次顯示20筆
            x = input("請按Enter鍵繼續...(Q:回主選單)")
            if x == 'Q' or x == 'q': break
            n = 0
        """
    conn.close()  # 關閉資料庫連線


def disp_10data_a():
    print("建立資料庫連線, 資料庫 : " + db_filename)
    conn = sqlite3.connect(db_filename)  # 建立資料庫連線

    print("要事先能知道表單的名稱 prices 與 各欄位的名稱 gdate")

    cursor = conn.execute("SELECT * FROM prices ORDER BY gdate DESC;")

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
    print("建立資料庫連線, 資料庫 : " + db_filename)
    conn = sqlite3.connect(db_filename)  # 建立資料庫連線

    print("要事先能知道表單的名稱 prices 與 各欄位的名稱 gdate")

    cursor = conn.execute("SELECT * FROM prices ORDER BY gdate DESC;")
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
    raw = cursor.fetchall()
    # print(raw)
    dataclip = [(str(i[0]), str(i[1]), str(i[2]), str(i[3])) for i in raw]
    print(dataclip)

    conn.close()  # 關閉資料庫連線


print("中油歷年油價查詢系統")

print("1.顯示歷年油價資訊")
# disp_alldata()
print("2.最近10週油價資訊")
disp_10data_b()

# ----------------------------------------------------------------

print("讀取資料庫範例")

db_filename = "C:/_git/vcs/_1.data/______test_files1/_db/DataBasePM25.sqlite"

import sqlite3

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

"""
# 建立一個資料表
sqlstr= 'CREATE TABLE IF NOT EXISTS TablePM25 ("no" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE ,"SiteName" TEXT NOT NULL ,"PM25" INTEGER)'
cursor.execute(sqlstr)
"""

print("從資料庫讀取資料...")
cursor = conn.execute("SELECT * FROM TablePM25")
rows = cursor.fetchall()

i = 0
for row in rows:
    print("站名:{}   PM2.5={}".format(row[1], row[2]))
    i += 1
    if i > 10:
        break

conn.close()  # 關閉資料庫連線

# ----------------------------------------------------------------

print("從資料庫讀出一筆資料")

db_filename = "C:/_git/vcs/_1.data/______test_files1/_db/python01.sqlite"

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.execute("SELECT * FROM table01 WHERE num = 1")
row = cursor.fetchone()
if not row == None:
    print("{}\t{}".format(row[0], row[1]))

conn.close()  # 關閉資料庫連線

# ----------------------------------------------------------------

print("從資料庫讀出全部資料")

db_filename = "C:/_git/vcs/_1.data/______test_files1/_db/python01.sqlite"

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.execute("SELECT * FROM table01")
rows = cursor.fetchall()
print(rows)
for row in rows:
    print("{}\t{}".format(row[0], row[1]))

conn.close()  # 關閉資料庫連線

# ----------------------------------------------------------------

print("從資料庫讀出全部資料")

db_filename = "C:/_git/vcs/_1.data/______test_files1/_db/headlines.sqlite"

conn = sqlite3.connect(db_filename)  # 建立資料庫連線

print("讀取全部, 只顯示前10筆")
cursor = conn.execute("SELECT * FROM titles")
rows = cursor.fetchall()
# print(rows)
r = 0
for row in rows:
    print("{}\t{}\t{}".format(row[0], row[1], row[2]))
    r += 1
    if r == 10:
        break

print("只讀前10筆")
cursor = conn.execute("SELECT * FROM titles LIMIT 10")
rows = cursor.fetchall()
print(rows)

print("從第3筆開始讀5筆資料(從0起算)")
cursor = conn.execute("SELECT * FROM titles LIMIT 3, 5")
rows = cursor.fetchall()
print(rows)

print("讀5筆資料出來, 從第3筆開始讀 (從0起算)")
cursor = conn.execute("SELECT * FROM titles LIMIT 5 OFFSET 3")
rows = cursor.fetchall()
print(rows)

conn.close()  # 關閉資料庫連線

# ----------------------------------------------------------------
