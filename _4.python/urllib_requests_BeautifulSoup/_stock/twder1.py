'''

金融匯率股票相關

twder


'''

    



print('------------------------------------------------------------')	#60個

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



print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個


import twder


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





print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個

