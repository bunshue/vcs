"""
一本精通 - LINE BOT 開發技巧
"""


import os
import sys
import time
import random


print("------------------------------------------------------------")  # 60個

from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>hello world</h1>"


@app.route("/webhook", methods=["POST"])
def webhook():
    # 轉換成 dict 格式
    req = request.get_json()
    print(req)
    # 取得回覆文字
    reText = req["queryResult"]["fulfillmentText"]
    print(reText)
    # 在回覆的文字後方加上 ( webhook ) 識別
    return {"fulfillmentText": f"{reText} ( webhook )", "source": "webhookdata"}

app.run()

print("------------------------------------------------------------")  # 60個

from flask import Flask, request
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)  # 連結 ngrok


@app.route("/")
def home():
    return "<h1>hello world</h1>"


@app.route("/webhook", methods=["POST"])
def webhook():
    # 轉換成 dict 格式
    req = request.get_json()
    print(req)
    # 取得回覆文字
    reText = req["queryResult"]["fulfillmentText"]
    print(reText)
    # 在回覆的文字後方加上 ( webhook ) 識別
    return {"fulfillmentText": f"{reText} ( webhook )", "source": "webhookdata"}


app.run()

print("------------------------------------------------------------")  # 60個


def webhook(request):
    try:
        req = request.get_json()
        reText = req["queryResult"]["fulfillmentText"]
        return {"fulfillmentText": f"{reText} ( webhook )", "source": "webhookdata"}
    except:
        print(request.args)


print("------------------------------------------------------------")  # 60個

import google.cloud.dialogflow_v2 as dialogflow
from flask import Flask, request

# 讀取下載的金鑰 json
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "dialogflow_key.json"
project_id = "XXXX"  # dialogflow 的 project id
language = "zh-TW"  # 語系
session_id = "oxxostudio"  # 自訂義的 session id


# 建立連接 Dialogflow 的函式
def dialogflowFn(text):
    # 使用 Token 和 dialogflow 建立連線
    session_client = dialogflow.SessionsClient()
    # 連接對應專案
    session = session_client.session_path(project_id, session_id)
    # 設定語系
    text_input = dialogflow.types.TextInput(text=text, language_code=language)
    # 根據語系取得輸入內容
    query_input = dialogflow.types.QueryInput(text=text_input)
    try:
        # 連線 Dialogflow 取得回應資料
        response = session_client.detect_intent(
            session=session, query_input=query_input
        )
        # 印出相關資訊
        print("input:", response.query_result.query_text)
        print("intent:", response.query_result.intent.display_name)
        print("reply:", response.query_result.fulfillment_text)
        # 回傳回應的文字
        return response.query_result.fulfillment_text
    except:
        return "error"


app = Flask(__name__)


@app.route("/")
def home():
    # 取得輸入的文字
    text = request.args.get("text")
    # 透過 Dialogflow 得到回應的文字
    reply = dialogflowFn(text)
    return reply


app.run()

print("------------------------------------------------------------")  # 60個

import google.cloud.dialogflow_v2 as dialogflow

# 金鑰 json
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "dialogflow_key.json"
project_id = "XXXX"  # dialogflow 的 project id
language = "zh-TW"  # 語系
session_id = "oxxostudio"  # 自訂義的 session id


def dialogflowFn(text):
    # 使用 Token 和 dialogflow 建立連線
    session_client = dialogflow.SessionsClient()
    # 連接對應專案
    session = session_client.session_path(project_id, session_id)
    # 設定語系
    text_input = dialogflow.types.TextInput(text=text, language_code=language)
    # 根據語系取得輸入內容
    query_input = dialogflow.types.QueryInput(text=text_input)
    try:
        # 連線 Dialogflow 取得回應資料
        response = session_client.detect_intent(
            session=session, query_input=query_input
        )
        print("input:", response.query_result.query_text)
        print("intent:", response.query_result.intent.display_name)
        print("reply:", response.query_result.fulfillment_text)
        # 回傳回應的文字
        return response.query_result.fulfillment_text
    except:
        return "error"


def webhook(request):
    try:
        text = request.args.get("text")
        return dialogflowFn(text)
    except:
        print(request.args)


print("------------------------------------------------------------")  # 60個

from flask_ngrok import run_with_ngrok

from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>hello world</h1>"


@app.route("/webhook", methods=["POST"])
def webhook():
    req = request.get_json()  # 轉換成 dict 格式
    print(req)
    reText = req["queryResult"]["fulfillmentText"]  # 取得回覆文字
    print(reText)
    return {"fulfillmentText": f"{reText} ( webhook )", "source": "webhookdata"}

run_with_ngrok(app)

app.run()

print("------------------------------------------------------------")  # 60個

from flask import Flask, request
import requests, json, time

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>hello world</h1>"


@app.route("/webhook", methods=["POST"])
def webhook():
    req = request.get_json()
    print(req)
    # 取得 Dialogflow 的回應文字
    reText = req["queryResult"]["fulfillmentText"]
    # 取得 intent 分類
    intent = req["queryResult"]["intent"]["displayName"]
    # 取得 LINE replyToken
    replytoken = req["originalDetectIntentRequest"]["payload"]["data"]["replyToken"]
    token = "你的 LINE BOT Access Token"
    # 雷達回波圖網址，後方加上時間戳記，避免緩存
    img = f"https://cwbopendata.s3.ap-northeast-1.amazonaws.com/MSC/O-A0058-003.png?{time.time_ns()}"
    # 如果收到的 intent 是 radar
    if intent == "radar":
        headers = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json",
        }
        body = {
            "replyToken": replytoken,
            "messages": [
                {"type": "image", "originalContentUrl": img, "previewImageUrl": img}
            ],
        }
        # 使用 requests 方法回傳訊息到 ＬINE
        result = requests.request(
            "POST",
            "https://api.line.me/v2/bot/message/reply",
            headers=headers,
            data=json.dumps(body).encode("utf-8"),
        )
        print(result.text)
        # 完成後回傳訊息到 Dialogflow
        return {"source": "webhookdata"}
    # 如果收到的 intent 不是 radar
    else:
        # 使用 Dialogflow 產生的回應訊息
        return {"fulfillmentText": f"{reText} ( webhook )"}


app.run()

print("------------------------------------------------------------")  # 60個


from flask import Flask, request
import requests, json, time
from flask_ngrok import run_with_ngrok

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>hello world</h1>"


@app.route("/webhook", methods=["POST"])
def webhook():
    req = request.get_json()
    print(req)
    # 取得 Dialogflow 的回應文字
    reText = req["queryResult"]["fulfillmentText"]
    # 取得 intent 分類
    intent = req["queryResult"]["intent"]["displayName"]
    # 取得 LINE replyToken
    replytoken = req["originalDetectIntentRequest"]["payload"]["data"]["replyToken"]
    token = "你的 Access Token"
    # 雷達回波圖網址，後方加上時間戳記，避免緩存
    img = f"https://cwbopendata.s3.ap-northeast-1.amazonaws.com/MSC/O-A0058-003.png?{time.time_ns()}"
    # 如果收到的 intent 是 radar
    if intent == "radar":
        headers = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json",
        }
        body = {
            "replyToken": replytoken,
            "messages": [
                {"type": "image", "originalContentUrl": img, "previewImageUrl": img}
            ],
        }
        # 使用 requests 方法回傳訊息到 ＬINE
        result = requests.request(
            "POST",
            "https://api.line.me/v2/bot/message/reply",
            headers=headers,
            data=json.dumps(body).encode("utf-8"),
        )
        print(result.text)
        # 完成後回傳訊息到 Dialogflow
        return {"source": "webhookdata"}
    # 如果收到的 intent 不是 radar
    else:
        # 使用 Dialogflow 產生的回應訊息
        return {"fulfillmentText": f"{reText} ( webhook )"}


run_with_ngrok(app)  # 啟用 ngrok
app.run()

print("------------------------------------------------------------")  # 60個

import requests, json, time


def webhook(request):
    try:
        req = request.get_json()
        reText = req["queryResult"]["fulfillmentText"]
        intent = req["queryResult"]["intent"]["displayName"]
        replytoken = req["originalDetectIntentRequest"]["payload"]["data"]["replyToken"]
        token = "你的 LINE BOT Access Token"
        img = f"https://cwbopendata.s3.ap-northeast-1.amazonaws.com/MSC/O-A0058-003.png?{time.time_ns()}"
        if intent == "radar":
            headers = {
                "Authorization": "Bearer " + token,
                "Content-Type": "application/json",
            }
            body = {
                "replyToken": replytoken,
                "messages": [
                    {"type": "image", "originalContentUrl": img, "previewImageUrl": img}
                ],
            }
            result = requests.request(
                "POST",
                "https://api.line.me/v2/bot/message/reply",
                headers=headers,
                data=json.dumps(body).encode("utf-8"),
            )
            print(result.text)
            return {"source": "webhookdata"}
        else:
            return {"fulfillmentText": f"{reText} ( webhook )"}
    except:
        print(request.args)


print("------------------------------------------------------------")  # 60個

import google.cloud.dialogflow_v2 as dialogflow
from flask import Flask, request

# 載入 json 標準函式庫，處理回傳的資料格式
import json

# 載入 LINE Message API 相關函式庫
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "dialogflow_key.json"  # 金鑰 json
project_id = "XXXX"  # dialogflow project id
language = "zh-TW"  # 語系
session_id = "oxxostudio"  # 自訂 session id


# dialogflow 處理自然語言
def dialogflowFn(text):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    text_input = dialogflow.types.TextInput(text=text, language_code=language)
    query_input = dialogflow.types.QueryInput(text=text_input)
    print(query_input)
    try:
        response = session_client.detect_intent(
            session=session, query_input=query_input
        )
        print("input:", response.query_result.query_text)
        print("intent:", response.query_result.intent.display_name)
        print("reply:", response.query_result.fulfillment_text)
        return response.query_result.fulfillment_text
    except:
        return "error"


app = Flask(__name__)


@app.route("/", methods=["POST"])
def linebot():
    # 取得收到的訊息內容
    body = request.get_data(as_text=True)
    try:
        # json 格式化訊息內容
        json_data = json.loads(body)
        access_token = "Access Token"
        secret = "Channel Secret"
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
        # 取得 LINE 收到的文字訊息
        if type == "text":
            msg = json_data["events"][0]["message"]["text"]
            # 印出內容
            print(msg)
            # dialogflow 處理後回傳文字
            reply = dialogflowFn(msg)
        else:
            reply = "你傳的不是文字呦～"
        print(reply)
        # 回傳訊息
        line_bot_api.reply_message(tk, TextSendMessage(reply))
    except:
        print(body)
    # 驗證 Webhook 使用，不能省略
    return "OK"


if __name__ == "__main__":
    app.run()

print("------------------------------------------------------------")  # 60個

import google.cloud.dialogflow_v2 as dialogflow

import json
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

# 剛剛下載的金鑰 json
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "dialogflow_key.json"
project_id = "XXXXX"  # dialogflow 的 project id
language = "zh-TW"  # 語系
session_id = "oxxostudio"  # 自訂義的 session id


def dialogflowFn(text):
    # 使用 Token 和 dialogflow 建立連線
    session_client = dialogflow.SessionsClient()
    # 連接對應專案
    session = session_client.session_path(project_id, session_id)
    # 設定語系
    text_input = dialogflow.types.TextInput(text=text, language_code=language)
    # 根據語系取得輸入內容
    query_input = dialogflow.types.QueryInput(text=text_input)
    try:
        # 連線 Dialogflow 取得回應資料
        response = session_client.detect_intent(
            session=session, query_input=query_input
        )
        print("input:", response.query_result.query_text)
        print("intent:", response.query_result.intent.display_name)
        print("reply:", response.query_result.fulfillment_text)
        # 回傳回應的文字
        return response.query_result.fulfillment_text
    except:
        return "error"


def webhook(request):
    # 取得收到的訊息內容
    body = request.get_data(as_text=True)
    try:
        # json 格式化訊息內容
        json_data = json.loads(body)
        access_token = "Access Token"
        secret = "Channel Secret"
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
            reply = dialogflowFn(msg)
        else:
            reply = "你傳的不是文字呦～"
        print(reply)
        # 回傳訊息
        line_bot_api.reply_message(tk, TextSendMessage(reply))
    except:
        print(body)
    # 驗證 Webhook 使用，不能省略
    return "OK"


print("------------------------------------------------------------")  # 60個

import requests

url = "https://notify-api.line.me/api/notify"
token = "剛剛複製的權杖"
headers = {"Authorization": "Bearer " + token}  # 設定權杖
data = {"message": "測試一下！"}  # 設定要發送的訊息
# 使用 POST 方法發送訊息
data = requests.post(url, headers=headers, data=data)

print("------------------------------------------------------------")  # 60個

import requests

url = "https://notify-api.line.me/api/notify"
token = "剛剛複製的權杖"
headers = {"Authorization": "Bearer " + token}
data = {"message": "測試一下！", "stickerPackageId": "446", "stickerId": "1989"}
data = requests.post(url, headers=headers, data=data)

print("------------------------------------------------------------")  # 60個

import requests

url = "https://notify-api.line.me/api/notify"
token = "剛剛複製的權杖"
headers = {"Authorization": "Bearer " + token}
data = {
    "message": "測試一下！",
    "imageThumbnail": "https://steam.oxxostudio.tw/downlaod/python/line-notify-demo.png",
    "imageFullsize": "https://steam.oxxostudio.tw/downlaod/python/line-notify-demo.png",
}
data = requests.post(url, headers=headers, data=data)

print("------------------------------------------------------------")  # 60個

import requests

url = "https://notify-api.line.me/api/notify"
# 自己申請的 LINE Notify 權杖
token = "你的 LINE Notify 權杖"
# POST 使用的 headers
headers = {"Authorization": "Bearer " + token}
# POST 使用的 data
data = {
    "message": "從雷達回波看看會不會下雨～",
    "imageThumbnail": "https://cwbopendata.s3.ap-northeast-1.amazonaws.com/MSC/O-A0058-003.png",
    "imageFullsize": "https://cwbopendata.s3.ap-northeast-1.amazonaws.com/MSC/O-A0058-003.png",
}
data = requests.post(url, headers=headers, data=data)

print("------------------------------------------------------------")  # 60個

import requests

url = "https://notify-api.line.me/api/notify"
token = "你的 LINE Notify 權杖"
headers = {"Authorization": "Bearer " + token}
radar_img = "https://cwbopendata.s3.ap-northeast-1.amazonaws.com/MSC/O-A0058-003.png"
time_now = str(time.time_ns())  # 取得目前時間
data = {
    "message": "從雷達回波看看會不會下雨～",
    "imageThumbnail": radar_img + "?" + time_now,  # 加上時間參數
    "imageFullsize": radar_img + "?" + time_now,  # 加上時間參數
}
data = requests.post(url, headers=headers, data=data)

print("------------------------------------------------------------")  # 60個

def hello_world(request):
    request_json = request.get_json()
    print(request.args)  # 讀取 GET 方法參數
    print(request.form)  # 讀取 POST 方法參數
    print(request.path)  # 讀取網址
    print(request.method)  # 讀取叫用方法
    if request.args and "message" in request.args:
        return request.args.get("message")
    elif request_json and "message" in request_json:
        return request_json["message"]
    else:
        return f"Hello World!"


print("------------------------------------------------------------")  # 60個

def hello_world(request):
    request_json = request.get_json()
    print(request.args)  # 讀取 GET 方法參數
    print(request.form)  # 讀取 POST 方法參數
    print(request.path)  # 讀取網址
    print(request.method)  # 讀取叫用方法

    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "Content-Type",
        "Access-Control-Max-Age": "3600",
    }

    return ("Hello World!", 200, headers)  # 回傳同意跨域的 header


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
