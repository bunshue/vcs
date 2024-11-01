"""
海生, 自動把圖畫得比較好看

sns.set() 繪圖風格設置

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

plt.plot(x, y)
plt.title("無海生")
plt.show()

print("------------------------------------------------------------")  # 60個

print("前面加兩行變海生, 引用與設定")

# sns.set()
# sns.set(color_codes=True)
sns.set(rc={"figure.figsize": (6, 4)})

# 海生的中文設定 5 行
font_filename = (
    "C:/_git/vcs/_1.data/______test_files1/_font/TaipeiSansTCBeta-Regular.ttf"
)
import matplotlib as mpl
import matplotlib.font_manager as fm

fm.fontManager.addfont(font_filename)
mpl.rc("font", family="Taipei Sans TC Beta")

plt.plot(x, y)
plt.title("使用海生")

plt.show()

print("------------------------------------------------------------")  # 60個

print("用海生的函數畫圖")

"""
N = 1000
x = np.random.randn(N)
print(np.mean(x))
print('海生函數 histplot')
sns.histplot(x, kde=False)
"""

print("海生函數 lineplot")
sns.lineplot(data=y)

plt.title("用海生的函數畫圖")

plt.show()

print("------------------------------------------------------------")  # 60個

N = 1000  # 樣本數
μ = 87  # 平均值
σ = 2.5  # 標準差
x = np.random.randn(N) * σ + μ

print("平均值 :", x.mean())
print("標準差 :", x.std())

# sns.displot(x)
sns.histplot(x)

plt.show()

print("------------------------------------------------------------")  # 60個

# 一般畫圖 vs 海生畫圖

N = 1000  # 資料個數
num_bins = 50  # 直方圖顯示時的束數

mu, sigma = 100, 15  # 平均值, 標準差
x = np.random.normal(mu, sigma, N)  # 隨機數

n, bins, patches = plt.hist(
    x, bins=num_bins, density=True, color="green", rwidth=0.5, alpha=0.5
)  # 直方圖

# 繪製曲線圖
sns.kdeplot(x)
plt.title("用海生畫常態分佈")

plt.show()

print("------------------------------------------------------------")  # 60個

x = np.random.uniform(size=N)  # 隨機數

n, bins, patches = plt.hist(
    x, bins=num_bins, density=True, color="green", rwidth=0.5, alpha=0.5
)  # 直方圖

# 繪製曲線圖
sns.kdeplot(x)

plt.title("用海生畫均勻分佈")

plt.show()

print("------------------------------------------------------------")  # 60個

N = 10000  # 樣本數
mu = 0  # 平均值
sigma = 1  # 標準差

x1 = np.random.randn(N)  # 隨機數
x2 = np.random.uniform(size=N)  # 隨機數

left = -2
peak = 8  # mode尖峰值
right = 10
x3 = np.random.triangular(left, peak, right, N)

bins = 50  # 束

plt.figure(figsize=(12, 6))

plt.subplot(131)

count, bins, ignored = plt.hist(x1, bins, density=True)  # 直方圖
sns.kdeplot(x1)  # 核密度估計圖, 多了外圍那圈
plt.title("常態分布 + kdeplot")

plt.subplot(132)

plt.hist(x2, bins, density=True)  # 直方圖
sns.kdeplot(x2)  # 核密度估計圖, 多了外圍那圈
plt.title("均勻分布 + kdeplot")

plt.subplot(133)

plt.hist(x3, bins, density=True)
# sns.kdeplot(x3)  # 核密度估計圖, 多了外圍那圈
plt.title("np.random.triangular")

# 用density
# plt.hist(x3, bins, density=True)

plt.show()

print("------------------------------------------------------------")  # 60個

# 共同參數
x = np.linspace(0, 2 * np.pi, 30)
y = np.sin(x)
y0 = np.sin(x)
y1 = np.cos(x)
y2 = np.tan(x)

print("------------------------------------------------------------")  # 60個

plt.plot(x, y)
plt.title("無海生")
plt.show()

print("------------------------------------------------------------")  # 60個

# plt.xkcd()  #加此行變成搞笑風格

# 多此二行 變成海生風格

sns.set()

plt.rcParams[
    "font.sans-serif"
] = "Microsoft JhengHei"  # 海生設定中文字型 將字體換成 Microsoft JhengHei

plt.plot(x, y)
plt.title("使用海生")
plt.show()

print("------------------------------------------------------------")  # 60個

plt.xlabel("銷售張數")
plt.ylabel("成功次數")
sns.histplot(np.random.binomial(n=5, p=0.75, size=1000), kde=False)
# sns.histplot(np.random.binomial(n=10, p=0.35, size=1000), kde=False)

plt.title("二項式分布 Binomial")

plt.show()

print("------------------------------------------------------------")  # 60個

data = pd.read_csv("_data/president_heights.csv")
print(data.head())

height = np.array(data["height(cm)"])
print(height)

print("Mean of heights =", height.mean())
print("Standard Deviation of height =", height.std())
print("Minimum height =", height.min())
print("Maximum height =", height.max())

print("25th percentile =", np.percentile(height, 25))
print("Median =", np.median(height))
print("75th percentile =", np.percentile(height, 75))

sns.set()

plt.hist(height)
plt.title("Height Distribution of Presidents of USA")
plt.xlabel("height(cm)")
plt.ylabel("Number")

plt.show()

print("------------------------------------------------------------")  # 60個

x = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10]
sinus = [math.sin(v) for v in x]
cosinus = [math.cos(v) for v in x]

sns.set()

fig, axes = plt.subplots(1, 2, figsize=(6, 4))
ax1 = sns.lineplot(x=x, y=sinus, ax=axes[0])
ax2 = sns.scatterplot(x=x, y=cosinus, ax=axes[1])

plt.show()

print("------------------------------------------------------------")  # 60個

x = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10]
sinus = [math.sin(v) for v in x]
cosinus = [math.cos(v) for v in x]

df = pd.DataFrame()
df["x"] = x
df["sin"] = sinus
df["cos"] = cosinus
print(df.head())

df2 = pd.melt(df, id_vars=["x"], value_vars=["sin", "cos"])
print(df2.head())

sns.set()

sns.relplot(x="x", y="value", kind="scatter", col="variable", data=df2)

plt.show()

print("------------------------------------------------------------")  # 60個

x = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10]
sinus = [math.sin(v) for v in x]

sns.set_style("whitegrid")

sns.lineplot(x=x, y=sinus)

plt.show()

print("------------------------------------------------------------")  # 60個

x = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10]
sinus = [math.sin(v) for v in x]

sns.set_style("whitegrid")

sns.lineplot(x=x, y=sinus)
sns.despine()

plt.show()

print("------------------------------------------------------------")  # 60個

x = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10]
sinus = [math.sin(v) for v in x]

sns.set_style("darkgrid", {"axes.axisbelow": False})

sns.lineplot(x=x, y=sinus)

plt.show()

print(sns.axes_style())

print("------------------------------------------------------------")  # 60個

x = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10]
sinus = [math.sin(v) for v in x]

plt.rcParams["axes.unicode_minus"] = False
sns.set_style(
    "darkgrid", {"axes.axisbelow": False, "font.sans-serif": ["Microsoft JhengHei"]}
)
sns.lineplot(x=x, y=sinus)
plt.title("Sinus三角函數的波型")
plt.xlim(-2, 12)
plt.ylim(-2, 2)
plt.xlabel("x")
plt.ylabel("sin(x)")

plt.show()

print("------------------------------------------------------------")  # 60個

x = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10]
sinus = [math.sin(v) for v in x]
cosinus = [math.cos(v) for v in x]

df = pd.DataFrame()
df["x"] = x
df["sin"] = sinus
df["cos"] = cosinus
print(df.head())

df2 = pd.melt(df, id_vars=["x"], value_vars=["sin", "cos"])
print(df2.head())

sns.set()

sns.relplot(
    x="x", y="value", kind="scatter", col="variable", height=4, aspect=1.2, data=df2
)

plt.show()

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("_data/Kobe_stats.csv")

data = pd.DataFrame()
data["Season"] = pd.to_datetime(df["Season"])
data["PTS"] = df["PTS"]

sns.set()

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

# 繪製折線圖
# sns.set(style="white", font="meiryo")

# 調整資料的格式
# sns.set(style="white", font="meiryo")
# sns.set(style="white", font="meiryo")

# ax.legend(loc="lower left", bbox_to_anchor=(1, 0))
