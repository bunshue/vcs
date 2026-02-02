# ch4_32.py
import pandas as pd

url = 'http://www.stockq.org/market/currency.php'
currencys = pd.read_html(url)         # 讀取全球匯率行情表

item = 0
for currency in currencys:
    print("元素 : ", item)            # 列出元素編號
    print(currency)                   # 列出元素內容
    print()
    item += 1

    














