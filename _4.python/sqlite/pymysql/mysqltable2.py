import pymysql

conn = pymysql.connect('localhost',port=3306,user='root',passwd='1234',charset='utf8', db='pythondb')  #連結資料庫
cursor = conn.cursor()

cursor.execute("drop table if exists score")  #如果資料表已經存在,刪除後重建
sql = """
CREATE TABLE score (
sid int not null auto_increment primary key,
姓名 char(20),
座號 char(3),
國文 int,
數學 int
) 
"""
cursor.execute(sql)  #執行SQL指令

conn.commit()  #提交資料庫
cursor.close()
conn.close()
