from flask import Flask
app = Flask(__name__)

from flask import request, abort
from flask_sqlalchemy import SQLAlchemy
from linebot import  LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import requests
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

line_bot_api = LineBotApi('你的 CHANNEL_ACCESS_TOKEN')
handler = WebhookHandler('你的 CHANNEL_SECRET')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://管理者名稱:管理者密碼@127.0.0.1:5432/invoice'
db = SQLAlchemy(app)

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    userid = event.source.user_id
    sql_cmd = "select * from users where uid='" + userid + "'"
    query_data = db.engine.execute(sql_cmd)
    if len(list(query_data)) == 0:
        sql_cmd = "insert into users (uid, state, digit3) values('" + userid + "', 'no', 'no');"
        db.engine.execute(sql_cmd)
    else:
        query_data = db.engine.execute(sql_cmd)
        listdata = list(query_data)[0]
        mode = listdata[2]
        digit3 = listdata[3]
    mtext = event.message.text
    if mtext == '@使用說明':
        sendUse(event)

    elif mtext == '@顯示本期中獎號碼':
        showCurrent(event)

    elif mtext == '@顯示前期中獎號碼':
        showOld(event)

    elif mtext == '@輸入發票最後三碼':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='請輸入發票最後三碼進行對獎！'))

    elif len(mtext) == 3 and mtext.isdigit():
        show3digit(event, mtext, userid)

    elif len(mtext) == 5 and mtext.isdigit():
        show5digit(event, mtext, userid, mode, digit3)

def sendUse(event):  #使用說明
    try:
        text1 ='''
1. 「對獎」功能會提示使用者輸入發票最後三碼，若最後三碼有中獎，就提示使用者輸入發票前五碼。
2. 為方便使用者輸入，也可以直接輸入發票最後三碼直接對獎 (不需按「對獎」項目)。
3. 「前期中獎號碼」功能會顯示前兩期發票中獎號碼。
4. 「本期中獎號碼」功能會顯示最近一期發票中獎號碼。
               '''
        message = TextSendMessage(
            text = text1
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def showCurrent(event):
    try:
        content = requests.get('http://invoice.etax.nat.gov.tw/invoice.xml')
        tree = ET.fromstring(content.text)  #解析XML
        items = list(tree.iter(tag='item'))  #取得item標籤內容
        title = items[0][0].text  #期別
        ptext = items[0][2].text  #中獎號碼
        ptext = ptext.replace('<p>','').replace('</p>','\n')
        message = title + '月\n' + ptext[:-1]  #ptext[:-1]為移除最後一個\n
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=message))
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='讀取發票號碼發生錯誤！'))

def showOld(event):
    try:
        content = requests.get('http://invoice.etax.nat.gov.tw/invoice.xml')
        tree = ET.fromstring(content.text)  #解析XML
        items = list(tree.iter(tag='item'))  #取得item標籤內容
        message = ''
        for i in range(1,3):
            title = items[i][0].text  #期別
            ptext = items[i][2].text  #中獎號碼
            ptext = ptext.replace('<p>','').replace('</p>','\n')
            message = message + title + '月\n' + ptext + '\n'
        message = message[:-2]
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=message))
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='讀取發票號碼發生錯誤！'))

def show3digit(event, mtext, userid):
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
        prize6list1 = []  #頭獎後三碼六獎中獎號碼
        for i in range(3):
            prize6list1.append(temlist[3][9*i+5:9*i+8])
        prize6list2 = temlist[4].split('、')  #增開六獎
        sql_cmd = "update users set state='no', digit3='no' where uid='" + userid +"'"
        db.engine.execute(sql_cmd)
        if mtext in prizelist:
            message = '符合特別獎或特獎後三碼，請繼續輸入發票前五碼！'
            sql_cmd = "update users set state='special', digit3='" + mtext + "' where uid='" + userid +"'"
            db.engine.execute(sql_cmd)
        elif mtext in prize6list1:
            message = '恭喜！至少中六獎，請繼續輸入發票前五碼！'
            sql_cmd = "update users set state='head', digit3='" + mtext + "' where uid='" + userid +"'"
            db.engine.execute(sql_cmd)
        elif mtext in prize6list2:
            message = '恭喜！此張發票中了六獎！'
        else:
            message = '很可惜，未中獎。請輸入下一張發票最後三碼。'
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=message))
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='讀取發票號碼發生錯誤！'))

def show5digit(event, mtext, userid, mode, digit3):
    try:
        sql_cmd = "select * from users where uid='" + userid + "'"
        if mode == 'no':
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='請先輸入發票最後三碼！'))
        else:
            try:
                content = requests.get('http://invoice.etax.nat.gov.tw/invoice.xml')
                tree = ET.fromstring(content.text)  #解析DOM
                items = list(tree.iter(tag='item'))  #取得item標籤內容
                ptext = items[0][2].text  #中獎號碼
                ptext = ptext.replace('<p>','').replace('</p>','')
                temlist = ptext.split('：')
                special1 = temlist[1][0:5]  #特別獎前五碼
                special2 = temlist[2][0:5]  #特獎前五碼
                prizehead = []  #頭獎
                for i in range(3):
                    prizehead.append(temlist[3][9*i:9*i+8])
                sflag = False  #記錄是否中特別獎或特獎
                if mode=='special' and mtext==special1:
                    message = '恭喜！此張發票中了特別獎！'
                    sflag = True
                elif mode=='special' and mtext==special2:
                    message = '恭喜！此張發票中了特獎！'
                    sflag = True
                if mode=='special' and sflag==False:
                    message = '很可惜，未中獎。請輸入下一張發票最後三碼。'
                elif mode=='head' and sflag==False:
                    for i in range(3):
                        if digit3 == prizehead[i][5:8]:
                            pnumber = prizehead[i]  #中獎的頭獎號碼
                            break
                    if mtext == pnumber[:5]:
                        message = '恭喜！此張發票中了頭獎！'
                    elif mtext[1:5] == pnumber[1:5]:
                        message = '恭喜！此張發票中了二獎！'
                    elif mtext[2:5] == pnumber[2:5]:
                        message = '恭喜！此張發票中了三獎！'
                    elif mtext[3:5] == pnumber[3:5]:
                        message = '恭喜！此張發票中了四獎！'
                    elif mtext[4] == pnumber[4]:
                        message = '恭喜！此張發票中了五獎！'
                    else:
                        message = '恭喜！此張發票中了六獎！'
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text=message))
                sql_cmd = "update users set state='no', digit3='no' where uid='" + userid +"'"
                db.engine.execute(sql_cmd)
            except:
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text='讀取發票號碼發生錯誤！'))
    except:
        sql_cmd = "update users set set state='no', digit3='no' where uid='" + userid +"'"
        db.engine.execute(sql_cmd)
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='模式文字檔讀取錯誤！'))

if __name__ == '__main__':
    app.run()
