import sqlite3                             	# 匯入sqlite3套件
conn = sqlite3.connect('singMatch.db')    	# 連線資料庫
sql1 = 'CREATE TABLE IF NOT EXISTS 技巧( \
         編號 INTEGER UNIQUE NOT NULL, \
         技巧30 INTEGER)'
conn.execute(sql1)                         	# 執行SQL指令

print ('請輸入「技巧」資料表的記錄資料')
again = 'y'
while again.lower() == 'y':
    newId = int(input('編號 : '))
    newScore = int(input('技巧30 : '))
    record = (newId, newScore)
    sql2 = 'INSERT INTO 技巧 VALUES(?,?)'
    conn.execute(sql2,record)
    conn.commit()
    again = input('是否繼續輸入資料 ? ')
conn.close()