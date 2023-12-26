# ch29_13.py
import pymysql
conn = pymysql.connect(host = 'localhost',
                       port = 3306,
                       user = 'root',
                       charset = 'utf8',
		       password = 'hung')

mycursor = conn.cursor()
mycursor.execute("CREATE DATABASE mydb2")



