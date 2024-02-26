"""
Flask是一個使用Python編寫的輕量級Web應用框架。


https://hackmd.io/@shaoeChen/SyP4YEnef?type=view


"""

import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個

"""
# case 1
# 網址 http://127.0.0.1:5000

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

app.run()
"""


print("------------------------------------------------------------")  # 60個
"""
# case 2
# 網址 http://127.0.0.1:3000

from flask import Flask

app = Flask(__name__)

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
"""
print("------------------------------------------------------------")  # 60個

"""
# case 3
# 網址 http://127.0.0.1:3000

from flask import Flask, url_for, redirect
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
  return 'hello'

@app.route('/<name>', methods=['GET'])
def b(name):
  return redirect(url_for('index')) # 執行參照 index() 路徑要做的事情


@app.route('/<name>/<qq>', methods=['GET'])
def c(name, qq):
  return url_for('index')  # 返回 index() 參照的路徑

app.run(port=3000)

"""
print("------------------------------------------------------------")  # 60個

"""
# case 4
# 網址 http://127.0.0.1:3000

from flask import  Flask, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
  return render_template('test.html') # 預設一定放在 templates 資料夾內

@app.route('/<name>', methods=['GET'])
def i2(name):
  return render_template('test.html', name=name) # 可將參數傳給網頁的 {{name}} 接收

if __name__ == '__main__':
    app.debug = True
    app.run(port=3000)

"""

print("------------------------------------------------------------")  # 60個
"""
# case 5 多了 username
# 網址 http://localhost:3000/?username=david

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST']) 
def login():
    if request.method == 'GET': 
        return 'Hello ' + request.values['username']  # 

if __name__ == '__main__':
    app.debug = True
    app.run(port=3000)
"""
print("------------------------------------------------------------")  # 60個

"""
# case 6
# 網址 http://127.0.0.1:3000

# 參考 http://docs.jinkan.org/docs/jinja2/templates.html#template-inheritance
from flask import  Flask, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
  return render_template('test.html') # 預設一定放在 templates 資料夾內

@app.route('/<name>', methods=['GET'])
def i2(name):
  return render_template('content.html', name=name) # 可將參數傳給網頁的 {{name}} 接收

if __name__ == '__main__':
    app.debug = True
    app.run(port=3000)
"""

print("------------------------------------------------------------")  # 60個

"""
# case 7
# 網址 http://127.0.0.1:3000

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 可接受跨域

@app.route('/', methods=['GET', 'POST'])
def hello():
    a = request.args
    return a


#app.run(port=3000, host='0.0.0.0', debug=True) # host 可以改 ip
app.run(port=3000, debug=True)
"""

print("------------------------------------------------------------")  # 60個

""" fail
# case 8
# 網址 http://127.0.0.1:3000

from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False    # 支援中文


@app.route('/', methods=['GET', 'POST'])
def hello():
    a = request.args
    name = str(request.args['name'])
    url = 'https://mis.twse.com.tw/stock/api/getStockInfo.jsp?ex_ch=tse_'+name+'.tw'
    page = requests.get(url)
    j = json.loads(page.text)
    return j

app.run(port=3000, debug=True)
"""

print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
