"""
一本精通 - LINE BOT 開發技巧


- [Chapter 03 - 開發環境設定＆串接 LINE BOT](ch3)
- [Chapter 04 - 解析 LINE 訊息](ch4)
- [Chapter 05 - 傳送 LINE 訊息的方法](ch5)
- [Chapter 06 - 傳送不同類型的 LINE 訊息](ch6)
- [Chapter 07 - 實作 LINE 氣象機器人](ch7)
- [Chapter 08 - 串接 Dialogflow 打造聊天機器人](ch8)
- [Chapter 09 - 使用 LINE Notify 推播通知](ch9)
- [Chapter 10 - 使用 Google Clud Functions](ch10)



"""


import os
import sys
import time
import random


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

"""
#檔案 : C:\_git\vcs\_4.python\__code\_oxxo\linebot\ch3\cmd1.txt

from google.colab import drive
drive.mount('/content/drive', force_remount=True)
 
!mkdir -p /drive
!mount --bind /content/drive/My\ Drive /drive
!mkdir -p /drive/ngrok-ssh
!mkdir -p ~/.ssh

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\_oxxo\linebot\ch3\cmd2.txt

!mkdir -p /drive/ngrok-ssh
%cd /drive/ngrok-ssh
!wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip -O ngrok-stable-linux-amd64.zip
!unzip -u ngrok-stable-linux-amd64.zip
!cp /drive/ngrok-ssh/ngrok /ngrok
!chmod +x /ngrok
"""

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\linebot\ch3\code01.py

# Copyright © https://steam.oxxostudio.tw

from flask import Flask

app = Flask(__name__)


@app.route("/<name>")
def home(name):
    return f"<h1>hello {name}</h1>"


app.run()

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\linebot\ch3\code02.py

# Copyright © https://steam.oxxostudio.tw

from flask import Flask, request

# 載入 json 標準函式庫，處理回傳的資料格式
import json

# 載入 LINE Message API 相關函式庫
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)


@app.route("/", methods=["POST"])
def linebot():
    # 取得收到的訊息內容
    body = request.get_data(as_text=True)
    try:
        # json 格式化訊息內容
        json_data = json.loads(body)
        access_token = "你的 LINE Channel access token"
        secret = "你的 LINE Channel secret"
        # 確認 token 是否正確
        line_bot_api = LineBotApi(access_token)
        # 確認 secret 是否正確
        handler = WebhookHandler(secret)
        # 加入回傳的 headers
        signature = request.headers["X-Line-Signature"]
        # 綁定訊息回傳的相關資訊
        handler.handle(body, signature)
        # 取得回傳訊息的 Token
        tk = json_data["events"][0]["replyToken"]
        # 取得 LINe 收到的訊息類型
        type = json_data["events"][0]["message"]["type"]
        if type == "text":
            # 取得 LINE 收到的文字訊息
            msg = json_data["events"][0]["message"]["text"]
            # 印出內容
            print(msg)
            reply = msg
        else:
            reply = "你傳的不是文字呦～"
        print(reply)
        # 回傳訊息
        line_bot_api.reply_message(tk, TextSendMessage(reply))
    except:
        # 如果發生錯誤，印出收到的內容
        print(body)
    # 驗證 Webhook 使用，不能省略
    return "OK"


if __name__ == "__main__":
    app.run()

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\linebot\ch3\code03.py

# Copyright © https://steam.oxxostudio.tw

from flask import Flask
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)


@app.route("/<name>")
def home(name):
    return f"<h1>hello {name}</h1>"


app.run()

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\linebot\ch3\code04.py

# Copyright © https://steam.oxxostudio.tw

from flask_ngrok import run_with_ngrok
from flask import Flask, request

# 載入 LINE Message API 相關函式庫
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

# 載入 json 標準函式庫，處理回傳的資料格式
import json

app = Flask(__name__)


@app.route("/", methods=["POST"])
def linebot():
    # 取得收到的訊息內容
    body = request.get_data(as_text=True)
    try:
        # json 格式化訊息內容
        json_data = json.loads(body)
        access_token = "你的 LINE Channel access token"
        secret = "你的 LINE Channel secret"
        # 確認 token 是否正確
        line_bot_api = LineBotApi(access_token)
        # 確認 secret 是否正確
        handler = WebhookHandler(secret)
        # 加入回傳的 headers
        signature = request.headers["X-Line-Signature"]
        # 綁定訊息回傳的相關資訊
        handler.handle(body, signature)
        # 取得 LINE 收到的文字訊息
        msg = json_data["events"][0]["message"]["text"]
        # 取得回傳訊息的 Token
        tk = json_data["events"][0]["replyToken"]
        # 回傳訊息
        line_bot_api.reply_message(tk, TextSendMessage(msg))
        # 印出內容
        print(msg, tk)
    except:
        # 如果發生錯誤，印出收到的內容
        print(body)
    # 驗證 Webhook 使用，不能省略
    return "OK"


if __name__ == "__main__":
    # 串連 ngrok 服務
    run_with_ngrok(app)
    app.run()

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\linebot\ch3\code05.py

# Copyright © https://steam.oxxostudio.tw

import json
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage


def linebot(request):
    try:
        access_token = "你的 LINE Channel access token"
        secret = "你的 LINE Channel secret"
        body = request.get_data(as_text=True)
        json_data = json.loads(body)
        line_bot_api = LineBotApi(access_token)
        handler = WebhookHandler(secret)
        signature = request.headers["X-Line-Signature"]
        handler.handle(body, signature)
        msg = json_data["events"][0]["message"]["text"]
        tk = json_data["events"][0]["replyToken"]
        line_bot_api.reply_message(tk, TextSendMessage(msg))
        print(msg, tk)
    except:
        print(request.args)
    return "OK"


print("------------------------------------------------------------")  # 60個


# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\linebot\ch4\code01.py

# Copyright © https://steam.oxxostudio.tw

# 如果是本機環境不用 flask_ngrok
from flask_ngrok import run_with_ngrok

from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/", methods=["POST"])
def linebot():
    # 讀取資料 json_data
    body = request.get_data(as_text=True)
    # 轉換成 json 格式 ( 字典格式 )
    json_data = json.loads(body)
    print(json_data)
    return "OK"


if __name__ == "__main__":
    # 如果是本機環境不用 run_with_ngrok(app)
    run_with_ngrok(app)
    app.run()

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\linebot\ch5\code01.py

# Copyright © https://steam.oxxostudio.tw

# Colab 才需要，本機環境請刪除
from flask_ngrok import run_with_ngrok
from flask import Flask, request
from linebot import LineBotApi, WebhookHandler

# 載入 TextSendMessage 模組
from linebot.models import TextSendMessage
import json

app = Flask(__name__)


@app.route("/", methods=["POST"])
def linebot():
    body = request.get_data(as_text=True)
    json_data = json.loads(body)
    print(json_data)
    try:
        line_bot_api = LineBotApi("你的 Channel access token")
        handler = WebhookHandler("你的 LINE Channel secret")
        signature = request.headers["X-Line-Signature"]
        handler.handle(body, signature)
        # 取得 reply token
        tk = json_data["events"][0]["replyToken"]
        # 取得使用者發送的訊息
        msg = json_data["events"][0]["message"]["text"]
        # 設定回傳同樣的訊息
        text_message = TextSendMessage(text=msg)
        # 回傳訊息
        line_bot_api.reply_message(tk, text_message)
    except:
        print("error")
    return "OK"


if __name__ == "__main__":
    # Colab 才需要，本機環境請刪除
    run_with_ngrok(app)
    app.run()

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\linebot\ch5\code02.py

# Copyright © https://steam.oxxostudio.tw

# Colab 才需要，本機環境請刪除
from flask_ngrok import run_with_ngrok
from flask import Flask, request
from linebot import LineBotApi, WebhookHandler

# 載入 StickerSendMessage 模組
from linebot.models import StickerSendMessage
import json

app = Flask(__name__)


@app.route("/", methods=["POST"])
def linebot():
    body = request.get_data(as_text=True)
    json_data = json.loads(body)
    print(json_data)
    try:
        line_bot_api = LineBotApi("你的 Channel access token")
        handler = WebhookHandler("你的 LINE Channel secret")
        signature = request.headers["X-Line-Signature"]
        handler.handle(body, signature)
        # 取得 reply token
        tk = json_data["events"][0]["replyToken"]
        # 取得 stickerId
        stickerId = json_data["events"][0]["message"]["stickerId"]
        # 取得 packageId
        packageId = json_data["events"][0]["message"]["packageId"]
        # 設定要回傳的表情貼圖
        sticker_message = StickerSendMessage(sticker_id=stickerId, package_id=packageId)
        # 回傳訊息
        line_bot_api.reply_message(tk, sticker_message)
    except:
        print("error")
    return "OK"


if __name__ == "__main__":
    # Colab 才需要，本機環境請刪除
    run_with_ngrok(app)
    app.run()

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\linebot\ch5\code03.py

# Copyright © https://steam.oxxostudio.tw

# Colab 才需要，本機環境請刪除
from flask_ngrok import run_with_ngrok
from flask import Flask, request
from linebot import LineBotApi, WebhookHandler

# 載入 TextSendMessage 和 ImageSendMessage 模組
from linebot.models import TextSendMessage, ImageSendMessage
import json

app = Flask(__name__)


@app.route("/", methods=["POST"])
def linebot():
    body = request.get_data(as_text=True)
    json_data = json.loads(body)
    print(json_data)
    try:
        line_bot_api = LineBotApi("你的 Channel access token")
        handler = WebhookHandler("你的 LINE Channel secret")
        signature = request.headers["X-Line-Signature"]
        handler.handle(body, signature)
        tk = json_data["events"][0]["replyToken"]
        msg = json_data["events"][0]["message"]["text"]
        # 取得對應的圖片，如果沒有取得，會是 False
        img_url = reply_img(msg)
        if img_url:
            # 如果有圖片網址，回傳圖片
            img_message = ImageSendMessage(
                original_content_url=img_url, preview_image_url=img_url
            )
            line_bot_api.reply_message(tk, img_message)
        else:
            # 如果是 False，回傳文字
            text_message = TextSendMessage(text="找不到相關圖片")
            line_bot_api.reply_message(tk, text_message)
    except:
        print("error")
    return "OK"


# 建立回覆圖片的函式
def reply_img(text):
    # 文字對應圖片網址的字典
    img = {
        "皮卡丘": "https://upload.wikimedia.org/wikipedia/en/a/a6/Pok%C3%A9mon_Pikachu_art.png",
        "傑尼龜": "https://upload.wikimedia.org/wikipedia/en/5/59/Pok%C3%A9mon_Squirtle_art.png",
    }
    if text in img:
        return img[text]
    else:
        # 如果找不到對應的圖片，回傳 False
        return False


if __name__ == "__main__":
    run_with_ngrok(app)
    app.run()

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\linebot\ch5\code04.py

# Copyright © https://steam.oxxostudio.tw

# Colab 才需要，本機環境請刪除
from flask_ngrok import run_with_ngrok
from flask import Flask, request
from linebot import LineBotApi, WebhookHandler

# 載入 TextSendMessage 和 LocationSendMessage 模組
from linebot.models import TextSendMessage, LocationSendMessage
import json

app = Flask(__name__)


@app.route("/", methods=["POST"])
def linebot():
    body = request.get_data(as_text=True)
    json_data = json.loads(body)
    print(json_data)
    try:
        line_bot_api = LineBotApi("你的 Channel access token")
        handler = WebhookHandler("你的 LINE Channel secret")
        signature = request.headers["X-Line-Signature"]
        handler.handle(body, signature)
        tk = json_data["events"][0]["replyToken"]
        msg = json_data["events"][0]["message"]["text"]
        # 取得對應的地址，如果沒有取得，會是 False
        location_dect = reply_location(msg)
        if location_dect:
            # 如果有地點資訊，回傳地點
            location_message = LocationSendMessage(
                title=location_dect["title"],
                address=location_dect["address"],
                latitude=location_dect["latitude"],
                longitude=location_dect["longitude"],
            )
            line_bot_api.reply_message(tk, location_message)
        else:
            # 如果是 False，回傳文字
            text_message = TextSendMessage(text="找不到相關地點")
            line_bot_api.reply_message(tk, text_message)
    except:
        print("error")
    return "OK"


# 建立回覆地點的函式
def reply_location(text):
    # 建立地點與文字對應的字典
    location = {
        "101": {
            "title": "台北 101",
            "address": "110台北市信義區信義路五段7號",
            "latitude": "25.034095712145003",
            "longitude": "121.56489941996108",
        },
        "總統府": {
            "title": "總統府",
            "address": "100台北市中正區重慶南路一段122號",
            "latitude": "25.040319874750914",
            "longitude": "121.51162883484746",
        },
    }
    if text in location:
        return location[text]
    else:
        # 如果找不到對應的地點，回傳 False
        return False


if __name__ == "__main__":
    # Colab 才需要，本機環境請刪除
    run_with_ngrok(app)
    app.run()

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\linebot\ch5\code05.py

# Copyright © https://steam.oxxostudio.tw

import json
from linebot import LineBotApi, WebhookHandler

# 載入對應的函式庫
from linebot.models import (
    TextSendMessage,
    StickerSendMessage,
    ImageSendMessage,
    LocationSendMessage,
)


def linebot(request):
    try:
        body = request.get_data(as_text=True)
        # json 格式化收到的訊息
        json_data = json.loads(body)
        line_bot_api = LineBotApi("你的 Channel access token")
        handler = WebhookHandler("你的 Channel secret")
        signature = request.headers["X-Line-Signature"]
        handler.handle(body, signature)
        # 取得 reply token
        tk = json_data["events"][0]["replyToken"]
        # 取得 message 的類型
        tp = json_data["events"][0]["message"]["type"]
        if tp == "text":
            # 如果是文字類型的訊息，取出文字並對應到 reply_msg 的函式
            msg = reply_msg(json_data["events"][0]["message"]["text"])
            if msg[0] == "text":
                # 如果要回傳的訊息是 text，使用 TextSendMessage 方法
                line_bot_api.reply_message(tk, TextSendMessage(text=msg[1]))
            if msg[0] == "location":
                # 如果要回傳的訊息是 location，使用 LocationSendMessage 方法
                line_bot_api.reply_message(
                    tk,
                    LocationSendMessage(
                        title=msg[1]["title"],
                        address=msg[1]["address"],
                        latitude=msg[1]["latitude"],
                        longitude=msg[1]["longitude"],
                    ),
                )
            if msg[0] == "image":
                # 如果要回傳的訊息是 image，使用 ImageSendMessage 方法
                line_bot_api.reply_message(
                    tk,
                    ImageSendMessage(
                        original_content_url=msg[1], preview_image_url=msg[1]
                    ),
                )
        if tp == "sticker":
            # 如果收到的訊息是表情貼圖
            stickerId = json_data["events"][0]["message"]["stickerId"]  # 取得 stickerId
            packageId = json_data["events"][0]["message"]["packageId"]  # 取得 packageId
            # 使用 StickerSendMessage 方法回傳同樣的表情貼圖
            line_bot_api.reply_message(
                tk, StickerSendMessage(sticker_id=stickerId, package_id=packageId)
            )
        if tp == "location":
            # 如果是收到的訊息是地點資訊
            line_bot_api.reply_message(tk, TextSendMessage(text="好地點！"))
        if tp == "image":
            # 如果是收到的訊息是圖片
            line_bot_api.reply_message(tk, TextSendMessage(text="好圖給讚！"))
        if tp == "audio":
            # 如果是收到的訊息是聲音
            line_bot_api.reply_message(tk, TextSendMessage(text="聲音讚喔～"))
        if tp == "video":
            # 如果是收到的訊息是影片
            line_bot_api.reply_message(tk, TextSendMessage(text="影片內容真是不錯！"))
    except:
        print("error", body)
    return "OK"


# 定義回覆訊息的函式
def reply_msg(text):
    # 客製化回覆文字
    msg_dict = {
        "hi": "Hi! 你好呀～",
        "hello": "Hello World!!!!",
        "你好": "你好呦～",
        "help": "有什麼要幫忙的嗎？",
    }
    # 如果出現特定地點，提供地點資訊
    local_dict = {
        "總統府": {
            "title": "總統府",
            "address": "100台北市中正區重慶南路一段122號",
            "latitude": "25.040319874750914",
            "longitude": "121.51162883484746",
        }
    }
    # 如果出現特定圖片文字，提供圖片網址
    img_dict = {
        "皮卡丘": "https://upload.wikimedia.org/wikipedia/en/a/a6/Pok%C3%A9mon_Pikachu_art.png",
        "傑尼龜": "https://upload.wikimedia.org/wikipedia/en/5/59/Pok%C3%A9mon_Squirtle_art.png",
    }
    # 預設回覆的文字就是收到的訊息
    reply_msg_content = ["text", text]
    if text in msg_dict:
        reply_msg_content = ["text", msg_dict[text.lower()]]
    if text in local_dict:
        reply_msg_content = ["location", local_dict[text.lower()]]
    if text in img_dict:
        reply_msg_content = ["image", img_dict[text.lower()]]
    return reply_msg_content


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\linebot\ch5\code06.py

# Copyright © https://steam.oxxostudio.tw

# Colab 才需要，本機環境請刪除
from flask_ngrok import run_with_ngrok
from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import TextSendMessage

app = Flask(__name__)


@app.route("/")
def home():
    line_bot_api = LineBotApi("你的 access token")
    try:
        # 取得網址的 msg 參數
        msg = request.args.get("msg")
        if msg != None:
            # 如果有 msg 參數，觸發 LINE Message API 的 push_message 方法
            line_bot_api.push_message("你的 User ID", TextSendMessage(text=msg))
            return msg
        else:
            return "OK"
    except:
        print("error")


if __name__ == "__main__":
    # Colab 才需要，本機環境請刪除
    run_with_ngrok(app)
    app.run()

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\linebot\ch5\code07.py

# Copyright © https://steam.oxxostudio.tw

# Colab 才需要，本機環境請刪除
from flask_ngrok import run_with_ngrok
from flask import Flask, request
from linebot import LineBotApi, WebhookHandler

# 載入對應的函式庫
from linebot.models import (
    TextSendMessage,
    StickerSendMessage,
    ImageSendMessage,
    LocationSendMessage,
)

app = Flask(__name__)


@app.route("/")
def home():
    line_bot_api = LineBotApi("你的 access token")
    try:
        msg = request.args.get("msg")
        if msg == "1":
            # 如果 msg 等於 1，發送文字訊息
            line_bot_api.push_message("你的 user ID", TextSendMessage(text="hello"))
        elif msg == "2":
            # 如果 msg 等於 2，發送表情貼圖
            line_bot_api.push_message(
                "你的 user ID", StickerSendMessage(package_id=1, sticker_id=2)
            )
        elif msg == "3":
            # 如果 msg 等於 3，發送圖片
            imgurl = "https://upload.wikimedia.org/wikipedia/en/a/a6/Pok%C3%A9mon_Pikachu_art.png"
            line_bot_api.push_message(
                "你的 user ID",
                ImageSendMessage(original_content_url=imgurl, preview_image_url=imgurl),
            )
        elif msg == "4":
            # 如果 msg 等於 4，發送地址資訊
            line_bot_api.push_message(
                "你的 user ID",
                LocationSendMessage(
                    title="總統府",
                    address="100台北市中正區重慶南路一段122號",
                    latitude="25.040319874750914",
                    longitude="121.51162883484746",
                ),
            )
        else:
            msg = "ok"  # 如果沒有 msg 或 msg 不是 1～4，將 msg 設定為 ok
        return msg
    except:
        print("error")


if __name__ == "__main__":
    # Colab 才需要，本機環境請刪除
    run_with_ngrok(app)
    app.run()

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\linebot\ch5\code08.py

# Copyright © https://steam.oxxostudio.tw

from linebot import LineBotApi, WebhookHandler
from linebot.models import (
    TextSendMessage,
    StickerSendMessage,
    ImageSendMessage,
    LocationSendMessage,
)


def pushmsg(request):
    line_bot_api = LineBotApi("你的 access token")
    try:
        msg = request.args.get("msg")
        if msg == "1":
            line_bot_api.push_message("你的 user ID", TextSendMessage(text="hello"))
        elif msg == "2":
            line_bot_api.push_message(
                "你的 user ID", StickerSendMessage(package_id=1, sticker_id=2)
            )
        elif msg == "3":
            imgurl = "https://upload.wikimedia.org/wikipedia/en/a/a6/Pok%C3%A9mon_Pikachu_art.png"
            line_bot_api.push_message(
                "你的 user ID",
                ImageSendMessage(original_content_url=imgurl, preview_image_url=imgurl),
            )
        elif msg == "4":
            line_bot_api.push_message(
                "你的 user ID",
                LocationSendMessage(
                    title="總統府",
                    address="100台北市中正區重慶南路一段122號",
                    latitude="25.040319874750914",
                    longitude="121.51162883484746",
                ),
            )
        else:
            msg = "ok"
        return msg
    except:
        print("error")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\linebot\ch5\code09.py

# Copyright © https://steam.oxxostudio.tw

import requests, json

# 設定 request 的 headers，注意前方要有 Bearer
headers = {
    "Authorization": "Bearer 你的 access token",
    "Content-Type": "application/json",
}

# 設定 request 的 body，必須包含 replyToken 和 messages
body = {"replyToken": replyToken, "messages": [{"type": "text", "text": "hello"}]}

# 向指定網址用 POST 方法發送 request
req = requests.request(
    "POST",
    "https://api.line.me/v2/bot/message/reply",
    headers=headers,
    data=json.dumps(body).encode("utf-8"),
)
print(req.text)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\linebot\ch5\code10.py

# Copyright © https://steam.oxxostudio.tw

import requests, json

# 設定 request 的 headers，注意前方要有 Bearer
headers = {
    "Authorization": "Bearer 你的 access token",
    "Content-Type": "application/json",
}

# 設定 request 的 body，必須包含 to 和 messages
body = {"to": "你的 user ID", "messages": [{"type": "text", "text": "hello"}]}
# 向指定網址用 POST 方法發送 request
req = requests.request(
    "POST",
    "https://api.line.me/v2/bot/message/push",
    headers=headers,
    data=json.dumps(body).encode("utf-8"),
)
# 印出得到的結果
print(req.text)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\linebot\ch6\code01.py

# Copyright © https://steam.oxxostudio.tw

from linebot import LineBotApi, WebhookHandler

# 需要額外載入對應的函示庫
from linebot.models import (
    PostbackAction,
    URIAction,
    MessageAction,
    TemplateSendMessage,
    ButtonsTemplate,
)

line_bot_api = LineBotApi("你的 Channel access token")
line_bot_api.push_message(
    "你的 user ID",
    TemplateSendMessage(
        alt_text="ButtonsTemplate",
        template=ButtonsTemplate(
            thumbnail_image_url="https://steam.oxxostudio.tw/download/python/line-template-message-demo.jpg",
            title="OXXO.STUDIO",
            text="這是按鈕樣板",
            actions=[
                PostbackAction(label="postback", data="發送 postback"),
                MessageAction(label="說 hello", text="hello"),
                URIAction(label="前往 STEAM 教育學習網", uri="https://steam.oxxostudio.tw"),
            ],
        ),
    ),
)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\linebot\ch6\code02.py

# Copyright © https://steam.oxxostudio.tw

from linebot import LineBotApi, WebhookHandler

# 需要額外載入對應的函示庫
from linebot.models import MessageAction, TemplateSendMessage, ConfirmTemplate

line_bot_api = LineBotApi("你的 Channel access token")
line_bot_api.push_message(
    "你的 user ID",
    TemplateSendMessage(
        alt_text="ConfirmTemplate",
        template=ConfirmTemplate(
            text="你好嗎？",
            actions=[
                MessageAction(label="好喔", text="好喔"),
                MessageAction(label="好喔", text="不好喔"),
            ],
        ),
    ),
)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\linebot\ch6\code03.py

# Copyright © https://steam.oxxostudio.tw

from linebot import LineBotApi, WebhookHandler

# 需要額外載入對應的函示庫
from linebot.models import (
    MessageAction,
    TemplateSendMessage,
    CarouselTemplate,
    CarouselColumn,
)

line_bot_api = LineBotApi("你的 Channel access token")
line_bot_api.push_message(
    "你的 user ID",
    TemplateSendMessage(
        alt_text="CarouselTemplate",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url="https://steam.oxxostudio.tw/download/python/line-template-message-demo.jpg",
                    title="選單 1",
                    text="說明文字 1",
                    actions=[
                        PostbackAction(label="postback", data="data1"),
                        MessageAction(label="hello", text="hello"),
                        URIAction(label="oxxo.studio", uri="http://oxxo.studio"),
                    ],
                ),
                CarouselColumn(
                    thumbnail_image_url="https://steam.oxxostudio.tw/download/python/line-template-message-demo2.jpg",
                    title="選單 2",
                    text="說明文字 2",
                    actions=[
                        PostbackAction(label="postback", data="data1"),
                        MessageAction(label="hi", text="hi"),
                        URIAction(
                            label="STEAM 教育學習網", uri="https://steam.oxxostudio.tw"
                        ),
                    ],
                ),
            ]
        ),
    ),
)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\linebot\ch6\code04.py

# Copyright © https://steam.oxxostudio.tw

from linebot import LineBotApi, WebhookHandler

# 需要額外載入對應的函示庫
from linebot.models import (
    MessageAction,
    TemplateSendMessage,
    ImageCarouselTemplate,
    ImageCarouselColumn,
)

line_bot_api = LineBotApi("你的 Channel access token")
line_bot_api.push_message(
    "你的 user ID",
    TemplateSendMessage(
        alt_text="ImageCarousel template",
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url="https://upload.wikimedia.org/wikipedia/en/a/a6/Pok%C3%A9mon_Pikachu_art.png",
                    action=MessageAction(label="皮卡丘", text="皮卡丘"),
                ),
                ImageCarouselColumn(
                    image_url="https://upload.wikimedia.org/wikipedia/en/5/59/Pok%C3%A9mon_Squirtle_art.png",
                    action=MessageAction(label="傑尼龜", text="傑尼龜"),
                ),
            ]
        ),
    ),
)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\linebot\ch6\code05.py

# Copyright © https://steam.oxxostudio.tw

from linebot import LineBotApi, WebhookHandler

# 載入對應的函式庫
from linebot.models import FlexSendMessage, BubbleContainer, ImageComponent

line_bot_api = LineBotApi("你的 Access Token")
# 剛剛 Flex Message 的 JSON 檔案就貼在下方
line_bot_api.push_message(
    "你的 User ID",
    FlexSendMessage(
        alt_text="hello",
        contents={
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
                "size": "full",
                "aspectRatio": "20:13",
                "aspectMode": "cover",
                "action": {"type": "uri", "uri": "http://linecorp.com/"},
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "Brown Cafe",
                        "weight": "bold",
                        "size": "xl",
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                            {
                                "type": "icon",
                                "size": "sm",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                            },
                            {
                                "type": "icon",
                                "size": "sm",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                            },
                            {
                                "type": "icon",
                                "size": "sm",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                            },
                            {
                                "type": "icon",
                                "size": "sm",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                            },
                            {
                                "type": "icon",
                                "size": "sm",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png",
                            },
                            {
                                "type": "text",
                                "text": "4.0",
                                "size": "sm",
                                "color": "#999999",
                                "margin": "md",
                                "flex": 0,
                            },
                        ],
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Place",
                                        "color": "#aaaaaa",
                                        "size": "sm",
                                        "flex": 1,
                                    },
                                    {
                                        "type": "text",
                                        "text": "Miraina Tower, 4-1-6 Shinjuku, Tokyo",
                                        "wrap": True,
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 5,
                                    },
                                ],
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Time",
                                        "color": "#aaaaaa",
                                        "size": "sm",
                                        "flex": 1,
                                    },
                                    {
                                        "type": "text",
                                        "text": "10:00 - 23:00",
                                        "wrap": True,
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 5,
                                    },
                                ],
                            },
                        ],
                    },
                ],
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                            "type": "uri",
                            "label": "CALL",
                            "uri": "https://linecorp.com",
                        },
                    },
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                            "type": "uri",
                            "label": "WEBSITE",
                            "uri": "https://linecorp.com",
                        },
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm",
                    },
                ],
                "flex": 0,
            },
        },
    ),
)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\linebot\ch6\code06.py

# Copyright © https://steam.oxxostudio.tw

import requests
import json

# 設定 headers，輸入你的 Access Token，記得前方要加上「Bearer 」( 有一個空白 )
headers = {
    "Authorization": "Bearer 你的 Access Token",
    "Content-Type": "application/json",
}

body = {
    "size": {"width": 2500, "height": 1686},  # 設定尺寸
    "selected": "true",  # 預設是否顯示
    "name": "Richmenu demo",  # 選單名稱
    "chatBarText": "Richmenu demo",  # 選單在 LINE 顯示的標題
    "areas": [  # 選單內容
        {
            "bounds": {"x": 341, "y": 75, "width": 560, "height": 340},  # 選單位置與大小
            "action": {"type": "message", "text": "電器"},  # 點擊後傳送文字
        },
        {
            "bounds": {"x": 1434, "y": 229, "width": 930, "height": 340},
            "action": {"type": "message", "text": "運動用品"},
        },
        {
            "bounds": {"x": 122, "y": 641, "width": 560, "height": 340},
            "action": {"type": "message", "text": "客服"},
        },
        {
            "bounds": {"x": 1012, "y": 645, "width": 560, "height": 340},
            "action": {"type": "message", "text": "餐廳"},
        },
        {
            "bounds": {"x": 1813, "y": 677, "width": 560, "height": 340},
            "action": {"type": "message", "text": "鞋子"},
        },
        {
            "bounds": {"x": 423, "y": 1203, "width": 560, "height": 340},
            "action": {"type": "message", "text": "美食"},
        },
        {
            "bounds": {"x": 1581, "y": 1133, "width": 560, "height": 340},
            "action": {"type": "message", "text": "衣服"},
        },
    ],
}
# 向指定網址發送 request
req = requests.request(
    "POST",
    "https://api.line.me/v2/bot/richmenu",
    headers=headers,
    data=json.dumps(body).encode("utf-8"),
)
# 印出得到的結果
print(req.text)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\linebot\ch6\code07.py

# Copyright © https://steam.oxxostudio.tw

from linebot import LineBotApi, WebhookHandler

line_bot_api = LineBotApi("你的 Access Token")

# import os
# os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用

# 開啟對應的圖片
with open("demo.jpg", "rb") as f:
    line_bot_api.set_rich_menu_image("你的圖文選單 ID", "image/jpeg", f)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\linebot\ch6\code08.py

# Copyright © https://steam.oxxostudio.tw

import requests

headers = {"Authorization": "Bearer 你的 Access Token"}

req = requests.request(
    "POST", "https://api.line.me/v2/bot/user/all/richmenu/你的圖文選單 ID", headers=headers
)

print(req.text)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\linebot\ch6\code09.py

# Copyright © https://steam.oxxostudio.tw

import requests, json

headers = {
    "Authorization": "Bearer 你的 access token",
    "Content-Type": "application/json",
}

body = {
    "size": {"width": 2500, "height": 1200},  # 設定尺寸
    "selected": "true",  # 預設是否顯示
    "name": "aaa",  # 選單名稱 ( 別名 Alias Id )
    "chatBarText": "選單 A",  # 選單在 LINE 顯示的標題
    "areas": [  # 選單內容
        {
            "bounds": {"x": 0, "y": 0, "width": 830, "height": 280},
            "action": {"type": "postback", "data": "no-data"},  # 按鈕 A 使用 postback
        },
        {
            "bounds": {"x": 835, "y": 0, "width": 830, "height": 640},
            "action": {
                "type": "richmenuswitch",
                "richMenuAliasId": "bbb",
                "data": "change-to-bbb",
            },  # 按鈕 B 使用 richmenuswitch
        },
        {
            "bounds": {"x": 1670, "y": 0, "width": 830, "height": 640},
            "action": {
                "type": "richmenuswitch",
                "richMenuAliasId": "ccc",
                "data": "change-to-ccc",
            },  # 按鈕 C 使用 richmenuswitch
        },
    ],
}
req = requests.request(
    "POST",
    "https://api.line.me/v2/bot/richmenu",
    headers=headers,
    data=json.dumps(body).encode("utf-8"),
)
print(req.text)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\linebot\ch6\code10.py

# Copyright © https://steam.oxxostudio.tw

from linebot import LineBotApi, WebhookHandler

line_bot_api = LineBotApi("你的 Access Token")

# import os
# os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用

# 開啟對應的圖片
with open("line-rich-menu-switch-demo-a.jpg", "rb") as f:
    line_bot_api.set_rich_menu_image("你的圖文選單 ID", "image/jpeg", f)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\linebot\ch6\code11.py

# Copyright © https://steam.oxxostudio.tw

import requests
import json

headers = {
    "Authorization": "Bearer 你的 access token",
    "Content-Type": "application/json",
}
body = {"richMenuAliasId": "aaa", "richMenuId": "圖文選單 id"}
req = requests.request(
    "POST",
    "https://api.line.me/v2/bot/richmenu/alias",
    headers=headers,
    data=json.dumps(body).encode("utf-8"),
)
print(req.text)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\linebot\ch6\code12.py

# Copyright © https://steam.oxxostudio.tw

import requests

headers = {
    "Authorization": "Bearer 你的 access token",
    "Content-Type": "application/json",
}
req = requests.request(
    "POST", "https://api.line.me/v2/bot/user/all/richmenu/圖文選單 id", headers=headers
)
print(req.text)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\linebot\ch6\code13.py

# Copyright © https://steam.oxxostudio.tw

import requests, json

headers = {
    "Authorization": "Bearer 你的 access token",
    "Content-Type": "application/json",
}

body = {
    "size": {"width": 2500, "height": 1200},  # 設定尺寸
    "selected": "true",  # 預設是否顯示
    "name": "bbb",  # 選單名稱 ( 別名 Alias Id )
    "chatBarText": "選單 B",  # 選單在 LINE 顯示的標題
    "areas": [  # 選單內容
        {
            "bounds": {"x": 0, "y": 0, "width": 830, "height": 280},
            "action": {
                "type": "richmenuswitch",
                "richMenuAliasId": "aaa",
                "data": "change-to-aaa",
            },  # 按鈕 A 使用 richmenuswitch
        },
        {
            "bounds": {"x": 835, "y": 0, "width": 830, "height": 640},
            "action": {"type": "postback", "data": "no-data"},  # 按鈕 B 使用 postback
        },
        {
            "bounds": {"x": 1670, "y": 0, "width": 830, "height": 640},
            "action": {
                "type": "richmenuswitch",
                "richMenuAliasId": "ccc",
                "data": "change-to-ccc",
            },  # 按鈕 C 使用 richmenuswitch
        },
    ],
}
req = requests.request(
    "POST",
    "https://api.line.me/v2/bot/richmenu",
    headers=headers,
    data=json.dumps(body).encode("utf-8"),
)
print(req.text)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\linebot\ch6\code14.py

# Copyright © https://steam.oxxostudio.tw

from linebot import LineBotApi, WebhookHandler

line_bot_api = LineBotApi("你的 Access Token")

# import os
# os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用

# 開啟對應的圖片
with open("line-rich-menu-switch-demo-b.jpg", "rb") as f:
    line_bot_api.set_rich_menu_image("你的圖文選單 ID", "image/jpeg", f)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\linebot\ch6\code15.py

# Copyright © https://steam.oxxostudio.tw

import requests
import json

headers = {
    "Authorization": "Bearer 你的 access token",
    "Content-Type": "application/json",
}
body = {"richMenuAliasId": "bbb", "richMenuId": "圖文選單 id"}
req = requests.request(
    "POST",
    "https://api.line.me/v2/bot/richmenu/alias",
    headers=headers,
    data=json.dumps(body).encode("utf-8"),
)
print(req.text)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\linebot\ch6\code16.py

# Copyright © https://steam.oxxostudio.tw

import requests, json

headers = {
    "Authorization": "Bearer 你的 access token",
    "Content-Type": "application/json",
}

body = {
    "size": {"width": 2500, "height": 1200},  # 設定尺寸
    "selected": "true",  # 預設是否顯示
    "name": "ccc",  # 選單名稱 ( 別名 Alias Id )
    "chatBarText": "選單 C",  # 選單在 LINE 顯示的標題
    "areas": [  # 選單內容
        {
            "bounds": {"x": 0, "y": 0, "width": 830, "height": 280},
            "action": {
                "type": "richmenuswitch",
                "richMenuAliasId": "aaa",
                "data": "change-to-aaa",
            },  # 按鈕 A 使用 richmenuswitch
        },
        {
            "bounds": {"x": 835, "y": 0, "width": 830, "height": 640},
            "action": {
                "type": "richmenuswitch",
                "richMenuAliasId": "bbb",
                "data": "change-to-ccc",
            },  # 按鈕 B 使用 richmenuswitch
        },
        {
            "bounds": {"x": 1670, "y": 0, "width": 830, "height": 640},
            "action": {"type": "postback", "data": "no-data"},  # 按鈕 C 使用 postback
        },
    ],
}
req = requests.request(
    "POST",
    "https://api.line.me/v2/bot/richmenu",
    headers=headers,
    data=json.dumps(body).encode("utf-8"),
)
print(req.text)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\linebot\ch6\code17.py

# Copyright © https://steam.oxxostudio.tw

from linebot import LineBotApi, WebhookHandler

line_bot_api = LineBotApi("你的 Access Token")

# import os
# os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用

# 開啟對應的圖片
with open("line-rich-menu-switch-demo-c.jpg", "rb") as f:
    line_bot_api.set_rich_menu_image("你的圖文選單 ID", "image/jpeg", f)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\linebot\ch6\code18.py

# Copyright © https://steam.oxxostudio.tw

import requests
import json

headers = {
    "Authorization": "Bearer 你的 access token",
    "Content-Type": "application/json",
}
body = {"richMenuAliasId": "ccc", "richMenuId": "圖文選單 id"}
req = requests.request(
    "POST",
    "https://api.line.me/v2/bot/richmenu/alias",
    headers=headers,
    data=json.dumps(body).encode("utf-8"),
)
print(req.text)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
