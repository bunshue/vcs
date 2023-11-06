import pandas_datareader as pdr

df = pdr.DataReader("2330.TW", "yahoo")
print(df.shape)
print(df.head())