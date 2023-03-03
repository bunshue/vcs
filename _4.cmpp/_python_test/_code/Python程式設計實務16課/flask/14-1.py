# 程式14-1 (Python 3 version)

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '歡迎光臨，您好！'

@app.route('/about')
def about():
    return '這是一個使用Flask建立的小網站測試'

@app.route('/user/<username>')
def show_user(username):
    return 'User Name is {}'.format(username)

if __name__ == '__main__':
    app.run()
