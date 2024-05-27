import sqlite3                             	# 匯入sqlite3套件
conn = sqlite3.connect('singMatch.db')    	# 連線資料庫
sql = 'CREATE TABLE IF NOT EXISTS 參賽者( \
       編號 INTEGER UNIQUE NOT NULL,\
       姓名 TEXT, \
       性別 TEXT, \
       電話 TEXT)'
conn.execute(sql)                          	# 執行SQL指令
conn.close()                               	# 關閉資料庫
