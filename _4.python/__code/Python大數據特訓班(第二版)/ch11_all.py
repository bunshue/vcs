# twstock1.py
import twstock

stock = twstock.Stock('2317')  #鴻海
print('近31個收盤價：')
print(stock.price)   #近31個收盤價
print('近6個收盤價：')
print(stock.price[-6:])   #近6日之收盤價

real = twstock.realtime.get('2317')
if real['success']:
    print('即時股票資料：')
    print(real)  #即時資料
    print('目前股價：')
    print(real['realtime']['latest_trade_price'])  #即時價格
else:
    print('錯誤：' + real['rtmessage'])

# linenotify.py
import requests

msg = '這是 LINE Notify 發送的訊息。'
token = '你的 LINE ifNoty 權杖'  #權杖
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
    
    

# linestock.py
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

token = '你的 LINE ifNoty 權杖'  #權杖
counterLine = 0  #儲存發送次數
counterError = 0  #儲存錯誤次數

print('程式開始執行！')
while True:
    realdata = twstock.realtime.get('2317')  #即時資料
    if realdata['success']:
        realprice = realdata['realtime']['latest_trade_price']  #目前股價
        if float(realprice) >= 80:
            counterLine = sendline(1, realprice, counterLine, token)
        elif float(realprice) <= 60:
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
