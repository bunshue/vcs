import plotly
from plotly.graph_objs import Scatter, Layout

x = [1, 2, 3, 4]
y = [4, 3, 2, 1]
plotly.offline.plot({
    "data": [Scatter(x=x, y=y)],
    "layout": Layout(title="hello world")
})