import sqlite3                         	# 匯入sqlite3套件
conn = sqlite3.connect('singMatch.db') 	# 連線資料庫
selId = int(input('請輸入要移除的 編號 : '))
sql = 'DELETE FROM 參賽者 WHERE 編號 = {0}'.format(selId)
conn.execute(sql)                      	# 執行SQL指令
print('編號 = {0} 的記錄 已經刪除....'.format(selId))
conn.commit()                           # 更新資料庫
conn.close()  