import sqlite3

db_filename = 'test_new.sqlite'
print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename) # 建立資料庫連線

cursor = conn.cursor() # 建立 cursor 物件

print('建立一個資料表')

#Create table table01, num 和 tel
#primary key (num), num不可重複 
sqlstr='create table if not exists table01 ("num" INTEGER PRIMARY KEY NOT NULL ,"tel" TEXT)'
cursor.execute(sqlstr)

'''
#Insert 新增一筆記錄, num不可重複
sqlstr='insert into table01 values(4, "02-1234567")'
cursor.execute(sqlstr)
'''

conn.commit() # 主動更新
conn.close()  # 關閉資料庫連線


print('抓一筆資料')
db_filename = 'test_new.sqlite'
print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename) # 建立資料庫連線

cursor = conn.execute('select * from table01 where num = 1')
row = cursor.fetchone()
if not row==None:
    print("{}\t{}".format(row[0],row[1]))

conn.close()  # 關閉資料庫連線


print('抓全部資料')

db_filename = 'test_new.sqlite'
print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename) # 建立資料庫連線

cursor = conn.execute('select * from table01')
rows = cursor.fetchall()    #讀取全部資料
length = len(rows)

for i in range(length):
    #print(type(rows[i]))
    print('第' + str(i) + '筆資料 : ', end="")
    print(rows[i])
    print("{}\t{}".format(rows[i][0],rows[i][1]))

conn.close()  # 關閉資料庫連線

