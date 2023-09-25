from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://管理者名稱:管理者密碼@127.0.0.1:5432/NTUHQA'
db = SQLAlchemy(app)

@app.route('/')
def index():
    sql = """
    CREATE TABLE users (
    id serial NOT NULL,
    uid character varying(50) NOT NULL,
    question character varying(250) NOT NULL,
    PRIMARY KEY (id))
    """
    db.engine.execute(sql)
    return "資料表建立成功！"

if __name__ == '__main__':
   app.run(debug=True)