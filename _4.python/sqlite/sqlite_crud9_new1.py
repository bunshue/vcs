'''

新進測試

'''

#----------------------------------------------------------------

print('新進測試')

import sqlite3
import datetime

#db_filename  = 'ims_sql/db_ims.sqlite'
#db_filename = 'C:/_git/vcs/_1.data/______test_files1/_db/gasoline.sqlite'
#db_filename  = 'db_20230703_113217.sqlite'
db_filename  = 'ttttq2b.sqlite'

print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename) # 建立資料庫連線
cursor = conn.cursor() # 建立 cursor 物件

#sqlstr = 'CREATE TABLE if not exists table01 ("id_num" INTEGER PRIMARY KEY NOT NULL, "name"  TEXT NOT NULL, "money"  TEXT NOT NULL, "update_time" TIMESTAMP)'
#sqlstr = 'CREATE TABLE if not exists table01 ("id_num" INTEGER, "name"  TEXT NOT NULL, "money"  TEXT NOT NULL, "update_time" TIMESTAMP)'
sqlstr = '''
CREATE TABLE if not exists table01 (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(50),
  birth_date DATE CHECK(birth_date > '1900-01-01' ),
  join_date DATE CHECK(join_date > birth_date),
  salary integer CHECK(salary > 0) -- 預設錯誤時會顯示 new_user_salary_check
);
'''

cursor.execute(sqlstr)
conn.commit() # 更新

#sql = "INSERT INTO table01('id_num', 'name', 'money', 'update_time') values({},'{}','{}','{}');"
sql = "INSERT INTO table01 (first_name, birth_date, join_date, salary) VALUES('Joe', '1980-02-02', '1990-04-04', 1234);"

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

