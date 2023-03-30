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
else:
    print('錯誤：' + real['rtmessage'])
print('目前股價：')
print(real['realtime']['latest_trade_price'])  #即時價格
