from flask import Flask
app = Flask(__name__)

from flask import Flask, request, abort
from linebot import  LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextSendMessage, TextMessage

import requests
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

line_bot_api = LineBotApi('使用者Channel access token')
handler = WebhookHandler('使月者Channel secret')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    mtext = event.message.text
    if mtext == '@本期中獎號碼':
        try:
            message = monoNum(0)
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text=message))
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='讀取發票號碼發生錯誤！'))

    elif mtext == '@前期中獎號碼':
        try:
            message = monoNum(1) + '\n\n'
            message += monoNum(2)
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text=message))
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='讀取發票號碼發生錯誤！'))

    elif mtext == '@輸入發票最後三碼':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='請輸入發票最後三碼進行對獎！'))

    elif len(mtext) == 3 and mtext.isdigit():
        try:
            content = requests.get('http://invoice.etax.nat.gov.tw/invoice.xml')
            tree = ET.fromstring(content.text)
            items = list(tree.iter(tag='item'))  #取得item標籤內容
            ptext = items[0][2].text  #中獎號碼
            ptext = ptext.replace('<p>','').replace('</p>','')
            temlist = ptext.split('：')
            prizelist = []  #特別獎或特獎後三碼
            prizelist.append(temlist[1][5:8])
            prizelist.append(temlist[2][5:8])
            for i in range(3):  #頭獎後三碼
                prizelist.append(temlist[3][9*i+5:9*i+8])
            sixlist = temlist[4].split('、')  #增開六獎
            for i in range(len(sixlist)):
                prizelist.append(sixlist[i])
            if mtext in prizelist:
                message = '符合某獎項後三碼，請自行核對發票前五碼！\n\n'
                message += monoNum(0)
            else:
                message = '很可惜，未中獎。請輸入下一張發票最後三碼。'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text=message))
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='讀取發票號碼發生錯誤！'))

    else:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='請輸入發票最後三碼進行對獎！'))

def monoNum(n):
    content = requests.get('http://invoice.etax.nat.gov.tw/invoice.xml')
    tree = ET.fromstring(content.text)  #解析XML
    items = list(tree.iter(tag='item'))  #取得item標籤內容
    title = items[n][0].text  #期別
    ptext = items[n][2].text  #中獎號碼
    ptext = ptext.replace('<p>','').replace('</p>','\n')
    return title + '月\n' + ptext[:-1]  #ptext[:-1]為移除最後一個\n

if __name__ == '__main__':
    app.run()
