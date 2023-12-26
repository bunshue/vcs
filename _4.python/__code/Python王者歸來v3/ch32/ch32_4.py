# ch32_4.py
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
# 下載台積電最近三個月的股價數據
tsmc = yf.Ticker("2330.TW")                 
data = tsmc.history(period='1y')

# 計算5日和20日的簡單移動平均
data['SMA5'] = data['Close'].rolling(window=5).mean()
data['SMA20'] = data['Close'].rolling(window=20).mean()

# 繪製收盤價和移動平均線
plt.figure(figsize=(10, 6))
plt.plot(data['Close'], label='Close Price', alpha=0.5)
plt.plot(data['SMA5'], label='5-Day SMA', alpha=0.8)
plt.plot(data['SMA20'], label='20-Day SMA', alpha=0.8)
plt.title('台積電股價 5 日和 20 日移動平均線')
plt.xlabel('日期')
plt.ylabel('價格')
plt.legend()
plt.grid(True)
plt.show()

# 移動平均生成交易信號
# 買入信號: 5日均線從下方突破20日均線
# 賣出信號: 5日均線從上方跌破20日均線
data['Signal'] = 0.0
data.iloc[5:, data.columns.get_loc('Signal')] =\
    np.where(data['SMA5'].iloc[5:] > data['SMA20'].iloc[5:], 1.0, 0.0)
data['Signal_change'] = data['Signal'].diff()

# 找出買入和賣出的日期
buy_dates = data[data['Signal_change'] == 1].index
sell_dates = data[data['Signal_change'] == -1].index

print(f"買入日期: {buy_dates.tolist()}")
print(f"賣出日期: {sell_dates.tolist()}")



