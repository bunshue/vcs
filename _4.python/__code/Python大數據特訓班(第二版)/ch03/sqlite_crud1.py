import sqlite3
conn = sqlite3.connect('school.db') # 建立資料庫連線
# 建立一個資料表
sqlstr='''CREATE TABLE IF NOT EXISTS scores \
("id"  INTEGER PRIMARY KEY NOT NULL,
 "name"  TEXT NOT NULL,
 "chinese"  INTEGER NOT NULL,
 "english"  INTEGER NOT NULL,
 "math"  INTEGER NOT NULL
 )
'''
conn.execute(sqlstr)
conn.commit() # 更新
conn.close()  # 關閉資料庫連線