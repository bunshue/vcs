from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>')
def hello(name):
    return '{}，歡迎來到 Flask!'.format(name)

if __name__ == '__main__':
    app.run()
