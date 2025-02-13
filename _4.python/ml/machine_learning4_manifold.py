"""
manifold

# Manifold(岐管, 流形) learning: non-linear dimension reduction


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

import sklearn.linear_model
from sklearn import datasets
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn.decomposition import PCA

# 不要顯示一些警告
import warnings

# warnings.filterwarnings("ignore")

from sklearn.manifold import MDS
from sklearn.manifold import TSNE
from sklearn.manifold import LocallyLinearEmbedding
from sklearn.manifold import Isomap


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# MDS
df = pd.read_csv("data/machine_learning4_iris.csv")

X = np.asarray(df.iloc[:, :4])
X -= np.mean(X, axis=0)
X /= np.std(X, axis=0, ddof=1)

D = sklearn.metrics.pairwise.pairwise_distances(X, metric="euclidean")

stress = [
    MDS(
        dissimilarity="precomputed",
        n_components=k,
        random_state=9487,
        max_iter=300,
        eps=1e-9,
    )
    .fit(D)
    .stress_
    for k in range(1, X.shape[1] + 1)
]

print("Stress", stress)
plt.plot(range(1, 5), stress)

K = 2
mds = MDS(
    dissimilarity="precomputed",
    n_components=K,
    random_state=9487,
    max_iter=300,
    eps=1e-9,
)
Xmds = mds.fit_transform(D)

pca = PCA(n_components=K)
pca.fit(X)
PC = pca.transform(X)

print("Correlation between PCA and MDS")
cor = [
    np.corrcoef(Xmds[:, j], PC[:, j])[0, 1]
    for j in range(min(Xmds.shape[1], PC.shape[1]))
]
print(cor)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
digits = datasets.load_digits()
print(type(digits))
print(len(digits))

print("TSNE")
n_components = 2  # 削減後の次元を2に設定
model = TSNE(n_components=n_components)
print(model.fit_transform(digits.data))
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# load images of the digits 0 through 5 and visualize several of them

digits = datasets.load_digits(n_class=6)

fig, ax = plt.subplots(8, 8, figsize=(6, 6))
for i, axi in enumerate(ax.flat):
    axi.imshow(digits.images[i], cmap="binary")
    axi.set(xticks=[], yticks=[])

show()


# project the digits into 2 dimensions using IsoMap
iso = Isomap(n_components=2)
projection = iso.fit_transform(digits.data)


# plot the results
plt.scatter(
    projection[:, 0],
    projection[:, 1],
    lw=0.1,
    c=digits.target,
    cmap=plt.cm.get_cmap("cubehelix", 6),
)
plt.colorbar(ticks=range(6), label="digit value")
plt.clim(-0.5, 5.5)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

colors = [
    "#348ABD",
    "#A60628",
    "#7A68A6",
    "#467821",
    "#D55E00",
    "#CC79A7",
    "#56B4E9",
    "#009E73",
    "#F0E442",
    "#0072B2",
]


def plot_embedding(ax, X):
    x_min, x_max = np.min(X, 0), np.max(X, 0)
    X = (X - x_min) / (x_max - x_min)
    for i in range(X.shape[0]):
        ax.text(
            X[i, 0],
            X[i, 1],
            str(digits.target[i]),
            color=colors[int(y[i] % 10)],
            fontdict={"size": 12},
        )


def format_plot(ax, x_label, y_label, title):
    ax.xaxis.set_major_formatter(plt.NullFormatter())
    ax.yaxis.set_major_formatter(plt.NullFormatter())

    ax.set_title(title)


# PCA降維
from sklearn import decomposition
from sklearn import manifold

digits = datasets.load_digits(n_class=10)

X = digits.data
y = digits.target

X_pca = decomposition.TruncatedSVD(n_components=2).fit_transform(X)

fig, ax = plt.subplots()
plot_embedding(ax, X_pca)
format_plot(ax, "", "", "PCA")

show()

print("------------------------------")  # 30個

embedder = manifold.SpectralEmbedding(
    n_components=2, random_state=0, eigen_solver="arpack"
)
X_se = embedder.fit_transform(X)

tsne = manifold.TSNE(n_components=2, init="pca", random_state=0)

X_tsne = tsne.fit_transform(X)

mds = manifold.MDS(n_components=2, n_init=1, max_iter=100)
X_mds = mds.fit_transform(X)

fig, ax = plt.subplots(2, 2)

fig.subplots_adjust(left=0.0625, right=0.95, wspace=0.1)

plot_embedding(ax[0, 0], X_pca)
format_plot(ax[0, 0], "", "", "PCA")

plot_embedding(ax[0, 1], X_mds)
format_plot(ax[0, 1], "", "", "MDS")

plot_embedding(ax[1, 0], X_se)
format_plot(ax[1, 0], "", "", "Spectral")

plot_embedding(ax[1, 1], X_tsne)
format_plot(ax[1, 1], "", "", "tSNE")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Pairwise distance between European cities

url = "data/machine_learning4_eurodist.csv"
df = pd.read_csv(url)

print(df.iloc[:5, :5])

city = df["city"]
D = np.array(df.iloc[:, 1:])  # Distance matrix

# Arbitrary choice of K=2 components

mds = MDS(
    dissimilarity="precomputed",
    n_components=2,
    random_state=9487,
    max_iter=3000,
    eps=1e-9,
)
X = mds.fit_transform(D)

# Recover coordinates of the cities in Euclidean referential whose orientation is arbitrary:

Deuclidean = sklearn.metrics.pairwise.pairwise_distances(X, metric="euclidean")
print(np.round(Deuclidean[:5, :5]))

# Plot: apply some rotation and flip
theta = 80 * np.pi / 180.0
rot = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
Xr = np.dot(X, rot)
# flip x
Xr[:, 0] *= -1

plt.scatter(Xr[:, 0], Xr[:, 1])

for i in range(len(city)):
    plt.text(Xr[i, 0], Xr[i, 1], city[i])
plt.axis("equal")

show()

print("------------------------------")  # 30個

k_range = range(1, min(5, D.shape[0] - 1))
stress = [
    MDS(
        dissimilarity="precomputed",
        n_components=k,
        random_state=9487,
        max_iter=300,
        eps=1e-9,
    )
    .fit(D)
    .stress_
    for k in k_range
]

print(stress)
plt.plot(k_range, stress)
plt.xlabel("k")
plt.ylabel("stress")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("make_s_curve 三維S曲線數據集")
N = 1000
X, y = datasets.make_s_curve(n_samples=N)

print(X[:, 0].max(), X[:, 0].min())  # 1 ~ -1
print(X[:, 1].max(), X[:, 1].min())  # 2 ~ 0
print(X[:, 2].max(), X[:, 2].min())  # 2 ~ -2

fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=y)
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("make_s_curve 三維S曲線數據集")
from matplotlib.ticker import NullFormatter

N = 1000
X, color = datasets.make_s_curve(n_samples=N, noise=0)

fig = plt.figure(figsize=(8, 6))

# Add 3d scatter plot
ax = fig.add_subplot(111, projection="3d")
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=color, cmap=plt.cm.Spectral)
ax.scatter(0, 0, 0, c="r", s=50)

elevation, azimuth = 4, -72  # 仰角 方位角
ax.view_init(elev=elevation, azim=azimuth)  # 仰角(elevation), 方位角(azimuth)
# 仰角(elevation), 看向原點, xy平面之夾角
# 方位角(azimuth), 看向原點, 與+y軸之夾角

ax.set_xlabel("X", color="r")
ax.set_ylabel("Y", color="g")
ax.set_zlabel("Z", color="b")

# 不要畫刻度
ax.xaxis.set_major_formatter(NullFormatter())
ax.yaxis.set_major_formatter(NullFormatter())
ax.axis("tight")

show()

print("------------------------------")  # 30個

print("make_s_curve 三維S曲線數據集")

from mpl_toolkits.mplot3d import Axes3D
from sklearn import manifold

N = 1000
X, color = datasets.make_s_curve(n_samples=N, noise=0)
print(X.shape)
print(color.shape)

isomap = manifold.Isomap(n_neighbors=10, n_components=2)
X_isomap = isomap.fit_transform(X)

print("t-SNE")

tsne = manifold.TSNE(n_components=2, init="pca", random_state=9487)
X_tsne = tsne.fit_transform(X)

fig = plt.figure(figsize=(15, 5))
plt.suptitle("Manifold Learning", fontsize=14)

ax = fig.add_subplot(131, projection="3d")
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=color, cmap=plt.cm.Spectral)
ax.view_init(4, -72)
plt.title('2D "S shape" manifold in 3D')

ax = fig.add_subplot(132)
plt.scatter(X_isomap[:, 0], X_isomap[:, 1], c=color, cmap=plt.cm.Spectral)
plt.title("Isomap")
plt.xlabel("First component")
plt.ylabel("Second component")

ax = fig.add_subplot(133)
plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=color, cmap=plt.cm.Spectral)
plt.title("t-SNE")
plt.xlabel("First component")
plt.ylabel("Second component")
plt.axis("tight")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from matplotlib.ticker import NullFormatter
from sklearn import manifold

n_samples = 300
n_components = 2
(fig, subplots) = plt.subplots(3, 5, figsize=(15, 8))
perplexities = [5, 30, 50, 100]

X, y = datasets.make_circles(n_samples=n_samples, factor=0.5, noise=0.05)

red = y == 0
green = y == 1

ax = subplots[0][0]
ax.scatter(X[red, 0], X[red, 1], c="r")
ax.scatter(X[green, 0], X[green, 1], c="g")
ax.xaxis.set_major_formatter(NullFormatter())
ax.yaxis.set_major_formatter(NullFormatter())
plt.axis("tight")

for i, perplexity in enumerate(perplexities):
    ax = subplots[0][i + 1]

    t0 = time.time()
    tsne = manifold.TSNE(
        n_components=n_components,
        init="random",
        random_state=9487,
        perplexity=perplexity,
    )
    Y = tsne.fit_transform(X)
    t1 = time.time()
    print("circles, perplexity=%d in %.2g sec" % (perplexity, t1 - t0))
    ax.set_title("Perplexity=%d" % perplexity)
    ax.scatter(Y[red, 0], Y[red, 1], c="r")
    ax.scatter(Y[green, 0], Y[green, 1], c="g")
    ax.xaxis.set_major_formatter(NullFormatter())
    ax.yaxis.set_major_formatter(NullFormatter())
    ax.axis("tight")

X, color = datasets.make_s_curve(n_samples)

ax = subplots[1][0]
ax.scatter(X[:, 0], X[:, 2], c=color)
ax.xaxis.set_major_formatter(NullFormatter())
ax.yaxis.set_major_formatter(NullFormatter())

for i, perplexity in enumerate(perplexities):
    ax = subplots[1][i + 1]

    t0 = time.time()
    tsne = manifold.TSNE(
        n_components=n_components, init="random", random_state=0, perplexity=perplexity
    )
    Y = tsne.fit_transform(X)
    t1 = time.time()
    print("S-curve, perplexity=%d in %.2g sec" % (perplexity, t1 - t0))

    ax.set_title("Perplexity=%d" % perplexity)
    ax.scatter(Y[:, 0], Y[:, 1], c=color)
    ax.xaxis.set_major_formatter(NullFormatter())
    ax.yaxis.set_major_formatter(NullFormatter())
    ax.axis("tight")


# Another example using a 2D uniform grid
x = np.linspace(0, 1, int(np.sqrt(n_samples)))
xx, yy = np.meshgrid(x, x)
X = np.hstack(
    [
        xx.ravel().reshape(-1, 1),
        yy.ravel().reshape(-1, 1),
    ]
)
color = xx.ravel()
ax = subplots[2][0]
ax.scatter(X[:, 0], X[:, 1], c=color)
ax.xaxis.set_major_formatter(NullFormatter())
ax.yaxis.set_major_formatter(NullFormatter())

for i, perplexity in enumerate(perplexities):
    ax = subplots[2][i + 1]

    t0 = time.time()
    tsne = manifold.TSNE(
        n_components=n_components, init="random", random_state=0, perplexity=perplexity
    )
    Y = tsne.fit_transform(X)
    t1 = time.time()
    print("uniform grid, perplexity=%d in %.2g sec" % (perplexity, t1 - t0))

    ax.set_title("Perplexity=%d" % perplexity)
    ax.scatter(Y[:, 0], Y[:, 1], c=color)
    ax.xaxis.set_major_formatter(NullFormatter())
    ax.yaxis.set_major_formatter(NullFormatter())
    ax.axis("tight")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" import fail

from sklearn.datasets import make_swiss_roll

data, color = make_swiss_roll(n_samples=1500)
n_neighbors = 12 # 近傍點の數 
n_components = 2 # 削減後の次元數

model = LocallyLinearEmbedding(n_neighbors=n_neighbors,

n_components=n_components)

model.fit(data)  # 學習訓練.fit

print(model.transform(data)) # 変換したデータ
"""
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
