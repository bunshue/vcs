import yfinance as yf
import matplotlib.pyplot as plt

'''
#df = yf.Ticker('TSLA')                   # 美股 Tesla
df = yf.Ticker("0005.HK").history(period="10y")

df = df.filter(["Close"])
df = df.rename(columns = {"Close" : "GT"})

#plt.style.use("seaborn-darkgrid")
plt.xlabel("Date")
plt.ylabel('Price')
plt.plot(df["GT"], linewidth = 1)
plt.show()
'''

'''
import yfinance as yf   
print(type(yf.Ticker))
#<class 'type'>
tsla=yf.Ticker('TSLA')                   # 美股 Tesla
print(type(tsla))
#<class 'yfinance.ticker.Ticker'>       
tw2330=yf.Ticker("2330.TW")      # 台積電  
print(type(tw2330))
#<class 'yfinance.ticker.Ticker'>
'''



import yfinance as yf

tw2330=yf.Ticker('2330.TW')
tsla=yf.Ticker('TSLA')
     
#print(tw2330.info)
print(tsla.get_info())
     




