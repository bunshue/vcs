"""
# hist 集合

np.random.normal
np.random.randn
np.random.rand(
np.random.uniform(size=N)
random.randint

"""

print("------------------------------------------------------------")  # 60個

N = 500  # 資料個數
num_bins = 50  # 直方圖顯示時的束數

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
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
#          編號               圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(
    num="hist 集合 1",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.suptitle("皆為 np.random.normal\t" + r"$\mu = 200, \sigma=25$")

mu = 100  # 平均值
sigma = 15  # 標準差
mu, sigma = 100, 15
x = np.random.normal(mu, sigma, size=N * 10)  # 隨機數
# 生成 N 組標準常態分配（平均值為 0，標準差為 1 的常態分配）隨機變數
# x = np.random.normal(size=N*10)
# x = np.random.normal(size=N)


# 第一張圖
plt.subplot(231)

plt.hist(
    x,
    bins=num_bins,
    histtype="bar",
    facecolor="r",
    edgecolor="g",
    alpha=0.75,
    rwidth=0.8,
    label="Normal distribution",
)
plt.title("histtype 1 : bar")

# 第二張圖
plt.subplot(232)

plt.hist(
    x,
    bins=num_bins,
    histtype="barstacked",
    facecolor="g",
    edgecolor="b",
    alpha=0.75,
    rwidth=0.8,
    label="Normal distribution",
)
plt.title("histtype 2 : barstacked")

# 第三張圖
plt.subplot(233)

plt.hist(
    x,
    bins=num_bins,
    histtype="step",
    facecolor="c",
    edgecolor="r",
    alpha=0.75,
    rwidth=0.8,
    label="Normal distribution",
)
plt.title("histtype 3 : step + 多筆資料")

mu, sigma = 80, 10
x2 = np.random.normal(mu, sigma, size=N * 10)  # 隨機數
mu, sigma = 120, 10
x3 = np.random.normal(mu, sigma, size=N * 10)  # 隨機數

plt.hist(
    x2,
    bins=num_bins,
    histtype="step",
    facecolor="m",
    edgecolor="g",
    alpha=0.75,
    rwidth=0.8,
    label="Normal distribution",
)

plt.hist(
    x3,
    bins=num_bins,
    histtype="step",
    facecolor="y",
    edgecolor="b",
    alpha=0.75,
    rwidth=0.8,
    label="Normal distribution",
)

# 合寫, 但效果不對
# plt.hist([x2, x3], bins=num_bins, histtype="step", facecolor="y", edgecolor="b", alpha=0.75, rwidth=0.8, label="Normal distribution")


# 第四張圖
plt.subplot(234)
# 縱軸不做正規化處理為數量，直條的間距填滿
plt.hist(
    x,
    bins=num_bins,
    histtype="stepfilled",
    facecolor="c",
    edgecolor="m",
    alpha=0.75,
    rwidth=0.8,
    label="Normal distribution",
)
plt.title("histtype 4 : stepfilled")

# 第五張圖
plt.subplot(235)

kwargs = dict(
    histtype="stepfilled", alpha=0.3, bins=num_bins // 2, rwidth=0.8
)
plt.hist(x, **kwargs)
plt.title("以字典傳送參數")


# 第六張圖
plt.subplot(236)

# 縱軸執行正規化處理表示為機率
# 指定bins
bins = [50, 70, 85, 95, 100, 105, 115, 130, 150]

# bins = range(0, 151, 10) #設定bin的範圍
plt.hist(x, bins, rwidth=0.8)

plt.title("unequal bins")

plt.show()

print("------------------------------------------------------------")  # 60個
#          編號               圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(
    num="hist 集合 2",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 資料個數
N = 10000

# 第一張圖
plt.subplot(231)

sides = 6  # 骰子有幾面
dice = []  # 建立擲骰子的串列

# 產生擲骰子的串列
for i in range(N):
    ranNum = random.randint(1, sides)  # 產生1-6隨機數
    dice.append(ranNum)

# 建立 N 個 1-6(含) 的整數隨機數 same
# dice = np.random.randint(1, sides + 1, size=N)  # 建立隨機數

plt.hist(dice, bins=6, rwidth=0.5, cumulative=False, alpha=0.3)  # 繪製hist圖
plt.ylabel("次數")
plt.title("測試 10000 次 不累積統計")

# 第二張圖
plt.subplot(232)

print("資料同上, 改了 累積統計")

#plt.hist(dice, bins=6, rwidth=0.5, cumulative=True, alpha=0.3)  # 繪製hist圖
plt.hist(dice, bins=6, rwidth=0.5, cumulative=True, alpha=0.3)  # 繪製hist圖

plt.ylabel("次數")
plt.title("測試 10000 次, 累積統計")

# 第三張圖
plt.subplot(233)

d1 = np.random.randint(1, 6 + 1, N)  # 不含尾
d2 = np.random.randint(1, 6 + 1, N)

dsums = d1 + d2

plt.hist(dsums, bins=11, rwidth=0.5)

plt.xlabel("兩個骰子和")
plt.ylabel("次數")
plt.title("擲兩個骰子 10000 次 看其分布")

# 第四張圖
plt.subplot(234)

x = np.random.rand(N, 3)  # 產生共3組，每組 N 個隨機數
plt.hist(x, bins=num_bins // 10)
plt.title("產生共3組，每組 10000 個隨機數")

# 第五張圖
plt.subplot(235)

# 生成 N 組介於 0 與 1 之間均勻分配隨機變數
x = np.random.uniform(size=N)
# x = np.random.uniform(0.0, 5.0, size=N)     # 隨機數 #另外範圍
plt.hist(x, bins=num_bins, rwidth=0.8)
plt.title("np.random.uniform")

# 第六張圖
plt.subplot(236)

x = np.random.exponential(scale=2, size=N)
plt.hist(x, bins=num_bins, label="Exponential distribution")
plt.title("np.random.exponential")

plt.show()

print("------------------------------------------------------------")  # 60個
#          編號               圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(
    num="hist 集合 3",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 第一張圖
plt.subplot(231)

N = 10000  # 資料個數
num_bins = 50  # 直方圖顯示時的束數

mu = 100  # 平均值
sigma = 15  # 標準差
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(N)  # 隨機數

n, bins, patches = plt.hist(
    x, bins=num_bins, density=True, color="green", rwidth=0.5, alpha=0.5
)

# 繪製曲線圖
x = bins
y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-((bins - mu) ** 2) / (2 * sigma**2))
plt.plot(x, y, "--", color="r", linewidth=2)

plt.ylabel("機率")

# plt.title(r"$\mu=100,\ \sigma=15$, 加 理想曲線", fontweight="bold")
plt.title(
    r"$f(x)=\frac{1}{\sigma\sqrt{2\pi}}e^{\frac{-1}{2}(\frac{x-\mu}{\sigma})^{2}}    $",
    fontsize=20,
)

# 第二張圖
plt.subplot(232)

mu, sigma = 100, 15
x = np.linspace(mu - 50, mu + 50, 3000)  # 從N1到N2, 分成N個, 包含頭尾
y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-((x - mu) ** 2) / (2 * sigma**2))
plt.plot(x, y, "--", color="r", linewidth=2)

# 第三張圖
plt.subplot(233)

print("另外用海生畫出來")

import seaborn as sns  # 海生, 自動把圖畫得比較好看

mu = 100  # 平均值
sigma = 15  # 標準差
mu, sigma = 100, 15
x = np.random.normal(mu, sigma, N)  # 隨機數

n, bins, patches = plt.hist(
    x, bins=num_bins, density=True, color="green", rwidth=0.5, alpha=0.5
)  # 直方圖

# 繪製曲線圖
sns.kdeplot(x)


# 第四張圖
plt.subplot(234)


import seaborn as sns  # 海生, 自動把圖畫得比較好看

x = np.random.uniform(size=N)  # 隨機數

n, bins, patches = plt.hist(
    x, bins=num_bins, density=True, color="green", rwidth=0.5, alpha=0.5
)  # 直方圖

# 繪製曲線圖
sns.kdeplot(x)


# 第五張圖
plt.subplot(235)


# 第六張圖
plt.subplot(236)

sc1 = [
    90,
    72,
    45,
    18,
    13,
    81,
    65,
    68,
    73,
    84,
    75,
    79,
    58,
    78,
    96,
    100,
    98,
    64,
    43,
    2,
    63,
    71,
    27,
    35,
    45,
    65,
]

sc2 = [
    90,
    72,
    45,
    18,
    13,
    81,
    65,
    68,
    73,
    84,
    75,
    79,
    58,
    78,
    96,
    100,
    98,
    64,
    43,
    2,
    63,
    71,
    27,
    35,
    45,
    65,
]

# 指定束範圍
# plt.hist([sc1, sc2], 9)
plt.hist(
    [sc1, sc2],
    bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
    edgecolor="r",
    rwidth=0.5,
)

plt.ylabel("學生人數")
plt.xlabel("分數")
plt.title("成績表")


plt.show()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("hist參數大合集")

plt.figure(figsize=(12, 8))

mu = 100  # 平均值
sigma = 15  # 標準差
mu, sigma = 100, 15
x = np.random.normal(mu, sigma, size=N * 10)  # 隨機數

print("x : 需要製作直方圖的一維數組")
print("bins : 直方圖的柱數，即要分的組數，默認為10")
print("histtype : 直方圖類型，『bar』, 『barstacked』, 『step』, 『stepfilled』")
print("histtype : bar 傳統的條形直方圖")
print("histtype : barstacked 堆疊的條形直方圖")
print("histtype : step 未填充的條形直方圖，只有外邊框")
print("histtype : stepfilled 有填充的直方圖")
print("color：顏色串列， color=['r','g','b','c','m'], 若有多組數據 依序顯示顏色")
print("facecolor : 直方圖顏色")
print("edgecolor : 直方圖邊框顏色")
print("alpha : 透明度")
print("rwidth : 柱子的寬度占bins寬的比例 0~1")
print("orientation : 直方圖方向 'vertical'(垂直, 預設), 'horizontal'(水平)")
print("density : 密度, 是否將得到的直方圖向量歸一化")
print("density : 密度, 如果為true，則返回的元組的第一個參數n將為頻率而非默認的頻數")
print("density : False : 頻數, True : 頻率")
print("cumulative : 如果為True，則計算累計頻數；如果normed或density取值為True，則計算累計頻率")
print("align : 此參數是可選參數，它控制如何繪制直方圖。 {‘left’，‘mid’，‘right’}")
print("align : left 柱子的中心位於bins的左邊緣")
print("align : mid 柱子位於bins左右邊緣之間")
print("align : right 柱子的中心位於bins的右邊緣")


"""

#尚未使用過的參數 尚無使用範例
bottom : 數組，標量值或None；每個柱子底部相對於y=0的位置。如果是標量值，則每個柱子相對於y=0向上/向下的偏移量相同。如果是數組，則根據數組元素取值移動對應的柱子；即直方圖上下便宜距離；
bottom : 此參數是每個容器底部基線的位置。
range：元組(tuple)或None；剔除較大和較小的離群值，給出全局範圍；如果為None，則默認為(x.min(), x.max())；即x軸的範圍；
range:此參數是可選參數，它是箱子的上下限。
weights : 與x形狀相同的權重數組；將x中的每個元素乘以對應權重值再計數；如果normed或density取值為True，則會對權重進行歸一化處理。這個參數可用於繪制已合并的數據的直方圖；
weights : 此參數是可選參數，并且是一個權重數組，與x的形狀相同。
log:此參數是可選參數，用於將直方圖軸設置為對數刻度
log：布爾值。如果取值為True，則坐標軸的刻度為對數刻度；
如果log為True且x是一維數組，則計數為0的取值將被剔除，
僅返回非空的(frequency, bins, patches）；
stacked：布爾值。如果取值為True，則輸出的圖為多個數據集堆疊累計的結果；
如果取值為False且histtype=‘bar’或’step’，則多個數據集的柱子并排排列；

返回值（用參數接收返回值，便於設置數據標簽）：
n：直方圖向量，即每個分組下的統計值，是否歸一化由參數normed設定。
當normed取默認值時，n即為直方圖各組內元素的數量（各組頻數）；
bins: 返回各個bin的區間範圍；
patches：返回每個bin里面包含的數據，是一個list。

"""

n, bins, patches = plt.hist(
    x,
    bins=10,
    #bins = 'auto'
    #bins = range(10, 101, 10),  # 設定bin的範圍
    histtype="bar",
    align='right',
    # color=['red','green','blue','cyan','magenta'], 若有多組數據 依序顯示顏色
    facecolor="red",
    edgecolor="green",
    alpha=0.75,
    rwidth=0.9,
    orientation="vertical",
    cumulative=False,
    density=False,
    label="常態分佈",   #以便在圖例中顯示
)

print("標示高度")
for i in range(len(n)):
    print("x = ", bins[i] + 10, ", y = ", n[i], ", text =", int(n[i]))
    plt.text(bins[i] + 10, n[i], int(n[i]), ha="center", va="bottom", fontsize=12)

print("返回值")
print("每一柱的高度(y軸) : ", n)
print("每一柱的起訖(x軸) : ", bins)
print(patches)
for p in patches:
    print(type(p))
    print(p)

total_n = sum(n)
print("總樣本數 : ", total_n)

print("總柱數 : ", len(n))

xx = []
for i in range(len(bins) - 1):
    xx.append((bins[i] + bins[i + 1]) / 2)

yy = n
plt.plot(xx, yy, "--", color="r", linewidth=2)

plt.title("hist參數大合集")
plt.xlabel("")
plt.ylabel("個數統計")

plt.show()


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


"""

二維頻次直方圖

就像將一維數組分為區間創建一維頻次直方圖一樣，我們也可以將二維數組按照二維區 間進行切分，來創建二維頻次直方圖。

1.plt.hist2d:二維頻次直方圖
繪製二維頻次直方圖最簡單的方法，就是使用Matplotlib的plt.hist2d函數。

# NG
plt.hist2d(x, y, bins=30, cmap='Blues')
cb = plt.colorbar()
cb.set_label('counts in bin')

plt.show()

2.plt.hexbin:六邊形區間劃分

二維頻次直方圖是由與坐標軸正交的方塊分割而成的，
還有一種常用的方式是用正六邊形分割。
Matplotlib 提供了 plt.hexbin 滿足此類需求，將二維數據集分割成蜂窩狀。

# NG
plt.hexbin(x, y, gridsize=30, cmap='Blues')
cb = plt.colorbar(label='xxxxx')
plt.show()

"""

