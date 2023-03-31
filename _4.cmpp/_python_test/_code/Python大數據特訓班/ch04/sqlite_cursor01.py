import sqlite3
conn = sqlite3.connect('test.sqlite') # 建立資料庫連線
cursor = conn.cursor() # 建立 cursor 物件

# 建立一個資料表
sqlstr='CREATE TABLE IF NOT EXISTS table01 \
("num" INTEGER PRIMARY KEY NOT NULL ,"tel" TEXT)'
cursor.execute(sqlstr)

# 新增一筆記錄
sqlstr='insert into table01 values(1,"02-1234567")'
cursor.execute(sqlstr)

conn.commit() # 主動更新
conn.close()  # 關閉資料庫連線


#抓一筆資料


import sqlite3
conn = sqlite3.connect('test.sqlite') # 建立資料庫連線
cursor = conn.execute('select * from table01 where num=1')
row = cursor.fetchone()
if not row==None:
    print("{}\t{}".format(row[0],row[1]))

conn.close()  # 關閉資料庫連線



#抓全部資料

import sqlite3
conn = sqlite3.connect('test.sqlite') # 建立資料庫連線
cursor = conn.execute('select * from table01')
rows = cursor.fetchall()
print(rows)
for row in rows:
    print("{}\t{}".format(row[0],row[1]))

conn.close()  # 關閉資料庫連線

