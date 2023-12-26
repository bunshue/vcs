# ch41_2.py
import pymysql
conn = pymysql.connect('localhost', port=3306, user='root',
		      password='hung', charset='utf8', db='mydb')


with conn.cursor() as cursor:
    sql = """
    CREATE TABLE IF NOT EXISTS Scores (
        ID int NOT NULL AUTO_INCREMENT PRIMARY KEY,
        Name varchar(20),
        Math int(3),
        Eng int(3)
    )
    """

    cursor.execute(sql)
    conn.commit()
conn.close()

