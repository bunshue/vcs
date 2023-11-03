import sqlite3

# 建立資料庫連接
conn = sqlite3.connect("Books.sqlite")
cursor = conn.cursor()
sql = "DELETE FROM Books WHERE id='D0002'"
sql2 = "DELETE FROM Books WHERE id='D0003'"
try:
    cursor.execute(sql) 
    cursor.execute(sql2)
    conn.commit()
    print("刪除 2 筆記錄...")
except:
    conn.rollback()
    print("刪除記錄失敗...")
conn.close() 

