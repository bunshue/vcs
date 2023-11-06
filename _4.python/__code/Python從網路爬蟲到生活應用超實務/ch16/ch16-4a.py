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