from bs4 import BeautifulSoup
import requests
from telegram import Bot, Update
from telegram.ext import Dispatcher
from telegram.ext import MessageHandler, Filters
from flask import Flask
from flask import request

token = "<API權杖>"
webhook_URL = "https://212370c3399b.ngrok.io/callback" 
url = "https://ifoodie.tw/explore/台北市/list?sortby=rating"

def getTop(limit=5):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    item_lst = soup.find("div", class_="item-list")
    items = item_lst.find_all("div",class_="restaurant-item",limit=limit)
    output = ""
    index = 1
    for item in items:
        title = item.find("a", class_="title-text")
        title_txt = title.text if title else "N/A"
        address = item.find("div", class_="address-row") 
        address_txt = address.text if address else "N/A"
        price = item.find("div", class_="avg-price")
        price_txt = price.text[2:] if price else "N/A"
        output += str(index) + ": \n名稱: " + title_txt
        output += "\n地址: " + address_txt
        output += "\n價格: " + price_txt
        output += "\n"
        index += 1        
    return output

app = Flask(__name__)

bot = Bot(token)
dispatcher = Dispatcher(bot, None, workers=0)

def handle_msg(update, context):
    text = context.message.text
    if "美食" in text or "food" in text or "Food" in text:
        reply_msg = getTop(3)
    else:
        reply_msg = text
    bot.send_message(context.message.chat_id, text=reply_msg)        

msg_handler = MessageHandler(Filters.text & (~Filters.command), handle_msg)
dispatcher.add_handler(msg_handler)

@app.route("/callback", methods=["POST", "GET"])
def callback():
    if (request.method == "POST") or (request.method == "GET"):
        update = Update.de_json(request.get_json(force=True), bot)
        print(update.message)
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
