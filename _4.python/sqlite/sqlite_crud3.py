#我的sql規劃

'''
原始資料 9 筆
	id	name	money
第1筆 : 5	Apple	333
第2筆 : 1	Banana	777
第3筆 : 4	Cat	444    (此筆資料多餘, 應刪除)

'''

import time
import sqlite3

db_filename = 'C:/_git/vcs/_1.data/______test_files1/_db/my_db.sqlite';

#print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename) # 建立資料庫連線

cursor = conn.cursor() # 建立 cursor 物件

print('建立一個資料表')

#若資料庫已存在 則不用重新建立

sqlstr = 'create table if not exists table01 ("id_num" INTEGER, "name"  TEXT NOT NULL, "money"  TEXT NOT NULL)'

cursor.execute(sqlstr)
conn.commit() # 更新

print('新增資料 2 筆')
#Insert
number = 7
name = 'Happy'
money = 999
sqlstr = "insert into table01 values({},'{}','{}');".format(number, name, money)
cursor.execute(sqlstr)
number = 6
name = 'India'
money = 555
sqlstr = "insert into table01 values({},'{}','{}');".format(number, name, money)
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
    print('第' + str(i + 1) + '筆資料 : ', end="")
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
    print('第' + str(i + 1) + '筆資料 : ', end="")
    #print(rows[i])
    print("{}\t{}\t{}".format(rows[i][0], rows[i][1], rows[i][2]))
conn.close()  # 關閉資料庫連線

print('用fetchall()讀取 全部資料 依 name 排序, 升冪')
#print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename) # 建立資料庫連線
cursor = conn.execute('select * from table01 order by name;')#由小到大, 升冪
#cursor = conn.execute('select * from table01 order by name desc;')#由小到大 + 反相 = 由大到小, 降冪
rows = cursor.fetchall()    #讀取全部資料
length = len(rows)
print('共有', length, '筆資料')
for i in range(length):
    #print(type(rows[i]))
    print('第' + str(i + 1) + '筆資料 : ', end="")
    #print(rows[i])
    print("{}\t{}\t{}".format(rows[i][0], rows[i][1], rows[i][2]))
conn.close()  # 關閉資料庫連線

print('用fetchall()讀取 全部資料 依 money 排序, 降冪')
#print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename) # 建立資料庫連線
#cursor = conn.execute('select * from table01 order by money;')#由小到大, 升冪
cursor = conn.execute('select * from table01 order by money desc;')#由小到大 + 反相 = 由大到小, 降冪
rows = cursor.fetchall()    #讀取全部資料
length = len(rows)
print('共有', length, '筆資料')
for i in range(length):
    #print(type(rows[i]))
    print('第' + str(i + 1) + '筆資料 : ', end = "")
    #print(rows[i])
    print("{}\t{}\t{}".format(rows[i][0], rows[i][1], rows[i][2]))
conn.close()  # 關閉資料庫連線


#----------------------------------------------------------------


