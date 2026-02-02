# ch4_31.py
import pandas as pd

url = 'http://www.stockq.org/market/currency.php'
currencys = pd.read_html(url)

print(type(currencys))              # 列出資料型態
print(currencys)                    # 列出匯率的串列內容





    














