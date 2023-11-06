import datetime
import pandas_datareader as pdr

start = datetime.datetime.now() - datetime.timedelta(days=60)
end = datetime.date.today()
df = pdr.DataReader("2330.TW", "yahoo", start, end)
print(df.shape)
print(df.head())