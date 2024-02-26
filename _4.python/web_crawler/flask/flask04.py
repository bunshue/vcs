import sys
import sqlite3

'''
#資料庫 之 資料表 建立一次就好
import time

db_filename = 'db_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.sqlite';

#print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename) # 建立資料庫連線
cursor = conn.cursor() # 建立 cursor 物件

print('建立一個資料表')

#CREATE 建立
#CREATE TABLE table01
#PRIMARY KEY 主鍵
#序號 自動遞增 不可重複

sqlstr = """
CREATE TABLE IF NOT EXISTS table01 (
    id_text  TEXT NOT NULL,
    name  TEXT NOT NULL,
    money INTEGER NOT NULL,
    weight INTEGER NOT NULL CHECK(weight > 0) -- 預設錯誤時會顯示
);
"""

cursor.execute(sqlstr)
conn.commit() # 更新


#db_filename = "my_db.sqlite"

con = sqlite3.connect(db_filename)

print("Opened database successfully")
cur = con.cursor()
data = [("007", "david", 1234, 5678)]
 
cur.executemany("INSERT INTO table01 VALUES(?, ?, ?, ?)", data)
print("Table created successfully")
con.commit()
con.close()


print('------------------------------------------------------------')	#60個

#讀取資料

import sqlite3

#db_filename = "my_db.sqlite"

con = sqlite3.connect(db_filename)
print("Opened database successfully")
cur = con.cursor()
name = 'david'
sql = 'SELECT * FROM table01 WHERE name="%s";'%(name)
cur.execute(sql)
student = cur.fetchone() 
print(student)
con.commit()
con.close()

'''
print('------------------------------------------------------------')	#60個

#http://localhost:3000/?name=david

import sqlite3
from flask import Flask, request

db_filename = "my_db.sqlite"

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        name = request.values['name']
        con = sqlite3.connect(db_filename)
        print("Opened database successfully")
        cur = con.cursor()
        sql = 'SELECT * FROM table01 WHERE name="%s";' % (name)
        cur.execute(sql)
        student = cur.fetchone()
        print(student)
        con.commit()
        con.close()

        if student:
            # http://localhost:3000/?name=oxxo
            return f'歡迎光臨 : {student[1]} , {student[2]} , {student[3]}'
        else:
            #return 'Can not find...'
            return f'找不到使用者'

if __name__ == '__main__':
    app.debug = True
    app.run(port=3000)


print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個





