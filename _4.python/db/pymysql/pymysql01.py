import sys
import pymysql

print("------------------------------------------------------------")  # 60個

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


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



