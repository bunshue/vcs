import pandas as pd
import twstock
import sqlite3

tsmc = "2330"
stock = twstock.Stock(tsmc)
df = pd.DataFrame(stock.fetch_from(2020,1))
df["date"] = pd.to_datetime(df["date"]) 
df.set_index("date", inplace=True)
print(df.head())
conn = sqlite3.connect(tsmc+".db")
df.to_sql(tsmc, conn, if_exists="replace")
print("已經將股票資料存入SQLite資料庫...")