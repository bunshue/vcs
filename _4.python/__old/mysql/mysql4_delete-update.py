try:
 import MySQLdb                         # pip install MySQL-python
except:
 import pymysql as MySQLdb             #  pip install MySQLdb

db = MySQLdb.connect(host="127.0.0.1", user="admin", passwd="admin", db="mydatabase")
cursor = db.cursor()

sql="INSERT INTO mytable (value01, value02, value03,value04) VALUES ('1','1','1','1');"
cursor.execute(sql)
db.commit()

sql="UPDATE `mytable` SET `value01`='2' WHERE `value01`='1'"
cursor.execute(sql)
db.commit()

sql="DELETE FROM `mytable` where `value01`='2';"
cursor.execute(sql)
db.commit()

cursor.execute("SELECT * FROM mytable")
result = cursor.fetchall()
for record in result:
    print("value01=%s value02=%s" %(record[0],record[1]))
