from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy()
POSTGRES = {
    'user': 'admin',
    'password': '123456',
    'db': 'NTUHQA',
    'host': 'localhost',
    'port': '5432',
}
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(password)s@%(host)s:%(port)s/%(db)s' % POSTGRES
db.init_app(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    uid = db.Column(db.String(50),nullable=False)
    question = db.Column(db.String(250),nullable=False)

if __name__ == '__main__':
    app.run()

