# ch36_5.py
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent,TextMessage,TextSendMessage,ImageSendMessage

app = Flask(__name__)

handler = WebhookHandler('9df449a13001ff8ab66b1a087fd49d3b')
line_bot_api = LineBotApi('3ToyZz4q3dUa6oNL3d8v/aq0hGFzbqocA1OU5n2f7o9qaZs4PaDGAjD7QPCDajyArmoBdNtpHAARL/hADZZ69Ns2YgZRmKLeSyAddO/+FIoTfKEQosbGKABgsjF9SVUXUjG91M0qvu3/PSbUl43bfAdB04t89/1O/w1cDnyilFU=')

# 收 Line 訊息
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return "OK"

# 設計回應程式
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if isinstance(event.message, TextMessage):
        msg = event.message.text
        if msg =="南極旅遊":
            fig_url = "https://aaa.24ht.com.tw/travel.jpg"
            line_bot_api.reply_message(event.reply_token,
                ImageSendMessage(original_content_url=fig_url,
                                 preview_image_url=fig_url))
        if msg == "客服中心":
            txt = "歡迎使用客服\n請聯繫我\n0800-000-000"
            line_bot_api.reply_message(event.reply_token,
                               TextSendMessage(text=txt))

if __name__ == "__main__":
    app.run()





