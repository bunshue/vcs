import twstock
import time
import requests

print('程式開始執行！')
while True:
    realdata = twstock.realtime.get('2317')  #即時資料
    if realdata['success']:
        realprice = realdata['realtime']['latest_trade_price']  #目前股價
        print('鴻海目前股價：' + realprice)
        time.sleep(60)  #每1分鐘讀一次     
    else:
        time.sleep(60)  #每1分鐘讀一次     
    
