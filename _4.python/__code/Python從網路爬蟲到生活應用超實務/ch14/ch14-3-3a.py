import datetime
import yfinance as yf

start = datetime.datetime.now() - datetime.timedelta(days=60)
end = datetime.date.today()
df = yf.download("2330.TW", start, end)
print(df.shape)
print(df.head())