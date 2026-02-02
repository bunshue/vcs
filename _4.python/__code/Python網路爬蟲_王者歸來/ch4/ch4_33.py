# ch4_33.py
import pandas as pd

url = 'http://www.stockq.org/market/currency.php'
currencys = pd.read_html(url)                               # 讀取全球匯率行情表

currency = currencys[7]                                     # 讀取第7元素
currency = currency.drop(currency.index[[0,1]])             # 拋棄前2 row
currency.columns = ['貨幣', '匯率', '漲跌', '比例', '台北'] # 建立column標題
currency.index = range(len(currency.index))                 # 建立row標題
print(currency)


    














