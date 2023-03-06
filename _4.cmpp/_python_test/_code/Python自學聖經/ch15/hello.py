from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello():
    return '歡迎來到 Flask!'

if __name__ == '__main__':
    app.run()
