# ch29_17.py
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





