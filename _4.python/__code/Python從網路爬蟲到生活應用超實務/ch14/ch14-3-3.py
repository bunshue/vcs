import yfinance as yf

df = yf.download("2330.TW")
print(df.shape)
print(df.head())