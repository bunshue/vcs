"""
無 scikit-learn(sklearn)的


correlation

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


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個

# 統率, 武力, 智力, 政治, 魅力
main_features = [87, 86, 82, 78, 100]  # 劉備 特徵值
people_names = [  # 比較人物人名
    "諸葛亮",
    "關羽",
    "張飛",
    "趙雲",
    "曹操",
    "司馬懿",
    "孫權",
    "周瑜",
    "呂布",
]

people_features = [  # 比較人物特徵值
    [99, 42, 100, 100, 92],
    [92, 100, 74, 51, 83],
    [86, 99, 78, 36, 57],
    [79, 94, 77, 82, 91],
    [100, 85, 93, 96, 95],
    [95, 62, 98, 95, 84],
    [72, 84, 76, 85, 93],
    [93, 71, 94, 81, 92],
    [84, 98, 61, 12, 55],
]

dist = []  # 儲存人物相似度值
for feature in people_features:
    distances = 0
    for i in range(len(feature)):
        distances += (main_features[i] - feature[i]) ** 2
    dist.append(math.sqrt(distances))

min_ = min(dist)  # 求最小值
min_index = dist.index(min_)  # 最小值的索引

print(f"與 劉備 最相似的人物 : {people_names[min_index]}")
print(f"相似度值 : {dist[min_index]}")
for i in range(len(dist)):
    print(f"人物 : {people_names[i]}, 相似度 : {dist[i]:6.2f}")

print("------------------------------------------------------------")  # 60個

# numpy cumsum()函數簡介
# 函數作用：求數組的所有元素的累計和，可通過參數axis指定求某個軸向的統計值。

a = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]])

print(a)

print("累計和")
cc = a.cumsum()
print(cc)
# array([ 1,  3,  6, 10, 15, 21], dtype=int32)

print("累計和, axis=0")
cc = np.cumsum(a, axis=0)
print(cc)

print("累計和, axis=1")
cc = np.cumsum(a, axis=1)
print(cc)

# 隨機漫步算法

n_person = 2000
n_times = 500

t = np.arange(n_times)
steps = 2 * np.random.randint(2, size=(n_person, n_times)) - 1

amount = np.cumsum(steps, axis=1)
sd_amount = amount**2
mean_sd_amount = sd_amount.mean(axis=0)

plt.figure(figsize=(8, 6))

plt.xlabel(r"$t$")
plt.ylabel(r"$\sqrt{\langle (\delta x)^2 \rangle}$")

plt.plot(t, np.sqrt(mean_sd_amount), "g.")
plt.plot(t, np.sqrt(t), "r-")

plt.title("隨機漫步算法")

show()

print("------------------------------------------------------------")  # 60個

# 多項式擬合

N = 10
n_order = 3  # 3階

x = np.linspace(0, 1, N)
y = x + 0.4 * (np.random.rand(N) - 0.5)
p = np.poly1d(np.polyfit(x, y, n_order))
print(p.coeffs)

t = np.linspace(0, 1, 100)

plt.plot(x, x, "r-", label="理論")
plt.plot(x, y, "go", label="實驗")
plt.plot(t, p(t), "b-", label="擬合")
plt.legend()

plt.title("多項式擬合, " + str(n_order) + " 階")

show()

print("------------------------------------------------------------")  # 60個

N = 20

x = np.linspace(0, 1, N)  # [0, 1] 之間創建 20 個點
y = x + 0.2 * np.random.rand(N) - 0.1


def plot_polynomial_fit(x, y, n_order):
    p = np.poly1d(np.polyfit(x, y, n_order))

    # 畫出擬合出來的多項式所表達的曲線以及原始的點
    t = np.linspace(0, 1, 200)
    plt.plot(x, x, "r-", label="理論")
    plt.plot(x, y, "go", label="實驗")
    plt.plot(t, p(t), "b-", label="擬合")
    return p


plt.figure(figsize=(18, 6))
titles = ["Under Fitting", "Fitting", "Over Fitting"]
models = [None, None, None]

n_order = 1
plt.subplot(131)
models[0] = plot_polynomial_fit(x, y, n_order)
plt.title(titles[0] + ", " + str(n_order) + " 階")

n_order = 3
plt.subplot(132)
models[1] = plot_polynomial_fit(x, y, n_order)
plt.title(titles[1] + ", " + str(n_order) + " 階")

n_order = 10
plt.subplot(133)
models[2] = plot_polynomial_fit(x, y, n_order)
plt.title(titles[2] + ", " + str(n_order) + " 階")

plt.legend()
show()

print("------------------------------")  # 30個

for m in models:
    print("model coeffs: {0}".format(m.coeffs))

print("------------------------------")  # 30個

# 針對一階多項式的模型，不同的參數擬合出來的直線和訓練樣本對應的位置關系
coeffs_1d = [0.2, 0.6]

plt.figure(figsize=(9, 6))
t = np.linspace(0, 1, 200)

plt.plot(x, y, "ro", t, models[0](t), "-", t, np.poly1d(coeffs_1d)(t), "r-")

plt.annotate(
    r"L1: $y = {1} + {0}x$".format(coeffs_1d[0], coeffs_1d[1]),
    xy=(0.8, np.poly1d(coeffs_1d)(0.8)),
    xycoords="data",
    xytext=(-90, -50),
    textcoords="offset points",
    fontsize=16,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)

plt.annotate(
    r"L2: $y = {1} + {0}x$".format(models[0].coeffs[0], models[0].coeffs[1]),
    xy=(0.3, models[0](0.3)),
    xycoords="data",
    xytext=(-90, -50),
    textcoords="offset points",
    fontsize=16,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)

show()

print("------------------------------------------------------------")  # 60個

# 邏輯回歸模型成本函數


def f_1(x):
    return -np.log(x)


def f_0(x):
    return -np.log(1 - x)


X = np.linspace(0.01, 0.99, 100)
f = [f_1, f_0]
titles = ["y=1: $-log(h_\\theta(x))$", "y=0: $-log(1 - h_\\theta(x))$"]

plt.figure(figsize=(12, 6))

for i in range(len(f)):
    plt.subplot(1, 2, i + 1)
    plt.title(titles[i])
    plt.xlabel("$h_\\theta(x)$")
    plt.ylabel("$Cost(h_\\theta(x), y)$")
    plt.plot(X, f[i](X), "r-")

plt.suptitle("邏輯回歸模型成本函數")

show()

print("------------------------------------------------------------")  # 60個

print("L1/L2 範數")


def L1(x):
    return 1 - np.abs(x)


def L2(x):
    return np.sqrt(1 - np.power(x, 2))


def contour(v, x):
    return 5 - np.sqrt(v - np.power(x + 2, 2))  # 4x1^2 + 9x2^2 = v


def format_spines(title):
    ax = plt.gca()  # gca 代表當前坐標軸，即 'get current axis'
    ax.spines["right"].set_color("none")  # 隱藏坐標軸
    ax.spines["top"].set_color("none")
    ax.xaxis.set_ticks_position("bottom")  # 設置刻度顯示位置
    ax.spines["bottom"].set_position(("data", 0))  # 設置下方坐標軸位置
    ax.yaxis.set_ticks_position("left")
    ax.spines["left"].set_position(("data", 0))  # 設置左側坐標軸位置

    plt.title(title)
    plt.xlim(-4, 4)
    plt.ylim(-4, 4)


plt.figure(figsize=(8.4, 4), dpi=144)

x = np.linspace(-1, 1, 100)
cx = np.linspace(-3, 1, 100)

plt.subplot(1, 2, 1)
format_spines("L1 norm")
plt.plot(x, L1(x), "r-", x, -L1(x), "r-")
plt.plot(
    cx, contour(20, cx), "r--", cx, contour(15, cx), "r--", cx, contour(10, cx), "r--"
)

plt.subplot(1, 2, 2)
format_spines("L2 norm")
plt.plot(x, L2(x), "b-", x, -L2(x), "b-")
plt.plot(
    cx, contour(19, cx), "b--", cx, contour(15, cx), "b--", cx, contour(10, cx), "b--"
)

show()

print("------------------------------------------------------------")  # 60個


def entropy(px):
    return -(px * np.log2(px))


x = np.linspace(0.01, 1, 100)

plt.figure(figsize=(8, 6))
plt.title("$Entropy(x) = - P(x) * log_2(P(x))$")
plt.xlim(0, 1)
plt.ylim(0, 0.6)
plt.xlabel("P(x)")
plt.ylabel("Entropy")
plt.plot(x, entropy(x), "r-")

show()

print("------------------------------------------------------------")  # 60個


def gini_impurity(px):
    return px * (1 - px)


x = np.linspace(0.01, 1, 100)

plt.figure(figsize=(8, 6))
plt.title("$Gini(x) = P(x) (1 - P(x))$")
plt.xlim(0, 1)
plt.ylim(0, 0.6)
plt.xlabel("P(x)")
plt.ylabel("Gini Impurity")
plt.plot(x, entropy(x), "r-")

show()

print("------------------------------------------------------------")  # 60個


def gaussian_kernel(x, mean, sigma):
    return np.exp(-((x - mean) ** 2) / (2 * sigma**2))


x = np.linspace(0, 6, 500)
mean = 1
sigma1 = 0.1
sigma2 = 0.3

plt.figure(figsize=(12, 6))

# sub plot 1
plt.subplot(1, 2, 1)
plt.title("Gaussian for $\sigma={0}$".format(sigma1))

plt.xlim(0, 2)
plt.ylim(0, 1.1)
ax = plt.gca()  # gca 代表當前坐標軸，即 'get current axis'
ax.spines["right"].set_color("none")  # 隱藏坐標軸
ax.spines["top"].set_color("none")

plt.plot(x, gaussian_kernel(x, mean, sigma1), "r-")

# sub plot 2
plt.subplot(1, 2, 2)
plt.title("Gaussian for $\sigma={0}$".format(sigma2))

plt.xlim(0, 2)
plt.ylim(0, 1.1)
ax = plt.gca()  # gca 代表當前坐標軸，即 'get current axis'
ax.spines["right"].set_color("none")  # 隱藏坐標軸
ax.spines["top"].set_color("none")

plt.plot(x, gaussian_kernel(x, mean, sigma2), "r-")

show()

print("------------------------------------------------------------")  # 60個


def normal_distribution(x, mean, sigma):
    return (1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(
        -((x - mean) ** 2) / (2 * sigma**2)
    )


x = np.linspace(0, 6, 500)
mean1 = 1
mean2 = 1
sigma1 = 0.1
sigma2 = 0.3

plt.figure(figsize=(12, 6))

# sub plot 1
plt.subplot(1, 2, 1)
plt.title("Gaussian Distribution for $\mu={0}, \sigma={1}$".format(mean1, sigma1))

plt.xlim(0, 2)
plt.ylim(0, 5)
ax = plt.gca()  # gca 代表當前坐標軸，即 'get current axis'
ax.spines["right"].set_color("none")  # 隱藏坐標軸
ax.spines["top"].set_color("none")

plt.plot(x, normal_distribution(x, mean1, sigma1), "r-")

# sub plot 2
plt.subplot(1, 2, 2)
plt.title("Gaussian Distribution for $\mu={0}, \sigma={1}$".format(mean2, sigma2))

plt.xlim(0, 2)
plt.ylim(0, 5)
ax = plt.gca()  # gca 代表當前坐標軸，即 'get current axis'
ax.spines["right"].set_color("none")  # 隱藏坐標軸
ax.spines["top"].set_color("none")

plt.plot(x, normal_distribution(x, mean2, sigma2), "r-")

show()

print(normal_distribution(6, 5.855, np.sqrt(3.5033e-02)))

print("------------------------------------------------------------")  # 60個

dots = np.array([[1, 1.5], [2, 1.5], [3, 3.6], [4, 3.2], [5, 5.5]])


def cross_point(x0, y0):
    """
    1. line1: y = x
    2. line2: y = -x + b => x = b/2
    3. [x0, y0] is in line2 => b = x0 + y0

    => x1 = b/2 = (x0 + y0) / 2
    => y1 = x1
    """
    x1 = (x0 + y0) / 2
    return x1, x1


plt.figure(figsize=(8, 6))
plt.title("2-dimension to 1-dimension")

plt.xlim(0, 8)
plt.ylim(0, 6)
ax = plt.gca()  # gca 代表當前坐標軸，即 'get current axis'
ax.spines["right"].set_color("none")  # 隱藏坐標軸
ax.spines["top"].set_color("none")

plt.scatter(dots[:, 0], dots[:, 1], marker="s", c="b")

plt.plot([0.5, 6], [0.5, 6], "-r")

for d in dots:
    x1, y1 = cross_point(d[0], d[1])
    plt.plot([d[0], x1], [d[1], y1], "--b")
    plt.scatter(x1, y1, marker="o", c="r")

plt.annotate(
    r"projection point",
    xy=(x1, y1),
    xycoords="data",
    xytext=(x1 + 0.5, y1 - 0.5),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)

plt.annotate(
    r"vector $u^{(1)}$",
    xy=(4.5, 4.5),
    xycoords="data",
    xytext=(5, 4),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)
show()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
hours_phone_used = [0, 0, 0, 1, 1.3, 1.5, 2, 2.2, 2.6, 3.2, 4.1, 4.4, 4.4, 5]
work_performance = [87, 89, 91, 90, 82, 80, 78, 81, 76, 85, 80, 75, 73, 72]

x = np.array(hours_phone_used)
y = np.array(work_performance)
n = len(x)
x_mean = x.mean()
y_mean = y.mean()
print("資料數:", n)
print("x平均:", x_mean)
print("y平均:", y_mean)

diff = (x - x_mean) * (y - y_mean)
print("x偏差*y編差和:", diff.sum())
covar = diff.sum() / n
print("共變異數:", covar)

corr = covar / (x.std() * y.std())
print("相關係數:", corr)

print("------------------------------")  # 30個

df = pd.DataFrame({"手機使用時間(小時)": hours_phone_used, "工作效率": work_performance})

print("用pd算相關係數")
print("相關係數:", df.corr())

df.plot(kind="scatter", x="手機使用時間(小時)", y="工作效率")
plt.title("手機使用時數與工作效率")
show()

sns.heatmap(
    df.corr(), linewidths=0.1, vmax=1.0, square=True, linecolor="white", annot=True
)
show()

print("------------------------------------------------------------")  # 60個
"""
""" data/correlation.csv
     A    B    C    D
0  0.5  0.9  0.4  NaN
1  0.8  0.6  NaN  NaN
2  0.7  0.3  0.8  0.9
3  0.8  0.3  NaN  0.2
4  0.9  NaN  0.7  0.3
5  0.2  0.7  0.6  NaN
"""

df = pd.read_csv("data/correlation.csv")

""" 目前無法造出有NaN的df
datas = [
    [0.5, 0.9, 0.4, "NaN"],
    [0.8, 0.6, "NaN", "NaN"],
    [0.7, 0.3, 0.8, 0.9],
    [0.8, 0.3, "NaN", 0.2],
    [0.9, "NaN", 0.7, 0.3],
    [0.2, 0.7, 0.6, "NaN"],
    ]
columns = ["A", "B", "C", "D"]
df = pd.DataFrame(np.array(datas), columns=columns)
"""
print(df)

df.info()  # 這樣就已經把資料集彙總資訊印出來

# 將df的 相關係數 轉 html
# df.corr().to_html("test_csv_corr2html.html")

sns.heatmap(
    df.corr(), linewidths=0.1, vmax=1.0, square=True, linecolor="white", annot=True
)
# show()

print("------------------------------------------------------------")  # 60個

"""
数据相关性分析中，经常用到data.corr()函数，data.corr()表示了data中的两个变量之间的相关性，取值范围为[-1,1],取值接近-1，表示反相关，类似反比例函数，取值接近1，表正相关。
DataFrame.corr()函数使用说明如下：

DataFrame.corr(method='pearson', min_periods=1)

参数说明：
method：可选值为{‘pearson’, ‘kendall’, ‘spearman’}
pearson：Pearson相关系数来衡量两个数据集合是否在一条线上面，即针对线性数据的相关系数计算，针对非线性                                           数据便会有误差。
kendall：用于反映分类变量相关性的指标，即针对无序序列的相关系数，非正太分布的数据
spearman：非线性的，非正太分析的数据的相关系数
min_periods：样本最少的数据量
返回值：各类型之间的相关系数DataFrame表格。
"""

df = pd.DataFrame(
    [[1, 6, 7, 5, 1], [2, 10, 8, 3, 4], [3, 4, 0, 10, 2]],
    columns=["val1", "val2", "val3", "val4", "val5"],
)
print(df)


# 5个变量的数据如表所示
# 各变量数据相关性的热力图

sns.heatmap(
    df.corr(), linewidths=0.1, vmax=1.0, square=True, linecolor="white", annot=True
)
show()

# 从图中可以看出，val2和val3的相关性最高为0.83，其次是val2和val5。

print("------------------------------------------------------------")  # 60個

"""
pandas相关系数-DataFrame.corr()参数详解

DataFrame.corr(method='pearson', min_periods=1)

参数说明：
method：可选值为{‘pearson’, ‘kendall’, ‘spearman’}
               pearson：Pearson相关系数来衡量两个数据集合是否在一条线上面，即针对线性数据的相关系数计算，针对非线性数据便会有误差。
                kendall：用于反映分类变量相关性的指标，即针对无序序列的相关系数，非正太分布的数据
                spearman：非线性的，非正太分布的数据的相关系数
min_periods：样本最少的数据量

返回值：各类型之间的相关系数DataFrame表格。
"""

x = [a for a in range(11)]


def y1_x(x):
    return x * 2


def y2_x(x):
    return x**2 // 4


def y3_x(x):
    return (x - 5) ** 2


def y4_x(x):
    return 10 - x


y1 = [y1_x(i) for i in x]
y2 = [y2_x(i) for i in x]
y3 = [y3_x(i) for i in x]
y4 = [y4_x(i) for i in x]

print("x :", x)
print("y1 :", y1)
print("y2 :", y2)
print("y3 :", y3)
print("y4 :", y4)

df = pd.DataFrame({"x": x, "y1": y1, "y2": y2, "y3": y3, "y4": y4})
print(df)
print(df.columns)

columns = ["x", "2倍", "平方除4", "(減5)平方", "10-x"]
df.columns = columns

df.plot(kind="line", legend=True, title="線圖", figsize=[10, 5])

cc = df.head()
print(cc)

cc = df.corr()
print(cc)

plt.figure(figsize=(12, 8))
plt.subplot(221)
sns.heatmap(cc, annot=True, cmap="coolwarm")

cc = df.corr(method="spearman")
print(cc)
plt.subplot(222)
sns.heatmap(cc, annot=True, cmap="coolwarm")

cc = df.corr(method="kendall")
print(cc)
plt.subplot(223)
sns.heatmap(cc, annot=True, cmap="coolwarm")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("線性迴歸")


def my_linear_regression_train(xArr, yArr):  # 訓練模型
    m, n = np.shape(xArr)
    xMat = np.mat(np.ones((m, n + 1)))  # 加第一列設爲1，用於計算截距
    x = np.mat(xArr)
    xMat[:, 1 : n + 1] = x[:, 0:n]
    yMat = np.mat(yArr).T
    xTx = xMat.T * xMat
    if np.linalg.det(xTx) == 0.0:  # 行列式的值爲0，無逆矩陣
        print("This matrix is sigular, cannot do inverse")
        return None
    ws = xTx.I * (xMat.T * yMat)
    return ws


def predict(xArr, ws):  # 預測
    m, n = np.shape(xArr)
    xMat = np.mat(np.ones((m, n + 1)))  # 加第一列設爲1, 爲計算截距
    x = np.mat(xArr)
    xMat[:, 1 : n + 1] = x[:, 0:n]
    return xMat * ws


x = [[1], [2], [3], [4]]
y = [4.1, 5.9, 8.1, 10.1]
ws = my_linear_regression_train(x, y)
if isinstance(ws, np.ndarray):
    print(ws)  # 返回結果：[[2.  ] [2.02]]
    print(predict([[5]], ws))  # 返回結果：[[12.1]]
    plt.scatter(x, y, s=20)  # 繪圖
    yHat = predict(x, ws)
    plt.plot(x, yHat, linewidth=2.0)
    show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("邏輯迴歸")


def sigmoid(x):  # S函數實現
    return 1.0 / (1.0 + np.exp(-x))


x = np.arange(-10, 10, 0.2)  # 生成從-10, 10， 間隔爲0.2的數組
y = [sigmoid(i) for i in x]
plt.grid(True)  # 顯示網格
plt.plot(x, y)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("信息量和熵")


def entropy(*c):
    if len(c) <= 0:
        return -1
    result = 0
    for x in c:
        result += (-x) * math.log(x, 2)
    return result


print(entropy(0.99, 0.01))
print(entropy(0.5, 0.5))
print(entropy(0.333, 0.333, 0.333))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("Apriori關聯規則")


def load1():
    return [
        ["香蕉", "蘋果", "梨", "葡萄", "櫻桃", "西瓜", "芒果", "枇杷"],
        ["蘋果", "菠蘿", "梨", "香蕉", "荔枝", "芒果", "橙子"],
        ["菠蘿", "香蕉", "桔子", "橙子"],
        ["菠蘿", "梨", "枇杷"],
        ["蘋果", "香蕉", "梨", "荔枝", "枇杷", "芒果", "香瓜"],
    ]


# 建立所有物品集合
def create_collection_1(data):
    c = []
    for item in data:
        for g in item:
            if not [g] in c:
                c.append([g])
    c.sort()
    return list(map(frozenset, c))


def check_support(d_list, c_list, min_support):
    # d_list是購物數據，c_list是物品集合，support是支持度
    c_dic = {}  # 組合計數
    for d in d_list:  # 每次購物
        for c in c_list:  # 每個組
            if c.issubset(d):
                if c in c_dic:
                    c_dic[c] += 1  # 組合計數加1
                else:
                    c_dic[c] = 1  # 將組合加入字典
    d_count = float(len(d_list))  # 購物次數
    ret = []
    support_dic = {}
    for key in c_dic:
        support = c_dic[key] / d_count
        if support >= min_support:  # 判斷支持度
            ret.append(key)
        support_dic[key] = support  # 記錄支持度
    return ret, support_dic  # 返回滿足支持率的組和支持度字典


def create_collection_n(lk, k):
    ret = []
    for i in range(len(lk)):
        for j in range(i + 1, len(lk)):
            l1 = list(lk[i])[: k - 2]
            l1.sort()
            l2 = list(lk[j])[: k - 2]
            l2.sort()
            if l1 == l2:
                ret.append(lk[i] | lk[j])
    return ret


def apriori(data, min_support=0.5):
    c1 = create_collection_1(data)
    d_list = list(map(set, data))  # 將購物列表轉換成集合列表
    l1, support_dic = check_support(d_list, c1, min_support)
    l = [l1]
    k = 2
    while len(l[k - 2]) > 0:
        ck = create_collection_n(l[k - 2], k)  # 建立新組合
        lk, support = check_support(d_list, ck, min_support)  # 判斷新組是否適合支持率
        support_dic.update(support)
        l.append(lk)  # 將本次結果加入整體
        k += 1
    return l, support_dic


data = load1()
l, support_dic = apriori(data)
print(l)
print()
print(support_dic)

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
