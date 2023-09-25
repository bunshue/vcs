from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:123456@127.0.0.1:5432/testdb'
db = SQLAlchemy(app)

class students(db.Model):
   __tablename__ = 'students'
   sid = db.Column(db.Integer, primary_key = True)
   name = db.Column(db.String(50), nullable = False)
   tel = db.Column(db.String(50))
   addr = db.Column(db.String(200))
   email = db.Column(db.String(100))

   def __init__(self, name, tel, addr, email):
       self.name = name
       self.tel = tel
       self.addr = addr
       self.email = email

@app.route('/')
def index():
    db.create_all()
    return "資料庫連線成功！"

if __name__ == '__main__':
   app.run()