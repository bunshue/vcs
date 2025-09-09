import sys

"""
openai  model `text-davinci-003` 已過時
改成
gpt-3.5-turbo-instruct

"""

print('------------------------------------------------------------')	#60個

print("------------------------------------------------------------")  # 60個
print("Python 網頁服務與應用")
print("------------------------------------------------------------")  # 60個

from flask import Flask  # 載入 Flask

app = Flask(__name__)  # 建立 app 變數為 Flask 物件，__name__ 表示目前執行的程式

@app.route("/")  # 使用函式裝飾器，建立一個路由 ( Routes )，可針對主網域 / 發出請求
def home():  # 發出請求後會執行 home() 的函式
    return "<h1>hello world</h1>"  # 執行函式後會回傳特定的網頁內容

app.run()  # 執行

print("------------------------------------------------------------")  # 60個

from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["POST"])
def home():
    return "<h1>hello world</h1>"


app.run()

print("------------------------------------------------------------")  # 60個

url = "http://127.0.0.1:5000/"
response = requests.post(url)  # 使用 post 方法
print(response.text)  # 讀取並印出 text 屬性

print("------------------------------------------------------------")  # 60個

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>hello world</h1>"


app.run(host="0.0.0.0", port=5555)


print("------------------------------------------------------------")  # 60個

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>hello world</h1>"


@app.route("/ok")
def ok():
    return "<h1>ok</h1>"


@app.route("/yes")
def yes():
    return "<h1>yes</h1>"


app.run()

print("------------------------------------------------------------")  # 60個

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>hello world</h1>"


@app.route("/<msg>")  # 加入 <msg> 讀取網址
def ok(msg):  # 加入參數
    return f"<h1>{msg}</h1>"  # 使用變數


app.run()


print("------------------------------------------------------------")  # 60個

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>hello world</h1>"


@app.route("/<path:msg>")  # 加入 path: 轉換成「路徑」的類型
def ok(msg):
    return f"<h1>{msg}</h1>"


app.run()

print("------------------------------------------------------------")  # 60個

from flask import Flask, request  # 載入了 request

app = Flask(__name__)


@app.route("/")
def home():
    print(request.args)  # 使用 request.args
    return "<h1>hello world</h1>"


app.run()

print("------------------------------------------------------------")  # 60個

from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["POST"])
def home():
    print(request.form)  # 使用 request.form
    return "<h1>hello world</h1>"


app.run()


from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def home():
    name = request.args.get("name")
    return render_template("test.html", name=name)


app.run()


print("------------------------------------------------------------")  # 60個

from flask import Flask, request, render_template  # 載入 render_template

app = Flask(__name__)


@app.route("/")
def home():
    name = request.args.get("name")
    return render_template("test.html", name=name)  # 使用網頁樣板，並傳入參數


app.run()

print("------------------------------------------------------------")  # 60個

from flask import Flask

app = Flask(__name__)


@app.route("/<name>")
def home(name):
    return f"<h1>hello {name}</h1>"


app.run()

print("------------------------------------------------------------")  # 60個

from flask import Flask
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)


@app.route("/<name>")
def home(name):
    return f"<h1>hello {name}</h1>"


app.run()


print("------------------------------------------------------------")  # 60個

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
    req = request.get_json()
    print(req)
    reText = req["queryResult"]["fulfillmentText"]
    print(reText)
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

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "dialogflow_key.json"  # 剛剛下載的金鑰 json
project_id = "XXXX"  # dialogflow 的 project id
language = "zh-TW"  # 語系
session_id = "oxxostudio"  # 自訂義的 session id


def dialogflowFn(text):
    session_client = dialogflow.SessionsClient()  # 使用 Token 和 dialogflow 建立連線
    session = session_client.session_path(project_id, session_id)  # 連接對應專案
    text_input = dialogflow.types.TextInput(text=text, language_code=language)  # 設定語系
    query_input = dialogflow.types.QueryInput(text=text_input)  # 根據語系取得輸入內容
    try:
        response = session_client.detect_intent(
            session=session, query_input=query_input
        )  # 連線 Dialogflow 取得回應資料
        print("input:", response.query_result.query_text)
        print("intent:", response.query_result.intent.display_name)
        print("reply:", response.query_result.fulfillment_text)
        return response.query_result.fulfillment_text  # 回傳回應的文字
    except:
        return "error"


app = Flask(__name__)


@app.route("/")
def home():
    text = request.args.get("text")  # 取得輸入的文字
    reply = dialogflowFn(text)  # 取得 Dialogflow 回應的文字
    return reply


app.run()

print("------------------------------------------------------------")  # 60個

import google.cloud.dialogflow_v2 as dialogflow

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "dialogflow_key.json"  # 金鑰 json
project_id = "XXXX"  # dialogflow 的 project id
language = "zh-TW"  # 語系
session_id = "oxxostudio"  # 自訂義的 session id


def dialogflowFn(text):
    session_client = dialogflow.SessionsClient()  # 使用 Token 和 dialogflow 建立連線
    session = session_client.session_path(project_id, session_id)  # 連接對應專案
    text_input = dialogflow.types.TextInput(text=text, language_code=language)  # 設定語系
    query_input = dialogflow.types.QueryInput(text=text_input)  # 根據語系取得輸入內容
    try:
        response = session_client.detect_intent(
            session=session, query_input=query_input
        )  # 連線 Dialogflow 取得回應資料
        print("input:", response.query_result.query_text)
        print("intent:", response.query_result.intent.display_name)
        print("reply:", response.query_result.fulfillment_text)
        return response.query_result.fulfillment_text  # 回傳回應的文字
    except:
        return "error"


def webhook(request):
    try:
        # req = request.get_json()
        text = request.args.get("text")
        return dialogflowFn(text)
    except:
        print(request.args)


print("------------------------------------------------------------")  # 60個

from firebase import firebase

url = "https://XXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)  # 初始化，第二個參數作用在負責使用者登入資訊，通常設定為 None
fdb.put("/", "oxxo", 123)

print("------------------------------------------------------------")  # 60個

from firebase import firebase

url = "https://XXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)
fdb.put("/test", "oxxo", 123)

print("------------------------------------------------------------")  # 60個

from firebase import firebase

url = "https://XXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)
fdb.put("/", "oxxo", {"apple": 100, "orange": 200})

print("------------------------------------------------------------")  # 60個

from firebase import firebase

url = "https://XXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)
fdb.put("/", "oxxo", [123, 456, 789])

print("------------------------------------------------------------")  # 60個

from firebase import firebase

url = "https://XXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)
fdb.post("/", 123)

print("------------------------------------------------------------")  # 60個

from firebase import firebase

url = "https://XXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)
fdb.post("/oxxo", 123)

print("------------------------------------------------------------")  # 60個

from firebase import firebase

url = "https://XXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)
fdb.post("/", {"apple": 100, "orange": 200})

print("------------------------------------------------------------")  # 60個

from firebase import firebase

url = "https://XXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)
result = fdb.get("/", "oxxo")
print(result)  # 123

print("------------------------------------------------------------")  # 60個

from firebase import firebase

url = "https://XXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)
result = fdb.get("/fruit", "apple")
print(result)

print("------------------------------------------------------------")  # 60個

from firebase import firebase

url = "https://XXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)
result = fdb.get("/", None)
print(result)  # {'fruit': {'apple': 100, 'orange': 200}, 'oxxo': 123}
print(result["fruit"]["apple"])  # 100

print("------------------------------------------------------------")  # 60個

from firebase import firebase

url = "https://XXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)
fdb.delete("/", "oxxo")

print("------------------------------------------------------------")  # 60個

from firebase import firebase

url = "https://XXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)
fdb.delete("/", None)

print("------------------------------------------------------------")  # 60個

from firebase import firebase

url = "https://XXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)

for i in range(10):
    fdb.put("/", f"a{i}", time.time())

for i in range(10):
    fdb.put_async("/", f"b{i}", time.time())

print("------------------------------------------------------------")  # 60個

from firebase import firebase

url = "https://XXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)


def oxxo_callback(response):
    print("ok")


fdb.put_async("/", "oxxo", 123, oxxo_callback)  # ok

print("------------------------------------------------------------")  # 60個

from firebase import firebase

url = "https://XXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)

for i in range(10):
    fdb.post("/", time.time())

for i in range(10):
    fdb.post_async("/", time.time())

print("------------------------------------------------------------")  # 60個

from firebase import firebase

url = "https://XXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)


def oxxo_callback(response):
    print("ok")


fdb.post_async("/", 123, oxxo_callback)  # ok

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("openai ST")
print("------------------------------------------------------------")  # 60個

import openai

openai.api_key = "你的 API Key"

response = openai.Completion.create(
    model="text-davinci-003",
    prompt="講個笑話來聽聽",
    max_tokens=128,
    temperature=0.5,
)

completed_text = response["choices"][0]["text"]
print(completed_text)

print("------------------------------------------------------------")  # 60個

import openai

openai.api_key = "你的 API KEY"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    max_tokens=128,
    temperature=0.5,
    messages=[
        {"role": "user", "content": "我叫做 oxxo"},
        {"role": "assistant", "content": "原來你是 oxxo 呀"},
        {"role": "user", "content": "請問我叫什麼名字？"},
    ],
)
print(response.choices[0].message.content)

print("------------------------------------------------------------")  # 60個

import openai

openai.api_key = "你的 API Key"

messages = ""
while True:
    msg = input("me > ")
    messages = f"{messages}{msg}\n"  # 將過去的語句連接目前的對話，後方加上 \n 可以避免標點符號結尾問題
    response = openai.Completion.create(
        model="text-davinci-003", prompt=messages, max_tokens=128, temperature=0.5
    )

    ai_msg = response["choices"][0]["text"].replace("\n", "")
    print("ai > " + ai_msg)
    messages = f"{messages}\n{ai_msg}\n\n"  # 合併 AI 回應的話

print("------------------------------------------------------------")  # 60個

import openai

openai.api_key = "你的 API Key"

messages = []
while True:
    msg = input("me > ")
    messages.append({"role": "user", "content": msg})  # 添加 user 回應
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", max_tokens=128, temperature=0.5, messages=messages
    )
    ai_msg = response.choices[0].message.content.replace("\n", "")
    messages.append({"role": "assistant", "content": ai_msg})  # 添加 ChatGPT 回應
    print(f"ai > {ai_msg}")

print("------------------------------------------------------------")  # 60個

import openai

openai.api_key = "你的 API Key"

from firebase import firebase

url = "https://XXXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)  # 初始化 Firebase Realtime database
chatgpt = fdb.get("/", "chatgpt")  # 取的 chatgpt 節點的資料

if chatgpt == None:
    messages = ""  # 如果節點沒有資料，訊息內容設定為空
else:
    messages = chatgpt  # 如果節點有資料，使用該資料作為歷史聊天記錄

while True:
    msg = input("me > ")
    if msg == "!reset":
        message = ""
        fdb.delete("/", "chatgpt")  # 如果輸入 !reset 就清空歷史紀錄
        print("ai > 對話歷史紀錄已經清空！")
    else:
        messages = f"{messages}{msg}\n"  # 在輸入的訊息前方加上歷史紀錄
        response = openai.Completion.create(
            model="text-davinci-003", prompt=messages, max_tokens=128, temperature=0.5
        )

        ai_msg = response["choices"][0]["text"].replace("\n", "")  # 取得 ChatGPT 的回應
        print("ai > " + ai_msg)
        messages = f"{messages}\n{ai_msg}\n\n"  # 在訊息中加入 ChatGPT 的回應
        fdb.put("/", "chatgpt", messages)  # 更新資料庫資料


print("------------------------------------------------------------")  # 60個

import openai

openai.api_key = "你的 API Key"

from firebase import firebase

url = "https://XXXXXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)  # 初始化 Firebase Realtimr database
chatgpt = fdb.get("/", "chatgpt")  # 讀取 chatgpt 節點中所有的資料

if chatgpt == None:
    messages = []  # 如果沒有資料，預設訊息為空串列
else:
    messages = chatgpt  # 如果有資料，訊息設定為該資料

while True:
    msg = input("me > ")
    if msg == "!reset":
        fdb.delete("/", "chatgpt")  # 如果輸入 !reset 就清空 chatgpt 的節點內容
        messages = []
        print("ai > 對話歷史紀錄已經清空！")
    else:
        messages.append({"role": "user", "content": msg})  # 將輸入的訊息加入歷史紀錄的串列中
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", max_tokens=128, temperature=0.5, messages=messages
        )
        ai_msg = response.choices[0].message.content.replace("\n", "")  # 取得回應訊息
        messages.append({"role": "assistant", "content": ai_msg})  # 將回應訊息加入歷史紀錄串列中
        fdb.put("/", "chatgpt", messages)  # 更新 chatgpt 節點內容
        print(f"ai > {ai_msg}")


print("------------------------------------------------------------")  # 60個
print("openai SP")
print("------------------------------------------------------------")  # 60個




print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個





