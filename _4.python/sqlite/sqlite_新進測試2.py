'''

新進測試

'''

print('------------------------------------------------------------')	#60個
print('準備工作')

import sqlite3
import time

def show_data_base_contents(db_filename, table_name, length):
    conn = sqlite3.connect(db_filename) # 建立資料庫連線
    sqlstr = 'SELECT * FROM {};'.format(table_name)#same
    sqlstr = 'SELECT * FROM %s' % table_name
    cursor = conn.execute(sqlstr)

    n = 0
    for row in cursor:
        print(row)
        n = n + 1
        #讀取 N 筆資料, 即跳出
        if n == length:
            break
    conn.close()  # 關閉資料庫連線

def show_data_base_contents_all(db_filename, table_name):
    conn = sqlite3.connect(db_filename) # 建立資料庫連線
    sqlstr = 'SELECT * FROM {};'.format(table_name)#same
    sqlstr = 'SELECT * FROM %s' % table_name
    results = str(conn.execute(sqlstr).fetchall())
    print(results)
    conn.close()  # 關閉資料庫連線

print('------------------------------------------------------------')	#60個

print('新進測試')

db_filename = 'C:/_git/vcs/_1.data/______test_files2/db_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.sqlite';

mem_conn = sqlite3.connect(':memory:')	# 建立資料庫連線, 記憶體
disk_conn = sqlite3.connect('example.db') # 建立資料庫連線, 磁碟

cursor = mem_conn.cursor()
cursor.execute("CREATE TABLE table01 (name_last, age)")

print('目前共有修改資料次數 : ', mem_conn.total_changes)

who = "David"
age = 18

cursor.execute("INSERT INTO table01 VALUES (?, ?)", (who, age))

print('目前共有修改資料次數 : ', mem_conn.total_changes)

cursor.execute("INSERT INTO table01 VALUES (?, ?)", (who, age))
cursor.execute("INSERT INTO table01 VALUES (?, ?)", (who, age))
cursor.execute("INSERT INTO table01 VALUES (?, ?)", (who, age))
print('目前共有修改資料次數 : ', mem_conn.total_changes)

cursor.execute('''CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)''')
cursor.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")


mem_conn.commit()

cursor.execute("SELECT * FROM table01")
print(cursor.fetchall())

#使用 backup 命令将内存数据库备份到磁盘数据库。

# 备份内存数据库到磁盘数据库
mem_conn.backup(disk_conn)

'''
backup 覆蓋
attach 附加
'''

'''
# 将磁盘数据库附加到内存数据库中
mem_conn.execute("ATTACH DATABASE 'example.db' AS disk_db")

# 执行插入命令将数据插入到磁盘数据库中
mem_conn.execute("INSERT INTO disk_db.example_table VALUES (1, 'example')")
'''

# 关闭数据库连接对象
mem_conn.close()
disk_conn.close()

print('------------------------------------------------------------')	#60個

db_filename = 'example.db'
table_name = 'table01'
show_data_base_contents_all(db_filename, table_name)


table_name = 'stocks'
show_data_base_contents_all(db_filename, table_name)





print('------------------------------------------------------------')	#60個
print('測 executemany')

import sqlite3
stocks = [('2006-01-05', 'BUY', 'RHAT', 100, 35.14),
          ('2006-03-28', 'BUY', 'IBM', 1000, 45.0),
          ('2006-04-06', 'SELL', 'IBM', 500, 53.0),
          ('2006-04-05', 'BUY', 'MSFT', 1000, 72.0)]
conn = sqlite3.connect(":memory:")
conn.execute("create table stocks (date text, buysell text, symb text, amount int, price real)")
conn.executemany("insert into stocks values (?, ?, ?, ?, ?)", stocks)    
cur = conn.cursor()
    
for row in cur.execute('SELECT * FROM stocks ORDER BY price'):
    print(row)
    
# Output:
# ('2006-01-05', 'BUY', 'RHAT', 100, 35.14)
# ('2006-03-28', 'BUY', 'IBM', 1000, 45.0)
# ('2006-04-06', 'SELL', 'IBM', 500, 53.0)
# ('2006-04-05', 'BUY', 'MSFT', 1000, 72.0)


cur.execute('SELECT * FROM stocks ORDER BY price')

one_row_data = cur.fetchone()
print('fetchone', one_row_data)

while one_row_data:
    one_row_data = cur.fetchone()
    print('fetchone', one_row_data)
    

print('------------------------------------------------------------')	#60個
print('測試各種fetch')
'''
fetchone()	#抓一行 tuple
fetchmany(size=cursor.arraysize)	#抓n行 list
fetchall()	#抓取剩下的全部 list

'''

db_filename  = 'ims_sql/db_ims.sqlite'
db_filename = 'C:/_git/vcs/_1.data/______test_files1/_db/gasoline.sqlite'
#db_filename  = 'db_20230703_113217.sqlite'

print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename) # 建立資料庫連線

cursor = conn.execute('SELECT * FROM prices;')

aaaa = cursor.fetchone()
print(type(aaaa))
print(aaaa)

aaaa = cursor.fetchone()
print(type(aaaa))
print(aaaa)

bbbb = cursor.fetchmany(3)
print(type(bbbb))
print(bbbb)

cccc = cursor.fetchall()
print(type(cccc))
#print(cccc)







conn.close()  # 關閉資料庫連線



print('------------------------------------------------------------')	#60個
print('xxxxx new 0717')

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute("CREATE TABLE table01(key INTEGER PRIMARY KEY, task TEXT)")

tasks = (
'give food to fish',
'prepare group meeting',
'fight with a zebra',
)

for task in tasks:
    cursor.execute("INSERT INTO table01 VALUES(NULL, ?)", (task,))

cursor.execute("SELECT * FROM table01")
print(cursor.fetchall())


# Update a record, just for good measure.
cursor.execute("UPDATE table01 SET task = 'learn italian' WHERE key = 1")


cursor.execute("SELECT * FROM table01")
print(cursor.fetchall())


key_id = 2
cursor.execute("SELECT * FROM table01 WHERE key=?", (str(key_id),))
key, task = cursor.fetchone()

print(key)
print(task)





print("程式執行完畢！")




'''

注意：不要使用%s 將字串插入 SQL 命令，因為它可能使你的程式容易受到 SQL 注入攻擊（請參閱 SQL 注入 ）。

'''
