#我的sql規劃

'''
table01
        string          int             string
	filename	filesize	description
第1筆 : filename1       123             'aaaa'
第2筆 : filename2       456             'bbbb'
第3筆 : filename3       789             'cccc'

updatetime
        string
	updatetime
第1筆 : 2023-05-29 13:57:39.206064
第2筆 : 2023-05-29 13:57:43.085771
第3筆 : 2023-05-29 13:57:48.938803
'''

filename1 = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
filename2 = 'C:/_git/vcs/_1.data/______test_files1/file2.txt'
filename3 = 'C:/_git/vcs/_1.data/______test_files1/bear.jpg'

import os
import time
import datetime
import sqlite3

db_filename = 'C:/_git/vcs/_1.data/______test_files2/my_db.sqlite';

#print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename) # 建立資料庫連線

cursor = conn.cursor() # 建立 cursor 物件

print('建立一個資料表')

#若資料庫已存在 則不用重新建立

sqlstr = 'create table if not exists table01 ("filename" TEXT NOT NULL, "filesize"  INT, "description"  TEXT NOT NULL)'

cursor.execute(sqlstr)
conn.commit() # 更新

print('新增資料 3 筆')
#Insert
filename = filename1
filesize = os.path.getsize(filename1)
description = 'aaaa'
sqlstr = "insert into table01 values('{}','{}','{}');".format(filename, filesize, description)
cursor.execute(sqlstr)

filename = filename2
filesize = os.path.getsize(filename2)
description = 'bbbb'
sqlstr = "insert into table01 values('{}','{}','{}');".format(filename, filesize, description)
cursor.execute(sqlstr)

filename = filename3
filesize = os.path.getsize(filename3)
description = 'cccc'
sqlstr = "insert into table01 values('{}','{}','{}');".format(filename, filesize, description)
cursor.execute(sqlstr)

conn.commit() # 更新
conn.close()  # 關閉資料庫連線

print('建立資料庫連線, 寫入時間戳記')

#print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename) # 建立資料庫連線
cursor = conn.cursor() # 建立 cursor 物件
print('建立一個資料表')
#若資料庫已存在 則不用重新建立
sqlstr = 'create table if not exists updatetime ("updatetime" TEXT NOT NULL)'
cursor.execute(sqlstr)
conn.commit() # 更新

print('新增資料 1 筆')
#Insert
current_time = datetime.datetime.now() # 取得現在時間
sqlstr = "insert into updatetime values('{}');".format(current_time)
cursor.execute(sqlstr)

conn.commit() # 更新
conn.close()  # 關閉資料庫連線

print('不是用fetchall()讀取 全部資料')
#print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename) # 建立資料庫連線
cursor = conn.execute('select * from table01')
i = 0
for row in cursor:
    #print(type(rows[i]))
    print('第' + str(i + 1) + '筆資料 : ', end = "")
    #print(rows[i])
    print("{}\t{}\t{}".format(row[0], row[1], row[2]))
    i = i + 1
conn.close()  # 關閉資料庫連線

print('用fetchall()讀取 全部資料 預設排序(依第1項升冪排序)')
#print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename) # 建立資料庫連線
cursor = conn.execute('select * from table01')
rows = cursor.fetchall()    #讀取全部資料
length = len(rows)
print('共有', length, '筆資料')
for i in range(length):
    #print(type(rows[i]))
    print('第' + str(i + 1) + '筆資料 : ', end = "")
    #print(rows[i])
    print("{}\t{}\t{}".format(rows[i][0], rows[i][1], rows[i][2]))
conn.close()  # 關閉資料庫連線

print('用fetchall()讀取 全部資料 依 filesize 排序, 降冪')
#print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename) # 建立資料庫連線
#cursor = conn.execute('select * from table01 order by filesize;')#由小到大, 升冪
cursor = conn.execute('select * from table01 order by filesize desc;')#由小到大 + 反相 = 由大到小, 降冪
rows = cursor.fetchall()    #讀取全部資料
length = len(rows)
print('共有', length, '筆資料')
for i in range(length):
    #print(type(rows[i]))
    print('第' + str(i + 1) + '筆資料 : ', end = "")
    #print(rows[i])
    print("{}\t{}\t{}".format(rows[i][0], rows[i][1], rows[i][2]))
conn.close()  # 關閉資料庫連線


print('不是用fetchall()讀取 全部資料')
#print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename) # 建立資料庫連線
cursor = conn.execute('select * from updatetime')
i = 0
for row in cursor:
    #print(type(rows[i]))
    print('第' + str(i + 1) + '筆資料 : ', end = "")
    #print(rows[i])
    print("{}".format(row[0]))
    i = i + 1
conn.close()  # 關閉資料庫連線



#----------------------------------------------------------------


