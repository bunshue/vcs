# plotly 集合 1

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

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print('------------------------------------------------------------')	#60個

import plotly.offline
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots
import squarify

#畫派圖4 利用plotly繪製圓形圖
sales_dep = pd.DataFrame({
    "label": ["第1業務部", "第2業務部", "第3業務部", 
              "網路事業部1", "網路事業部2"],
    "value": [500, 320, 130, 75, 20]})
fig = go.Figure(data=[go.Pie(labels=sales_dep["label"],
                             values=sales_dep["value"])])

fig.show()  # 繪製圖表

print('------------------------------------------------------------')	#60個

#甜甜圈圖

# 資料 
sales_dep = pd.DataFrame({
    "label": ["第1業務部", "第2業務部", "第3業務部",
              "網路事業部1", "網路事業部2"],
    "value": [500, 320, 130, 75, 20]}) 

# Pie圖表部分 
fig = go.Figure(data=[go.Pie(labels=sales_dep["label"],
                             values=sales_dep["value"],
                             hole=0.5)]) 
                              
# 圖表標題與甜甜圈部分的文字 
fig.update_layout(title_text="各部門業績",
                  annotations=[{
                                "text": "業績明細",
                                "x": 0.5,
                                "y": 0.5,
                                "font_size": 20,
                                "showarrow": False}])

fig.show()  # 繪製圖表

print('------------------------------------------------------------')	#60個

filename = 'data/weather_sample.csv'
weather = pd.read_csv(filename, header=0, parse_dates=["年月"])

#利用plotly繪製折線圖的範例
fig = px.line(weather, x="年月", y="東京-平均氣溫(℃)")

fig.show()  # 繪製圖表

#利用plotly繪製多張折線圖的範例

tmp_tokyo = go.Scatter(x=weather["年月"], y=weather["東京-平均氣溫(℃)"], 
                       mode="lines", name="東京") 
tmp_osaka = go.Scatter(x=weather["年月"], y=weather["大阪-平均氣溫(℃)"],
                       mode="lines", name="大阪")
tmp_naha = go.Scatter(x=weather["年月"], y=weather["那霸-平均氣溫(℃)"],
                      mode="lines", name="那霸")
tmp_hakodate = go.Scatter(x=weather["年月"], y=weather["函館-平均氣溫(℃)"],
                          mode="lines", name="函館") 
# 指定版面編排方式 
layout = go.Layout(xaxis=dict(title="各都市平均氣溫", type="date",
                              dtick="M1"), # 以dtick:'M1'顯示每個月的標籤
                   yaxis=dict(title="氣溫"))
fig = go.Figure(data=[tmp_tokyo, tmp_osaka, tmp_naha, tmp_hakodate], 
                layout=layout)

fig.show()  # 繪製圖表


print('------------------------------------------------------------')	#60個

#瀑布圖
fig = go.Figure(go.Waterfall(    
    # 指定為絕對值或差值    
    measure=["absolute", "relative", "relative", "relative", "relative",
             "total"],
    # 定義項目    
    x=["上個月餘額", "打工收入", "薪資", "浮動費用", "固定費用", "本月餘額"],    
    #定義標籤的項目
    textposition = "outside",
    text=["30", "+10", "+50", "-32", "-10", "48"],
    # 定義數值
    y=[30, 10, 50, -32, -10, 0],
    connector={"line": {"color": "rgb(0, 0, 0)"}}))

fig.update_layout(title="我的帳戶餘額增減趨勢",
                  showlegend=True )

fig.show()  # 繪製圖表

print('------------------------------------------------------------')	#60個

import seaborn as sns #海生, 自動把圖畫得比較好看

#矩形樹狀圖
# 調整大小
sns.set(rc={"figure.figsize": (5, 5),
            "figure.dpi": 400})

# 取得plotly的2007年人口資訊
pop_df = px.data.gapminder().query("year == 2007")

# 依降冪的順序排序人口
pop_df = pop_df.sort_values("pop", ascending=False)

# 只取得前15筆資料
pop_df = pop_df.head(15)

# 人口
pop = list(pop_df["pop"])

# 國碼
code = list(pop_df["iso_alpha"])

# 繪製矩形樹狀圖
squarify.plot(pop, label=code, 
              color=sns.color_palette("husl", len(pop)))

# 取消座標軸標
plt.axis("off")
plt.show()

#旭日圖
# 定義資料
org = [
        {"name": "全公司", "parent": "", "num": 50},
        {"name": "人事・總務部", "parent": "全公司", "num": 10},
        {"name": "業務部", "parent": "全公司", "num": 20},
        {"name": "第1業務室", "parent": "業務部", "num": 15},
        {"name": "第2業務室", "parent": "業務部", "num": 5},
        {"name": "開發部", "parent": "全公司", "num": 20},
        {"name": "第1開發室", "parent": "開發部", "num": 10},
        {"name": "第2開發室", "parent": "開發部", "num": 7},
        {"name": "諮詢窗口", "parent": "開發部", "num": 3},
    ]

# 定義圖表
trace = go.Sunburst(labels=[record["name"] for record in org],
                    parents=[record["parent"] for record in org],
                    values=[record["num"] for record in org],
                    branchvalues="total",
                    outsidetextfont={"size": 30, "color": "#82A9DA"},
)

# 定義圖表版面
layout = go.Layout(margin=go.layout.Margin(t=0, l=0, r=0, b=0))

# 繪製圖表
#plotly.offline.iplot(go.Figure([trace], layout)) 只供 ipython notebook 使用


#雷達圖
# 定義資料
data = [
    {"label": "品質", "value": 5},
    {"label": "價格", "value": 4},
    {"label": "宅配", "value": 2.7},
    {"label": "客製化", "value": 3.4},
    {"label": "網站實用度", "value": 4.3},
    {"label": "照片與實物的一致程度", "value": 3.5},
]

df = pd.DataFrame({
    "label": [record["label"] for record in data],
    "value": [record["value"] for record in data],
})

print(df)

# 定義圖表
fig = px.line_polar(df, r="value", theta="label", line_close=True)

# 定義圖表版面
fig.update_traces(fill="toself")

fig.show()  # 繪製圖表

#繪製重疊的雷達圖

# 定義資料 
data = [
    {
        "姓名": "顧客1",
        "品質": 5,
        "價格": 4,
        "宅配": 2.7,
        "客製化": 3.4,
        "網站實用度": 4.3,
        "照片與實物的一致程度": 3.5
    },
    {
        "姓名": "顧客2",
        "品質": 4,
        "價格": 3,
        "宅配": 4.5,
        "客製化": 4.5,
        "網站實用度": 1,
        "照片與實物的一致程度": 4.5
    }
]

# 建立資料框架 
df = pd.DataFrame(data).set_index("姓名") 
# 調整資料框架格式
df = df.stack().rename_axis(["姓名", "label"]).reset_index().rename(columns={0: "value"}) 

fig = px.line_polar(df, r="value", theta="label", color="姓名", line_close=True) 

fig.show()  # 繪製圖表



print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個




