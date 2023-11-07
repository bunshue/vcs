import sqlite3
from datetime import datetime


def db_save(db, name):
    connect = sqlite3.connect(db)    # 與資料庫連線
    # 新建 mytable 資料表  (如果尚未建立的話)
    sql = 'CREATE TABLE IF NOT EXISTS mytable \
            ("姓名" TEXT, "打卡時間" TEXT)'
    connect.execute(sql)     # 執行 SQL 語法
    # 取得現在時間
    save_time = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
    # 新增一筆資料的 SQL 語法
    sql = f'insert into mytable values("{name}", "{save_time}")'
    connect.execute(sql)         # 執行 SQL 語法
    connect.commit()             # 更新資料庫
    connect.close()              # 關閉資料庫
    print('儲存成功')

    #------------------------------#
db_save('mydatabase.sqlite', '丹丹')
