'''

新進測試
測試 SERIAL 測不出效果

測試 TIMESTAMP
測試 DATE
測試 CHECK

'''

#----------------------------------------------------------------

print('新進測試')

import sqlite3
import datetime

#db_filename  = 'ims_sql/db_ims.sqlite'
#db_filename = 'C:/_git/vcs/_1.data/______test_files1/_db/gasoline.sqlite'
#db_filename  = 'db_20230703_113217.sqlite'
db_filename  = 'sssss4.sqlite'

print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename) # 建立資料庫連線
cursor = conn.cursor() # 建立 cursor 物件

#sqlstr = 'CREATE TABLE IF NOT EXISTS table01 ("id_num" INTEGER PRIMARY KEY NOT NULL, "name"  TEXT NOT NULL, "money"  TEXT NOT NULL, "update_time" TIMESTAMP)'
#sqlstr = 'CREATE TABLE IF NOT EXISTS table01 ("id_num" INTEGER, "name"  TEXT NOT NULL, "money"  TEXT NOT NULL, "update_time" TIMESTAMP)'


sqlstr = '''
CREATE TABLE IF NOT EXISTS table01 (
  id SERIAL PRIMARY KEY,
  name VARCHAR(50),
  birthday DATE CHECK(birthday > '1900-01-01' ),
  work_time DATE CHECK(work_time > birthday),
  money integer CHECK(money > 0) -- 預設錯誤時會顯示
);
'''

cursor.execute(sqlstr)
conn.commit() # 更新

name = 'David'
birthday = '2006-03-11'
work_time = '2023-07-11'
money = 2345
sql = "INSERT INTO table01 (name, birthday, work_time, money) VALUES ('{}', '{}', '{}', {})".format(name, birthday, work_time, money)
print(sql)

#或者直接寫
#sql = "INSERT INTO table01 (name, birthday, work_time, money) VALUES ('Joe', '1980-02-02', '1990-04-04', 1234);"

cursor.execute(sql)

'''
id_num = 3
name = 'David'
money = 333
update_time = datetime.datetime.now()

sqlstr = sql.format(id_num, name, money, update_time)
cursor.execute(sqlstr)
'''

conn.commit() # 更新
conn.close()  # 關閉資料庫連線


conn = sqlite3.connect(db_filename) # 建立資料庫連線

cursor = conn.execute('SELECT * FROM table01')

n = 0
for row in cursor:
    print(row)
    n = n + 1
    #讀取10筆資料, 即跳出

conn.close()  # 關閉資料庫連線




print("程式執行完畢！")

