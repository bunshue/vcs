import sys
import pymysql

print("------------------------------------------------------------")  # 60個


import csv
import pymysql

conn = pymysql.connect('localhost',port=3306,user='root',passwd='1234',charset='utf8', db='zipcode')  #連結資料庫

with conn.cursor() as cursor:
    sqlstr = """
    CREATE TABLE IF NOT EXISTS zipcode (
      Zip5 char(5) NOT NULL,
      City varchar(10) NOT NULL,
      Area varchar(10) NOT NULL,
      Road varchar(100) NOT NULL,
      Scope varchar(255) NOT NULL
    );    
    """
    cursor.execute(sqlstr)

    with open('data/zipcode.csv', 'r', encoding='utf-8') as f:
        datas = csv.reader(f)
        for data in datas:
            if data != "":
                sqlstr = "insert into zipcode (Zip5, City, Area, Road, Scope) values ('{}', '{}', '{}', '{}', '{}')".format(data[0], data[1], data[2], data[3], data[4])
                cursor.execute(sqlstr)
    conn.commit()
conn.close()             

with open('data/zipcode.csv', 'r', encoding='utf-8') as f:
    datas = csv.reader(f)
    datas.remove(1)
    for data in datas:
        print(data)

import csv
import pymysql

conn = pymysql.connect('localhost', port=3306, user='root', passwd='1234', db='pydata')
cursor = conn.cursor()

try:
    with open('data/711.csv', 'r', newline='') as f:
        datas = csv.reader(f)
        for data in datas:
            sql = "INSERT INTO 711shops(`sid`, `county`, `sname`, `saddress`) VALUES ('{}', '{}', '{}', '{}')".format(data[0],data[1],data[2],data[3])
            cursor.execute(sql)
        conn.commit()
    cursor.close()
    conn.close()
except:
    cursor.close()
    conn.close()

import pymysql
conn = pymysql.connect('localhost',port=3306,user='root',passwd='1234',charset='utf8', db='zipcode')  #連結資料庫

with conn.cursor() as cursor:
    sqlstr = """
    CREATE TABLE IF NOT EXISTS zipcode (
      Zip5 char(5) NOT NULL,
      City varchar(10) NOT NULL,
      Area varchar(10) NOT NULL,
      Road varchar(100) NOT NULL,
      Scope varchar(255) NOT NULL
    );    
    """
    cursor.execute(sqlstr)
    conn.commit()
conn.close()       

import csv
import pymysql

conn = pymysql.connect('localhost',port=3306,user='root',passwd='1234',charset='utf8', db='zipcode')  #連結資料庫

try:
    with conn.cursor() as cursor:
        with open('data/zipcode.csv', 'r', encoding='utf-8') as f:
            datas = csv.reader(f)
            for data in datas:
                if data != "":
                    sqlstr = "insert into zipcode (Zip5, City, Area, Road, Scope) values ('{}', '{}', '{}', '{}', '{}')".format(data[0], data[1], data[2], data[3], data[4])
                    print(sqlstr)
                    cursor.execute(sqlstr)
                    conn.commit()
    conn.close() 
except:
    conn.close()             



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


print("------------------------------------------------------------")  # 60個

