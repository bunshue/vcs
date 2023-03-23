import sqlite3

db_filename = 'C:/_git/vcs/_4.cmpp/_python_test/data/test.sqlite'
print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename)

# 更新資料
conn.execute("UPDATE contact SET name='{}' WHERE id={}".format('Ken', 1))
conn.commit() # 更新

conn.close()  # 關閉資料庫連線
