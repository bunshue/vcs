# ch11_6.py
import sqlite3
conn = sqlite3.connect("myInfo.db")     # 資料庫連線
results = conn.execute("SELECT * from students")
allstudents = results.fetchall()        # 結果轉成元素是元組的串列
for student in allstudents:
    print(student)
conn.close()                            # 關閉資料庫連線












