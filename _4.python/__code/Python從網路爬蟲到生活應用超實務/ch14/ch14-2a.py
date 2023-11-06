import twstock

stock = twstock.Stock("2330") 
print("股票代號:", stock.sid)
print("各日收盤價:", stock.price)
print("各日最高價:", stock.high)
print("各日最低價:", stock.low)
print("各日成交股數:", stock.capacity)
print("各日的日期:", stock.date)
