# ch11_3_1.py
import sqlite3
conn = sqlite3.connect("myInfo2.db")    # 資料庫連線
sql = '''Create table student2(  
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        gender TEXT)'''
conn.execute(sql)                       # 執行SQL指令
conn.close()                            # 關閉資料庫連線












