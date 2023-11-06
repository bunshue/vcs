import pandas as pd
import twstock

stock = twstock.Stock("2330") 
data = stock.fetch_from(2019, 1)

df = pd.DataFrame(data)
df["date"] = pd.to_datetime(df["date"]) 
df = df.set_index("date")

df["5_Day_Mean"] = df["close"].rolling(window=5).mean()
df["20_Day_Mean"] = df["close"].rolling(window=20).mean()
df["60_Day_Mean"] = df["close"].rolling(window=60).mean()

df[["5_Day_Mean","20_Day_Mean","60_Day_Mean"]].plot(figsize=(10, 5))
