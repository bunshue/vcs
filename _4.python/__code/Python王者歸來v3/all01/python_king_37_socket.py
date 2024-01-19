import socket

host = "127.0.0.1"                                      # 主機的IP
port = 2255                                             # 連接port編號
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # 建立socket物件
s.bind((host, port))                                    # 綁定IP和port
s.listen(5)                                             # TCP監聽
print(f"Server在 {host}:{port}")
print("waiting for connection ...")
while True:
    conn, addr = s.accept()                             # 被動接收客戶連線
    print(f"目前連線網址 {addr} ")
    data = conn.recv(1024)                              # 接收客戶的數據
    print(data)                                         # 列印數據
    conn.sendall(b"HTTP/1.1 200 OK \r\n\r\n Welcome to Deepmind")
    conn.close()                                        # 關閉連線

print("------------------------------------------------------------")  # 60個

import socket
host = "127.0.0.1"                                      # 主機的IP
port = 2255                                             # 連接port編號
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # 建立socket物件
s.connect((host, port))
data = input("請輸入資料 : ")
s.send(data.encode())                       # 轉成 bytes 資料傳送

receive_data = s.recv(1024).decode()        # 接收所傳來的資料同時解成字串
print(f"接收數據 {receive_data}")           # 列印接收的數據
s.close()                                   # 關閉socket

print("------------------------------------------------------------")  # 60個

import socket
host = socket.gethostname()                             # 主機的域名
port = 2255                                             # 連接port編號
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # 建立socket物件
s.bind((host, port))                                    # 綁定IP和port
s.listen()                                              # TCP監聽
print("Server端 : waiting ...")
conn, addr = s.accept()                                 # 被動接收客戶連線
print("Server端:已經連線")
msg = conn.recv(1024).decode()                          # 接收客戶的數據

while msg != "bye":
    if msg:
        print(f"顯示收到內容 : {msg}")                  # 輸出Client訊息
    mydata = input("輸入傳送內容 : ")                   # 讀取輸入內容
    conn.send(mydata.encode())                          # 編碼為bytes後輸出
    if mydata == "bye":                                 # 如果是bye
        break                                           # 離開while迴圈
    print("Server端 : waiting ...")
    msg = conn.recv(1024).decode()                      # 讀取輸入內容
conn.close()
s.close()

print("------------------------------------------------------------")  # 60個

import socket
host = socket.gethostname()                             # 主機的域名
port = 2255                                             # 連接port編號
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # 建立socket物件
s.connect((host, port))                                 # 執行連線
print("Client端 : 已經連線")
msg = ''                                                # 主要是初次連線用

while msg != "bye":
    mydata = input("輸入傳送內容 : ")                   # 讀取輸入內容
    s.send(mydata.encode())                             # 編碼為bytes後輸出
    if mydata == "bye":                                 # 如果是bye
        break                                           # 離開while迴圈
    print("Client端 : waiting ...")
    msg = s.recv(1024).decode()                         # 讀取輸入內容
    print(f"顯示收到內容 : {msg}")                      # 輸出Server訊息                   
s.close()

print("------------------------------------------------------------")  # 60個

import socket
host = host = "127.0.0.1"                               # 主機的域名
port = 2255                                             # 連接port編號
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    # 建立socket物件
s.bind((host, port))                                    # 綁定IP和port
print("Server : 綁定完成")
print("Waiting ...")

f, addr = s.recvfrom(1024)                              # 被動接收客戶數據
print(f"received from {addr}")
c = f.decode()                                          # 將bytes資料解碼
c = (float(f) - 32) * 5 / 9                             # 轉成攝氏溫度
mydata = str(c)                                         # 轉成字串
s.sendto(mydata.encode(), addr)                         # bytes資料編碼再傳送
s.close()

print("------------------------------------------------------------")  # 60個

import socket
host = host = "127.0.0.1"                               # 主機的域名
port = 2255                                             # 連接port編號
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    # 建立socket物件

mydata = input("請輸入華氏溫度 : ")
s.sendto(mydata.encode(), (host, port))                 # 送給伺服器
print(f"攝氏溫度 : {s.recv(1024).decode()}")
s.close()

print("------------------------------------------------------------")  # 60個

import openai

# 設定API金鑰
openai.api_key = 'Your_API_Key'

# 定義對話函數
def chat(messages):
    response = openai.ChatCompletion.create(
        model = "gpt-4",
        messages = messages,
        max_tokens = 150            # 限制回應token數
    )
    return response.choices[0].message['content']

print("歡迎來到深智 Deepwisdom 客服中心")

# 初始化對話串列
messages = [{"role": "system", "content": "你是深智公司客服人員"}]

# 執行對話
while True:
    user_input = input("    客戶 : ")
    if user_input.lower() == "bye":
        print("深智客服 : 感謝您的諮詢，祝您有美好的一天！")
        break
    messages.append({"role": "user", "content": user_input})
    response = chat(messages)
    print("深智客服 : " + response)
    messages.append({"role": "assistant", "content": response})

print("------------------------------------------------------------")  # 60個

import openai

# 設定API金鑰 
openai.api_key = 'Your_API_Key'

# 定義對話函數
def chat(messages):
    response = openai.ChatCompletion.create(
        model = "gpt-4",
        messages = messages,
        max_tokens = 150     # 限制回應token數
    )
    return response.choices[0].message['content']

print("歡迎使用Emoji Translation工具")

# 初始化對話串列
messages = [{"role": "system", "content": "你是emoji翻譯專家"}]

# 執行對話
while True:
    user_input = input("請輸入要翻譯的文字 : ")
    if user_input.lower() == "bye":
        print("Emoji翻譯專家 : 感謝您的使用，再見！👋")
        break
    # 將用戶輸入的文字構建為帶有翻譯要求的問句
    translation_request = f"翻譯下列文字為emojis: '{user_input}'"
    messages.append({"role": "user", "content": translation_request})
    response = chat(messages)
    print("Emoji翻譯專家  : " + response)
    messages.append({"role": "assistant", "content": response})

print("------------------------------------------------------------")  # 60個

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "歡迎來到深智數位"

if __name__ == "__main__":
    app.run()

print("------------------------------------------------------------")  # 60個

from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/index")
@app.route("/hello")
def hello():
    return "歡迎來到深智數位"

if __name__ == "__main__":
    app.run()

print("------------------------------------------------------------")  # 60個

from flask import Flask
app = Flask(__name__)


@app.route("/<name>")
def hello(name):
    return f"Hi! {name} 歡迎光臨深智數位"

if __name__ == "__main__":
    app.run()

print("------------------------------------------------------------")  # 60個

from flask import ( Flask, request, abort )
import os
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi(os.getenv('Channel_token'))
handler = WebhookHandler(os.getenv('Channel_secret'))

# 收Line 訊息
@app.route("/", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    return 'OK'

# Echo 回應, 相當於學你說話
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

print("------------------------------------------------------------")  # 60個

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

print("------------------------------------------------------------")  # 60個

