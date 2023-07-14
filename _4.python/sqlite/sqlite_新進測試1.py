'''

新進測試

'''

print('----------------------------------------------------------------------')	#70個
print('準備工作')

import sqlite3

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


db_filename  = 'ims_sql/db_ims.sqlite'
db_filename = 'C:/_git/vcs/_1.data/______test_files1/_db/gasoline.sqlite'
#db_filename  = 'db_20230703_113217.sqlite'

print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename) # 建立資料庫連線

print('要事先能知道表單的名稱 prices 與 各欄位的名稱 gdate')

cursor = conn.execute('SELECT * FROM prices ORDER BY gdate DESC;')

n = 0
for row in cursor:
    print(row)
    print("日期：{}，92無鉛：{}，95無鉛：{}，98無鉛：{}". format(row[0], row[1], row[2], row[3]))
    n = n + 1
    #讀取10筆資料, 即跳出
    if n == 5:
        break

conn.close()  # 關閉資料庫連線

print('-------------------')
table_name  = 'prices'
length = 5
show_data_base_contents(db_filename, table_name, length)
print('-------------------')
show_data_base_contents_all(db_filename, table_name)

#----------------------------------------------------------------


'''

新進測試
測試 SERIAL 測不出效果

測試 TIMESTAMP
測試 DATE
測試 CHECK

測試部分填入資料

'''

print('----------------------------------------------------------------------')	#70個
print('新進測試')

import sqlite3
import datetime

db_filename  = 'sssss4.sqlite'

print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename) # 建立資料庫連線
cursor = conn.cursor() # 建立 cursor 物件

sqlstr = '''
CREATE TABLE IF NOT EXISTS table01 (
  --id SERIAL PRIMARY KEY,   無效
  id_num INTEGER,
  name VARCHAR(50),
  birthday DATE CHECK(birthday > '1900-01-01'),
  work_time DATE CHECK(work_time > birthday),
  money INTEGER CHECK(money > 0), -- 預設錯誤時會顯示
  update_time TIMESTAMP
);
'''

cursor.execute(sqlstr)
conn.commit() # 更新

id_num = 3
name = 'David'
birthday = '2006-03-11'
work_time = '2023-07-11'
money = 2345
update_time = datetime.datetime.now()

sql = "INSERT INTO table01 (id_num, name, birthday, work_time, money, update_time) VALUES ({}, '{}', '{}', '{}', {}, '{}')"
#print(sql)
sqlstr = sql.format(id_num, name, birthday, work_time, money, update_time)

#或者直接寫
#sqlstr = "INSERT INTO table01 (id_num, name, birthday, work_time, money) VALUES (5, 'David', 'xxxx', 'xxxx', 1234, 'xxxx');"

cursor.execute(sqlstr)

print('資料不足時, 部分填入資料')
id_num = 5
name = 'Eric'
update_time = datetime.datetime.now()

sql = "INSERT INTO table01 (id_num, name, update_time) VALUES ({}, '{}', '{}')"
#print(sql)
sqlstr = sql.format(id_num, name, update_time)
cursor.execute(sqlstr)

conn.commit() # 更新
conn.close()  # 關閉資料庫連線

conn = sqlite3.connect(db_filename) # 建立資料庫連線

cursor = conn.execute('SELECT * FROM table01')

n = 0
for row in cursor:
    print(row)
    n = n + 1
    #讀取10筆資料, 即跳出

conn.close()  # 關閉資料庫連線


print('----------------------------------------------------------------------')	#70個
print('一次寫入多行的語法')

import sqlite3
import datetime

db_filename  = 'sssss4_many1.sqlite'

print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename) # 建立資料庫連線
cursor = conn.cursor() # 建立 cursor 物件
conn.execute("CREATE virtual TABLE table01 using fts3(name, ingredients)")
conn.executescript("""
    INSERT INTO table01 (name, ingredients) VALUES ('broccoli stew', 'broccoli peppers cheese tomatoes');
    INSERT INTO table01 (name, ingredients) VALUES ('pumpkin stew', 'pumpkin onions garlic celery');
    INSERT INTO table01 (name, ingredients) VALUES ('broccoli pie', 'broccoli cheese onions flour');
    INSERT INTO table01 (name, ingredients) VALUES ('pumpkin pie', 'pumpkin sugar flour butter');
    """)

for row in conn.execute("select rowid, name, ingredients from table01 where name match 'pie'"):
    print(row)


#conn.commit() # 更新

table_name  = 'table01'
show_data_base_contents_all(db_filename, table_name)


print('----------------------------------------------------------------------')	#70個
print('一次寫入多行的語法')

import sqlite3

con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.executescript("""
    CREATE TABLE person(
        firstname,
        lastname,
        age
    );

    CREATE TABLE book(
        title,
        author,
        published
    );

    INSERT INTO book(title, author, published)
    VALUES (
        'Dirk Gently''s Holistic Detective Agency',
        'Douglas Adams',
        1987
    );
    """)


print('----------------------------------------------------------------------')	#70個
print('xxxxx')


import sqlite3

con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("CREATE TABLE people (name_last, age)")

who = 'David'
age = 18

cur.execute("INSERT INTO people VALUES (?, ?)", (who, age))


print('----------------------------------------------------------------------')	#70個
print('xxxxx')



print("程式執行完畢！")

