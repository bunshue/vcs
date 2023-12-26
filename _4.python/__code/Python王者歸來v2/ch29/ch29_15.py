# ch29_15.py
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


