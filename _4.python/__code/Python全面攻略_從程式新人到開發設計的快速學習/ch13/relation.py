import sqlite3                             	# 匯入sqlite3套件
conn = sqlite3.connect('singMatch.db')    	# 連線資料庫

print ('編號\t姓名\t音色50\t技巧30\t儀態20\t總分')
sql = 'SELECT 參賽者.編號,參賽者.姓名,音色.音色50, \
       技巧.技巧30,儀態.儀態20 from 參賽者 \
       INNER JOIN 音色 ON 音色.編號 = 參賽者.編號 \
       INNER JOIN 技巧 ON 技巧.編號 = 參賽者.編號 \
       INNER JOIN 儀態 ON 儀態.編號 = 參賽者.編號'
result = conn.execute(sql)
for r in result:
    tot = r[2] + r[3] + r[4]
    print('%d\t%s\t%d\t%d\t%d\t%d' %(r[0],r[1],r[2],r[3],r[4],tot))
conn.close()