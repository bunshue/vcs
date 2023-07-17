import twstock
# 以鴻海的股票代號建立 Stock 物件
stock = twstock.Stock('2317')  
# 取得 2019 年 12 月的資料
stocklist = stock.fetch(2019,12)   
for s in stocklist:
    print(s.date.strftime('%Y-%m-%d'), end='\t')
    print(s.open, end='\t')
    print(s.high, end='\t')
    print(s.low, end='\t')
    print(s.close)