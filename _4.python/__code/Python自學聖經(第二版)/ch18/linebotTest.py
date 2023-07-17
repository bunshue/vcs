from flask import Flask
app = Flask(__name__)

from flask import request, abort
from linebot import  LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

line_bot_api = LineBotApi('5P6YQbws0M1vMwSq5r0cpGZe1VBJCZX2cT65ywd+6hvsrjXI6gi3Je64Hau6kmTd+AEQL2AGNk3G7nm8Fjw1L/wL9qIDepSTuMV+2OysJRK0hZQRwykaOIeCAgKsdaytNDLWaDVyfVzjsKeQ8HBiMAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('e03713c489707ceac29953031dde79a0')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))

if __name__ == '__main__':
    app.run()
