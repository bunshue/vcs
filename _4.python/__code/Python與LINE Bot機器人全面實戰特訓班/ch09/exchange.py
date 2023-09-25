import twder

currencies = {'美金':'USD','美元':'USD','港幣':'HKD','英鎊':'GBP','澳幣':'AUD','加拿大幣':'CAD',\
              '加幣':'CAD','新加坡幣':'SGD','新幣':'SGD','瑞士法郎':'CHF','瑞郎':'CHF','日圓':'JPY',\
              '日幣':'JPY','南非幣':'ZAR','瑞典幣':'SEK','紐元':'NZD','紐幣':'NZD','泰幣':'THB',\
              '泰銖':'THB','菲國比索':'PHP','菲律賓幣':'PHP','印尼幣':'IDR','歐元':'EUR','韓元':'KRW',\
              '韓幣':'KRW','越南盾':'VND','越南幣':'VND','馬來幣':'MYR','人民幣':'CNY' }
keys = currencies.keys()
tlist = ['現金買入', '現金賣出', '即期買入', '即期賣出']
currency = '美元'
show = currency + '匯率：\n'
if currency in keys:
    for i in range(4):
        exchange = float(twder.now(currencies[currency])[i+1])
        show = show + tlist[i] + '：' + str(exchange) + '\n'
    print(show)
else:
     print('無此貨幣資料！')