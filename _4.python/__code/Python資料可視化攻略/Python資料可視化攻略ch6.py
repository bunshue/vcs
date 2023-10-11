import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns #海生, 自動把圖畫得比較好看

import plotly.offline
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots
import squarify

#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei

#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

"""
#Chapter6：定位資訊視覺化手法

定位資訊視覺化手法
地圖資訊的視覺化函式庫

pip install folium

"""

import plotly.express as px
import folium
import json
import pandas as pd
from branca.colormap import linear
from folium.plugins import HeatMap


print('------------------------------------------------------------')	#60個

#分區標色的世界地圖

#plotly的2007年世界各國人均GDP資料

gapminder = px.data.gapminder().query("year == 2007")
print(gapminder)

print('------------------------------------------------------------')	#60個

#根據世界各國人均GDP標色的範例

base_map = folium.Map(location = [50, 0], zoom_start = 1.8)

# 新增Choropleth
folium.Choropleth(
    geo_data=json.load(open("countries.geo.json","r", encoding ='UTF-8')),
    data=gapminder,                        # 使用的資料
    fill_opacity=1,                        # 填色的透明度
    line_color = "black",                  # 邊界顏色
    nan_fill_color="#888888",              # 遺漏值的填色
    columns = ["iso_alpha", "gdpPercap"],  # 填色所需的Key與欄位名稱
    key_on = "feature.id",                 # 與資料對應的geo.json的Key
    fill_color = "PuRd",                   # 填色使用的調色盤
).add_to(base_map)

#將地圖資料繪製成地球儀的範例

gapminder = px.data.gapminder().query("year == 2007")
fig = px.scatter_geo(gapminder, locations="iso_alpha", color="continent",
                     hover_name="country", size="pop",
                     projection="orthographic")
fig.show()

print('------------------------------------------------------------')	#60個

#分區標色的日本地圖
#繪製都道府縣行政區域的範例

# 定義基礎地圖 
base_map = folium.Map(location=[35.655616, 139.338853], zoom_start=5.0) 
# 新增Choropleth
folium.Choropleth(geo_data=json.load(open("prefs_064/japan.geojson", "r", encoding ='UTF-8')),
#folium.Choropleth(geo_data=json.load(open("prefs_064/TWN.geo.json", "r", encoding ='UTF-8')),                  
                  fill_color="red",   # 填色
                  fill_opacity=0.3,   # 填色的透明度
                  line_color="black", # 邊界線顏色
                  line_weight=1       # 邊界線粗細
).add_to(base_map)
base_map


#都道府縣標色地圖
#根據資料框架的值替日本的都道府縣標色的範例

# 載入資料
df = pd.read_csv("japan_pop.csv")
# 定義基礎地圖
base_map = folium.Map(location=[35.655616, 139.338853], zoom_start=5.0) 
# 新增Choropleth
folium.Choropleth(geo_data=json.load(open("prefs_064/japan.geojson", "r", encoding ='UTF-8')),
                  data=df,                          # 都道府縣的資料
                  columns=["name", "value"],        # 用於填色的Key與欄位名稱
                  key_on="feature.properties.name", # geojson的行政區域的Key
                  fill_color='PuRd'                 # 填色的調色處
).add_to(base_map)
base_map


#顯示地圖的點資訊
#在地圖某一點標記符號的範例

map = folium.Map(location=[35.702083, 139.745023], zoom_start=13)
# 標記符號
folium.Marker(location= [35.685175,139.7528]).add_to(map)
map




print('------------------------------------------------------------')	#60個

#將作為底圖的地圖設定為cartodbpositron的範例

map = folium.Map(location=[35.702083, 139.745023],
                 tiles="cartodbpositron", zoom_start=10) 
# 標記符號 
folium.Marker(location=[35.685175, 139.7528]).add_to(map) 
map

#將作為底圖的地圖設定為Stamen Toner的範例

map = folium.Map(location=[35.702083, 139.745023],
                 tiles="Stamen Toner", zoom_start=10) 
# 標記符號 
folium.Marker(location=[35.685175, 139.7528]).add_to(map) 
map



#在兩個地點標記符號的範例

map = folium.Map(location=[35.702083, 139.745023], tiles="cartodbpositron",zoom_start=13)
# 標記符號
folium.Marker(location=[35.685175, 139.7528]).add_to(map)      # 第一個地點的經緯度
folium.Marker(location=[35.699861, 139.763889]).add_to(map)    # 第一個地點的經緯度
map




print('------------------------------------------------------------')	#60個

#在地圖繪製大小不同的圓形
#定義資料

stations = [
    {
        "name": "Shinjuku", "lat": 35.690921, "lon": 139.700257,
        "amount": 778618,
    },
    {
        "name": "Ikebukuro", "lat": 35.728926, "lon": 139.71038,
        "amount": 566516,
    },
    {
        "name": "Tokyo", "lat": 35.681382, "lon": 139.766083,
        "amount": 452549,
    },
    {
        "name": "Yurakucho", "lat": 35.675069, "lon": 139.763328,
        "amount": 169943,
    },
    {
        "name": "Kanda", "lat": 35.69169, "lon": 139.770883,
        "amount": 103940,
    },
    {
        "name": "Bakurocho", "lat": 35.693361, "lon": 139.782389,
        "amount": 25784,
    },
    {
        "name": "Etchujima", "lat": 35.667944, "lon": 139.792694,
        "amount": 5502,
    }
]

stations_df = pd.DataFrame(stations)
print(stations_df)




print('------------------------------------------------------------')	#60個

#在地圖繪製圓形的範例

# 以銷售量最少的車站為銷售量基準
base_amount = min(stations_df["amount"])

# 圓形的縮放倍率
scale = 10

# 定義地圖
map = folium.Map(location=[35.702083, 139.745023], zoom_start=11)

# 利用圓形說明銷售量
for index, row in stations_df.iterrows():
    location = (row["lat"], row["lon"])   # 座標
    radius = scale * (row["amount"] / base_amount) # 圓形的大小
    # 在地圖新增圓形
    folium.Circle(location=location,      # 地點的經緯度
                  radius=radius,          # 圓形的大小
                  color="darkblue",       # 圓形的顏色
                  fill_color="darkblue",  # 圓形的填色
                  popup=row["name"]       # 於滑鼠移入之際顯示的項目
    ).add_to(map)
map


print('------------------------------------------------------------')	#60個

#在地圖繪製熱圖

# 定義地圖
map = folium.Map(location=[35.681382, 139.766083],
                 tiles="cartodbpositron", zoom_start=11)

# 根據經緯度資訊在地圖繪製熱圖
map.add_child(HeatMap(stations_df[["lat", "lon"]], radius=70))
map


#指定在地圖顯示的符號種類

# 設定符號的圖片檔
MARKER_IMG = "original_icon\ATM_icon.png"  
# 符號的透明度
OPACITY = 1  
# 定義資料
stations = [
    {"name": "Shinjuku", "lat": 35.690921, "lon": 139.700257},
    {"name": "Ikebukuro", "lat": 35.728926, "lon": 139.71038},
    {"name": "Tokyo", "lat": 35.681382, "lon": 139.766083}
]

# 轉換為資料框架
df = pd.DataFrame({"name": [x["name"] for x in stations],
                   "lat": [x["lat"] for x in stations],
                   "lon": [x["lon"] for x in stations]})

# 定義地圖
map = folium.Map(location=[35.702083, 139.745023], zoom_start=13) 
# 繪製圖片
dx = 0.005 
dy = 0.005 
for index, row in df.iterrows():
    bounds = [[row["lat"] - dx, row["lon"] - dy],
              [row["lat"] + dx, row["lon"] + dy]]    
    map.add_child(folium.raster_layers.ImageOverlay(MARKER_IMG, opacity=OPACITY,
                                                bounds=bounds)) 
map





print('------------------------------------------------------------')	#60個

#以線條串起兩個地點
#在兩個地點之間畫線

map = folium.Map(location=[36, 137.59], zoom_start=5)

# 在地圖繪製線條
folium.PolyLine(
    locations=[
        [35.54732, 139.7726452], 
        [34.7863123, 135.4355808]
    ]
).add_to(map)

# 顯示地圖
map


print('------------------------------------------------------------')	#60個

#在多個地點之間畫線的範例


# 定義起點、終點與線條的粗細
lines = [
    {
        "from": [35.54732, 139.7726452],    # 第一個起點的經緯度
        "to": [34.7863123, 135.4355808],    # 第一個終點的經緯度
        "weight": 5                         # 線條粗細
    },
    {
        "from": [35.54732, 139.7726452],    # 第二個起點的經緯度
        "to": [26.231408, 127.685525],      # 第二個終點的經緯度
        "weight": 2                         # 線條粗細
    }
]

# 定義地圖
map = folium.Map(location=[36, 137.59], zoom_start=5)

# 在地圖繪製線條
for line in lines:
    folium.PolyLine(
        locations=[line["from"], line["to"]],
        weight=line["weight"]
    ).add_to(map)

# 顯示地圖
map







print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

