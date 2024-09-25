from flask import Flask
 
app = Flask(__name__)

@app.route("/")
def main():
    return "Hello World!"

@app.route("/callback")
def callback():
    return "Callback"

@app.route("/user/<username>")
def user(username):
    return "使用者名稱: " + str(username)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
   



#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch16\ch16-3.py

from flask import Flask, jsonify
 
app = Flask(__name__)

@app.route("/")
def main():
    return jsonify({"name": "Joe Chen",
                    "email": "hueyan@ms2.hinet.net"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch16\ch16-3a.py

from bs4 import BeautifulSoup
import requests
from flask import Flask, jsonify
 
url = "https://ifoodie.tw/explore/台北市/list?sortby=rating"

def getTop(limit=5):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    item_lst = soup.find("div", class_="item-list")
    items = item_lst.find_all("div",class_="restaurant-item",limit=limit)
    outputs = []
    for item in items:
        title = item.find("a", class_="title-text")
        title_txt = title.text if title else "N/A"
        address = item.find("div", class_="address-row") 
        address_txt = address.text if address else "N/A"
        price = item.find("div", class_="avg-price")
        price_txt = price.text[2:] if price else "N/A"
        result = { "title":   title_txt, 
                   "address": address_txt,
                   "price":   price_txt }
        outputs.append(result)        
    return outputs

app = Flask(__name__)
@app.route("/")
def main():
    return jsonify(getTop(5))
@app.route("/top/<limit>")
def top(limit):
    return jsonify(getTop(int(limit)))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch16\ch16-4.py

from flask import Flask,request,abort
from linebot import LineBotApi,WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent,TextMessage,TextSendMessage

channel_token  = "<Channel access token>"
channel_secret = "<Channel secret>"

app = Flask(__name__)
line_bot_api = LineBotApi(channel_token)
handler = WebhookHandler(channel_secret)

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
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))
    
if __name__ == "__main__":
    app.run(port=8080)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch16\ch16-4a.py

from bs4 import BeautifulSoup
import requests
from flask import Flask,request,abort
from linebot import LineBotApi,WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent,TextMessage,TextSendMessage

channel_token  = "<Channel access token>"
channel_secret = "<Channel secret>"
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
line_bot_api = LineBotApi(channel_token)
handler = WebhookHandler(channel_secret)

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
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text
    if "美食" in text or "food" in text or "Food" in text:
        reply_msg = getTop(3)
    else:
        reply_msg = text 
    line_bot_api.reply_message(event.reply_token,
                        TextSendMessage(text=reply_msg))

if __name__ == "__main__":
    app.run(port=8080)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch16\ch16-5.py

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

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch16\ch16-5a.py

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

print("------------------------------------------------------------")  # 60個

