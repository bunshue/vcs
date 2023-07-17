import pymysql
conn = pymysql.connect('localhost',port=3306,user='root',passwd='1234',charset='utf8', db='pythondb')  #連結資料庫

with conn.cursor() as cursor:
    sql = """
    insert into scores (Name, Chinese, English, Math) values 
    ('葉大雄',65,62,40),
    ('陳靜香',85,90,87),
    ('王聰明',92,90,95)
    """
    cursor.execute(sql)
    conn.commit()  #提交資料庫
conn.close()