import pymysql
conn = pymysql.connect('localhost',port=3306,user='root',passwd='1234',charset='utf8', db='pythondb')  #連結資料庫

with conn.cursor() as cursor:
    sql = "select * from scores"
    cursor.execute(sql)
    datas = cursor.fetchall()   # 取出所有資料
    print(datas)
    print('-' * 30)             # 畫分隔線
    sql = "select * from scores"
    cursor.execute(sql)    
    data = cursor.fetchone()    # 取出第一筆資料
    print(data)
    
conn.close()