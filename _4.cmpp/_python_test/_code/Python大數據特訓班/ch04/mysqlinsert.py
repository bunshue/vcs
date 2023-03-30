import pymysql

conn = pymysql.connect('localhost',port=3306,user='root',passwd='1234',charset='utf8', db='pythondb')  #連結資料庫
cursor = conn.cursor()

sql = "insert into score (姓名,座號,國文,數學) values (1,'李大毛','1',92,80)"
cursor.execute(sql)
sql = "insert into score (姓名,座號,國文,數學) values ('林小明','2',83,61)"
cursor.execute(sql)
sql = "insert into score (姓名,座號,國文,數學) values ('黃金龍','4',53,71)"
cursor.execute(sql)
sql = "insert into score (姓名,座號,國文,數學) values ('劉火樹','6',87,89)"
cursor.execute(sql)
sql = "insert into score (姓名,座號,國文,數學) values ('何美麗','7',73,95)"
cursor.execute(sql)

conn.commit()  #提交資料庫
cursor.close()
conn.close()
