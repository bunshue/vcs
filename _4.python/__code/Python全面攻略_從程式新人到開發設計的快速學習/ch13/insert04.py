import sqlite3                             	# 匯入sqlite3套件
conn = sqlite3.connect('singMatch.db')    	# 連線資料庫
sql1 = 'CREATE TABLE IF NOT EXISTS 儀態( \
         編號 INTEGER UNIQUE NOT NULL, \
         儀態20 INTEGER)'
conn.execute(sql1)                         	# 執行SQL指令

print ('請輸入「儀態」資料表的記錄資料')
again = 'y'
while again.lower() == 'y':
    newId = int(input('編號 : '))
    newScore = int(input('儀態20 : '))
    record = (newId, newScore)
    sql2 = 'INSERT INTO 儀態 VALUES(?,?)'
    conn.execute(sql2,record)
    conn.commit()
    again = input('是否繼續輸入資料 ? ')
conn.close()