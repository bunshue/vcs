import mysql.connector

conn = mysql.connector.connect(
    host='localhost', port='3306', user='DevAuth', password='Dev127336', database='DevDb')

cursor = conn.cursor()


appDesc = """
Please input action code :

1 - Insert Data
2 - Update Data
3 - Delect Date
--- --- ---
0 - exit

"""
isRun = True

while(isRun):
    sql = "select * from app_info;"
    cursor.execute(sql)
    records = cursor.fetchall()
    for r in records:
        print(r)

    ctrl = input(appDesc)

    if ctrl == "0":
        isRun = False
    elif ctrl == "1":
        sql = """
        INSERT INTO app_info (name, version, author, `date`, remark)
        VALUES('App', '1.0.1', 'DevAuth', '2021-01-01', 'App-v1.0.1');
        """
        cursor.execute(sql)
        conn.commit()
    elif ctrl == "2":
        row_id = input("row_id = ? ")
        sql = """
        update app_info
        set name = 'AppNew' , version='1.0.2' , remark = 'App-v1.0.2' 
        WHERE id={};
        """.format(row_id)
        cursor.execute(sql)
        conn.commit()
    elif ctrl == "3":
        row_id = input("row_id = ? ")
        sql = """
        delete from app_info
        where id={};
        """.format(row_id)
        cursor.execute(sql)
        conn.commit()


cursor.close()
conn.close()
