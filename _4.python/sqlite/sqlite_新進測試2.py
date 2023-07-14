'''

新進測試

'''

print('----------------------------------------------------------------------')	#70個
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

print('----------------------------------------------------------------------')	#70個

print('新進測試')

db_filename = 'C:/_git/vcs/_1.data/______test_files2/db_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.a.qlite';


mem_conn = sqlite3.connect(':memory:')	# 建立資料庫連線, 記憶體
disk_conn = sqlite3.connect('example.db') # 建立資料庫連線, 磁碟

cursor = mem_conn.cursor()
cursor.execute("CREATE TABLE table01 (name_last, age)")

who = "David"
age = 18

cursor.execute("INSERT INTO table01 VALUES (?, ?)", (who, age))


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

print('----------------------------------------------------------------------')	#70個

db_filename = 'example.db'
table_name = 'table01'
show_data_base_contents_all(db_filename, table_name)


table_name = 'stocks'
show_data_base_contents_all(db_filename, table_name)





print('----------------------------------------------------------------------')	#70個
print('xxxxx')



print("程式執行完畢！")

