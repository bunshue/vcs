from app import app, handler

from flask import request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from linebot.exceptions import InvalidSignatureError

from app.models_for_login import User, users_dict
from app.custom_models import CallDatabase

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    
    使用者 = request.form['user_id']
    if (使用者 in users_dict) and (request.form['password'] == users_dict[使用者]['password']):
        user = User()
        user.id = 使用者
        login_user(user)
        flash(f'{使用者}！歡迎加入草泥馬訓練家的行列！')
        return redirect(url_for('from_start'))

    flash('登入失敗了...')
    return render_template('login.html')

@app.route("/logout")
@login_required
def logout():
    使用者 = current_user.get_id()
    logout_user()
    flash(f'{使用者}！歡迎下次再來！')
    return render_template('login.html')

@app.route("/from_start")
@login_required
def from_start():
    return render_template("from_start.html")

@app.route("/show_records")
@login_required
def show_records():
    dataclip = CallDatabase.web_select_overall()
    return render_template("show_records.html", html_dataclip=dataclip)

@app.route("/select_records", methods=['GET', 'POST'])
@login_required
def select_records():
    if request.method == 'POST':
        print(request.form)
        dataclip = CallDatabase.web_select_specific(request.form)
        return render_template("show_records.html", html_dataclip=dataclip)
    else:
        return render_template("select_records.html")

@app.route("/select_records_comfortable", methods=['GET', 'POST'])
@login_required
def select_records_comfortable():
    if request.method == 'POST':
        print(request.form)
        dataclip = CallDatabase.web_select_specific(request.form)
        return render_template("show_records.html", html_dataclip=dataclip)
    else:
        unique_name = CallDatabase.line_select_distinct('alpaca_name')
        unique_training = CallDatabase.line_select_distinct('training')
        unique_date = CallDatabase.line_select_distinct('date')
        uniques = [unique_name, unique_training, unique_date]
        return render_template("select_records_comfortable.html", uniques=uniques)

# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'