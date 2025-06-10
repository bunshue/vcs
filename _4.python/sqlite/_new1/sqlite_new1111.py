import sqlite3

print("------------------------------------------------------------")  # 60個

conn = sqlite3.connect('tmp_test_aaa.sqlite') # 建立資料庫連線

# 建立一個資料表
sqlstr='''CREATE TABLE "contact" \
("id"  INTEGER PRIMARY KEY NOT NULL,
 "name"  TEXT NOT NULL,
 "tel"  TEXT NOT NULL)
'''
conn.execute(sqlstr)
conn.commit() # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個

# fetchall.py

conn = sqlite3.connect('tmp_test_aaa.sqlite') # 建立資料庫連線
cursor = conn.execute('select * from contact')
rows = cursor.fetchall()
# 顯示原始資料
print(rows)
# 逐筆顯示資料
for row in rows:
    print(row[0],row[1])
conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個

# fetchone.py

conn = sqlite3.connect('data/test_bbb.sqlite') # 建立資料庫連線
cursor = conn.execute('select * from contact')
row = cursor.fetchone()
print(row[0], row[1])

conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個

# sqlite_crud2.py

conn = sqlite3.connect('tmp_test_aaa.sqlite') # 建立資料庫連線
# 定義資料串列
datas = [[1, 'David', '02-123456789'],
        [2, 'Lily', '02-987654321'],]
for data in datas:
    # 新增資料
    conn.execute("INSERT INTO contact (id, name, tel) VALUES \
                 ({}, '{}', '{}')".format(data[0], data[1], data[2]))
conn.commit() # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個

# sqlite_crud3.py

conn = sqlite3.connect('tmp_test_aaa.sqlite') # 建立資料庫連線
# 更新資料
conn.execute("UPDATE contact SET name='{}' WHERE id={}".format('Ken', 1))
conn.commit() # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個

# sqlite_crud4.py

conn = sqlite3.connect('tmp_test_aaa.sqlite') # 建立資料庫連線
# 刪除資料
conn.execute("DELETE FROM contact WHERE id={}".format(1))
conn.commit() # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個

# sqlite_cursor.py

conn = sqlite3.connect('tmp_test_aaa.sqlite') # 建立資料庫連線
cursor = conn.cursor() # 建立 cursor 物件

# 建立一個資料表
sqlstr='''CREATE TABLE IF NOT EXISTS table01 \
("id"  INTEGER PRIMARY KEY NOT NULL,
 "name"  TEXT NOT NULL,
 "tel"  TEXT NOT NULL)
'''
cursor.execute(sqlstr)

# 新增一筆記錄
sqlstr='insert into table01 values(1, "David", "02-1234567")'
cursor.execute(sqlstr)
conn.commit() # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
Topic: 关系型数据库处理
Desc : 
"""
import sqlite3


def db_operation():
    db = sqlite3.connect('tmp_database.db')
    c = db.cursor()
    c.execute('create table portfolio (symbol text, shares integer, price real)')
    db.commit()

    stocks = [
        ('GOOG', 100, 490.1),
        ('AAPL', 50, 545.75),
        ('FB', 150, 7.45),
        ('HPQ', 75, 33.2),
    ]
    c.executemany('insert into portfolio values (?,?,?)', stocks)
    db.commit()

    for row in db.execute('select * from portfolio'):
        print(row)

    min_price = 12
    for row in db.execute('select * from portfolio where price >= ?', (min_price,)):
        print(row)

if __name__ == '__main__':
    db_operation()




print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個




