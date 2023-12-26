# ch29_22.py
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










