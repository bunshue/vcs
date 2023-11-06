import plotly
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv("AAPL.csv")
data = [go.Scatter(
        x=df.Date,
        y=df["Close"])]
plotly.offline.plot(data, filename="ch15-2-2c.html")