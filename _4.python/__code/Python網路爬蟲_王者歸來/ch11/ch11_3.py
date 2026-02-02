# ch11_3.py
import sqlite3
conn = sqlite3.connect("myInfo.db")     # 資料庫連線
sql = '''Create table students(  
        id int,
        name text,
        gender text)'''
conn.execute(sql)                       # 執行SQL指令
conn.close()                            # 關閉資料庫連線












