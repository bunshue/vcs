# ch29_14.py
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


