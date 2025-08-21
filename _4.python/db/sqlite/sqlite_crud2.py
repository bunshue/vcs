"""
sqlite基本範例 其他
"""

# 同一個資料庫內 可以放多個table table名稱不同即可

"""
MySQL將每個資料庫稱為schema

MySQL主要DataType
BOOLEAN
INT
TYNYINT         -128 ~ 127
CHAR(字數)      字串
VARCHAR(字數)   字串
TEXT            字串
NUMERIC         數值
DOUBLE
FLOAT
DECIMAL
SERIAL          序列
DATE
TIME
TIMESTAMP       時間戳
DATETIME
INTERVAL        間隔
GEOMETRY        經緯度

關鍵字        用全大寫
自定義的變數  用小寫加底線

TableName
表格名稱

ColumnName    DataType
欄名      

SELECT 陳述式 FROM 陳述式

取得
SELECT * FROM 哪裏;   取得所有資料

      A,B,C,D
SELECT 什麼 FROM 哪裏;
       欄名      表格名稱


SELECT 什麼 FROM 哪裏 WHERE 條件; (可用邏輯運算子做組合條件)
       欄名      表格名稱


SELECT * FROM customer WHERE birthday < '1990-01-01';

SELECT 什麼 FROM 哪裏 ORDER BY 什麼 ASC;
      欄名      表格名稱       欄名,排列方法
以升冪排序 ASC(預設)
以降冪排序 DESC

限制讀取個數
SELECT 什麼 FROM 哪裏 LIMIT 10         #只讀前10筆
SELECT * FROM titles LIMIT 3, 5        #從第3筆開始讀5筆資料(從0起算)
SELECT * FROM titles LIMIT 5 OFFSET 3  #讀5筆資料出來, 從第3筆開始讀 (從0起算)'

SQL之資料一定要'方正' ???    不一定
sqlite試用一下輸入NULL 或是用'' ""即可  不一定

"""

"""
增刪查改（英語：CRUD），全稱
增加（CREATE，意為「建立」）、
刪除（DELETE）、
查詢（Read，意為「讀取」）、
改正（UPDATE，意為「更新」），
在電腦程式語言中是一連串常見的動作行為，
"""

print("------------------------------------------------------------")  # 60個

import time
import sqlite3

db_filename = (
    "C:/_git/vcs/_1.data/______test_files2/ddb_"
    + time.strftime("%Y%m%d_%H%M%S", time.localtime())
    + ".b.sqlite"
)

# print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename)  # 建立資料庫連線

cursor = conn.cursor()  # 建立 cursor 物件

print("建立表單")
cursor.execute(
    "CREATE TABLE table01" "(" "   filename VARCHAR(32)," "   filesize VARCHAR(32)" ")"
)


print("INSERT")
cursor.execute(
    "INSERT INTO table01" "  (filename, filesize)" "  VALUES" "  (?, ?)",
    ("aaaa.mp4", "12345"),
)


print("SELECT")
cursor.execute("SELECT * FROM table01" "  WHERE filename = ?", ("aaaa.mp4",))

print("Fetchall")
rows = cursor.fetchall()
if len(rows) > 1:
    print(rows)

"""    
    # Nope.  Someone else got there.  Remove our lock.
    cursor.execute("DELETE FROM table01"
                   "  WHERE filename = ?",
                   (self.filename,))
    self.connection.commit()  # 更新
else:
    # Yup.  We're done, so go home.
    return
else:
"""

"""
print('SELECT')
cursor.execute("SELECT * FROM table01"
               "  WHERE filename = ?",
               (self.filename,))
rows = cursor.fetchall()
if len(rows) == 1:
    print('aaaaaa')

print('DELETE')
cursor.execute("DELETE FROM table01"
               "  WHERE filename = ?",
               ('aaaa.mp4',))
"""
conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個


def disp_data():
    return
    print("顯示所有資料")
    cursor = conn.execute("SELECT * FROM password")
    print("帳號\t密碼")
    print("================")
    for row in cursor:
        print("{}\t{}".format(row[0], row[1]))


import sqlite3

db_filename = "C:/_git/vcs/_1.data/______test_files1/_db/python02.sqlite"

conn = sqlite3.connect(db_filename)

disp_data()

print("新增資料")

new_name = "John"
sqlstr = "SELECT * FROM password WHERE name = '{}'".format(new_name)  # 一定要符合大小寫
# sqlstr = "SELECT * FROM password WHERE name LIKE '{}'".format(new_name) #大小寫皆可

cursor = conn.execute(sqlstr)
row = cursor.fetchone()

if not row == None:
    print("{} 帳號已存在!".format(new_name), "無法再新增")
else:
    new_password = "12345678"
    sqlstr = "INSERT INTO password VALUES('{}', '{}');".format(new_name, new_password)
    conn.execute(sqlstr)
    conn.commit()
    print("資料 {} 已儲存完畢".format(new_name))

disp_data()

print("修改資料")

old_name = "David"
sqlstr = "SELECT * FROM password WHERE name = '{}'".format(old_name)
cursor = conn.execute(sqlstr)
row = cursor.fetchone()
# print(row)
if row == None:
    print("{} 帳號不存在!".format(old_name), "無法修改資料")
else:
    print("原來密碼為：{}".format(row[1]))
    new_password = "abcdefg"
    sqlstr = "UPDATE password SET pass = '{}' WHERE name = '{}'".format(
        new_password, old_name
    )
    conn.execute(sqlstr)
    conn.commit()
    print("資料 {} 已修改完成".format(old_name))

disp_data()

print("刪除資料")
name = "John"
sqlstr = "SELECT * FROM password WHERE name = '{}'".format(name)
cursor = conn.execute(sqlstr)
row = cursor.fetchone()
if row == None:
    print("{} 帳號不存在!".format(name), "無法刪除資料")
else:
    sqlstr = "DELETE FROM password WHERE name = '{}'".format(name)
    conn.execute(sqlstr)
    conn.commit()
    print("刪除{}的資料!：".format(name), "已完成")

disp_data()

conn.close()

print("------------------------------------------------------------")  # 60個

print("測試 例外 的寫法")

import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE table01 (id INTEGER PRIMARY KEY, name VARCHAR UNIQUE)")

with conn:
    conn.execute("INSERT INTO table01(name) VALUES (?)", ("David",))
    conn.execute("INSERT INTO table01(name) VALUES (?)", ("Lion",))
    conn.execute("INSERT INTO table01(name) VALUES (?)", ("Mouse",))

try:
    with conn:
        conn.execute("INSERT INTO table01(name) VALUES (?)", ("Lion",))
except sqlite3.IntegrityError:
    print("無法重複輸入相同的資料")

cursor = conn.execute("SELECT * FROM table01")  # SELECT * : 取得所有資料
rows = cursor.fetchall()  # 讀取全部資料
length = len(rows)
print("共有", length, "筆資料")
for i in range(length):
    # print(type(rows[i]))
    print("第" + str(i + 1) + "筆資料 : ", end="")
    print(rows[i])
conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個


print("測試 TIMESTAMP")


import sqlite3

import datetime

con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("CREATE TABLE table01(my_date DATE, my_timestamp TIMESTAMP)")

today = datetime.date.today()
now = datetime.datetime.now()

cur.execute("INSERT INTO table01(my_date, my_timestamp) VALUES (?, ?)", (today, now))
cur.execute("SELECT my_date, my_timestamp FROM table01")
row = cur.fetchone()
print(today, "=>", row[0], type(row[0]))
print(now, "=>", row[1], type(row[1]))

cur.execute(
    'SELECT current_date as "my_date [date]", current_timestamp as "my_timestamp [timestamp]"'
)
row = cur.fetchone()
print("current_date", row[0], type(row[0]))
print("current_timestamp", row[1], type(row[1]))

print("------------------------------------------------------------")  # 60個

print("測試 xxxx")

import sqlite3

persons = [("Hugo", "Boss"), ("Calvin", "Klein")]

con = sqlite3.connect(":memory:")

# Create the table
con.execute("CREATE TABLE person(firstname, lastname)")

# Fill the table
con.executemany("INSERT INTO person(firstname, lastname) VALUES (?, ?)", persons)

# Print the table contents
for row in con.execute("SELECT firstname, lastname FROM person"):
    print(row)

print("I just deleted", con.execute("DELETE FROM person").rowcount, "rows")


print("------------------------------------------------------------")  # 60個


print("測試 xxxx")


print("程式執行完畢！")


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
