import sqlite3
conn = sqlite3.connect('school.db') # 建立資料庫連線
cursor = conn.execute('select * from scores')
rows = cursor.fetchall()
# 顯示原始資料
print(rows)
# 逐筆顯示資料
for row in rows:
    print(row[0],row[1])
conn.close()  # 關閉資料庫連線