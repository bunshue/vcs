from telegram import Bot, Update
from telegram.ext import Dispatcher
from telegram.ext import MessageHandler, Filters
from flask import Flask
from flask import request

token = "<API權杖>"
webhook_URL = "https://8eaa46651097.ngrok.io/callback" 
app = Flask(__name__)

bot = Bot(token)
dispatcher = Dispatcher(bot, None, workers=0)

def echo(update, context):
    text = context.message.text
    bot.send_message(context.message.chat_id, text=text)

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

@app.route("/callback", methods=["POST", "GET"])
def callback():
    if (request.method == "POST") or (request.method == "GET"):
        update = Update.de_json(request.get_json(force=True), bot)
        dispatcher.process_update(update)
        return "OK"
    else:
        return "ERROR"  
@app.route("/setwebhook", methods=["GET", "POST"])
def set_webhook():
    s = bot.setWebhook(webhook_URL)
    if s:
        return "成功完成 Webhook URL 設定:" + webhook_URL
    else:
        return "Webhook URL 設定失敗!"
@app.route("/deletewebhook", methods=["GET", "POST"])
def delete_webhook():
    s = bot.deleteWebhook()
    if s:
        return "成功刪除 Webhook URL 設定!"
    else:
        return "刪除 Webhook URL 設定失敗!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
