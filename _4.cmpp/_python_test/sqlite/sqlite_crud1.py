#同一個資料庫內 可以放多個table table名稱不同即可

'''
增刪查改（英語：CRUD），全稱
增加（Create，意為「建立」）、
刪除（Delete）、
查詢（Read，意為「讀取」）、
改正（Update，意為「更新」），
在電腦程式語言中是一連串常見的動作行為，
'''

'''
原始資料 9 筆
	id	name	money
第1筆 : 5	Apple	333
第2筆 : 1	Banana	777
第3筆 : 4	Cat	444    (此筆資料多餘, 應刪除)

第4筆 : 9	Dog	888
第5筆 : 2	Dog	888    (此筆資料錯誤, 應為Eagle 111)

第6筆 : 8	Frog	666    (詢問是否刪除此筆資料)
第7筆 : 3	Giraffe	222

第8筆 : 7	Happy	999
第9筆 : 6	India	555

修改2號的name

刪除4號

詢問是否刪除8號資料

各種排序顯示資料庫內容
'''

import time
import sqlite3

db_filename = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/db_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.sqlite';

#print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename) # 建立資料庫連線

cursor = conn.cursor() # 建立 cursor 物件

print('建立一個資料表')
''' 其他寫法
#cursor.execute("create table table01 ( id_num char(5), subjectId char(4) not null, " +
#               "animalNumber integer, title varchar(50) not null, primary key (id_num))")   #id_num不可重複

#id_num可重複
#cursor.execute("create table table01 ( id_num char(5), subjectId char(4) not null, " +
#               "animalNumber integer, title varchar(50) not null)")

#id_num可重複, 若資料庫已存在 則不用重新建立
cursor.execute("create table if not exists table01 ( id_num char(5), subjectId char(4) not null, " +
               "animalNumber integer, title varchar(50) not null)")
'''
#Create 建立
#Create table table01, id_num(int) 和 name(text) 和 money(int),
#primary key (id_num), id_num不可重複
sqlstr='create table if not exists table01 ("id_num" INTEGER PRIMARY KEY NOT NULL, "name"  TEXT NOT NULL, "money"  TEXT NOT NULL)'
#sqlstr='create table table01 ("id_num" INTEGER PRIMARY KEY NOT NULL, "name"  TEXT NOT NULL, "money"  TEXT NOT NULL)'

cursor.execute(sqlstr)
conn.commit() # 更新

print('新增資料 3 筆 寫法一')
#Insert 增加
#Insert 新增資料, id_num不可重複
sqlstr='insert into table01 values(5, "Apple", 333)'
cursor.execute(sqlstr)
sqlstr='insert into table01 values(1, "Banana", 777)'
cursor.execute(sqlstr)
sqlstr='insert into table01 values(4, "Cat", 444)'
cursor.execute(sqlstr)

print('新增資料 2 筆 寫法二')
cursor.execute("insert into table01 (id_num, name, money) " + "values (9, 'Dog', 888)")
#id_num不重複 但name money 重複
cursor.execute("insert into table01 (id_num, name, money) " + "values (2, 'Dog', 888)")

print('新增資料 2 筆 寫法三')
# 定義資料串列
datas = [[8, 'Frog', 666],
        [3, 'Giraffe', 222],]

#Insert
for data in datas:
    # 新增資料
    # print("insert into table01 (id_num, name, money) VALUES ({}, '{}', '{}')".format(data[0], data[1], data[2]))
    conn.execute("insert into table01 (id_num, name, money) VALUES ({}, '{}', '{}')".format(data[0], data[1], data[2]))
conn.commit() # 更新

print('新增資料 2 筆 寫法四')
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

#Update 更新
print('更新資料, 修改2號的資料')
#print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename) # 建立資料庫連線
conn.execute("update table01 SET name = '{}'  WHERE id_num={}".format('Eagle', 2))  #修改2號的資料, 要先確保已經有2號的資料, 才可以修改
conn.execute("update table01 SET money = '{}' WHERE id_num={}".format(111, 2))      #修改2號的資料, 要先確保已經有2號的資料, 才可以修改
conn.commit() # 更新
conn.close()  # 關閉資料庫連線

#Delete 刪除
print('刪除資料, 刪除4號的資料')
#print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename) # 建立資料庫連線
conn.execute("delete FROM table01 WHERE id_num={}".format(4))
conn.commit() # 更新
conn.close()  # 關閉資料庫連線

#Select 讀取
print('讀取資料庫資料')
#print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename) # 建立資料庫連線
cursor = conn.execute('select * from table01')
conn.commit() # 更新
conn.close()  # 關閉資料庫連線

#Select 讀取
#print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename) # 建立資料庫連線
print('指明抓一筆資料, 9號')
number = 9
cursor = conn.execute('select * from table01 where id_num = ' + str(number))
row = cursor.fetchone()
if not row == None:
    print("{}\t{}\t{}".format(row[0], row[1], row[2]))
else:
    print('找不到' + str(number) + '號資料')

print('指明抓一筆資料, 15號')
number = 15
cursor = conn.execute('select * from table01 where id_num = ' + str(number))
row = cursor.fetchone()
if not row == None:
    print("{}\t{}\t{}".format(row[0], row[1], row[2]))
else:
    print('找不到' + str(number) + '號資料')
    
conn.commit() # 更新
conn.close()  # 關閉資料庫連線


'''
#讀取一筆資料
row = cursor.fetchone()
print(row[0], row[1], row[2])
#再讀取一筆資料
row = cursor.fetchone()
print(row[0], row[1], row[2])
'''

'''
rows = cursor.fetchall()    #讀取全部資料
print('共有 : ' + str(len(rows)) + " 筆資料")
print('顯示原始資料')
print(rows)

print('逐筆顯示資料')
for row in rows:
    print(row[0], row[1], row[2])
'''

print('尋找資料')
#print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename) # 建立資料庫連線
number = 8
sqlstr = "select * from table01 where id_num={};".format(number)
cursor = conn.execute(sqlstr)
rows = cursor.fetchall()    #讀取全部資料
if len(rows) > 0:
    print("找到資料 {}\t{}\t{}".format(rows[0][0], rows[0][1], rows[0][2]))
    answer = input("確定要刪除嗎？(y/n)")
    if answer == 'y' or answer == 'Y':
        sqlstr = "delete from table01 where id_num={};".format(number)
        conn.execute(sqlstr)
        conn.commit() # 更新
        print("已刪除指定的資料")
else:
    print('找不到資料')

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

print('用fetchall()讀取 全部資料')
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
    print('第' + str(i + 1) + '筆資料 : ', end="")
    #print(rows[i])
    print("{}\t{}\t{}".format(rows[i][0], rows[i][1], rows[i][2]))
conn.close()  # 關閉資料庫連線

'''
print('刪除資料庫中的資料表')
#print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename) # 建立資料庫連線
cursor = conn.execute('drop table table01')
conn.commit() # 更新
conn.close()  # 關閉資料庫連線
'''

import time
import sqlite3

db_filename = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/ddb_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.sqlite';

#print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename) # 建立資料庫連線

cursor = conn.cursor() # 建立 cursor 物件

print('建立表單')
cursor.execute("create table talbe01"
"("
"   filename varchar(32),"
"   filesize varchar(32)"
")")


print('Insert')
cursor.execute("insert into talbe01"
"  (filename, filesize)"
"  values"
"  (?, ?)",
('aaaa.mp4', '12345'))


print('Select')
cursor.execute("select * from talbe01"
"  where filename = ?",
('aaaa.mp4',))

print('Fetchall')
rows = cursor.fetchall()
if len(rows) > 1:
    print(rows)



'''    
    # Nope.  Someone else got there.  Remove our lock.
    cursor.execute("delete from talbe01"
                   "  where filename = ?",
                   (self.filename,))
    self.connection.commit()  # 更新
else:
    # Yup.  We're done, so go home.
    return
else:
'''

'''
print('Select')
cursor.execute("select * from talbe01"
               "  where filename = ?",
               (self.filename,))
rows = cursor.fetchall()
if len(rows) == 1:
    print('aaaaaa')

print('Delete')
cursor.execute("delete from talbe01"
               "  where filename = ?",
               ('aaaa.mp4',))
'''






conn.close()  # 關閉資料庫連線

