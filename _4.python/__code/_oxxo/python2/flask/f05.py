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