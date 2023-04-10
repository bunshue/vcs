import time
import sqlite3

db_filename = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/db_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.sqlite';

print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename) # 建立資料庫連線

cursor = conn.cursor() # 建立 cursor 物件

print('建立一個資料表')
''' 其他寫法
#cursor.execute("create table table01 ( id char(5), subjectId char(4) not null, " +
#               "animalNumber integer, title varchar(50) not null, primary key (id))")

#id可重複
#cursor.execute("create table table01 ( id char(5), subjectId char(4) not null, " +
#               "animalNumber integer, title varchar(50) not null)")

#id可重複, 若資料庫已存在 則不用重新建立
cursor.execute("create table if not exists table01 ( id char(5), subjectId char(4) not null, " +
               "animalNumber integer, title varchar(50) not null)")
'''
#Create
#Create table table01, id 和 name 和 tel,
#primary key (id), id不可重複
sqlstr='create table if not exists table01 ("id" INTEGER PRIMARY KEY NOT NULL, "name"  TEXT NOT NULL, "tel"  TEXT NOT NULL)'
#sqlstr='create table table01 ("id" INTEGER PRIMARY KEY NOT NULL, "name"  TEXT NOT NULL, "tel"  TEXT NOT NULL)'

cursor.execute(sqlstr)
conn.commit() # 更新

print('新增資料 3 筆 寫法一')
#Insert
#Insert 新增資料, id不可重複
sqlstr='insert into table01 values(1, "Apple", "01-11111111")'
cursor.execute(sqlstr)
sqlstr='insert into table01 values(2, "Banana", "02-22222222")'
cursor.execute(sqlstr)
sqlstr='insert into table01 values(3, "Cat", "03-33333333")'
cursor.execute(sqlstr)

print('新增資料 2 筆 寫法二')
cursor.execute("insert into table01 (id, name, tel) " + "values (4, 'Dog', '04-44444444')")
#id不重複 但name重複
cursor.execute("insert into table01 (id, name, tel) " + "values (5, 'Dog', '05-55555555')")

print('新增資料 2 筆 寫法三')
# 定義資料串列
datas = [[6, 'Frog', '06-66666666'],
        [7, 'Giraffe', '07-77777777'],]

#Insert
for data in datas:
    # 新增資料
    # print("insert into table01 (id, name, tel) VALUES ({}, '{}', '{}')".format(data[0], data[1], data[2]))
    conn.execute("insert into table01 (id, name, tel) VALUES ({}, '{}', '{}')".format(data[0], data[1], data[2]))
conn.commit() # 更新

conn.close()  # 關閉資料庫連線


print('更新資料, 修改1號的資料')
print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename) # 建立資料庫連線

conn.execute("update table01 SET name='{}' WHERE id={}".format('Ken', 1))   #修改1號的資料
conn.commit() # 更新

conn.close()  # 關閉資料庫連線



print('刪除資料, 刪除4號的資料')
print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename) # 建立資料庫連線

# Delete 刪除資料
conn.execute("delete FROM table01 WHERE id={}".format(4))
conn.commit() # 更新

conn.close()  # 關閉資料庫連線


print('讀取資料庫資料')

print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename)
cursor = conn.execute('select * from table01')

'''
print('指名抓一筆資料')

cursor = conn.execute('select * from table01 where id = 3')
row = cursor.fetchone()
if not row==None:
    print("{}\t{}\t{}".format(row[0], row[1], row[2]))
'''

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

print('抓全部資料')

cursor = conn.execute('select * from table01')
rows = cursor.fetchall()    #讀取全部資料
length = len(rows)

for i in range(length):
    #print(type(rows[i]))
    print('第' + str(i) + '筆資料 : ', end="")
    print(rows[i])
    print("{}\t{}\t{}".format(rows[i][0], rows[i][1], rows[i][2]))

conn.close()  # 關閉資料庫連線



