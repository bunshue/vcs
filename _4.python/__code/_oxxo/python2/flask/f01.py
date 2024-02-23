# 參考 https://hackmd.io/@shaoeChen/SyP4YEnef?type=view
from flask import Flask
app = Flask(__name__)
# 第二行的語法是一個約定俗成的用法，就是這樣，沒有其它的用意，讓 flask 知道 root 在何處!


def text():
    return 'Hello'

@app.route('/', methods=['GET'])
def i0():
    return f'<h1>{text()}!!!</h1>'

# flask 支援的參數型別有四種：str, int, float, path，預設 str
# <int:name>
@app.route('/<name>', methods=['GET'])
def i1(name):
    return f'<h1>{text()} {name}!!!</h1>'


@app.route('/<name>/<age>', methods=['GET'])
def i2(name, age):
    return f'<h1>{text()} {name}!!! ( {age} )</h1>'


app.run(port=3000, debug=True)
