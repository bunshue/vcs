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
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "data/AQI_20231124.csv"
df = pd.read_csv(filename)
print(df["aqi"])

# 過濾資料
# print(df[(df.aqi < 30)&(df.wind_speed>2)])

df.plot(x="sitename", y=["aqi"])  # 進行繪圖(X軸為地點,Y軸為aqi數值)

show()

print(df["aqi"])
print(df.sort_index(ascending=True).head())
print(df.sort_index(ascending=False).head())

aqi_filter = df["aqi"] > 60

YYY = df[aqi_filter]

print(YYY.head())

pic = df.plot(kind="scatter", x="pm10", y="aqi", title="PM10指數與AQI之關係")

show()

print(pic)

print("------------------------------------------------------------")  # 60個

print("PM2.5與風向之關聯性")

df = pd.read_excel("abc.xlsx")

x = df.WindDirec

y = df.PM25

plt.scatter(x, y)

show()

"""
由於政府公開資料的格式問題，導致風向與PM2.5的視覺化呈現有困難(僅每小時資料提供風向)
因此風向與PM2.5關聯性，將改以文獻閱讀為主
"""
print("------------------------------------------------------------")  # 60個

print("各國PM2.5與溫度比較")

print("北京")

df = pd.read_excel("BeijingPM20100101_20151231.xlsx")

cc = df.head()
print(cc)

x = df["TEMP"]
y = df["PM25"]

plt.xlabel("溫度")  # X軸名稱
plt.ylabel("PM2.5")  # Y軸名稱
plt.title("北京PM2.5與溫度比較")  # 標題
plt.scatter(x, y)
show()

print("瀋陽")

df = pd.read_excel("ShenyangPM20100101_20151231.xlsx")

x = df["TEMP"]
y = df["PM25"]

plt.xlabel("溫度")  # X軸名稱
plt.ylabel("PM2.5")  # Y軸名稱
plt.title("瀋陽PM2.5與溫度比較")  # 標題
plt.scatter(x, y)
show()

""" fail
print('伊朗大不里士')

df=pd.read_excel('Abrasan.xlsx')

cc = df.head()
print(cc)

x=df['TEMP']
y=df['PM25']

plt.xlabel("溫度")                   #X軸名稱
plt.ylabel("PM2.5")                   #Y軸名稱
plt.title("大不里士PM2.5與溫度比較")                    #標題
plt.scatter(x,y)
plt.shop()
"""

"""
結論
綜合日本長崎大學的研究，以及所能蒐集到的數據來看，也許溫度與PM2.5呈現正相關，但是每個國家的情況不同，並沒有一個絕對的基準。
例如印度大部分地區溫度也都蠻高的，但是空汙也相當嚴重，這部分可能又須考量到當地的產業結構等相關問題。
"""

print("------------------------------------------------------------")  # 60個

df = pd.read_excel("1129-0900.xlsx")  # 2018/11/29日早上9點00分的資料

df.plot()
show()

sns.pairplot(df)
show()

sns.pairplot(df, vars=["PM2.5", "AQI", "WindSpeed"], kind="reg")
show()

pic = df.plot(
    kind="scatter", x="WindSpeed", y="PM2.5", title="風速與PM2.5之關係"
)  # 風速越小，PM2.5指數越高
show()

pic = df.plot(kind="scatter", x="WindSpeed", y="AQI", title="風速與AQI之關係")
show()

pic = df.plot(
    kind="scatter", x="PM2.5", y="AQI", title="PM2.5指數與AQI之關係"
)  # PM2.5指數與AQI似乎出現正相關
show()

df.plot(kind="kde")
show()

plt.scatter(df["WindSpeed"], df["PM2.5"], color="red")
show()

plt.scatter(df["WindSpeed"], df["AQI"], color="blue")
show()

plt.scatter(df["WindSpeed"], df["PM2.5"], color="red")
show()

plt.scatter(df["WindSpeed"], df["AQI"], color="blue")
show()

print("------------------------------------------------------------")  # 60個

sns.set_context("notebook")

df = pd.read_excel("2017_PM25.xlsx")

cc = df.head(12)
print(cc)

df.plot(x="監測月份", y=["PM25"], title="2017年度鳳山區PM2.5變化圖")
show()

df.plot(x="監測月份", y=["PM10"], title="2017年度鳳山區PM10變化圖")
show()

df.plot(x="監測月份", y=["SO2"], title="2017年度鳳山區SO2變化圖")
show()

df.plot(x="監測月份", y=["CO"], title="2017年度鳳山區CO變化圖")
show()

df.plot(x="監測月份", y=["O3"], title="2017年度鳳山區O3變化圖")
show()

df.plot(kind="scatter", x="PM10", y="PM25", title="PM2.5與PM10的關係")
show()

df.plot(kind="scatter", x="NO", y="PM25", title="PM2.5與NO的關係")
show()

df.plot(kind="scatter", x="NO2", y="PM25", title="PM2.5與NO2的關係")
show()

df.plot(kind="scatter", x="O3", y="PM25", title="PM2.5與O3的關係")
show()

df.plot(kind="scatter", x="CO", y="PM25", title="PM2.5與CO的關係")
show()

df.plot(kind="scatter", x="SO2", y="PM25", title="PM2.5與SO2的關係")
show()

df.plot(kind="scatter", x="TEMP", y="PM25", title="PM2.5與溫度的關係")
show()

df.plot(kind="scatter", x="RAIN", y="PM25", title="PM2.5與降雨的關係")
show()

df.plot(kind="scatter", x="Humidity", y="PM25", title="PM2.5與濕度的關係")
show()

df.plot(kind="scatter", x="WIND_SPEED", y="PM25", title="PM2.5與風速的關係")
show()

# 正相關 PM10和PM2.5
sns.lmplot(x="PM10", y="PM25", data=df)
plt.title("正相關 PM10和PM2.5")
show()

# 正相關 NO和PM2.5
sns.lmplot(x="NO", y="PM25", data=df)
plt.title("正相關 NO和PM2.5")
show()

# 正相關 NO2和PM2.5
sns.lmplot(x="NO2", y="PM25", data=df)
plt.title("正相關 NO2和PM2.5")
show()

# 正相關 O3和PM2.5
sns.lmplot(x="O3", y="PM25", data=df)
plt.title("正相關 O3和PM2.5")
show()

# 正相關 CO和PM2.5
sns.lmplot(x="CO", y="PM25", data=df)
plt.title("正相關 CO和PM2.5")
show()

# 正相關 SO2和PM2.5
sns.lmplot(x="SO2", y="PM25", data=df)
plt.title("正相關 SO2和PM2.5")
show()

# NOX,THC,NMCH,CH4和PM2.5皆呈現正相關

# 正相關 NOX和PM2.5
sns.lmplot(x="Nox", y="PM25", data=df)
plt.title("正相關 NOX和PM2.5")
show()

# 正相關 THC和PM2.5
sns.lmplot(x="THC", y="PM25", data=df)
plt.title("正相關 THC和PM2.5")
show()

# 正相關 NMHC和PM2.5
sns.lmplot(x="NMHC", y="PM25", data=df)
plt.title("正相關 NMHC和PM2.5")
show()

# 正相關 CH4和PM2.5
sns.lmplot(x="CH4", y="PM25", data=df)
plt.title("正相關 CH4和PM2.5")
show()

# 負相關 溫度和PM2.5
sns.lmplot(x="TEMP", y="PM25", data=df)
plt.title("負相關 溫度和PM2.5")
show()

# 負相關 雨量和PM2.5
sns.lmplot(x="RAIN", y="PM25", data=df)
plt.title("負相關 雨量和PM2.5")
show()

# 負相關 濕度和PM2.5
sns.lmplot(x="Humidity", y="PM25", data=df)
plt.title("負相關 濕度和PM2.5")
show()

# 負相關 風速和PM2.5
sns.lmplot(x="WIND_SPEED", y="PM25", data=df)
plt.title("負相關 風速和PM2.5")
show()

# 負相關 降雨量和PM2.5
sns.lmplot(x="RAIN_COND", y="PM25", data=df)
plt.title("負相關 降雨量和PM2.5")
show()

print("------------------------------------------------------------")  # 60個

plt.style.use("fivethirtyeight")

# 空氣盒子數據溫度與空污

# 使用三種不同的資料

# df = pd.read_csv("200811-201811.csv")
# df=pd.read_excel('20160101-20190101(Daily).xlsx')
df = pd.read_excel("data/KH-1982-2018.xlsx")
cc = df.isnull().sum()
print(cc)

ax = df.plot(kind="scatter", x="TEMP", y="PM25")

ax.set_title("TEMP v.s. PM25")
show()

print("------------------------------------------------------------")  # 60個

# 空氣盒子數據PM25與各項因子之視覺化散布圖
# 高雄1982至2018年之PM25與各氣象因子視覺化散布圖
# 高雄2008至2018年之PM25與各氣象因子視覺化散布圖

# 高雄1982年至2018年之資料 高雄2008年至2018年之資料

plt.style.use("fivethirtyeight")

# 使用三種不同的資料

# df = pd.read_csv("200811-201811.csv")  #高雄2008年至2018年之資料
df = pd.read_excel("data/KH-1982-2018.xlsx")  # 高雄1982年至2018年之資料

cc = df.isnull().sum()
print(cc)

cc = df.head()
print(cc)

ax = df.plot(kind="scatter", x="TEMP", y="PM25")
ax.set_title("TEMP v.s. PM25")
show()

ax = df.plot(kind="scatter", x="Humidity", y="PM25")
ax.set_title("Humidity v.s. PM25")
show()

ax = df.plot(kind="scatter", x="WindSpeed", y="PM25")
ax.set_title("WindSpeed v.s. PM25")
show()

ax = df.plot(kind="scatter", x="CH4", y="PM25")
ax.set_title("CH4 v.s. PM25")
show()

ax = df.plot(kind="scatter", x="NMHC", y="PM25")
ax.set_title("NMHC v.s. PM25")
show()

ax = df.plot(kind="scatter", x="THC", y="PM25")
ax.set_title("THC v.s. PM25")
show()

ax = df.plot(kind="scatter", x="NO2", y="PM25")
ax.set_title("NO2 v.s. PM25")
show()

ax = df.plot(kind="scatter", x="NO", y="PM25")
ax.set_title("NO v.s. PM25")
show()

ax = df.plot(kind="scatter", x="Nox", y="PM25")
ax.set_title("Nox v.s. PM25")
show()

ax = df.plot(kind="scatter", x="PM25", y="PM25")
ax.set_title("PM25 v.s. PM25")
show()

ax = df.plot(kind="scatter", x="O3", y="PM25")
ax.set_title("O3 v.s. PM25")
show()

ax = df.plot(kind="scatter", x="CO", y="PM25")
ax.set_title("CO v.s. PM25")
show()

ax = df.plot(kind="scatter", x="SO2", y="PM25")
ax.set_title("SO2 v.s. PM25")
show()

# 取相關係數, 得到各變數間的相關係數，再用heatmap作圖
heatmap = df.corr()
sns.heatmap(heatmap, cmap="coolwarm")
plt.title("相關係數")
show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個

"""
# 分別從HTML和CSV讀取空氣數據資料

#初始化

#從網站表格引入數據

df = pd.read_html("http://www.86pm25.com/city/gaoxiong.html")
data=df[0]
data.drop(labels=['污染等级'],axis='columns')

#從CSV引入數據

df = pd.read_csv("https://opendata.epa.gov.tw/ws/Data/ATM00625/?$format=csv")
print(df)

#選出高雄市的數據

df1 = df.set_index(['county'])
df1.loc['高雄市']
"""
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

plt.style.use('fivethirtyeight')

print("------------------------------------------------------------")  # 60個

#df畫兩欄位的 散布圖
df.plot(kind="scatter", x="TEMP", y="PM25", title="溫度與PM2.5之關係")
show()


print('屬性轉換 前, 顯示 df 之屬性')
cc1 = df.dtypes
print(cc1)

# df屬性轉換
df["SO2"] = pd.to_numeric(df.SO2, errors="coerce")
df["CO"] = pd.to_numeric(df.CO, errors="coerce")

print('屬性轉換 後, 顯示 df 之屬性, 看不出差異')
cc2 = df.dtypes
print(cc2)



#df = pd.read_csv("C:/_git/vcs/_4.python/ml/data/198207-201811.csv")
df = pd.read_csv("C:/_git/vcs/_4.python/ml/data/200811-201811.csv")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

