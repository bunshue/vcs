# plotly 集合 2

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print('------------------------------------------------------------')	#60個

"""
import plotly.offline
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots

"""
print('------------------------------------------------------------')	#60個

import plotly
from plotly.graph_objs import Scatter, Layout

x = [1, 2, 3, 4]
y = [4, 3, 2, 1]
plotly.offline.plot({
    "data": [Scatter(x=x, y=y)],
    "layout": Layout(title="hello world")
})

print('------------------------------------------------------------')	#60個

print('繪製散佈圖')
import plotly
import plotly.graph_objs as go
 
df = pd.read_csv("data/NBA_players_salary_stats_2018.csv")
x = df["PTS"]
y = df["salary"]
trace = go.Scatter(
    x = x,
    y = y,
    mode = "markers"
)
data = [trace]
plotly.offline.plot(data, filename="tmp_ch15-2-2.html")

print('------------------------------------------------------------')	#60個

print('同時繪製多條折線和散佈圖')
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
plotly.offline.plot(data, filename="tmp_ch15-2-2a.html")

print('------------------------------------------------------------')	#60個

print('繪製箱型圖')
import plotly

df = pd.read_csv("data/NBA_salary_rankings_2018.csv")
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
plotly.offline.plot({"data":data,"layout":layout}, filename="tmp_ch15-2-2b.html")

print('------------------------------------------------------------')	#60個

print('繪製金融圖表(時間序列圖)')
import plotly
import plotly.graph_objs as go

df = pd.read_csv("data/AAPL.csv")
data = [go.Scatter(
        x=df.Date,
        y=df["Close"])]
plotly.offline.plot(data, filename="tmp_ch15-2-2c.html")

print('------------------------------------------------------------')	#60個

print('繪製金融圖表(OHLC圖)')
import plotly
import plotly.graph_objs as go

df = pd.read_csv("data/AAPL.csv").head(10)
trace = go.Ohlc(x=df.Date,
                open= df["Open"],
                high=df["High"],
                low=df["Low"],
                close=df["Close"])
data = [trace]
plotly.offline.plot(data, filename="tmp_ch15-2-2d.html")

print('------------------------------------------------------------')	#60個

print('讀取資料存入資料庫')

import twstock
import sqlite3

tsmc = "2330"
stock = twstock.Stock(tsmc)
df = pd.DataFrame(stock.fetch_from(2020,1))
df["date"] = pd.to_datetime(df["date"]) 
df.set_index("date", inplace=True)
print(df.head())
conn = sqlite3.connect("tmp_"+tsmc+".db")
df.to_sql(tsmc, conn, if_exists="replace")
print("已經將股票資料存入SQLite資料庫...")

print('------------------------------------------------------------')	#60個

print('繪製金融圖表(OHLC圖) 台積電')
import plotly
import plotly.graph_objs as go
import sqlite3

tsmc = "2330"
conn = sqlite3.connect("tmp_"+tsmc+".db")
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
}, filename="tmp_ch15-4.html")

print('------------------------------------------------------------')	#60個

print('繪製金融圖表(時間序列圖) 台積電')

import plotly
import plotly.graph_objs as go
import sqlite3

tsmc = "2330"
conn = sqlite3.connect("tmp_"+tsmc+".db")
df = pd.read_sql("SELECT * FROM '2330'", con=conn)
data = [go.Scatter(
        x=df.date,
        y=df["capacity"])]
plotly.offline.plot({
    "data": data,
    "layout": go.Layout(title="台積電2020年的成交股數的時序圖")
}, filename="tmp_ch15-4a.html")

print('------------------------------------------------------------')	#60個



print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個

