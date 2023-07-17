import sqlite3
conn = sqlite3.connect('school.db') # 建立資料庫連線
cursor = conn.cursor() # 建立 cursor 物件
# 建立一個資料表
sqlstr='''CREATE TABLE IF NOT EXISTS scores \
("id"  INTEGER PRIMARY KEY NOT NULL,
 "name"  TEXT NOT NULL,
 "chinese"  INTEGER NOT NULL,
 "english"  INTEGER NOT NULL,
 "math"  INTEGER NOT NULL
 )
'''
cursor.execute(sqlstr)

# 新增記錄
cursor.execute('insert into scores values(1, "葉大雄", 65, 62, 40)')
cursor.execute('insert into scores values(2, "陳靜香", 85, 90, 87)')
cursor.execute('insert into scores values(3, "王聰明", 92, 90, 95)')
conn.commit() # 更新
conn.close()  # 關閉資料庫連線