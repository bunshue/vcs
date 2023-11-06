import pandas as pd
import twstock

stock = twstock.Stock("2330") 
data = stock.fetch(2020, 7)

df = pd.DataFrame(data)
df["date"] = pd.to_datetime(df["date"]) 
df = df.set_index("date")
df[["close","open","high","low"]].plot()


