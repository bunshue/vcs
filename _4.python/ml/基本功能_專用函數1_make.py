"""
基本功能_專用函數1

使用 scikit-learn(sklearn) 的 函數

sklearn內建資料集集合

預設方法建立資料集

一些簡易的運算
"""

"""
機器學習筆記：常用數據集之scikit-learn生成分類和聚類數據集
本文介紹分類和聚類數據集的生成，包括以下9個接口函數，其中，
有六個是用于單標簽類數據生成：

(1) make_blobs()
(2) make_classification()
(3) make_gaussian_quantiles()
(4) make_hastie_10_2()
(5) make_circles()
(6) make_moons()

一個用于多標簽類數據生成:
(7) make_multilabel_classification()

還有兩個用于雙聚類數據集生成：
(8) make_biclusters
(9) make_checkerboard
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

import ssl

ssl._create_default_https_context = ssl._create_stdlib_context

print("------------------------------------------------------------")  # 60個

from sklearn.datasets import make_regression  # 迴歸資料集
from sklearn.datasets import make_blobs  # 集群資料集
from sklearn.datasets import make_classification  # 分類資料集
from sklearn.datasets import make_moons  # 非線性的資料集
from sklearn.datasets import make_circles  # 圓形分佈的資料集
from sklearn.datasets import make_gaussian_quantiles
from sklearn.datasets import make_hastie_10_2
from sklearn.datasets import make_multilabel_classification as make_ml_clf
from sklearn.datasets import make_biclusters
from sklearn.datasets import make_checkerboard

print("------------------------------------------------------------")  # 60個

import sklearn
from sklearn import datasets
from sklearn import svm
from sklearn import metrics

print(sklearn.__version__)
# print(dir(datasets))
print(sklearn)


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

plt.figure(num="make_regression", figsize=(16, 9))

print("------------------------------")  # 30個
plt.subplot(231)

plt.title("make_regression 迴歸資料集")

N = 50  # n_samples, 樣本數
M = 1  # n_features, 特徵數(資料的維度)
T = 1  # n_targets, 標籤類別
NOISE = 10  # noise, 分散程度

# X, y = datasets.make_regression(n_samples=N, n_features=M, n_targets=T, noise=NOISE)

print("make_regression,", N, "個樣本, ", M, "個特徵")

X, y, coef = make_regression(
    n_samples=N,
    n_features=M,
    noise=20,
    coef=True,
    random_state=9487
    # n_targets=1, noise=1.5,
)
print(X.shape, y.shape)
print(coef)

plt.scatter(X[:, 0], y)
plt.plot([min(X), max(X)], [min(X) * coef, max(X) * coef], "r")

print("------------------------------")  # 30個
plt.subplot(232)

print("------------------------------")  # 30個
plt.subplot(233)

print("------------------------------")  # 30個
plt.subplot(234)

plt.title("make_classification 分類資料集")

print("分類資料集")

N = 50  # n_samples, 樣本數
M = 1  # n_features, 特徵數(資料的維度)
print("make_classification,", N, "個樣本, ", M, "個特徵")

X, y = make_classification(
    n_samples=N,
    n_classes=3,
    n_features=20,
    n_informative=15,
    n_redundant=5,
    random_state=9487,
)
print(X.shape)

# 繪圖
# 樣本點的形狀
markers = ["x", "o", "^"]

# 針對類別各畫一個散佈圖
for k in range(3):
    X_0 = []
    X_1 = []
    for i in range(len(y)):
        if y[i] == k:
            X_0.append(X[i, 0])
            X_1.append(X[i, 1])
            plt.scatter(X_0, X_1, marker=markers[k], s=50)

print("------------------------------")  # 30個
plt.subplot(235)

print("------------------------------")  # 30個
plt.subplot(236)

print("使用center_box")

N = 1000  # n_samples, 樣本數
M = 2  # n_features, 特徵數(資料的維度)
GROUPS = 6  # centers, 分群數
STD = 0.3  # cluster_std, 資料標準差
print("make_blobs,", N, "個樣本, ", M, "個特徵, 分成", GROUPS, "群")

X, y, centers = make_blobs(
    n_samples=N,
    n_features=M,
    centers=GROUPS,
    cluster_std=STD,
    center_box=(-10.0, 10.0),
    return_centers=True,
)

print(GROUPS, "群 的中心點 :\n", centers)

plt.scatter(*zip(*X))

# 標記群集中心
plt.scatter(centers[:, 0], centers[:, 1], marker="*", s=200, color="r")
# 目前還不會把框畫出來 center_box

plt.suptitle("各種 make_regression")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

plt.figure(num="make_blobs", figsize=(16, 9))

N = 10  # n_samples, 樣本數
M = 4  # n_features, 特徵數(資料的維度)
GROUPS = 3  # centers, 分群數
STD = 1  # cluster_std, 資料標準差
print("make_blobs,", N, "個樣本, ", M, "個特徵, 分成", GROUPS, "群")

X, y, centers = make_blobs(
    n_samples=N, centers=GROUPS, cluster_std=STD, n_features=M, return_centers=True
)

print(GROUPS, "群 的中心點 : ", centers)
print(GROUPS, "個目標")
print("資料的維度")
print("X :\t", X.shape)
print("y :\t", y.shape)
print("資料的內容")
print("X :\n", X)
print("y :\n", y)

print("------------------------------")  # 30個
plt.subplot(231)
N, M, GROUPS, STD = 100, 2, 3, 1
X, y, centers = make_blobs(
    n_samples=N, centers=GROUPS, cluster_std=STD, n_features=M, return_centers=True
)
plt.scatter(X[:, 0], X[:, 1], c=y)
# 標記群集中心
plt.scatter(centers[:, 0], centers[:, 1], marker="*", s=200, color="r")
plt.title("sd=1, 3群")

print("------------------------------")  # 30個
plt.subplot(232)
N, M, GROUPS, STD = 100, 2, 5, 1
X, y, centers = make_blobs(
    n_samples=N, centers=GROUPS, cluster_std=STD, n_features=M, return_centers=True
)
plt.scatter(X[:, 0], X[:, 1], c=y)
# 標記群集中心
plt.scatter(centers[:, 0], centers[:, 1], marker="*", s=200, color="r")
plt.title("sd=1, 5群")

print("------------------------------")  # 30個
plt.subplot(233)
print("每群不同大小, 指定中心位置")

N0, N1, N2, N3 = 50, 150, 250, 400  # 樣本數
cx0, cy0 = 100, 120  # 第0群的中心位置
cx1, cy1 = 250, 300  # 第1群的中心位置
cx2, cy2 = 700, 150  # 第2群的中心位置
cx3, cy3 = 300, 500  # 第3群的中心位置

X, y, centers = make_blobs(
    n_samples=[N0, N1, N2, N3],
    n_features=2,
    centers=[[cx0, cy0], [cx1, cy1], [cx2, cy2], [cx3, cy3]],
    cluster_std=50,
    return_centers=True,
)

plt.scatter(X[:, 0], X[:, 1], c=y)
# 標記群集中心
plt.scatter(centers[:, 0], centers[:, 1], marker="*", s=200, color="r")
plt.title("每群不同大小, 指定中心位置")

print("------------------------------")  # 30個
plt.subplot(234)
N, M, GROUPS = 100, 2, 3
X, y, centers = make_blobs(
    n_samples=N, centers=GROUPS, n_features=M, return_centers=True
)
plt.scatter(X[:, 0], X[:, 1], c=y)
# 標記群集中心
plt.scatter(centers[:, 0], centers[:, 1], marker="*", s=200, color="r")
plt.axis([-15, 15, -15, 15])
plt.title("無 sd")

print("------------------------------")  # 30個
plt.subplot(235)
N, M, GROUPS, STD = 100, 2, 3, 3
X, y, centers = make_blobs(
    n_samples=N, centers=GROUPS, cluster_std=STD, n_features=M, return_centers=True
)
plt.scatter(X[:, 0], X[:, 1], c=y)
# 標記群集中心
plt.scatter(centers[:, 0], centers[:, 1], marker="*", s=200, color="r")
plt.axis([-15, 15, -15, 15])
plt.title("sd=3")

print("------------------------------")  # 30個
plt.subplot(236)
N, M, GROUPS, STD = 100, 2, 3, 6
X, y, centers = make_blobs(
    n_samples=N, centers=GROUPS, cluster_std=STD, n_features=M, return_centers=True
)
plt.scatter(X[:, 0], X[:, 1], c=y)
# 標記群集中心
plt.scatter(centers[:, 0], centers[:, 1], marker="*", s=200, color="r")
plt.axis([-15, 15, -15, 15])
plt.title("sd=6")

plt.suptitle("各種 make_blobs")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

plt.figure(num="make_其他", figsize=(16, 9))

print("------------------------------")  # 30個
plt.subplot(231)

plt.title("make_moons 非線性的資料集")

N = 100  # make_moons 未指定個數, 就是100個
X, y = make_moons(n_samples=N, noise=0.05)
print(X.shape)

# 針對類別各畫一個散佈圖
colors = ["red", "blue"]
for k in range(2):
    X_0 = []
    X_1 = []
    for i in range(len(y)):
        if y[i] == k:
            X_0.append(X[i, 0])
            X_1.append(X[i, 1])
            plt.scatter(X_0, X_1, s=50, c=colors[k])

print("------------------------------")  # 30個
plt.subplot(232)

plt.title("make_circles 圓形分佈的資料集")

X, y = make_circles(n_samples=N, noise=0.05)
print(X.shape)

# 針對類別各畫一個散佈圖
colors = ["red", "blue"]
for k in range(2):
    X_0 = []
    X_1 = []
    for i in range(len(y)):
        if y[i] == k:
            X_0.append(X[i, 0])
            X_1.append(X[i, 1])
            plt.scatter(X_0, X_1, s=50, c=colors[k])

print("------------------------------")  # 30個
plt.subplot(233)

print("------------------------------")  # 30個
plt.subplot(234)

print("------------------------------")  # 30個
plt.subplot(235)

print("------------------------------")  # 30個
plt.subplot(236)

plt.suptitle("各種 make_其他")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


plt.figure(num="make_regression", figsize=(16, 9))

print("------------------------------")  # 30個
plt.subplot(231)

print("------------------------------")  # 30個
plt.subplot(232)

print("------------------------------")  # 30個
plt.subplot(233)

print("------------------------------")  # 30個
plt.subplot(234)

print("------------------------------")  # 30個
plt.subplot(235)

print("------------------------------")  # 30個
plt.subplot(236)

plt.suptitle("各種 make_regression")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" 畫在一起 TBD
plt.figure(
    num="sklearn內建資料集集合",
    figsize=(16, 9),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

print("------------------------------")  # 30個
#plt.subplot(231)
#plt.title("make_classification")
"""

"""
2. make_classification

make_blobs()和make_classification()都用于生成多類別的數據集，
每個類別都是由一個或者多個正態分布簇(normally-distributed cluster)構成。

make_blobs對于各簇的中心和標準偏差提供了更方便的控制選項，
通常用于聚類算法的演示。而make_classification則更加側重于通過各種手段導入各種“噪聲”的影響，
比如說，相關的、冗余的、沒有信息量的特征；每個類分成多個正態分布簇；特征空間的線性變換等等。
"""

# make_classification()生成二分類數據集

N = 500  # n_samples, 樣本數
M = 5  # n_features, 特徵數(資料的維度)
print("make_classification,", N, "個樣本, ", M, "個特徵")

X, y = make_classification(
    n_samples=N,
    n_features=M,
    n_redundant=0,
    n_clusters_per_class=1,
    n_informative=1,
    n_classes=2,
    random_state=9487,
)

# scatter plot, dots colored by class value
df = pd.DataFrame(dict(x=X[:, 0], y=X[:, 1], label=y))
colors = {0: "red", 1: "blue"}
fig, ax = plt.subplots()
grouped = df.groupby("label")
for key, group in grouped:
    group.plot(ax=ax, kind="scatter", x="x", y="y", label=key, color=colors[key])

print(X.shape, y.shape)
plt.title("make_classification")
show()

print("------------------------------")  # 30個
# plt.subplot(234)
# plt.title("make_moons")

""" 
4. make_moons
        make_moons()函數生成一個二分類問題數據集，
        它生成兩個半月形對應兩個分類。可以通過noise參數來控制噪聲量。
        適合于非線性分類算法的演示。
"""

# make_moons: Generate isotropic Gaussian blobs for clustering.
# 經常用于非線性分類示例。

N = 500  # 樣本數
X, y = make_moons(n_samples=N, shuffle=True, noise=0.1, random_state=9487)

# scatter plot, dots colored by class value
df = pd.DataFrame(dict(x=X[:, 0], y=X[:, 1], label=y))
colors = {0: "red", 1: "blue"}
fig, ax = plt.subplots()
grouped = df.groupby("label")
for key, group in grouped:
    group.plot(ax=ax, kind="scatter", x="x", y="y", label=key, color=colors[key])

plt.title("make_moons")
show()

print("------------------------------")  # 30個
# plt.subplot(235)
# plt.title("make_circles")

"""
5. make_circles
顧名思義，每個類別的樣本構成一個圓形。
"""
# make_circles: generates a binary classification problem with datasets that fall into concentric circles.
# Make a large circle containing a smaller circle in 2d.
# A simple toy dataset to visualize clustering and classification algorithms, suitable for algorithms that can learn complex non-linear manifolds.

N = 500  # 樣本數
X, y = make_circles(n_samples=N, noise=0.05)
# 'noise' is used to control the amount of noise in the shapes.

# scatter plot, dots colored by class value
df = pd.DataFrame(dict(x=X[:, 0], y=X[:, 1], label=y))
colors = {0: "red", 1: "blue"}
fig, ax = plt.subplots(figsize=[6, 6])
grouped = df.groupby("label")
for key, group in grouped:
    group.plot(ax=ax, kind="scatter", x="x", y="y", label=key, color=colors[key])

plt.title("make_circles")
show()

print("------------------------------")  # 30個
# plt.subplot(236)
# plt.title("make_gaussian_quantiles")

"""
6. make_gaussian_quantiles
make_gaussian_quantiles()首先生成一個多維正態分布樣本集，
然后，將這樣本集基于分位點(quantiles)分割成多個(n_classes=3 by default)嵌套的多維同心超球，
每個超球屬于一類，并使得大致各類的樣本基本相等。
基于分位點進行分割是什么意思呢？
以一維正態分布為例，大致來說就是這樣分割的。
假設n_classes = 3，因此對應的兩個分割用的分位點就是33%和66%。
取樣本中位于[0, 33%]分位區間的作為第一類，位于[33%, 66%]分位區間的作為第二類，
位于[66%, 100%]分位區間的作為第三類。
對于多維數據，是基于對應的𝜒2分布的分位數來進行分類。
"""

N = 1000  # 樣本數
data, target = make_gaussian_quantiles(n_samples=N, cov=1.0, n_classes=3)

# scatter plot, dots colored by class value
df = pd.DataFrame(dict(x=data[:, 0], y=data[:, 1], label=target))
colors = {0: "red", 1: "blue", 2: "k"}
fig, ax = plt.subplots(figsize=[6, 6])
grouped = df.groupby("label")
for key, group in grouped:
    group.plot(ax=ax, kind="scatter", x="x", y="y", label=key, color=colors[key])

plt.title("make_gaussian_quantiles")
show()

# 以上畫一起 有問題 df plot~~~~~


"""
7. make_hastie_10_2
這個函數是專門用于以下Hastie的機器學習經典教材中例10.2所提及的數據集的生成，用于二分類問題。為一本書中的一個例子專門列了一個函數，確實是很拼。可以看作是make_gaussian_quantiles的一種特例，或者反過來說make_gaussian_quantiles是make_hastie_10_2的推廣。
T. Hastie, R. Tibshirani and J. Friedman, “Elements of Statistical Learning Ed. 2”, Springer, 2009.》
該數據集有10個特征，是i.i.d（獨立同分布）的標準正態分布，target y定義如下：
y[i] = 1 if np.sum(X[i] ** 2) > 9.34 else -1
"""

N = 1000  # 樣本數
data, target = make_hastie_10_2(n_samples=N, random_state=9487)

# target[target==-1] = 0  # 原數據集生成的target為[1,-1],這里變換為[1,0]
# target = target.astype('int32') # 變換成整數

df = pd.DataFrame(data)
df["target"] = target

print(df)

"""
這是一個10維的數據，所以不容易以散點圖的形式進行圖示化。以下通過圖示的方式看看各個維度是不是獨立同分布（i.i.d）的標準高斯分布。
"""
from scipy.stats import norm

plt.figure(figsize=(20, 6))
for k in range(10):
    df[k].plot(kind="kde", secondary_y=True, label="feature#" + str(k))

x = np.linspace(-8, 8, 1000)
plt.plot(x, norm.pdf(x), "r-", lw=2, alpha=0.6, label="theoretic std norm pdf")

plt.title("make_hastie_10_2")
plt.legend()
show()

# 如上圖可知，10個特征分量確實基本上都是與標準正態分布吻合的。

"""
8. 多標簽數據集生成
多標簽數據集用于當存在多各類別，而待分類的數據可能屬于其中的一類或者同時屬于多個類別，或者甚至不屬于任何類別。比如說，當需要識別在一張圖像中所包含的交通信號等的類型。一張圖片可能不包含信號燈，也可能只包含一個紅燈或綠燈或黃燈，也可能同時包含一個紅燈和綠燈（如果這張圖片覆蓋了一個十字路口的兩個方向的信號燈的話）。
"""
x, y = make_ml_clf(n_samples=1000, n_features=10, n_classes=3, random_state=9487)
print(x.shape, y.shape)
print(y[:10, :])

"""
可以看出，由于是多分類（本例是3分類）多標簽的，
所以target(label)采用了one-hot編碼的形式，
每個數據樣本的label中可能有一個或多個1，表示屬于1個類別或者多個類別。
當然，雖然以上沒有顯示出來，也存在不屬于任何類別的樣本，即其label為全零向量。
"""

"""
9. make_biclusters
make_biclusters用于生成具有恒定塊對角線結構(constant block diagonal structure)
的數組以進行雙向聚類。所謂“雙向聚類”，是指對變量和實例同時聚類。
本數據集可以用于譜協聚類(SpectralCoclustering)算法的示例。
"""

data, rows, columns = make_biclusters(
    shape=(300, 300), n_clusters=5, noise=5, shuffle=False, random_state=9487
)

plt.matshow(data, cmap=plt.cm.Blues)
plt.title("Original dataset")
show()

"""
10. make_checkerboard
make_checkerboard()用于生成一個具有棋盤格結構的數組，以進行雙向聚類。
"""

data, rows, columns = make_checkerboard(
    shape=(300, 300), n_clusters=5, noise=5, shuffle=False, random_state=9487
)

plt.matshow(data, cmap=plt.cm.Blues)
plt.title("Original dataset")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 瑞士捲
"""
===================================
Swiss Roll reduction with LLE
===================================
An illustration of Swiss Roll reduction
with locally linear embedding
"""

# This import is needed to modify the way figure behaves
from mpl_toolkits.mplot3d import Axes3D

#----------------------------------------------------------------------
# Locally linear embedding of the swiss roll

from sklearn import manifold

X, color = datasets.make_swiss_roll(n_samples=1500)

print("Computing LLE embedding")
X_r, err = manifold.locally_linear_embedding(X, n_neighbors=12,
                                             n_components=2)
print("Done. Reconstruction error: %g" % err)

#----------------------------------------------------------------------
# Plot result

fig = plt.figure()

ax = fig.add_subplot(211, projection='3d')
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=color, cmap=plt.cm.Spectral)

ax.set_title("Original data")
ax = fig.add_subplot(212)
ax.scatter(X_r[:, 0], X_r[:, 1], c=color, cmap=plt.cm.Spectral)
plt.axis('tight')
plt.xticks([]), plt.yticks([])
plt.title('Projected data')
plt.show()

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

"""
sklearn 使用make_regression生成回歸樣本數據及NumPy擬合

1. 介紹
sklearn的make_regression函數能生成回歸樣本數據。

2. 函數語法
make_regression(n_samples=100, n_features=100, n_informative=10, n_targets=1, bias=0.0, 
                effective_rank=None, tail_strength=0.5, noise=0.0, shuffle=True, coef=False, random_state=None)

3. 參數說明：
n_samples：樣本數
n_features：特征數(自變量個數)
n_informative：參與建模特征數
n_targets：因變量個數
noise：噪音
bias：偏差(截距)
coef：是否輸出coef標識
random_state：隨機狀態若為固定值則每次產生的數據都一樣
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
