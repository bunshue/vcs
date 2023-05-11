import sqlite3
conn = sqlite3.connect('test.sqlite') # 建立資料庫連線
cursor = conn.execute('select * from table01')
rows = cursor.fetchall()
print(rows)
for row in rows:
    print("{}\t{}".format(row[0],row[1]))

conn.close()  # 關閉資料庫連