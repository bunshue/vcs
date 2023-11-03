import pymysql

db = pymysql.connect(host="localhost",user="root",password="",database="mybook",charset="utf8")
cursor = db.cursor()
sql = "DELETE FROM book WHERE id='P0004'"
sql2 = "DELETE FROM book WHERE id='P0005'"
try:
    cursor.execute(sql) 
    cursor.execute(sql2)
    db.commit()
    print("刪除 2 筆記錄...")
except:
    db.rollback()
    print("刪除記錄失敗...")
db.close() 

