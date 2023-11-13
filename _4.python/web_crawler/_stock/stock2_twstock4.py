# Python 測試 twstock 4

import twstock
import time
import requests

stock = twstock.Stock('2317')  #鴻海
print('近31個收盤價：')
print(stock.price)   #近31個收盤價
print('近6個收盤價：')
print(stock.price[-6:])   #近6日之收盤價

realdata = twstock.realtime.get('2317')  #即時資料
print(realdata)

if realdata['success']:
    print('即時股票資料：')
    print(realdata)  #即時資料
else:
    print('錯誤：' + realdata['rtmessage'])

realprice = realdata['realtime']['latest_trade_price']  #目前股價
if realprice == '-':
    print('找不到資料')
else:
    print('鴻海目前股價：' + realprice)

print('-----------------------------------')

time.sleep(30)  #等一下

print('每一分鐘抓一次資料')

while True:
    realdata = twstock.realtime.get('2317')  #即時資料
    print(realdata)
    if realdata['success']:
        realprice = realdata['realtime']['latest_trade_price']  #目前股價
        if realprice == '-':
            print('找不到資料')
        else:
            print('鴻海目前股價：' + realprice)
        time.sleep(60)  #每1分鐘讀一次
    else:
        print('twstock 讀取錯誤，錯誤原因：' + realdata['rtmessage'])
        time.sleep(60)  #每1分鐘讀一次


