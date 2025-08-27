"""
20190408-空氣盒子數據Scikit-Learn Time Series實作


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
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

sns.set()

df = pd.read_excel("data/TimeSeries_198211-201811.xlsx")
cc = df.head()
print(cc)

df.info()  # 這樣就已經把結果印出來

df.Date = pd.to_datetime(df.Date)
df.set_index("Date", inplace=True)

cc = df.head(5)
print(cc)

df[["CH4"]].plot(figsize=(20, 10), linewidth=5, fontsize=20)
plt.xlabel("Year", fontsize=20)
plt.title("CH4", fontsize=40)

plt.show()

print("------------------------------------------------------------")  # 60個

PM25 = df[["PM25"]]
PM25.rolling(12).mean().plot(figsize=(20, 10), linewidth=5, fontsize=20)
plt.xlabel("Year", fontsize=20)
plt.title("PM2.5", fontsize=40)

plt.show()

print("------------------------------------------------------------")  # 60個

O3 = df[["O3"]]
O3.rolling(12).mean().plot(figsize=(20, 10), linewidth=5, fontsize=20)
plt.xlabel("Year", fontsize=20)
plt.title("O3", fontsize=40)

plt.show()

print("------------------------------------------------------------")  # 60個

CO = df[["CO"]]
CO.rolling(12).mean().plot(figsize=(20, 10), linewidth=5, fontsize=20)
plt.xlabel("Year", fontsize=20)
plt.title("CO", fontsize=40)

plt.show()

print("------------------------------------------------------------")  # 60個

CH4 = df[["CH4"]]
CH4.rolling(12).mean().plot(figsize=(20, 10), linewidth=5, fontsize=20)
plt.xlabel("Year", fontsize=20)
plt.title("CH4", fontsize=40)

plt.show()

print("------------------------------------------------------------")  # 60個

df_rm = pd.concat(
    [
        PM25.rolling(12).mean(),
        O3.rolling(12).mean(),
        CO.rolling(12).mean(),
        CH4.rolling(12).mean(),
    ],
    axis=1,
)
df_rm.plot(figsize=(20, 10), linewidth=5, fontsize=20)
plt.xlabel("Year", fontsize=20)

plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
