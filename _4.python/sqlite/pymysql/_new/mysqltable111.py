import pymysql
conn = pymysql.connect('localhost',port=3306,user='root',passwd='1234',charset='utf8', db='pythondb')  #連結資料庫

with conn.cursor() as cursor:
    sql = """
    CREATE TABLE IF NOT EXISTS Scores (
      ID int NOT NULL AUTO_INCREMENT PRIMARY KEY,
      Name varchar(20),
      Chinese int(3),
      English int(3),
      Math int(3)
    );
    """
    cursor.execute(sql)  #執行SQL指令
    conn.commit()  #提交資料庫
conn.close()