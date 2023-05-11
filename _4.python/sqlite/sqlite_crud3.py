import time
import sqlite3

db_filename = 'C:/_git/vcs/_1.data/______test_files2/db_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.sqlite';

#print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename) # 建立資料庫連線
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

#----------------------------------------------------------------
print('從資料庫讀出一筆資料')

db_filename = 'C:/_git/vcs/_1.data/______test_files1/_db/python01.sqlite';

conn = sqlite3.connect(db_filename) # 建立資料庫連線
cursor = conn.execute('select * from table01 where num=1')
row = cursor.fetchone()
if not row==None:
    print("{}\t{}".format(row[0],row[1]))

conn.close()  # 關閉資料庫連線

#----------------------------------------------------------------

print('從資料庫讀出全部資料')

db_filename = 'C:/_git/vcs/_1.data/______test_files1/_db/python01.sqlite';

conn = sqlite3.connect(db_filename) # 建立資料庫連線
cursor = conn.execute('select * from table01')
rows = cursor.fetchall()
print(rows)
for row in rows:
    print("{}\t{}".format(row[0],row[1]))

conn.close()  # 關閉資料庫連線



#----------------------------------------------------------------




#----------------------------------------------------------------

