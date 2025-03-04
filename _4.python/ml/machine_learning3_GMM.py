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

gmm = GaussianMixture(n_components=2, random_state=9487)
gmm.fit(X)  # 學習訓練.fit

print(X.shape)
print("GaussianMixture訓練後結果 :")
print("各群的平均")
print(gmm.means_)  # 各 Gauss 分布の平均
print("各群的分散數")
print(gmm.covariances_)  # 各 Gauss 分布の分散
print(gmm.weights_)
print(gmm.converged_)
print(gmm.n_iter_)

y_pred = gmm.predict([[0, 0], [12, 3]])
print("預測結果 :\n", y_pred, sep="")

sys.exit()
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

iris = datasets.load_iris()
X = iris.data
y = iris.target  # 資料集目標

print("設定要分的群數")
n_components = 3

gmm = GaussianMixture(n_components=n_components)

gmm.fit(X)  # 學習訓練.fit

y_pred = gmm.predict(X)
print("預測結果 :\n", y_pred, sep="")

print("各群的平均")
print(gmm.means_)  # 各 Gauss 分布の平均

print("各群的分散數")
print(gmm.covariances_)  # 各 Gauss 分布の分散

# print(X.shape)
# print(y_pred.shape)

plt.subplot(211)
plt.scatter(X[:, 0], X[:, 1], c=y)

plt.subplot(212)
plt.scatter(X[:, 0], X[:, 1], c=y_pred)

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
gmm = GaussianMixture(n_components=2, n_init=10, max_iter=100)

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

# Gaussian Mixture Modeling
# Perform clsutering
gmm = GaussianMixture(n_components=2, n_init=10, max_iter=100)
gmm.fit(X)  # 學習訓練.fit
# GaussianMixture(n_components=2, n_init=10)
# Where are the clsuter centers
cc = gmm.means_
print(cc)

# Did algorithm converge?
cc = gmm.converged_
print(cc)

# How many iterations did it perform?
cc = gmm.n_iter_
print(cc)

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

kmeans = KMeans(4, random_state=9487)
labels = kmeans.fit(X).predict(X)
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


kmeans = KMeans(n_clusters=4, random_state=9487)
plot_kmeans(kmeans, X)

# 匯入SKlearn中GMM模組，並且建立4組資料
gmm = GaussianMixture(n_components=4)
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
    labels = gmm.fit(X).predict(X)
    if label:
        ax.scatter(X[:, 0], X[:, 1], c=labels, s=40, cmap="viridis", zorder=2)
    else:
        ax.scatter(X[:, 0], X[:, 1], s=40, zorder=2)
    ax.axis("equal")

    w_factor = 0.2 / gmm.weights_.max()
    for pos, covar, w in zip(gmm.means_, gmm.covariances_, gmm.weights_):
        draw_ellipse(pos, covar, alpha=w * w_factor)


gmm = GaussianMixture(n_components=4, random_state=9487)
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
    models[i] = GaussianMixture(N[i]).fit(X)

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


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
