import sqlite3
conn = sqlite3.connect('test.sqlite') # 建立資料庫連線

# 建立一個資料表
sqlstr='''CREATE TABLE "contact" \
("id"  INTEGER PRIMARY KEY NOT NULL,
 "name"  TEXT NOT NULL,
 "tel"  TEXT NOT NULL)
'''
conn.execute(sqlstr)
conn.commit() # 更新
conn.close()  # 關閉資料庫連線