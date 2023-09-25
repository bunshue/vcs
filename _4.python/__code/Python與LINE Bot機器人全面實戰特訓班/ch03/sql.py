from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:123456@127.0.0.1:5432/testdb'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return "資料庫連線成功！"

@app.route('/setup')
def setup():
    sql = """
    CREATE TABLE students2 (
    sid serial NOT NULL,
    name character varying(50) NOT NULL,
    tel character varying(50),
    addr character varying(200),
    email character varying(100),
    PRIMARY KEY (sid))
    """
    db.engine.execute(sql)
    return "資料表建立成功！"

@app.route('/insert')
def insert():
    sql = """
    INSERT INTO students2 (name, tel, addr, email) VALUES('炭治郎', '0911111111', '台北市信義路101號', 'tjl@test.com');
    INSERT INTO students2 (name, tel, addr, email) VALUES('彌豆子', '0922222222', '台北市南京東路50號', 'mdj@test.com');
    INSERT INTO students2 (name, tel, addr, email) VALUES('伊之助', '0933333333', '台北市北門路20號', 'yjj@test.com');
    """
    db.engine.execute(sql)
    return "資料新增成功！"

@app.route('/query')
def query():
    sql = "SELECT * FROM students2 ORDER BY sid"
    students = db.engine.execute(sql)
    msg = ""
    for student in students:
        msg += f"{student['name']}, {student['tel']}, {student['addr']}, {student['email']}<br>"
    return msg

@app.route('/updateusr/<int:uid>')
def updateusr(uid):
    sql = "UPDATE students2 SET name = '炭之郎' WHERE sid = " + str(uid)
    db.engine.execute(sql)
    return "資料修改成功！"

@app.route('/deleusr/<int:uid>')
def deleusr(uid):
    sql = "DELETE FROM students2 WHERE sid = " + str(uid)
    db.engine.execute(sql)
    return "資料刪除成功！"

if __name__ == '__main__':
   app.run(debug=True)