import plotly
import plotly.graph_objs as go
import pandas as pd
 
df = pd.read_csv("NBA_players_salary_stats_2018.csv")
x = df["PTS"]
y = df["salary"]
trace = go.Scatter(
    x = x,
    y = y,
    mode = "markers"
)
data = [trace]
plotly.offline.plot(data, filename="ch15-2-2.html")