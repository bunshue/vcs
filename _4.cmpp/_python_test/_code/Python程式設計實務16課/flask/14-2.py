# 程式14-2 (Python 3 version)

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return '歡迎光臨，您好！'

@app.route('/about')
def about():
    return '這是一個使用Flask建立的小網站測試'

@app.route('/user/')
@app.route('/user/<username>')
def show_user(username=None):
    return render_template('show_user.html', name=username)

if __name__ == '__main__':
    app.run()
