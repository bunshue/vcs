'''

新進測試

SQLite Autoincrement（自動遞增）

SQLite 的 AUTOINCREMENT 是一個關鍵字，用于表中的字段值自動遞增。
我們可以在創建表時在特定的列名稱上使用 AUTOINCREMENT 關鍵字實現該字段值的自動增加。
關鍵字 AUTOINCREMENT 只能用于整型（INTEGER）字段。

'''

print('------------------------------------------------------------')	#60個
print('準備工作')

import sqlite3
import time

print('新進測試')

db_filename = 'cccc' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.a.qlite'

print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename) # 建立資料庫連線

cursor = conn.cursor() # 建立 cursor 物件

print('建立表單')

cursor.execute("CREATE TABLE table01"
"("
"   ID INTEGER PRIMARY KEY   AUTOINCREMENT,"
"   NAME           TEXT      NOT NULL,"
"   AGE            INT       NOT NULL,"
"   ADDRESS        CHAR(50),"
"   SALARY         REAL"
")")


cursor.execute("INSERT INTO table01 (NAME, AGE, ADDRESS, SALARY) VALUES (?, ?, ?, ?)", ('Paul', 32, 'California', 20000.00))
cursor.execute("INSERT INTO table01 (NAME, AGE, ADDRESS, SALARY) VALUES (?, ?, ?, ?)", ('Allen', 25, 'Texas', 15000.00))
cursor.execute("INSERT INTO table01 (NAME, AGE, ADDRESS, SALARY) VALUES (?, ?, ?, ?)", ('Teddy', 23, 'Norway', 20000.00))
cursor.execute("INSERT INTO table01 (NAME, AGE, ADDRESS, SALARY) VALUES (?, ?, ?, ?)", ('Mark', 25, 'Rich-Mond ', 65000.00))
cursor.execute("INSERT INTO table01 (NAME, AGE, ADDRESS, SALARY) VALUES (?, ?, ?, ?)", ('David', 27, 'Texas', 85000.00))
cursor.execute("INSERT INTO table01 (NAME, AGE, ADDRESS, SALARY) VALUES (?, ?, ?, ?)", ('Kim', 22, 'South-Hall', 45000.00))
cursor.execute("INSERT INTO table01 (NAME, AGE, ADDRESS, SALARY) VALUES (?, ?, ?, ?)", ('James', 24, 'Houston', 10000.00))

conn.commit() # 更新


conn.close()  # 關閉資料庫連線


print("程式執行完畢！")




