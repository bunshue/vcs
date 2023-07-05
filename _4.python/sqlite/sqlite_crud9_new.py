'''

新進測試

'''

#----------------------------------------------------------------

print('新進測試')

import sqlite3

db_filename  = 'ims_sql/db_ims.sqlite'
db_filename = 'C:/_git/vcs/_1.data/______test_files1/_db/gasoline.sqlite'
#db_filename  = 'db_20230703_113217.sqlite'

print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename) # 建立資料庫連線

print('要事先能知道表單的名稱 prices 與 各欄位的名稱 gdate')

cursor = conn.execute('SELECT * FROM prices ORDER BY gdate DESC;')

n = 0
for row in cursor:
    print(row)
    print("日期：{}，92無鉛：{}，95無鉛：{}，98無鉛：{}". format(row[0], row[1], row[2], row[3]))
    n = n + 1
    #讀取10筆資料, 即跳出
    if n == 10:
        break

conn.close()  # 關閉資料庫連線

print("程式執行完畢！")

