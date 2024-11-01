"""
海生, 自動把圖畫得比較好看
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

# 共同參數
x = np.linspace(0, 2 * np.pi, 30)
y = np.sin(x)
y0 = np.sin(x)
y1 = np.cos(x)
y2 = np.tan(x)

print("------------------------------------------------------------")  # 60個

# 海生設定

# sns.set()  # 無參數, 海生預設設定, 會清除中文設定
# sns.set(....) # 海生風格設定

# sns.set()  # 無參數, 海生預設設定, 會清除中文設定
# sns.set(color_codes=True)
sns.set(rc={"figure.figsize": (6, 4)})

#sns.set_style("whitegrid")
#sns.set_style("darkgrid", {"axes.axisbelow": False})
#sns.set_style("darkgrid", {"axes.axisbelow": False, "font.sans-serif": ["Microsoft JhengHei"]})

# 海生的中文設定 5 行
font_filename = (
    "C:/_git/vcs/_1.data/______test_files1/_font/TaipeiSansTCBeta-Regular.ttf"
)
import matplotlib as mpl
import matplotlib.font_manager as fm

fm.fontManager.addfont(font_filename)
mpl.rc("font", family="Taipei Sans TC Beta")

print("------------------------------------------------------------")  # 60個
'''
print("使用海生")

plt.plot(x, y)
plt.title("使用海生")

plt.show()

print("------------------------------------------------------------")  # 60個

"""
N = 1000
xx = np.random.randn(N)
print(np.mean(xx))
print('海生函數 histplot')
sns.histplot(xx, kde=False)
"""

print("------------------------------------------------------------")  # 60個

N = 1000  # 樣本數
μ = 87  # 平均值
σ = 2.5  # 標準差
xx = np.random.randn(N) * σ + μ

print("平均值 :", xx.mean())
print("標準差 :", xx.std())

num_bins = 50  # 直方圖顯示時的束數
plt.hist(xx, num_bins, density=True)  # 直方圖

plt.show()

print("------------------------------------------------------------")  # 60個

N = 1000  # 資料個數
num_bins = 50  # 直方圖顯示時的束數

mu, sigma = 100, 15  # 平均值, 標準差
xx = np.random.normal(mu, sigma, N)  # 隨機數

n, bins, patches = plt.hist(
    xx, bins=num_bins, density=True, color="green", rwidth=0.5, alpha=0.5
)  # 直方圖

# 繪製曲線圖
sns.kdeplot(xx)
plt.title("用海生畫常態分佈")

plt.show()

print("------------------------------------------------------------")  # 60個

N = 10000  # 樣本數
N = 1000  # 資料個數
num_bins = 50  # 直方圖顯示時的束數

mu, sigma = 100, 15  # 平均值, 標準差
xx = np.random.normal(mu, sigma, N)  # 隨機數

plt.figure(figsize=(12, 6))

plt.subplot(131)

count, bins, ignored = plt.hist(xx, num_bins, density=True)  # 直方圖
sns.kdeplot(xx)  # 核密度估計圖, 多了外圍那圈
plt.title("常態分布 + kdeplot")

plt.subplot(132)

plt.hist(xx, num_bins, density=True)  # 直方圖
sns.kdeplot(xx)  # 核密度估計圖, 多了外圍那圈
plt.title("常態分布 + kdeplot")

plt.subplot(133)

plt.hist(xx, num_bins, density=True)  # 直方圖
sns.kdeplot(xx)  # 核密度估計圖, 多了外圍那圈
plt.title("常態分布 + kdeplot")

plt.show()

print("------------------------------------------------------------")  # 60個

# 共同參數
x = np.linspace(0, 2 * np.pi, 30)
y = np.sin(x)
y0 = np.sin(x)
y1 = np.cos(x)
y2 = np.tan(x)

fig, axes = plt.subplots(1, 2, figsize=(6, 4))

ax1 = sns.lineplot(x=x, y=y, ax=axes[0])
ax2 = sns.scatterplot(x=x, y=y, ax=axes[1])

plt.show()

print("------------------------------------------------------------")  # 60個

df = pd.DataFrame()
df["x"] = x
df["sin"] = y0
df["cos"] = y1
print(df.head())

df2 = pd.melt(df, id_vars=["x"], value_vars=["sin", "cos"])
print(df2.head())

sns.relplot(x="x", y="value", kind="scatter", col="variable", data=df2)

plt.show()

print("------------------------------------------------------------")  # 60個
'''

sns.lineplot(x=x, y=y)
sns.despine()  # ?

plt.show()

print(sns.axes_style())

print("------------------------------------------------------------")  # 60個

sns.lineplot(x=x, y=y)

plt.title("Sinus三角函數的波型")
plt.xlim(-2, 12)
plt.ylim(-2, 2)
plt.xlabel("x")
plt.ylabel("sin(x)")

plt.show()

print("------------------------------------------------------------")  # 60個

df = pd.DataFrame()
df["x"] = x
df["sin"] = y0
df["cos"] = y1
print(df.head())

df2 = pd.melt(df, id_vars=["x"], value_vars=["sin", "cos"])
print(df2.head())

sns.relplot(
    x="x", y="value", kind="scatter", col="variable", height=4, aspect=1.2, data=df2
)

plt.show()

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("_data/Kobe_stats.csv")

data = pd.DataFrame()
data["Season"] = pd.to_datetime(df["Season"])
data["PTS"] = df["PTS"]

sns.relplot(x="Season", y="PTS", data=data, kind="line")

plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


# sns折線圖的繪製範例
# sns.set(style="whitegrid", font="meiryo")

# 調整資料的格式
# sns.set(style="white", font="meiryo")

# ax.legend(loc="lower left", bbox_to_anchor=(1, 0))


# 海生函數 廢棄
sns.lineplot(data=y)
sns.displot(x)
sns.histplot(x)






# plt.xkcd()  #加此行變成搞笑風格

# 多此二行 變成海生風格

plt.rcParams[
    "font.sans-serif"
] = "Microsoft JhengHei"  # 海生設定中文字型 將字體換成 Microsoft JhengHei



sns.histplot(np.random.binomial(n=5, p=0.75, size=1000), kde=False)
# sns.histplot(np.random.binomial(n=10, p=0.35, size=1000), kde=False)

plt.title("二項式分布 Binomial")

plt.show()

print("------------------------------------------------------------")  # 60個

