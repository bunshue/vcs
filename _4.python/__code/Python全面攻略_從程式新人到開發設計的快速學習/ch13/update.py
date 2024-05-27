import sqlite3                         	# 匯入sqlite3套件
conn = sqlite3.connect('singMatch.db') 	# 連線資料庫
selId = int(input('請輸入要異動的 編號 : '))
print('\n選擇要異動的欄位名稱...')
field = input('1.姓名  2.性別  3.電話 ..... ? ')
if field == '1':
    newName = input('姓名 :')
    sql = 'UPDATE 參賽者 \
           SET 姓名 = "{0}" \
           WHERE 編號 = {1}'.format(newName, selId)
elif field == '2':
    newSex = input('性別 :')
    sql = 'UPDATE 參賽者 \
           SET 性別 = "{0}" \
           WHERE 編號 = {1}'.format(newSex, selId)
elif field == '3':
    newTel = input('電話 :')
    sql = 'UPDATE 參賽者 \
           SET 電話 = "{0}" \
           WHERE 編號 = {1}'.format(newTel, selId)
   
conn.execute(sql)                      	# 執行SQL指令
conn.commit()                           # 更新資料庫
conn.close()                           	# 關閉資料庫