import pymysql

conn = pymysql.connect('localhost',port=3306,user='root',passwd='1234',charset='utf8', db='pythondb')  #連結資料庫
cursor = conn.cursor()

sql1 = "select * from score"  #查詢資料
cursor.execute(sql1)
data = cursor.fetchall()
print('全部資料：')
print(data)

sql2 = "update score set 國文=98 where 座號 = '%s' " % ('4')  #修改資料
cursor.execute(sql2)
cursor.execute(sql1)
data = cursor.fetchall()
print('修改後資料：')
print(data)

sql3 = "delete from score where 座號 = '%s' " % ('6')  #刪除資料
cursor.execute(sql3)
cursor.execute(sql1)
data = cursor.fetchall()
print('刪除後資料：')
print(data)

conn.commit()  #提交資料庫
cursor.close()
conn.close()
