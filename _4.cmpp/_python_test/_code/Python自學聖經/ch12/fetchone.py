import sqlite3

db_filename = 'C:/_git/vcs/_4.cmpp/_python_test/data/test.sqlite'
print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename)

cursor = conn.execute('select * from contact')
row = cursor.fetchone()
print(row[0], row[1])

conn.close()  # 關閉資料庫連線
