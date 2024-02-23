import sqlite3
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        name = request.values['name']
        con = sqlite3.connect('sqlite/sq01.db')
        print("Opened database successfully")
        cur = con.cursor()
        sql = 'SELECT * FROM test WHERE name="%s";' % (name)
        cur.execute(sql)
        student = cur.fetchone()
        print(student)
        con.commit()
        con.close()

        if student:
            # http://localhost:3000/?name=oxxo
            return f'Hello {student[1]} , {student[2]} , {student[3]}'
        else:
            return 'Can not find...'


if __name__ == '__main__':
    app.debug = True
    app.run(port=3000)
