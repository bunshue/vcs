import sqlite3
conn = sqlite3.connect('school.db') # 建立資料庫連線
# 刪除資料
conn.execute("DELETE FROM scores WHERE id={}".format(1))
conn.commit() # 更新
conn.close()  # 關閉資料庫連線