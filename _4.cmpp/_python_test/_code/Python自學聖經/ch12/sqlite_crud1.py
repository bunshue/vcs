import sqlite3

db_filename = 'C:/_git/vcs/_4.cmpp/_python_test/data/test.sqlite'
print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename)

# 建立一個資料表
sqlstr='''CREATE TABLE "contact" \
("id"  INTEGER PRIMARY KEY NOT NULL,
 "name"  TEXT NOT NULL,
 "tel"  TEXT NOT NULL)
'''
conn.execute(sqlstr)
conn.commit() # 更新

conn.close()  # 關閉資料庫連線
