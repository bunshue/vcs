import sqlite3

# 建立資料庫連接
conn = sqlite3.connect("Books.sqlite")
cursor = conn.cursor()
sql = """UPDATE Books SET price=650 
         WHERE id='D0002' """
sql2 = """UPDATE Books SET price=700 
         WHERE id='D0003' """
try:
    cursor.execute(sql) 
    cursor.execute(sql2)
    conn.commit()
    print("更新 2 筆記錄...")
except:
    conn.rollback()
    print("更新記錄失敗...")
conn.close() 
