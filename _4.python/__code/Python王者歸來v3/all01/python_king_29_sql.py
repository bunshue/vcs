import sys

import sqlite3

conn = sqlite3.connect("myData.db")
conn.close()

print("------------------------------------------------------------")  # 60個

import sqlite3
conn = sqlite3.connect("data29_2.db")   # 資料庫連線
cursor = conn.cursor()
sql = '''Create table students(  
        id int,
        name text,
        gender text)'''
cursor.execute(sql)                     # 執行SQL指令
cursor.close()                          # 關閉
conn.close()                            # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個

import sqlite3
conn = sqlite3.connect("myInfo.db")     # 資料庫連線
sql = '''Create table students(  
        id int,
        name text,
        gender text)'''
conn.execute(sql)                       # 執行SQL指令
conn.close()                            # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個

import sqlite3
conn = sqlite3.connect("myInfo2.db")    # 資料庫連線
sql = '''Create table student2(  
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        gender TEXT)'''
conn.execute(sql)                       # 執行SQL指令
conn.close()                            # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個

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

print("------------------------------------------------------------")  # 60個

import sqlite3
conn = sqlite3.connect("myInfo2.db")     # 資料庫連線
print("請輸入myInfo資料庫student2表單資料")
while True:
    n_name = input("請輸入name : ")
    n_gender = input("請輸入gender : ")
    x = (n_name, n_gender)
    sql = '''insert into student2(name, gender) values(?,?)'''  
    conn.execute(sql,x)
    conn.commit()                       # 更新資料庫
    again = input("繼續(y/n)? ")
    if again[0].lower() == "n":
        break
conn.close()                            # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個

import sqlite3
conn = sqlite3.connect("myInfo.db")     # 資料庫連線
results = conn.execute("SELECT * from students")
for record in results:
    print("id = ", record[0])
    print("name = ", record[1])
    print("gender = ", record[2])
conn.close()                            # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個

import sqlite3
conn = sqlite3.connect("myInfo2.db")     # 資料庫連線
results = conn.execute("SELECT * from student2")
for record in results:
    print("id = ", record[0])
    print("name = ", record[1])
    print("gender = ", record[2])
conn.close()                            # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個

import sqlite3
conn = sqlite3.connect("myInfo.db")     # 資料庫連線
results = conn.execute("SELECT * from students")
allstudents = results.fetchall()        # 結果轉成元素是元組的串列
for student in allstudents:
    print(student)
conn.close()                            # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個

import sqlite3
conn = sqlite3.connect("myInfo.db")     # 資料庫連線
results = conn.execute("SELECT name from students")
allstudents = results.fetchall()        # 結果轉成元素是元組的串列
for student in allstudents:
    print(student)
conn.close()                            # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個

import sqlite3
conn = sqlite3.connect("myInfo.db")     # 資料庫連線
sql = '''SELECT name, gender
        from students
        where gender = "F"'''
results = conn.execute(sql)
allstudents = results.fetchall()        # 結果轉成元素是元組的串列
for student in allstudents:
    print(student)
conn.close()                            # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個

import sqlite3
conn = sqlite3.connect("myInfo.db")     # 資料庫連線
sql = '''UPDATE students
        set name = "Tomy"
        where id = 1'''
results = conn.execute(sql)
conn.commit()                           # 更新資料庫
results = conn.execute("SELECT name from students")
allstudents = results.fetchall()        # 結果轉成元素是元組的串列
for student in allstudents:
    print(student)
conn.close()                            # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個

import sqlite3
conn = sqlite3.connect("myInfo.db")     # 資料庫連線
sql = '''DELETE
        from students
        where id = 2'''
results = conn.execute(sql)
conn.commit()                           # 更新資料庫
results = conn.execute("SELECT name from students")
allstudents = results.fetchall()        # 結果轉成元素是元組的串列
for student in allstudents:
    print(student)
conn.close()                            # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個

import sqlite3
import csv
import matplotlib.pyplot as plt

conn = sqlite3.connect("populations.db")    # 資料庫連線
sql = '''Create table population( 
        area TEXT,
        male int,                     
        female int,
        total int)'''
conn.execute(sql)                           # 執行SQL指令

fn = 'Taipei_Population.csv'
with open(fn) as csvFile:                   # 儲存在SQLite
    csvReader = csv.reader(csvFile)
    listCsv = list(csvReader)               # 轉成串列
    csvData = listCsv[4:]                   # 切片刪除前4 rows
    for row in csvData:
        area = row[0]                       # 區名稱
        male = int(row[7])                  # 男性人數
        female = int(row[8])                # 女性人數
        total = int(row[6])                 # 總人數
        x = (area, male, female, total)
        sql = '''insert into population values(?,?,?,?)'''
        conn.execute(sql,x)
        conn.commit()

results = conn.execute("SELECT * from population")
for record in results:
    print("區域       = ", record[0])
    print("男性人口數 = ", record[1])
    print("女性人口數 = ", record[2])
    print("總計人口數 = ", record[3])
       
conn.close()                                # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個

import sqlite3
import matplotlib.pyplot as plt
from pylab import mpl

conn = sqlite3.connect("populations.db")    # 資料庫連線
results = conn.execute("SELECT * from population")

area, male, female, total = [], [], [], []
for record in results:                      # 將人口資料放入串列
    area.append(record[0])
    male.append(record[1])
    female.append(record[2])
    total.append(record[3])       
conn.close()                                # 關閉資料庫連線

mpl.rcParams["font.sans-serif"] = ["SimHei"]        # 使用黑體
seq = area
linemale, = plt.plot(seq, male, '-*', label='男性人口數')
linefemale, = plt.plot(seq, female, '-o', label='女性人口數')
linetotal, = plt.plot(seq, total, '-^', label='總計人口數')

plt.legend(handles=[linemale, linefemale, linetotal], loc='best')
plt.title(u"台北市", fontsize=24)
plt.xlabel("2019年", fontsize=14)
plt.ylabel("人口數", fontsize=14)
plt.show()

print("------------------------------------------------------------")  # 60個

import pymysql
conn = pymysql.connect(host = 'localhost',
                       port = 3306,
                       user = 'root',
                       charset = 'utf8',
		       password = 'hung')

mycursor = conn.cursor()
mycursor.execute("CREATE DATABASE mydb2")

print("------------------------------------------------------------")  # 60個

import pymysql
conn = pymysql.connect(host = 'localhost',
                       port = 3306,
                       user = 'root',
                       charset = 'utf8',
		       password = 'hung',
                       database = 'mydb1')

mycursor = conn.cursor()

sql = """
CREATE TABLE IF NOT EXISTS Customers (
    ID int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Name varchar(20),
    City varchar(20)
)"""
mycursor.execute(sql)

print("------------------------------------------------------------")  # 60個

import pymysql
conn = pymysql.connect(host = 'localhost',
                       port = 3306,
                       user = 'root',
                       charset = 'utf8',
		       password = 'hung',
                       database = 'mydb1')

mycursor = conn.cursor()

sql = "INSERT INTO customers (Name, City)  VALUES (%s, %s)"
val = ("Peter", "Taipei")

mycursor.execute(sql, val)
conn.commit()           # 執行插入
print(f"插入資料錄 {mycursor.rowcount} 筆")

print("------------------------------------------------------------")  # 60個

import pymysql
conn = pymysql.connect(host = 'localhost',
                       port = 3306,
                       user = 'root',
                       charset = 'utf8',
		       password = 'hung',
                       database = 'mydb1')

mycursor = conn.cursor()

sql = "INSERT INTO customers (Name, City)  VALUES (%s, %s)"
val = [("Kevin", "Taipei"),
       ("John", "Tokyo"),
       ("Nancy", "Beijing")
      ]

mycursor.executemany(sql, val)
conn.commit()           # 執行插入
print(f"插入資料錄 {mycursor.rowcount} 筆")

print("------------------------------------------------------------")  # 60個

import pymysql
conn = pymysql.connect(host = 'localhost',
                       port = 3306,
                       user = 'root',
                       charset = 'utf8',
		       password = 'hung',
                       database = 'mydb1')

mycursor = conn.cursor()

mycursor.execute("SELECT * FROM customers")
result = mycursor.fetchall()
for r in result:
    print(r)

print("------------------------------------------------------------")  # 60個

import pymysql
conn = pymysql.connect(host = 'localhost',
                       port = 3306,
                       user = 'root',
                       charset = 'utf8',
		       password = 'hung',
                       database = 'mydb1')

mycursor = conn.cursor()

mycursor.execute("SELECT * FROM customers")
result = mycursor.fetchone()
print(result)

print("------------------------------------------------------------")  # 60個

import pymysql
conn = pymysql.connect(host = 'localhost',
                       port = 3306,
                       user = 'root',
                       charset = 'utf8',
		       password = 'hung',
                       database = 'mydb1')

mycursor = conn.cursor()

mycursor.execute("SELECT * FROM customers WHERE City = 'Taipei'")
result = mycursor.fetchall()
for r in result:
    print(r)

print("------------------------------------------------------------")  # 60個

import pymysql
conn = pymysql.connect(host = 'localhost',
                       port = 3306,
                       user = 'root',
                       charset = 'utf8',
		       password = 'hung',
                       database = 'mydb1')

mycursor = conn.cursor()

sql = "UPDATE customers SET City = 'Chicago' WHERE City = 'Tokyo'"
mycursor.execute(sql)
conn.commit()

mycursor.execute("SELECT * FROM customers")
result = mycursor.fetchall()
for r in result:
    print(r)

print("------------------------------------------------------------")  # 60個

import pymysql
conn = pymysql.connect(host = 'localhost',
                       port = 3306,
                       user = 'root',
                       charset = 'utf8',
		       password = 'hung',
                       database = 'mydb1')

mycursor = conn.cursor()

sql = "UPDATE customers SET City = 'New Taipei' WHERE id = 2"
mycursor.execute(sql)
conn.commit()

mycursor.execute("SELECT * FROM customers")
result = mycursor.fetchall()
for r in result:
    print(r)

print("------------------------------------------------------------")  # 60個

import pymysql
conn = pymysql.connect(host = 'localhost',
                       port = 3306,
                       user = 'root',
                       charset = 'utf8',
		       password = 'hung',
                       database = 'mydb1')

mycursor = conn.cursor()

sql = "DELETE from customers WHERE id = 2"
mycursor.execute(sql)
conn.commit()

mycursor.execute("SELECT * FROM customers")
result = mycursor.fetchall()
for r in result:
    print(r)

print("------------------------------------------------------------")  # 60個

import pymysql
conn = pymysql.connect(host = 'localhost',
                       port = 3306,
                       user = 'root',
                       charset = 'utf8',
		       password = 'hung',
                       database = 'mydb1')

mycursor = conn.cursor()

mycursor.execute("SELECT * FROM customers LIMIT 2")
result = mycursor.fetchall()
for r in result:
    print(r)

print("------------------------------------------------------------")  # 60個

import pymysql
conn = pymysql.connect(host = 'localhost',
                       port = 3306,
                       user = 'root',
                       charset = 'utf8',
		       password = 'hung',
                       database = 'mydb1')

mycursor = conn.cursor()
sql = "DROP TABLE IF EXISTS customers"
mycursor.execute(sql)

print("------------------------------------------------------------")  # 60個
