# Python 測試 twstock 3

import twstock
import pandas as p

stock_code = str(2330)
stock = twstock.realtime.get(stock_code)

#檢查是不是即時資料 是:顯示True 不是:顯示False  
print(stock['success'])

result = p.DataFrame(stock).T.iloc[1:3]
result.columns = ['股票代碼', '地區', '股票名稱', '公司全名','現在時間', '最新成交價', '成交量', '累計成交量', '最佳5檔賣出價', '最佳5檔賣出量', '最佳5檔買進價', '最佳5檔買進量', '開盤價', '最高價', '最低價']
print(result)
