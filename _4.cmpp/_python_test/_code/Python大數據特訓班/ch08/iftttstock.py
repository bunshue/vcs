import twstock
import time
import requests

counterLine = 0  #儲存發送次數
counterError = 0  #儲存錯誤次數

print('程式開始執行！')
while True:
    realdata = twstock.realtime.get('2317')  #即時資料
    if realdata['success']:
        realprice = realdata['realtime']['latest_trade_price']  #目前股價
        if float(realprice) >= 84:
            print('鴻海目前股價：' + realprice)
            counterLine = counterLine + 1
            url_ifttt ='https://maker.ifttt.com/trigger/stockLINE/with/key/授權碼?value1=' + realprice  #發送LINE訊息網址
            res1 = requests.get(url_ifttt)  #發送請求
            print('第' + str(counterLine) + '次發送LINE回傳訊息：' + res1.text)
        if counterLine >= 3:  #最多發送3次就結束程式
            print('程式結束！')
            break
        time.sleep(300)  #每5分鐘讀一次     
    else:
        print('twstock 讀取錯誤，錯誤原因：' + realdata['rtmessage'])
        counterError = counterError + 1
        if counterError >= 3:  #最多錯誤3次
            print('程式結束！')
            break
        time.sleep(300)  #每5分鐘讀一次     
    