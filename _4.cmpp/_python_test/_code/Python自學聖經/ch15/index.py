from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return '這是本網站首頁!'

if __name__ == '__main__':
    app.run()
