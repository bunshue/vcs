"""
疫情數據分析


"""

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

print("------------------------------------------------------------")  # 60個

print("疫情數據分析")

# 讀入疫情數據, 做簡單的分析
df0 = pd.read_csv(
    "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
)

# 在 pandas 最常用的指令, 大概就是用 head 看看 Data Frame 長什麼樣子。
print("看看資料的前5筆a")
print(df0.head())

# 我們把一些不用的欄位刪掉。
df0 = df0.drop(columns=["Province/State", "Lat", "Long"])

# 再欣賞一下, 看 Data Frame 是不是又清爽一些？
print("看看資料的前5筆b, 少了3個欄位")
print(df0.head())

# 為了方便說明, 我們只選擇幾個國家來分析。
df = df0.loc[
    df0["Country/Region"].isin(
        ["Taiwan*", "Japan", "Korea, South", "Germany", "Singapore"]
    )
]
print("選幾個國家來分析")
print(df)

print("df 這個 Data Frame 改以國家為 index")
df = df.set_index("Country/Region")

print("行列互換")
df = df.T
print(df.head())

print("改成每日新增案例, 而不是累計案例")
df = df.diff()
print(df.head())

print("去掉第一天")
df = df.drop(["1/22/20"])
print(df.head())

print("把 index 的日期改為「真的」日期")
df.index = pd.to_datetime(df.index)
print(df.head())

# 我們來依人口調整, 較能比較。最後我們希望得到的是「每 10 萬人中, 有多少人染疫」
population = np.array([84284340, 125753381, 51351596, 5936285, 23897291]) / 100000
dfm = df / population
print("每10萬人中,有多少人染疫")
print(dfm.tail())

# 畫個最近 2 個月的圖試試看
dfm[-60:].plot()
plt.title("最近2個月的圖")
plt.show()

print("看各國疫情最高峰的數目大概是多少, 這樣也知道台灣的狀況應該算如何")
print(dfm.max(axis=0))

# 注意前面我們發現, 我們的數據有些問題。可能有些日子疫情沒有更新, 所以新增是 0, 結果加到下一天去。
# 在實際的工作中, 我們會花很多時間去調校, 做「資料清理」。
# 現在我們準備看看各國疫情高峰期, 走勢大概是怎麼樣的。

de = dfm["Germany"]
jp = dfm["Japan"]
kr = dfm["Korea, South"]
sg = dfm["Singapore"]
tw = dfm["Taiwan*"]

# 試以德國為例, 我們看看最高峰前後兩個月的樣子。
n = de.argmax()
period = de[n - 60 : n + 60]
ma = period.rolling(window=7).mean()[6:]
period[6:].plot()
ma.plot()
plt.title("德國的情況")
plt.show()

# 把剛剛的想法寫成一個函式, 簡簡單單就應用到不同國家。


def peak_period(country):
    n = country.argmax()
    period = country[n - 60 : n + 60]
    ma = period.rolling(window=7).mean()[6:]
    period[6:].plot()
    ma.plot()


# 日本的情況
peak_period(jp)
plt.title("日本的情況")
plt.show()

# 韓國的情況
peak_period(kr)
plt.title("韓國的情況")
plt.show()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
