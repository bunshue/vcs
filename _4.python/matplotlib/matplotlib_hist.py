"""

np.random.normal
np.random.randn
np.random.rand(
np.random.uniform(size=N)
random.randint

Python Matplotlib.pyplot.hist()用法及代碼示例

Matplotlib是Python中的一個庫，它是數字的-NumPy庫的數學擴展。
Pyplot是Matplotlib模塊的基于狀態的接口，該模塊提供了MATLAB-like接口。
matplotlib.pyplot.hist()函數

matplotlib庫的pyplot模塊中的hist()函數用于繪制直方圖。

用法： matplotlib.pyplot.hist(x, bins=None, range=None, density=False, weights=None, cumulative=False, bottom=None, histtype=’bar’, align=’mid’, orientation=’vertical’, rwidth=None, log=False, color=None, label=None, stacked=False, \*, data=None, \*\*kwargs)

參數：此方法接受以下描述的參數：

    x:此參數是數據序列。
    bins:此參數是可選參數，它包含整數，序列或字符串。
    range:此參數是可選參數，它是箱子的上下限。
    density:此參數是可選參數，它包含布爾值。
    weights:此參數是可選參數，并且是一個權重數組，與x的形狀相同。
    bottom:此參數是每個容器底部基線的位置。
    histtype:此參數是可選參數，用于繪制直方圖的類型。 {‘bar’，‘barstacked’，‘step’，‘stepfilled’}
    align:此參數是可選參數，它控制如何繪制直方圖。 {‘left’，‘mid’，‘right’}
    rwidth:此參數是可選參數，它是條形圖的相對寬度，是箱寬度的一部分
    log:此參數是可選參數，用于將直方圖軸設置為對數刻度
    color:此參數是一個可選參數，它是一個顏色規格或一系列顏色規格，每個數據集一個。
    label:此參數是可選參數，它是一個字符串或匹配多個數據集的字符串序列。

返回值：這將返回以下內容：

    n:這將返回直方圖箱的值。
    垃圾桶：這將返回箱子的邊。
    補丁：這將返回用于創建直方圖的單個補丁的列表。

"""

"""
Matplotlib（直方图） - hist()参数解释

plt.hist(x, bins=None, range=None, density=None, weights=None, cumulative=False, bottom=None, histtype='bar', align='mid', orientation='vertical', rwidth=None, log=False, color=None, label=None, stacked=False, normed=None, *, data=None, **kwargs)

x: 作直方图所要用的数据，必须是一维数组；多维数组可以先进行扁平化再作图；必选参数；
bins: 直方图的柱数，即要分的组数，默认为10；
range：元组(tuple)或None；剔除较大和较小的离群值，给出全局范围；如果为None，则默认为(x.min(), x.max())；即x轴的范围；
density：布尔值。如果为true，则返回的元组的第一个参数n将为频率而非默认的频数；
weights：与x形状相同的权重数组；将x中的每个元素乘以对应权重值再计数；如果normed或density取值为True，则会对权重进行归一化处理。这个参数可用于绘制已合并的数据的直方图；
cumulative：布尔值；如果为True，则计算累计频数；如果normed或density取值为True，则计算累计频率；
bottom：数组，标量值或None；每个柱子底部相对于y=0的位置。如果是标量值，则每个柱子相对于y=0向上/向下的偏移量相同。如果是数组，则根据数组元素取值移动对应的柱子；即直方图上下便宜距离；
align：{‘left’, ‘mid’, ‘right’}；‘left’：柱子的中心位于bins的左边缘；‘mid’：柱子位于bins左右边缘之间；‘right’：柱子的中心位于bins的右边缘；
histtype：{‘bar’, ‘barstacked’, ‘step’, ‘stepfilled’}；'bar’是传统的条形直方图；'barstacked’是堆叠的条形直方图；'step’是未填充的条形直方图，只有外边框；‘stepfilled’是有填充的直方图；当histtype取值为’step’或’stepfilled’，rwidth设置失效，即不能指定柱子之间的间隔，默认连接在一起；
stacked：布尔值。如果取值为True，则输出的图为多个数据集堆叠累计的结果；如果取值为False且histtype=‘bar’或’step’，则多个数据集的柱子并排排列；
orientation：{‘horizontal’, ‘vertical’}：如果取值为horizontal，则条形图将以y轴为基线，水平排列；简单理解为类似bar()转换成barh()，旋转90°；
rwidth：标量值或None。柱子的宽度占bins宽的比例；
log：布尔值。如果取值为True，则坐标轴的刻度为对数刻度；如果log为True且x是一维数组，则计数为0的取值将被剔除，仅返回非空的(frequency, bins, patches）；
color：具体颜色，数组（元素为颜色）或None。
label：字符串（序列）或None；有多个数据集时，用label参数做标注区分；
edgecolor: 直方图边框颜色；
alpha: 透明度；

返回值（用参数接收返回值，便于设置数据标签）：
n：直方图向量，即每个分组下的统计值，是否归一化由参数normed设定。当normed取默认值时，n即为直方图各组内元素的数量（各组频数）；
bins: 返回各个bin的区间范围；
patches：返回每个bin里面包含的数据，是一个list。
其他参数与plt.bar()类似。


"""

"""
以上實例中我們生成了三組不同的隨機數據，并使用 hist() 函數繪制了它們的直方圖。通過設置不同的均值和標準差，我們可以生成具有不同分布特征的隨機數據。

我們設置了 bins 參數為 30，這意味著將數據范圍分成 30 個等寬的區間，然后統計每個區間內數據的頻數。
我們設置了 alpha 參數為 0.5，這意味著每個直方圖的顏色透明度為 50%。

我們使用 label 參數設置了每個直方圖的標簽，以便在圖例中顯示。

然后使用 legend() 函數顯示圖例。最后，我們使用 title()、xlabel() 和 ylabel() 函數設置了圖表的標題和坐標軸標簽。
"""
"""
plt.hist()參數設置

arr: 需要計算直方圖的一維數組；
bins: 直方圖的柱數，可選項，默認為10；
density: : 是否將得到的直方圖向量歸一化。默認為0；
color：顏色序列，默認為None；
facecolor: 直方圖顏色；
edgecolor: 直方圖邊框顏色；
alpha: 透明度；
histtype: 直方圖類型，『bar』, 『barstacked』, 『step』, 『stepfilled』；
rwidth

"""

# hist 集合

N = 500  # 資料個數
num_bins = 50  # 直方圖顯示時的束數

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"

import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random

# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 15  # 設定字型大小

print("------------------------------------------------------------")  # 60個
'''
#          編號               圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(
    num="hist 集合 1",
    figsize=(20, 15),
    dpi=84,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 第一張圖
plt.subplot(231)

x = np.random.normal(size=N)
cc = plt.hist(x, bins=num_bins)
print(type(cc))
print(cc)

plt.title("np.random.normal")


# 第二張圖
plt.subplot(232)

# 生成三組隨機數據
data1 = np.random.normal(0, 1, 1000)
data2 = np.random.normal(2, 1, 1000)
data3 = np.random.normal(-2, 1, 1000)

# 繪制直方圖
plt.hist(data1, bins=30, alpha=0.5, label="Data 1")
plt.hist(data2, bins=30, alpha=0.5, label="Data 2")
plt.hist(data3, bins=30, alpha=0.5, label="Data 3")

# 設置圖表屬性
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("np.random.normal, 3組數據")

# 第三張圖
plt.subplot(233)

# 同坐標軸的多個頻次直方圖
x1 = np.random.normal(0, 0.8, 1000)
x2 = np.random.normal(-2, 1, 1000)
x3 = np.random.normal(3, 2, 1000)
kwargs = dict(histtype="stepfilled", alpha=0.3, density=True, bins=40)
plt.hist(x1, **kwargs)
plt.hist(x2, **kwargs)
plt.hist(x3, **kwargs)
plt.title("np.random.normal")


# 第四張圖
plt.subplot(234)

# 生成 N 組標準常態分配（平均值為 0，標準差為 1 的常態分配）隨機變數
x1 = np.random.normal(size=N)
plt.hist(x=x1, bins=num_bins, label="Normal distribution")
plt.title("np.random.normal")


# 第五張圖
plt.subplot(235)

print("以直方圖顯示常態分佈")
print("alpha調整透明度 給多個直方圖畫在一起用")

# 生成 N 組標準常態分配（平均值為 0，標準差為 1 的常態分配）隨機變數

x = np.random.randn(N)  # 常態分佈數字
plt.hist(x, bins=num_bins, color="r", alpha=0.3)

x = np.random.randn(N)  # 常態分佈數字
plt.hist(x, bins=num_bins, color="g", alpha=0.3)

x = np.random.randn(N)  # 常態分佈數字
plt.hist(x, bins=num_bins, color="b", alpha=0.3)

plt.title("np.random.randn")


# 第六張圖
plt.subplot(236)

x = np.random.randn(N, 3)

colors = ["red", "green", "blue"]

plt.hist(x, num_bins, density=True, histtype="bar", color=colors, label=colors)
plt.legend(prop={"size": 10})
plt.title("一次顯示三組數據", fontweight="bold")

plt.show()

print("------------------------------------------------------------")  # 60個

#          編號               圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(
    num="hist 集合 2",
    figsize=(20, 15),
    dpi=84,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 第一張圖
plt.subplot(231)

N = 10000  # 擲骰子次數
sides = 6  # 骰子有幾面
dice = []  # 建立擲骰子的串列

# 產生擲骰子的串列
for i in range(N):
    ranNum = random.randint(1, sides)  # 產生1-6隨機數
    dice.append(ranNum)

h = plt.hist(dice, bins=6, rwidth=0.5)  # 繪製hist圖

print("bins的y軸 ", h[0])
print("bins的x軸 ", h[1])
plt.ylabel("次數")
plt.title("測試 10000 次")


# 第二張圖
plt.subplot(232)

print("比上面多了 累積統計")

N = 10000  # 擲骰子次數
sides = 6  # 骰子有幾面
dice = []  # 建立擲骰子的串列

# 產生擲骰子的串列
for i in range(N):
    ranNum = random.randint(1, sides)  # 產生1-6隨機數
    dice.append(ranNum)

h = plt.hist(dice, bins=6, rwidth=0.5, cumulative=True)  # 繪製hist圖

print("bins的y軸 ", h[0])
print("bins的x軸 ", h[1])
plt.ylabel("次數")
plt.title("測試 10000 次, 累積統計")


# 第三張圖
plt.subplot(233)

N = 500  # 資料個數
N = 1000  # 資料個數

d1 = np.random.randint(1, 6 + 1, N)  # 不含尾
d2 = np.random.randint(1, 6 + 1, N)

dsums = d1 + d2

# count, bins, ignored = plt.hist(dsums, bins=11, rwidth=0.5, density=True)   #以密度表示
count, bins, ignored = plt.hist(dsums, bins=11, rwidth=0.5)  # 以總數表示

plt.xlabel("兩個骰子和")
# plt.ylabel("密度")   #density = True
plt.ylabel("次數")
plt.title("擲兩個骰子多次 看其分布")


# 第四張圖
plt.subplot(234)

x = np.random.rand(N, 3)  # 產生共3組，每組 N 個隨機數
plt.hist(x, bins=num_bins // 10)
plt.title("產生共3組，每組 N 個隨機數")

# 第五張圖
plt.subplot(235)

sides = 6
# 建立 N 個 1-6(含) 的整數隨機數
dice = np.random.randint(1, sides + 1, size=N)  # 建立隨機數

h = plt.hist(dice, sides, rwidth=0.5)  # 繪製hist圖
print("bins的y軸 ", h[0])
print("bins的x軸 ", h[1])
plt.ylabel("Frequency")
plt.title("Test N times")

# 第六張圖
plt.subplot(236)

# 生成 N 組介於 0 與 1 之間均勻分配隨機變數
x = np.random.uniform(size=N)
# x = np.random.uniform(0.0, 5.0, size=N)     # 隨機數 #另外範圍
plt.hist(x, bins=num_bins, rwidth=0.8)
plt.title("np.random.uniform")

plt.show()

print("------------------------------------------------------------")  # 60個

#          編號               圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(
    num="hist 集合 3",
    figsize=(20, 15),
    dpi=84,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 第一張圖
plt.subplot(231)

grade = [
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

n, b, p = plt.hist(grade, bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], rwidth=0.5)

for i in range(len(n)):
    plt.text(b[i] + 10, n[i], int(n[i]), ha="center", va="bottom", fontsize=12)

plt.title("全班成績直方圖分布圖")
plt.xlabel("考試分數")
plt.ylabel("人數統計")

# 第二張圖
plt.subplot(232)

score = [
    800,
    750,
    450,
    680,
    802,
    630,
    710,
    450,
    250,
    320,
    610,
    670,
    815,
    870,
    900,
    650,
    450,
    730,
    840,
    675,
    795,
    585,
    870,
    960,
    190,
]

plt.hist(score, bins=[10, 255, 405, 605, 785, 905, 990], rwidth=0.5)
plt.title("多益成績分布直方圖")
plt.xlabel("成績")
plt.ylabel("人數")

# 第三張圖
plt.subplot(233)

score = [
    800,
    750,
    450,
    680,
    802,
    630,
    710,
    450,
    250,
    320,
    610,
    670,
    815,
    870,
    900,
    650,
    450,
    730,
    840,
    675,
    795,
    585,
    870,
    960,
    190,
]
n, b, p = plt.hist(score, bins=[10, 255, 405, 605, 785, 905, 990], rwidth=0.5)

for i in range(len(n)):
    plt.text(b[i] + 10, n[i], int(n[i]), ha="center", va="bottom", fontsize=10)
plt.title("多益成績分布直方圖")
plt.xlabel("成績")
plt.ylabel("人數")


# 第四張圖
plt.subplot(234)

grade = [
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

plt.hist(grade, bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], rwidth=0.5)
plt.title("全班成績直方圖分布圖")
plt.xlabel("考試分數")
plt.ylabel("人數統計")


# 第五張圖
plt.subplot(235)

grade = [
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

plt.hist(
    grade, bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], edgecolor="b", rwidth=0.5
)
plt.title("全班成績直方圖分布圖")
plt.xlabel("考試分數")
plt.ylabel("人數統計")


# 第六張圖
plt.subplot(236)

grade = [
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

n, b, p = plt.hist(
    grade, bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], edgecolor="r", rwidth=0.5
)

for i in range(len(n)):
    plt.text(b[i] + 10, n[i], int(n[i]), ha="center", va="bottom", fontsize=12)

plt.title("全班成績直方圖分布圖")
plt.xlabel("考試分數")
plt.ylabel("人數統計")


plt.show()

print("------------------------------------------------------------")  # 60個

#          編號               圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(
    num="hist 集合 4",
    figsize=(20, 15),
    dpi=84,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 第一張圖
plt.subplot(231)

import statistics

sc = [
    60,
    10,
    40,
    80,
    80,
    30,
    80,
    60,
    70,
    90,
    50,
    50,
    50,
    70,
    60,
    80,
    80,
    50,
    60,
    70,
    70,
    40,
    30,
    70,
    60,
    80,
    20,
    80,
    70,
    50,
    90,
    80,
    40,
    40,
    70,
    60,
    80,
    30,
    20,
    70,
]
print(f"平均成績 = {np.mean(sc)}")
print(f"中位成績 = {np.median(sc)}")
print(f"眾數成績 = {statistics.mode(sc)}")

plt.hist(sc, 9, rwidth=0.5)

plt.ylabel("學生人數")
plt.xlabel("分數")
plt.title("成績表")


# 第二張圖
plt.subplot(232)

import statistics

sc1 = [
    60,
    10,
    40,
    80,
    80,
    30,
    80,
    60,
    70,
    90,
    50,
    50,
    50,
    70,
    60,
    80,
    80,
    50,
    60,
    70,
    70,
    40,
    30,
    70,
    60,
    80,
    20,
    80,
    70,
    50,
    90,
    80,
    40,
    40,
    70,
    60,
    80,
    30,
    20,
    70,
]

sc2 = [
    50,
    10,
    60,
    80,
    70,
    30,
    80,
    60,
    30,
    90,
    50,
    50,
    90,
    70,
    60,
    50,
    80,
    50,
    60,
    70,
    60,
    50,
    30,
    70,
    70,
    80,
    10,
    80,
    70,
    50,
    90,
    80,
    40,
    50,
    70,
    60,
    80,
    40,
    20,
    70,
]

plt.hist([sc1, sc2], 9)

plt.ylabel("學生人數")
plt.xlabel("分數")
plt.title("成績表")

# 第三張圖
plt.subplot(233)

x = [21, 42, 23, 4, 5, 26, 77, 88, 9, 10, 31, 32, 33, 34, 35, 36, 37, 18, 49, 50, 100]
num_bins = 10
n, bins, patches = plt.hist(x, num_bins, rwidth=0.5)

print("ccccc")
print(str(n) + "\n" + str(bins))


# 第四張圖
plt.subplot(234)


# 第五張圖
plt.subplot(235)


# 第六張圖
plt.subplot(236)

N = 50000
exp_samples = np.random.exponential(scale=2, size=N)
plt.hist(x=exp_samples, bins=1000, label="Exponential distribution")


plt.show()


print("------------------------------------------------------------")  # 60個

#          編號               圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(
    num="hist 集合 5",
    figsize=(20, 15),
    dpi=84,
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
# x = np.random.normal(mu, sigma, N)                  # 隨機數   另外做法

count, bins, ignored = plt.hist(
    x, bins=num_bins, density=True, color="green", rwidth=0.5, alpha=0.5
)  # 直方圖

# print('bins = ', bins)
# print('len bins = ', len(bins))

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

count, bins, ignored = plt.hist(
    x, bins=num_bins, density=True, color="green", rwidth=0.5, alpha=0.5
)  # 直方圖

# 繪製曲線圖
sns.kdeplot(x)


# 第四張圖
plt.subplot(234)


import seaborn as sns  # 海生, 自動把圖畫得比較好看

x = np.random.uniform(size=N)  # 隨機數

count, bins, ignored = plt.hist(
    x, bins=num_bins, density=True, color="green", rwidth=0.5, alpha=0.5
)  # 直方圖

# 繪製曲線圖
sns.kdeplot(x)


# 第五張圖
plt.subplot(235)


# 第六張圖
plt.subplot(236)

N = 500  # 資料個數
num_bins = 50  # 直方圖顯示時的束數

x = np.random.randn(N)
plt.hist(x, num_bins, rwidth=0.5)


plt.show()
'''

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


"""  新進資料

plt.hist 參數

facecolor="yellow"
edgecolor="red"

facecolor: 直方圖顏色；   = color
edgecolor: 直方圖邊框顏色；

# 亂數種子
np.random.seed(1234567)
np.random.seed(0)
np.random.seed(10**7)


plt.hist(
    density=True,
    histtype="stepfilled",
    color="steelblue",
    edgecolor="none",
    rwidth=0.5,
)



#plt.hist(x, bins = 'auto')
#plt.hist(x, bins = 'auto', density = True)   #y軸改成密度

#plt.hist(x, bins=range(-5, 5, 1), alpha=0.5)  #設定bin的範圍




#plt.style.use("seaborn-white")

plt.text(60, 0.025, r"$\mu=100,\ \sigma=15$")





----------------------


print("描繪頻率分布圖")

print('用pandas讀取csv檔, 之後用plt.hist畫出來')
# 讀入csv檔
filename = "_data/python_ReadWrite_CSV7_onigiri.csv"
dat = pd.read_csv(filename, encoding="UTF-8")

print(type(dat))
print(dat)

# 頻率分布圖
plt.hist(dat["店長"], bins=range(0, 200, 10), alpha=0.5)
plt.hist(dat["太郎"], bins=range(0, 200, 10), alpha=0.5)

bins=range(0, 200, 10)
for b in bins:
    print(b)

print("計算平均數、變異數、標準差")

print("店長---------")
print("平均:", np.mean(dat["店長"]))
print("變異數:", np.var(dat["店長"]))
print("標準差:", np.std(dat["店長"]))

print("太郎---------")
print("平均:", np.mean(dat["太郎"]))
print("變異數:", np.var(dat["太郎"]))
print("標準差:", np.std(dat["太郎"]))


--------------------------------


score = [
    800,
    750,
    450,
    680,
    802,
    630,
    710,
    450,
    250,
    320,
    610,
    670,
    815,
    870,
    900,
    650,
    450,
    730,
    840,
    675,
    795,
    585,
    870,
    960,
    190,
]
n, b, p = plt.hist(score, bins=[10, 255, 405, 605, 785, 905, 990], rwidth=0.5)

for i in range(len(n)):
    plt.text(b[i] + 10, n[i], int(n[i]), ha="center", va="bottom", fontsize=10)

plt.title("多益成績分布直方圖")
plt.xlabel("成績")
plt.ylabel("人數")

"""


"""
二維頻次直方圖

就像將一維數組分為區間創建一維頻次直方圖一樣，我們也可以將二維數組按照二維區 間進行切分，來創建二維頻次直方圖。

1.plt.hist2d:二維頻次直方圖

繪製二維頻次直方圖最簡單的方法，就是使用Matplotlib的plt.hist2d函數。
"""

"""NG
plt.hist2d(x, y, bins=30, cmap='Blues')
cb = plt.colorbar()
cb.set_label('counts in bin')

plt.show()
"""

"""
2.plt.hexbin:六邊形區間劃分

二維頻次直方圖是由與坐標軸正交的方塊分割而成的，還有一種常用的方式是用正六邊形分割。Matplotlib 提供了 plt.hexbin 滿足此類需求，將二維數據集分割成蜂窩狀。
"""

"""NG
plt.hexbin(x, y, gridsize=30, cmap='Blues')
cb = plt.colorbar(label='count in bin')
plt.show()

"""


"""
for i in range(len(n)):
    print("x = ", b[i]+10, ", y = ",n[i], ", text =", int(n[i]))
    plt.text(b[i]+10, n[i], int(n[i]), ha='center', va='bottom', fontsize=10)


"""

plt.figure(
    num="hist 集合 1",
    figsize=(15, 6),
    dpi=84,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

N = 10000  # 資料個數
num_bins = 50  # 直方圖顯示時的束數

# 平均 200，標準差為 25 的分佈
mu = 200
sigma = 25
x = np.random.normal(mu, sigma, size=N)

# 第一張圖
plt.subplot(121)

#縱軸不做正規化處理為數量，直條的間距填滿
plt.hist(x, bins=num_bins, histtype="stepfilled", facecolor="g", alpha=0.75)
plt.title("stepfilled\n" + r"$\mu = 200, \sigma=25$")


# 第二張圖
plt.subplot(122)

#縱軸執行正規化處理表示為機率，直條的寬度大小為 80%
bins = [100, 150, 180, 195, 205, 220, 250, 300]
plt.hist(x, bins, histtype="bar", rwidth=0.8)
plt.title("unequal bins\n" + r"$\mu = 200, \sigma=25$")


plt.show()
