'''

新進測試

建立多個表單 要分開寫

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


db_filename = 'cccc' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.sqlite'

print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename) # 建立資料庫連線

cursor = conn.cursor() # 建立 cursor 物件

print('建立表單')

sqlstr = """
CREATE TABLE IF NOT EXISTS table01 (
    id    INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age  INT NOT NULL,
    address  CHAR(50),
    salary REAL
);
"""
cursor.execute(sqlstr)

#conn.commit() # 更新
#conn.close()  # 關閉資料庫連線


#建立三個表單

sqlstr = 'DROP TABLE IF EXISTS table01'
cursor.execute(sqlstr)

sqlstr = 'DROP TABLE IF EXISTS table02'
cursor.execute(sqlstr)

sqlstr = 'DROP TABLE IF EXISTS table03'
cursor.execute(sqlstr)

sqlstr = """
    CREATE TABLE table01 (
    id serial NOT NULL,
    uid character varying(50) NOT NULL,
    PRIMARY KEY (id));
"""
cursor.execute(sqlstr)

sqlstr = """
    CREATE TABLE table02 (
    id serial NOT NULL,
    uid character varying(50) NOT NULL,
    PRIMARY KEY (id));
"""
cursor.execute(sqlstr)

sqlstr = """
    CREATE TABLE table03 (
    id serial NOT NULL,
    bid character varying(50) NOT NULL,
    roomtype character varying(20) NOT NULL,
    roomamount character varying(5) NOT NULL,
    datein character varying(20) NOT NULL,
    dateout character varying(20) NOT NULL,
    PRIMARY KEY (id));
"""
cursor.execute(sqlstr)

sqlstr = """
    CREATE TABLE students2 (
    sid serial NOT NULL,
    name character varying(50) NOT NULL,
    tel character varying(50),
    addr character varying(200),
    email character varying(100),
    PRIMARY KEY (sid))
"""
cursor.execute(sqlstr)

sqlstr = """
    CREATE TABLE users1 (
    id serial NOT NULL,
    uid character varying(50) NOT NULL,
    question character varying(250) NOT NULL,
    PRIMARY KEY (id))
"""
cursor.execute(sqlstr)

sqlstr = """
    CREATE TABLE login (
    id serial NOT NULL,
    uid character varying(50) NOT NULL,
    state character varying(10) NOT NULL,
    PRIMARY KEY (id))
"""
cursor.execute(sqlstr)

sqlstr = """
    CREATE TABLE users2 (
    id serial NOT NULL,
    uid character varying(50) NOT NULL,
    state character varying(10) NOT NULL,
    digit3 character varying(10) NOT NULL,
    PRIMARY KEY (id))
"""
cursor.execute(sqlstr)

sqlstr = """
    CREATE TABLE setting (
    id serial NOT NULL,
    uid character varying(50) NOT NULL,
    lang character varying(10) NOT NULL,
    sound character varying(10) NOT NULL,
    PRIMARY KEY (id))
"""
cursor.execute(sqlstr)

conn.commit() # 更新
conn.close()  # 關閉資料庫連線


