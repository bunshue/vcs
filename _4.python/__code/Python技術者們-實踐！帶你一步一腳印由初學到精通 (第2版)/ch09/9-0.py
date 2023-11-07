import requests
import pandas as pd
import matplotlib.pyplot as plt


def get_price(url):
    data = requests.get(url)  # GET請求
    data_prices = data.json()['stats']  # 解析json格式，並取出'status'對應到的值
    df = pd.DataFrame(data_prices)  # 將list轉為dataframe
    df.columns = ['datetime', 'twd']  # 設定欄索引名稱
    df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')  # 將毫秒轉為時間日期格式
    df.index = df['datetime']  # 設定列索引
    return df


url = 'https://www.coingecko.com/price_charts/1/twd/90_days.json'
bitcoin = get_price(url)
# 利用'twd'欄位的值計算窗口為100的均線, 並加入bitcoin的dataframe之中
bitcoin['ma'] = bitcoin['twd'].rolling(window=100).mean()

# 以'twd'和'ma'欄位的值繪圖
bitcoin[['twd', 'ma']].plot(
    kind='line', figsize=[15, 5], xlim=('2021-01-20', '2021-01-27'))
plt.show()
