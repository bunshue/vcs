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

df = pd.read_csv("data/200811-201811.csv")

from pylab import mpl

mpl.rcParams["font.sans-serif"] = ["Microsoft YaHei"]

# 指定默認字形：解決plot不能顯示中文問題

mpl.rcParams["axes.unicode_minus"] = False

print(df.head(10))

cc = len(df)
print(cc)

cc = df.describe()
print(cc)

cc = df.nlargest(3, "PM25")
print(cc)

cc = df.nsmallest(3, "PM25")
print(cc)

df = df.drop(labels=["SO2", "CO"], axis="columns")  # 刪除SO2和CO這兩個欄位

cc = df.head()
print(cc)

dfSort = df.sort_values(by="PM25", ascending=False)
cc = dfSort.head(20)
print(cc)

df[["WindSpeed", "TEMP"]]  # 顯示Columns(列)為AQI及WindSpeed的數據

cc = df[df.O3 < 15]
print(cc)

cc = df[(df.PM25 < 30) & (df.TEMP > 30)]  # 列出PM2.5值大於30且溫度大於30的數值
print(cc)

df.plot(kind="scatter", x="TEMP", y="PM25", title="溫度與PM2.5之關係")

plt.show()

# df.to_csv('New_Data.csv',encoding='utf8')  #存檔至New_Data.csv中
# df.to_excel('New_Data.xlsx', encoding='utf8')#存檔至New_Data.xlsx

print("------------------------------------------------------------")  # 60個

df = pd.read_excel("data/AQI.xlsx")
gc = sns.pairplot(df)

cc = df.corr()
print(cc)

df_1127 = pd.read_excel("data/20181127.xlsx")
gc = sns.pairplot(df_1127, kind="reg")

cc = df_1127.corr()
print(cc)

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/198207-201811.csv")
pd.set_option("display.max_rows", 1000)  # 設定最大能顯示1000rows
pd.set_option("display.max_columns", 1000)  # 設定最大能顯示1000columns

from pylab import mpl

mpl.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
# 指定默認字形：解決plot不能顯示中文問題
mpl.rcParams["axes.unicode_minus"] = False

# 檢查屬性
print(df.dtypes)

# 屬性轉換

df["SO2"] = pd.to_numeric(df.SO2, errors="coerce")
df["CO"] = pd.to_numeric(df.CO, errors="coerce")
df["CO2"] = pd.to_numeric(df.CO2, errors="coerce")
df["O3"] = pd.to_numeric(df.O3, errors="coerce")
df["PM25"] = pd.to_numeric(df.PM25, errors="coerce")
df["Nox"] = pd.to_numeric(df.Nox, errors="coerce")
df["NO"] = pd.to_numeric(df.NO, errors="coerce")
df["NO2"] = pd.to_numeric(df.NO2, errors="coerce")
df["THC"] = pd.to_numeric(df.THC, errors="coerce")
df["NMHC"] = pd.to_numeric(df.NMHC, errors="coerce")
df["CH4"] = pd.to_numeric(df.CH4, errors="coerce")
df["WindSpeed"] = pd.to_numeric(df.WindSpeed, errors="coerce")
df["TEMP"] = pd.to_numeric(df.TEMP, errors="coerce")
df["Humidity"] = pd.to_numeric(df.Humidity, errors="coerce")

cc = df.head()
print(cc)

# 處理缺失值

new_df = df.dropna()

cc = new_df.head()
print(cc)


# 檢查屬性是否已經改變

cc = new_df.dtypes
print(cc)

# 存檔至新的CSV
new_df.to_csv("2014-2018.csv", encoding="utf8")

print("------------------------------------------------------------")  # 60個

pd.set_option("display.max_rows", 1000)  # 設定最大能顯示1000rows
pd.set_option("display.max_columns", 1000)  # 設定最大能顯示1000columns

# 2.解決plot不能顯示中文問題
from pylab import mpl

mpl.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
mpl.rcParams["axes.unicode_minus"] = False

# 3.讀取檔案
df = pd.read_excel("C:/Users/Yanwei/a.xlsx")

# 4.資料操作
# 4.1基本操作
df.head(10)  # 顯示出前10筆資料，預設值為5筆資料

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
print("作業完成")
print("------------------------------------------------------------")  # 60個
