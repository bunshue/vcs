# ch32_1.py
import yfinance as yf

apple = yf.Ticker("AAPL")                           # 建立Apple物件
print("Apple公司財務報表")
financials = apple.financials                       # 獲取財務報表
print(financials)
quarterly_financials = apple.quarterly_financials   # 獲取季度財務報表
print(quarterly_financials)

tsmc = yf.Ticker("2330.TW")                         # 建立Apple物件
print("台積電財務報表")
financials = tsmc.financials                        # 獲取財務報表
print(financials)
quarterly_financials = tsmc.quarterly_financials    # 獲取季度財務報表
print(quarterly_financials)



