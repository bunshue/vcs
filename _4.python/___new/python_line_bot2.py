"""
一本精通 - LINE BOT 開發技巧
"""


import os
import sys
import time
import random


print("------------------------------------------------------------")  # 60個


# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\linebot\ch7\code01.py

# Copyright © https://steam.oxxostudio.tw

# Colab 使用，本機環境請刪除
from flask_ngrok import run_with_ngrok

from flask import Flask, request

# 載入 LINE Message API 相關函式庫
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage

# 載入 json 標準函式庫，處理回傳的資料格式
import json

app = Flask(__name__)


@app.route("/", methods=["POST"])
def linebot():
    # 取得收到的訊息內容
    body = request.get_data(as_text=True)
    try:
        line_bot_api = LineBotApi("你的 LINE Channel access token")
        handler = WebhookHandler("你的 LINE Channel secret")
        signature = request.headers["X-Line-Signature"]
        handler.handle(body, signature)
        # 轉換內容為 json 格式
        json_data = json.loads(body)
        print(json_data)
    except:
        print("error")
    return "OK"


if __name__ == "__main__":
    # Colab 使用，本機環境請刪除
    run_with_ngrok(app)
    app.run()

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\linebot\ch7\code02.py

# Copyright © https://steam.oxxostudio.tw

# Colab 使用，本機環境請刪除
from flask_ngrok import run_with_ngrok

from flask import Flask, request

# 載入 LINE Message API 相關函式庫
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage

# 載入 json 標準函式庫，處理回傳的資料格式
import requests, json, time

app = Flask(__name__)

access_token = "你的 LINE Channel access token"
channel_secret = "你的 LINE Channel secret"


@app.route("/", methods=["POST"])
def linebot():
    # 取得收到的訊息內容
    body = request.get_data(as_text=True)
    try:
        line_bot_api = LineBotApi(access_token)
        handler = WebhookHandler(channel_secret)
        signature = request.headers["X-Line-Signature"]
        handler.handle(body, signature)
        # 轉換內容為 json 格式
        json_data = json.loads(body)
        # 取得回傳訊息的 Token ( reply message 使用 )
        reply_token = json_data["events"][0]["replyToken"]
        # 取得使用者 ID ( push message 使用 )
        user_id = json_data["events"][0]["source"]["userId"]
        print(json_data)
        # 如果傳送的是 message
        if "message" in json_data["events"][0]:
            # 如果 message 的類型是文字 text
            if json_data["events"][0]["message"]["type"] == "text":
                # 取出文字
                text = json_data["events"][0]["message"]["text"]
                # 如果是雷達回波圖相關的文字
                if text == "雷達回波圖" or text == "雷達回波":
                    # 傳送雷達回波圖 ( 加上時間戳記 )
                    reply_image(
                        f"https://cwbopendata.s3.ap-northeast-1.amazonaws.com/MSC/O-A0058-003.png?{time.time_ns()}",
                        reply_token,
                        access_token,
                    )
                else:
                    # 如果是一般文字，直接回覆同樣的文字
                    reply_message(text, reply_token, access_token)
    except:
        print("error")
    return "OK"


if __name__ == "__main__":
    # Colab 使用，本機環境請刪除
    run_with_ngrok(app)
    app.run()


# LINE 回傳圖片函式
def reply_image(msg, rk, token):
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    body = {
        "replyToken": rk,
        "messages": [
            {"type": "image", "originalContentUrl": msg, "previewImageUrl": msg}
        ],
    }
    req = requests.request(
        "POST",
        "https://api.line.me/v2/bot/message/reply",
        headers=headers,
        data=json.dumps(body).encode("utf-8"),
    )
    print(req.text)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\linebot\ch7\code03.py

# Copyright © https://steam.oxxostudio.tw

import requests

url = "你取得的地震資訊 JSON 網址"
data = requests.get(url)
data_json = data.json()
eq = data_json["records"]["earthquake"]  # 轉換成 json 格式
for i in eq:
    loc = i["earthquakeInfo"]["epiCenter"]["location"]  # 地震地點
    val = i["earthquakeInfo"]["magnitude"]["magnitudeValue"]  # 芮氏規模
    dep = i["earthquakeInfo"]["depth"]["value"]  # 地震深度
    eq_time = i["earthquakeInfo"]["originTime"]  # 地震時間
    print(f"地震發生於{loc}，芮氏規模 {val} 級，深度 {dep} 公里，發生時間 {eq_time}")

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\linebot\ch7\code04.py

# Copyright © https://steam.oxxostudio.tw

# Colab 使用，本機環境請刪除
from flask_ngrok import run_with_ngrok

from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import requests, json, time

app = Flask(__name__)

access_token = "你的 LINE Channel access token"
channel_secret = "你的 LINE Channel secret"


@app.route("/", methods=["POST"])
def linebot():
    body = request.get_data(as_text=True)
    try:
        line_bot_api = LineBotApi(access_token)
        handler = WebhookHandler(channel_secret)
        signature = request.headers["X-Line-Signature"]
        handler.handle(body, signature)
        json_data = json.loads(body)
        reply_token = json_data["events"][0]["replyToken"]
        user_id = json_data["events"][0]["source"]["userId"]
        print(json_data)
        if "message" in json_data["events"][0]:
            if json_data["events"][0]["message"]["type"] == "text":
                text = json_data["events"][0]["message"]["text"]
                if text == "雷達回波圖" or text == "雷達回波":
                    reply_image(
                        f"https://cwbopendata.s3.ap-northeast-1.amazonaws.com/MSC/O-A0058-003.png?{time.time_ns()}",
                        reply_token,
                        access_token,
                    )
                # 如果是地震相關的文字
                elif text == "地震資訊" or text == "地震":
                    # 爬取地震資訊
                    msg = earth_quake()
                    # 傳送地震資訊 ( 用 push 方法，因為 reply 只能用一次 )
                    push_message(msg[0], user_id, access_token)
                    # 傳送地震圖片 ( 用 reply 方法 )
                    reply_image(msg[1], reply_token, access_token)
                else:
                    # 如果是一般文字，直接回覆同樣的文字
                    reply_message(text, reply_token, access_token)
    except:
        print("error")
    return "OK"


if __name__ == "__main__":
    # Colab 使用，本機環境請刪除
    run_with_ngrok(app)
    app.run()


# 地震資訊函式
def earth_quake():
    # 預設回傳的訊息
    msg = ["找不到地震資訊", "https://example.com/demo.jpg"]
    try:
        code = "你的氣象資料授權碼"
        url = f"https://opendata.cwb.gov.tw/api/v1/rest/datastore/E-A0016-001?Authorization={code}"
        # 爬取地震資訊網址
        e_data = requests.get(url)
        # json 格式化訊息內容
        e_data_json = e_data.json()
        # 取出地震資訊
        eq = e_data_json["records"]["earthquake"]
        for i in eq:
            loc = i["earthquakeInfo"]["epiCenter"]["location"]  # 地震地點
            val = i["earthquakeInfo"]["magnitude"]["magnitudeValue"]  # 地震規模
            dep = i["earthquakeInfo"]["depth"]["value"]  # 地震深度
            eq_time = i["earthquakeInfo"]["originTime"]  # 地震時間
            img = i["reportImageURI"]  # 地震圖
            msg = [f"{loc}，芮氏規模 {val} 級，深度 {dep} 公里，發生時間 {eq_time}。", img]
            break  # 取出第一筆資料後就 break
        return msg  # 回傳 msg
    except:
        return msg  # 如果取資料有發生錯誤，直接回傳 msg


# LINE push 訊息函式
def push_message(msg, uid, token):
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    body = {"to": uid, "messages": [{"type": "text", "text": msg}]}
    req = requests.request(
        "POST",
        "https://api.line.me/v2/bot/message/push",
        headers=headers,
        data=json.dumps(body).encode("utf-8"),
    )
    print(req.text)


# LINE 回傳訊息函式
def reply_message(msg, rk, token):
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    body = {"replyToken": rk, "messages": [{"type": "text", "text": msg}]}
    req = requests.request(
        "POST",
        "https://api.line.me/v2/bot/message/reply",
        headers=headers,
        data=json.dumps(body).encode("utf-8"),
    )
    print(req.text)


# LINE 回傳圖片函式
def reply_image(msg, rk, token):
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    body = {
        "replyToken": rk,
        "messages": [
            {"type": "image", "originalContentUrl": msg, "previewImageUrl": msg}
        ],
    }
    req = requests.request(
        "POST",
        "https://api.line.me/v2/bot/message/reply",
        headers=headers,
        data=json.dumps(body).encode("utf-8"),
    )
    print(req.text)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\linebot\ch7\code05.py

# Copyright © https://steam.oxxostudio.tw

# Colab 使用，本機環境請刪除
from flask_ngrok import run_with_ngrok

from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import requests, json, time

app = Flask(__name__)

access_token = "你的 LINE Channel access token"
channel_secret = "你的 LINE Channel secret"


@app.route("/", methods=["POST"])
def linebot():
    body = request.get_data(as_text=True)
    try:
        line_bot_api = LineBotApi(access_token)
        handler = WebhookHandler(channel_secret)
        signature = request.headers["X-Line-Signature"]
        handler.handle(body, signature)
        json_data = json.loads(body)
        reply_token = json_data["events"][0]["replyToken"]
        user_id = json_data["events"][0]["source"]["userId"]
        print(json_data)
        if "message" in json_data["events"][0]:
            # 如果 message 的類型是地圖 location
            if json_data["events"][0]["message"]["type"] == "location":
                # 取出地址資訊，並將「台」換成「臺」
                address = json_data["events"][0]["message"]["address"].replace("台", "臺")
                print(address)
            if json_data["events"][0]["message"]["type"] == "text":
                text = json_data["events"][0]["message"]["text"]
                if text == "雷達回波圖" or text == "雷達回波":
                    reply_image(
                        f"https://cwbopendata.s3.ap-northeast-1.amazonaws.com/MSC/O-A0058-003.png?{time.time_ns()}",
                        reply_token,
                        access_token,
                    )
                # 如果是地震相關的文字
                elif text == "地震資訊" or text == "地震":
                    # 爬取地震資訊
                    msg = earth_quake()
                    # 傳送地震資訊 ( 用 push 方法，因為 reply 只能用一次 )
                    push_message(msg[0], user_id, access_token)
                    # 傳送地震圖片 ( 用 reply 方法 )
                    reply_image(msg[1], reply_token, access_token)
                else:
                    # 如果是一般文字，直接回覆同樣的文字
                    reply_message(text, reply_token, access_token)
    except:
        print("error")
    return "OK"


if __name__ == "__main__":
    # Colab 使用，本機環境請刪除
    run_with_ngrok(app)
    app.run()


# 地震資訊函式
def earth_quake():
    # 預設回傳的訊息
    msg = ["找不到地震資訊", "https://example.com/demo.jpg"]
    try:
        code = "你的氣象資料授權碼"
        url = f"https://opendata.cwb.gov.tw/api/v1/rest/datastore/E-A0016-001?Authorization={code}"
        # 爬取地震資訊網址
        e_data = requests.get(url)
        # json 格式化訊息內容
        e_data_json = e_data.json()
        # 取出地震資訊
        eq = e_data_json["records"]["earthquake"]
        for i in eq:
            loc = i["earthquakeInfo"]["epiCenter"]["location"]  # 地震地點
            val = i["earthquakeInfo"]["magnitude"]["magnitudeValue"]  # 地震規模
            dep = i["earthquakeInfo"]["depth"]["value"]  # 地震深度
            eq_time = i["earthquakeInfo"]["originTime"]  # 地震時間
            img = i["reportImageURI"]  # 地震圖
            msg = [f"{loc}，芮氏規模 {val} 級，深度 {dep} 公里，發生時間 {eq_time}。", img]
            break  # 取出第一筆資料後就 break
        return msg  # 回傳 msg
    except:
        return msg  # 如果取資料有發生錯誤，直接回傳 msg


# LINE push 訊息函式
def push_message(msg, uid, token):
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    body = {"to": uid, "messages": [{"type": "text", "text": msg}]}
    req = requests.request(
        "POST",
        "https://api.line.me/v2/bot/message/push",
        headers=headers,
        data=json.dumps(body).encode("utf-8"),
    )
    print(req.text)


# LINE 回傳訊息函式
def reply_message(msg, rk, token):
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    body = {"replyToken": rk, "messages": [{"type": "text", "text": msg}]}
    req = requests.request(
        "POST",
        "https://api.line.me/v2/bot/message/reply",
        headers=headers,
        data=json.dumps(body).encode("utf-8"),
    )
    print(req.text)


# LINE 回傳圖片函式
def reply_image(msg, rk, token):
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    body = {
        "replyToken": rk,
        "messages": [
            {"type": "image", "originalContentUrl": msg, "previewImageUrl": msg}
        ],
    }
    req = requests.request(
        "POST",
        "https://api.line.me/v2/bot/message/reply",
        headers=headers,
        data=json.dumps(body).encode("utf-8"),
    )
    print(req.text)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\linebot\ch7\code06.py

# Copyright © https://steam.oxxostudio.tw

# Colab 使用，本機環境請刪除
from flask_ngrok import run_with_ngrok

from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import requests, json, time, statistics  # import statistics 函式庫

app = Flask(__name__)

access_token = "你的 LINE Channel access token"
channel_secret = "你的 LINE Channel secret"


@app.route("/", methods=["POST"])
def linebot():
    body = request.get_data(as_text=True)
    try:
        line_bot_api = LineBotApi(access_token)
        handler = WebhookHandler(channel_secret)
        signature = request.headers["X-Line-Signature"]
        handler.handle(body, signature)
        json_data = json.loads(body)
        reply_token = json_data["events"][0]["replyToken"]
        user_id = json_data["events"][0]["source"]["userId"]
        print(json_data)
        if "message" in json_data["events"][0]:
            # 如果 message 的類型是地圖 location
            if json_data["events"][0]["message"]["type"] == "location":
                # 取出地址資訊，並將「台」換成「臺」
                address = json_data["events"][0]["message"]["address"].replace("台", "臺")
                print(address)
                # 回覆爬取到的相關氣象資訊
                reply_message(
                    f"{address}\n\n{current_weather(address)}",
                    reply_token,
                    access_token,
                )
            if json_data["events"][0]["message"]["type"] == "text":
                text = json_data["events"][0]["message"]["text"]
                if text == "雷達回波圖" or text == "雷達回波":
                    reply_image(
                        f"https://cwbopendata.s3.ap-northeast-1.amazonaws.com/MSC/O-A0058-003.png?{time.time_ns()}",
                        reply_token,
                        access_token,
                    )
                # 如果是地震相關的文字
                elif text == "地震資訊" or text == "地震":
                    # 爬取地震資訊
                    msg = earth_quake()
                    # 傳送地震資訊 ( 用 push 方法，因為 reply 只能用一次 )
                    push_message(msg[0], user_id, access_token)
                    # 傳送地震圖片 ( 用 reply 方法 )
                    reply_image(msg[1], reply_token, access_token)
                else:
                    # 如果是一般文字，直接回覆同樣的文字
                    reply_message(text, reply_token, access_token)
    except:
        print("error")
    return "OK"


if __name__ == "__main__":
    # Colab 使用，本機環境請刪除
    run_with_ngrok(app)
    app.run()


# 地震資訊函式
def earth_quake():
    # 預設回傳的訊息
    msg = ["找不到地震資訊", "https://example.com/demo.jpg"]
    try:
        code = "你的氣象資料授權碼"
        url = f"https://opendata.cwb.gov.tw/api/v1/rest/datastore/E-A0016-001?Authorization={code}"
        # 爬取地震資訊網址
        e_data = requests.get(url)
        # json 格式化訊息內容
        e_data_json = e_data.json()
        # 取出地震資訊
        eq = e_data_json["records"]["earthquake"]
        for i in eq:
            loc = i["earthquakeInfo"]["epiCenter"]["location"]  # 地震地點
            val = i["earthquakeInfo"]["magnitude"]["magnitudeValue"]  # 地震規模
            dep = i["earthquakeInfo"]["depth"]["value"]  # 地震深度
            eq_time = i["earthquakeInfo"]["originTime"]  # 地震時間
            img = i["reportImageURI"]  # 地震圖
            msg = [f"{loc}，芮氏規模 {val} 級，深度 {dep} 公里，發生時間 {eq_time}。", img]
            break  # 取出第一筆資料後就 break
        return msg  # 回傳 msg
    except:
        return msg  # 如果取資料有發生錯誤，直接回傳 msg


# LINE push 訊息函式
def push_message(msg, uid, token):
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    body = {"to": uid, "messages": [{"type": "text", "text": msg}]}
    req = requests.request(
        "POST",
        "https://api.line.me/v2/bot/message/push",
        headers=headers,
        data=json.dumps(body).encode("utf-8"),
    )
    print(req.text)


# LINE 回傳訊息函式
def reply_message(msg, rk, token):
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    body = {"replyToken": rk, "messages": [{"type": "text", "text": msg}]}
    req = requests.request(
        "POST",
        "https://api.line.me/v2/bot/message/reply",
        headers=headers,
        data=json.dumps(body).encode("utf-8"),
    )
    print(req.text)


# LINE 回傳圖片函式
def reply_image(msg, rk, token):
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    body = {
        "replyToken": rk,
        "messages": [
            {"type": "image", "originalContentUrl": msg, "previewImageUrl": msg}
        ],
    }
    req = requests.request(
        "POST",
        "https://api.line.me/v2/bot/message/reply",
        headers=headers,
        data=json.dumps(body).encode("utf-8"),
    )
    print(req.text)


# 目前天氣函式
def current_weather(address):
    # 定義好待會要用的變數
    city_list, area_list, area_list2 = {}, {}, {}
    # 預設回傳訊息
    msg = "找不到氣象資訊。"

    # 定義取得資料的函式
    def get_data(url):
        # 爬取目前天氣網址的資料
        w_data = requests.get(url)
        # json 格式化訊息內容
        w_data_json = w_data.json()
        # 取出對應地點的內容
        location = w_data_json["cwbopendata"]["location"]
        for i in location:
            name = i["locationName"]  # 測站地點
            city = i["parameter"][0]["parameterValue"]  # 縣市名稱
            area = i["parameter"][2]["parameterValue"]  # 鄉鎮行政區
            temp = check_data(i["weatherElement"][3]["elementValue"]["value"])  # 氣溫
            humd = check_data(
                round(float(i["weatherElement"][4]["elementValue"]["value"]) * 100, 1)
            )  # 相對濕度
            r24 = check_data(i["weatherElement"][6]["elementValue"]["value"])  # 累積雨量
            if area not in area_list:
                # 以鄉鎮區域為 key，儲存需要的資訊
                area_list[area] = {"temp": temp, "humd": humd, "r24": r24}
            if city not in city_list:
                # 以主要縣市名稱為 key，準備紀錄裡面所有鄉鎮的數值
                city_list[city] = {"temp": [], "humd": [], "r24": []}
            city_list[city]["temp"].append(temp)  # 記錄主要縣市裡鄉鎮區域的溫度 ( 串列格式 )
            city_list[city]["humd"].append(humd)  # 記錄主要縣市裡鄉鎮區域的濕度 ( 串列格式 )
            city_list[city]["r24"].append(r24)  # 記錄主要縣市裡鄉鎮區域的雨量 ( 串列格式 )

    # 定義如果數值小於 0，回傳 False 的函式
    def check_data(e):
        return False if float(e) < 0 else float(e)

    # 定義產生回傳訊息的函式
    def msg_content(loc, msg):
        a = msg
        for i in loc:
            if i in address:  # 如果地址裡存在 key 的名稱
                temp = f"氣溫 {loc[i]['temp']} 度，" if loc[i]["temp"] != False else ""
                humd = f"相對濕度 {loc[i]['humd']}%，" if loc[i]["humd"] != False else ""
                r24 = f"累積雨量 {loc[i]['r24']}mm" if loc[i]["r24"] != False else ""
                description = f"{temp}{humd}{r24}".strip("，")
                a = f"{description}。"  # 取出 key 的內容作為回傳訊息使用
                break
        return a

    try:
        # 因為目前天氣有兩組網址，兩組都爬取
        code = "你的氣象資料授權碼"
        get_data(
            f"https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/O-A0001-001?Authorization={code}&downloadType=WEB&format=JSON"
        )
        get_data(
            f"https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/O-A0003-001?Authorization={code}&downloadType=WEB&format=JSON"
        )

        for i in city_list:
            if i not in area_list2:
                # 將主要縣市裡的數值平均後，以主要縣市名稱為 key，再度儲存一次，如果找不到鄉鎮區域，就使用平均數值
                area_list2[i] = {
                    "temp": round(statistics.mean(city_list[i]["temp"]), 1),
                    "humd": round(statistics.mean(city_list[i]["humd"]), 1),
                    "r24": round(statistics.mean(city_list[i]["r24"]), 1),
                }
        msg = msg_content(area_list2, msg)  # 將訊息改為「大縣市」
        msg = msg_content(area_list, msg)  # 將訊息改為「鄉鎮區域」
        return msg  # 回傳 msg
    except:
        return msg  # 如果取資料有發生錯誤，直接回傳 msg


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\linebot\ch7\code07.py

# Copyright © https://steam.oxxostudio.tw

# Colab 使用，本機環境請刪除
from flask_ngrok import run_with_ngrok

from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import requests, json, time, statistics  # import statistics 函式庫

app = Flask(__name__)

access_token = "你的 LINE Channel access token"
channel_secret = "你的 LINE Channel secret"


@app.route("/", methods=["POST"])
def linebot():
    body = request.get_data(as_text=True)
    try:
        line_bot_api = LineBotApi(access_token)
        handler = WebhookHandler(channel_secret)
        signature = request.headers["X-Line-Signature"]
        handler.handle(body, signature)
        json_data = json.loads(body)
        reply_token = json_data["events"][0]["replyToken"]
        user_id = json_data["events"][0]["source"]["userId"]
        print(json_data)
        if "message" in json_data["events"][0]:
            # 如果 message 的類型是地圖 location
            if json_data["events"][0]["message"]["type"] == "location":
                # 取出地址資訊，並將「台」換成「臺」
                address = json_data["events"][0]["message"]["address"].replace("台", "臺")
                print(address)
                # 回覆爬取到的相關氣象資訊
                reply_message(
                    f"{address}\n\n{current_weather(address)}\n\n{forecast(address)}",
                    reply_token,
                    access_token,
                )
            if json_data["events"][0]["message"]["type"] == "text":
                text = json_data["events"][0]["message"]["text"]
                if text == "雷達回波圖" or text == "雷達回波":
                    reply_image(
                        f"https://cwbopendata.s3.ap-northeast-1.amazonaws.com/MSC/O-A0058-003.png?{time.time_ns()}",
                        reply_token,
                        access_token,
                    )
                # 如果是地震相關的文字
                elif text == "地震資訊" or text == "地震":
                    # 爬取地震資訊
                    msg = earth_quake()
                    # 傳送地震資訊 ( 用 push 方法，因為 reply 只能用一次 )
                    push_message(msg[0], user_id, access_token)
                    # 傳送地震圖片 ( 用 reply 方法 )
                    reply_image(msg[1], reply_token, access_token)
                else:
                    # 如果是一般文字，直接回覆同樣的文字
                    reply_message(text, reply_token, access_token)
    except:
        print("error")
    return "OK"


if __name__ == "__main__":
    # Colab 使用，本機環境請刪除
    run_with_ngrok(app)
    app.run()


# 地震資訊函式
def earth_quake():
    # 預設回傳的訊息
    msg = ["找不到地震資訊", "https://example.com/demo.jpg"]
    try:
        code = "你的氣象資料授權碼"
        url = f"https://opendata.cwb.gov.tw/api/v1/rest/datastore/E-A0016-001?Authorization={code}"
        # 爬取地震資訊網址
        e_data = requests.get(url)
        # json 格式化訊息內容
        e_data_json = e_data.json()
        # 取出地震資訊
        eq = e_data_json["records"]["earthquake"]
        for i in eq:
            loc = i["earthquakeInfo"]["epiCenter"]["location"]  # 地震地點
            val = i["earthquakeInfo"]["magnitude"]["magnitudeValue"]  # 地震規模
            dep = i["earthquakeInfo"]["depth"]["value"]  # 地震深度
            eq_time = i["earthquakeInfo"]["originTime"]  # 地震時間
            img = i["reportImageURI"]  # 地震圖
            msg = [f"{loc}，芮氏規模 {val} 級，深度 {dep} 公里，發生時間 {eq_time}。", img]
            break  # 取出第一筆資料後就 break
        return msg  # 回傳 msg
    except:
        return msg  # 如果取資料有發生錯誤，直接回傳 msg


# LINE push 訊息函式
def push_message(msg, uid, token):
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    body = {"to": uid, "messages": [{"type": "text", "text": msg}]}
    req = requests.request(
        "POST",
        "https://api.line.me/v2/bot/message/push",
        headers=headers,
        data=json.dumps(body).encode("utf-8"),
    )
    print(req.text)


# LINE 回傳訊息函式
def reply_message(msg, rk, token):
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    body = {"replyToken": rk, "messages": [{"type": "text", "text": msg}]}
    req = requests.request(
        "POST",
        "https://api.line.me/v2/bot/message/reply",
        headers=headers,
        data=json.dumps(body).encode("utf-8"),
    )
    print(req.text)


# LINE 回傳圖片函式
def reply_image(msg, rk, token):
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    body = {
        "replyToken": rk,
        "messages": [
            {"type": "image", "originalContentUrl": msg, "previewImageUrl": msg}
        ],
    }
    req = requests.request(
        "POST",
        "https://api.line.me/v2/bot/message/reply",
        headers=headers,
        data=json.dumps(body).encode("utf-8"),
    )
    print(req.text)


# 目前天氣函式
def current_weather(address):
    # 定義好待會要用的變數
    city_list, area_list, area_list2 = {}, {}, {}
    # 預設回傳訊息
    msg = "找不到氣象資訊。"

    # 定義取得資料的函式
    def get_data(url):
        # 爬取目前天氣網址的資料
        w_data = requests.get(url)
        # json 格式化訊息內容
        w_data_json = w_data.json()
        # 取出對應地點的內容
        location = w_data_json["cwbopendata"]["location"]
        for i in location:
            name = i["locationName"]  # 測站地點
            city = i["parameter"][0]["parameterValue"]  # 縣市名稱
            area = i["parameter"][2]["parameterValue"]  # 鄉鎮行政區
            temp = check_data(i["weatherElement"][3]["elementValue"]["value"])  # 氣溫
            humd = check_data(
                round(float(i["weatherElement"][4]["elementValue"]["value"]) * 100, 1)
            )  # 相對濕度
            r24 = check_data(i["weatherElement"][6]["elementValue"]["value"])  # 累積雨量
            if area not in area_list:
                # 以鄉鎮區域為 key，儲存需要的資訊
                area_list[area] = {"temp": temp, "humd": humd, "r24": r24}
            if city not in city_list:
                # 以主要縣市名稱為 key，準備紀錄裡面所有鄉鎮的數值
                city_list[city] = {"temp": [], "humd": [], "r24": []}
            city_list[city]["temp"].append(temp)  # 記錄主要縣市裡鄉鎮區域的溫度 ( 串列格式 )
            city_list[city]["humd"].append(humd)  # 記錄主要縣市裡鄉鎮區域的濕度 ( 串列格式 )
            city_list[city]["r24"].append(r24)  # 記錄主要縣市裡鄉鎮區域的雨量 ( 串列格式 )

    # 定義如果數值小於 0，回傳 False 的函式
    def check_data(e):
        return False if float(e) < 0 else float(e)

    # 定義產生回傳訊息的函式
    def msg_content(loc, msg):
        a = msg
        for i in loc:
            if i in address:  # 如果地址裡存在 key 的名稱
                temp = f"氣溫 {loc[i]['temp']} 度，" if loc[i]["temp"] != False else ""
                humd = f"相對濕度 {loc[i]['humd']}%，" if loc[i]["humd"] != False else ""
                r24 = f"累積雨量 {loc[i]['r24']}mm" if loc[i]["r24"] != False else ""
                description = f"{temp}{humd}{r24}".strip("，")
                a = f"{description}。"  # 取出 key 的內容作為回傳訊息使用
                break
        return a

    try:
        # 因為目前天氣有兩組網址，兩組都爬取
        code = "你的氣象資料授權碼"
        get_data(
            f"https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/O-A0001-001?Authorization={code}&downloadType=WEB&format=JSON"
        )
        get_data(
            f"https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/O-A0003-001?Authorization={code}&downloadType=WEB&format=JSON"
        )

        for i in city_list:
            if i not in area_list2:
                # 將主要縣市裡的數值平均後，以主要縣市名稱為 key，再度儲存一次，如果找不到鄉鎮區域，就使用平均數值
                area_list2[i] = {
                    "temp": round(statistics.mean(city_list[i]["temp"]), 1),
                    "humd": round(statistics.mean(city_list[i]["humd"]), 1),
                    "r24": round(statistics.mean(city_list[i]["r24"]), 1),
                }
        msg = msg_content(area_list2, msg)  # 將訊息改為「大縣市」
        msg = msg_content(area_list, msg)  # 將訊息改為「鄉鎮區域」
        return msg  # 回傳 msg
    except:
        return msg  # 如果取資料有發生錯誤，直接回傳 msg


# 氣象預報函式
def forecast(address):
    area_list = {}
    # 將主要縣市個別的 JSON 代碼列出
    json_api = {
        "宜蘭縣": "F-D0047-001",
        "桃園市": "F-D0047-005",
        "新竹縣": "F-D0047-009",
        "苗栗縣": "F-D0047-013",
        "彰化縣": "F-D0047-017",
        "南投縣": "F-D0047-021",
        "雲林縣": "F-D0047-025",
        "嘉義縣": "F-D0047-029",
        "屏東縣": "F-D0047-033",
        "臺東縣": "F-D0047-037",
        "花蓮縣": "F-D0047-041",
        "澎湖縣": "F-D0047-045",
        "基隆市": "F-D0047-049",
        "新竹市": "F-D0047-053",
        "嘉義市": "F-D0047-057",
        "臺北市": "F-D0047-061",
        "高雄市": "F-D0047-065",
        "新北市": "F-D0047-069",
        "臺中市": "F-D0047-073",
        "臺南市": "F-D0047-077",
        "連江縣": "F-D0047-081",
        "金門縣": "F-D0047-085",
    }
    msg = "找不到天氣預報資訊。"  # 預設回傳訊息
    try:
        code = "你的氣象開放平台授權碼"
        url = f"https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/F-C0032-001?Authorization={code}&downloadType=WEB&format=JSON"
        f_data = requests.get(url)  # 取得主要縣市預報資料
        f_data_json = f_data.json()  # json 格式化訊息內容
        # 取得縣市的預報內容
        location = f_data_json["cwbopendata"]["dataset"]["location"]
        for i in location:
            city = i["locationName"]  # 縣市名稱
            wx8 = i["weatherElement"][0]["time"][0]["parameter"][
                "parameterName"
            ]  # 天氣現象
            mint8 = i["weatherElement"][1]["time"][0]["parameter"][
                "parameterName"
            ]  # 最低溫
            maxt8 = i["weatherElement"][2]["time"][0]["parameter"][
                "parameterName"
            ]  # 最高溫
            ci8 = i["weatherElement"][2]["time"][0]["parameter"]["parameterName"]  # 舒適度
            pop8 = i["weatherElement"][2]["time"][0]["parameter"][
                "parameterName"
            ]  # 降雨機率
            # 組合成回傳的訊息，存在以縣市名稱為 key 的字典檔裡
            area_list[city] = f"未來 8 小時{wx8}，最高溫 {maxt8} 度，最低溫 {mint8} 度，降雨機率 {pop8} %"
        for i in area_list:
            if i in address:  # 如果使用者的地址包含縣市名稱
                msg = area_list[i]  # 將 msg 換成對應的預報資訊
                # 將進一步的預報網址換成對應的預報網址
                url = f"https://opendata.cwb.gov.tw/api/v1/rest/datastore/{json_api[i]}?Authorization={code}&elementName=WeatherDescription"
                f_data = requests.get(url)  # 取得主要縣市裡各個區域鄉鎮的氣象預報
                f_data_json = f_data.json()  # json 格式化訊息內容
                # 取得預報內容
                location = f_data_json["records"]["locations"][0]["location"]
                break
        for i in location:
            city = i["locationName"]  # 取得縣市名稱
            wd = i["weatherElement"][0]["time"][1]["elementValue"][0]["value"]  # 綜合描述
            if city in address:  # 如果使用者的地址包含鄉鎮區域名稱
                msg = f"未來八小時天氣{wd}"  # 將 msg 換成對應的預報資訊
                break
        return msg  # 回傳 msg
    except:
        return msg  # 如果取資料有發生錯誤，直接回傳 msg


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\linebot\ch7\code08.py

# Copyright © https://steam.oxxostudio.tw

# Colab 使用，本機環境請刪除
from flask_ngrok import run_with_ngrok

from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import requests, json, time, statistics

app = Flask(__name__)

access_token = "你的 LINE Channel access token"
channel_secret = "你的 LINE Channel secret"


@app.route("/", methods=["POST"])
def linebot():
    body = request.get_data(as_text=True)
    try:
        line_bot_api = LineBotApi(access_token)
        handler = WebhookHandler(channel_secret)
        signature = request.headers["X-Line-Signature"]
        handler.handle(body, signature)
        json_data = json.loads(body)
        reply_token = json_data["events"][0]["replyToken"]
        user_id = json_data["events"][0]["source"]["userId"]
        print(json_data)
        if "message" in json_data["events"][0]:
            if json_data["events"][0]["message"]["type"] == "location":
                address = json_data["events"][0]["message"]["address"].replace("台", "臺")
                print(address)
                # 回覆爬取到的相關氣象資訊
                reply_message(
                    f"{address}\n\n{current_weather(address)}\n\n{aqi(address)}\n\n{forecast(address)}",
                    reply_token,
                    access_token,
                )
            if json_data["events"][0]["message"]["type"] == "text":
                text = json_data["events"][0]["message"]["text"]
                if text == "雷達回波圖" or text == "雷達回波":
                    reply_image(
                        f"https://cwbopendata.s3.ap-northeast-1.amazonaws.com/MSC/O-A0058-003.png?{time.time_ns()}",
                        reply_token,
                        access_token,
                    )
                elif text == "地震資訊" or text == "地震":
                    msg = earth_quake()
                    push_message(msg[0], user_id, access_token)
                    reply_image(msg[1], reply_token, access_token)
                else:
                    reply_message(text, reply_token, access_token)
    except:
        print("error")
    return "OK"


if __name__ == "__main__":
    # Colab 使用，本機環境請刪除
    run_with_ngrok(app)
    app.run()


# 地震資訊函式
def earth_quake():
    # 預設回傳的訊息
    msg = ["找不到地震資訊", "https://example.com/demo.jpg"]
    try:
        code = "你的氣象資料授權碼"
        url = f"https://opendata.cwb.gov.tw/api/v1/rest/datastore/E-A0016-001?Authorization={code}"
        e_data = requests.get(url)
        e_data_json = e_data.json()
        eq = e_data_json["records"]["earthquake"]
        for i in eq:
            loc = i["earthquakeInfo"]["epiCenter"]["location"]
            val = i["earthquakeInfo"]["magnitude"]["magnitudeValue"]
            dep = i["earthquakeInfo"]["depth"]["value"]
            eq_time = i["earthquakeInfo"]["originTime"]
            img = i["reportImageURI"]
            msg = [f"{loc}，芮氏規模 {val} 級，深度 {dep} 公里，發生時間 {eq_time}。", img]
            break
        return msg
    except:
        return msg


# LINE push 訊息函式
def push_message(msg, uid, token):
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    body = {"to": uid, "messages": [{"type": "text", "text": msg}]}
    req = requests.request(
        "POST",
        "https://api.line.me/v2/bot/message/push",
        headers=headers,
        data=json.dumps(body).encode("utf-8"),
    )
    print(req.text)


# LINE 回傳訊息函式
def reply_message(msg, rk, token):
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    body = {"replyToken": rk, "messages": [{"type": "text", "text": msg}]}
    req = requests.request(
        "POST",
        "https://api.line.me/v2/bot/message/reply",
        headers=headers,
        data=json.dumps(body).encode("utf-8"),
    )
    print(req.text)


# LINE 回傳圖片函式
def reply_image(msg, rk, token):
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    body = {
        "replyToken": rk,
        "messages": [
            {"type": "image", "originalContentUrl": msg, "previewImageUrl": msg}
        ],
    }
    req = requests.request(
        "POST",
        "https://api.line.me/v2/bot/message/reply",
        headers=headers,
        data=json.dumps(body).encode("utf-8"),
    )
    print(req.text)


# 目前天氣函式
def current_weather(address):
    city_list, area_list, area_list2 = {}, {}, {}
    msg = "找不到氣象資訊。"

    def get_data(url):
        w_data = requests.get(url)
        w_data_json = w_data.json()
        location = w_data_json["cwbopendata"]["location"]
        for i in location:
            name = i["locationName"]
            city = i["parameter"][0]["parameterValue"]
            area = i["parameter"][2]["parameterValue"]
            temp = check_data(i["weatherElement"][3]["elementValue"]["value"])
            humd = check_data(
                round(float(i["weatherElement"][4]["elementValue"]["value"]) * 100, 1)
            )
            r24 = check_data(i["weatherElement"][6]["elementValue"]["value"])
            if area not in area_list:
                area_list[area] = {"temp": temp, "humd": humd, "r24": r24}
            if city not in city_list:
                city_list[city] = {"temp": [], "humd": [], "r24": []}
            city_list[city]["temp"].append(temp)
            city_list[city]["humd"].append(humd)
            city_list[city]["r24"].append(r24)

    def check_data(e):
        return False if float(e) < 0 else float(e)

    def msg_content(loc, msg):
        a = msg
        for i in loc:
            if i in address:
                temp = f"氣溫 {loc[i]['temp']} 度，" if loc[i]["temp"] != False else ""
                humd = f"相對濕度 {loc[i]['humd']}%，" if loc[i]["humd"] != False else ""
                r24 = f"累積雨量 {loc[i]['r24']}mm" if loc[i]["r24"] != False else ""
                description = f"{temp}{humd}{r24}".strip("，")
                a = f"{description}。"
                break
        return a

    try:
        code = "你的氣象資料授權碼"
        get_data(
            f"https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/O-A0001-001?Authorization={code}&downloadType=WEB&format=JSON"
        )
        get_data(
            f"https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/O-A0003-001?Authorization={code}&downloadType=WEB&format=JSON"
        )

        for i in city_list:
            if i not in area_list2:
                area_list2[i] = {
                    "temp": round(statistics.mean(city_list[i]["temp"]), 1),
                    "humd": round(statistics.mean(city_list[i]["humd"]), 1),
                    "r24": round(statistics.mean(city_list[i]["r24"]), 1),
                }
        msg = msg_content(area_list2, msg)
        msg = msg_content(area_list, msg)
        return msg
    except:
        return msg


def forecast(address):
    area_list = {}
    json_api = {
        "宜蘭縣": "F-D0047-001",
        "桃園市": "F-D0047-005",
        "新竹縣": "F-D0047-009",
        "苗栗縣": "F-D0047-013",
        "彰化縣": "F-D0047-017",
        "南投縣": "F-D0047-021",
        "雲林縣": "F-D0047-025",
        "嘉義縣": "F-D0047-029",
        "屏東縣": "F-D0047-033",
        "臺東縣": "F-D0047-037",
        "花蓮縣": "F-D0047-041",
        "澎湖縣": "F-D0047-045",
        "基隆市": "F-D0047-049",
        "新竹市": "F-D0047-053",
        "嘉義市": "F-D0047-057",
        "臺北市": "F-D0047-061",
        "高雄市": "F-D0047-065",
        "新北市": "F-D0047-069",
        "臺中市": "F-D0047-073",
        "臺南市": "F-D0047-077",
        "連江縣": "F-D0047-081",
        "金門縣": "F-D0047-085",
    }
    msg = "找不到天氣預報資訊。"
    try:
        code = "你的氣象開放平台授權碼"
        url = f"https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/F-C0032-001?Authorization={code}&downloadType=WEB&format=JSON"
        f_data = requests.get(url)
        f_data_json = f_data.json()
        location = f_data_json["cwbopendata"]["dataset"]["location"]
        for i in location:
            city = i["locationName"]
            wx8 = i["weatherElement"][0]["time"][0]["parameter"]["parameterName"]
            mint8 = i["weatherElement"][1]["time"][0]["parameter"]["parameterName"]
            maxt8 = i["weatherElement"][2]["time"][0]["parameter"]["parameterName"]
            ci8 = i["weatherElement"][2]["time"][0]["parameter"]["parameterName"]
            pop8 = i["weatherElement"][2]["time"][0]["parameter"]["parameterName"]
            area_list[city] = f"未來 8 小時{wx8}，最高溫 {maxt8} 度，最低溫 {mint8} 度，降雨機率 {pop8} %"
        for i in area_list:
            if i in address:
                msg = area_list[i]
                url = f"https://opendata.cwb.gov.tw/api/v1/rest/datastore/{json_api[i]}?Authorization={code}&elementName=WeatherDescription"
                f_data = requests.get(url)
                f_data_json = f_data.json()
                location = f_data_json["records"]["locations"][0]["location"]
                break
        for i in location:
            city = i["locationName"]
            wd = i["weatherElement"][0]["time"][1]["elementValue"][0]["value"]
            if city in address:
                msg = f"未來八小時天氣{wd}"
                break
        return msg
    except:
        return msg


# 空氣品質函式
def aqi(address):
    city_list, site_list = {}, {}
    msg = "找不到空氣品質資訊。"
    try:
        # 2022/12 時氣象局有修改了 API 內容，將部份大小寫混合全改成小寫，因此程式碼也跟著修正
        url = "https://data.epa.gov.tw/api/v2/aqx_p_432?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate%20desc&format=JSON"
        a_data = requests.get(url)  # 使用 get 方法透過空氣品質指標 API 取得內容
        a_data_json = a_data.json()  # json 格式化訊息內容
        for i in a_data_json["records"]:  # 依序取出 records 內容的每個項目
            city = i["county"]  # 取出縣市名稱
            if city not in city_list:
                city_list[city] = []  # 以縣市名稱為 key，準備存入串列資料
            site = i["sitename"]  # 取出鄉鎮區域名稱
            aqi = int(i["aqi"])  # 取得 AQI 數值
            status = i["status"]  # 取得空氣品質狀態
            site_list[site] = {"aqi": aqi, "status": status}  # 記錄鄉鎮區域空氣品質
            city_list[city].append(aqi)  # 將各個縣市裡的鄉鎮區域空氣 aqi 數值，以串列方式放入縣市名稱的變數裡
        for i in city_list:
            if i in address:  # 如果地址裡包含縣市名稱的 key，就直接使用對應的內容
                # 參考 https://airtw.epa.gov.tw/cht/Information/Standard/AirQualityIndicator.aspx
                aqi_val = round(
                    statistics.mean(city_list[i]), 0
                )  # 計算平均數值，如果找不到鄉鎮區域，就使用縣市的平均值
                aqi_status = ""  # 手動判斷對應的空氣品質說明文字
                if aqi_val <= 50:
                    aqi_status = "良好"
                elif aqi_val > 50 and aqi_val <= 100:
                    aqi_status = "普通"
                elif aqi_val > 100 and aqi_val <= 150:
                    aqi_status = "對敏感族群不健康"
                elif aqi_val > 150 and aqi_val <= 200:
                    aqi_status = "對所有族群不健康"
                elif aqi_val > 200 and aqi_val <= 300:
                    aqi_status = "非常不健康"
                else:
                    aqi_status = "危害"
                msg = f"空氣品質{aqi_status} ( AQI {aqi_val} )。"  # 定義回傳的訊息
                break
        for i in site_list:
            if i in address:  # 如果地址裡包含鄉鎮區域名稱的 key，就直接使用對應的內容
                msg = f'空氣品質{site_list[i]["status"]} ( AQI {site_list[i]["aqi"]} )。'
                break
        return msg  # 回傳 msg
    except:
        return msg  # 如果取資料有發生錯誤，直接回傳 msg


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\linebot\ch7\code09.py

# Copyright © https://steam.oxxostudio.tw

import requests
import json

headers = {
    "Authorization": "Bearer 你的 access token",
    "Content-Type": "application/json",
}

body = {
    "size": {"width": 2500, "height": 640},  # 設定尺寸
    "selected": "true",  # 預設是否顯示
    "name": "bbb",  # 選單名稱
    "chatBarText": "b",  # 選單在 LINE 顯示的標題
    "areas": [  # 選單內容
        {
            "bounds": {"x": 0, "y": 0, "width": 1250, "height": 640},  # 選單位置與大小
            "action": {
                "type": "uri",
                "uri": "https://line.me/R/nv/location/",
            },  # 點擊後開啟地圖定位，傳送位置資訊
        },
        {
            "bounds": {"x": 1251, "y": 0, "width": 625, "height": 640},  # 選單位置與大小
            "action": {"type": "message", "text": "雷達回波圖"},  # 點擊後傳送文字
        },
        {
            "bounds": {"x": 1879, "y": 0, "width": 625, "height": 640},  # 選單位置與大小
            "action": {"type": "message", "text": "地震資訊"},  # 點擊後傳送文字
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

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\linebot\ch7\code10.py

# Copyright © https://steam.oxxostudio.tw

from linebot import LineBotApi, WebhookHandler

line_bot_api = LineBotApi("你的 access token")

# import os
# os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用

# 開啟對應的圖片
with open("line-bot-weather-demo.jpg", "rb") as f:
    line_bot_api.set_rich_menu_image("你的圖文選單 ID", "image/jpeg", f)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\linebot\ch7\code11.py

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

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\linebot\ch7\code12.py

# Copyright © https://steam.oxxostudio.tw

from linebot import LineBotApi, WebhookHandler
from linebot.models import (
    TextSendMessage,
    StickerSendMessage,
    ImageSendMessage,
    LocationSendMessage,
)
import requests, statistics, json, time

access_token = "你的 access token"
channel_secret = "你的 channel_secret"


def linebot(request):
    body = request.get_data(as_text=True)
    try:
        json_data = json.loads(body)  # json 格式化訊息內容
        line_bot_api = LineBotApi(access_token)  # 確認 token 是否正確
        handler = WebhookHandler(channel_secret)
        signature = request.headers["X-Line-Signature"]  # 加入回傳的 headers
        handler.handle(body, signature)  # 綁定訊息回傳的相關資訊
        reply_token = json_data["events"][0][
            "replyToken"
        ]  # 取得回傳訊息的 Token ( reply message 使用 )
        user_id = json_data["events"][0]["source"][
            "userId"
        ]  # 取得使用者 ID ( push message 使用 )
        print(json_data)
        if "message" in json_data["events"][0]:  # 如果傳送的是 message
            if (
                json_data["events"][0]["message"]["type"] == "location"
            ):  # 如果 message 的類型是地圖 location
                address = json_data["events"][0]["message"]["address"].replace(
                    "台", "臺"
                )  # 取出地址資訊，並將「台」換成「臺」
                reply_message(
                    f"{address}\n\n{aqi(address)}\n\n{current_weather(address)}\n\n{forecast(address)}",
                    reply_token,
                    access_token,
                )  # 回覆爬取到的相關氣象資訊
            if (
                json_data["events"][0]["message"]["type"] == "text"
            ):  # 如果 message 的類型是文字 text
                text = json_data["events"][0]["message"]["text"]  # 取出文字
                if text == "地震資訊" or text == "地震":  # 如果是地震相關的文字
                    msg = earth_quake()  # 爬取地震資訊
                    push_message(
                        msg[0], user_id, access_token
                    )  # 傳送地震資訊 ( 用 push 方法，因為 reply 只能用一次 )
                    reply_image(
                        msg[1], reply_token, access_token
                    )  # 傳送地震圖片 ( 用 reply 方法 )
                elif text == "雷達回波圖" or text == "雷達回波":  # 如果是雷達回波圖相關的文字
                    # 傳送雷達回波圖 ( 加上時間戳記 )
                    reply_image(
                        f"https://cwbopendata.s3.ap-northeast-1.amazonaws.com/MSC/O-A0058-001.png?{time.time_ns()}",
                        reply_token,
                        access_token,
                    )
                else:
                    reply_message(text, reply_token, access_token)  # 如果是一般文字，直接回覆同樣的文字
    except:
        print("error")
    return "OK"


# 氣象預報函式
def forecast(address):
    area_list = {}
    # 將主要縣市個別的 JSON 代碼列出
    json_api = {
        "宜蘭縣": "F-D0047-001",
        "桃園市": "F-D0047-005",
        "新竹縣": "F-D0047-009",
        "苗栗縣": "F-D0047-013",
        "彰化縣": "F-D0047-017",
        "南投縣": "F-D0047-021",
        "雲林縣": "F-D0047-025",
        "嘉義縣": "F-D0047-029",
        "屏東縣": "F-D0047-033",
        "臺東縣": "F-D0047-037",
        "花蓮縣": "F-D0047-041",
        "澎湖縣": "F-D0047-045",
        "基隆市": "F-D0047-049",
        "新竹市": "F-D0047-053",
        "嘉義市": "F-D0047-057",
        "臺北市": "F-D0047-061",
        "高雄市": "F-D0047-065",
        "新北市": "F-D0047-069",
        "臺中市": "F-D0047-073",
        "臺南市": "F-D0047-077",
        "連江縣": "F-D0047-081",
        "金門縣": "F-D0047-085",
    }
    msg = "找不到天氣預報資訊。"  # 預設回傳訊息
    try:
        code = "你的氣象資料授權碼"
        url = f"https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/F-C0032-001?Authorization={code}&downloadType=WEB&format=JSON"
        f_data = requests.get(url)  # 取得主要縣市預報資料
        f_data_json = f_data.json()  # json 格式化訊息內容
        location = f_data_json["cwbopendata"]["dataset"]["location"]  # 取得縣市的預報內容
        for i in location:
            city = i["locationName"]  # 縣市名稱
            wx8 = i["weatherElement"][0]["time"][0]["parameter"][
                "parameterName"
            ]  # 天氣現象
            mint8 = i["weatherElement"][1]["time"][0]["parameter"][
                "parameterName"
            ]  # 最低溫
            maxt8 = i["weatherElement"][2]["time"][0]["parameter"][
                "parameterName"
            ]  # 最高溫
            ci8 = i["weatherElement"][2]["time"][0]["parameter"]["parameterName"]  # 舒適度
            pop8 = i["weatherElement"][2]["time"][0]["parameter"][
                "parameterName"
            ]  # 降雨機率
            area_list[
                city
            ] = f"未來 8 小時{wx8}，最高溫 {maxt8} 度，最低溫 {mint8} 度，降雨機率 {pop8} %"  # 組合成回傳的訊息，存在以縣市名稱為 key 的字典檔裡
        for i in area_list:
            if i in address:  # 如果使用者的地址包含縣市名稱
                msg = area_list[i]  # 將 msg 換成對應的預報資訊
                # 將進一步的預報網址換成對應的預報網址
                url = f"https://opendata.cwb.gov.tw/api/v1/rest/datastore/{json_api[i]}?Authorization={code}&elementName=WeatherDescription"
                f_data = requests.get(url)  # 取得主要縣市裡各個區域鄉鎮的氣象預報
                f_data_json = f_data.json()  # json 格式化訊息內容
                location = f_data_json["records"]["locations"][0]["location"]  # 取得預報內容
                break
        for i in location:
            city = i["locationName"]  # 取得縣市名稱
            wd = i["weatherElement"][0]["time"][1]["elementValue"][0]["value"]  # 綜合描述
            if city in address:  # 如果使用者的地址包含鄉鎮區域名稱
                msg = f"未來八小時天氣{wd}"  # 將 msg 換成對應的預報資訊
                break
        return msg  # 回傳 msg
    except:
        return msg  # 如果取資料有發生錯誤，直接回傳 msg


# 目前天氣函式
def current_weather(address):
    city_list, area_list, area_list2 = {}, {}, {}  # 定義好待會要用的變數
    msg = "找不到氣象資訊。"  # 預設回傳訊息

    # 定義取得資料的函式
    def get_data(url):
        w_data = requests.get(url)  # 爬取目前天氣網址的資料
        w_data_json = w_data.json()  # json 格式化訊息內容
        location = w_data_json["cwbopendata"]["location"]  # 取出對應地點的內容
        for i in location:
            name = i["locationName"]  # 測站地點
            city = i["parameter"][0]["parameterValue"]  # 城市
            area = i["parameter"][2]["parameterValue"]  # 行政區
            temp = check_data(i["weatherElement"][3]["elementValue"]["value"])  # 氣溫
            humd = check_data(
                round(float(i["weatherElement"][4]["elementValue"]["value"]) * 100, 1)
            )  # 相對濕度
            r24 = check_data(i["weatherElement"][6]["elementValue"]["value"])  # 累積雨量
            if area not in area_list:
                area_list[area] = {
                    "temp": temp,
                    "humd": humd,
                    "r24": r24,
                }  # 以鄉鎮區域為 key，儲存需要的資訊
            if city not in city_list:
                city_list[city] = {
                    "temp": [],
                    "humd": [],
                    "r24": [],
                }  # 以主要縣市名稱為 key，準備紀錄裡面所有鄉鎮的數值
            city_list[city]["temp"].append(temp)  # 記錄主要縣市裡鄉鎮區域的溫度 ( 串列格式 )
            city_list[city]["humd"].append(humd)  # 記錄主要縣市裡鄉鎮區域的濕度 ( 串列格式 )
            city_list[city]["r24"].append(r24)  # 記錄主要縣市裡鄉鎮區域的雨量 ( 串列格式 )

    # 定義如果數值小於 0，回傳 False 的函式
    def check_data(e):
        return False if float(e) < 0 else float(e)

    # 定義產生回傳訊息的函式
    def msg_content(loc, msg):
        a = msg
        for i in loc:
            if i in address:  # 如果地址裡存在 key 的名稱
                temp = f"氣溫 {loc[i]['temp']} 度，" if loc[i]["temp"] != False else ""
                humd = f"相對濕度 {loc[i]['humd']}%，" if loc[i]["humd"] != False else ""
                r24 = f"累積雨量 {loc[i]['r24']}mm" if loc[i]["r24"] != False else ""
                description = f"{temp}{humd}{r24}".strip("，")
                a = f"{description}。"  # 取出 key 的內容作為回傳訊息使用
                break
        return a

    try:
        # 因為目前天氣有兩組網址，兩組都爬取
        code = "你的氣象資料授權碼"
        get_data(
            f"https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/O-A0001-001?Authorization={code}&downloadType=WEB&format=JSON"
        )
        get_data(
            f"https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/O-A0003-001?Authorization={code}&downloadType=WEB&format=JSON"
        )

        for i in city_list:
            if (
                i not in area_list2
            ):  # 將主要縣市裡的數值平均後，以主要縣市名稱為 key，再度儲存一次，如果找不到鄉鎮區域，就使用平均數值
                area_list2[i] = {
                    "temp": round(statistics.mean(city_list[i]["temp"]), 1),
                    "humd": round(statistics.mean(city_list[i]["humd"]), 1),
                    "r24": round(statistics.mean(city_list[i]["r24"]), 1),
                }
        msg = msg_content(area_list2, msg)  # 將訊息改為「大縣市」
        msg = msg_content(area_list, msg)  # 將訊息改為「鄉鎮區域」
        return msg  # 回傳 msg
    except:
        return msg  # 如果取資料有發生錯誤，直接回傳 msg


# 空氣品質函式
def aqi(address):
    city_list, site_list = {}, {}
    msg = "找不到空氣品質資訊。"
    try:
        # 2022/12 時氣象局有修改了 API 內容，將部份大小寫混合全改成小寫，因此程式碼也跟著修正
        url = "https://data.epa.gov.tw/api/v2/aqx_p_432?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate%20desc&format=JSON"
        a_data = requests.get(url)  # 使用 get 方法透過空氣品質指標 API 取得內容
        a_data_json = a_data.json()  # json 格式化訊息內容
        for i in a_data_json["records"]:  # 依序取出 records 內容的每個項目
            city = i["county"]  # 取出縣市名稱
            if city not in city_list:
                city_list[city] = []  # 以縣市名稱為 key，準備存入串列資料
            site = i["sitename"]  # 取出鄉鎮區域名稱
            aqi = int(i["aqi"])  # 取得 AQI 數值
            status = i["status"]  # 取得空氣品質狀態
            site_list[site] = {"aqi": aqi, "status": status}  # 記錄鄉鎮區域空氣品質
            city_list[city].append(aqi)  # 將各個縣市裡的鄉鎮區域空氣 aqi 數值，以串列方式放入縣市名稱的變數裡
        for i in city_list:
            if i in address:  # 如果地址裡包含縣市名稱的 key，就直接使用對應的內容
                # https://airtw.epa.gov.tw/cht/Information/Standard/AirQualityIndicator.aspx
                aqi_val = round(
                    statistics.mean(city_list[i]), 0
                )  # 計算平均數值，如果找不到鄉鎮區域，就使用縣市的平均值
                aqi_status = ""  # 手動判斷對應的空氣品質說明文字
                if aqi_val <= 50:
                    aqi_status = "良好"
                elif aqi_val > 50 and aqi_val <= 100:
                    aqi_status = "普通"
                elif aqi_val > 100 and aqi_val <= 150:
                    aqi_status = "對敏感族群不健康"
                elif aqi_val > 150 and aqi_val <= 200:
                    aqi_status = "對所有族群不健康"
                elif aqi_val > 200 and aqi_val <= 300:
                    aqi_status = "非常不健康"
                else:
                    aqi_status = "危害"
                msg = f"空氣品質{aqi_status} ( AQI {aqi_val} )。"  # 定義回傳的訊息
                break
        for i in site_list:
            if i in address:  # 如果地址裡包含鄉鎮區域名稱的 key，就直接使用對應的內容
                msg = f'空氣品質{site_list[i]["status"]} ( AQI {site_list[i]["aqi"]} )。'
                break
        return msg  # 回傳 msg
    except:
        return msg  # 如果取資料有發生錯誤，直接回傳 msg


# 地震資訊函式
def earth_quake():
    msg = ["找不到地震資訊", "https://example.com/demo.jpg"]
    try:
        code = "你的氣象資料授權碼"
        url = f"https://opendata.cwb.gov.tw/api/v1/rest/datastore/E-A0016-001?Authorization={code}"
        e_data = requests.get(url)  # 爬取地震資訊網址
        e_data_json = e_data.json()  # json 格式化訊息內容
        eq = e_data_json["records"]["earthquake"]  # 取出地震資訊
        for i in eq:
            loc = i["earthquakeInfo"]["epiCenter"]["location"]  # 地震地點
            val = i["earthquakeInfo"]["magnitude"]["magnitudeValue"]  # 地震規模
            dep = i["earthquakeInfo"]["depth"]["value"]  # 地震深度
            eq_time = i["earthquakeInfo"]["originTime"]  # 地震時間
            img = i["reportImageURI"]  # 地震圖
            msg = [f"{loc}，芮氏規模 {val} 級，深度 {dep} 公里，發生時間 {eq_time}。", img]
            break  # 取出第一筆資料後就 break
        return msg  # 回傳 msg
    except:
        return msg  # 如果取資料有發生錯誤，直接回傳 msg


# LINE 回傳訊息函式
def reply_message(msg, rk, token):
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    body = {"replyToken": rk, "messages": [{"type": "text", "text": msg}]}
    req = requests.request(
        "POST",
        "https://api.line.me/v2/bot/message/reply",
        headers=headers,
        data=json.dumps(body).encode("utf-8"),
    )
    print(req.text)


# LINE 回傳圖片函式
def reply_image(msg, rk, token):
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    body = {
        "replyToken": rk,
        "messages": [
            {"type": "image", "originalContentUrl": msg, "previewImageUrl": msg}
        ],
    }
    req = requests.request(
        "POST",
        "https://api.line.me/v2/bot/message/reply",
        headers=headers,
        data=json.dumps(body).encode("utf-8"),
    )
    print(req.text)


# LINE push 訊息函式
def push_message(msg, uid, token):
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    body = {"to": uid, "messages": [{"type": "text", "text": msg}]}
    req = requests.request(
        "POST",
        "https://api.line.me/v2/bot/message/push",
        headers=headers,
        data=json.dumps(body).encode("utf-8"),
    )
    print(req.text)


# LINE push 圖片函式
def push_image(msg, uid, token):
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    body = {
        "to": uid,
        "messages": [
            {"type": "image", "originalContentUrl": msg, "previewImageUrl": msg}
        ],
    }
    req = requests.request(
        "POST",
        "https://api.line.me/v2/bot/message/push",
        headers=headers,
        data=json.dumps(body).encode("utf-8"),
    )
    print(req.text)


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
