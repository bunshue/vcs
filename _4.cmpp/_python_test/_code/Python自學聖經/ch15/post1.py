from flask import Flask
from flask import request
app = Flask(__name__)

from flask import render_template
@app.route('/post1')
def post1():
    return render_template('post1.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.values['username']
    password = request.values['password']
    if username=='david' and password=='1234':
        return '歡迎光臨本網站！'
    else:
        return '帳號或密碼錯誤！'

if __name__ == '__main__':
    app.run()
