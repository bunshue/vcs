# ch12_10.py
import pandas as pd
import twstock

stock2330 = twstock.realtime.get('2330')
buyPrice = stock2330['realtime']['best_bid_price']
buyNum = stock2330['realtime']['best_bid_volume']

selPrice = stock2330['realtime']['best_ask_price']
selNum = stock2330['realtime']['best_ask_volume']

dict2330 = {'BVolumn':buyNum,
            'Buy':buyPrice,
            'Sell':selPrice,
            'SVolumn':selNum}

df2330 = pd.DataFrame(dict2330, index=range(1,6))
print("台積電最佳五檔價量表")
print(df2330)






