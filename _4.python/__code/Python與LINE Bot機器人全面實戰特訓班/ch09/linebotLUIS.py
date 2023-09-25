from flask import Flask
app = Flask(__name__)

from flask import request, abort
from linebot import  LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import requests
import twder  #匯率套件

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

user_key = "你的氣象API授權碼"
doc_name = "F-C0032-001"

cities = ["臺北","新北","桃園","臺中","臺南","高雄","基隆","新竹","嘉義"]  #市
counties = ["苗栗","彰化","南投","雲林","嘉義","屏東","宜蘭","花蓮","臺東","澎湖","金門","連江"]  #縣
currencies = {'美金':'USD','美元':'USD','港幣':'HKD','英鎊':'GBP','澳幣':'AUD','加拿大幣':'CAD',\
              '加幣':'CAD','新加坡幣':'SGD','新幣':'SGD','瑞士法郎':'CHF','瑞郎':'CHF','日圓':'JPY',\
              '日幣':'JPY','南非幣':'ZAR','瑞典幣':'SEK','紐元':'NZD','紐幣':'NZD','泰幣':'THB',\
              '泰銖':'THB','菲國比索':'PHP','菲律賓幣':'PHP','印尼幣':'IDR','歐元':'EUR','韓元':'KRW',\
              '韓幣':'KRW','越南盾':'VND','越南幣':'VND','馬來幣':'MYR','人民幣':'CNY' }  #幣別字典
keys = currencies.keys()

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    mtext = event.message.text
    if mtext=='@使用說明':  #顯示使用說明
        sendUse(event)

    else:  #一般性輸入
        sendLUIS(event, mtext)

def sendUse(event):  #使用說明
    try:
        text1 ='''查詢天氣：輸入「XXXX天氣如何?」，例如「高雄天氣如何?」
輸入「XXXX有下雨嗎?」，例如「台中有下雨嗎?」

查詢匯率：輸入「XXXX匯率為多少?」，例如「美金匯率為多少?」
輸入「XXXX一元換新台幣多少元?」，例如「英鎊一元換新台幣多少元?」'''
        message = TextSendMessage(
            text = text1
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendLUIS(event, mtext):  #LUIS
    try:
        r = requests.get('https://westus.api.cognitive.microsoft.com/luis/prediction/v3.0/apps/be857f50-efbf-4487-a8bb-b1ab1e4819b0/slots/production/predict?subscription-key=b70c437cffee487b9ab2aa9ed6faaac6&verbose=true&show-all-intents=true&log=true&query=' + mtext)
        result = r.json()
        city = ''
        money = ''
        if result["prediction"]['topIntent'] == '縣市天氣':
            city = result["prediction"]['entities']['地點'][0]
        elif result["prediction"]['topIntent'] == '匯率查詢':
            money = result["prediction"]['entities']['幣別'][0]
        if city != '':  #天氣類地點存在
            flagcity = False  #檢查是否為縣市名稱
            city = city.replace('台', '臺')  #氣象局資料使用「臺」
            if city in cities:  #加上「市」
                city += '市'
                flagcity = True
            elif city in counties:  #加上「縣」
                city += '縣'
                flagcity = True
            if flagcity:  #是縣市名稱
                weather = city + '天氣資料：\n'             
                api_link = "https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/%s?Authorization=%s&downloadType=WEB&format=JSON" % (doc_name,user_key)
                datas = requests.get(api_link).json()
                column = ['天氣狀況','最高溫','最低溫','舒適度','降雨機率(%)']
                for data in datas['cwbopendata']['dataset']['location']:
                    if data['locationName'] == city:
                        for i in range(len(data['weatherElement'])):
                            weather += column[i] + ':'
                            weather += data['weatherElement'][i]['time'][0]['parameter']['parameterName'] + '\n'
                        weather = weather[:-1]  #移除最後一個換行
                        break                       
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text=weather))
            else:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text='無此地點天氣資料！'))
        elif not money == '':  #匯率類幣別存在
            if money in keys:
                rate = float(twder.now(currencies[money])[3])  #由匯率套件取得匯率
                message = money + '的匯率為 ' + str(rate)
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))
            else:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text='無此幣別匯率資料！'))
        else:  #其他未知輸入
            text = '無法了解你的意思，請重新輸入！'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=text))            
    except:
       line_bot_api.reply_message(event.reply_token, TextSendMessage(text='執行時產生錯誤！'))

if __name__ == '__main__':
    app.run()