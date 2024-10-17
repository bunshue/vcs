"""
Scikit-learn 詳解與企業應用_機器學習最佳入門與實戰

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

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 09_01_simple_kmeans_from_scratch
# 自行開發K-Means

import pandas as pd
import numpy as np
import math

# K-Means演算法類別


class Kmeans(object):
    # 訓練
    def fit(self, df, k=3):
        # 任意分成K組
        df["group"] = k - 1
        n = len(df) // 3
        # 前 k-1 組
        for i in range(k - 1):
            for j in range(n):
                df.loc[i * k + j, "group"] = i
        # print(df)

        # 重覆第EM步驟，直到資料所屬組別不再變動為止
        prev_df = pd.DataFrame()
        while not df.equals(prev_df):
            group_mean = df.groupby("group")["goals"].mean()
            print(group_mean)
            prev_df = df.copy()
            for i, row in prev_df.iterrows():
                df.loc[i, "group"] = np.argmin(np.abs(group_mean - row["goals"]))

        self.group_mean = group_mean
        return df

    # 預測
    def predict(self, x):
        return np.argmin(np.abs(self.group_mean - x))


# 載入資料集

df = pd.read_csv("./data/kmeans_data.csv")
print(df)

# 模型訓練

model = Kmeans()
clusters = model.fit(df)
print(clusters)

# 分組結果
grouped_df = clusters.groupby("group")
for key, item in grouped_df:
    print(f"group {key}:")
    print(item["player"].values, "\n")

# 預測

# 預測10個進球數
cc = model.predict(10)  # 第一組
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 09_02_kmeans_from_scratch

# 自行開發K-Means

import pandas as pd
import numpy as np
import math
import random
import matplotlib.pyplot as plt
import seaborn as sns

# 歐幾里得距離函數


def euclidean(point, data):
    return np.sqrt(np.sum((point - data) ** 2, axis=1))


# K-Means演算法類別


class KMeans:
    def __init__(self, n_clusters=8, max_iter=300):
        self.n_clusters = n_clusters  # 組數
        self.max_iter = max_iter  # EM 最大次數

    # 訓練
    def fit(self, X_train):
        # 生成1個質心
        self.centroids = [random.choice(X_train)]
        # 生成其他 n-1 個質心
        for _ in range(self.n_clusters - 1):
            # Calculate distances from points to the centroids
            dists = np.sum(
                [euclidean(centroid, X_train) for centroid in self.centroids], axis=0
            )
            # 正規化
            dists /= np.sum(dists)
            # 依據距離作為機率，隨機產生質心
            new_centroid_idx = np.random.choice(range(len(X_train)), size=1, p=dists)[0]
            self.centroids += [X_train[new_centroid_idx]]

        iteration = 0
        prev_centroids = [np.zeros(X_train.shape[1])] * self.n_clusters
        while (
            np.not_equal(self.centroids, prev_centroids).any()
            and iteration < self.max_iter
        ):
            # 找到最近的質心
            sorted_points = [[] for _ in range(self.n_clusters)]
            for x in X_train:
                dists = euclidean(x, self.centroids)
                centroid_idx = np.argmin(dists)
                sorted_points[centroid_idx].append(x)

            # 尋找新質心
            prev_centroids = self.centroids
            self.centroids = [np.mean(cluster, axis=0) for cluster in sorted_points]
            for i, centroid in enumerate(self.centroids):
                # 如果組內沒有任何樣本點，沿用上次的質心
                if np.isnan(centroid).any():
                    self.centroids[i] = prev_centroids[i]
            iteration += 1
        # print(iteration)

    # 模型評估
    def evaluate(self, X):
        centroids = []
        centroid_idxs = []
        for x in X:
            dists = euclidean(x, self.centroids)
            centroid_idx = np.argmin(dists)
            centroids.append(self.centroids[centroid_idx])
            centroid_idxs.append(centroid_idx)

        return centroids, centroid_idxs


# 生成分類資料

from sklearn.datasets import make_blobs

X_train, true_labels = make_blobs(n_samples=100, centers=5, random_state=42)
plt.scatter(X_train[:, 0], X_train[:, 1])
plt.show()

# 模型訓練

from sklearn.preprocessing import StandardScaler

# 標準化
X_train = StandardScaler().fit_transform(X_train)

# 訓練
kmeans = KMeans(n_clusters=5)
kmeans.fit(X_train)

# 模型評估

class_centers, classification = kmeans.evaluate(X_train)
sns.scatterplot(
    x=[X[0] for X in X_train],
    y=[X[1] for X in X_train],
    hue=true_labels,
    style=classification,
    palette="deep",
    legend=None,
)
plt.plot(
    [x for x, _ in kmeans.centroids],
    [y for _, y in kmeans.centroids],
    "*",
    markersize=20,
    color="r",
)
plt.title("k-means")
plt.show()

# 鳶尾花資料集測試

from sklearn import datasets

X, y = datasets.load_iris(return_X_y=True)

# 標準化
X_train = StandardScaler().fit_transform(X)

# 訓練
kmeans = KMeans(n_clusters=3)
kmeans.fit(X_train)

# 7

# 模型評估

from sklearn.metrics import accuracy_score

_, y_pred = kmeans.evaluate(X_train)
print(accuracy_score(y, y_pred))

# 0.22

# 驗證

# 實際值
cc = ",".join([str(i) for i in y])
print(cc)

# 預測值
cc = ",".join([str(i) for i in y_pred])
print(cc)

p = pd.Series(y_pred)
print(p[p == 1].index)

p = pd.Series(y)
print(p[p == 0].index)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 09_03_Scikit-learn_kmeans

# 鳶尾花資料集測試

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# 載入資料集

X, y = datasets.load_iris(return_X_y=True)

# 資料分割

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 特徵縮放

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 選擇演算法

from sklearn.cluster import KMeans

model = KMeans(n_clusters=3, init="k-means++", n_init="auto")

# 模型訓練

model.fit(X_train_std, y_train)

# KMeans(n_clusters=3, n_init='auto')

# 模型評估

# 計算準確率
y_pred = model.predict(X_test_std)
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 6.67%

# 比較實際值與預測值
cc = ",".join([str(i) for i in y_test]), ",".join([str(i) for i in y_pred])
print(cc)

cc = [i for i, j in enumerate(y_test) if j == 0] == [
    i for i, j in enumerate(y_pred) if j == 1
]
print(cc)

# 模型評估：資料點與所屬質心距離的平方和

cc = model.inertia_
print(cc)

# 111.5372270434027

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 09_04_kmeans_optimization_elbow

# 轉折判斷法(Elbow)

import numpy as np

# 生成分類資料

from sklearn.datasets import make_blobs

X, y = make_blobs(
    n_samples=150,
    n_features=2,
    centers=3,
    cluster_std=0.5,
    shuffle=True,
    random_state=0,
)

# 訓練模型

from sklearn.cluster import KMeans

km = KMeans(
    n_clusters=3, init="random", n_init=10, max_iter=300, tol=1e-04, random_state=0
)

# 模型評估

# 顯示失真(Distortion)的程度
y_km = km.fit_predict(X)
print("Distortion: %.2f" % km.inertia_)

# Distortion: 72.48

# 轉折判斷法(Elbow)

distortions = []
# 測試 1~10 群的失真
for i in range(1, 11):
    km = KMeans(n_clusters=i, init="k-means++", n_init=10, max_iter=300, random_state=0)
    km.fit(X)
    distortions.append(km.inertia_)

# 繪圖

import matplotlib.pyplot as plt

plt.plot(range(1, 11), distortions, marker="o")
plt.xlabel("集群數量", fontsize=14)
plt.ylabel("失真", fontsize=14)
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 09_05_kmeans_optimization_silhouette

# 輪廓圖分析(Silhouette Analysis)

from sklearn.cluster import KMeans
import numpy as np
from matplotlib import cm
from sklearn.metrics import silhouette_samples
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# 生成分類資料

X, y = make_blobs(
    n_samples=150,
    n_features=2,
    centers=3,
    cluster_std=0.5,
    shuffle=True,
    random_state=0,
)

# 訓練模型

km = KMeans(
    n_clusters=2, init="k-means++", n_init=10, max_iter=300, tol=1e-04, random_state=0
)
y_km = km.fit_predict(X)

# 輪廓係數

cluster_labels = np.unique(y_km)
n_clusters = cluster_labels.shape[0]
silhouette_vals = silhouette_samples(X, y_km, metric="euclidean")
silhouette_vals

# 繪製輪廓圖

# 輪廓圖
y_ax_lower, y_ax_upper = 0, 0
yticks = []
for i, c in enumerate(cluster_labels):
    c_silhouette_vals = silhouette_vals[y_km == c]
    c_silhouette_vals.sort()
    y_ax_upper += len(c_silhouette_vals)
    color = cm.jet(float(i) / n_clusters)
    plt.barh(
        range(y_ax_lower, y_ax_upper),
        c_silhouette_vals,
        height=1.0,
        edgecolor="none",
        color=color,
    )

    yticks.append((y_ax_lower + y_ax_upper) / 2.0)
    y_ax_lower += len(c_silhouette_vals)

# 輪廓係數平均數的垂直線
silhouette_avg = np.mean(silhouette_vals)
plt.axvline(silhouette_avg, color="red", linestyle="--")

plt.yticks(yticks, cluster_labels + 1)
plt.ylabel("集群", fontsize=14)
plt.xlabel("輪廓係數", fontsize=14)
plt.show()

# 使用3個集群訓練模型

km = KMeans(
    n_clusters=3, init="k-means++", n_init=10, max_iter=300, tol=1e-04, random_state=0
)
y_km = km.fit_predict(X)

# 繪製輪廓圖

cluster_labels = np.unique(y_km)
n_clusters = cluster_labels.shape[0]
silhouette_vals = silhouette_samples(X, y_km, metric="euclidean")

# 輪廓圖
y_ax_lower, y_ax_upper = 0, 0
yticks = []
for i, c in enumerate(cluster_labels):
    c_silhouette_vals = silhouette_vals[y_km == c]
    c_silhouette_vals.sort()
    y_ax_upper += len(c_silhouette_vals)
    color = cm.jet(float(i) / n_clusters)
    plt.barh(
        range(y_ax_lower, y_ax_upper),
        c_silhouette_vals,
        height=1.0,
        edgecolor="none",
        color=color,
    )

    yticks.append((y_ax_lower + y_ax_upper) / 2.0)
    y_ax_lower += len(c_silhouette_vals)

# 輪廓係數平均數的垂直線
silhouette_avg = np.mean(silhouette_vals)
plt.axvline(silhouette_avg, color="red", linestyle="--")

plt.yticks(yticks, cluster_labels + 1)
plt.ylabel("集群", fontsize=14)
plt.xlabel("輪廓係數", fontsize=14)
plt.show()

# 計算輪廓分數

from sklearn.metrics import silhouette_score

cc = silhouette_score(X, y)
print(cc)

# 0.7143417887288687

# 依據輪廓分數找最佳集群數量

# 測試 2~10 群的分數
silhouette_score_list = []
print("輪廓分數:")
for i in range(2, 11):
    km = KMeans(n_clusters=i, init="k-means++", n_init=10, max_iter=300, random_state=0)
    km.fit(X)
    y_km = km.fit_predict(X)
    silhouette_score_list.append(silhouette_score(X, y_km))
    print(f"{i}:{silhouette_score_list[-1]:.2f}")

print(f"最大值 {np.argmax(silhouette_score_list)+2}: {np.max(silhouette_score_list):.2f}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 09_06_agglomerative_hierarchical_clustering

# 凝聚階層集群(Agglomerative Hierarchical Clustering, AHC)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 生成資料

np.random.seed(123)
variables = ["X", "Y", "Z"]
labels = ["ID_0", "ID_1", "ID_2", "ID_3", "ID_4"]

X = np.random.random_sample([5, 3]) * 10
df = pd.DataFrame(X, columns=variables, index=labels)
print(df)

# 計算集群彼此間的距離

from scipy.spatial.distance import pdist, squareform

row_dist = pd.DataFrame(
    squareform(pdist(df, metric="euclidean")), columns=labels, index=labels
)
print(row_dist)

# 計算平均連結距離

from scipy.cluster.hierarchy import linkage

row_clusters = linkage(pdist(df, metric="euclidean"), method="average")
pd.DataFrame(
    row_clusters,
    columns=["row label 1", "row label 2", "distance", "no. of items in clust."],
    index=["cluster %d" % (i + 1) for i in range(row_clusters.shape[0])],
)

# 繪製樹狀圖(dendrogram)

from scipy.cluster.hierarchy import dendrogram

row_dendr = dendrogram(row_clusters, labels=labels)
plt.ylabel("歐幾里德距離", fontsize=14)
plt.show()

# 繪製熱力圖

fig = plt.figure(figsize=(8, 8), facecolor="white")
axd = fig.add_axes([0.09, 0.1, 0.2, 0.6])  # x-pos, y-pos, width, height

# 樹狀圖顯示在左邊
row_dendr = dendrogram(row_clusters, orientation="left")

# 降冪排序
df_rowclust = df.iloc[row_dendr["leaves"][::-1]]

# 不顯示刻度
axd.set_xticks([])
axd.set_yticks([])

# 不顯示座標軸
for i in axd.spines.values():
    i.set_visible(False)

# 繪製熱力圖
axm = fig.add_axes([0.23, 0.1, 0.6, 0.6])  # x-pos, y-pos, width, height
cax = axm.matshow(df_rowclust, interpolation="nearest", cmap="hot_r")
fig.colorbar(cax)
axm.set_xticklabels([""] + list(df_rowclust.columns))
axm.set_yticklabels([""] + list(df_rowclust.index))
plt.show()

# Scikit-learn AgglomerativeClustering

from sklearn.cluster import AgglomerativeClustering

# 分 3 類
ac = AgglomerativeClustering(n_clusters=3, metric="euclidean", linkage="complete")
labels = ac.fit_predict(X)
print("Cluster labels: %s" % labels)

# Cluster labels: [1 0 0 2 1]

# 分 2 類
ac = AgglomerativeClustering(n_clusters=2, metric="euclidean", linkage="complete")
labels = ac.fit_predict(X)
print("Cluster labels: %s" % labels)

# Cluster labels: [0 1 1 0 0]

# 使用鳶尾花資料集測試

from sklearn.datasets import load_iris


# 繪製樹狀圖
def plot_dendrogram(model, **kwargs):
    # 計算每個集群的筆數
    counts = np.zeros(model.children_.shape[0])
    n_samples = len(model.labels_)
    for i, merge in enumerate(model.children_):
        current_count = 0
        for child_idx in merge:
            if child_idx < n_samples:
                current_count += 1  # leaf node
            else:
                current_count += counts[child_idx - n_samples]
        counts[i] = current_count

    linkage_matrix = np.column_stack(
        [model.children_, model.distances_, counts]
    ).astype(float)

    # 繪製樹狀圖
    dendrogram(linkage_matrix, **kwargs)


# 載入資料集
X, _ = load_iris(return_X_y=True)

# distance_threshold=0 表示會建立完整的樹狀圖(dendrogram)
model = AgglomerativeClustering(distance_threshold=0, n_clusters=None)

model = model.fit(X)
plt.title("Hierarchical Clustering Dendrogram")
plot_dendrogram(model, truncate_mode="level", p=3)  # 限制 3 層
plt.ylabel("歐幾里德距離", fontsize=14)
plt.xlabel("每個集群的筆數", fontsize=14)
plt.show()

# 各種距離衡量方式的比較

import time
import matplotlib.pyplot as plt
import numpy as np

from sklearn.cluster import AgglomerativeClustering
from sklearn.neighbors import kneighbors_graph

# Generate sample data
n_samples = 1500
np.random.seed(0)
t = 1.5 * np.pi * (1 + 3 * np.random.rand(1, n_samples))
x = t * np.cos(t)
y = t * np.sin(t)


X = np.concatenate((x, y))
X += 0.7 * np.random.randn(2, n_samples)
X = X.T

# Create a graph capturing local connectivity. Larger number of neighbors
# will give more homogeneous clusters to the cost of computation
# time. A very large number of neighbors gives more evenly distributed
# cluster sizes, but may not impose the local manifold structure of
# the data
knn_graph = kneighbors_graph(X, 30, include_self=False)

for connectivity in (None, knn_graph):
    for n_clusters in (30, 3):
        plt.figure(figsize=(10, 4))
        for index, linkage in enumerate(("average", "complete", "ward", "single")):
            plt.subplot(1, 4, index + 1)
            model = AgglomerativeClustering(
                linkage=linkage, connectivity=connectivity, n_clusters=n_clusters
            )
            t0 = time.time()
            model.fit(X)
            elapsed_time = time.time() - t0
            plt.scatter(X[:, 0], X[:, 1], c=model.labels_, cmap=plt.cm.nipy_spectral)
            plt.title(
                "linkage=%s\n(time %.2fs)" % (linkage, elapsed_time),
                fontdict=dict(verticalalignment="top"),
            )
            plt.axis("equal")
            plt.axis("off")

            plt.subplots_adjust(bottom=0, top=0.89, wspace=0, left=0, right=1)
            plt.suptitle(
                "n_cluster=%i, connectivity=%r"
                % (n_clusters, connectivity is not None),
                size=17,
            )
            plt.tight_layout()

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 09_07_dbscan_simple_test

# 以密度為基礎的集群(Density-based spatial clustering of applications with noise, DBSCAN)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

# 生成資料

X = np.array([[1, 2], [2, 2], [2, 3], [8, 7], [8, 8], [25, 80]])
print(X)

# 模型訓練

model = DBSCAN(eps=3, min_samples=2).fit(X)
print(model.labels_)

# 生成更多資料，且非線性

from sklearn.datasets import make_moons

X, y = make_moons(n_samples=200, noise=0.05, random_state=0)
plt.scatter(X[:, 0], X[:, 1])
plt.show()

# 模型訓練，繪製結果

db = DBSCAN(eps=0.2, min_samples=5, metric="euclidean")
y_pred = db.fit_predict(X)
plt.scatter(
    X[y_pred == 0, 0],
    X[y_pred == 0, 1],
    c="lightblue",
    marker="o",
    s=40,
    edgecolor="black",
    label="cluster 1",
)
plt.scatter(
    X[y_pred == 1, 0],
    X[y_pred == 1, 1],
    c="red",
    marker="s",
    s=40,
    edgecolor="black",
    label="cluster 2",
)
plt.legend()
plt.show()

# 另一個範例，參閱Demo of DBSCAN clustering algorithm

from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler

centers = [[1, 1], [-1, -1], [1, -1]]
X, labels_true = make_blobs(
    n_samples=750, centers=centers, cluster_std=0.4, random_state=0
)

X = StandardScaler().fit_transform(X)

# 繪製資料

plt.figure(figsize=(10, 8))
plt.scatter(X[:, 0], X[:, 1])
plt.show()

# 模型訓練

labels = DBSCAN(eps=0.3, min_samples=10).fit_predict(X)

# 計算集群內樣本數、雜訊點個數
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)

print(f"集群數={n_clusters_}")
print(f"雜訊點個數={n_noise_}")

# 集群數=3
# 雜訊點個數=18

# 模型評估

from sklearn import metrics

print(f"Homogeneity: {metrics.homogeneity_score(labels_true, labels):.3f}")
print(f"Completeness: {metrics.completeness_score(labels_true, labels):.3f}")
print(f"V-measure: {metrics.v_measure_score(labels_true, labels):.3f}")
print(f"Adjusted Rand Index: {metrics.adjusted_rand_score(labels_true, labels):.3f}")
print(
    "Adjusted Mutual Information:"
    f" {metrics.adjusted_mutual_info_score(labels_true, labels):.3f}"
)
print(f"Silhouette Coefficient: {metrics.silhouette_score(X, labels):.3f}")

"""
Homogeneity: 0.953
Completeness: 0.883
V-measure: 0.917
Adjusted Rand Index: 0.952
Adjusted Mutual Information: 0.916
Silhouette Coefficient: 0.626
"""

# 繪製結果

plt.figure(figsize=(10, 8))
unique_labels = set(labels)
core_samples_mask = np.zeros_like(labels, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True

colors = [plt.cm.Spectral(each) for each in np.linspace(0, 1, len(unique_labels))]
for k, col in zip(unique_labels, colors):
    if k == -1:
        # Black used for noise.
        col = [0, 0, 0, 1]

    class_member_mask = labels == k

    xy = X[class_member_mask & core_samples_mask]
    plt.plot(
        xy[:, 0],
        xy[:, 1],
        "o",
        markerfacecolor=tuple(col),
        markeredgecolor="k",
        markersize=14,
    )

    xy = X[class_member_mask & ~core_samples_mask]
    plt.plot(
        xy[:, 0],
        xy[:, 1],
        "o",
        markerfacecolor=tuple(col),
        markeredgecolor="k",
        markersize=6,
    )

plt.title(f"Estimated number of clusters: {n_clusters_}")
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 09_08_gmm_test
# GMM測試，程式修改自Python Data Science Handbook 範例05.12-Gaussian-Mixtures.ipynb

import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
import numpy as np

# 生成分類資料

from sklearn.datasets import make_blobs

X, y_true = make_blobs(n_samples=400, centers=4, cluster_std=0.60, random_state=0)
X = X[:, ::-1]  # 特徵互調順序，繪圖效果較佳
print(X[:10])

# 進行 K-Means 集群，並繪圖

from sklearn.cluster import KMeans

kmeans = KMeans(4, init="k-means++", n_init=10, random_state=0)
labels = kmeans.fit(X).predict(X)
plt.scatter(X[:, 0], X[:, 1], c=labels, s=40, cmap="viridis")
plt.show()

# 繪製集群範圍

from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist


def plot_kmeans(kmeans, X, n_clusters=4, rseed=0, ax=None):
    labels = kmeans.fit_predict(X)

    # 繪製樣本點
    ax = ax or plt.gca()
    ax.axis("equal")
    ax.scatter(X[:, 0], X[:, 1], c=labels, s=40, cmap="viridis", zorder=2)

    # 以最大半徑繪製集群範圍
    centers = kmeans.cluster_centers_
    radii = [cdist(X[labels == i], [center]).max() for i, center in enumerate(centers)]
    for c, r in zip(centers, radii):
        ax.add_patch(
            plt.Circle(c, r, fc="#CCCCCC", lw=3, color="k", alpha=0.5, zorder=1)
        )


kmeans = KMeans(n_clusters=4, init="k-means++", n_init=10, random_state=0)
plot_kmeans(kmeans, X)
plt.show()

# 生成長條型資料

rng = np.random.RandomState(13)
X_stretched = np.dot(X, rng.randn(2, 2))

kmeans = KMeans(n_clusters=4, init="k-means++", n_init=10, random_state=0)
plot_kmeans(kmeans, X_stretched)
plt.show()

# 改用GMM

from sklearn.mixture import GaussianMixture

gmm = GaussianMixture(n_components=4).fit(X)
labels = gmm.predict(X)
plt.scatter(X[:, 0], X[:, 1], c=labels, s=40, cmap="viridis")
plt.show()

# 屬於各集群的機率

probs = gmm.predict_proba(X)
print(probs[:5].round(3))

# 繪製集群範圍

from matplotlib.patches import Ellipse


# 繪製橢圓
def draw_ellipse(position, covariance, ax=None, **kwargs):
    """Draw an ellipse with a given position and covariance"""
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


# 繪製GMM範圍
def plot_gmm(gmm, X, label=True, ax=None):
    ax = ax or plt.gca()
    labels = gmm.fit(X).predict(X)
    if label:
        ax.scatter(X[:, 0], X[:, 1], c=labels, s=40, cmap="viridis", zorder=2)
    else:
        ax.scatter(X[:, 0], X[:, 1], s=40, zorder=2)
    ax.axis("equal")

    # soft-edged sphere
    w_factor = 0.2 / gmm.weights_.max()
    for pos, covar, w in zip(gmm.means_, gmm.covariances_, gmm.weights_):
        draw_ellipse(pos, covar, alpha=w * w_factor)


gmm = GaussianMixture(n_components=4, random_state=42)
plot_gmm(gmm, X)
plt.show()

# 使用 GMM對長條型資料進行集群

gmm = GaussianMixture(n_components=4, covariance_type="full", random_state=42)
plot_gmm(gmm, X_stretched)
plt.show()

# 測試非線性資料

from sklearn.datasets import make_moons

Xmoon, ymoon = make_moons(200, noise=0.05, random_state=0)
plt.scatter(Xmoon[:, 0], Xmoon[:, 1])
plt.show()

# GMM 集群：設定2個集群

gmm2 = GaussianMixture(n_components=2, covariance_type="full", random_state=0)
plot_gmm(gmm2, Xmoon)
plt.show()

# GMM 集群：設定16個集群

gmm16 = GaussianMixture(n_components=16, covariance_type="full", random_state=0)
plot_gmm(gmm16, Xmoon, label=False)
plt.show()

# 以模型生成資料

Xnew, _ = gmm16.sample(400)
plt.scatter(Xnew[:, 0], Xnew[:, 1])
plt.show()

# 以AIC/BIC決定最佳集群數量

n_components = np.arange(1, 21)
models = [
    GaussianMixture(n, covariance_type="full", random_state=0).fit(Xmoon)
    for n in n_components
]

plt.plot(n_components, [m.bic(Xmoon) for m in models], label="BIC")
plt.plot(n_components, [m.aic(Xmoon) for m in models], label="AIC")
plt.legend(loc="best")
plt.xlabel("n_components")
plt.show()

# 生成手寫阿拉伯數字

from sklearn.datasets import load_digits

digits = load_digits()
cc = digits.data.shape
print(cc)

# (1797, 64)

# 顯示前 100 筆手寫阿拉伯數字


def plot_digits(data):
    fig, ax = plt.subplots(
        10, 10, figsize=(8, 8), subplot_kw=dict(xticks=[], yticks=[])
    )
    fig.subplots_adjust(hspace=0.05, wspace=0.05)
    for i, axi in enumerate(ax.flat):
        im = axi.imshow(data[i].reshape(8, 8), cmap="binary")
        im.set_clim(0, 16)


plot_digits(digits.data)
plt.show()

# 降維

from sklearn.decomposition import PCA

pca = PCA(0.99, whiten=True)
data = pca.fit_transform(digits.data)
print(data.shape)

# (1797, 41)

# 以AIC決定最佳集群數量

n_components = np.arange(50, 210, 10)
models = [GaussianMixture(n, covariance_type="full") for n in n_components]
aics = [model.fit(data).aic(data) for model in models]
plt.plot(n_components, aics)
plt.show()

# 以AIC決定最佳集群數量=110
# 設定集群數量=110

gmm = GaussianMixture(110, covariance_type="full", random_state=0)
gmm.fit(data)
print(gmm.converged_)

# True

# Now we can draw samples of 100 new points within this 41-dimensional projected space, using the GMM as a generative model:

# 生成100個樣本

data_new, _ = gmm.sample(100)
digits_new = pca.inverse_transform(data_new)
plot_digits(digits_new)
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 09_09_image_compression

# 影像壓縮(Image Compression)

import numpy as np
import matplotlib.pyplot as plt
from sklearn.utils import shuffle
from sklearn.datasets import load_sample_image
from sklearn.cluster import KMeans

# 載入測試圖片

flower = load_sample_image("flower.jpg")
plt.axis("off")
plt.imshow(flower)
plt.show()

# 存檔
plt.imsave("tmp_flower.jpg", flower)

# 正規化、取得圖片寬高及顏色維度、將寬高轉為一維

# 正規化
flower = np.array(flower, dtype=np.float64) / 255

# 取得圖片寬高及顏色維度
w, h, d = tuple(flower.shape)

# 將寬高轉為一維
image_array = np.reshape(flower, (w * h, d))
print(w, h, d)

# (427, 640, 3)

# 模型訓練及預測

# 隨機抽樣1000個像素
image_sample = shuffle(image_array, random_state=42)[:1000]

# K-Means模型訓練， 設定64個集群
kmeans = KMeans(n_clusters=64, random_state=42).fit(image_sample)

# 對所有像素進行集群
labels = kmeans.predict(image_array)

# 重建影像的函數


def reconstruct_image(cluster_centers, labels, w, h):
    d = cluster_centers.shape[1]
    image = np.zeros((w, h, d))
    label_index = 0
    for i in range(w):
        for j in range(h):
            # 以質心取代原圖像顏色
            image[i][j] = cluster_centers[labels[label_index]]
            label_index += 1
    return image


# 比較原圖與減色後的圖片

plt.figure(figsize=(14, 7))

# 原圖
plt.subplot(1, 2, 1)
plt.axis("off")
plt.title("原圖")
plt.imshow(flower)

plt.subplot(1, 2, 2)
plt.axis("off")
plt.title("重建的影像")
plt.imshow(reconstruct_image(kmeans.cluster_centers_, labels, w, h))
plt.show()

# 再使用K-Means，設定4個集群

# K-Means模型訓練， 設定4個集群
kmeans = KMeans(n_clusters=4, random_state=42).fit(image_sample)

# 對所有像素進行集群
labels = kmeans.predict(image_array)

plt.figure(figsize=(14, 7))
# 原圖
plt.subplot(1, 2, 1)
plt.axis("off")
plt.title("原圖")
plt.imshow(flower)

plt.subplot(1, 2, 2)
plt.axis("off")
plt.title("重建的影像")
plt.imshow(reconstruct_image(kmeans.cluster_centers_, labels, w, h))
plt.show()

# 存檔
plt.imsave(
    "tmp_flower_kmeans.jpg", reconstruct_image(kmeans.cluster_centers_, labels, w, h)
)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 09_10_customer_segmentation
# 客戶區隔(Customer segmentation)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 載入資料集
df = pd.read_csv(
    "C:/_git/vcs/_big_files/Scikit-learn_data/invoice.csv", encoding="ISO-8859-1"
)

# 只分析英國的顧客
df = df[df.Country == "United Kingdom"]
cc = df.head()
print(cc)

# 描述統計量
# df.describe().T

# 資料清理

# 移除非購買記錄

# 移除數量<=0的交易記錄
df = df[df["Quantity"] > 0]

# 移除單價<=0的交易記錄
df = df[df["UnitPrice"] > 0]
print(df.Quantity.describe())
cc = df.UnitPrice.describe()
print(cc)

# 刪除 Missing Value
df.dropna(subset=["CustomerID"], inplace=True)

# 檢查 Missing Value
cc = df.isnull().sum()
print(cc)

# 找出資料集的最近購買日期

# 找出資料集的最近購買日期
print(df["InvoiceDate"].max())

# 日期轉 YYYY-MM-DD
cc = df["date"] = pd.DatetimeIndex(df.InvoiceDate).date
print(cc)

# 計算 Recency

# 計算每個顧客的最近購買日期
recency_df = df.groupby(["CustomerID"], as_index=False)["date"].max()
recency_df.columns = ["CustomerID", "LastPurchaseDate"]

# 計算每個顧客的上次消費的日期距今天數
now = df["date"].max()
recency_df["Recency"] = recency_df.LastPurchaseDate.apply(lambda x: (now - x).days)
cc = recency_df.head()
print(cc)

recency_df.drop(columns=["LastPurchaseDate"], inplace=True)

# 計算 Frequency

# 計算每個顧客的消費次數
frequency_df = df.copy()
frequency_df.drop_duplicates(
    subset=["CustomerID", "InvoiceNo"], keep="first", inplace=True
)
frequency_df = frequency_df.groupby("CustomerID", as_index=False)["InvoiceNo"].count()
frequency_df.columns = ["CustomerID", "Frequency"]
cc = frequency_df.head()
print(cc)

# 計算 Monetary

# 計算每個顧客的累計消費金額
df["Total_cost"] = df["UnitPrice"] * df["Quantity"]
monetary_df = df.groupby("CustomerID", as_index=False)["Total_cost"].sum()
monetary_df.columns = ["CustomerID", "Monetary"]
cc = monetary_df.head()
print(cc)

# 合併 RFM

rf = recency_df.merge(frequency_df, left_on="CustomerID", right_on="CustomerID")
rfm = rf.merge(monetary_df, left_on="CustomerID", right_on="CustomerID")
rfm.set_index("CustomerID", inplace=True)
cc = rfm.head()
print(cc)

# 驗算

cc = df[df.CustomerID == 12346.0]
print(cc)

import datetime as dt

now = dt.date(2011, 12, 9)
cc = (now - dt.date(2011, 1, 18)).days == 325
print(cc)

# True

# 使用K-Means進行集群

from sklearn.cluster import KMeans

# 複製資料
rfm_segmentation = rfm.copy()

# 轉折判斷法
Nc = range(1, 20)
kmeans = [KMeans(n_clusters=i, init="k-means++", n_init="auto") for i in Nc]
for i in range(len(kmeans)):
    kmeans[i].fit(rfm_segmentation)
score = [kmeans[i].score(rfm_segmentation) for i in range(len(kmeans))]
wcss = [kmeans[i].inertia_ for i in range(len(kmeans))]

plt.plot(Nc, score)
plt.xticks(range(0, 20, 2))
plt.xlabel("Number of Clusters")
plt.ylabel("Score")
plt.title("Elbow Curve")
plt.show()

plt.plot(Nc, wcss)
plt.xticks(range(0, 20, 2))
plt.xlabel("Number of Clusters")
plt.ylabel("wcss")
plt.title("Elbow Curve")
plt.show()

# 分成3群

X = rfm_segmentation.copy()
kmeans = KMeans(
    n_clusters=3, init="k-means++", n_init=10, max_iter=300, random_state=0
).fit(X)

# 新增欄位，加入集群代碼
rfm_segmentation["cluster"] = kmeans.labels_

# 觀看集群 0 的前 10 筆資料
cc = rfm_segmentation[rfm_segmentation.cluster == 0].head(10)
print(cc)

# 計算每群筆數

cc = rfm_segmentation["cluster"].value_counts()
print(cc)

# 輪廓係數

from sklearn.metrics import silhouette_samples

y_km = rfm_segmentation["cluster"]
cluster_labels = np.unique(y_km)
n_clusters = cluster_labels.shape[0]
silhouette_vals = silhouette_samples(X, y_km, metric="euclidean")
cc = silhouette_vals
print(cc)

# 繪製輪廓圖

from matplotlib import cm

# 輪廓圖
y_ax_lower, y_ax_upper = 0, 0
yticks = []
for i, c in enumerate(cluster_labels):
    c_silhouette_vals = silhouette_vals[y_km == c]
    c_silhouette_vals.sort()
    y_ax_upper += len(c_silhouette_vals)
    color = cm.jet(float(i) / n_clusters)
    plt.barh(
        range(y_ax_lower, y_ax_upper),
        c_silhouette_vals,
        height=1.0,
        edgecolor="none",
        color=color,
    )

    yticks.append((y_ax_lower + y_ax_upper) / 2.0)
    y_ax_lower += len(c_silhouette_vals)

# 輪廓係數平均數的垂直線
silhouette_avg = np.mean(silhouette_vals)
plt.axvline(silhouette_avg, color="red", linestyle="--")

plt.yticks(yticks, cluster_labels + 1)
plt.ylabel("集群", fontsize=14)
plt.xlabel("輪廓係數", fontsize=14)
plt.tight_layout()
plt.show()

# 依據輪廓分數找最佳集群數量

# 測試 2~20 群的分數
from sklearn.metrics import silhouette_score

silhouette_score_list = []
print("輪廓分數:")
for i in range(2, 21):
    km = KMeans(n_clusters=i, init="k-means++", n_init=10, max_iter=300, random_state=0)
    km.fit(X)
    y_km = km.fit_predict(X)
    silhouette_score_list.append(silhouette_score(X, y_km))
    print(f"{i}:{silhouette_score_list[-1]:.2f}")

print(f"最大值 {np.argmax(silhouette_score_list)+2}: {np.max(silhouette_score_list):.2f}")

for i in range(2, 21):
    km = KMeans(
        n_clusters=i, init="k-means++", n_init=10, max_iter=300, random_state=0
    ).fit(X)

    # 新增欄位，加入集群代碼
    y_km = km.labels_
    cluster_labels = np.unique(y_km)
    n_clusters = cluster_labels.shape[0]
    silhouette_vals = silhouette_samples(X, y_km, metric="euclidean")

    # 輪廓圖
    y_ax_lower, y_ax_upper = 0, 0
    yticks = []
    for i, c in enumerate(cluster_labels):
        c_silhouette_vals = silhouette_vals[y_km == c]
        c_silhouette_vals.sort()
        y_ax_upper += len(c_silhouette_vals)
        color = cm.jet(float(i) / n_clusters)
        plt.barh(
            range(y_ax_lower, y_ax_upper),
            c_silhouette_vals,
            height=1.0,
            edgecolor="none",
            color=color,
        )

        yticks.append((y_ax_lower + y_ax_upper) / 2.0)
        y_ax_lower += len(c_silhouette_vals)

    # 輪廓係數平均數的垂直線
    silhouette_avg = np.mean(silhouette_vals)
    plt.axvline(silhouette_avg, color="red", linestyle="--")

    plt.yticks(yticks, cluster_labels + 1)
    plt.ylabel("集群", fontsize=14)
    plt.xlabel("輪廓係數", fontsize=14)
    plt.tight_layout()
    plt.show()

# RFM 分組


# 四分位數分組
def RScore(x, p, d):
    if x <= d[p][0.25]:
        return 1
    elif x <= d[p][0.50]:
        return 2
    elif x <= d[p][0.75]:
        return 3
    else:
        return 4


def FMScore(x, p, d):
    if x <= d[p][0.25]:
        return 4
    elif x <= d[p][0.50]:
        return 3
    elif x <= d[p][0.75]:
        return 2
    else:
        return 1


# 四分位數(quantile)
quantile = rfm.quantile(q=[0.25, 0.5, 0.75])
print(quantile)

cc = quantile.to_dict()
print(cc)

# RFM依四分位數給分

rfm_segmentation["R_Quartile"] = rfm_segmentation["Recency"].apply(
    RScore, args=("Recency", quantile)
)
rfm_segmentation["F_Quartile"] = rfm_segmentation["Frequency"].apply(
    FMScore, args=("Frequency", quantile)
)
rfm_segmentation["M_Quartile"] = rfm_segmentation["Monetary"].apply(
    FMScore, args=("Monetary", quantile)
)
cc = rfm_segmentation.head()
print(cc)

# 合併 RFM 分數
rfm_segmentation["RFMScore"] = (
    rfm_segmentation.R_Quartile.map(str)
    + rfm_segmentation.F_Quartile.map(str)
    + rfm_segmentation.M_Quartile.map(str)
)
cc = rfm_segmentation.head()
print(cc)

# 計算 RFM 總分
rfm_segmentation["Total_score"] = (
    rfm_segmentation["R_Quartile"]
    + rfm_segmentation["F_Quartile"]
    + rfm_segmentation["M_Quartile"]
)

cc = rfm_segmentation.head()
print(cc)

print("客戶篩選：")
print("Best Customers: ", len(rfm_segmentation[rfm_segmentation["RFMScore"] == "111"]))
print("Loyal Customers: ", len(rfm_segmentation[rfm_segmentation["F_Quartile"] == 1]))
print("Big Spenders: ", len(rfm_segmentation[rfm_segmentation["M_Quartile"] == 1]))
print("Almost Lost: ", len(rfm_segmentation[rfm_segmentation["RFMScore"] == "134"]))
print("Lost Customers: ", len(rfm_segmentation[rfm_segmentation["RFMScore"] == "344"]))
print(
    "Lost Cheap Customers: ",
    len(rfm_segmentation[rfm_segmentation["RFMScore"] == "444"]),
)
"""
客戶篩選：
Best Customers:  423
Loyal Customers:  791
Big Spenders:  980
Almost Lost:  31
Lost Customers:  187
Lost Cheap Customers:  396
"""
# 依分數顯示客戶名單
cc = rfm_segmentation.sort_values(
    by=["RFMScore", "Monetary"], ascending=[True, False]
).head(10)
print(cc)

# 依RFM級數顯示每一組的平均消費金額
cc = rfm_segmentation.groupby("RFMScore")["Monetary"].mean().head(10)
print(cc)

# 依RFM總分顯示每一組的平均消費金額
cc = rfm_segmentation.groupby("Total_score")["Monetary"].mean()

# 依RFM總分作圖，總分 3,4,5 有最高消費金額
rfm_segmentation.groupby("Total_score")["Monetary"].mean().plot(
    kind="bar", colormap="Blues_r"
)
plt.show()

# 依RFM總分作圖，總分 3,4,5 有最高消費次數
rfm_segmentation.groupby("Total_score")["Frequency"].mean().plot(
    kind="bar", colormap="Blues_r"
)
plt.show()

# 依RFM總分作圖，總分 10,11,12 Recency最高
rfm_segmentation.groupby("Total_score")["Recency"].mean().plot(
    kind="bar", colormap="Blues_r"
)
plt.show()

# 依據輪廓分數找最佳集群數量

# 測試 2~20 群的分數
from sklearn.metrics import silhouette_score

X = rfm_segmentation[["R_Quartile", "F_Quartile", "M_Quartile"]]
silhouette_score_list = []
print("輪廓分數:")
for i in range(2, 21):
    km = KMeans(n_clusters=i, init="k-means++", n_init=10, max_iter=300, random_state=0)
    km.fit(X)
    y_km = km.fit_predict(X)
    silhouette_score_list.append(silhouette_score(X, y_km))
    print(f"{i}:{silhouette_score_list[-1]:.2f}")

print(f"最大值 {np.argmax(silhouette_score_list)+2}: {np.max(silhouette_score_list):.2f}")

for i in range(2, 21):
    km = KMeans(
        n_clusters=i, init="k-means++", n_init=10, max_iter=300, random_state=0
    ).fit(X)

    # 新增欄位，加入集群代碼
    y_km = km.labels_
    cluster_labels = np.unique(y_km)
    n_clusters = cluster_labels.shape[0]
    silhouette_vals = silhouette_samples(X, y_km, metric="euclidean")

    # 輪廓圖
    y_ax_lower, y_ax_upper = 0, 0
    yticks = []
    for i, c in enumerate(cluster_labels):
        c_silhouette_vals = silhouette_vals[y_km == c]
        c_silhouette_vals.sort()
        y_ax_upper += len(c_silhouette_vals)
        color = cm.jet(float(i) / n_clusters)
        plt.barh(
            range(y_ax_lower, y_ax_upper),
            c_silhouette_vals,
            height=1.0,
            edgecolor="none",
            color=color,
        )

        yticks.append((y_ax_lower + y_ax_upper) / 2.0)
        y_ax_lower += len(c_silhouette_vals)

    # 輪廓係數平均數的垂直線
    silhouette_avg = np.mean(silhouette_vals)
    plt.axvline(silhouette_avg, color="red", linestyle="--")

    plt.yticks(yticks, cluster_labels + 1)
    plt.ylabel("集群", fontsize=14)
    plt.xlabel("輪廓係數", fontsize=14)
    plt.tight_layout()
    plt.show()

# 分成4個集群

kmeans = KMeans(n_clusters=4, random_state=0).fit(X)

# 新增欄位，加入集群代碼
rfm_segmentation["cluster"] = kmeans.labels_

# 觀看集群 0 的前 10 筆資料
cc = rfm_segmentation[rfm_segmentation.cluster == 0].head(10)
print(cc)

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.colors as mcolors

fig = plt.figure(figsize=(12, 8))
dx = fig.add_subplot(111, projection="3d")
colors = ["green", "blue", "red", "yellow"]

for i in range(rfm_segmentation.cluster.nunique()):
    dx.scatter(
        rfm_segmentation[rfm_segmentation.cluster == i].R_Quartile,
        rfm_segmentation[rfm_segmentation.cluster == i].F_Quartile,
        rfm_segmentation[rfm_segmentation.cluster == i].M_Quartile,
        c=colors[i],
        label="Cluster " + str(i),
        s=10,
        alpha=1.0,
    )

dx.set_xlabel("Recency", fontsize=14)
dx.set_ylabel("Frequency", fontsize=14)
dx.set_zlabel("Monetary", fontsize=14)
dx.legend(fontsize=12)
plt.tight_layout()
plt.show()

cc = rfm_segmentation.cluster.value_counts()
print(cc)

cc = rfm_segmentation.groupby("cluster")[
    ["R_Quartile", "F_Quartile", "M_Quartile", "Total_score"]
].mean()
print(cc)

# 結論
# 集群 1為VIP，其他依序為3、2、0。


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()
