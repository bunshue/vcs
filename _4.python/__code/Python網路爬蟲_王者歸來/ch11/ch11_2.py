# ch11_2.py
import sqlite3
conn = sqlite3.connect("data11_2.db")   # 資料庫連線
cursor = conn.cursor()
sql = '''Create table students(  
        id int,
        name text,
        gender text)'''
cursor.execute(sql)                     # 執行SQL指令
cursor.close()                          # 關閉
conn.close()                            # 關閉資料庫連線












