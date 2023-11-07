import sqlite3


def db_check(db):
    try:
        connect = sqlite3.connect(db)   # 與資料庫連線
        sql = 'select * from mytable'   # 選取資料表中所有資料的 SQL 語法
        cursor = connect.execute(sql)   # 執行 SQL 語法得到 cursor 物件
        dataset = cursor.fetchall()     # 取得所有資料
        print('姓名\t打卡時間')
        print('----\t  ----')
        for data in dataset:
            print(f"{data[0]}\t{data[1]}")
    except:
        print('讀取資料庫錯誤')
    connect.close()

    #---------------------------#
db_check('mydatabase.sqlite')
