import pymysql

book = "P0004,Node.js程式設計,陳會安,550,程式設計,2020-01-01"
f = book.split(",")

db = pymysql.connect(host="localhost",user="root",password="",database="mybook",charset="utf8")
cursor = db.cursor()
sql = """INSERT INTO book (id,title,author,price,category,pubdate)
         VALUES ('{0}','{1}','{2}',{3},'{4}','{5}')"""
sql = sql.format(f[0], f[1], f[2], f[3], f[4], f[5])
print(sql)
try:
    cursor.execute(sql)
    db.commit()
    print("新增一筆記錄...")
except:
    db.rollback() 
    print("新增記錄失敗...")
db.close()

