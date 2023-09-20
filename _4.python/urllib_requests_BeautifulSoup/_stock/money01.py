'''

金融匯率股票相關



'''

import twder

'''
print('------------------------------------------------------------')	#60個

print('twder：新台幣匯率擷取')
print(twder.currencies())
print(twder.currency_name_dict())


print(twder.now_all())


print(twder.now('USD'))

print(twder.past_day('USD'))

print(twder.past_six_month('USD'))

#print(twder.specify_month('USD', 2020, 5))


print('------------------------------------------------------------')	#60個

#應用：新台幣國際匯率查詢
import twder

currencies = {'美元':'USD','港幣':'HKD','英鎊':'GBP','澳幣':'AUD','加拿大幣':'CAD','加幣':'CAD',
        '新加坡幣':'SGD','瑞士法郎':'CHF','日幣':'JPY','南非幣':'ZAR','瑞典幣':'SEK',
        '紐幣':'NZD','泰銖':'THB','菲律賓幣':'PHP','印尼幣':'IDR','歐元':'EUR','韓元':'KRW',\
        '越南盾':'VND','越南幣':'VND','馬來幣':'MYR','人民幣':'CNY' }
keys = currencies.keys()
tlist = ['現金買入', '現金賣出', '即期買入', '即期賣出']
currency = '\u52A0\u62FF\u5927\u5E63' #@param ['美元', '港幣', '英鎊', '澳幣', '加拿大幣', '加幣', '新加坡幣', '瑞士法郎', '日幣', '南非幣', '瑞典幣' , '紐幣' ,'泰銖' ,'菲律賓幣' ,'印尼幣' ,'歐元' ,'韓元' , '越南盾' ,'越南幣' ,'馬來幣' ,'人民幣']
show = currency + '匯率：\n'
if currency in keys:
    for i in range(4):
        exchange = twder.now(currencies[currency])[i+1]
        show = show + tlist[i] + '：' + str(exchange) + '\n'
    print(show)
else:
    print('無此貨幣資料！')


print('------------------------------------------------------------')	#60個

print('google-currency：不同幣值換算')

from google_currency import convert 

print(convert('USD', 'JPY', 230))

from google_currency import convert 
import json
samount = 100 #@param {type:'integer'}
damount = convert('USD', 'JPY', samount)
retdict = json.loads(damount)
print('{} 元美金 = 日幣 {} 元'.format(samount, retdict['amount']))

print('------------------------------------------------------------')	#60個

print('twstock：台灣股票')

import twstock
stock = twstock.Stock('2317')
print(stock.price)


print("日期：",stock.date[-1])
print("開盤價：",stock.open[-1])
print("最高價：",stock.high[-1])
print("最低價：",stock.low[-1])
print("收盤價：",stock.price[-1])

stock.fetch(2020,1)
stock.fetch_31()

stock.fetch_from(2021,9)
real = twstock.realtime.get('2317')
print(real)

if real['success']:
    print('股票名稱、即時股票資料：')
    print('股票名稱：',real['info']['name'])     
    print('開盤價：',real['realtime']['open'])
    print('最高價：',real['realtime']['high'])  
    print('最低價：',real['realtime']['low'])
    print('目前股價：',real['realtime']['latest_trade_price'])   
else:
    print('錯誤：' + real['rtmessage'])
'''

'''
import requests

msg = '這是 LINE Notify 發送的訊息。'
token = '你的 LINE Notify 權杖'  #權杖
headers = {
    "Authorization": "Bearer " + token, 
    "Content-Type" : "application/x-www-form-urlencoded"
}
payload = {'message': msg}
notify = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
if notify.status_code == 200:
    print('發送 LINE Notify 成功！')
else:
    print('發送 LINE Notify 失敗！')
'''    

print('------------------------------------------------------------')	#60個

print('應用：使用LINE監控即時股價')

'''
import twstock
import time
import requests

def lineNotify(token, msg):
    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }

    payload = {'message': msg}
    notify = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return notify.status_code

def sendline(mode, realprice, counterLine, token):
    print('鴻海目前股價：' + str(realprice))
    if mode == 1:
        message = '現在鴻海股價為 ' + str(realprice) + '元，可以賣出股票了！'
    else:
        message = '現在鴻海股價為 ' + str(realprice) + '元，可以買入股票了！'
    code = lineNotify(token, message)
    if code == 200:
        counterLine = counterLine + 1
        print('第 ' + str(counterLine) + ' 次發送 LINE 訊息。')
    else:
        print('發送 LINE 訊息失敗！')
    return counterLine

token = '你的 LINE Notify 權杖'  #權杖
counterLine = 0  #儲存發送次數
counterError = 0  #儲存錯誤次數

print('程式開始執行！')
while True:
    realdata = twstock.realtime.get('2317')  #即時資料
    if realdata['success']:
        realprice = realdata['realtime']['latest_trade_price']  #目前股價
        if realprice != '-':
          if float(realprice) >= 40:
              counterLine = sendline(1, realprice, counterLine, token)
          elif float(realprice) <= 20:
              counterLine = sendline(2, realprice, counterLine, token)
          if counterLine >= 3:  #最多發送3次就結束程式
              print('程式結束！')
              break
    else:
        print('twstock 讀取錯誤，錯誤原因：' + realdata['rtmessage'])
        counterError = counterError + 1
        if counterError >= 3:  #最多錯誤3次
            print('程式結束！')
            break
    for i in range(300):  #每5分鐘讀一次
        time.sleep(1)
'''

print('------------------------------------------------------------')	#60個

print('TWCB：中央銀行資料庫')


import TWCB

print(TWCB.get_info())

df1 = TWCB.get('BP01D01.px')
print(df1)

df1.to_csv('匯率日報表.csv')

data_list = TWCB.get_by_search('美元之匯率')

TWCB.get_all()

import json
import pandas as pd
import os
with open('download_TWCB.json','r',encoding='utf-8') as f:
    test_data = json.load(f)
if not os.path.isdir('twcb'):
    os.mkdir('twcb')
for key in test_data.keys():
    data = pd.read_json(test_data[key])
    data.to_csv('twcb/' + key + '.csv')
    



print('------------------------------------------------------------')	#60個


