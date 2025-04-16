"""
主成分分析 Principal Component Analysis, PCA
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

from common1 import *
import scipy
import sklearn.linear_model
from sklearn import datasets
from sklearn.datasets import make_blobs  # 集群資料集
from sklearn.datasets import make_moons
from sklearn.datasets import make_circles
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn import metrics
from sklearn.decomposition import PCA
from sklearn.decomposition import KernelPCA  # KernelPCA 萃取特徵

from matplotlib.colors import ListedColormap
from sklearn.preprocessing import MinMaxScaler
from sklearn import tree


def show():
    plt.show()
    pass


print(__doc__)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("PCA 降維度, 4維 => 2維")

N = 20  # 散點的數量

X = np.random.randint(0, 100, size=(N, 2))  # 產生 N x 4 陣列，內容為 0～100 隨機數字

n_components = 1  # 降維後的維度

clf = PCA(n_components=n_components)

clf = clf.fit(X)

X2 = clf.transform(X)

# X2 = clf.fit_transform(X)  # .fit + .transform一起做

print("轉換前 維度 :", X.shape)
print("轉換後 維度 :", X2.shape)

print(X2)
plt.subplot(211)
plt.scatter(X[:, 0], X[:, 1], c="r")
plt.scatter(X[8, 0], X[8, 1], c="g")
plt.title("轉換前之第0 1維")

plt.subplot(212)
plt.scatter(X2[:], X2[:], c="g")
plt.scatter(X2[8], X2[8], c="r")
plt.title("轉換前之第2 3維")

show()

"""
plt.subplot(221)
plt.scatter(X[:, 0], X[:, 1])
plt.title("轉換前之第0 1維")

plt.subplot(222)
plt.scatter(X[:, 2], X[:, 3])
plt.title("轉換前之第2 3維")

plt.subplot(223)
plt.scatter(X2[:, 0], X2[:, 1])
plt.title("轉換後之第0 1維")

plt.subplot(224)
# 如果有4維的話
# plt.scatter(X2[:,2], X2[:,3])
# plt.title('轉換後之第2 3維')

show()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("數學方法降維")

iris = datasets.load_iris()
X = iris.data
y = iris.target  # 資料集目標

df = pd.DataFrame(X, columns=["萼長", "萼寬", "瓣長", "瓣寬"])
# print(df)

mat = df.corr()
print("相關係數 :\n", mat, sep="")

sns.heatmap(
    mat,
    annot=True,
    vmax=1,
    vmin=-1,
    xticklabels=True,
    yticklabels=True,
    square=True,
    cmap="gray",
)

show()

print("------------------------------")  # 30個

plt.subplot(121)
plt.scatter(X[:, 0], X[:, 1], c=np.array(y))
plt.title("iris轉換前之第0 1維(共4維)")

n_components = 2  # 降維後的維度
clf = PCA(n_components=n_components)

X2 = clf.fit_transform(df)  # .fit + .transform一起做

print("轉換前 4維 :", X.shape)
print("轉換後 2維 :", X2.shape)

plt.subplot(122)
plt.scatter(X2[:, 0], X2[:, 1], c=np.array(y))
plt.title("iris轉換後之第0 1維(共2維)")

show()

"""
explained_variance_ratio_ : 主成分的方差比例
explained_variance_ : 主成分的方差比值
用于确定重要主成分
"""
print("主成分的方差比例 explained_variance_ratio_")
print(clf.explained_variance_ratio_)
print("和")
print(clf.explained_variance_ratio_.sum())

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 建立資料
N = 100
experience = np.random.normal(size=N)
salary = 1500 + experience + np.random.normal(size=N, scale=0.5)

X = np.column_stack([experience, salary])
print("轉換前 :", X.shape)

# PCA with scikit-learn
n_components = 2  # 降維後的維度
clf = PCA(n_components=n_components)

clf.fit(X)

print("主成分的方差比例 explained_variance_ratio_")
print(clf.explained_variance_ratio_)

X2 = clf.transform(X)

print("轉換後 :", X2.shape)

plt.subplot(121)
plt.scatter(X[:, 0], X[:, 1])
plt.xlabel("X0")
plt.ylabel("X1")

plt.subplot(122)
plt.scatter(X2[:, 0], X2[:, 1])
plt.xlabel("PC1 (var=%.2f)" % clf.explained_variance_ratio_[0])
plt.ylabel("PC2 (var=%.2f)" % clf.explained_variance_ratio_[1])
plt.axis("equal")
plt.tight_layout()

show()

print("------------------------------------------------------------")  # 60個
# decomposition_solutions
print("------------------------------------------------------------")  # 60個

# 使用iris資料 做 PCA

# Apply PCA on iris dataset

# https://tgmstat.wordpress.com/2013/11/28/computing-and-visualizing-pca-in-r/

df = pd.read_csv("data/machine_learning4_iris.csv")

cc = df.head()
print(cc)

cc = df.describe()
print(cc)

X = np.array(df.iloc[:, :4])
# np.around(np.corrcoef(X.T), 3)

# Center and standardize

X = np.array(df.iloc[:, :4])
X -= np.mean(X, axis=0)
X /= np.std(X, axis=0, ddof=1)
np.around(np.corrcoef(X.T), 3)

n_components = X.shape[1]  # 降維後的維度
clf = PCA(n_components=n_components)

clf.fit(X)

print("主成分的方差比例 explained_variance_ratio_")
print(clf.explained_variance_ratio_)

K = 2
n_components = X.shape[1]  # 降維後的維度
clf = PCA(n_components=n_components)

clf.fit(X)

X2 = clf.transform(X)
# print(X2)

print(clf.components_)
CorPC = pd.DataFrame(
    [
        [np.corrcoef(X[:, j], X2[:, k])[0, 1] for j in range(X.shape[1])]
        for k in range(K)
    ],
    columns=df.columns[:4],
    index=["X2 %i" % k for k in range(K)],
)

print(CorPC)

colors = {"setosa": "r", "versicolor": "g", "virginica": "blue"}
print(df["species"].unique())
# plt.scatter(df['experience'], df['salary'], c=df['education'].apply(lambda x: colors[x]), s=100)
plt.scatter(X2[:, 0], X2[:, 1], c=df["species"].apply(lambda x: colors[x]))
plt.xlabel("PC1")
plt.ylabel("PC2")

# Pairewise plot

df["PC1"] = X2[:, 0]
df["PC2"] = X2[:, 1]

ax = sns.pairplot(df, hue="species")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 實現PCA演算法

# 建立測試資料

# 第一個類別
mu_vec1 = np.array([0, 0, 0])  # 平均數
cov_mat1 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])  # 共變異矩陣
class1_sample = np.random.multivariate_normal(mu_vec1, cov_mat1, 20).T

# 第二個類別
mu_vec2 = np.array([1, 1, 1])  # 平均數
cov_mat2 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])  # 共變異矩陣
class2_sample = np.random.multivariate_normal(mu_vec2, cov_mat2, 20).T

cc = class1_sample.shape, class2_sample.shape
print(cc)

from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection="3d")
ax.plot(
    class1_sample[0, :],
    class1_sample[1, :],
    class1_sample[2, :],
    "o",
    markersize=8,
    color="blue",
    alpha=0.5,
    label="類別1",
)
ax.plot(
    class2_sample[0, :],
    class2_sample[1, :],
    class2_sample[2, :],
    "^",
    markersize=8,
    alpha=0.5,
    color="red",
    label="類別2",
)

plt.title("測試資料")
ax.legend(loc="upper right")

show()

# 合併資料

all_samples = np.concatenate((class1_sample, class2_sample), axis=1)
cc = all_samples.shape
print(cc)

# 計算共變異數矩陣(covariance matrix)

cov_mat = np.cov([all_samples[0, :], all_samples[1, :], all_samples[2, :]])
print("共變異數矩陣:\n", cov_mat)

# 計算特徵向量(eigenvector)及對應的特徵值(eigenvalue, λ)

# 計算特徵值(eigenvalue)及對應的特徵向量(eigenvector)
eig_val_sc, eig_vec_sc = np.linalg.eig(cov_mat)
print("特徵向量:\n", eig_vec_sc)
print("特徵值:\n", eig_val_sc)

# 繪製特徵向量

from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d
from matplotlib.patches import FancyArrowPatch


# 繪製箭頭
class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def do_3d_projection(self, renderer=None):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, self.axes.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        return np.min(zs)


# 設定 3D 繪圖
fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111, projection="3d")

# 繪製特徵向量
ax.plot(
    all_samples[0, :],
    all_samples[1, :],
    all_samples[2, :],
    "o",
    markersize=8,
    color="green",
    alpha=0.2,
)
[mean_x, mean_y, mean_z] = np.mean(all_samples, axis=1)
ax.plot([mean_x], [mean_y], [mean_z], "o", markersize=10, color="red", alpha=0.5)
for v in eig_vec_sc.T:
    a = Arrow3D(
        [mean_x, v[0]],
        [mean_y, v[1]],
        [mean_z, v[2]],
        mutation_scale=20,
        lw=3,
        arrowstyle="-|>",
        color="r",
    )
    ax.add_artist(a)
ax.set_xlabel("x_values")
ax.set_ylabel("y_values")
ax.set_zlabel("z_values")

show()

# 合併特徵向量及特徵值，針對特徵值降冪排序，挑出前2名。

# 合併特徵向量及特徵值
eig_pairs = [(np.abs(eig_val_sc[i]), eig_vec_sc[:, i]) for i in range(len(eig_val_sc))]

# 針對特徵值降冪排序
eig_pairs.sort(key=lambda x: x[0], reverse=True)

# 挑出前2名
for i in eig_pairs[:2]:
    print(i[1])

# 座標轉換矩陣

matrix_w = np.hstack((eig_pairs[0][1].reshape(3, 1), eig_pairs[1][1].reshape(3, 1)))
print("Matrix W:\n", matrix_w)

# 原始資料乘以轉換矩陣，得到主成分

transformed = matrix_w.T.dot(all_samples)
cc = transformed.shape
print(cc)

# 繪製轉換後的資料

plt.plot(
    transformed[0, 0:20],
    transformed[1, 0:20],
    "o",
    markersize=7,
    color="blue",
    alpha=0.5,
    label="class1",
)
plt.plot(
    transformed[0, 20:40],
    transformed[1, 20:40],
    "^",
    markersize=7,
    color="red",
    alpha=0.5,
    label="class2",
)
plt.xlim([-4, 4])
plt.ylim([-4, 4])
plt.xlabel("x_values")
plt.ylabel("y_values")
plt.legend()
plt.title("Transformed samples with class labels")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Scikit-learn LDA實作

X, y = make_circles(n_samples=1_000, factor=0.3, noise=0.05, random_state=0)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y)

# 繪製訓練及測試資料
_, (train_ax, test_ax) = plt.subplots(ncols=2, sharex=True, sharey=True, figsize=(8, 4))
train_ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train)
train_ax.set_ylabel("Feature #1")
train_ax.set_xlabel("Feature #0")
train_ax.set_title("Training data")

test_ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test)
test_ax.set_xlabel("Feature #0")
_ = test_ax.set_title("Testing data")
show()

# PCA 萃取特徵
n_components = 2  # 降維後的維度
clf = PCA(n_components=n_components)

# KernelPCA 萃取特徵
kernel_pca = KernelPCA(
    n_components=None, kernel="rbf", gamma=10, fit_inverse_transform=True, alpha=0.1
)

X_test_pca = clf.fit(X_train).transform(X_test)  # 學習訓練.fit

# 繪製原始測試資料及經PCA轉換後的新資料

fig, (orig_data_ax, pca_proj_ax) = plt.subplots(ncols=2, figsize=(10, 4))

orig_data_ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test)
orig_data_ax.set_ylabel("Feature #1")
orig_data_ax.set_xlabel("Feature #0")
orig_data_ax.set_title("Testing data")

pca_proj_ax.scatter(X_test_pca[:, 0], X_test_pca[:, 1], c=y_test)
pca_proj_ax.set_ylabel("Principal component #1")
pca_proj_ax.set_xlabel("Principal component #0")
pca_proj_ax.set_title("Projection of testing data\n using PCA")

# Text(0.5, 1.0, 'Projection of testing data\n using PCA')
show()

# KernelPCA 萃取特徵
kernel_pca = KernelPCA(
    n_components=None, kernel="rbf", gamma=10, fit_inverse_transform=True, alpha=0.1
)

X_test_kernel_pca = kernel_pca.fit(X_train).transform(X_test)  # 學習訓練.fit

fig, (orig_data_ax, kernel_pca_proj_ax) = plt.subplots(ncols=2, figsize=(10, 4))

orig_data_ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test)
orig_data_ax.set_ylabel("Feature #1")
orig_data_ax.set_xlabel("Feature #0")
orig_data_ax.set_title("Testing data")

kernel_pca_proj_ax.scatter(X_test_kernel_pca[:, 0], X_test_kernel_pca[:, 1], c=y_test)
kernel_pca_proj_ax.set_ylabel("Principal component #1")
kernel_pca_proj_ax.set_xlabel("Principal component #0")
_ = kernel_pca_proj_ax.set_title("Projection of testing data\n using KernelPCA")
show()

# 載入上/下弦月資料

# X, y = make_moons(n_samples=1_000, noise=0.05, random_state=0)
X, y = make_moons(n_samples=1000, random_state=123)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y)

_, (train_ax, test_ax) = plt.subplots(ncols=2, sharex=True, sharey=True, figsize=(8, 4))

train_ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train)
train_ax.set_ylabel("Feature #1")
train_ax.set_xlabel("Feature #0")
train_ax.set_title("Training data")

test_ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test)
test_ax.set_xlabel("Feature #0")
_ = test_ax.set_title("Testing data")
show()

# PCA 萃取特徵
n_components = 2  # 降維後的維度
clf = PCA(n_components=n_components)

# KernelPCA 萃取特徵
kernel_pca = KernelPCA(
    n_components=None, kernel="rbf", gamma=10, fit_inverse_transform=True, alpha=0.1
)

X_test_pca = clf.fit(X_train).transform(X_test)  # 學習訓練.fit

fig, (orig_data_ax, pca_proj_ax) = plt.subplots(ncols=2, figsize=(10, 4))

orig_data_ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test)
orig_data_ax.set_ylabel("Feature #1")
orig_data_ax.set_xlabel("Feature #0")
orig_data_ax.set_title("Testing data")

pca_proj_ax.scatter(X_test_pca[:, 0], X_test_pca[:, 1], c=y_test)
pca_proj_ax.set_ylabel("Principal component #1")
pca_proj_ax.set_xlabel("Principal component #0")
pca_proj_ax.set_title("Projection of testing data\n using PCA")

# Text(0.5, 1.0, 'Projection of testing data\n using PCA')
show()

# KernelPCA 萃取特徵
kernel_pca = KernelPCA(n_components=None, kernel="rbf", gamma=15)

X_test_kernel_pca = kernel_pca.fit(X_train).transform(X_test)  # 學習訓練.fit

fig, (orig_data_ax, kernel_pca_proj_ax) = plt.subplots(ncols=2, figsize=(10, 4))

orig_data_ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test)
orig_data_ax.set_ylabel("Feature #1")
orig_data_ax.set_xlabel("Feature #0")
orig_data_ax.set_title("Testing data")

kernel_pca_proj_ax.scatter(X_test_kernel_pca[:, 0], X_test_kernel_pca[:, 1], c=y_test)
kernel_pca_proj_ax.set_ylabel("Principal component #1")
kernel_pca_proj_ax.set_xlabel("Principal component #0")
_ = kernel_pca_proj_ax.set_title("Projection of testing data\n using KernelPCA")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# t-SNE測試
from sklearn.manifold import TSNE

# 生成3個集群資料

num_points_per_class = 50

# Class 1
mean1 = [0, 0]
cov = [[0.1, 0], [0, 0.1]]
X1 = np.random.multivariate_normal(mean1, cov, num_points_per_class)

# Class 2
mean2 = [10, 0]
X2 = np.random.multivariate_normal(mean2, cov, num_points_per_class)

# Class 3
mean3 = [5, 6]
X3 = np.random.multivariate_normal(mean3, cov, num_points_per_class)

X = np.concatenate([X1, X2, X3], axis=0)
cc = X.shape
print(cc)

scaler = MinMaxScaler()  # 特徵縮放
X = scaler.fit_transform(X)  # .fit + .transform一起做

# 繪圖
colors = ["red", "green", "blue"]
for i in range(3):
    plt.scatter(X[i * 50 : (i + 1) * 50, 0], X[i * 50 : (i + 1) * 50, 1], c=colors[i])

show()

# t-SNE

perplexity = 25
X_embedded = TSNE(
    n_components=1, perplexity=perplexity, learning_rate="auto", init="random"
).fit_transform(
    X
)  # .fit + .transform一起做
for i in range(3):
    plt.scatter(X_embedded[i * 50 : (i + 1) * 50], np.zeros(50), c=colors[i])
show()

# PCA
n_components = 1  # 降維後的維度
X_pca = PCA(n_components=n_components).fit_transform(X)  # .fit + .transform一起做

for i in range(3):
    plt.scatter(X_pca[i * 50 : (i + 1) * 50], np.zeros(50), c=colors[i])
show()

# 困惑度(perplexity)測試

perplexity = 2
X_embedded = TSNE(
    n_components=1, perplexity=perplexity, learning_rate="auto", init="random"
).fit_transform(
    X
)  # .fit + .transform一起做

for i in range(3):
    plt.scatter(X_embedded[i * 50 : (i + 1) * 50], np.zeros(50), c=colors[i])
show()


perplexity = 130
X_embedded = TSNE(
    n_components=1, perplexity=perplexity, learning_rate="auto", init="random"
).fit_transform(
    X
)  # .fit + .transform一起做

for i in range(3):
    plt.scatter(X_embedded[i * 50 : (i + 1) * 50], np.zeros(50), c=colors[i])
show()


# 非線性分離
# 生成S曲線資料
from matplotlib import ticker
from sklearn import manifold
from sklearn import datasets

n_samples = 1500
S_points, S_color = datasets.make_s_curve(n_samples, random_state=0)
cc = S_points.shape, S_color.shape
print(cc)

# ((1500, 3), (1500,))

# 定義繪圖函數


def plot_2d(points, points_color, title):
    fig, ax = plt.subplots(figsize=(3, 3), facecolor="white", constrained_layout=True)
    fig.suptitle(title, size=16)
    add_2d_scatter(ax, points, points_color)
    show()


def add_2d_scatter(ax, points, points_color, title=None):
    x, y = points.T
    ax.scatter(x, y, c=points_color, s=50, alpha=0.8)
    ax.set_title(title)
    ax.xaxis.set_major_formatter(ticker.NullFormatter())
    ax.yaxis.set_major_formatter(ticker.NullFormatter())


def plot_3d(points, points_color, title):
    x, y, z = points.T

    fig, ax = plt.subplots(
        figsize=(6, 6),
        facecolor="white",
        tight_layout=True,
        subplot_kw={"projection": "3d"},
    )
    fig.suptitle(title, size=16)
    col = ax.scatter(x, y, z, c=points_color, s=50, alpha=0.8)
    ax.view_init(azim=-60, elev=9)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.zaxis.set_major_locator(ticker.MultipleLocator(1))

    fig.colorbar(col, ax=ax, orientation="horizontal", shrink=0.6, aspect=60, pad=0.01)
    show()


# 繪製原始資料

plot_3d(S_points, S_color, "Original S-curve samples")

# 繪製降維後資料

t_sne = manifold.TSNE(
    n_components=2,
    perplexity=30,
    init="random",
    n_iter=250,
    random_state=0,
)
S_t_sne = t_sne.fit_transform(S_points)  # .fit + .transform一起做

plot_2d(S_t_sne, S_color, "T-distributed Stochastic  \n Neighbor Embedding")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from PIL import Image
from PIL import ImageEnhance
import matplotlib.cm as cm
import matplotlib.image as img
import pylab
import cv2

# 创建 eigValPct(eigVals, percentage)
# 函数传入的参数是特征值eigVals和百分比percentage，返回需要降到的维度数num


def eigValPct(eigVals, percentage):
    sortArray = np.sort(eigVals)[::-1]  # 特征值从大到小排序
    pct = np.sum(sortArray) * percentage
    tmp = 0
    num = 0
    for eigVal in sortArray:
        tmp += eigVal
        num += 1
        if tmp >= pct:
            return num


"""
创建 im_PCA(dataMat, percentage=0.9)
函数有两个参数，其中dataMat是已经转换成矩阵matrix形式的数据集，每列表示一个维度；
其中的percentage表示取前多少个特征需要达到的方差占比，默认为0.9
"""


def im_PCA(dataMat, percentage=0.9):
    meanVals = np.mean(dataMat, axis=0)
    meanRemoved = dataMat - meanVals
    # 这里不管是对去中心化数据或原始数据计算协方差矩阵，结果都一样，特征值大小会变，但相对大小不会改变
    # 标准的计算需要除以(dataMat.shape[0]-1)，不算也不会影响结果，理由同上
    covMat = np.dot(np.transpose(meanRemoved), meanRemoved)
    eigVals, eigVects = np.linalg.eig(np.mat(covMat))
    k = eigValPct(eigVals, percentage)  # 要达到方差的百分比percentage，需要前k个向量
    print("K =", k)
    eigValInd = np.argsort(eigVals)[::-1]  # 对特征值eigVals从大到小排序
    eigValInd = eigValInd[:k]
    redEigVects = eigVects[:, eigValInd]  # 主成分
    lowDDataMat = meanRemoved * redEigVects  # 将原始数据投影到主成分上得到新的低维数据lowDDataMat
    reconMat = (lowDDataMat * redEigVects.T) + meanVals  # 得到重构数据reconMat
    return lowDDataMat, reconMat


def PrintError(data, recdata):
    sum1 = 0
    sum2 = 0
    D_value = data - recdata  # 计算两幅图像之间的差值矩阵
    # 计算两幅图像之间的误差率，即信息丢失率
    for i in range(data.shape[0]):
        sum1 += np.dot(data[i], data[i])
        sum2 += np.dot(D_value[i], D_value[i])
    print("丢失信息量：", sum2)
    print("原始信息量：", sum1)
    print("信息丢失率：", sum2 / sum1)


filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg"
img = cv2.imread(filename)
blue = img[:, :, 0]
dataMat = np.mat(blue)
lowDDataMat, reconMat = im_PCA(dataMat, 1)
print("原始数据", blue.shape, "降维数据", lowDDataMat.shape)
print(dataMat)
print(reconMat)
# 格式必须转换为uint8格式，这里丢失了很多信息！！！
reconMat = np.array(reconMat, dtype="uint8")

plt.imshow(cv2.cvtColor(blue, cv2.COLOR_BGR2RGB))
plt.title("blue")
show()

plt.imshow(cv2.cvtColor(np.array(reconMat, dtype="uint8"), cv2.COLOR_BGR2RGB))
plt.title("reconMat")
show()

n_components = 426  # 降維後的維度
clf = PCA(n_components=n_components).fit(blue)
# 降维
x_new = clf.transform(blue)
# 还原降维后的数据到原空间
recdata = clf.inverse_transform(x_new)
print(recdata)
# 计算误差
PrintError(np.array(blue, dtype="double"), np.array(reconMat, dtype="double"))

plt.imshow(cv2.cvtColor(np.array(recdata, dtype="uint8"), cv2.COLOR_BGR2RGB))
plt.title("sklearn-recdata")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/wine.data.csv")

cc = df.head()
print(cc)

# df.iloc[:,1:].describe()

# Boxplots by output labels/classes

for c in df.columns[1:]:
    df.boxplot(c, by="Class", figsize=(7, 4))
    plt.title("{}\n".format(c))
    plt.xlabel("Wine Class")
    show()


plt.figure(figsize=(10, 6))
plt.scatter(
    df["OD280/OD315 of diluted wines"],
    df["Flavanoids"],
    c=df["Class"],
    edgecolors="k",
    alpha=0.75,
    s=150,
)
plt.grid(True)
plt.title("Scatter plot of two features showing the \ncorrelation and class seperation")
plt.xlabel("OD280/OD315 of diluted wines")
plt.ylabel("Flavanoids")
show()

# Are the features independent? Plot co-variance matrix


def correlation_matrix(df):
    from matplotlib import pyplot as plt
    from matplotlib import cm as cm

    fig = plt.figure(figsize=(16, 12))
    ax1 = fig.add_subplot(111)
    cmap = cm.get_cmap("jet", 30)
    cax = ax1.imshow(df.corr(), interpolation="nearest", cmap=cmap)
    ax1.grid(True)
    plt.title("Wine data set features correlation")
    labels = df.columns
    ax1.set_xticklabels(labels)
    ax1.set_yticklabels(labels)
    # Add colorbar, make sure to specify tick locations to match desired ticklabels
    fig.colorbar(cax, ticks=[0.1 * i for i in range(-11, 11)])
    show()


cc = correlation_matrix(df)
print(cc)

# Principal Component Analysis
# Data scaling

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()  # 特徵縮放

X = df.drop("Class", axis=1)
y = df["Class"]

X = scaler.fit_transform(X)  # .fit + .transform一起做

dfx = pd.DataFrame(data=X, columns=df.columns[1:])

cc = dfx.head()
print(cc)

cc = dfx.describe()
print(cc)

pca = PCA(n_components=None)

dfx_pca = pca.fit(dfx)

# Plot the explained variance ratio

plt.figure(figsize=(10, 6))
plt.scatter(
    x=[i + 1 for i in range(len(dfx_pca.explained_variance_ratio_))],
    y=dfx_pca.explained_variance_ratio_,
    s=200,
    alpha=0.75,
    c="orange",
    edgecolor="k",
)
plt.grid(True)
plt.title("Explained variance ratio of the \nfitted principal component vector")
plt.xlabel("Principal components")
plt.xticks([i + 1 for i in range(len(dfx_pca.explained_variance_ratio_))])
plt.yticks()
plt.ylabel("Explained variance ratio")
show()

dfx_trans = pca.transform(dfx)

# Put it in a data frame

dfx_trans = pd.DataFrame(data=dfx_trans)

cc = dfx_trans.head()
print(cc)

plt.figure(figsize=(10, 6))
plt.scatter(
    dfx_trans[0], dfx_trans[1], c=df["Class"], edgecolors="k", alpha=0.75, s=150
)
plt.grid(True)
plt.title("Class separation using first two principal components")
plt.xlabel("Principal component-1")
plt.ylabel("Principal component-2")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
主成分分析
某金融服务公司为了了解贷款客户的信用程度，评价客户的信用等级，采用信用评级常用的5C方法，说明客户违约的可能性。

    品格：指客户的名誉；
    能力：指客户的偿还能力；
    资本：指客户的财务势力和财务状况；
    担保：指对申请贷款项担保的覆盖程度；
    环境：指外部经济、政策环境对客户的影响。
    每个单项都是由专家打分给出的。
"""

loan = pd.read_csv("data/Loan_aply.csv")
cc = loan.head()
print(cc)

# plt.figure(figsize=(2, 2))
plt.scatter(loan["X1"], loan["X2"])
plt.title("Scatter")

show()

sns.pairplot(loan.loc[:, "X1":])
show()

# 计算相关系数矩阵

cc = loan.loc[:, "X1":].corr(method="pearson")
print(cc)

# 初次查看主成分的解释方差占比

pca = PCA()
pca.fit(loan.loc[:, "X1":])

print(pca.explained_variance_ratio_)

# [ 0.84585431  0.08914623  0.04259067  0.01663007  0.00577872]

print(pca.components_)

"""
[[ 0.46881402  0.48487556  0.47274449  0.46174663  0.32925948]
 [ 0.83061232 -0.32991571  0.02117417 -0.43090441 -0.12293025]
 [ 0.0214065   0.0148012  -0.4127194  -0.24084475  0.87805421]
 [ 0.25465387 -0.28771993 -0.58858207  0.70628304 -0.0842856 ]
 [ 0.15808149  0.75700032 -0.50921327 -0.2104032  -0.31367674]]
"""

pca1 = PCA(n_components=1, whiten=True)
pca1.fit(loan.loc[:, "X1":])

"""
PCA(copy=True, iterated_power='auto', n_components=1, random_state=None,
  svd_solver='auto', tol=0.0, whiten=True)
"""
# 将打分结果和原始数据联结

score = pd.DataFrame(
    pca1.transform(loan.loc[:, "X1":]),
    columns=[
        "score",
    ],
)
loan.join(score).sort_values(by="score", ascending=False)

print(pca1.components_)

# 数据标准化的方法 http://www.cnblogs.com/chaosimple/p/4153167.html

# 因子分析
"""
cities_10记录了十个沿海省份的经济指标
变量 	含义
X1 	GDP
X2 	人均GDP
X3 	工业增加值
X4 	第三产业增加值
X5 	固定资产投资
X6 	基本建设投资
X7 	社会消费品零售总额
X8 	海关出口总额
X9 	地方财政收入
"""

cities = pd.read_csv("data/cities_10.csv", encoding="gbk")
print(cities)

cc = cities.loc[:, "X1":].corr(method="pearson").head()
print(cc)

from sklearn.preprocessing import scale

scale_cities = scale(cities.loc[:, "X1":])
pca_c = PCA(n_components=3, whiten=True).fit(scale_cities)
pca_c.explained_variance_ratio_

# array([ 0.80112955,  0.12214932,  0.0607924 ])

pca_c1 = PCA(n_components=2, whiten=True).fit(scale_cities)
pd.DataFrame(pca_c1.components_)

# sklearn中的因子分析是极大似然法,不推荐使用

from sklearn.decomposition import FactorAnalysis

fa = FactorAnalysis(n_components=2).fit(scale_cities)
pd.DataFrame(fa.components_)


cities_scores = pd.DataFrame(fa.transform(scale_cities), columns=["total", "avg"])
cities[["AREA"]].join(cities_scores)

# 对通信消费数据profile_telecom进行因子分析

profile = pd.read_csv("data/profile_telecom.csv")
cc = profile.head()
print(cc)

data = profile.loc[:, "cnt_call":]
cc = data.corr(method="pearson")
print(cc)

# 对数据进行标准化

from sklearn.preprocessing import scale

data_scaled = scale(data)

telecom_pca = PCA(n_components=2, whiten=True).fit(data_scaled)
telecom_pca.explained_variance_ratio_

telecom_pca.components_

telecom_pca.transform(data_scaled)

telecom_fa = FactorAnalysis(n_components=2).fit(data_scaled)
cc = pd.DataFrame(fa.components_).T
print(cc)

# 奇异值分解

A = np.matrix(
    [[5, 5, 0, 5], [5, 0, 3, 4], [3, 4, 0, 3], [0, 0, 5, 3], [5, 4, 4, 5], [5, 4, 5, 5]]
)

U, s, VH = np.linalg.svd(A)
print(U.shape, s.shape, VH.shape)

# (6, 6) (4,) (4, 4)

# plt.figure(figsize=[3, 2])
plt.plot(s)
show()

S = np.diag(s[:2])
UU = U[:, :2]

bob_T = np.matrix([5, 5, 0, 0, 0, 5])

bob_T.dot(UU).dot(np.linalg.inv(S))

# matrix([[-0.37752201,  0.08020351]])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
X1 品格：指客户的名誉；
X2 能力：指客户的偿还能力；
X3 资本：指客户的财务实力和财务状况；
X4 担保：指对申请贷款项担保的覆盖程度；
X5 环境：指外部经济、政策环境对客户的影响
"""
# 一、主成分分析

# 引入数据

model_data = pd.read_csv("data/Loan_aply.csv", encoding="gbk")
cc = model_data.head()
print(cc)

data = model_data.loc[:, "X1":]
cc = data.head()
print(cc)

# 查看相关系数矩阵，判定做变量降维的必要性（非必须）

corr_matrix = data.corr(method="pearson")

# 做主成分之前，进行中心标准化

from sklearn import preprocessing

data = preprocessing.scale(data)
# 使用sklearn的主成分分析，用于判断保留主成分的数量

"""说明：1、第一次的n_components参数应该设的大一点
   说明：2、观察explained_variance_ratio_和explained_variance_的取值变化，建议explained_variance_ratio_累积大于0.85，explained_variance_需要保留的最后一个主成分大于0.8，
"""
pca = PCA(n_components=4)
pca.fit(data)
print(pca.explained_variance_)  # 建议保留1个主成分
print(pca.explained_variance_ratio_)  # 建议保留1个主成分

pca = PCA(n_components=1).fit(data)  # 综上,2个主成分

newdata = pca.fit_transform(data)

citi10_pca = model_data.join(pd.DataFrame(newdata))

# 通过主成分在每个变量上的权重的绝对值大小，确定每个主成分的代表性

pd.DataFrame(pca.components_).T

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# correspondence analysis

"""
变量 	说明 	        标签
NO 	编号 	        -
salary 	收入 	        1:[0 1000], 2:[1000 3000], 3:[3001 5000], 4:[5001 7000], 5:[7001 9000], 6:>9000
educ 	教育程度 	1:高中以下, 2:大专, 3:本科, 4:大于硕士
freq 	频次 	        1:1次, 2:2-3次, 3:4-5次, 4:6-8次, 5:9-12次, 6:>13次
compan 	购物原因 	1:家人,2:情人, 3:朋友, 4: 同学, 5:客户, 6:无聊
purpose 目的 	        1:享受, 2:陪同异性, 3:生活用品, 4:公事, 5:无聊
average 单次平均消费 	1:小于50, 2:[50 99], 3: [100,149], 4:[150 199], 5:≥200
"""

df = pd.read_csv("data/shopping.csv")
cc = df.head()
print(cc)

purpose_dict = {
    1: "enjoyment",
    2: "opposite sex",
    3: "daily use",
    4: "business",
    5: "no reason",
}
average_dict = {1: "<50", 2: "[50 99]", 3: "[100 149]", 4: "[150 199]", 5: ">200"}
df.purpose.replace(purpose_dict, inplace=True)
df.average.replace(average_dict, inplace=True)

cross_table = pd.crosstab(df.purpose, df.average)
cross_table

from numpy.linalg import svd


class CA(object):
    """Simple corresondence analysis.

    Inputs
    ------
    ct : array_like, shape (n_samples, n_features)
      Two-way contingency table, training set, where `n_samples`
      is the number of samples and `n_features` is the number of features.

    Attributes
    ------
    F_ : array, shape (n_features, K)
      principal coordinates of columns. Where `K` = min(`n_features`, `n_samples`).

    G_ : array, shape (n_samples, K)
      principal coordinates of rows. Where `K` = min(`n_features`, `n_samples`).

    explained_variance_ratio_ : array, shape(K, )
      Percentage of variance explained by each of the selected components.

    Notes
    -----
    The implementation follows that presented in 'Correspondence
    Analysis in R, with Two- and Three-dimensional Graphics: The ca
    Package,' Journal of Statistical Software, May 2007, Volume 20,
    Issue 3.
    """

    def __init__(self, cross_table):
        N = np.matrix(cross_table, dtype=float)

        # correspondence matrix from contingency table
        P = N / N.sum()

        # row and column marginal totals of P as vectors
        r = P.sum(axis=1)
        c = P.sum(axis=0).T

        # diagonal matrices of row/column sums
        D_r_rsq = np.diag(1.0 / np.sqrt(r.A1))
        D_c_rsq = np.diag(1.0 / np.sqrt(c.A1))

        # the matrix of standarized residuals
        Z = D_r_rsq * (P - r * c.T) * D_c_rsq

        # compute the SVD
        U, D_a, V = svd(Z, full_matrices=False)
        D_a = np.asmatrix(np.diag(D_a))
        V = V.T

        # principal coordinates of columns
        F = D_c_rsq * V * D_a

        # principal coordinates of rows
        G = D_r_rsq * U * D_a

        # standard coordinates of rows
        X = D_r_rsq * U

        # standard coordinates of columns
        Y = D_c_rsq * V

        eigenvals = np.diagonal(D_a) ** 2
        explained_variance_ratio = eigenvals.cumsum() / eigenvals.sum()

        # the total variance of the data matrix
        inertia = sum(
            [
                (P[i, j] - r[i, 0] * c[j, 0]) ** 2 / (r[i, 0] * c[j, 0])
                for i in range(N.shape[0])
                for j in range(N.shape[1])
            ]
        )  # equals np.power(S, 2).sum() or eigenvalus.sum() or np.trace(S.T * S)

        self.F_ = F.A
        self.G_ = G.A
        self.inertia_ = inertia
        self.eigenvals_ = eigenvals
        self.explained_variance_ratio_ = explained_variance_ratio


ca = CA(cross_table)

print(ca.explained_variance_ratio_)

# [ 0.51057984  0.92001143  0.96850523  1.          1.        ]

# R型和Q型分析的特征向量（加权后）

F = ca.F_
G = ca.G_

print(F[:, :2])

# 绘制感知图

for i, s in enumerate(cross_table.columns):
    x, y = F[i, 0], F[i, 1]
    plt.plot(x, y, "bo")
    plt.text(x, y, s, va="bottom", ha="left", color="b")

for i, s in enumerate(cross_table.index):
    x, y = G[i, 0], G[i, 1]
    plt.plot(x, y, "r^")
    plt.text(x, y, s, va="bottom", ha="left", color="r")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
第十三讲 信息压缩

-- 第一部分 连续变量压缩

    AvgIncome 当地人均收入
    ID 员工ID
    gender 性别
    Dept 部门
    performance 绩效总分
    adaptation 适应总分
    emotion 情绪总分
"""

from sklearn.decomposition import FactorAnalysis
from sklearn.decomposition import FastICA
from sklearn import preprocessing

model_data = pd.read_csv("data/staff_performances.csv")
cc = model_data.head()
print(cc)

data = model_data.loc[:, "performance":]
cc = data.head()
print(cc)

cc = data.describe().T
print(cc)

plt.scatter(model_data["performance"], model_data["adaptation"])
plt.title("Scatter")
show()

sns.pairplot(data)
show()

# 计算相关系数矩阵

corr_matrix = data.corr(method="pearson")
# corr_matrix = corr_matrix.abs()
print(corr_matrix)

# 初次查看主成分的解释方差占比

pca = PCA(n_components=3, whiten=True)

newData = pca.fit_transform(data)

pca.explained_variance_ratio_

pca.components_

pca = PCA(n_components=1, whiten=True)

newData = pca.fit_transform(data)
print(newData.T)

# 将打分结果和原始数据联结

score = pd.DataFrame(newData)
data_new = model_data.join(score)
cc = data_new.head()
print(cc)

# data_new.sort(0)
""" 要改
/home/quant/anaconda2/lib/python2.7/site-packages/ipykernel/__main__.py:1: FutureWarning: sort(columns=....) is deprecated, use sort_values(by=.....)
  if __name__ == '__main__':
"""
# 数据标准化的方法 http://www.cnblogs.com/chaosimple/p/4153167.html

model_data = pd.read_csv("data/cities_10.csv", encoding="gbk")
cc = model_data.head()
print(cc)

data = model_data.loc[:, "X1":]
cc = data.head()
print(cc)

sns.pairplot(data)
show()

corr_matrix = data.corr(method="pearson")
# corr_matrix = corr_matrix.abs()
cc = corr_matrix
print(cc)

pca = PCA(n_components=3, whiten=True)
newData = pca.fit(data)
cc = pd.DataFrame(pca.components_).T
print(cc)

fa = FactorAnalysis(n_components=3)
newData = fa.fit(data)
cc = pd.DataFrame(fa.components_).T
print(cc)

model_data = pd.read_csv("data/profile_telecom.csv")
cc = model_data.head()
print(cc)

data = model_data.loc[:, "cnt_call":]
cc = data.head()
print(cc)

sns.pairplot(data)
show()

corr_matrix = data.corr(method="pearson")
# corr_matrix = corr_matrix.abs()
cc = corr_matrix
print(cc)

pca = PCA(n_components=3, whiten=True)
newData = pca.fit(data)
cc = pd.DataFrame(pca.components_).T
print(cc)

# 对数据进行标准化

# data_scaled = (data - np.mean(data, 0)) / (np.std(data))#归一化，因为FactorAnalysis没有white选项
data_scaled = preprocessing.scale(data + 0.0)  # 归一化，但是只能用于浮点类型变量
cc = pd.DataFrame(data_scaled).head()
print(cc)

fa = FactorAnalysis(n_components=3)
newData = fa.fit(data_scaled)
cc = pd.DataFrame(fa.components_).T
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# chapter13_2 PCA_FCA_Varselect_city10

"""
X1	GDP
X2	人均GDP
X3	工业增加值
X4	第三产业增加值
X5	固定资产投资
X6	基本建设投资
X7	社会消费品零售总额
X8	海关出口总额
X9	地方财政收入
"""
# 一、主成分分析

# 引入数据

model_data = pd.read_csv("data/cities_10.csv", encoding="gbk")
cc = model_data.head()
print(cc)

data = model_data.loc[:, "X1":]
cc = data.head()
print(cc)

# 查看相关系数矩阵，判定做变量降维的必要性（非必须）

corr_matrix = data.corr(method="pearson")

# 做主成分之前，进行中心标准化

from sklearn import preprocessing

data = preprocessing.scale(data)
# 使用sklearn的主成分分析，用于判断保留主成分的数量

"""说明：1、第一次的n_components参数应该设的大一点
   说明：2、观察explained_variance_ratio_和explained_variance_的取值变化，建议explained_variance_ratio_累积大于0.85，explained_variance_需要保留的最后一个主成分大于0.8，
"""
pca = PCA(n_components=3)
pca.fit(data)
print(pca.explained_variance_)  # 建议保留2个主成分
print(pca.explained_variance_ratio_)  # 建议保留2个主成分

pca = PCA(n_components=2).fit(data)  # 综上,2个主成分

newdata = pca.fit_transform(data)

# 通过主成分在每个变量上的权重的绝对值大小，确定每个主成分的代表性
pd.DataFrame(pca.components_).T
# 第一个主成分在第2个变量权重低,其余均高
# 第二个主成分在第2个变量权重高,其余均低
#############################################################################################
# 二、因子分析
# 因子分析的概念很多，作为刚入门的人，我们可以认为因子分析是主成分分析的延续

# pip install fa_kit

from fa_kit import FactorAnalysis
from fa_kit import plotting as fa_plotting

fa = FactorAnalysis.load_data_samples(data, preproc_demean=True, preproc_scale=True)
fa.extract_components()

# 设定提取主成分的方式。默认为“broken_stick”方法，建议使用“top_n”法

fa.find_comps_to_retain(method="top_n", num_keep=2)
# 通过最大方差法进行因子旋转

pd.DataFrame(fa.comps["rot"])  # 查看因子权重
fa.rotate_components(method="varimax")
fa_plotting.graph_summary(fa)
# - 说明：可以通过第三张图观看每个因子在每个变量上的权重，权重越高，代表性越强

# 获取因子得分

# 到目前还没有与PCA中fit_transform类似的函数，因此只能手工计算因子
# 以下是矩阵相乘的方式计算因子：因子=原始数据（n*k）*权重矩阵(k*num_keep)
fas = pd.DataFrame(fa.comps["rot"])
data = pd.DataFrame(data)  # 注意data数据需要标准化
fa_score = pd.DataFrame(np.dot(data, fas))

# 第三步：根据因子得分进行数据分析

a = fa_score.rename(columns={0: "Gross", 1: "Avg"})
citi10_fa = model_data.join(a)

# df存檔 citi10_fa.to_csv("data/citi10_fa.csv")

x = citi10_fa["Gross"]
y = citi10_fa["Avg"]
label = citi10_fa["AREA"]
plt.scatter(x, y)
for a, b, l in zip(x, y, label):
    plt.text(a, b + 0.1, "%s." % l, ha="center", va="bottom", fontsize=14)

show()


model_data = pd.read_csv("data/cities_10.csv", encoding="gbk")
cc = model_data.head()
print(cc)

data = model_data.loc[:, "X1":]

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# chapter13_3 PCA_FCA_Varselect_bank

"""
CNT_TBM 柜台交易次数	
CNT_ATM ATM机交易次数
CNT_POS POS机交易次数	
CNT_CSC 有偿服务次数

"""
# 一、主成分分析

# 引入数据

model_data = pd.read_csv("data/profile_bank.csv")
data = model_data.loc[:, "CNT_TBM":"CNT_CSC"]

# 查看相关系数矩阵，判定做变量降维的必要性（非必须）

corr_matrix = data.corr(method="pearson")
# corr_matrix = data.corr(method='spearman')

# 做主成分之前，进行中心标准化

from sklearn import preprocessing

data = preprocessing.scale(data)
# 使用sklearn的主成分分析，用于判断保留主成分的数量

"""说明：1、第一次的n_components参数应该设的大一点
   说明：2、观察explained_variance_ratio_和explained_variance_的取值变化，建议explained_variance_ratio_累积大于0.85，explained_variance_需要保留的最后一个主成分大于0.8，
"""
pca = PCA(n_components=3)
pca.fit(data)
print(pca.explained_variance_)  # 建议保留2个主成分
print(pca.explained_variance_ratio_)  # 建议保留3个主成分

pca = PCA(n_components=3).fit(data)  # 综上,2个主成分

newdata = pca.fit_transform(data)

# 通过主成分在每个变量上的权重的绝对值大小，确定每个主成分的代表性

pd.DataFrame(pca.components_).T
# 第一个主成分在第3个变量权重差不多高
# 第二个主成分在第1个变量权重高,其余均低
# 第三个主成分在第4个变量权重高,其余均低
#############################################################################################
# 二、因子分析
# 因子分析的概念很多，作为刚入门的人，我们可以认为因子分析是主成分分析的延续

from fa_kit import FactorAnalysis
from fa_kit import plotting as fa_plotting

fa = FactorAnalysis.load_data_samples(data, preproc_demean=True, preproc_scale=True)
fa.extract_components()

# 设定提取主成分的方式。默认为“broken_stick”方法，建议使用“top_n”法

fa.find_comps_to_retain(method="top_n", num_keep=3)
# 通过最大方差法进行因子旋转

pd.DataFrame(fa.comps["rot"])  # 查看因子权重
fa.rotate_components(method="varimax")
fa_plotting.graph_summary(fa)
# - 说明：可以通过第三张图观看每个因子在每个变量上的权重，权重越高，代表性越强

# 获取因子得分

# 到目前还没有与PCA中fit_transform类似的函数，因此只能手工计算因子
# 以下是矩阵相乘的方式计算因子：因子=原始数据（n*k）*权重矩阵(k*num_keep)
fas = pd.DataFrame(fa.comps["rot"])
data = pd.DataFrame(data)  # 注意data数据需要标准化
fa_score = pd.DataFrame(np.dot(data, fas))

# 第三步：根据因子得分进行数据分析

a = fa_score.rename(columns={0: "Gross", 1: "Avg"})
profile_bank_fa = model_data.join(a)

model_data = pd.read_csv("data/profile_bank.csv")
data = model_data.loc[:, "CNT_TBM":"CNT_CSC"]

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

model_data = pd.read_csv("data/creditcard_exp.csv")
cc = model_data.head()
print(cc)

data = model_data.loc[:, "gender":]

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# varselect_bank

model_data = pd.read_csv("data/profile_bank.csv")
data = model_data.loc[:, "CNT_TBM":"CNT_CSC"]
k = 3
alphaMax = 5
alphastep = 0.2

from sklearn import preprocessing
from sklearn.decomposition import SparsePCA
from functools import reduce

data = preprocessing.scale(data)
n_components = k
pca_n = list()

pca_model = SparsePCA(n_components=n_components, alpha=5)
pca_model.fit(data)

pca = pd.DataFrame(pca_model.components_).T

n = data.shape[1] - sum(sum(np.array(pca != 0)))

best_alpha = 5
pca_model = SparsePCA(n_components=n_components, alpha=best_alpha)
pca_model.fit(data)
pca = pd.DataFrame(pca_model.components_).T
data = pd.DataFrame(data)

score = pd.DataFrame(pca_model.fit_transform(data))

r = []
R_square = []
for xk in range(data.shape[1]):  # xk输入变量个数
    for paj in range(n_components):  # paj主成分个数
        r.append(abs(np.corrcoef(data.iloc[:, xk], score.iloc[:, paj])[0, 1]))
        r_max1 = max(r)
        r.remove(r_max1)
        r.append(-2)
        r_max2 = max(r)
        R_square.append((1 - r_max1**2) / (1 - r_max2**2))

R = abs(pd.DataFrame(np.array(r).reshape((data.shape[1], n_components))))
R_square = abs(pd.DataFrame(np.array(R_square).reshape((data.shape[1], n_components))))
var_list = []
# print(R_square)

for i in range(n_components):
    vmin = R_square[i].min()
    print(R_square[i])
    print(vmin)
    print(R_square[R_square[i] == min][i])
    var_list.append(R_square[R_square[i] == vmin][i].index[0])

news_ids = []
for id in var_list:
    if id not in news_ids:
        news_ids.append(id)
print(news_ids)
orgdata = model_data.loc[:, "CNT_TBM":"CNT_CSC"]
data_vc = orgdata.iloc[:, np.array(news_ids).reshape(len(news_ids))]

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 第十四讲 聚类
# 1、层次聚类

import scipy
import scipy.cluster.hierarchy as sch
from scipy.cluster.vq import vq, kmeans, whiten
from sklearn import metrics
from sklearn import preprocessing
from sklearn import cluster

print("------------------------------------------------------------")  # 60個

orgData = pd.read_csv("data/cities_10.csv", index_col="AREA", encoding="gbk")
cc = orgData.head()
print(cc)

# orgData.describe()

# 标准化
x_scaled = preprocessing.scale(orgData + 0.0)  # 归一化，但是只能用于浮点类型变量
cc = pd.DataFrame(x_scaled).head()
print(cc)

# 变量压缩
pca = PCA(n_components=2)
newData = pca.fit_transform(x_scaled)

cc = pca.explained_variance_ratio_
print(cc)

print(newData)

# 1. 层次聚类
# 生成点与点之间的距离矩阵,这里用的欧氏距离:
disMat = sch.distance.pdist(newData, "euclidean")
# 进行层次聚类:
Z = sch.linkage(disMat, method="average")
# 将层级聚类结果以树状图表示出来并保存为plot_dendrogram.png
P = sch.dendrogram(Z)
# 存檔 plt.savefig('tmp_plot_dendrogram1.png')

# 2、K-means聚类

iris = pd.read_csv("data/iris_one_book.csv")
x = iris.loc[:, "Sepal.Length":"Petal.Width"]
y = iris["Species"]

# 归一化的使用说明 http://www.cnblogs.com/chaosimple/p/4153167.html

x_scaled = preprocessing.scale(x + 0.0)  # 归一化，但是只能用于浮点类型变量
cc = pd.DataFrame(x_scaled).head()
print(cc)

pca = PCA(n_components=3)
newData = pca.fit_transform(x_scaled)

cc = pca.explained_variance_ratio_
print(cc)

score = pd.DataFrame(newData)
cc = score.head()
print(cc)

# http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans

from sklearn.cluster import KMeans

kmeans = cluster.KMeans(n_clusters=3)  # MiniBatchKMeans()分批处理
# kmeans = cluster.KMeans(n_clusters=3, init='random', n_init=1)
result = kmeans.fit(x_scaled)
print(result)

cc = result.labels_
print(cc)

lo = plt.scatter(
    score[0][result.labels_ == 0], score[1][result.labels_ == 0], marker="x"
)
lo = plt.scatter(
    score[0][result.labels_ == 1], score[1][result.labels_ == 1], marker="o"
)
lo = plt.scatter(
    score[0][result.labels_ == 2], score[1][result.labels_ == 2], marker="+"
)

# 聚类效果评估
# Silhouette Coefficient
# http://scikit-learn.org/stable/modules/clustering.html#clustering

# 計算輪廓分數
cc = metrics.silhouette_score(x_scaled, result.labels_, metric="euclidean")
# print("分", CLUSTERS, "群, 計算輪廓分數:", cc)
print("計算輪廓分數:", cc)

# Adjusted Rand index
# http://scikit-learn.org/stable/modules/clustering.html#clustering

cc = metrics.adjusted_rand_score(y, result.labels_)
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# chapter14_1 Hclus_FCA_city10.py

# 第十四讲 聚类

# 层次聚类

# 第一步：手动测试主成分数量

model_data = pd.read_csv("data/cities_10.csv", encoding="gbk")
cc = model_data.head()
print(cc)

data = model_data.loc[:, "X1":]
cc = data.head()
print(cc)

# 查看相关系数矩阵，判定做变量降维的必要性（非必须）

corr_matrix = data.corr(method="pearson")
# corr_matrix = corr_matrix.abs()
corr_matrix

# 做主成分之前，进行中心标准化

from sklearn import preprocessing

data = preprocessing.scale(data)

# 使用sklearn的主成分分析，用于判断保留主成分的数量

# 说明：1、第一次的n_components参数应该设的大一点
# 说明：2、观察explained_variance_ratio_和explained_variance_的取值变化，建议explained_variance_ratio_累积大于0.85，explained_variance_需要保留的最后一个主成分大于0.8，

pca = PCA(n_components=3)
newData = pca.fit(data)
print(pca.explained_variance_)
print(pca.explained_variance_ratio_)

# 第二步：根据主成分分析确定需要保留的主成分数量，进行因子分析

# 导入包，并对输入的数据进行主成分提取。为保险起见，data需要进行中心标准化

from fa_kit import FactorAnalysis
from fa_kit import plotting as fa_plotting

fa = FactorAnalysis.load_data_samples(data, preproc_demean=True, preproc_scale=True)
fa.extract_components()

# 设定提取主成分的方式。默认为“broken_stick”方法，建议使用“top_n”法

fa.find_comps_to_retain(method="top_n", num_keep=2)

# 通过最大方差法进行因子旋转

fa.rotate_components(method="varimax")
fa_plotting.graph_summary(fa)

# 说明：可以通过第三张图观看每个因子在每个变量上的权重，权重越高，代表性越强

# 获取因子得分

pd.DataFrame(fa.comps["rot"])

fas = pd.DataFrame(fa.comps["rot"])
data = pd.DataFrame(data)
score = pd.DataFrame(np.dot(data, fas))

# 第三步：根据因子得分进行数据分析

a = score.rename(columns={0: "Gross", 1: "Avg"})
citi10_fa = model_data.join(a)

# df存檔 citi10_fa.to_csv("data/citi10_fa.csv")

x = citi10_fa["Gross"]
y = citi10_fa["Avg"]
label = citi10_fa["AREA"]
plt.scatter(x, y)
for a, b, l in zip(x, y, label):
    plt.text(a, b + 0.1, "%s." % l, ha="center", va="bottom", fontsize=14)

show()

import scipy.cluster.hierarchy as sch

# 1. 层次聚类
# 生成点与点之间的距离矩阵,这里用的欧氏距离:
disMat = sch.distance.pdist(citi10_fa[["Gross", "Avg"]], "euclidean")
# 进行层次聚类:
Z = sch.linkage(disMat, method="ward")
# 将层级聚类结果以树状图表示出来并保存为plot_dendrogram.png
P = sch.dendrogram(
    Z, labels=["辽宁", "山东", "河北", "天津", "江苏", "上海", "浙江", "福建", "广东", "广西"]
)
# 存檔 plt.savefig('tmp_plot_dendrogram2.png')

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Kmeans_FA_bank.py

# K-means聚类分析

# 手动测试主成分数量

model_data = pd.read_csv("data/profile_bank.csv")
data = model_data.loc[:, "CNT_TBM":"CNT_CSC"]
cc = data.head()
print(cc)

# 查看相关系数矩阵，判定做变量降维的必要性（非必须）

corr_matrix = data.corr(method="pearson")
# corr_matrix = corr_matrix.abs()
corr_matrix

# 做主成分之前，进行中心标准化

from sklearn import preprocessing

data = preprocessing.scale(data)

# 使用sklearn的主成分分析，用于判断保留主成分的数量

# 说明：1、第一次的n_components参数应该设的大一点
# 说明：2、观察explained_variance_ratio_和explained_variance_的取值变化，建议explained_variance_ratio_累积大于0.85，explained_variance_需要保留的最后一个主成分大于0.8，

pca = PCA(n_components=3)
newData = pca.fit(data)
print(pca.explained_variance_)
print(pca.explained_variance_ratio_)

# 通过主成分在每个变量上的权重的绝对值大小，确定每个主成分的代表性

pd.DataFrame(pca.components_).T

# 第二步：根据主成分分析确定需要保留的主成分数量，进行因子分析

# 导入包，并对输入的数据进行主成分提取。为保险起见，data需要进行中心标准化

from fa_kit import FactorAnalysis
from fa_kit import plotting as fa_plotting

fa = FactorAnalysis.load_data_samples(data, preproc_demean=True, preproc_scale=True)
fa.extract_components()

# 设定提取主成分的方式。默认为“broken_stick”方法，建议使用“top_n”法

fa.find_comps_to_retain(method="top_n", num_keep=3)

# 通过最大方差法进行因子旋转

fa.rotate_components(method="varimax")
fa_plotting.graph_summary(fa)

# 说明：可以通过第三张图观看每个因子在每个变量上的权重，权重越高，代表性越强

# 获取因子得分

pd.DataFrame(fa.comps["rot"])

fas = pd.DataFrame(fa.comps["rot"])
data = pd.DataFrame(data)
score = pd.DataFrame(np.dot(data, fas))

# 第三步：根据因子得分进行数据分析

fa_scores = score.rename(columns={0: "ATM_POS", 1: "TBM", 2: "CSC"})
cc = fa_scores.head()
print(cc)

# 第四步：使用因子得分进行k-means聚类

# k-means聚类的第一种方式：不进行变量分布的正态转换--用于寻找异常值

# 查看变量的偏度

var = ["ATM_POS", "TBM", "CSC"]
skew_var = {}
for i in var:
    skew_var[i] = abs(fa_scores[i].skew())
    skew = pd.Series(skew_var).sort_values(ascending=False)
skew

# 进行k-means聚类

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=3)  # MiniBatchKMeans()分批处理
# kmeans = cluster.KMeans(n_clusters=3, init='random', n_init=1)
result = kmeans.fit(fa_scores)
# print(result)

# 对分类结果进行解读

model_data_l = model_data.join(pd.DataFrame(result.labels_))
model_data_l = model_data_l.rename(columns={0: "clustor"})
cc = model_data_l.head()
print(cc)

import matplotlib

# get_ipython().magic('matplotlib inline')
model_data_l.clustor.value_counts().plot(kind="pie")
show()

# k-means聚类的第二种方式：进行变量分布的正态转换--用于客户细分

# 进行变量分布的正态转换

from sklearn import preprocessing

quantile_transformer = preprocessing.QuantileTransformer(
    output_distribution="normal", random_state=0
)
fa_scores_trans = quantile_transformer.fit_transform(fa_scores)
fa_scores_trans = pd.DataFrame(fa_scores_trans)
fa_scores_trans = fa_scores_trans.rename(columns={0: "ATM_POS", 1: "TBM", 2: "CSC"})
cc = fa_scores_trans.head()
print(cc)

var = ["ATM_POS", "TBM", "CSC"]
skew_var = {}
for i in var:
    skew_var[i] = abs(fa_scores_trans[i].skew())
    skew = pd.Series(skew_var).sort_values(ascending=False)
skew

# 进行k-means聚类

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=3)  # MiniBatchKMeans()分批处理
# kmeans = cluster.KMeans(n_clusters=3, init='random', n_init=1)
result = kmeans.fit(fa_scores_trans)
# print(result)

# 对分类结果进行解读

model_data_l = model_data.join(pd.DataFrame(result.labels_))
model_data_l = model_data_l.rename(columns={0: "clustor"})
cc = model_data_l.head()
print(cc)

import matplotlib

# get_ipython().magic('matplotlib inline')
model_data_l.clustor.value_counts().plot(kind="pie")
show()

from sklearn import tree

clf = tree.DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,
    min_samples_split=100,
    min_samples_leaf=100,
    random_state=12345,
)  # 当前支持计算信息增益和GINI
clf.fit(model_data, result.labels_)

import pydotplus
from IPython.display import Image  # 用IPython
import sklearn.tree as tree

# 決策樹可視化存檔
dot_data = tree.export_graphviz(
    clf,
    out_file=None,
    feature_names=model_data.columns,
    class_names=["0", "1", "2"],
    filled=True,
)

graph = pydotplus.graph_from_dot_data(dot_data)
# Image(graph.create_png())   # 用IPython顯示圖片

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


from sklearn import (
    manifold,
    datasets,
    decomposition,
    ensemble,
    discriminant_analysis,
    random_projection,
    neighbors,
)


# PCA結果參數
print(pca.explained_variance_)  # 建议保留9个主成分
print(pca.explained_variance_ratio_)  # 建议保留8个主成分


print("------------------------------------------------------------")  # 60個

n_samples = 100
experience = np.random.normal(size=n_samples)
salary = 1500 + experience + np.random.normal(size=n_samples, scale=0.5)
X = np.column_stack([experience, salary])

X = np.column_stack([experience, salary])

n_components = 2  # 降維後的維度
clf = PCA(n_components=n_components)

clf.fit(X)

print("主成分的方差比例 explained_variance_ratio_")
print(clf.explained_variance_ratio_)


R2 = clf.fit_transform(A)  # .fit + .transform一起做
print(R2)
print(clf.inverse_transform(R2))

ax = plt.gca()  # gca 代表當前坐標軸，即 'get current axis'
