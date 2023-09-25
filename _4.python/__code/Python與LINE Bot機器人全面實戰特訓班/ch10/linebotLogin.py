from flask import Flask
app = Flask(__name__)

from flask import request, abort
from flask_sqlalchemy import SQLAlchemy
from linebot import  LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

line_bot_api = LineBotApi('你的 CHANNEL_ACCESS_TOKEN')
handler = WebhookHandler('你的 CHANNEL_SECRET')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://管理者名稱:管理者密碼@127.0.0.1:5432/invoice'
db = SQLAlchemy(app)

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    userid = event.source.user_id
    sql_cmd = "select * from login where uid='" + userid + "'"
    query_data = db.engine.execute(sql_cmd)
    datalist = list(query_data)
    if len(datalist) == 0:
        sql_cmd = "insert into login (uid, state) values('" + userid + "', 'no');"
        db.engine.execute(sql_cmd)
        mode = 'no'
    else:
        mode = datalist[0][2]

    mtext = event.message.text
    if mtext == '@請輸入帳號' and mode == 'no':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='請輸入你的帳號：'))
    elif mtext == '@請輸入帳號' and mode == 'login':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='你已輸入帳號，請輸入密碼：'))
    elif mode == 'no':
        if mtext == 'david':
            sql_cmd = "update login set state='login' where uid='" + userid +"'"
            db.engine.execute(sql_cmd)
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='請輸入你的密碼：'))
        else:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='無此帳號！'))
    elif mode == 'login':
        if mtext == '123456':
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='歡迎登入本系統！'))
        else:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='密碼錯誤！'))
        sql_cmd = "update login set state='no' where uid='" + userid +"'"
        db.engine.execute(sql_cmd)

if __name__ == '__main__':
    app.run()
