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
    # plt.show()
    pass

'''
print(__doc__)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("PCA 降維度, 4維 => 2維")

N = 500  # 散點的數量

X = np.random.randint(0, 100, size=(N, 4))  # 產生 N x 4 陣列，內容為 0～100 隨機數字

n_components = 2  # 降維後的維度

clf = PCA(n_components=n_components)

clf = clf.fit(X)
X2 = clf.transform(X)

print("轉換前 4維 :", X.shape)
print("轉換後 2維 :", X2.shape)

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


class BasicPCA:
    def fit(self, X):
        # U : Unitary matrix having left singular vectors as columns.
        #     Of shape (n_samples,n_samples) or (n_samples,n_comps), depending on
        #     full_matrices.
        #
        # s : The singular values, sorted in non-increasing order. Of shape (n_comps,),
        #     with n_comps = min(n_samples, n_features).
        #
        # Vh: Unitary matrix having right singular vectors as rows.
        #     Of shape (n_features, n_features) or (n_comps, n_features) depending on full_matrices.
        self.mean = X.mean(axis=0)
        Xc = X - self.mean  # Centering is required
        U, s, V = scipy.linalg.svd(Xc, full_matrices=False)
        self.explained_variance_ = (s**2) / X.shape[0]
        self.explained_variance_ratio_ = (
            self.explained_variance_ / self.explained_variance_.sum()
        )
        self.princ_comp_dir = V

    def transform(self, X):
        Xc = X - self.mean
        return np.dot(Xc, self.princ_comp_dir.T)


# 1. 自建資料 做 PCA
# dataset
n_samples = 100
experience = np.random.normal(size=n_samples)
salary = 1500 + experience + np.random.normal(size=n_samples, scale=0.5)
X = np.column_stack([experience, salary])

X = np.column_stack([experience, salary])

n_components = 2  # 降維後的維度
clf = PCA(n_components=n_components)

clf.fit(X)

basic_pca = BasicPCA()

basic_pca.fit(X)

print("主成分的方差比例 explained_variance_ratio_")
print(clf.explained_variance_ratio_)
# assert np.all(basic_pca.transform(X) == clf.transform(X))


# 2. 使用iris資料 做 PCA

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

print("PCA 算法模擬")

A = np.array([[3, 2000], [2, 3000], [4, 5000], [5, 8000], [1, 2000]], dtype="float")

# 數據歸一化
mean = np.mean(A, axis=0)
norm = A - mean
# 數據縮放
scope = np.max(norm, axis=0) - np.min(norm, axis=0)
norm = norm / scope
print(norm)

U, S, V = np.linalg.svd(np.dot(norm.T, norm))
print(U)

U_reduce = U[:, 0].reshape(2, 1)
print(U_reduce)

R = np.dot(norm, U_reduce)
print(R)

Z = np.dot(R, U_reduce.T)
print(Z)

print(np.multiply(Z, scope) + mean)

print("------------------------------")  # 30個

print("使用 sklearn 包實現")

from sklearn.pipeline import Pipeline


def std_PCA(**argv):
    scaler = MinMaxScaler()
    clf = PCA(**argv)
    pipeline = Pipeline([("scaler", scaler), ("pca", clf)])
    return pipeline


n_components = 1  # 降維後的維度
clf = std_PCA(n_components=n_components)
R2 = clf.fit_transform(A)  # .fit + .transform一起做
print(R2)

print(clf.inverse_transform(R2))

print("------------------------------")  # 30個

print("降維及恢復示意圖")

plt.figure(figsize=(8, 8))

plt.title("Physcial meanings of PCA")

ymin = xmin = -1
ymax = xmax = 1
plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)
ax = plt.gca()  # gca 代表當前坐標軸，即 'get current axis'
ax.spines["right"].set_color("none")  # 隱藏坐標軸
ax.spines["top"].set_color("none")

plt.scatter(norm[:, 0], norm[:, 1], marker="s", c="b")
plt.scatter(Z[:, 0], Z[:, 1], marker="o", c="r")
plt.arrow(0, 0, U[0][0], U[1][0], color="r", linestyle="-")
plt.arrow(0, 0, U[0][1], U[1][1], color="r", linestyle="--")
plt.annotate(
    r"$U_{reduce} = u^{(1)}$",
    xy=(U[0][0], U[1][0]),
    xycoords="data",
    xytext=(U_reduce[0][0] + 0.2, U_reduce[1][0] - 0.1),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)
plt.annotate(
    r"$u^{(2)}$",
    xy=(U[0][1], U[1][1]),
    xycoords="data",
    xytext=(U[0][1] + 0.2, U[1][1] - 0.1),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)
plt.annotate(
    r"raw data",
    xy=(norm[0][0], norm[0][1]),
    xycoords="data",
    xytext=(norm[0][0] + 0.2, norm[0][1] - 0.2),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)
plt.annotate(
    r"projected data",
    xy=(Z[0][0], Z[0][1]),
    xycoords="data",
    xytext=(Z[0][0] + 0.2, Z[0][1] - 0.1),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
'''
# 實現PCA演算法

# 建立測試資料

# 固定隨機種子
np.random.seed(2342347)

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

np.random.seed(10)
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

# 特徵縮放
scaler = MinMaxScaler()
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
).fit_transform(X)  # .fit + .transform一起做

for i in range(3):
    plt.scatter(X_embedded[i * 50 : (i + 1) * 50], np.zeros(50), c=colors[i])
show()


perplexity = 130
X_embedded = TSNE(
    n_components=1, perplexity=perplexity, learning_rate="auto", init="random"
).fit_transform(X)  # .fit + .transform一起做

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

scaler = StandardScaler()

X = df.drop("Class", axis=1)
y = df["Class"]

X = scaler.fit_transform(X)  # .fit + .transform一起做

dfx = pd.DataFrame(data=X, columns=df.columns[1:])

cc = dfx.head()
print(cc)

cc = dfx.describe()
print(cc)

# PCA class import and analysis

from sklearn.decomposition import PCA

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
