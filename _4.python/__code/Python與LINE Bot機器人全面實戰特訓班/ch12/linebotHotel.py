from flask import Flask
app = Flask(__name__)

from flask import request, abort, render_template
from flask_sqlalchemy import SQLAlchemy
from linebot import  LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, PostbackEvent, ImageSendMessage, LocationSendMessage, TemplateSendMessage, ButtonsTemplate, URITemplateAction, ConfirmTemplate, PostbackTemplateAction
from urllib.parse import parse_qsl

# 定義 LINE Bot Channel Secret 及 Access Token
line_bot_api = LineBotApi('你的 CHANNEL_ACCESS_TOKEN')
handler = WebhookHandler('你的 CHANNEL_SECRET')
# 定義 PostgreSQL 連線字串
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://管理者名稱:管理者密碼@127.0.0.1:5432/hotel'
db = SQLAlchemy(app)
# 定義 LIFF ID
liffid = '申請的LIFF ID'

#LIFF靜態頁面
@app.route('/page')
def page():
	return render_template('hotel_form.html', liffid = liffid)
	
# 重置資料庫
@app.route('/createdb')
def createdb():
    sql = """
    DROP TABLE IF EXISTS hoteluser, booking;

    CREATE TABLE hoteluser (
    id serial NOT NULL,
    uid character varying(50) NOT NULL,
    PRIMARY KEY (id));

    CREATE TABLE booking (
    id serial NOT NULL,
    bid character varying(50) NOT NULL,
    roomtype character varying(20) NOT NULL,
    roomamount character varying(5) NOT NULL,
    datein character varying(20) NOT NULL,
    dateout character varying(20) NOT NULL,
    PRIMARY KEY (id))
    """
    db.engine.execute(sql)    
    return "資料表建立成功！"

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
    user_id = event.source.user_id
    sql_cmd = "select * from hoteluser where uid='" + user_id + "'"
    query_data = db.engine.execute(sql_cmd)
    if len(list(query_data)) == 0:
        sql_cmd = "insert into hoteluser (uid) values('" + user_id + "');"
        db.engine.execute(sql_cmd)

    mtext = event.message.text
    if mtext == '@使用說明':
        sendUse(event)

    elif mtext == '@房間預約':
        sendBooking(event, user_id)

    elif mtext == '@取消訂房':
        sendCancel(event, user_id)

    elif mtext == '@關於我們':
        sendAbout(event)

    elif mtext == '@位置資訊':
        sendPosition(event)

    elif mtext == '@聯絡我們':
        sendContact(event)

    elif mtext[:3] == '###' and len(mtext) > 3:  #處理LIFF傳回的FORM資料
         manageForm(event, mtext, user_id)

    elif mtext[:6] == '123456' and len(mtext) > 6:  #推播給所有顧客
         pushMessage(event, mtext)

@handler.add(PostbackEvent)  #PostbackTemplateAction觸發此事件
def handle_postback(event):
    backdata = dict(parse_qsl(event.postback.data))  #取得Postback資料
    if backdata.get('action') == 'yes':
        sendYes(event, event.source.user_id)
    else:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='你已放棄取消訂房操作！'))

def sendUse(event):  #使用說明
    try:
        text1 ='''
1. 「房間預約」及「取消訂房」可預訂及取消訂房。每個 LINE 帳號只能進行一個預約記錄。
2. 「關於我們」對旅館做簡單介紹及旅館圖片。
3. 「位置資料」列出旅館地址，並會顯示地圖。
4. 「聯絡我們」可直接撥打電話與我們聯繫。
               '''
        message = TextSendMessage(
            text = text1
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendBooking(event, user_id):  #房間預約
    try:
        sql_cmd = "select * from booking where bid='" + user_id + "'"
        query_data = db.engine.execute(sql_cmd)
        if len(list(query_data)) == 0:
            message = TemplateSendMessage(
                alt_text = "房間預約",
                template = ButtonsTemplate(
                    thumbnail_image_url='https://i.imgur.com/1NSDAvo.jpg',
                    title='房間預約',
                    text='您目前沒有訂房記錄，可以開始預訂房間。',
                    actions=[
                        URITemplateAction(label='房間預約', uri='https://liff.line.me/' + liffid)  #開啟LIFF讓使用者輸入訂房資料
                    ]
                )
            )
        else:  #已有訂房記錄
            message = TextSendMessage(
                text = '您目前已有訂房記錄，不能再訂房。'
            )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendCancel(event, user_id):  #取消訂房
    try:
        sql_cmd = "select * from booking where bid='" + user_id + "'"
        query_data = db.engine.execute(sql_cmd)
        bookingdata = list(query_data)
        if len(bookingdata) > 0:
            roomtype = bookingdata[0][2]
            amount = bookingdata[0][3]
            in_date = bookingdata[0][4]
            out_date = bookingdata[0][5]
            text1 = "您預訂的房間資料如下："
            text1 += "\n房間型式：" + roomtype
            text1 += "\n房間數量：" + amount
            text1 += "\n入住日期：" + in_date
            text1 += "\n退房日期：" + out_date
            message = [
                TextSendMessage(  #顯示訂房資料
                    text = text1
                ),
                TemplateSendMessage(  #顯示確認視窗
                    alt_text='取消訂房確認',
                    template=ConfirmTemplate(
                        text='你確定要取消訂房嗎？',
                        actions=[
                            PostbackTemplateAction(  #按鈕選項
                                label='是',
                                data='action=yes'
                            ),
                            PostbackTemplateAction(
                                label='否',
                                data='action=no'
                           )
                        ]
                    )
                )
            ]
        else:  #沒有訂房記錄
            message = TextSendMessage(
                text = '您目前沒有訂房記錄！'
            )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendAbout(event):  #關於我們
    try:
        text1 = "我們提供良好的環境及優質的住宿服務，使您有賓至如歸的感受，歡迎來體驗美好的經歷。"
        message = [
            TextSendMessage(  #旅館簡介
                text = text1
            ),
            ImageSendMessage(  #旅館圖片
                original_content_url = "https://i.imgur.com/1NSDAvo.jpg",
                preview_image_url = "https://i.imgur.com/1NSDAvo.jpg"
            ),
        ]
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendPosition(event):  #位置資訊
    try:
        text1 = "地址：南投縣埔里鎮信義路85號"
        message = [
            TextSendMessage(  #顯示地址
                text = text1
            ),
            LocationSendMessage(  #顯示地圖
                title = "宜居旅舍",
                address = text1,
                latitude = 23.97381,
                longitude = 120.977198
            ),
        ]
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendContact(event):  #聯絡我們
    try:
        message = TemplateSendMessage(
            alt_text = "聯絡我們",
            template = ButtonsTemplate(
                thumbnail_image_url='https://i.imgur.com/tVjKzPH.jpg',
                title='聯絡我們',
                text='打電話給我們',
                actions=[
                    URITemplateAction(label='撥打電話', uri='tel:0123456789')  #開啟打電話功能
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def manageForm(event, mtext, user_id):  #處理LIFF傳回的FORM資料
    try:
        flist = mtext[3:].split('/')  #去除前三個「#」字元再分解字串
        roomtype = flist[0]  #取得輸入資料
        amount = flist[1]
        in_date = flist[2]
        out_date = flist[3]
        sql_cmd = "insert into booking (bid, roomtype, roomamount, datein, dateout) values('" + user_id + "', '" + roomtype + "', '" + amount + "', '" + in_date + "', '" + out_date + "');"
        db.engine.execute(sql_cmd)
        text1 = "您的房間已預訂成功，資料如下："
        text1 += "\n房間型式：" + roomtype
        text1 += "\n房間數量：" + amount
        text1 += "\n入住日期：" + in_date
        text1 += "\n退房日期：" + out_date
        message = TextSendMessage(  #顯示訂房資料
            text = text1
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendYes(event, user_id):  #處理取消訂房
    try:
        sql_cmd = "delete from booking where bid='" + user_id + "'"
        db.engine.execute(sql_cmd)
        message = TextSendMessage(
            text = "您的房間預訂已成功刪除。\n期待您再次預訂房間，謝謝！"
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def pushMessage(event, mtext):  ##推播訊息給所有顧客
    try:
        msg = mtext[6:]  #取得訊息
        sql_cmd = "select * from hoteluser"
        query_data = db.engine.execute(sql_cmd)
        userall = list(query_data)
        for user in userall:  #逐一推播
            message = TextSendMessage(
                text = msg
            )
            line_bot_api.push_message(to=user[1], messages=[message])  #推播訊息
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

if __name__ == '__main__':
    app.run()