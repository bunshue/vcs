"""
高斯混合模型(Gaussian Mixture Models, GMM)，它可以被視為k-means的延伸，將資料做更正確的聚類。

高斯混合模型顧名思義它就是混合了多（K）個高斯機率密度函數來近似我們的目標機率密度函數
差在說 GMM 是透過調整各（K）個高斯分布的 mean 跟 variance 並給予它們不同的權重（weights）
來實現 approach 這件事。

GaussianMixture
class sklearn.mixture.GaussianMixture(n_components=1, *, covariance_type='full', tol=0.001,
reg_covar=1e-06, max_iter=100, n_init=1, init_params='kmeans',
weights_init=None, means_init=None, precisions_init=None,
random_state=None, warm_start=False, verbose=0, verbose_interval=10)

GaussianMixture
参量
n_components	混合高斯模型个数，默认为 1
covariance_type
协方差类型，{‘full’,‘tied’, ‘diag’, ‘spherical’}
full 指每个分量有各自不同的标准协方差矩阵，完全协方差矩阵（元素都不为零）
tied 指所有分量有相同的标准协方差矩阵（HMM 会用到）
diag 指每个分量有各自不同对角协方差矩阵（非对角为零，对角不为零）
spherical 指每个分量有各自不同的简单协方差矩阵，球面协方差矩阵（非对角为零，对角完全相同，球面特性），默认‘full’ 完全协方差矩阵

tol		EM 迭代停止阈值，默认为 1e-3 即 0.001.
reg_covar	协方差对角非负正则化，保证协方差矩阵均为正，默认为 0
max_iter	最大迭代次数，默认 100
n_init		初始化次数，用于产生最佳初始参数，默认为 1
init_params	初始化参数类型 {‘kmeans’, ‘random’}
初始化参数实现方式，默认用 kmeans 实现，也可以选择随机产生
weights_init	各组成模型的先验权重，可以自己设，默认按照 init_params 产生
means_init	初始化均值，同 weights_init
precisions_init	初始化精确度（模型个数，特征个数），默认按照 init_params 实现
random_state	随机数发生器
warm_start	若为 True，则 fit（）调用会以上一次 fit（）的结果作为初始化参数，适合相同问题多次 fit 的情况，能加速收敛，默认为 False。
verbose		使能迭代信息显示，默认为 0，可以为 1 或者大于 1（显示的信息不同）
verbose_interval	与 verbose 挂钩，若使能迭代信息显示，设置多少次迭代后显示信息，默认 10 次。

属性
weights_ : array, shape (n_components,)
This attribute stores the mixing weights for each mixture component.
每个混合模型的权重。
means_ : array, shape (n_components, n_features)
Mean parameters for each mixture component.
每个混合模型的均值。
covars_ : array
Covariance parameters for each mixture component. The shape depends on covariance_type:
每个混合模型的协方差。矩阵大小取决于covariance_type定义的协方差矩阵类型
converged_ : bool
True when convergence was reached in fit(), False otherwise.
当在fit()中达到收敛时为真，否则为假。

函数
1. aic(X) Akaike information criterion for the current model on the input X.
输入 X 上当前模型的 aic（X）Akaike 信息标准。
2. bic(X) Bayesian information criterion for the current model on the input X.　　　　　　　　
输入 X 上当前模型的 bic（X）贝叶斯信息准则。
3. fit(X[, y]) Estimate model parameters with the EM algorithm.　　　　　　　　　　　　　　
fit（X [，y]）使用 EM 算法估算模型参数。
4. get_params([deep]) Get parameters for this estimator.　　　　　　　　　　　　　　　　
get_params（[deep]）获取此估算器的参数。
5. predict(X) Predict the labels for the data samples in X using trained model.　　　　　　　　
预测（X）使用训练模型预测 X 中数据样本的标签。
6. predict_proba(X) Predict posterior probability of each component given the data.　　　　　　
predict_proba（X）预测给定数据的每个组件的后验概率。
7. sample([n_samples]) Generate random samples from the fitted Gaussian distribution.　　　　
sample（[n_samples]）从拟合的高斯分布生成随机样本。
8. score(X[, y]) Compute the per-sample average log-likelihood of the given data X.　　　　
得分（X [，y]）计算给定数据 X 的每样本平均对数似然。
9. score_samples(X) Compute the weighted log probabilities for each sample.　　　　　　
score_samples（X）计算每个样本的加权对数概率。
10. set_params( ** params) Set the parameters of this estimator.　　　　　　　　　　　　　　
set_params（**params）设置此估算器的参数。
"""

"""
GaussianMixture类中的covariance_type参数可以选择不同的协方差矩阵类型，
包括'full'、'tied'、'diag'和'spherical'等，
分别表示完全协方差矩阵、共享协方差矩阵、对角协方差矩阵和球形协方差矩阵。
"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import re
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

import tensorflow as tf
from sklearn import datasets
from sklearn import preprocessing
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn.preprocessing import StandardScaler  # 用於標準化數據，即將數據轉換為均值為0，方差為1的分佈。
from tensorflow.keras.callbacks import TensorBoard
from tensorflow.keras.models import model_from_json
from sklearn.metrics import accuracy_score
from sklearn.decomposition import NMF
from sklearn.cluster import KMeans  # K均值聚類分析


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個

from sklearn.mixture import GaussianMixture

import warnings

warnings.filterwarnings("ignore")

print("------------------------------------------------------------")  # 60個

X = np.array([[1, 2], [1, 4], [1, 0], [10, 2], [10, 4], [10, 0]])

N_COMPONENTS = 2  # 要分成的群數
print("使用GaussianMixture分成", N_COMPONENTS, "群")
gmm = GaussianMixture(n_components=N_COMPONENTS, random_state=9487)
gmm.fit(X)  # 學習訓練.fit

print(X.shape)

print("GaussianMixture訓練後結果 :(打印模型參數)")

print("各群的平均 / 群集中心")
print(gmm.means_)  # 各 Gauss 分布の平均
print("各群的分散數 / covariances")
print(gmm.covariances_)  # 各 Gauss 分布の分散
print("weights:", gmm.weights_)
print(gmm.weights_)
print("是否達到收斂?", gmm.converged_)
print("遞迴次數 :", gmm.n_iter_)

y_pred = gmm.predict([[0, 0], [12, 3]])
print("預測結果 :\n", y_pred, sep="")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

N = 100
mu1, sigma1 = 0, 4
mu2, sigma2 = 5, 4
x1 = np.random.normal(mu1, sigma1, size=(N, 2))
x2 = np.random.normal(mu2, sigma2, size=(N, 2))

X = np.concatenate([x1, x2], axis=0)

plt.subplot(221)
plt.hist(X, bins=100, alpha=0.6)

plt.subplot(222)
# plt.scatter(X[:, 0], X[:, 1], c='r')
plt.scatter(x1[:, 0], x1[:, 1], c="r")
plt.scatter(x2[:, 0], x2[:, 1], c="g")

# 构建GMM模型
N_COMPONENTS = 3  # 要分成的群數
print("使用GaussianMixture分成", N_COMPONENTS, "群")
gmm = GaussianMixture(n_components=N_COMPONENTS, covariance_type="full")

gmm.fit(X)  # 學習訓練.fit

y_pred = gmm.predict(X)
print("預測結果 :\n", y_pred, sep="")

plt.subplot(223)
plt.hist(y_pred, bins=100, alpha=0.6)

plt.subplot(224)
plt.scatter(X[:, 0], X[:, 1], c=y_pred)

# 標記群集中心
plt.scatter(
    gmm.means_[:, 0],
    gmm.means_[:, 1],
    marker="*",
    s=200,
    c="r",
    alpha=0.8,
)

plt.show()

xpdf = np.linspace(-10, 10, 100).reshape(-1, 2)
print(type(xpdf))
print(xpdf)
print(xpdf.shape)

cc = gmm.score_samples(xpdf)
print(cc)

density = np.exp(gmm.score_samples(xpdf))

# plt.hist(X, 80, alpha=0.5)
plt.plot(xpdf, density, "-r")
plt.xlim(-10, 20)
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

iris = datasets.load_iris()
X = iris.data
y = iris.target  # 資料集目標

N_COMPONENTS = 3  # 要分成的群數
print("使用GaussianMixture分成", N_COMPONENTS, "群")
gmm = GaussianMixture(n_components=N_COMPONENTS)

gmm.fit(X)  # 學習訓練.fit

y_pred = gmm.predict(X)
print("預測結果 :\n", y_pred, sep="")

plt.subplot(211)
plt.scatter(X[:, 0], X[:, 1], c=y)

plt.subplot(212)
plt.scatter(X[:, 0], X[:, 1], c=y_pred)

# 標記群集中心
plt.scatter(
    gmm.means_[:, 0],
    gmm.means_[:, 1],
    marker="*",
    s=200,
    c="r",
    alpha=0.8,
)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
Mall Customer Segmentation Data
資料集的資料包括：
客戶 ID
性別
年齡
年收入
花費指數

Mall_Customers.csv 200筆資料 5欄位
CustomerID,Genre,Age,Annual Income (k$),Spending Score (1-100)
0001,Male,19,15,39
0002,Male,21,15,81
0003,Female,20,16,6
0004,Female,23,16,77
0005,Female,31,17,40
0006,Female,22,17,76
0007,Female,35,18,6
0008,Female,23,18,94
0009,Male,64,19,3
"""

"""
讀取資料集並適當地重新命名列名
刪除 customerid 列，並將 Gender 列轉換為 [0,1]
使用 sklearn 的 StandardScaler() 對資料集進行標準化
使用高斯混合模型進行分群
"""

df = pd.read_csv("data/Mall_Customers.csv")

# cleaning/renaming column names
df.rename(
    columns={
        "Annual Income (k$)": "AnnualIncome(k$)",
        "Spending Score (1-100)": "SpendingScore(1-100)",
    },
    inplace=True,
)

# Dropping CustomerID column
df.drop(["CustomerID"], inplace=True, axis=1)

# Transforming Gender
df.Gender[df.Gender == "Male"] = 1
df.Gender[df.Gender == "Female"] = 0

df["age_cat"] = pd.cut(
    df["Age"],
    bins=[0, 35, 55, 100],  # Else devise your bins: [0,20,60,110]
    labels=["y", "m", "s"],
)

df["income_cat"] = pd.cut(df["AnnualIncome(k$)"], bins=3, labels=["l", "m", "h"])
"""
首先，使用 rename 方法，將資料框（DataFrame）的某些列名進行了重新命名。
接著，使用 drop 方法，刪除了資料框中的 "CustomerID" 這一列。這樣做的目的是去除不需要的客戶ID資訊。
同時，也對 "Gender" 這一列進行了轉換，將男性表示為1，女性表示為0。
接著使用 cut 方法，將 "Age" 這一列數值型特徵進行了分類。
將年齡區間劃分為三個類別：'y'（年輕）、'm'（中年）、's'（老年），並將結果存儲在新的 "age_cat" 列中。
最後，再次使用 cut 方法，這次是對 "AnnualIncome(k$)" 這一列進行分類。
它將年收入區間分為三個類別：'l'（低收入）、'm'（中等收入）、'h'（高收入），並將結果存儲在新的 "income_cat" 列中。
"""
# Scale dataset
# Drop Categorical Values
df.drop(columns=["age_cat", "income_cat"], inplace=True)

# Scaling using StandardScaler
ss = StandardScaler()
ss.fit(df)
X = ss.transform(df)
"""
先從資料框（DataFrame）中刪除名為 'age_cat' 和 'income_cat' 的列，這些列可能包含類別值或非數值資料。

接下來，使用 sklearn 中的 StandardScaler() 對剩餘的數值列進行標準化，將資料縮放為均值為0，標準差為1的標準分佈，並將標準化後的資料存儲在變數 X 中，以供後續的機器學習或統計分析使用。
"""
# Gaussian Mixture Modeling
# Perform clsutering

N_COMPONENTS = 2  # 要分成的群數
print("使用GaussianMixture分成", N_COMPONENTS, "群")
gmm = GaussianMixture(n_components=N_COMPONENTS, n_init=10, max_iter=100)

gmm.fit(X)  # 學習訓練.fit

y_pred = gmm.predict(X)
print("預測結果 :\n", y_pred, sep="")
"""
最後，我們使用高斯混合模型 (Gaussian Mixture Model, GMM) 來進行資料分群，
並用已經訓練好的模型對資料集 X 進行預測。
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Display multiple outputs from a jupyter cell
from IPython.core.interactiveshell import InteractiveShell

InteractiveShell.ast_node_interactivity = "all"
# Set numpy options to display wide array
np.set_printoptions(
    precision=3, threshold=np.inf  # Display upto 3 decimal places  # Display full array
)
# Seting display options
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", 100)

# Load Dataset
# Reading dataset
df = pd.read_csv("data/Mall_Customers.csv")

# Data Preprocess
# cleaning/renaming column names
df.rename(
    columns={
        "Annual Income (k$)": "AnnualIncome(k$)",
        "Spending Score (1-100)": "SpendingScore(1-100)",
    },
    inplace=True,
)
cc = df.head()
print(cc)

# Dropping CustomerID column
df.drop(["CustomerID"], inplace=True, axis=1)
# Transforming Gender
# pd.Series(np.where(df.Gender.values == 'Male', 1, 0, inplace = True))
df.Gender[df.Gender == "Male"] = 1
df.Gender[df.Gender == "Female"] = 0
# df.Gender.map(dict(Male=1, Female=0))
df["age_cat"] = pd.cut(
    df["Age"],
    bins=[0, 35, 55, 100],  # Else devise your bins: [0,20,60,110]
    labels=["y", "m", "s"],
)
df["income_cat"] = pd.cut(df["AnnualIncome(k$)"], bins=3, labels=["l", "m", "h"])
cc = df.head()
print(cc)

# Scale dataset
# Drop Categorical Values
df.drop(columns=["age_cat", "income_cat"], inplace=True)
# Scaling using StandardScaler
ss = StandardScaler()
ss.fit(df)
X = ss.transform(df)
# StandardScaler()

N_COMPONENTS = 2  # 要分成的群數
print("使用GaussianMixture分成", N_COMPONENTS, "群")
gmm = GaussianMixture(n_components=N_COMPONENTS, n_init=10, max_iter=100)
gmm.fit(X)  # 學習訓練.fit

# GaussianMixture(n_components=2, n_init=10)

y_pred = gmm.predict(X)
print("預測結果 :\n", y_pred, sep="")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

sns.set()

# 正如剛開始說的，可以查看上圖黃色的數據及紫色的資料數據，位置極為接近，很難將資料做正確的分群

from sklearn.datasets import make_blobs  # 集群資料集

N = 400  # n_samples, 樣本數
M = 2  # n_features, 特徵數(資料的維度)
GROUPS = 4  # centers, 分群數
STD = 0.60  # cluster_std, 資料標準差
print("make_blobs,", N, "個樣本, ", M, "個特徵, 分成", GROUPS, "群")

X, y_true = make_blobs(n_samples=N, centers=GROUPS, cluster_std=STD)

X = X[:, ::-1]

CLUSTERS = 4  # 要分成的群數
print("使用KMeans分成", CLUSTERS, "群")
kmeans = KMeans(CLUSTERS)
labels = kmeans.fit(X).predict(X)  # 學習訓練.fit+預測
plt.scatter(X[:, 0], X[:, 1], c=labels, s=40, cmap="viridis")
show()

# 因此，若是可以以中心點繪製一個圓圈，中心點與資料向量的距離最遠為圓的半徑，如果資料點分布在圓圈外，代表該資料點不為任何群集的資料

from scipy.spatial.distance import cdist


def plot_kmeans(kmeans, X, n_clusters=4, rseed=0, ax=None):
    labels = kmeans.fit_predict(X)

    # plot the input data
    ax = ax or plt.gca()
    ax.axis("equal")
    ax.scatter(X[:, 0], X[:, 1], c=labels, s=40, cmap="viridis", zorder=2)

    # plot the representation of the KMeans model
    centers = kmeans.cluster_centers_
    radii = [cdist(X[labels == i], [center]).max() for i, center in enumerate(centers)]
    for c, r in zip(centers, radii):
        ax.add_patch(plt.Circle(c, r, fc="#ACACCA", lw=3, alpha=0.5, zorder=1))


CLUSTERS = 4  # 要分成的群數
print("使用KMeans分成", CLUSTERS, "群")
kmeans = KMeans(n_clusters=CLUSTERS)
plot_kmeans(kmeans, X)

# 匯入SKlearn中GMM模組，並且建立4組資料
N_COMPONENTS = 4  # 要分成的群數
print("使用GaussianMixture分成", N_COMPONENTS, "群")
gmm = GaussianMixture(n_components=N_COMPONENTS)
gmm.fit(X)  # 學習訓練.fit
labels = gmm.predict(X)
plt.scatter(X[:, 0], X[:, 1], c=labels, s=40, cmap="viridis")
show()

"""
建立一個繪製聚類圓的函數draw_ellipse，來實作聚類最大化(expectation-maximization ,EM)，
持續實作E-M步驟，重複直到收斂：
E步驟：對於每個點，找到每個聚類中成員的權重
M步驟：對於每個群集「權重」，根據所有數據點更新其位置
"""
from matplotlib.patches import Ellipse


def draw_ellipse(position, covariance, ax=None, **kwargs):
    ax = ax or plt.gca()

    # Convert covariance to principal axes
    if covariance.shape == (2, 2):
        U, s, Vt = np.linalg.svd(covariance)
        angle = np.degrees(np.arctan2(U[1, 0], U[0, 0]))
        width, height = 2 * np.sqrt(s)
    else:
        angle = 0
        width, height = 2 * np.sqrt(covariance)

    # Draw the Ellipse
    for nsig in range(1, 4):
        ax.add_patch(Ellipse(position, nsig * width, nsig * height, angle, **kwargs))


def plot_gmm(gmm, X, label=True, ax=None):
    ax = ax or plt.gca()
    labels = gmm.fit(X).predict(X)  # 學習訓練.fit + 預測
    if label:
        ax.scatter(X[:, 0], X[:, 1], c=labels, s=40, cmap="viridis", zorder=2)
    else:
        ax.scatter(X[:, 0], X[:, 1], s=40, zorder=2)
    ax.axis("equal")

    w_factor = 0.2 / gmm.weights_.max()
    for pos, covar, w in zip(gmm.means_, gmm.covariances_, gmm.weights_):
        draw_ellipse(pos, covar, alpha=w * w_factor)


N_COMPONENTS = 4  # 要分成的群數
print("使用GaussianMixture分成", N_COMPONENTS, "群")
gmm = GaussianMixture(n_components=N_COMPONENTS)

plot_gmm(gmm, X)
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 高斯混合模型(Gaussian Mixture Models)

from numpy import random
from tqdm.notebook import tqdm

# MNIST Dataset

from sklearn.datasets import load_digits

digits = load_digits()
X = digits.data / 16
y = digits.target
plt.rcParams["figure.figsize"] = (10, 10)
plt.gray()
for i in range(100):
    plt.subplot(10, 10, i + 1)
    plt.imshow(digits.images[i], cmap=plt.cm.gray, vmax=16, interpolation="nearest")
    plt.xticks(())
    plt.yticks(())
show()

# t-SNE

from scipy.spatial.distance import cdist


def Nearest_Neighbor(X, n_neighbors):
    distance = cdist(X, X, "euclidean")
    neighbors_index = np.argsort(distance, axis=1)[:, 1 : n_neighbors + 1]
    neighbors = np.sort(distance, axis=1)[:, 1 : n_neighbors + 1]
    return neighbors, neighbors_index


def _binary_search_perplexity(neighbors, neighbors_index, perplexity, verbose):
    EPSILON_DBL = 1e-8
    PERPLEXITY_TOLERANCE = 1e-5
    n_steps = 100
    n_samples, n_neighbors = neighbors.shape
    using_neighbors = n_neighbors < n_samples
    beta_sum = 0.0
    desired_entropy = math.log(perplexity)
    P = np.zeros((n_samples, n_samples), dtype=np.float64)
    for i in tqdm(range(n_samples)):
        beta_min = -np.Inf
        beta_max = np.Inf
        beta = 1.0
        for l in range(n_steps):
            sum_Pi = 0.0
            P[i, neighbors_index[i]] = np.exp(-neighbors[i] * beta)
            sum_Pi = np.sum(P[i, :])
            if sum_Pi == 0.0:
                sum_Pi = EPSILON_DBL
            P[i, :] /= sum_Pi
            sum_disti_Pi = np.sum(P[i, neighbors_index[i]] * neighbors[i])
            entropy = math.log(sum_Pi) + beta * sum_disti_Pi
            entropy_diff = entropy - desired_entropy
            if math.fabs(entropy_diff) <= PERPLEXITY_TOLERANCE:
                break
            if entropy_diff > 0.0:
                beta_min = beta
                if beta_max == np.Inf:
                    beta *= 2.0
                else:
                    beta = (beta + beta_max) / 2.0
            else:
                beta_max = beta
                if beta_min == -np.Inf:
                    beta /= 2.0
                else:
                    beta = (beta + beta_min) / 2.0
        beta_sum += beta
    return P


def PCA(X, n_components, N):
    X_center = X - np.mean(X, axis=0)
    W, D, V = np.linalg.svd(X_center.T)
    X_embedded = np.dot(X_center, W[:, :n_components])
    return X_embedded


from scipy.spatial.distance import pdist


def _kl_divergence(X_embedded, P, N, n_components):
    MACHINE_EPSILON_ARRAY = np.ones(N) * np.finfo(np.double).eps
    dist = (cdist(X_embedded, X_embedded, "euclidean") ** 2 + 1) ** -1
    Q = np.maximum(dist / np.sum(dist.ravel()), MACHINE_EPSILON_ARRAY)
    PQd = (P - Q) * dist
    grad = np.zeros(X_embedded.shape)
    for i in range(N):
        grad[i] = 4 * np.dot(PQd[i], X_embedded[i] - X_embedded)
    return grad


def gradient_descent(Y, P, gradient, max_iter, learning_rate, momentum):
    for t in tqdm(range(max_iter)):
        if t < 1:
            pre_pre_Y = Y.copy()
            Y = pre_pre_Y - learning_rate * gradient
            pre_Y = Y.copy()
        else:
            Y = pre_Y - learning_rate * gradient + momentum * (pre_Y - pre_pre_Y)
            pre_pre_Y = pre_Y.copy()
            pre_Y = Y.copy()
        gradient = _kl_divergence(Y, P, N, n_components)
    return Y


N, M = X.shape
n_neighbors = 30
n_components = 2
neighbors, neighbors_index = Nearest_Neighbor(X, n_neighbors)
early_exaggeration = 12.0
MACHINE_EPSILON = np.finfo(np.double).eps
neighbors = neighbors.reshape(N, -1)
neighbors = neighbors.astype(np.float32, copy=False)
conditional_P = _binary_search_perplexity(neighbors, neighbors_index, 30, 0)
indptr = np.linspace(0, N * n_neighbors, N + 1).astype(int)
P = conditional_P + conditional_P.T
P /= 2 * N
X_embedded = PCA(X, n_components, N)
grad = _kl_divergence(X_embedded, P, N, n_components)
Y = X_embedded.copy()
gradient = grad.copy()
max_iter = 750
learning_rate = 200
momentum = 0.2
X_sub = gradient_descent(
    Y, P * early_exaggeration, gradient, max_iter, learning_rate, momentum
)
"""
HBox(children=(IntProgress(value=0, max=1797), HTML(value='')))
HBox(children=(IntProgress(value=0, max=750), HTML(value='')))
"""

import scipy

# k-mean (initialize)
k = 10
d = 2
N = X.shape[0]
X_emb = X_sub.copy()
init_index = np.zeros(k)
k_mean = np.zeros((k, d))
for i in range(k):
    k_mean[i] = np.mean(X_emb[y == i], axis=0)
max_iter = 100
for t in range(max_iter):
    # 求歐式距離
    dist = scipy.spatial.distance.cdist(X_emb, k_mean, metric="euclidean")
    cluster_index = np.argmin(dist, axis=1)
    for i in range(k):
        BOOL = cluster_index == i
        k_mean[i] = np.mean(X_emb[BOOL], axis=0)
print(k_mean)
"""
[[-0.3116179  -6.15116405]
 [-0.5181387   1.6181603 ]
 [ 2.42447593  1.91901611]
 [ 1.65106903  0.10733067]
 [-2.23269261  1.91501257]
 [-0.23900392 -0.66208265]
 [-2.31167841 -2.55344481]
 [-0.53893996  2.98178897]
 [ 0.56721679  1.09964458]
 [ 1.21542755 -0.56525115]]
"""
# GMM
mean = k_mean.copy()
var = np.zeros((k, d, d))
for i in range(k):
    var[i] = np.diag(np.ones(d))
alpha = np.ones(k) / k
gaussian_tmp = np.zeros((k, N))
max_iter = 100
for itr in tqdm(range(max_iter)):
    for i in range(k):
        const = 1 / np.sqrt(((2 * np.pi) ** d) * np.linalg.det(var[i]))
        var_inv = np.linalg.inv(var[i])
        for j in range(N):
            gaussian_tmp[i, j] = const * np.exp(
                -0.5 * np.dot(np.dot(X_emb[j] - mean[i], var_inv), X_emb[j] - mean[i])
            )
    beta = alpha[:, None] * gaussian_tmp
    beta /= np.sum(beta, axis=0)
    sum_beta = np.sum(beta, axis=1)
    for i in range(k):
        mean[i] = np.sum(beta[i, :, None] * X_emb, axis=0) / sum_beta[i]
    for i in range(k):
        var[i] = np.dot((beta[i, :, None] * (X_emb - mean[i])).T, (X_emb - mean[i])) / (
            sum_beta[i] * d
        )
    alpha = sum_beta / N
print(alpha)
print(var[0])
"""
HBox(children=(IntProgress(value=0), HTML(value='')))
[0.09905398 0.16949675 0.10626801 0.18035446 0.10694566 0.10028305
 0.10072343 0.10729567 0.0206847  0.0088943 ]
[[ 0.05358957 -0.00084825]
 [-0.00084825  0.04330102]]
"""

# Plot

from matplotlib.patches import Ellipse

color = [
    "#FF0000",
    "#FFFF00",
    "#00FF00",
    "#00FFFF",
    "#0000FF",
    "#FF00FF",
    "#FF0088",
    "#FF8800",
    "#00FF99",
    "#7700FF",
]
plt.rcParams["figure.figsize"] = (18, 10)
fig = plt.figure()
ax = fig.add_subplot(
    111,
    xlim=(min(X_emb[:, 0]), max(X_emb[:, 0])),
    ylim=(min(X_emb[:, 1]), max(X_emb[:, 1])),
)
for i in range(0, 10):
    BOOL = y == i
    plt.scatter(X_emb[BOOL, 0], X_emb[BOOL, 1], c=color[i], label=i)
    for j in range(1, 5):
        ellipse = Ellipse(
            (mean[i, 0], mean[i, 1]),
            5 * j * var[i, 0, 0],
            5 * j * var[i, 1, 1],
            angle=math.atan(var[i, 0, 1] / var[i, 0, 0]) * 180 / np.pi,
            color=color[i],
            alpha=0.2,
        )
        ax.add_artist(ellipse)
plt.xticks([])
plt.yticks([])
plt.legend(fontsize=10)
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
1D Gaussian Mixture Example
---------------------------
Figure 4.2.

Example of a one-dimensional Gaussian mixture model with three components.
The left panel shows a histogram of the data, along with the best-fit model
for a mixture with three components. The center panel shows the model selection
criteria AIC (see Section 4.3) and BIC (see Section 5.4) as a function of the
number of components. Both are minimized for a three-component model. The
right panel shows the probability that a given point is drawn from each class
as a function of its position. For a given x value, the vertical extent of
each region is proportional to that probability. Note that extreme values
are most likely to belong to class 1.
"""

# ----------------------------------------------------------------------
# This function adjusts matplotlib settings for a uniform feel in the textbook.
# Note that with usetex=True, fonts are rendered with LaTeX.  This may
# result in an error if LaTeX is not installed on your system.  In that case,
# you can set usetex to False.
"""
if "setup_text_plots" not in globals():
    from astroML.plotting import setup_text_plots
setup_text_plots(fontsize=8, usetex=True)
"""
# ------------------------------------------------------------
# Set up the dataset.
#  We'll create our dataset by drawing samples from Gaussians.

random_state = np.random.RandomState(seed=1)

X = np.concatenate(
    [
        random_state.normal(-1, 1.5, 350),
        random_state.normal(0, 1, 500),
        random_state.normal(3, 0.5, 150),
    ]
).reshape(-1, 1)

# ------------------------------------------------------------
# Learn the best-fit GaussianMixture models
# Here we'll use scikit-learn's GaussianMixture model. The fit() method
# uses an Expectation-Maximization approach to find the best
# mixture of Gaussians for the data

# fit models with 1-10 components
N = np.arange(1, 11)
models = [None for i in range(len(N))]

for i in range(len(N)):
    models[i] = GaussianMixture(N[i]).fit(X)  # 學習訓練.fit

# compute the AIC and the BIC
AIC = [m.aic(X) for m in models]
BIC = [m.bic(X) for m in models]

# ------------------------------------------------------------
# Plot the results
#  We'll use three panels:
#   1) data + best-fit mixture
#   2) AIC and BIC vs number of components
#   3) probability that a point came from each component

fig = plt.figure(figsize=(10, 6))
fig.subplots_adjust(left=0.12, right=0.97, bottom=0.21, top=0.9, wspace=0.5)


# plot 1: data + best-fit mixture
ax = fig.add_subplot(131)
M_best = models[np.argmin(AIC)]

x = np.linspace(-6, 6, 1000)
logprob = M_best.score_samples(x.reshape(-1, 1))
responsibilities = M_best.predict_proba(x.reshape(-1, 1))
pdf = np.exp(logprob)
pdf_individual = responsibilities * pdf[:, np.newaxis]

ax.hist(X, 30, density=True, histtype="stepfilled", alpha=0.4)
ax.plot(x, pdf, "-k")
ax.plot(x, pdf_individual, "--k")
ax.text(0.04, 0.96, "Best-fit Mixture", ha="left", va="top", transform=ax.transAxes)
ax.set_xlabel("$x$")
ax.set_ylabel("$p(x)$")


# plot 2: AIC and BIC
ax = fig.add_subplot(132)
ax.plot(N, AIC, "-k", label="AIC")
ax.plot(N, BIC, "--k", label="BIC")
ax.set_xlabel("n. components")
ax.set_ylabel("information criterion")
ax.legend(loc=2)


# plot 3: posterior probabilities for each component
ax = fig.add_subplot(133)

p = responsibilities
p = p[:, (1, 0, 2)]  # rearrange order so the plot looks better
p = p.cumsum(1).T

ax.fill_between(x, 0, p[0], color="gray", alpha=0.3)
ax.fill_between(x, p[0], p[1], color="gray", alpha=0.5)
ax.fill_between(x, p[1], 1, color="gray", alpha=0.7)
ax.set_xlim(-6, 6)
ax.set_ylim(0, 1)
ax.set_xlabel("$x$")
ax.set_ylabel(r"$p({\rm class}|x)$")

ax.text(-5, 0.3, "class 1", rotation="vertical")
ax.text(0, 0.5, "class 2", rotation="vertical")
ax.text(3, 0.3, "class 3", rotation="vertical")

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from scipy.stats import norm
from scipy.stats import multivariate_normal

# change default figure and font size
plt.rcParams["figure.figsize"] = 8, 6
plt.rcParams["font.size"] = 12

# gaussian distribution with different values of the mean and variance
x = np.linspace(start=-10, stop=10, num=200)
mean_opt = [0, 0, 2]
var_opt = [1, 4, 4]

for m, v in zip(mean_opt, var_opt):
    y = norm(m, np.sqrt(v)).pdf(x)
    plt.plot(x, y, label="$\mu$ = {}, $\sigma^2$ = {}".format(m, v))
    plt.legend()

plt.show()


# revised from
# http://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.stats.multivariate_normal.html
x, y = np.mgrid[-4:4:0.01, -4:4:0.01]
position = np.empty(x.shape + (2,))
position[:, :, 0] = x
position[:, :, 1] = y

# different values for the covariance matrix
covariances = [[[1, 0], [0, 1]], [[1, 0], [0, 3]], [[1, -1], [-1, 3]]]
titles = ["spherical", "diag", "full"]

plt.figure(figsize=(15, 6))
for i in range(3):
    plt.subplot(1, 3, i + 1)
    z = multivariate_normal([0, 0], covariances[i]).pdf(position)
    plt.contour(x, y, z)
    plt.title("{}, {}".format(titles[i], covariances[i]))
    plt.xlim([-4, 4])
    plt.ylim([-4, 4])

plt.show()

# generate some random data to work with
np.random.seed(2)
x1 = np.random.normal(0, 2, size=2000)
x2 = np.random.normal(5, 5, size=2000)
data = [x1, x2]


def plot_hist(data):
    for x in data:
        plt.hist(x, bins=80, alpha=0.6)

    plt.xlim(-10, 20)


plot_hist(data)
plt.show()


# estimate the mean and variance of the data
x1_mean, x1_var = np.mean(x1), np.var(x1)
x2_mean, x2_var = np.mean(x2), np.var(x2)
x_mean = [x1_mean, x2_mean]
x_var = [x1_var, x2_var]


def plot_guassian(x_mean, x_var):
    """
    note that scipy's normal distribution requires the
    standard deviation (square root of variance)
    instead of the variance
    """
    x = np.linspace(start=-10, stop=20, num=200)
    for m, v in zip(x_mean, x_var):
        y = norm(m, np.sqrt(v)).pdf(x)
        plt.plot(x, y)


plot_hist(data)
plot_guassian(x_mean, x_var)
plt.show()

# E Step
# M Step
# Implementing the EM algorithm


def generate_data(n_data, means, covariances, weights):
    """creates a list of data points"""
    n_clusters, n_features = means.shape

    data = np.zeros((n_data, n_features))
    for i in range(n_data):
        # pick a cluster id and create data from this cluster
        k = np.random.choice(n_clusters, size=1, p=weights)[0]
        x = np.random.multivariate_normal(means[k], covariances[k])
        data[i] = x

    return data


# Model parameters, including the mean
# covariance matrix and the weights for each cluster
init_means = np.array([[5, 0], [1, 1], [0, 5]])

init_covariances = np.array(
    [[[0.5, 0.0], [0, 0.5]], [[0.92, 0.38], [0.38, 0.91]], [[0.5, 0.0], [0, 0.5]]]
)

init_weights = [1 / 4, 1 / 2, 1 / 4]

# generate data
np.random.seed(4)
X = generate_data(100, init_means, init_covariances, init_weights)

plt.plot(X[:, 0], X[:, 1], "ko")
plt.tight_layout()
plt.show()


class GMM:
    """
    Full covariance Gaussian Mixture Model,
    trained using Expectation Maximization.

    Parameters
    ----------
    n_components : int
        Number of clusters/mixture components in which the data will be
        partitioned into.

    n_iters : int
        Maximum number of iterations to run the algorithm.

    tol : float
        Tolerance. If the log-likelihood between two iterations is smaller than
        the specified tolerance level, the algorithm will stop performing the
        EM optimization.

    seed : int
        Seed / random state used to initialize the parameters.
    """

    def __init__(self, n_components: int, n_iters: int, tol: float, seed: int):
        self.n_components = n_components
        self.n_iters = n_iters
        self.tol = tol
        self.seed = seed

    def fit(self, X):
        # data's dimensionality and responsibility vector
        n_row, n_col = X.shape
        self.resp = np.zeros((n_row, self.n_components))

        # initialize parameters
        np.random.seed(self.seed)
        chosen = np.random.choice(n_row, self.n_components, replace=False)
        self.means = X[chosen]
        self.weights = np.full(self.n_components, 1 / self.n_components)

        # for np.cov, rowvar = False,
        # indicates that the rows represents obervation
        shape = self.n_components, n_col, n_col
        self.covs = np.full(shape, np.cov(X, rowvar=False))

        log_likelihood = 0
        self.converged = False
        self.log_likelihood_trace = []

        for i in range(self.n_iters):
            log_likelihood_new = self._do_estep(X)
            self._do_mstep(X)

            if abs(log_likelihood_new - log_likelihood) <= self.tol:
                self.converged = True
                break

            log_likelihood = log_likelihood_new
            self.log_likelihood_trace.append(log_likelihood)

        return self

    def _do_estep(self, X):
        """
        E-step: compute responsibilities,
        update resp matrix so that resp[j, k] is the responsibility of cluster k for data point j,
        to compute likelihood of seeing data point j given cluster k, use multivariate_normal.pdf
        """
        self._compute_log_likelihood(X)
        log_likelihood = np.sum(np.log(np.sum(self.resp, axis=1)))

        # normalize over all possible cluster assignments
        self.resp = self.resp / self.resp.sum(axis=1, keepdims=1)
        return log_likelihood

    def _compute_log_likelihood(self, X):
        for k in range(self.n_components):
            prior = self.weights[k]
            likelihood = multivariate_normal(self.means[k], self.covs[k]).pdf(X)
            self.resp[:, k] = prior * likelihood

        return self

    def _do_mstep(self, X):
        """M-step, update parameters"""

        # total responsibility assigned to each cluster, N^{soft}
        resp_weights = self.resp.sum(axis=0)

        # weights
        self.weights = resp_weights / X.shape[0]

        # means
        weighted_sum = np.dot(self.resp.T, X)
        self.means = weighted_sum / resp_weights.reshape(-1, 1)
        # covariance
        for k in range(self.n_components):
            diff = (X - self.means[k]).T
            weighted_sum = np.dot(self.resp[:, k] * diff, diff.T)
            self.covs[k] = weighted_sum / resp_weights[k]

        return self


def plot_contours(data, means, covs, title):
    """visualize the gaussian components over the data"""
    plt.figure()
    plt.plot(data[:, 0], data[:, 1], "ko")

    delta = 0.025
    k = means.shape[0]
    x = np.arange(-2.0, 7.0, delta)
    y = np.arange(-2.0, 7.0, delta)
    x_grid, y_grid = np.meshgrid(x, y)
    coordinates = np.array([x_grid.ravel(), y_grid.ravel()]).T

    col = ["green", "red", "indigo"]
    for i in range(k):
        mean = means[i]
        cov = covs[i]
        z_grid = multivariate_normal(mean, cov).pdf(coordinates).reshape(x_grid.shape)
        plt.contour(x_grid, y_grid, z_grid, colors=col[i])

    plt.title(title)
    plt.tight_layout()


# use our implementation of the EM algorithm
# and fit a mixture of Gaussians to the simulated data
gmm = GMM(n_components=3, n_iters=1, tol=1e-4, seed=4)
gmm.fit(X)  # 學習訓練.fit

plot_contours(X, gmm.means, gmm.covs, "Initial clusters")
plt.show()

gmm = GMM(n_components=3, n_iters=50, tol=1e-4, seed=4)
gmm.fit(X)  # 學習訓練.fit

print("converged iteration:", len(gmm.log_likelihood_trace))
plot_contours(X, gmm.means, gmm.covs, "Final clusters")
plt.show()

N_COMPONENTS = 3  # 要分成的群數
print("使用GaussianMixture分成", N_COMPONENTS, "群")
gmm = GaussianMixture(n_components=N_COMPONENTS, covariance_type="full", max_iter=600)
gmm.fit(X)  # 學習訓練.fit

plot_contours(X, gmm.means_, gmm.covariances_, "Final clusters")
plt.show()

# How many Gaussians?

n_components = np.arange(1, 10)
clfs = [GaussianMixture(n, max_iter=1000).fit(X) for n in n_components]
bics = [clf.bic(X) for clf in clfs]
aics = [clf.aic(X) for clf in clfs]

plt.plot(n_components, bics, label="BIC")
plt.plot(n_components, aics, label="AIC")
plt.xlabel("n_components")
plt.legend()
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import plot_utils
import sklearn

colors = sns.color_palette()

iris = datasets.load_iris()
X = iris.data[:, :2]  # 'sepal length (cm)''sepal width (cm)'
y_iris = iris.target

gmm2 = GaussianMixture(n_components=2, covariance_type="full").fit(X)  # 學習訓練.fit
gmm3 = GaussianMixture(n_components=3, covariance_type="full").fit(X)  # 學習訓練.fit
gmm4 = GaussianMixture(n_components=4, covariance_type="full").fit(X)  # 學習訓練.fit

plt.figure(figsize=(9, 3))
plt.subplot(131)
plt.scatter(
    X[:, 0], X[:, 1], c=[colors[lab] for lab in gmm2.predict(X)]
)  # , color=colors)
for i in range(gmm2.covariances_.shape[0]):
    plot_utils.plot_cov_ellipse(
        cov=gmm2.covariances_[i, :],
        pos=gmm2.means_[i, :],
        facecolor="none",
        linewidth=2,
        edgecolor=colors[i],
    )
    plt.scatter(
        gmm2.means_[i, 0],
        gmm2.means_[i, 1],
        edgecolor=colors[i],
        marker="o",
        s=100,
        facecolor="w",
        linewidth=2,
    )
plt.title("K=2")

plt.subplot(132)
plt.scatter(X[:, 0], X[:, 1], c=[colors[lab] for lab in gmm3.predict(X)])
for i in range(gmm3.covariances_.shape[0]):
    plot_utils.plot_cov_ellipse(
        cov=gmm3.covariances_[i, :],
        pos=gmm3.means_[i, :],
        facecolor="none",
        linewidth=2,
        edgecolor=colors[i],
    )
    plt.scatter(
        gmm3.means_[i, 0],
        gmm3.means_[i, 1],
        edgecolor=colors[i],
        marker="o",
        s=100,
        facecolor="w",
        linewidth=2,
    )
plt.title("K=3")

plt.subplot(133)
plt.scatter(
    X[:, 0], X[:, 1], c=[colors[lab] for lab in gmm4.predict(X)]
)  # .astype(np.float))
for i in range(gmm4.covariances_.shape[0]):
    plot_utils.plot_cov_ellipse(
        cov=gmm4.covariances_[i, :],
        pos=gmm4.means_[i, :],
        facecolor="none",
        linewidth=2,
        edgecolor=colors[i],
    )
    plt.scatter(
        gmm4.means_[i, 0],
        gmm4.means_[i, 1],
        edgecolor=colors[i],
        marker="o",
        s=100,
        facecolor="w",
        linewidth=2,
    )
_ = plt.title("K=4")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 貝葉斯信息量準則（Bayesian information criterion, BIC）

iris = datasets.load_iris()
X = iris.data
y_iris = iris.target

ks = np.arange(1, 10)
bic = list()

for k in ks:
    N_COMPONENTS = k  # 要分成的群數
    print("使用GaussianMixture分成", N_COMPONENTS, "群")
    gmm = GaussianMixture(n_components=N_COMPONENTS, covariance_type="full")
    gmm.fit(X)  # 學習訓練.fit
    bic.append(gmm.bic(X))

plt.plot(ks, bic)
plt.xlabel("要分成的群數")
plt.ylabel("貝葉斯信息量準則")
show()

k_chosen = ks[np.argmin(bic)]
print("Choose k=", k_chosen)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Density Estimation: Gaussian Mixture Models

from scipy import stats

sns.set()

X = np.concatenate(
    [
        np.random.normal(0, 2, 2000),
        np.random.normal(5, 5, 2000),
        np.random.normal(3, 0.5, 600),
    ]
).reshape(-1, 1)


plt.hist(X, 80)
plt.xlim(-10, 20)
show()

clf = GaussianMixture(n_components=4)

print(X.shape)

clf.fit(X)

xpdf = np.linspace(-10, 20, 4600).reshape(-1, 1)
print(xpdf.shape)
cc = clf.score_samples(xpdf)
print(cc)
density = np.exp(clf.score_samples(xpdf))

plt.hist(X, 80, density=True, alpha=0.5)
plt.plot(xpdf, density, "-r")
plt.xlim(-10, 20)
show()

print(clf.means_)
print(clf.covariances_)
print(clf.weights_)

plt.hist(X, 80, density=True, alpha=0.3)
plt.plot(xpdf, density, "-r")

for i in range(clf.n_components):
    pdf = clf.weights_[i] * stats.norm(
        clf.means_[i, 0], np.sqrt(clf.covariances_[i, 0])
    ).pdf(xpdf)
    plt.fill(xpdf, pdf, facecolor="gray", edgecolor="none", alpha=0.3)
plt.xlim(-10, 20)
show()

# How many Gaussians?
# Given a model, we can use one of several means to evaluate how well it fits the data. For example, there is the Aikaki Information Criterion (AIC) and the Bayesian Information Criterion (BIC)
print(clf.bic(X))
print(clf.aic(X))

# Let's take a look at these as a function of the number of gaussians:

n_estimators = np.arange(1, 10)
clfs = [GaussianMixture(n).fit(X) for n in n_estimators]
bics = [clf.bic(X) for clf in clfs]
aics = [clf.aic(X) for clf in clfs]

plt.plot(n_estimators, bics, label="BIC")
plt.plot(n_estimators, aics, label="AIC")
plt.legend()
show()

print("選取 AIC 和 BIC 最小的 分群數目")
# It appears that for both the AIC and BIC, 4 components is preferred.

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Example: GMM For Outlier Detection

# Outlier : 離開本體的部分；分離物；露宿者

# GMM is what's known as a Generative Model: it's a probabilistic model from which a dataset can be generated. One thing that generative models can be useful for is outlier detection: we can simply evaluate the likelihood of each point under the generative model the points with a suitably low likelihood (where "suitable" is up to your own bias/variance preference) can be labeld outliers.

X = np.concatenate(
    [
        np.random.normal(0, 2, 2000),
        np.random.normal(5, 5, 2000),
        np.random.normal(3, 0.5, 600),
    ]
).reshape(-1, 1)
print(X.shape)

# Add 20 outliers
true_outliers = np.sort(np.random.randint(0, len(X), 20))
print("選出20個突出值的index :", true_outliers)

y = X.copy()
y[true_outliers] += 50 * np.random.randn()

clf = GaussianMixture(4).fit(y)
xpdf = np.linspace(-10, 20, 1000).reshape(-1, 1)
print(xpdf.shape)
cc = clf.score_samples(xpdf)
print(cc)

density_noise = np.exp(clf.score_samples(xpdf))

plt.hist(y, 80, density=True, alpha=0.5)
plt.plot(xpdf, density_noise, "-r")
# plt.xlim(-10, 20)
show()

# Now let's evaluate the log-likelihood of each point under the model, and plot these as a function of y:

log_likelihood = clf.score_samples(y)
plt.plot(y, log_likelihood, ".k")
show()

detected_outliers = np.where(log_likelihood < -9)[0]

print("true outliers:")
print(true_outliers)
print("\ndetected outliers:")
print(detected_outliers)

cc = set(true_outliers) - set(detected_outliers)
print(cc)

cc = set(detected_outliers) - set(true_outliers)
print(cc)

""" NG
# Other Density Estimators

from sklearn.neighbors import KernelDensity

#kde = KernelDensity(kernel='gaussian', bandwidth=0.15).fit(X[:, None])
kde = KernelDensity(kernel='gaussian', bandwidth=0.15).fit(X)

density_kde = np.exp(kde.score_samples(xpdf[:, None]))
"""
plt.hist(X, 80, density=True, alpha=0.5)
plt.plot(xpdf, density_noise, "-r", label="GMM")
# plt.plot(xpdf, density_kde, "-g", label="KDE")
plt.xlim(-10, 20)
plt.legend()
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
