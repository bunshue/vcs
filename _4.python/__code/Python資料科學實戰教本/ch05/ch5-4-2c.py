import pymysql

db = pymysql.connect(host="localhost",user="root",password="",database="mybook",charset="utf8")
cursor = db.cursor()
sql = """UPDATE book SET price=500, 
         pubdate='2020/02/01'
         WHERE id='P0004' """
sql2 = """UPDATE book SET price=600, 
         pubdate='2019/03/01'
         WHERE id='P0005' """
try:
    cursor.execute(sql) 
    cursor.execute(sql2)
    db.commit()
    print("更新 2 筆記錄...")
except:
    db.rollback()
    print("更新記錄失敗...")
db.close() 
