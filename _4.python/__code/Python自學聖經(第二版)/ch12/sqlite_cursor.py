import sqlite3
conn = sqlite3.connect('test.sqlite') # 建立資料庫連線
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