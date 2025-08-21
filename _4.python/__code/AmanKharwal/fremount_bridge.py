"""
fremount_bridge

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

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

data = pd.read_csv("data/fremont-bridge.csv", index_col="Date", parse_dates=True)
cc = data.head()
print(cc)

data.columns = ["West", "East"]
cc = data.head()
print(cc)

data["Total"] = data["West"] + data["East"]
cc = data.head()
print(cc)

cc = data.dropna().describe()
print(cc)

sns.set()  # 多了這行, 即使用海生風格

data.plot()
plt.ylabel("Hourly Bicycle count")
plt.show()

weekly = data.resample("W").sum()
weekly.plot(style=[":", "--", "-"])
plt.ylabel("Weekly bicycle count")
plt.show()

daily = data.resample("D").sum()
daily.rolling(30, center=True).sum().plot(style=[":", "--", "-"])
plt.ylabel("mean hourly count")
plt.show()

daily.rolling(50, center=True, win_type="gaussian").sum(std=10).plot(
    style=[":", "--", "-"]
)
plt.show()

by_time = data.groupby(data.index.time).mean()
hourly_ticks = 4 * 60 * 60 * np.arange(6)
by_time.plot(xticks=hourly_ticks, style=[":", "--", "-"])
plt.ylabel("Traffic according to time")
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個
