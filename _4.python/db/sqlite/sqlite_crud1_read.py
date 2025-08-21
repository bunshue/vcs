"""
讀取資料庫大全
"""
"""
Filename :

讀出一個完整的資料庫大全

1. 一個資料庫內  多個表單 能找出所有表單
2. 依序開啟每個表單 讀出所有資料


搜尋排序.....




"""

import sys
import sqlite3

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
db_filename = "C:/_git/vcs/_1.data/______test_files1/_db/gasoline.sqlite"
db_filename = "data/example.db"
db_filename = "data/myInfo.db"
db_filename = "data/myInfo2.db"
db_filename = "data/populations.db"
db_filename = "data/singMatch.db"

print("建立資料庫連線, 資料庫 :" + db_filename)
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
    rows = cursor.fetchall()
    print("內容 :", rows)

conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


"""
各種讀取資料庫範例

"""

import sys
import sqlite3

print("------------------------------------------------------------")  # 60個

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

print("------------------------------------------------------------")  # 60個

print("讀取資料庫範例")

db_filename = "C:/_git/vcs/_1.data/______test_files1/_db/DataBasePM25.sqlite"

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

print("------------------------------------------------------------")  # 60個

print("從資料庫讀出一筆資料")

db_filename = "C:/_git/vcs/_1.data/______test_files1/_db/python01.sqlite"

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.execute("SELECT * FROM table01 WHERE num = 1")
row = cursor.fetchone()

if not row == None:
    print("{}\t{}".format(row[0], row[1]))

conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個

print("從資料庫讀出全部資料")

db_filename = "C:/_git/vcs/_1.data/______test_files1/_db/python01.sqlite"

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.execute("SELECT * FROM table01")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個

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
