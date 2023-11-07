from flask import Flask  # 匯入 Flask 類別
app = Flask(__name__)  # 透過 Flask 類別建立一個物件


@app.route('/')
def hello():
    return 'Hello Flask!'


if __name__ == '__main__':
    app.run()
    print('網站已結束')
