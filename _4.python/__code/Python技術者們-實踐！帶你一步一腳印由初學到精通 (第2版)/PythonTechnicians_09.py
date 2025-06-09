import requests
import pandas as pd
import matplotlib.pyplot as plt


def get_price(url):
    data = requests.get(url)  # GET請求
    data_prices = data.json()["stats"]  # 解析json格式，並取出'status'對應到的值
    df = pd.DataFrame(data_prices)  # 將list轉為dataframe
    df.columns = ["datetime", "twd"]  # 設定欄索引名稱
    df["datetime"] = pd.to_datetime(df["datetime"], unit="ms")  # 將毫秒轉為時間日期格式
    df.index = df["datetime"]  # 設定列索引
    return df


url = "https://www.coingecko.com/price_charts/1/twd/90_days.json"
bitcoin = get_price(url)
# 利用'twd'欄位的值計算窗口為100的均線, 並加入bitcoin的dataframe之中
bitcoin["ma"] = bitcoin["twd"].rolling(window=100).mean()

# 以'twd'和'ma'欄位的值繪圖
bitcoin[["twd", "ma"]].plot(
    kind="line", figsize=[15, 5], xlim=("2021-01-20", "2021-01-27")
)

plt.show()

print("------------------------------------------------------------")  # 60個

import bitcoin_module as m


def strategy(df, total, ma_num, stop_earn):
    df["ma"] = df["twd"].rolling(window=ma_num).mean()
    df = df[ma_num - 1 :]  # 將前面的none值去掉
    entry_price = 0  # 進場點
    max_price = 0  # 最高點
    min_price = 0  # 最低點
    state = "wait_long"  # 設定初始狀態為'等待做多'
    for i in range(len(df)):
        # 等待做多
        if state == "wait_long":
            if df["twd"][i] > df["ma"][i]:
                max_price = df["twd"][i]
                entry_price = df["twd"][i]
                state = "entry_long"
        # 等待做空
        elif state == "wait_short":
            if df["twd"][i] < df["ma"][i]:
                min_price = df["twd"][i]
                entry_price = df["twd"][i]
                state = "entry_short"
        # 進場做多
        elif state == "entry_long":
            if df["twd"][i] > max_price:
                max_price = df["twd"][i]
            if df["twd"][i] < max_price:
                total += df["twd"][i] - entry_price
                state = "wait_short"
            elif df["twd"][i] - entry_price > stop_earn and stop_earn != 0:
                total += df["twd"][i] - entry_price
                state = "wait_short"
        # 進場做空
        elif state == "entry_short":
            if df["twd"][i] < min_price:
                min_price = df["twd"][i]
            if df["twd"][i] > min_price:
                total += entry_price - df["twd"][i]
                state = "wait_long"
            elif entry_price - df["twd"][i] > stop_earn and stop_earn != 0:
                total += entry_price - df["twd"][i]
                state = "wait_long"
    return total


url = "https://www.coingecko.com/price_charts/1/twd/90_days.json"
bitcoin = m.get_price(url)
total = strategy(bitcoin, 1000000, 200, 1000)
# 期初資金為100萬, 均線為200, 停利點為1000

print("顯示出淨值 : ")
print(total)  # 顯示出淨值


print("------------------------------------------------------------")  # 60個
