import sqlite3                             	# 匯入sqlite3套件
conn = sqlite3.connect('singMatch.db')    	# 連線資料庫
sql1 = 'CREATE TABLE IF NOT EXISTS 音色( \
        編號 INTEGER UNIQUE NOT NULL, \
        音色50 INTEGER)'
conn.execute(sql1)                         	# 執行SQL指令

print ('請輸入「音色」資料表的記錄資料')
again = 'y'
while again.lower() == 'y':
    newId = int(input('編號 : '))
    newScore = int(input('音色50 : '))
    record = (newId, newScore)
    sql2 = 'INSERT INTO 音色 VALUES(?,?)'
    conn.execute(sql2,record)
    conn.commit()
    again = input('是否繼續輸入資料 ? ')
conn.close()