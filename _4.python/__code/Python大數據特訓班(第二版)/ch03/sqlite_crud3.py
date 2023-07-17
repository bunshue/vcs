import sqlite3
conn = sqlite3.connect('school.db') # 建立資料庫連線
# 更新資料
conn.execute("UPDATE scores SET name='{}' WHERE id={}".format('林胖虎', 1))
conn.commit() # 更新
conn.close()  # 關閉資料庫連線