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