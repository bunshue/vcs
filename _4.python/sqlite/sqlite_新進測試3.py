import sys
import sqlite3

print("------------------------------------------------------------")  # 60個
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
print("------------------------------------------------------------")  # 60個

# sqlite_cursor.py
import sqlite3

conn = sqlite3.connect("tmp_school.db")  # 建立資料庫連線
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
print("------------------------------------------------------------")  # 60個

# sqlite_crud1.py
import sqlite3

conn = sqlite3.connect("tmp_school.db")  # 建立資料庫連線
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

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# sqlite_crud2.py
import sqlite3

conn = sqlite3.connect("data/school222.db")  # 建立資料庫連線
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
print("------------------------------------------------------------")  # 60個

# sqlite_crud3.py
import sqlite3

conn = sqlite3.connect("tmp_school.db")  # 建立資料庫連線
# 更新資料
conn.execute("UPDATE scores SET name='{}' WHERE id={}".format("林胖虎", 1))
conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# sqlite_crud4.py
import sqlite3

conn = sqlite3.connect("tmp_school.db")  # 建立資料庫連線
# 刪除資料
conn.execute("DELETE FROM scores WHERE id={}".format(1))
conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

# fetchall.py
import sqlite3

conn = sqlite3.connect("tmp_school.db")  # 建立資料庫連線
cursor = conn.execute("select * from scores")
rows = cursor.fetchall()
# 顯示原始資料
print(rows)
# 逐筆顯示資料
for row in rows:
    print(row[0], row[1])
conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# fetchone.py
import sqlite3

conn = sqlite3.connect("tmp_school.db")  # 建立資料庫連線
cursor = conn.execute("select * from scores")
row = cursor.fetchone()
print(row[0], row[1])
conn.close()  # 關閉資料庫連線


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import sqlite3
import datetime

def db_save(db, name):
    connect = sqlite3.connect(db)  # 與資料庫連線
    # 新建 mytable 資料表  (如果尚未建立的話)
    sql = 'CREATE TABLE IF NOT EXISTS mytable ("姓名" TEXT, "打卡時間" TEXT)'
    connect.execute(sql)  # 執行 SQL 語法
    # 取得現在時間
    save_time = datetime.datetime.now().strftime("%Y-%m-%d %H.%M.%S")
    # 新增一筆資料的 SQL 語法
    sql = f'insert into mytable values("{name}", "{save_time}")'
    connect.execute(sql)  # 執行 SQL 語法
    connect.commit()  # 更新資料庫
    connect.close()  # 關閉資料庫
    print("儲存成功")


db_save("tmp_mydatabase.sqlite", "丹丹")


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


def db_check(db):
    try:
        connect = sqlite3.connect(db)  # 與資料庫連線
        sql = "select * from mytable"  # 選取資料表中所有資料的 SQL 語法
        cursor = connect.execute(sql)  # 執行 SQL 語法得到 cursor 物件
        dataset = cursor.fetchall()  # 取得所有資料
        print("姓名\t打卡時間")
        print("----\t  ----")
        for data in dataset:
            print(f"{data[0]}\t{data[1]}")
    except:
        print("讀取資料庫錯誤")
    connect.close()


db_check("tmp_mydatabase.sqlite")

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





import datetime
now = datetime.datetime.now()
time = now.strftime("%Y-%m-%d %H:%M:%S")
cur.execute("INSERT INTO message VALUES(?,?,?,?,?)", (name, mail, site, content, time))


import sqlite3  # 匯入sqlite3模組

con = sqlite3.connect("message")  # 連線到資料庫
cur = con.cursor()  # 獲得資料庫游標, 'GBK')
cur.execute("select * from message")  # 執行SQL敘述
results = cur.fetchall()  # 獲得資料

for result in results:
    print(result)

cur.close()  # 關閉游標
con.close()  # 關閉資料庫連線



print("------------------------------------------------------------")  # 60個



import sqlite3


def sqlite_insert(title, username, email, message_text):
    connect = sqlite3.connect('database.sqlite')
    connect.execute("INSERT INTO message_board (title, username, email, message_text, date) VALUES (?, ?, ?, ?, DATETIME('now'))",
                    (title, username, email, message_text))
    connect.commit()
    connect.close()


def sqlite_read():
    conn = sqlite3.connect('database.sqlite')
    creat_sql = 'create table if not exists message_board ("title" TEXT, "username" TEXT, "email" TEXT, "message_text" TEXT, "date" TEXT)'
    conn.execute(creat_sql)
    read_sql = 'select * from message_board'
    read_data = conn.execute(read_sql)
    dataset = read_data.fetchall()
    conn.close()
    return list(dataset)



print("------------------------------------------------------------")  # 60個
