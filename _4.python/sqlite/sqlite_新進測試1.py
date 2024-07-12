"""

新進測試

"""

print("------------------------------------------------------------")  # 60個
print("準備工作")

import sqlite3


def show_data_base_contents(db_filename, table_name, length):
    conn = sqlite3.connect(db_filename)  # 建立資料庫連線
    sqlstr = "SELECT * FROM {};".format(table_name)  # same
    sqlstr = "SELECT * FROM %s" % table_name
    cursor = conn.execute(sqlstr)

    n = 0
    for row in cursor:
        print(row)
        n = n + 1
        # 讀取 N 筆資料, 即跳出
        if n == length:
            break
    conn.close()  # 關閉資料庫連線


def show_data_base_contents_all(db_filename, table_name):
    conn = sqlite3.connect(db_filename)  # 建立資料庫連線
    sqlstr = "SELECT * FROM {};".format(table_name)  # same
    sqlstr = "SELECT * FROM %s" % table_name
    results = str(conn.execute(sqlstr).fetchall())
    print(results)
    conn.close()  # 關閉資料庫連線


print("------------------------------------------------------------")  # 60個

print("新進測試")


db_filename = "ims_sql/db_ims.sqlite"
db_filename = "C:/_git/vcs/_1.data/______test_files1/_db/gasoline.sqlite"
# db_filename  = 'db_20230703_113217.sqlite'

print("建立資料庫連線, 資料庫 : " + db_filename)
conn = sqlite3.connect(db_filename)  # 建立資料庫連線

print("要事先能知道表單的名稱 prices 與 各欄位的名稱 gdate")

cursor = conn.execute("SELECT * FROM prices ORDER BY gdate DESC;")

n = 0
for row in cursor:
    print(row)
    print("日期：{}，92無鉛：{}，95無鉛：{}，98無鉛：{}".format(row[0], row[1], row[2], row[3]))
    n = n + 1
    # 讀取10筆資料, 即跳出
    if n == 5:
        break

conn.close()  # 關閉資料庫連線

print("-------------------")
table_name = "prices"
length = 5
show_data_base_contents(db_filename, table_name, length)
print("-------------------")
show_data_base_contents_all(db_filename, table_name)

# ----------------------------------------------------------------


"""

新進測試
測試 SERIAL 測不出效果

測試 TIMESTAMP
測試 DATE
測試 CHECK

測試部分填入資料

"""

print("------------------------------------------------------------")  # 60個
print("新進測試")

import sqlite3
import datetime

db_filename = "sssss4.sqlite"

print("建立資料庫連線, 資料庫 : " + db_filename)
conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

sqlstr = """
CREATE TABLE IF NOT EXISTS table01 (
  --id SERIAL PRIMARY KEY,   無效
  id_num INTEGER,
  name VARCHAR(50),
  birthday DATE CHECK(birthday > '1900-01-01'),
  work_time DATE CHECK(work_time > birthday),
  money INTEGER CHECK(money > 0), -- 預設錯誤時會顯示
  update_time TIMESTAMP
);
"""

cursor.execute(sqlstr)
conn.commit()  # 更新

id_num = 3
name = "David"
birthday = "2006-03-11"
work_time = "2023-07-11"
money = 2345
update_time = datetime.datetime.now()

sql = "INSERT INTO table01 (id_num, name, birthday, work_time, money, update_time) VALUES ({}, '{}', '{}', '{}', {}, '{}')"
# print(sql)
sqlstr = sql.format(id_num, name, birthday, work_time, money, update_time)

# 或者直接寫
# sqlstr = "INSERT INTO table01 (id_num, name, birthday, work_time, money) VALUES (5, 'David', 'xxxx', 'xxxx', 1234, 'xxxx');"

cursor.execute(sqlstr)

print("資料不足時, 部分填入資料")
id_num = 5
name = "Eric"
update_time = datetime.datetime.now()

sql = "INSERT INTO table01 (id_num, name, update_time) VALUES ({}, '{}', '{}')"
# print(sql)
sqlstr = sql.format(id_num, name, update_time)
cursor.execute(sqlstr)

conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

conn = sqlite3.connect(db_filename)  # 建立資料庫連線

cursor = conn.execute("SELECT * FROM table01")

n = 0
for row in cursor:
    print(row)
    n = n + 1
    # 讀取10筆資料, 即跳出

conn.close()  # 關閉資料庫連線


print("------------------------------------------------------------")  # 60個
print("一次寫入多行的語法 executescript")

import sqlite3
import datetime

db_filename = "sssss4_many1.sqlite"

print("建立資料庫連線, 資料庫 : " + db_filename)
conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件
conn.execute("CREATE virtual TABLE table01 using fts3(name, ingredients)")
conn.executescript(
    """
    INSERT INTO table01 (name, ingredients) VALUES ('broccoli stew', 'broccoli peppers cheese tomatoes');
    INSERT INTO table01 (name, ingredients) VALUES ('pumpkin stew', 'pumpkin onions garlic celery');
    INSERT INTO table01 (name, ingredients) VALUES ('broccoli pie', 'broccoli cheese onions flour');
    INSERT INTO table01 (name, ingredients) VALUES ('pumpkin pie', 'pumpkin sugar flour butter');
    """
)

for row in conn.execute(
    "SELECT rowid, name, ingredients FROM table01 WHERE name MATCH 'pie'"
):
    print(row)

# conn.commit() # 更新

table_name = "table01"
show_data_base_contents_all(db_filename, table_name)


print("------------------------------------------------------------")  # 60個
print("一次寫入多行的語法 executescript")

import sqlite3

con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.executescript(
    """
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
    """
)

print("------------------------------------------------------------")  # 60個
print("xxxxx")

import sqlite3

con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("CREATE TABLE people (name_last, age)")

who = "David"
age = 18

cur.execute("INSERT INTO people VALUES (?, ?)", (who, age))


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


# 檔案 : C:\_git\vcs\_4.python\sqlite\sqlite_新進測試2.py

"""

新進測試

"""

print("------------------------------------------------------------")  # 60個
print("準備工作")

import sqlite3
import time


def show_data_base_contents(db_filename, table_name, length):
    conn = sqlite3.connect(db_filename)  # 建立資料庫連線
    sqlstr = "SELECT * FROM {};".format(table_name)  # same
    sqlstr = "SELECT * FROM %s" % table_name
    cursor = conn.execute(sqlstr)

    n = 0
    for row in cursor:
        print(row)
        n = n + 1
        # 讀取 N 筆資料, 即跳出
        if n == length:
            break
    conn.close()  # 關閉資料庫連線


def show_data_base_contents_all(db_filename, table_name):
    conn = sqlite3.connect(db_filename)  # 建立資料庫連線
    sqlstr = "SELECT * FROM {};".format(table_name)  # same
    sqlstr = "SELECT * FROM %s" % table_name
    results = str(conn.execute(sqlstr).fetchall())
    print(results)
    conn.close()  # 關閉資料庫連線


print("------------------------------------------------------------")  # 60個

print("新進測試")

db_filename = (
    "C:/_git/vcs/_1.data/______test_files2/db_"
    + time.strftime("%Y%m%d_%H%M%S", time.localtime())
    + ".sqlite"
)

mem_conn = sqlite3.connect(":memory:")  # 建立資料庫連線, 記憶體
disk_conn = sqlite3.connect("example.db")  # 建立資料庫連線, 磁碟

cursor = mem_conn.cursor()
cursor.execute("CREATE TABLE table01 (name_last, age)")

print("目前共有修改資料次數 : ", mem_conn.total_changes)

who = "David"
age = 18

cursor.execute("INSERT INTO table01 VALUES (?, ?)", (who, age))

print("目前共有修改資料次數 : ", mem_conn.total_changes)

cursor.execute("INSERT INTO table01 VALUES (?, ?)", (who, age))
cursor.execute("INSERT INTO table01 VALUES (?, ?)", (who, age))
cursor.execute("INSERT INTO table01 VALUES (?, ?)", (who, age))
print("目前共有修改資料次數 : ", mem_conn.total_changes)

cursor.execute(
    """CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)"""
)
cursor.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")


mem_conn.commit()

cursor.execute("SELECT * FROM table01")
print(cursor.fetchall())

# 使用 backup 命令将内存数据库备份到磁盘数据库。

# 备份内存数据库到磁盘数据库
mem_conn.backup(disk_conn)

"""
backup 覆蓋
attach 附加
"""

"""
# 将磁盘数据库附加到内存数据库中
mem_conn.execute("ATTACH DATABASE 'example.db' AS disk_db")

# 执行插入命令将数据插入到磁盘数据库中
mem_conn.execute("INSERT INTO disk_db.example_table VALUES (1, 'example')")
"""

# 关闭数据库连接对象
mem_conn.close()
disk_conn.close()

print("------------------------------------------------------------")  # 60個

db_filename = "example.db"
table_name = "table01"
show_data_base_contents_all(db_filename, table_name)


table_name = "stocks"
show_data_base_contents_all(db_filename, table_name)


print("------------------------------------------------------------")  # 60個
print("測 executemany")

import sqlite3

stocks = [
    ("2006-01-05", "BUY", "RHAT", 100, 35.14),
    ("2006-03-28", "BUY", "IBM", 1000, 45.0),
    ("2006-04-06", "SELL", "IBM", 500, 53.0),
    ("2006-04-05", "BUY", "MSFT", 1000, 72.0),
]
conn = sqlite3.connect(":memory:")
conn.execute(
    "create table stocks (date text, buysell text, symb text, amount int, price real)"
)
conn.executemany("insert into stocks values (?, ?, ?, ?, ?)", stocks)
cur = conn.cursor()

for row in cur.execute("SELECT * FROM stocks ORDER BY price"):
    print(row)

# Output:
# ('2006-01-05', 'BUY', 'RHAT', 100, 35.14)
# ('2006-03-28', 'BUY', 'IBM', 1000, 45.0)
# ('2006-04-06', 'SELL', 'IBM', 500, 53.0)
# ('2006-04-05', 'BUY', 'MSFT', 1000, 72.0)


cur.execute("SELECT * FROM stocks ORDER BY price")

one_row_data = cur.fetchone()
print("fetchone", one_row_data)

while one_row_data:
    one_row_data = cur.fetchone()
    print("fetchone", one_row_data)


print("------------------------------------------------------------")  # 60個
print("測試各種fetch")
"""
fetchone()	#抓一行 tuple
fetchmany(size=cursor.arraysize)	#抓n行 list
fetchall()	#抓取剩下的全部 list

"""

db_filename = "ims_sql/db_ims.sqlite"
db_filename = "C:/_git/vcs/_1.data/______test_files1/_db/gasoline.sqlite"
# db_filename  = 'db_20230703_113217.sqlite'

print("建立資料庫連線, 資料庫 : " + db_filename)
conn = sqlite3.connect(db_filename)  # 建立資料庫連線

cursor = conn.execute("SELECT * FROM prices;")

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
# print(cccc)


conn.close()  # 關閉資料庫連線


print("------------------------------------------------------------")  # 60個
print("xxxxx new 0717")

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute("CREATE TABLE table01(key INTEGER PRIMARY KEY, task TEXT)")

tasks = (
    "give food to fish",
    "prepare group meeting",
    "fight with a zebra",
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


"""

注意：不要使用%s 將字串插入 SQL 命令，因為它可能使你的程式容易受到 SQL 注入攻擊（請參閱 SQL 注入 ）。

"""

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\sqlite\sqlite_新進測試4.py

"""

新進測試

建立多個表單 要分開寫

"""

print("------------------------------------------------------------")  # 60個
print("準備工作")

import sqlite3
import time


def show_data_base_contents(db_filename, table_name, length):
    conn = sqlite3.connect(db_filename)  # 建立資料庫連線
    sqlstr = "SELECT * FROM {};".format(table_name)  # same
    sqlstr = "SELECT * FROM %s" % table_name
    cursor = conn.execute(sqlstr)

    n = 0
    for row in cursor:
        print(row)
        n = n + 1
        # 讀取 N 筆資料, 即跳出
        if n == length:
            break
    conn.close()  # 關閉資料庫連線


def show_data_base_contents_all(db_filename, table_name):
    conn = sqlite3.connect(db_filename)  # 建立資料庫連線
    sqlstr = "SELECT * FROM {};".format(table_name)  # same
    sqlstr = "SELECT * FROM %s" % table_name
    results = str(conn.execute(sqlstr).fetchall())
    print(results)
    conn.close()  # 關閉資料庫連線


print("------------------------------------------------------------")  # 60個


db_filename = "cccc" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".sqlite"

print("建立資料庫連線, 資料庫 : " + db_filename)
conn = sqlite3.connect(db_filename)  # 建立資料庫連線

cursor = conn.cursor()  # 建立 cursor 物件

print("建立表單")

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

# conn.commit() # 更新
# conn.close()  # 關閉資料庫連線


# 建立三個表單

sqlstr = "DROP TABLE IF EXISTS table01"
cursor.execute(sqlstr)

sqlstr = "DROP TABLE IF EXISTS table02"
cursor.execute(sqlstr)

sqlstr = "DROP TABLE IF EXISTS table03"
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

conn.commit()  # 更新
conn.close()  # 關閉資料庫連線


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\sqlite\sqlite_新進測試5.py

"""

新進測試

建立多個表單 要分開寫

"""

print("------------------------------------------------------------")  # 60個
print("準備工作")


print("------------------------------------------------------------")  # 60個

''' CREATE + PK
sql = """Create table student2(  
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        gender TEXT)"""
'''

print("------------------------------------------------------------")  # 60個

""" INSERT
import sqlite3
conn = sqlite3.connect("myInfo.db")     # 資料庫連線
print("請輸入myInfo資料庫students表單資料")
while True:
    new_id = int(input("請輸入id : "))  # 轉成整數
    new_name = input("請輸入name : ")
    new_gender = input("請輸入gender : ")
    x = (new_id, new_name, new_gender)
    sql = '''insert into students values(?,?,?)'''
    conn.execute(sql,x)
    conn.commit()                       # 更新資料庫
    again = input("繼續(y/n)? ")
    if again[0].lower() == "n":
        break
conn.close()                            # 關閉資料庫連線
"""

print("------------------------------------------------------------")  # 60個

# INSERT
import sqlite3

conn = sqlite3.connect("myInfo2.db")  # 資料庫連線

n_name = "david"
n_gender = "M"
x = (n_name, n_gender)
sql = """insert into student2(name, gender) values(?,?)"""
conn.execute(sql, x)
conn.commit()  # 更新資料庫

conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個

import sqlite3

conn = sqlite3.connect("myInfo.db")  # 資料庫連線
results = conn.execute("SELECT * from students")
for record in results:
    print("id = ", record[0])
    print("name = ", record[1])
    print("gender = ", record[2])
conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個

import sqlite3

conn = sqlite3.connect("myInfo2.db")  # 資料庫連線
results = conn.execute("SELECT * from student2")
for record in results:
    print("id = ", record[0])
    print("name = ", record[1])
    print("gender = ", record[2])
conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個

import sqlite3

conn = sqlite3.connect("myInfo.db")  # 資料庫連線
results = conn.execute("SELECT * from students")
allstudents = results.fetchall()  # 結果轉成元素是元組的串列
for student in allstudents:
    print(student)
conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個

import sqlite3

conn = sqlite3.connect("myInfo.db")  # 資料庫連線
results = conn.execute("SELECT name from students")
allstudents = results.fetchall()  # 結果轉成元素是元組的串列
for student in allstudents:
    print(student)
conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個

import sqlite3

conn = sqlite3.connect("myInfo.db")  # 資料庫連線
sql = '''SELECT name, gender
        from students
        where gender = "F"'''
results = conn.execute(sql)
allstudents = results.fetchall()  # 結果轉成元素是元組的串列
for student in allstudents:
    print(student)
conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個

import sqlite3

conn = sqlite3.connect("myInfo.db")  # 資料庫連線
sql = """UPDATE students
        set name = "Tomy"
        where id = 1"""
results = conn.execute(sql)
conn.commit()  # 更新資料庫
results = conn.execute("SELECT name from students")
allstudents = results.fetchall()  # 結果轉成元素是元組的串列
for student in allstudents:
    print(student)
conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個

import sqlite3

conn = sqlite3.connect("myInfo.db")  # 資料庫連線
sql = """DELETE
        from students
        where id = 2"""
results = conn.execute(sql)
conn.commit()  # 更新資料庫
results = conn.execute("SELECT name from students")
allstudents = results.fetchall()  # 結果轉成元素是元組的串列
for student in allstudents:
    print(student)
conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個

import csv
import time
import sqlite3
import matplotlib.pyplot as plt

db_filename = "tmp_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".sqlite"

conn = sqlite3.connect(db_filename)  # 資料庫連線
sql = """Create table population( 
        area TEXT,
        male int,                     
        female int,
        total int)"""
conn.execute(sql)  # 執行SQL指令

fn = "Taipei_Population.csv"
with open(fn) as csvFile:  # 儲存在SQLite
    csvReader = csv.reader(csvFile)
    listCsv = list(csvReader)  # 轉成串列
    csvData = listCsv[4:]  # 切片刪除前4 rows
    for row in csvData:
        area = row[0]  # 區名稱
        male = int(row[7])  # 男性人數
        female = int(row[8])  # 女性人數
        total = int(row[6])  # 總人數
        x = (area, male, female, total)
        sql = """insert into population values(?,?,?,?)"""
        conn.execute(sql, x)
        conn.commit()

results = conn.execute("SELECT * from population")
for record in results:
    print("區域       = ", record[0])
    print("男性人口數 = ", record[1])
    print("女性人口數 = ", record[2])
    print("總計人口數 = ", record[3])

conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個


import sqlite3
import matplotlib.pyplot as plt
from pylab import mpl

conn = sqlite3.connect(db_filename)  # 資料庫連線
results = conn.execute("SELECT * from population")

area, male, female, total = [], [], [], []
for record in results:  # 將人口資料放入串列
    area.append(record[0])
    male.append(record[1])
    female.append(record[2])
    total.append(record[3])
conn.close()  # 關閉資料庫連線

mpl.rcParams["font.sans-serif"] = ["SimHei"]  # 使用黑體
seq = area
(linemale,) = plt.plot(seq, male, "-*", label="男性人口數")
(linefemale,) = plt.plot(seq, female, "-o", label="女性人口數")
(linetotal,) = plt.plot(seq, total, "-^", label="總計人口數")

plt.legend(handles=[linemale, linefemale, linetotal], loc="best")
plt.title("台北市", fontsize=24)
plt.xlabel("2019年", fontsize=14)
plt.ylabel("人口數", fontsize=14)
plt.show()


print("------------------------------------------------------------")  # 60個


import sqlite3

try:
    # 嘗試連接到資料庫
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()
    # 嘗試執行查詢，可能會引發異常
    cursor.execute("SELECT * FROM non_existent_table")
except sqlite3.Error as e:
    # 捕獲並處理 SQLite 特定的異常
    print(f"Database error: {e}")
except Exception as e:
    # 捕獲並處理其他所有異常
    print(f"Exception occurred: {e}")
finally:
    # 確保資料庫連接被關閉
    conn.close()

print("------------------------------------------------------------")  # 60個

import sqlite3

conn = sqlite3.connect("data29_1.db")  # 資料庫連線
sql = '''SELECT name, tel
        from students
        where gender = "F"'''
results = conn.execute(sql)
allstudents = results.fetchall()  # 結果轉成元素是元組的串列
for student in allstudents:
    print(student)
conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\sqlite\sqlite_新進測試6.py

import sqlite3  # 匯入sqlite3模組

con = sqlite3.connect("python.sqlite")  # 連線到資料庫
cur = con.cursor()  # 獲得資料庫游標
cur.execute("insert into people (name,age,sex) values ('Jee',21,'F')")  # 執行SQL敘述
r = cur.execute("delete from people where age=20")  # 執行SQL敘述
con.commit()  # 傳送交易
cur.execute("select * from people")  # 執行SQL敘述
s = cur.fetchall()  # 獲得資料
print(s)  # 列印資料
cur.close()  # 關閉游標
con.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
