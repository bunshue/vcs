import sqlite3                          # 匯入sqlite3套件
conn = sqlite3.connect('singMatch.db')  # 連線資料庫
selName = input('請輸入要查詢的 姓名 : ')
sql = 'SELECT * FROM 參賽者 WHERE 姓名 = "{0}"'.format(selName)
data = conn.execute(sql)                # 執行SQL指令,傳回記錄資料
print('編號\t姓名\t性別\t電話')
for rec in data:
    print('%d\t%s\t%s\t%s' %(rec[0],rec[1],rec[2],rec[3]))
conn.close()                          # 關閉資料庫