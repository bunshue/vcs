from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello Flask!'


@app.route('/new', methods=['GET'])  # 新路由
def name():
    return 'Mary!'


if __name__ == '__main__':
    app.run()
