import plotly
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv("AAPL.csv").head(10)
trace = go.Ohlc(x=df.Date,
                open= df["Open"],
                high=df["High"],
                low=df["Low"],
                close=df["Close"])
data = [trace]
plotly.offline.plot(data, filename="ch15-2-2d.html")