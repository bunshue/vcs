import plotly
from plotly.graph_objs import Scatter

#plotly.offline.init_notebook_mode(connected=True)

data = [Scatter(x=["林大明", "陳聰明", "黃美麗", "熊小娟"], y=[67,89,72,95])]
plotly.offline.plot({
    "data": data
}) 