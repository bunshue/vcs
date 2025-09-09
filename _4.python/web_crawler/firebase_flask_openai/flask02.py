import sys

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





