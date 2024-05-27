import sqlite3                          # 匯入sqlite3套件
conn = sqlite3.connect('singMatch.db')  # 連線資料庫
print ('請輸入「參賽者」資料表的記錄資料')
again = 'y'
while again.lower() == 'y':
    newId = int(input('編號 : '))
    newName = input('姓名 : ')
    newSex = input('性別 : ')
    newTel = input('電話 : ')
    record = (newId, newName, newSex, newTel)
    sql = 'INSERT INTO 參賽者 VALUES(?,?,?,?)'
    conn.execute(sql,record)           # 執行SQL指令
    conn.commit()                      # 更新資料庫
    again = input('是否繼續輸入資料 ? ')
conn.close()                          # 關閉資料庫