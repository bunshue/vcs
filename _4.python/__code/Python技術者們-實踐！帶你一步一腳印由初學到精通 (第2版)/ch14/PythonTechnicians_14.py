from flask import Flask  # 匯入 Flask 類別
app = Flask(__name__)  # 透過 Flask 類別建立一個物件


@app.route('/')
def hello():
    return 'Hello Flask!'


if __name__ == '__main__':
    app.run()
    print('網站已結束')

print("------------------------------------------------------------")  # 60個


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


print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個

