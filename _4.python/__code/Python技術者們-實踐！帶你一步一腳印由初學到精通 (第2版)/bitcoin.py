import json
import requests
import pandas as pd


def get_price(url):
    print("get_price")
    # data = requests.get(url)  # GET請求
    # print('data')
    # print(data)
    filename = "bitcoin2025.json"
    fp = open(filename, "r")
    data = json.load(fp)
    # data['stats']
    data_prices = data["stats"]  # 解析json格式，並取出'status'對應到的值
    print("222")
    df = pd.DataFrame(data_prices)  # 將list轉為dataframe
    print("333")
    df.columns = ["datetime", "twd"]  # 設定欄索引名稱
    df["datetime"] = pd.to_datetime(df["datetime"], unit="ms")  # 將毫秒轉為時間日期格式
    print("444")
    df.index = df["datetime"]  # 設定列索引
    return df


def strategy(df, total, ma_num, stop_earn):
    df["ma"] = df["twd"].rolling(window=ma_num).mean()
    df = df[ma_num - 1 :]
    entry_price = 0
    max_price = 0
    min_price = 0
    state = "wait_long"
    for i in range(len(df)):
        if state == "wait_long":
            if df["twd"][i] > df["ma"][i]:
                # print(df['datetime'][i], "  entry_long  ", df['twd'][i])
                max_price = df["twd"][i]
                entry_price = df["twd"][i]
                state = "entry_long"
        elif state == "wait_short":
            if df["twd"][i] < df["ma"][i]:
                # print(df['datetime'][i], "  entry_short  ", df['twd'][i])
                min_price = df["twd"][i]
                entry_price = df["twd"][i]
                state = "entry_short"
        elif state == "entry_long":
            if df["twd"][i] > max_price:
                max_price = df["twd"][i]
                # print("up  ",max_price)
            if df["twd"][i] < max_price:
                # print(df['datetime'][i], "  out  ", df['twd'][i])
                total += df["twd"][i] - entry_price
                state = "wait_short"
            elif df["twd"][i] - entry_price > stop_earn and stop_earn != 0:
                # print(df['datetime'][i], "  out  ", df['twd'][i])
                total += df["twd"][i] - entry_price
                state = "wait_short"
        elif state == "entry_short":
            if df["twd"][i] < min_price:
                min_price = df["twd"][i]
                # print("down  ",min_price)
            if df["twd"][i] > min_price:
                # print(df['datetime'][i], "  out  ", df['twd'][i])
                total += entry_price - df["twd"][i]
                state = "wait_long"
            elif entry_price - df["twd"][i] > stop_earn and stop_earn != 0:
                # print(df['datetime'][i], "  out  ", df['twd'][i])
                total += entry_price - df["twd"][i]
                state = "wait_long"
    return total


print("------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt

url = "https://www.coingecko.com/price_charts/1/twd/90_days.json"
bitcoin = get_price(url)
print("bitcoin")
print(bitcoin)

total = 0
for i in range(0, 2000, 100):
    for j in range(0, 2000, 100):
        tmp_total = strategy(bitcoin, 1000000, i, j)
        if tmp_total > total:
            total = tmp_total  # 最佳淨值
            best_ma = i  # 最佳MA大小
            best_stop_earn = j  # 最佳停利點

for i in range(best_ma - 100, best_ma + 100, 10):
    for j in range(best_stop_earn - 100, best_stop_earn + 100, 10):
        tmp_total = strategy(bitcoin, 1000000, i, j)
        if tmp_total > total:
            total = tmp_total  # 最佳淨值
            best_ma = i  # 最佳MA大小
            best_stop_earn = j  # 最佳停利點

print("total=", total, " Best MA=", best_ma, " Best stop earn", best_stop_earn)
bitcoin["ma"] = bitcoin["twd"].rolling(window=best_ma).mean()
bitcoin[["twd", "ma"]].plot(
    kind="line", figsize=[15, 5], xlim=("2021-01-15", "2021-02-28")
)

plt.show()
