import sqlite3

book = "D0002,MySQL資料庫系統,600"
f = book.split(",")

# 建立資料庫連接
conn = sqlite3.connect("Books.sqlite")
# 建立SQL指令INSERT字串
sql = "INSERT INTO Books (id, title, price) VALUES ('{0}','{1}',{2})"
sql = sql.format(f[0], f[1], f[2])
print(sql)
cursor = conn.execute(sql)   # 執行SQL指令
print(cursor.rowcount)
conn.commit() # 確認交易
conn.close()  # 關閉資料庫連接

