import twstock
# 以鴻海的股票代號建立 Stock 物件
stock = twstock.Stock('2317')  
print("日期：",stock.date[-1])
print("開盤價：",stock.open[-1])
print("最高價：",stock.high[-1])
print("最低價：",stock.low[-1])
print("收盤價：",stock.price[-1])