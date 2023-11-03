import sqlite3

# 建立資料庫連接
conn = sqlite3.connect("Books.sqlite")
# 執行SQL指令SELECT
cursor = conn.execute("SELECT * FROM Books")
# 取出查詢結果的每一筆記錄
for row in cursor:
    print(row[0], row[1])
conn.close()  # 關閉資料庫連接
