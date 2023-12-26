import pymysql
conn = pymysql.connect('localhost', port=3306, user='root',
		      password='hung')


mycursor = conn.cursor()

mycursor.execute("CREATE DATABASE mydatabase")

