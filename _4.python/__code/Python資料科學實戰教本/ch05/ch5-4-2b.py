import pymysql

d = {
   "id": "P0005",
   "title": "Android程式設計",
   "author": "陳會安",
   "price": 650,
   "cat": "程式設計",
   "date": "2019-02-01"
}

db = pymysql.connect(host="localhost",user="root",password="",database="mybook",charset="utf8")
cursor = db.cursor()
sql = """INSERT INTO book (id,title,author,price,category,pubdate)
         VALUES ('{0}','{1}','{2}',{3},'{4}','{5}')"""
sql = sql.format(d['id'],d['title'],d['author'],d['price'],d['cat'],d['date'])
print(sql)
try:
    cursor.execute(sql) 
    db.commit()
    print("新增一筆記錄...")
except:
    db.rollback()
    print("新增記錄失敗...")
db.close() 
