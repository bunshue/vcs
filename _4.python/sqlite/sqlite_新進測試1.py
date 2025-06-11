"""

新進測試


資料庫 db
資料表 table 表單

"""

import sys
import csv
import time
import sqlite3
import datetime
import matplotlib.pyplot as plt

print("------------------------------------------------------------")  # 60個
print("準備工作")


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

db_filename = "tmp_sssss4.sqlite"

print("建立資料庫連線, 資料庫 : " + db_filename)
conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

# 建立一個資料表 table01 + 如果尚未建立的話 + PRIMARY KEY
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

db_filename = "tmp_sssss4_many1.sqlite"

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

con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("CREATE TABLE people (name_last, age)")

who = "David"
age = 18

cur.execute("INSERT INTO people VALUES (?, ?)", (who, age))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

db_filename = (
    "C:/_git/vcs/_1.data/______test_files2/db_"
    + time.strftime("%Y%m%d_%H%M%S", time.localtime())
    + ".sqlite"
)

mem_conn = sqlite3.connect(":memory:")  # 建立資料庫連線, 記憶體
disk_conn = sqlite3.connect("tmp_example.db")  # 建立資料庫連線, 磁碟

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
mem_conn.execute("ATTACH DATABASE 'tmp_example.db' AS disk_db")

# 执行插入命令将数据插入到磁盘数据库中
mem_conn.execute("INSERT INTO disk_db.example_table VALUES (1, 'example')")
"""

# 关闭数据库连接对象
mem_conn.close()
disk_conn.close()

print("------------------------------------------------------------")  # 60個

db_filename = "tmp_example.db"
table_name = "table01"
show_data_base_contents_all(db_filename, table_name)


table_name = "stocks"
show_data_base_contents_all(db_filename, table_name)


print("------------------------------------------------------------")  # 60個
print("測 executemany")

stocks = [
    ("2006-01-05", "BUY", "RHAT", 100, 35.14),
    ("2006-03-28", "BUY", "IBM", 1000, 45.0),
    ("2006-04-06", "SELL", "IBM", 500, 53.0),
    ("2006-04-05", "BUY", "MSFT", 1000, 72.0),
]
conn = sqlite3.connect(":memory:")
conn.execute(
    "CREATE TABLE stocks (date text, buysell text, symb text, amount int, price real)"
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

cc = cursor.fetchone()
print(type(cc))
print(cc)

cc = cursor.fetchone()
print(type(cc))
print(cc)

cc = cursor.fetchmany(3)
print(type(cc))
print(cc)

cc = cursor.fetchall()
print(type(cc))
# print(cc)

conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個
print("xxxxx new 0717")

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

# 建立一個資料表 table01 + PRIMARY KEY
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
注意：不要使用%s 將字串插入 SQL 命令，
因為它可能使你的程式容易受到 SQL 注入攻擊（請參閱 SQL 注入 ）。
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
新進測試
建立多個表單 要分開寫
"""
print("------------------------------------------------------------")  # 60個

db_filename = "tmp_db_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".sqlite"

print("建立資料庫連線, 資料庫 : " + db_filename)
conn = sqlite3.connect(db_filename)  # 建立資料庫連線

cursor = conn.cursor()  # 建立 cursor 物件

# 建立一個資料表 table01 + 如果尚未建立的話 + PRIMARY KEY
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

# 建立一個資料表 table01 + PRIMARY KEY
sqlstr = """
    CREATE TABLE table01 (
    id serial NOT NULL,
    uid character varying(50) NOT NULL,
    PRIMARY KEY (id));
"""
cursor.execute(sqlstr)

# 建立一個資料表 table02 + PRIMARY KEY
sqlstr = """
    CREATE TABLE table02 (
    id serial NOT NULL,
    uid character varying(50) NOT NULL,
    PRIMARY KEY (id));
"""
cursor.execute(sqlstr)

# 建立一個資料表 table03 + PRIMARY KEY
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

# 建立一個資料表 students2 + PRIMARY KEY
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

# 建立一個資料表 users1 + PRIMARY KEY
sqlstr = """
    CREATE TABLE users1 (
    id serial NOT NULL,
    uid character varying(50) NOT NULL,
    question character varying(250) NOT NULL,
    PRIMARY KEY (id))
"""
cursor.execute(sqlstr)

# 建立一個資料表 login + PRIMARY KEY
sqlstr = """
    CREATE TABLE login (
    id serial NOT NULL,
    uid character varying(50) NOT NULL,
    state character varying(10) NOT NULL,
    PRIMARY KEY (id))
"""
cursor.execute(sqlstr)

# 建立一個資料表 users2 + PRIMARY KEY
sqlstr = """
    CREATE TABLE users2 (
    id serial NOT NULL,
    uid character varying(50) NOT NULL,
    state character varying(10) NOT NULL,
    digit3 character varying(10) NOT NULL,
    PRIMARY KEY (id))
"""
cursor.execute(sqlstr)

# 建立一個資料表 setting + PRIMARY KEY
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
print("------------------------------------------------------------")  # 60個

"""
新進測試
建立多個表單 要分開寫
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

''' CREATE + PK
# 建立一個資料表 student2 + PRIMARY KEY
sql = """CREATE TABLE student2(  
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        gender TEXT)"""
'''

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" INSERT
conn = sqlite3.connect("tmp_myInfo.db")     # 資料庫連線
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
print("------------------------------------------------------------")  # 60個

# INSERT

conn = sqlite3.connect("tmp_myInfo2.db")  # 資料庫連線

n_name = "david"
n_gender = "M"
x = (n_name, n_gender)
sql = """insert into student2(name, gender) values(?,?)"""
conn.execute(sql, x)
conn.commit()  # 更新資料庫

conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

conn = sqlite3.connect("tmp_myInfo.db")  # 資料庫連線
results = conn.execute("SELECT * from students")
for record in results:
    print("id = ", record[0])
    print("name = ", record[1])
    print("gender = ", record[2])
conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

conn = sqlite3.connect("tmp_myInfo2.db")  # 資料庫連線
results = conn.execute("SELECT * from student2")
for record in results:
    print("id = ", record[0])
    print("name = ", record[1])
    print("gender = ", record[2])
conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

conn = sqlite3.connect("tmp_myInfo.db")  # 資料庫連線
results = conn.execute("SELECT * from students")
allstudents = results.fetchall()  # 結果轉成元素是元組的串列
for student in allstudents:
    print(student)
conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

conn = sqlite3.connect("tmp_myInfo.db")  # 資料庫連線
results = conn.execute("SELECT name from students")
allstudents = results.fetchall()  # 結果轉成元素是元組的串列
for student in allstudents:
    print(student)
conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

conn = sqlite3.connect("tmp_myInfo.db")  # 資料庫連線
sql = '''SELECT name, gender
        from students
        where gender = "F"'''
results = conn.execute(sql)
allstudents = results.fetchall()  # 結果轉成元素是元組的串列
for student in allstudents:
    print(student)
conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

conn = sqlite3.connect("tmp_myInfo.db")  # 資料庫連線
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
print("------------------------------------------------------------")  # 60個

conn = sqlite3.connect("tmp_myInfo.db")  # 資料庫連線
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
print("------------------------------------------------------------")  # 60個

db_filename = "tmp_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".sqlite"

conn = sqlite3.connect(db_filename)  # 資料庫連線

sql = """CREATE TABLE population( 
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
print("------------------------------------------------------------")  # 60個

conn = sqlite3.connect(db_filename)  # 資料庫連線
results = conn.execute("SELECT * from population")

area, male, female, total = [], [], [], []
for record in results:  # 將人口資料放入串列
    area.append(record[0])
    male.append(record[1])
    female.append(record[2])
    total.append(record[3])
conn.close()  # 關閉資料庫連線

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
print("------------------------------------------------------------")  # 60個

try:
    # 嘗試連接到資料庫
    conn = sqlite3.connect("tmp_example.db")
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
print("------------------------------------------------------------")  # 60個

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
print("------------------------------------------------------------")  # 60個

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
print("讀取資料庫的所有資料")

conn = sqlite3.connect("singMatch.db")  # 連線資料庫

print("編號\t姓名\t音色50\t技巧30\t儀態20\t總分")
sql = "SELECT 參賽者.編號,參賽者.姓名,音色.音色50, \
       技巧.技巧30,儀態.儀態20 from 參賽者 \
       INNER JOIN 音色 ON 音色.編號 = 參賽者.編號 \
       INNER JOIN 技巧 ON 技巧.編號 = 參賽者.編號 \
       INNER JOIN 儀態 ON 儀態.編號 = 參賽者.編號"
result = conn.execute(sql)  # 執行SQL指令
for r in result:
    tot = r[2] + r[3] + r[4]
    print("%d\t%s\t%d\t%d\t%d\t%d" % (r[0], r[1], r[2], r[3], r[4], tot))

conn.close()  # 關閉資料庫

print("------------------------------")  # 30個

"""
#delete.py

conn = sqlite3.connect('singMatch.db') 	# 連線資料庫
selId = int(input('請輸入要移除的 編號 : '))
sql = 'DELETE FROM 參賽者 WHERE 編號 = {0}'.format(selId)
conn.execute(sql)                      	# 執行SQL指令
print('編號 = {0} 的記錄 已經刪除....'.format(selId))
conn.commit()                           # 更新資料庫
conn.close()  

print("------------------------------")  # 30個

#insert01.py

conn = sqlite3.connect('singMatch.db')  # 連線資料庫
print ('請輸入「參賽者」資料表的記錄資料')
again = 'y'
while again.lower() == 'y':
    newId = int(input('編號 : '))
    newName = input('姓名 : ')
    newSex = input('性別 : ')
    newTel = input('電話 : ')
    record = (newId, newName, newSex, newTel)
    sql = 'INSERT INTO 參賽者 VALUES(?,?,?,?)'
    conn.execute(sql,record)           # 執行SQL指令
    conn.commit()                      # 更新資料庫
    again = input('是否繼續輸入資料 ? ')
conn.close()                          # 關閉資料庫

print("------------------------------")  # 30個

#insert02.py

conn = sqlite3.connect('singMatch.db')    	# 連線資料庫

# 建立一個資料表 音色 + 如果尚未建立的話
sql1 = 'CREATE TABLE IF NOT EXISTS 音色( \
        編號 INTEGER UNIQUE NOT NULL, \
        音色50 INTEGER)'
conn.execute(sql1)                         	# 執行SQL指令

print ('請輸入「音色」資料表的記錄資料')
again = 'y'
while again.lower() == 'y':
    newId = int(input('編號 : '))
    newScore = int(input('音色50 : '))
    record = (newId, newScore)
    sql2 = 'INSERT INTO 音色 VALUES(?,?)'
    conn.execute(sql2,record)
    conn.commit()
    again = input('是否繼續輸入資料 ? ')
conn.close()

print("------------------------------")  # 30個

#insert03.py

conn = sqlite3.connect('singMatch.db')    	# 連線資料庫

# 建立一個資料表 技巧 + 如果尚未建立的話
sql1 = 'CREATE TABLE IF NOT EXISTS 技巧( \
         編號 INTEGER UNIQUE NOT NULL, \
         技巧30 INTEGER)'
conn.execute(sql1)                         	# 執行SQL指令

print ('請輸入「技巧」資料表的記錄資料')
again = 'y'
while again.lower() == 'y':
    newId = int(input('編號 : '))
    newScore = int(input('技巧30 : '))
    record = (newId, newScore)
    sql2 = 'INSERT INTO 技巧 VALUES(?,?)'
    conn.execute(sql2,record)
    conn.commit()
    again = input('是否繼續輸入資料 ? ')
conn.close()

print("------------------------------")  # 30個

#insert04.py

conn = sqlite3.connect('singMatch.db')    	# 連線資料庫

# 建立一個資料表 儀態 + 如果尚未建立的話
sql1 = 'CREATE TABLE IF NOT EXISTS 儀態( \
         編號 INTEGER UNIQUE NOT NULL, \
         儀態20 INTEGER)'
conn.execute(sql1)                         	# 執行SQL指令

print ('請輸入「儀態」資料表的記錄資料')
again = 'y'
while again.lower() == 'y':
    newId = int(input('編號 : '))
    newScore = int(input('儀態20 : '))
    record = (newId, newScore)
    sql2 = 'INSERT INTO 儀態 VALUES(?,?)'
    conn.execute(sql2,record)
    conn.commit()
    again = input('是否繼續輸入資料 ? ')
conn.close()
"""
print("------------------------------")  # 30個

# match.py


def fnCreateTable():
    # 建立一個資料表 參賽者 + 如果尚未建立的話
    sql1 = "CREATE TABLE IF NOT EXISTS 參賽者( \
            編號 INTEGER UNIQUE NOT NULL, \
            姓名 TEXT, \
            性別 TEXT, \
            電話 TEXT)"
    conn.execute(sql1)

    # 建立一個資料表 音色 + 如果尚未建立的話
    sql2 = "CREATE TABLE IF NOT EXISTS 音色( \
            編號 INTEGER UNIQUE NOT NULL, \
            音色50 INTEGER)"
    conn.execute(sql2)

    # 建立一個資料表 技巧 + 如果尚未建立的話
    sql3 = "CREATE TABLE IF NOT EXISTS 技巧( \
            編號 INTEGER UNIQUE NOT NULL, \
            技巧30 INTEGER)"
    conn.execute(sql3)

    # 建立一個資料表 儀態 + 如果尚未建立的話
    sql4 = "CREATE TABLE IF NOT EXISTS 儀態( \
            編號 INTEGER UNIQUE NOT NULL, \
            儀態20 INTEGER)"
    conn.execute(sql4)

    anykey = input("請按 <enter>鍵 繼續...")


def fnInsert01():
    print("\n請輸入「參賽者」資料表的記錄資料")
    again = "y"
    while again.lower() == "y":
        newId = int(input("編號 : "))
        newName = input("姓名 : ")
        newSex = input("性別 : ")
        newTel = input("電話 : ")
        record = (newId, newName, newSex, newTel)
        sql = "INSERT INTO 參賽者 VALUES(?,?,?,?)"
        conn.execute(sql, record)
        conn.commit()
        again = input("是否繼續輸入資料 ? ")


def fnSelect01():
    sql = "SELECT * FROM 參賽者"
    data = conn.execute(sql)
    print("編號\t姓名\t性別\t電話")
    for rec in data:
        print("%d\t%s\t%s\t%s" % (rec[0], rec[1], rec[2], rec[3]))
    anykey = input("請按 <enter>鍵 繼續...")


def fnDelect01():
    delId = int(input("請輸入要刪除的參賽者編號: "))
    sql = "DELETE FROM 參賽者 WHERE 編號 = {0}".format(delId)
    conn.execute(sql)
    conn.commit()
    anykey = input("請按 <enter>鍵 繼續...")


def fnInsert02():
    print("\n請輸入「音色」資料表的記錄資料")
    again = "y"
    while again.lower() == "y":
        newId = int(input("編號 : "))
        newScore = int(input("音色50 : "))
        record = (newId, newScore)
        sql = "INSERT INTO 音色 VALUES(?,?)"
        conn.execute(sql, record)
        conn.commit()
        again = input("是否繼續輸入資料 ? ")


def fnSelect02():
    sql = "SELECT * FROM 音色"
    data = conn.execute(sql)
    print("編號\t音色50")
    for rec in data:
        print("%d\t%d" % (rec[0], rec[1]))
    anykey = input("請按 <enter>鍵 繼續...")


def fnDelect02():
    delId = int(input("請輸入要刪除的音色編號: "))
    sql = "DELETE FROM 音色 WHERE 編號 = {0}".format(delId)
    conn.execute(sql)
    conn.commit()
    anykey = input("請按 <enter>鍵 繼續...")


def fnInsert03():
    print("\n請輸入「技巧」資料表的記錄資料")
    again = "y"
    while again.lower() == "y":
        newId = int(input("編號 : "))
        newScore = int(input("技巧30 : "))
        record = (newId, newScore)
        sql = "INSERT INTO 技巧 VALUES(?,?)"
        conn.execute(sql, record)
        conn.commit()
        again = input("是否繼續輸入資料 ? ")


def fnSelect03():
    sql = "SELECT * FROM 技巧"
    data = conn.execute(sql)
    print("編號\t技巧30")
    for rec in data:
        print("%d\t%d" % (rec[0], rec[1]))
    anykey = input("請按 <enter>鍵 繼續...")


def fnDelect03():
    delId = int(input("請輸入要刪除的技巧編號: "))
    sql = "DELETE FROM 技巧 WHERE 編號 = {0}".format(delId)
    conn.execute(sql)
    conn.commit()
    anykey = input("請按 <enter>鍵 繼續...")


def fnInsert04():
    print("\n請輸入「儀態」資料表的記錄資料")
    again = "y"
    while again.lower() == "y":
        newId = int(input("編號 : "))
        newScore = int(input("儀態20 : "))
        record = (newId, newScore)
        sql = "INSERT INTO 儀態 VALUES(?,?)"
        conn.execute(sql, record)
        conn.commit()
        again = input("是否繼續輸入資料 ? ")


def fnSelect04():
    sql = "SELECT * FROM 儀態"
    data = conn.execute(sql)
    print("編號\t儀態20")
    for rec in data:
        print("%d\t%d" % (rec[0], rec[1]))
    anykey = input("請按 <enter>鍵 繼續...")


def fnDelect04():
    delId = int(input("請輸入要刪除的儀態編號: "))
    sql = "DELETE FROM 儀態 WHERE 編號 = {0}".format(delId)
    conn.execute(sql)
    conn.commit()
    anykey = input("請按 <enter>鍵 繼續...")


def fnRelation():
    print("編號\t姓名\t音色50\t技巧30\t儀態20\t總分")
    sql = "SELECT 參賽者.編號,參賽者.姓名,音色.音色50, \
           技巧.技巧30,儀態.儀態20 from 參賽者 \
           INNER JOIN 音色 ON 音色.編號 = 參賽者.編號 \
           INNER JOIN 技巧 ON 技巧.編號 = 參賽者.編號 \
           INNER JOIN 儀態 ON 儀態.編號 = 參賽者.編號"
    result = conn.execute(sql)
    for r in result:
        tot = r[2] + r[3] + r[4]
        print("%d\t%s\t%d\t%d\t%d\t%d" % (r[0], r[1], r[2], r[3], r[4], tot))
    anykey = input("請按 <enter>鍵 繼續...")


#####  主程式  #####
conn = sqlite3.connect("singMatch.db")  # 連線資料庫
while True:
    print("\n*** 博碩歌唱比賽評分管理系統 ***")
    print("    1. 建立資料表")
    print("    2. 管理 參賽者 資料表")
    print("    3. 管理 音色 資料表")
    print("    4. 管理 技巧 資料表")
    print("    5. 管理 儀態 資料表")
    print("    6. 顯示 比賽總成績")
    print("    7. 離開系統")
    print("===========================")
    n = input("請選擇操作項目: ")

    if n == "1":
        fnCreateTable()
    elif n == "2":
        while True:
            print("\n** 管理 參賽者 資料表 **")
            print("   1. 新增記錄")
            print("   2. 查詢記錄")
            print("   3. 刪除記錄")
            print("   4. 回上一層操作")
            print("-------------------------")
            n2 = int(input("請選擇管理項目: "))
            if n2 == 1:
                fnInsert01()
            elif n2 == 2:
                fnSelect01()
            elif n2 == 3:
                fnDelect01()
            elif n2 == 4:
                break
    elif n == "3":
        while True:
            print("\n** 管理 音色 資料表 **")
            print("   1. 新增記錄")
            print("   2. 查詢記錄")
            print("   3. 刪除記錄")
            print("   4. 回上一層操作")
            print("-------------------------")
            n3 = int(input("請選擇管理項目: "))
            if n3 == 1:
                fnInsert02()
            elif n3 == 2:
                fnSelect02()
            elif n3 == 3:
                fnDelect02()
            elif n3 == 4:
                break
    elif n == "4":
        while True:
            print("\n** 管理 技巧 資料表 **")
            print("   1. 新增記錄")
            print("   2. 查詢記錄")
            print("   3. 刪除記錄")
            print("   4. 回上一層操作")
            print("-------------------------")
            n4 = int(input("請選擇管理項目: "))
            if n4 == 1:
                fnInsert03()
            elif n4 == 2:
                fnSelect03()
            elif n4 == 3:
                fnDelect03()
            elif n4 == 4:
                break
    elif n == "5":
        while True:
            print("\n** 管理 儀態 資料表 **")
            print("   1. 新增記錄")
            print("   2. 查詢記錄")
            print("   3. 刪除記錄")
            print("   4. 回上一層操作")
            print("-------------------------")
            n5 = int(input("請選擇管理項目: "))
            if n5 == 1:
                fnInsert04()
            elif n5 == 2:
                fnSelect04()
            elif n5 == 3:
                fnDelect04()
            elif n5 == 4:
                break
    elif n == "6":
        fnRelation()
    elif n == "7":
        break

conn.close()

print("------------------------------")  # 30個

# relation.py

conn = sqlite3.connect("singMatch.db")  # 連線資料庫

print("編號\t姓名\t音色50\t技巧30\t儀態20\t總分")
sql = "SELECT 參賽者.編號,參賽者.姓名,音色.音色50, \
       技巧.技巧30,儀態.儀態20 from 參賽者 \
       INNER JOIN 音色 ON 音色.編號 = 參賽者.編號 \
       INNER JOIN 技巧 ON 技巧.編號 = 參賽者.編號 \
       INNER JOIN 儀態 ON 儀態.編號 = 參賽者.編號"
result = conn.execute(sql)
for r in result:
    tot = r[2] + r[3] + r[4]
    print("%d\t%s\t%d\t%d\t%d\t%d" % (r[0], r[1], r[2], r[3], r[4], tot))
conn.close()

print("------------------------------")  # 30個

# select01.py

conn = sqlite3.connect("singMatch.db")  # 連線資料庫
sql = "SELECT * FROM 參賽者"
data = conn.execute(sql)  # 執行SQL指令,傳回記錄資料
print("編號\t姓名\t性別\t電話")
for rec in data:
    print("%d\t%s\t%s\t%s" % (rec[0], rec[1], rec[2], rec[3]))
conn.close()  # 關閉資料庫

print("------------------------------")  # 30個

# select02.py

conn = sqlite3.connect("singMatch.db")  # 連線資料庫
sql = "SELECT 姓名,電話 FROM 參賽者"
data = conn.execute(sql)  # 執行SQL指令,傳回記錄資料
print("姓名\t電話")
for rec in data:
    print("%s\t%s" % (rec[0], rec[1]))
conn.close()  # 關閉資料庫

print("------------------------------")  # 30個

# select03.py

conn = sqlite3.connect("singMatch.db")  # 連線資料庫
selId = int(input("請輸入要查詢的 編號 : "))
sql = "SELECT * FROM 參賽者 WHERE 編號 = {0}".format(selId)
data = conn.execute(sql)  # 執行SQL指令,傳回記錄資料
print("編號\t姓名\t性別\t電話")
for rec in data:
    print("%d\t%s\t%s\t%s" % (rec[0], rec[1], rec[2], rec[3]))
conn.close()  # 關閉資料庫

print("------------------------------")  # 30個

# select04.py

conn = sqlite3.connect("singMatch.db")  # 連線資料庫
selName = input("請輸入要查詢的 姓名 : ")
sql = 'SELECT * FROM 參賽者 WHERE 姓名 = "{0}"'.format(selName)
data = conn.execute(sql)  # 執行SQL指令,傳回記錄資料
print("編號\t姓名\t性別\t電話")
for rec in data:
    print("%d\t%s\t%s\t%s" % (rec[0], rec[1], rec[2], rec[3]))
conn.close()  # 關閉資料庫

print("------------------------------")  # 30個

# table.py

conn = sqlite3.connect("singMatch.db")  # 連線資料庫

# 建立一個資料表 參賽者 + 如果尚未建立的話
sql = "CREATE TABLE IF NOT EXISTS 參賽者( \
       編號 INTEGER UNIQUE NOT NULL,\
       姓名 TEXT, \
       性別 TEXT, \
       電話 TEXT)"
conn.execute(sql)  # 執行SQL指令
conn.close()  # 關閉資料庫

print("------------------------------")  # 30個

# update.py

conn = sqlite3.connect("singMatch.db")  # 連線資料庫
selId = int(input("請輸入要異動的 編號 : "))
print("\n選擇要異動的欄位名稱...")
field = input("1.姓名  2.性別  3.電話 ..... ? ")
if field == "1":
    newName = input("姓名 :")
    sql = 'UPDATE 參賽者 \
           SET 姓名 = "{0}" \
           WHERE 編號 = {1}'.format(
        newName, selId
    )
elif field == "2":
    newSex = input("性別 :")
    sql = 'UPDATE 參賽者 \
           SET 性別 = "{0}" \
           WHERE 編號 = {1}'.format(
        newSex, selId
    )
elif field == "3":
    newTel = input("電話 :")
    sql = 'UPDATE 參賽者 \
           SET 電話 = "{0}" \
           WHERE 編號 = {1}'.format(
        newTel, selId
    )

conn.execute(sql)  # 執行SQL指令
conn.commit()  # 更新資料庫
conn.close()  # 關閉資料庫

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

conn = sqlite3.connect("tmp_test.db")
c = conn.cursor()

# 建立一個資料表 TIPS + 如果尚未建立的話
c.execute(
    """CREATE TABLE IF NOT EXISTS TIPS 
       (NAME           TEXT    NOT NULL,
       ADDRESS        CHAR(50),
       BILL         REAL);"""
)  # 創建數據表

c.execute(
    "INSERT INTO TIPS (NAME,ADDRESS,BILL) \
      VALUES ('Zhang', 'Beijing', 1004.00 )"
)
# 向表中輸入數據

cursor = c.execute("SELECT * from TIPS")
for row in cursor:
    print(row)
conn.commit()
conn.close()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("查詢資料庫")
conn = sqlite3.connect("data/Books.sqlite")
# 執行SQL指令SELECT
cursor = conn.execute("SELECT * FROM Books")
# 取出查詢結果的每一筆記錄
print("ID\tTitle\t\t\tPrice")
for row in cursor:
    print(row[0], "\t", row[1], "\t", row[2])
conn.close()  # 關閉資料庫連接

print("------------------------------")  # 30個

print("加入資料庫")

conn = sqlite3.connect("data/Books.sqlite")

new_id = "D0002d"
new_title = "MySQL資料庫系統333"
new_price = "600"

# 建立SQL指令INSERT字串
sql = "INSERT INTO Books (id, title, price) VALUES ('{0}','{1}',{2})"
sql = sql.format(new_id, new_title, new_price)
print(sql)
cursor = conn.execute(sql)  # 執行SQL指令
print(cursor.rowcount)
conn.commit()  # 確認交易
conn.close()  # 關閉資料庫連接

print("------------------------------")  # 30個

print("加入資料庫 字典")

d = {"id": "D0003", "title": "MongoDB資料庫系統", "price": 650}  # 字典

conn = sqlite3.connect("data/Books.sqlite")
# 建立SQL指令INSERT字串
sql = "INSERT INTO Books (id, title, price) VALUES ('{0}','{1}',{2})"
sql = sql.format(d["id"], d["title"], d["price"])
print(sql)
cursor = conn.execute(sql)  # 執行SQL指令
print(cursor.rowcount)
conn.commit()  # 確認交易
conn.close()  # 關閉資料庫連接

print("------------------------------")  # 30個

print("更新資料庫")

conn = sqlite3.connect("data/Books.sqlite")
cursor = conn.cursor()

sql = """UPDATE Books SET price=650 WHERE id='D0002' """

sql2 = """UPDATE Books SET price=700 WHERE id='D0003' """
try:
    cursor.execute(sql)
    cursor.execute(sql2)
    conn.commit()
    print("更新 2 筆記錄...")
except:
    conn.rollback()
    print("更新記錄失敗...")
conn.close()

print("------------------------------")  # 30個

conn = sqlite3.connect("data/Books.sqlite")
cursor = conn.cursor()
sql = "DELETE FROM Books WHERE id='D0002'"
sql2 = "DELETE FROM Books WHERE id='D0003'"
try:
    cursor.execute(sql)
    cursor.execute(sql2)
    conn.commit()
    print("刪除 2 筆記錄...")
except:
    conn.rollback()
    print("刪除記錄失敗...")
conn.close()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("新建資料庫")

conn = sqlite3.connect("tmp_school.db")

cursor = conn.cursor()

# 建立一個資料表 scores + 如果尚未建立的話 + PRIMARY KEY
sqlstr = """CREATE TABLE IF NOT EXISTS scores \
("id"  INTEGER PRIMARY KEY NOT NULL,
 "name"  TEXT NOT NULL,
 "chinese"  INTEGER NOT NULL,
 "english"  INTEGER NOT NULL,
 "math"  INTEGER NOT NULL
 )
"""
cursor.execute(sqlstr)

print("加入資料庫")
cursor.execute('insert into scores values(1, "葉大雄", 65, 62, 40)')
cursor.execute('insert into scores values(2, "陳靜香", 85, 90, 87)')
cursor.execute('insert into scores values(3, "王聰明", 92, 90, 95)')
conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

print("加入資料庫")

conn = sqlite3.connect("tmp_school.db")
# 定義資料串列
datas = [[11, "葉大雄", 65, 62, 40], [12, "陳靜香", 85, 90, 87], [13, "王聰明", 92, 90, 95]]

# 新增資料
for data in datas:
    conn.execute(
        "INSERT INTO scores (id, name, chinese, english, math) VALUES \
                 ({}, '{}', {}, {}, {})".format(
            data[0], data[1], data[2], data[3], data[4]
        )
    )
conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

print("更新資料庫")

conn = sqlite3.connect("tmp_school.db")
# 更新資料
conn.execute("UPDATE scores SET name='{}' WHERE id={}".format("林胖虎", 1))
conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

print("刪除資料庫")

conn = sqlite3.connect("tmp_school.db")
# 刪除資料
conn.execute("DELETE FROM scores WHERE id={}".format(1))
conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

print("查詢資料庫")

# fetchall.py

conn = sqlite3.connect("tmp_school.db")
cursor = conn.execute("select * from scores")
rows = cursor.fetchall()
# 顯示原始資料
print(rows)
# 逐筆顯示資料
for row in rows:
    print(row[0], row[1])
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

print("查詢資料庫")

# fetchone.py

conn = sqlite3.connect("tmp_school.db")
cursor = conn.execute("select * from scores")
row = cursor.fetchone()
print(row[0], row[1])
conn.close()  # 關閉資料庫連線


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("建立資料庫")

name = "david"

connect = sqlite3.connect("tmp_mydatabase.sqlite")  # 與資料庫連線

# 建立一個資料表 mytable + 如果尚未建立的話
sql = 'CREATE TABLE IF NOT EXISTS mytable ("姓名" TEXT, "打卡時間" TEXT)'
connect.execute(sql)  # 執行 SQL 語法

print("加入資料庫")
# 取得現在時間
save_time = datetime.datetime.now().strftime("%Y-%m-%d %H.%M.%S")
# 新增一筆資料的 SQL 語法
sql = f'insert into mytable values("{name}", "{save_time}")'
connect.execute(sql)  # 執行 SQL 語法
connect.commit()  # 更新資料庫
connect.close()  # 關閉資料庫

print("------------------------------")  # 30個

print("讀取資料庫")

connect = sqlite3.connect("tmp_mydatabase.sqlite")  # 與資料庫連線
sql = "select * from mytable"  # 選取資料表中所有資料的 SQL 語法
cursor = connect.execute(sql)  # 執行 SQL 語法得到 cursor 物件
dataset = cursor.fetchall()  # 取得所有資料
print("姓名\t打卡時間")
print("----\t  ----")
for data in dataset:
    print(f"{data[0]}\t{data[1]}")
connect.close()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

conn = sqlite3.connect("tmp_test_aaa.sqlite")  # 建立資料庫連線

# 建立一個資料表 + PRIMARY KEY
sqlstr = """CREATE TABLE "contact" \
("id"  INTEGER PRIMARY KEY NOT NULL,
 "name"  TEXT NOT NULL,
 "tel"  TEXT NOT NULL)
"""
conn.execute(sqlstr)
conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

# fetchall.py

conn = sqlite3.connect("tmp_test_aaa.sqlite")  # 建立資料庫連線
cursor = conn.execute("select * from contact")
rows = cursor.fetchall()
# 顯示原始資料
print(rows)
# 逐筆顯示資料
for row in rows:
    print(row[0], row[1])
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

# fetchone.py

conn = sqlite3.connect("data/test_bbb.sqlite")  # 建立資料庫連線
cursor = conn.execute("select * from contact")
row = cursor.fetchone()
print(row[0], row[1])

conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

# sqlite_crud2.py

conn = sqlite3.connect("tmp_test_aaa.sqlite")  # 建立資料庫連線
# 定義資料串列
datas = [
    [1, "David", "02-123456789"],
    [2, "Lily", "02-987654321"],
]
for data in datas:
    # 新增資料
    conn.execute(
        "INSERT INTO contact (id, name, tel) VALUES \
                 ({}, '{}', '{}')".format(
            data[0], data[1], data[2]
        )
    )
conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

# sqlite_crud3.py

conn = sqlite3.connect("tmp_test_aaa.sqlite")  # 建立資料庫連線
# 更新資料
conn.execute("UPDATE contact SET name='{}' WHERE id={}".format("Ken", 1))
conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

# sqlite_crud4.py

conn = sqlite3.connect("tmp_test_aaa.sqlite")  # 建立資料庫連線
# 刪除資料
conn.execute("DELETE FROM contact WHERE id={}".format(1))
conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

# sqlite_cursor.py

conn = sqlite3.connect("tmp_test_aaa.sqlite")  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

# 建立一個資料表 table01 + 如果尚未建立的話 + PRIMARY KEY
sqlstr = """CREATE TABLE IF NOT EXISTS table01 \
("id"  INTEGER PRIMARY KEY NOT NULL,
 "name"  TEXT NOT NULL,
 "tel"  TEXT NOT NULL)
"""
cursor.execute(sqlstr)

# 新增一筆記錄
sqlstr = 'insert into table01 values(1, "David", "02-1234567")'
cursor.execute(sqlstr)
conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

def db_operation():
    db = sqlite3.connect("tmp_database.db")
    c = db.cursor()
    c.execute("create table portfolio (symbol text, shares integer, price real)")
    db.commit()

    stocks = [
        ("GOOG", 100, 490.1),
        ("AAPL", 50, 545.75),
        ("FB", 150, 7.45),
        ("HPQ", 75, 33.2),
    ]
    c.executemany("insert into portfolio values (?,?,?)", stocks)
    db.commit()

    for row in db.execute("select * from portfolio"):
        print(row)

    min_price = 12
    for row in db.execute("select * from portfolio where price >= ?", (min_price,)):
        print(row)


if __name__ == "__main__":
    db_operation()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("新建資料庫")

conn = sqlite3.connect("tmp_database111.sqlite")
cur = conn.cursor()  # 獲得資料庫游標, 'GBK')

# 建立一個資料表 message_board + 如果尚未建立的話
creat_sql = 'create table if not exists message_board ("title" TEXT, "username" TEXT, "email" TEXT, "message_text" TEXT, "date" TEXT)'
conn.execute(creat_sql)

print("加入資料庫")

name = "david"
mail = "david@lion.mouse"
site = "MacOS"
message = "delicious"
time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
cur.execute(
    "INSERT INTO message_board VALUES(?,?,?,?,?)", (name, mail, site, message, time)
)

con = sqlite3.connect("tmp_database111.sqlite")  # 連線到資料庫
cur = con.cursor()  # 獲得資料庫游標, 'GBK')
cur.execute("select * from message_board")  # 執行SQL敘述
results = cur.fetchall()  # 獲得資料

for result in results:
    print(result)

cur.close()  # 關閉游標
con.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個

print("讀取資料庫")

conn = sqlite3.connect("tmp_database111.sqlite")

# 建立一個資料表 message_board + 如果尚未建立的話
creat_sql = 'create table if not exists message_board ("title" TEXT, "username" TEXT, "email" TEXT, "message_text" TEXT, "date" TEXT)'
conn.execute(creat_sql)

read_sql = "select * from message_board"
read_data = conn.execute(read_sql)
dataset = read_data.fetchall()

conn.close()
print(dataset)

print("------------------------------------------------------------")  # 60個

"""
print('加入資料庫')
connect.execute("INSERT INTO message_board (title, username, email, message_text, date) VALUES (?, ?, ?, ?, DATETIME('now'))",
                (title, username, email, message_text))

print('讀取資料庫')

def sqlite_read():
    conn = sqlite3.connect('tmp_database111.sqlite')
    # 建立一個資料表 message_board + 如果尚未建立的話
    creat_sql = 'create table if not exists message_board ("title" TEXT, "username" TEXT, "email" TEXT, "message_text" TEXT, "date" TEXT)'
    conn.execute(creat_sql)
    read_sql = 'select * from message_board'
    read_data = conn.execute(read_sql)
    dataset = read_data.fetchall()
    conn.close()
    return list(dataset)

"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------")  # 30個




