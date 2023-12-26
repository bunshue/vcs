# ch36_4.py
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

handler = WebhookHandler('cbb3a72600c7c2944eadeeecd84af849')
line_bot_api = LineBotApi('UreuC7eV1pf1Ky0HO+ykv8sOPg56xv3RXjXS/21sllAtnCkz5gY3Tg3Xk9xgQECLrmoBdNtpHAARL/hADZZ69Ns2YgZRmKLeSyAddO/+FIr/kXk4Du1rd73323Zt17rGw8LUA1Wem+SoOnK+UgrtcwdB04t89/1O/w1cDnyilFU=')

# 收 Line 訊息
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        print(body, signature)
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return "OK"

# Echo 回應, 相當於學你說話
@handler.add(MessageEvent, message=TextMessage)
def echo_message(event):
    line_bot_api.reply_message(event.reply_token,
                               TextSendMessage(text=event.message.text))

if __name__ == "__main__":
    app.run()





