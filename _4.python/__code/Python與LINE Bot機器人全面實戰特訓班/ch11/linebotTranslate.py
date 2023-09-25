from flask import Flask
app = Flask(__name__)

from flask import request, abort
from flask_sqlalchemy import SQLAlchemy
from linebot import  LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, PostbackEvent, QuickReply, QuickReplyButton, PostbackAction, AudioSendMessage
from translate import Translator
from urllib.parse import quote
from urllib.parse import parse_qsl

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

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://管理者名稱:管理者密碼@127.0.0.1:5432/translate'
db = SQLAlchemy(app)

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    userid, lang, sound = readData(event)  #讀取原有設定
    mtext = event.message.text
    if mtext == '@使用說明':
        showUse(event)

    elif mtext == '@英文':
        setLang(event, 'en', sound, userid)

    elif mtext == '@日文':
        setLang(event, 'ja', sound, userid)

    elif mtext == '@其他語文':
        setElselang(event)

    elif mtext == '@顯示設定':
        showConfig(event, lang, sound)

    elif mtext == '@切換發音':
        toggleSound(event, lang, sound, userid)

    else:  #一般文字進行翻譯
        sendTranslate(event, lang, sound, mtext)

@handler.add(PostbackEvent)  #PostbackTemplateAction觸發此事件
def handle_postback(event):
    userid, lang, sound = readData(event)
    backdata = dict(parse_qsl(event.postback.data))  #取得data資料
    sendData(event, backdata, sound, userid)

def readData(event):  #讀取使用者id,語言及發音設定
    userid = event.source.user_id
    sql_cmd = "select * from setting where uid='" + userid + "'"
    query_data = db.engine.execute(sql_cmd)
    datalist = list(query_data)
    if len(datalist) == 0:
        sql_cmd = "insert into setting (uid, lang, sound) values('" + userid + "', 'en', 'no');"
        db.engine.execute(sql_cmd)
        lang = 'en'
        sound = 'no'
    else:
        lang = datalist[0][2]
        sound = datalist[0][3]
    return userid, lang, sound

def showUse(event):
    try:
        text1 = '''
1. 本應用可將中文翻譯為多國語言，並且可使用該語言朗讀。
2. 預設的翻譯語言為「英文」，發音預設為「不發音」。
3. 按「譯為英文」、「譯為日文」、「其他語文」鈕可設定翻譯後的語言。
4. 按「顯示設定」會顯示目前翻譯後語言及是否要朗讀翻譯後文字。
5. 按「切換發音」可設定是否朗讀翻譯後文字。
6. 輸入中文文句即可進行翻譯及朗讀。
                '''
        message = TextSendMessage(
            text = text1
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def setLang(event, lang, sound, userid):  #設定翻譯語言
    try:
        sql_cmd = "update setting set lang='" + lang + "', sound='" + sound + "' where uid='" + userid +"'"
        db.engine.execute(sql_cmd)
        message = TextSendMessage(
            text = '語言設定為：' + langtoword(lang)
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def setElselang(event):  #設定其他語言
    try:
        message = TextSendMessage(
            text = '請選擇語言：',
            quick_reply = QuickReply(  #使用快速選單
                items = [
                    QuickReplyButton(
                        action = PostbackAction(label='韓文', data='item=ko')
                    ),
                    QuickReplyButton(
                        action = PostbackAction(label='泰文', data='item=th')
                    ),
                    QuickReplyButton(
                        action = PostbackAction(label='越南文', data='item=vi')
                    ),
                    QuickReplyButton(
                        action = PostbackAction(label='法文', data='item=fr')
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def showConfig(event, lang, sound):  #顯示設定
    try:
        if sound == 'yes': sound1 = '發音'
        else:  sound1 = '不發音'
        text1 = '語言設定為：' + langtoword(lang)
        text1 += '\n發音設定為：' + sound1
        message = TextSendMessage(
            text = text1
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def toggleSound(event, lang, sound, userid):  #切換發音狀態
    try:
        if sound == 'yes':  #原來是發音就設為不發音
            sound='no'
            sound1 = '不發音'
        else:  #原來是不發音就設為發音
            sound='yes'
            sound1 = '發音'
        sql_cmd = "update setting set lang='" + lang + "', sound='" + sound + "' where uid='" + userid +"'"
        db.engine.execute(sql_cmd)
        message = TextSendMessage(
            text = '發音設定為：' + sound1
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendTranslate(event, lang, sound, mtext):  #翻譯及朗讀
    try:
        translator = Translator(from_lang="zh-Hant", to_lang=lang)  #來源是中文,翻譯後語言為lang
        translation = translator.translate(mtext)  #進行翻譯
        if sound == 'yes':  #發音
            text = quote(translation)
            stream_url = 'https://google-translate-proxy.herokuapp.com/api/tts?query=' + text + '&language=' + lang  #使用google語音API
            message = [  #若要發音需傳送文字及語音,必須使用陣列
                TextSendMessage(  #傳送翻譯後文字
                    text = translation
                ),
                AudioSendMessage(  #傳送語音
                    original_content_url = stream_url,
                    duration=20000  
                ),
            ]
        else:  #不發音
            message = TextSendMessage(
                text = translation
            )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendData(event, backdata, sound, userid):  #設定其他語言
    lang = backdata.get('item')  #取得快速選單的選取值
    setLang(event, lang, sound, userid)  #設定翻譯語言

def langtoword(lang):  #將語言代碼轉為中文字
    if lang == 'en':  word = '英文'
    elif lang == 'ja':  word = '日文'
    elif lang == 'ko':  word = '韓文'
    elif lang == 'th':  word = '泰文'
    elif lang == 'vi':  word = '越南文'
    elif lang == 'fr':  word = '法文'
    return word

if __name__ == '__main__':
    app.run()
