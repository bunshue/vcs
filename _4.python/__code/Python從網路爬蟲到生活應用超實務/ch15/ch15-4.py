import plotly
import plotly.graph_objs as go
import pandas as pd
import sqlite3

tsmc = "2330"
conn = sqlite3.connect(tsmc+".db")
df = pd.read_sql("SELECT * FROM '2330'", con=conn)
trace = go.Ohlc(x=df.date,
                open= df["open"],
                high=df["high"],
                low=df["low"],
                close=df["close"])
data = [trace]
plotly.offline.plot({
    "data": data,
    "layout": go.Layout(title="台積電2020年的OHLC圖")
}, filename="ch15-4.html")

