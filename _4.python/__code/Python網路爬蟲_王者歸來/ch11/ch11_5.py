# ch11_5.py
import sqlite3
conn = sqlite3.connect("myInfo.db")     # 資料庫連線
results = conn.execute("SELECT * from students")
for record in results:
    print("id = ", record[0])
    print("name = ", record[1])
    print("gender = ", record[2])
conn.close()                            # 關閉資料庫連線












