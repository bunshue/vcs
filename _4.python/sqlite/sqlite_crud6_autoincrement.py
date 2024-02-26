'''
SQLite Autoincrement（自動遞增）

SQLite 的 AUTOINCREMENT 是一個關鍵字，用于表中的字段值自動遞增。
我們可以在創建表時在特定的列名稱上使用 AUTOINCREMENT 關鍵字實現該字段值的自動增加。
關鍵字 AUTOINCREMENT 只能用于整型（INTEGER）字段。

'''

print('------------------------------------------------------------')	#60個
print('準備工作')

import sqlite3
import time

def show_data_base_contents_all(db_filename, table_name):
    conn = sqlite3.connect(db_filename) # 建立資料庫連線
    #SELECT * : 取得所有資料
    sqlstr = 'SELECT * FROM {};'.format(table_name)#same
    sqlstr = 'SELECT * FROM %s' % table_name
    results = str(conn.execute(sqlstr).fetchall())
    print(results)
    conn.close()  # 關閉資料庫連線

print('------------------------------------------------------------')	#60個

print('測試 序號自動遞增')

db_filename = 'cccc' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.sqlite'

print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename) # 建立資料庫連線

cursor = conn.cursor() # 建立 cursor 物件

print('建立表單')

sqlstr = """
CREATE TABLE IF NOT EXISTS table01 (
    id    INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age  INT NOT NULL,
    address  CHAR(50),
    salary REAL
);
"""
cursor.execute(sqlstr)

cursor.execute("INSERT INTO table01 (name, age, address, salary) VALUES (?, ?, ?, ?)", ('Paul', 32, 'California', 20000.00))
cursor.execute("INSERT INTO table01 (name, age, address, salary) VALUES (?, ?, ?, ?)", ('Allen', 25, 'Texas', 15000.00))
cursor.execute("INSERT INTO table01 (name, age, address, salary) VALUES (?, ?, ?, ?)", ('Teddy', 23, 'Norway', 20000.00))
cursor.execute("INSERT INTO table01 (name, age, address, salary) VALUES (?, ?, ?, ?)", ('Mark', 25, 'Rich-Mond ', 65000.00))
cursor.execute("INSERT INTO table01 (name, age, address, salary) VALUES (?, ?, ?, ?)", ('David', 27, 'Texas', 85000.00))
cursor.execute("INSERT INTO table01 (name, age, address, salary) VALUES (?, ?, ?, ?)", ('Kim', 22, 'South-Hall', 45000.00))
cursor.execute("INSERT INTO table01 (name, age, address, salary) VALUES (?, ?, ?, ?)", ('James', 24, 'Houston', 10000.00))

conn.commit() # 更新
conn.close()  # 關閉資料庫連線

print('------------------------------------------------------------')	#60個

print('讀取資料庫資料, 全部')
#print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename) # 建立資料庫連線
cursor = conn.execute('SELECT * FROM table01')      #SELECT * : 取得所有資料
rows = cursor.fetchall()    #讀取全部資料
print('共有 : ' + str(len(rows)) + " 筆資料")
#print('顯示原始資料')
#print(rows)
print('逐筆顯示資料')
for row in rows:
    print(row[0], row[1], row[2], row[3], row[4])

print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個




