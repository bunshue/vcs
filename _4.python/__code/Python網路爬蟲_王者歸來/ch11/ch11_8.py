# ch11_8.py
import sqlite3
conn = sqlite3.connect("myInfo.db")     # 資料庫連線
sql = '''SELECT name, gender
        from students
        where gender = "F"'''
results = conn.execute(sql)
allstudents = results.fetchall()        # 結果轉成元素是元組的串列
for student in allstudents:
    print(student)
conn.close()                            # 關閉資料庫連線












