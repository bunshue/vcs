# ch32_3.py
import yfinance as yf
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
# 下載蘋果公司最近三個月的股價數據
apple = yf.Ticker("AAPL")
data = apple.history(period="3mo")

# 計算5天和20天移動平均線
data['MA5'] = data['Close'].rolling(window=5).mean()
data['MA20'] = data['Close'].rolling(window=20).mean()

# 繪製股價和移動平均線
plt.figure(figsize=(10,6))
plt.plot(data['Close'], label='AAPL Close', color='blue')
plt.plot(data['MA5'], label='5-Day MA', color='green')
plt.plot(data['MA20'], label='20-Day MA', color='red')

# 標題和圖例
plt.title('Apple公司股價 5 日和 20 日移動平均線')
plt.xlabel('日期')
plt.ylabel('價格')
plt.legend()

# 顯示圖表
plt.show()


