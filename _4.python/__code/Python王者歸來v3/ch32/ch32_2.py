# ch32_2.py
import yfinance as yf

def fetch_apple_stock_price():
    # 獲取Apple股票資料
    apple = yf.Ticker("AAPL")
    
    # 獲取即時股價
    apple_stock_info = apple.history(period="1d")
    
    # 輸出股價
    print("Apple公司的股價(目前或最近交易日) : ")
    print("開盤價：", apple_stock_info['Open'].iloc[0])
    print("收盤價：", apple_stock_info['Close'].iloc[0])
    print("最高價：", apple_stock_info['High'].iloc[0])
    print("最低價：", apple_stock_info['Low'].iloc[0])
    print("交易量：", apple_stock_info['Volume'].iloc[0])

fetch_apple_stock_price()


