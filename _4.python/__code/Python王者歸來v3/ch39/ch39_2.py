# ch39_2.py
from flask import Flask, request, abort
import os
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import openai

app = Flask(__name__)

# 設定Line API & Webhook
line_bot_api = LineBotApi(os.getenv('Channel_token'))
handler = WebhookHandler(os.getenv('Channel_secret'))

# 設定OpenAI API
openai.api_key = os.getenv('OpenAI_key')

# 收Line 訊息
@app.route("/", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    return 'OK'

# 使用OpenAI回應Line訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_input = event.message.text

    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role":"system", "content":"你是深智公司客服人員"},
                    {"role":"user", "content":user_input}],
        max_tokens = 150     # 限制回應token數  
    )
    
    response = response.choices[0].message['content']

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=response.strip().replace('\n','')))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
