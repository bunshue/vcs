import sqlite3
conn = sqlite3.connect('school.db') # 建立資料庫連線
cursor = conn.execute('select * from scores')
row = cursor.fetchone()
print(row[0], row[1])
conn.close()  # 關閉資料庫連線