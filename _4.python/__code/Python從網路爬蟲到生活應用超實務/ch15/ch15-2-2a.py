import plotly
import plotly.graph_objs as go

days = list(range(24))
celsius1 = [25.6, 23.2, 18.5, 28.3, 26.5, 30.5, 32.6, 33.1]*3
celsius2 = [25.6, 23.2, 18.5, 28.3, 26.5, 30.5, 32.6, 33.1]*3
celsius3 = [25.6, 23.2, 18.5, 28.3, 26.5, 30.5, 32.6, 33.1]*3
for i in range(len(days)) :
    celsius1[i] -= 15
    celsius3[i] += 15
trace0 = go.Scatter(
    x = days,
    y = celsius1,
    mode = "markers",
    name = "標記"
)
trace1 = go.Scatter(
    x = days,
    y = celsius2,
    mode = "lines+markers",
    name = "折線+標記"
)
trace2 = go.Scatter(
    x = days,
    y = celsius3,
    mode = "lines",
    name = "折線"
)
data = [trace0, trace1, trace2]
plotly.offline.plot(data, filename="ch15-2-2a.html")