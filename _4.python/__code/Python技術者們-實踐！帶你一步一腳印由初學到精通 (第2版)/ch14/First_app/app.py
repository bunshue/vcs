from flask import Flask, render_template

app = Flask(__name__)


@ app.route('/')
def index():
    introduction = ["旗標科技", "台北市中正區 杭州南路一段15-1號19樓", "service@flag.com.tw"]
    return render_template('index.html', introduction=introduction)


if __name__ == '__main__':
    app.run(debug=True)
