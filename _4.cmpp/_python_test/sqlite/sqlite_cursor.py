import sqlite3

db_filename = 'C:/_git/vcs/_4.cmpp/_python_test/data/test.sqlite'
print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename) # 建立資料庫連線

cursor = conn.cursor() # 建立 cursor 物件

print('建立一個資料表')

#Create table table01, id 和 name 和 tel
sqlstr='create table if not exists table01 ("id"  INTEGER PRIMARY KEY NOT NULL, "name"  TEXT NOT NULL, "tel"  TEXT NOT NULL)'
cursor.execute(sqlstr)

#Insert 新增一筆記錄
#sqlstr='insert into table01 values(1, "David", "02-1234567")'
#cursor.execute(sqlstr)

conn.commit() # 主動更新
conn.close()  # 關閉資料庫連線
