# encoding:UTF-8
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
