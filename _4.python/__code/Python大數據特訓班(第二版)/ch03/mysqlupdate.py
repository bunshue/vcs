import pymysql
conn = pymysql.connect('localhost',port=3306,user='root',passwd='1234',charset='utf8', db='pythondb')  #連結資料庫

with conn.cursor() as cursor:
    sql = "update scores set Chinese = 98 where ID = 3"
    cursor.execute(sql)
    conn.commit()
    sql = "select * from scores where ID = 3"
    cursor.execute(sql)    
    data = cursor.fetchone()
    print(data)
    
conn.close()