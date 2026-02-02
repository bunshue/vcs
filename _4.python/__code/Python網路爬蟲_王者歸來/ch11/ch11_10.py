# ch11_10.py
import sqlite3
conn = sqlite3.connect("myInfo.db")     # 資料庫連線
sql = '''DELETE
        from students
        where id = 2'''
results = conn.execute(sql)
conn.commit()                           # 更新資料庫
results = conn.execute("SELECT name from students")
allstudents = results.fetchall()        # 結果轉成元素是元組的串列
for student in allstudents:
    print(student)
conn.close()                            # 關閉資料庫連線












