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

print("------------------------------------------------------------")  # 60個
'''
filename = "data/AQI_20231124.csv"
df = pd.read_csv(filename)
print(df.head())
print(len(df))
print(df.describe())
print(df["aqi"])

# print(df[(df.aqi < 30)&(df.wind_speed>2)])

# mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei']    # 指定默认字体：解决plot不能显示中文问题
# mpl.rcParams['axes.unicode_minus'] = False
df.plot(x="sitename", y=["aqi"])

plt.show()


print(df["aqi"])

print(df.sort_index(ascending=True).head())

print(df.sort_index(ascending=False).head())

print(df.shape)

#print(df.mean())  # NG, 包含字串

AQI_filter = df["aqi"] > 60

YYY = df[AQI_filter]

print(YYY.head())


from pylab import mpl

mpl.rcParams["font.sans-serif"] = ["Microsoft YaHei"]  # 指定默认字体：解决plot不能显示中文问题
mpl.rcParams["axes.unicode_minus"] = False

pic = df.plot(kind="scatter", x="pm10", y="aqi", title="PM10指數與AQI之關係")

plt.show()

print(pic)

#print(df.corr())  # NG, 包含字串

print("------------------------------------------------------------")  # 60個

filename = "data/AQI_20231124b.csv"
df = pd.read_csv(filename)
print(df["pm2.5"])

from pylab import mpl

mpl.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
# 指定默認字形：解決plot不能顯示中文問題
mpl.rcParams["axes.unicode_minus"] = False

# wind_speed有缺資料

pic = df.plot(
    kind="scatter", x="wind_speed", y="pm2.5", c="aqi", title="PM2.5指數與AQI與風速之關係"
)

plt.show()

print(pic)


from pylab import mpl

mpl.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
# 指定默認字形：解決plot不能顯示中文問題
mpl.rcParams["axes.unicode_minus"] = False
pic1 = df.plot(kind="scatter", x="wind_speed", y="aqi", title="風速與AQI與之關係")
print(pic1)

plt.show()

print("------------------------------------------------------------")  # 60個

print("PM2.5與風向之關聯性")

df = pd.read_excel("abc.xlsx")

x = df.WindDirec

y = df.PM25

plt.scatter(x, y)

plt.show()

"""
由於政府公開資料的格式問題，導致風向與PM2.5的視覺化呈現有困難(僅每小時資料提供風向)
因此風向與PM2.5關聯性，將改以文獻閱讀為主
"""

from IPython.display import Image
from IPython.core.display import HTML

PATH = "tree.png"  # 圖片路徑

Image(filename=PATH, width=600, height=600)

PATH2 = "wind-direction.png"  # 圖片路徑

Image(filename=PATH2, width=600, height=600)

print("------------------------------------------------------------")  # 60個

print("各國PM2.5與溫度比較")

print("北京")

df = pd.read_excel("BeijingPM20100101_20151231.xlsx")

cc = df.head()
print(cc)

from pylab import mpl

mpl.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
mpl.rcParams["axes.unicode_minus"] = False

x = df["TEMP"]
y = df["PM25"]

plt.xlabel("溫度")  # X軸名稱
plt.ylabel("PM2.5")  # Y軸名稱
plt.title("北京PM2.5與溫度比較")  # 標題
plt.scatter(x, y)
plt.show()

print("瀋陽")

df = pd.read_excel("ShenyangPM20100101_20151231.xlsx")

x = df["TEMP"]
y = df["PM25"]

plt.xlabel("溫度")  # X軸名稱
plt.ylabel("PM2.5")  # Y軸名稱
plt.title("瀋陽PM2.5與溫度比較")  # 標題
plt.scatter(x, y)
plt.show()

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

from pylab import mpl

mpl.rcParams["font.sans-serif"] = ["Microsoft YaHei"]

mpl.rcParams["axes.unicode_minus"] = False

df = pd.read_excel("1129-0900.xlsx")  # 2018/11/29日早上9點00分的資料

df.plot()

plt.show()


cc = df.info()
print(cc)

cc = df.describe()
print(cc)

sns.pairplot(df)

plt.show()

sns.pairplot(df, vars=["PM2.5", "AQI", "WindSpeed"], kind="reg")

plt.show()

"""
cc = df.corr()  # NG, 包含字串
print(cc)
"""

pic = df.plot(
    kind="scatter", x="WindSpeed", y="PM2.5", title="風速與PM2.5之關係"
)  # 風速越小，PM2.5指數越高
plt.show()

pic = df.plot(kind="scatter", x="WindSpeed", y="AQI", title="風速與AQI之關係")
plt.show()

pic = df.plot(
    kind="scatter", x="PM2.5", y="AQI", title="PM2.5指數與AQI之關係"
)  # PM2.5指數與AQI似乎出現正相關
plt.show()

df.plot(kind="kde")
plt.show()

plt.scatter(df["WindSpeed"], df["PM2.5"], color="red")
plt.show()


plt.scatter(df["WindSpeed"], df["AQI"], color="blue")
plt.show()

plt.scatter(df["WindSpeed"], df["PM2.5"], color="red")
plt.show()

plt.scatter(df["WindSpeed"], df["AQI"], color="blue")
plt.show()

print("------------------------------------------------------------")  # 60個

pd.set_option("display.max_rows", 1000)  # 設定最大能顯示1000rows
pd.set_option("display.max_columns", 1000)  # 設定最大能顯示1000columns

from pylab import mpl

mpl.rcParams["font.sans-serif"] = ["Microsoft YaHei"]

# 指定默認字形：解決plot不能顯示中文問題

mpl.rcParams["axes.unicode_minus"] = False

sns.set_context("notebook")

df = pd.read_excel("2017_PM25.xlsx")

cc = df.head(12)
print(cc)

print(df.dtypes)

print(df.describe())

#print(df.corr())  # NG, 包含字串

df.plot(x="監測月份", y=["PM25"], title="2017年度鳳山區PM2.5變化圖")
plt.show()

df.plot(x="監測月份", y=["PM10"], title="2017年度鳳山區PM10變化圖")
plt.show()

df.plot(x="監測月份", y=["SO2"], title="2017年度鳳山區SO2變化圖")
plt.show()

df.plot(x="監測月份", y=["CO"], title="2017年度鳳山區CO變化圖")
plt.show()

df.plot(x="監測月份", y=["O3"], title="2017年度鳳山區O3變化圖")
plt.show()

df.plot(kind="scatter", x="PM10", y="PM25", title="PM2.5與PM10的關係")
plt.show()

df.plot(kind="scatter", x="NO", y="PM25", title="PM2.5與NO的關係")
plt.show()

df.plot(kind="scatter", x="NO2", y="PM25", title="PM2.5與NO2的關係")
plt.show()

df.plot(kind="scatter", x="O3", y="PM25", title="PM2.5與O3的關係")
plt.show()

df.plot(kind="scatter", x="CO", y="PM25", title="PM2.5與CO的關係")
plt.show()

df.plot(kind="scatter", x="SO2", y="PM25", title="PM2.5與SO2的關係")
plt.show()

df.plot(kind="scatter", x="TEMP", y="PM25", title="PM2.5與溫度的關係")
plt.show()

df.plot(kind="scatter", x="RAIN", y="PM25", title="PM2.5與降雨的關係")
plt.show()

df.plot(kind="scatter", x="Humidity", y="PM25", title="PM2.5與濕度的關係")
plt.show()

df.plot(kind="scatter", x="WIND_SPEED", y="PM25", title="PM2.5與風速的關係")
plt.show()

# 正相關 PM10和PM2.5
sns.lmplot(x="PM10", y="PM25", data=df)
plt.title("正相關 PM10和PM2.5")
plt.show()

# 正相關 NO和PM2.5
sns.lmplot(x="NO", y="PM25", data=df)
plt.title("正相關 NO和PM2.5")
plt.show()

# 正相關 NO2和PM2.5
sns.lmplot(x="NO2", y="PM25", data=df)
plt.title("正相關 NO2和PM2.5")
plt.show()

# 正相關 O3和PM2.5
sns.lmplot(x="O3", y="PM25", data=df)
plt.title("正相關 O3和PM2.5")
plt.show()

# 正相關 CO和PM2.5
sns.lmplot(x="CO", y="PM25", data=df)
plt.title("正相關 CO和PM2.5")
plt.show()

# 正相關 SO2和PM2.5
sns.lmplot(x="SO2", y="PM25", data=df)
plt.title("正相關 SO2和PM2.5")
plt.show()

# NOX,THC,NMCH,CH4和PM2.5皆呈現正相關

# 正相關 NOX和PM2.5
sns.lmplot(x="Nox", y="PM25", data=df)
plt.title("正相關 NOX和PM2.5")
plt.show()

# 正相關 THC和PM2.5
sns.lmplot(x="THC", y="PM25", data=df)
plt.title("正相關 THC和PM2.5")
plt.show()

# 正相關 NMHC和PM2.5
sns.lmplot(x="NMHC", y="PM25", data=df)
plt.title("正相關 NMHC和PM2.5")
plt.show()

# 正相關 CH4和PM2.5
sns.lmplot(x="CH4", y="PM25", data=df)
plt.title("正相關 CH4和PM2.5")
plt.show()

# 負相關 溫度和PM2.5
sns.lmplot(x="TEMP", y="PM25", data=df)
plt.title("負相關 溫度和PM2.5")
plt.show()

# 負相關 雨量和PM2.5
sns.lmplot(x="RAIN", y="PM25", data=df)
plt.title("負相關 雨量和PM2.5")
plt.show()

# 負相關 濕度和PM2.5
sns.lmplot(x="Humidity", y="PM25", data=df)
plt.title("負相關 濕度和PM2.5")
plt.show()

# 負相關 風速和PM2.5
sns.lmplot(x="WIND_SPEED", y="PM25", data=df)
plt.title("負相關 風速和PM2.5")
plt.show()

# 負相關 降雨量和PM2.5
sns.lmplot(x="RAIN_COND", y="PM25", data=df)
plt.title("負相關 降雨量和PM2.5")
plt.show()

print("------------------------------------------------------------")  # 60個

plt.style.use("fivethirtyeight")

# 空氣盒子數據溫度與空污

# 使用三種不同的資料

# df = pd.read_csv("200811-201811.csv")
# df=pd.read_excel('20160101-20190101(Daily).xlsx')
df = pd.read_excel("data/KH-1982-2018.xlsx")
cc = df.isnull().sum()
print(cc)

cc = df.head()
print(cc)

cc = df.describe()
print(cc)

ax = df.plot(kind="scatter", x="TEMP", y="PM25")

ax.set_title("TEMP v.s. PM25")
plt.show()

cc = df.corr()
print(cc)

print("------------------------------------------------------------")  # 60個

""" NG

#pandas-profiling套件測試

#使用pandas_profiling模組分析並輸出成html

#高雄2008年至2018年之資料

import pandas_profiling

plt.style.use('fivethirtyeight')

df = pd.read_csv("200811-201811.csv")

profile = pandas_profiling.ProfileReport(df)

pandas_profiling.ProfileReport(df)

profile.to_file(outputfile="output.html")  #支援輸出html
"""

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

cc = df.corr()
print(cc)

ax = df.plot(kind="scatter", x="TEMP", y="PM25")
ax.set_title("TEMP v.s. PM25")
plt.show()


ax = df.plot(kind="scatter", x="Humidity", y="PM25")
ax.set_title("Humidity v.s. PM25")
plt.show()


ax = df.plot(kind="scatter", x="WindSpeed", y="PM25")
ax.set_title("WindSpeed v.s. PM25")
plt.show()

ax = df.plot(kind="scatter", x="CH4", y="PM25")
ax.set_title("CH4 v.s. PM25")
plt.show()

ax = df.plot(kind="scatter", x="NMHC", y="PM25")
ax.set_title("NMHC v.s. PM25")
plt.show()

ax = df.plot(kind="scatter", x="THC", y="PM25")
ax.set_title("THC v.s. PM25")
plt.show()

ax = df.plot(kind="scatter", x="NO2", y="PM25")
ax.set_title("NO2 v.s. PM25")
plt.show()

ax = df.plot(kind="scatter", x="NO", y="PM25")
ax.set_title("NO v.s. PM25")
plt.show()

ax = df.plot(kind="scatter", x="Nox", y="PM25")
ax.set_title("Nox v.s. PM25")
plt.show()

ax = df.plot(kind="scatter", x="PM25", y="PM25")
ax.set_title("PM25 v.s. PM25")
plt.show()

ax = df.plot(kind="scatter", x="O3", y="PM25")
ax.set_title("O3 v.s. PM25")
plt.show()

ax = df.plot(kind="scatter", x="CO", y="PM25")
ax.set_title("CO v.s. PM25")
plt.show()

ax = df.plot(kind="scatter", x="SO2", y="PM25")
ax.set_title("SO2 v.s. PM25")
plt.show()

heatmap = df.corr()
sns.heatmap(heatmap, cmap="coolwarm")
plt.show()

print("------------------------------------------------------------")  # 60個

'''
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

# 初始環境設定

df = pd.read_csv("data/200811-201811.csv")
pd.set_option("display.max_rows", 1000)  # 設定最大能顯示1000rows
pd.set_option("display.max_columns", 1000)  # 設定最大能顯示1000columns
from pylab import mpl

mpl.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
# 指定默認字形：解決plot不能顯示中文問題
mpl.rcParams["axes.unicode_minus"] = False

# 檢查屬性

cc = df.dtypes
print(cc)

print("------------------------------------------------------------")  # 60個

# Pandas資料分析筆記

pd.set_option("display.max_rows", 1000)  # 設定最大能顯示1000rows
pd.set_option("display.max_columns", 1000)  # 設定最大能顯示1000columns

# 2.解決plot不能顯示中文問題

from pylab import mpl

mpl.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
mpl.rcParams["axes.unicode_minus"] = False

# 3.讀取檔案

df = pd.read_csv(r"data/AQI_20231124.csv")

# 兩個df的差別
# 1)在前方加r，就不用反斜線
# 2)使用反斜線就不用加r

# 4.資料操作
# 4.1基本操作

df.head(10)  # 顯示出前10筆資料，預設值為5筆資料
df.tail(10)  # 顯示後10筆資料
df.shape  # 顯示出資料共有(X行,Y列)
len(df)  # 顯示資料總筆數
df.dtypes  # 顯示資料類型
df.describe()  # 顯示統計數字(最大、最小、平均......等)
df[["AQI"]]  # 顯示Columns(列)為AQI的數據
df.AQI  # 顯示Columns(列)為AQI的數據
df.columns = ["XXX", "XXX", "XXX"]  # 重新命名欄位
df.T  # 行與列互換
df.info()  # 顯示資料的狀態與資訊

# 4.2 iloc,loc,ix方法

df.iloc[4]  # 顯示第4筆資料的所有數據
df1 = df.set_index(["測站"])  # 將測站設定為索引(即擺到第一行第一列)
df1 = df1.reset_index(["測站"])  # 恢復原本設置
df1.loc["左營"]  # 列出所有左營的數據

# 4.3刪除資料

df.drop(labels=["SO2", "CO"], axis="columns")  # 刪除SO2和CO這兩個欄位
df = df.drop_duplicates()  # 刪除重複的資料
# axis=0和asxis='row'一樣
# axis=1和axis='columns'一樣

# 4.4處理NaN資料

df.dropna()  # 刪除NaN的資料
df = df.dropna()  # 將刪除後的資料存到變數
df.dropna(axis=1)  # 删除所有包含空值的列
df = df.fillna(0)  # 把NaN資料替換成0
df["A"].fillna(value=df["A"].mean())  # 把NaN值改成該屬性的所有平均值

# 4.5指定特殊需求

df.sort_index(ascending=True).head(100)  # 升階排序
df.sort_index(ascending=False).head(100)  # 降階排序

# 4.6備註

# 基本上df[['AQI']]和df.AQI功能一樣
# iloc只對數值類型有用，loc只對字串類型有用，ix混合iloc與loc(但不建議，易失敗)

# 5.字串處理
# 5.1大小寫與字串變更

df["PM2.5"].str.title()  # 讓字串第一個字為大寫
df["PM2.5"].str.lower()  # 讓字串全部變成小寫
df["PM2.5"].str.upper()  # 讓字串全部變成大寫
df["PM2.5"] = df["PM2.5"].str.replace("要改變的字串", "想改變成的字串")

# 5.2找出資料

df[df.AQI.startswith("高雄市")]  # 顯示出高雄市開頭的資料
df[df.AQI.endswith("高雄市")]  # 顯示出高雄市做為結尾的資料

# 6.來一點複雜操作

df[
    ["AQI", "WindSpeed"]
]  # 顯示Columns(列)為AQI及WindSpeed的數據df[df.AQI<50]          #顯示AQI<50的數值
df[(df.AQI < 30) & (df.WindSpeed > 2)]  # 列出AQI值大於30且風速大於2的數值
df["AQI"] / 2  # 將所有AQI值除以2(+,-,*,/皆適用)
# -----------------------------------------
AQI_filter = df["AQI"] > 60  # 使用布林，當AQI>60為True，<60為False

Bad_AQI = df[AQI_filter]  # 將過濾後的數值存入至Bad_AQI
Bad_AQI.head()  # 只顯示AQI>60的資料

AQI_filter_2 = (df["AQI"] > 60) & (df["PM2.5"] > 40)
# 使用布林，條件是AQI>60且PM2.5數值超過40

Bad_AQI_PM = df[AQI_filter_2]  # 將過濾後的數值存入至Bad_AQI_PM
Bad_AQI_PM.head()  # 只顯示AQI>60且PM2.5>40的資料

# 7.繪圖與存檔
# 7.1資料視覺化

df.plot(x="SiteName", y=["AQI"])  # 進行繪圖(X軸為地點,Y軸為AQI數值)
pic = df.plot(
    kind="scatter", x="WindSpeed", y="PM2.5", title="風速與PM2.5之關係"
)  # 製作散布圖,X軸風速,Y軸為PM2.5指數
print(pic)

# 7.2存檔

df.to_csv("New_Data.csv", encoding="utf8")  # 存檔至New_Data.csv中
df.to_json("New_Data.json", encoding="utf8")  # 存檔至New_Data.json
df.to_excel("New_Data.xlsx", encoding="utf8")  # 存檔至New_Data.xlsx

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
