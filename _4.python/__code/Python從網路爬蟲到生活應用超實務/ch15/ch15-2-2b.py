import plotly
import pandas as pd

df = pd.read_csv("NBA_salary_rankings_2018.csv")
df = df.sort_values("pos")
col = df.drop_duplicates(["pos"])
marker_color = ['red','blue','green',"black","orange"]
idx = 0 
data = []
for pos in col["pos"].values:
    d = df[(df.pos == pos)]
    idx = (idx+1) % len(marker_color) 
    data.append({"y": d["salary"].values, 
                 "type": "box",
                 "marker": {"color": marker_color[idx]},
                 "name": pos
                })
layout = {"xaxis": {"showgrid":False,"zeroline":False,
                    "tickangle":60,"showticklabels":False},
          "yaxis": {"zeroline":False,"gridcolor":"white"},
          "paper_bgcolor": "rgb(233,233,233)",
          "plot_bgcolor": "rgb(233,233,233)",
          }
plotly.offline.plot({"data":data,"layout":layout},
                    filename="ch15-2-2b.html")