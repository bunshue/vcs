import plotly
import plotly.graph_objs as go
import pandas as pd
import sqlite3

tsmc = "2330"
conn = sqlite3.connect(tsmc+".db")
df = pd.read_sql("SELECT * FROM '2330'", con=conn)
data = [go.Scatter(
        x=df.date,
        y=df["capacity"])]
plotly.offline.plot({
    "data": data,
    "layout": go.Layout(title="台積電2020年的成交股數的時序圖")
}, filename="ch15-4a.html")