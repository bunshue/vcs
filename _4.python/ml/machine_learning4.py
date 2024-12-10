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
from sklearn.datasets import make_blobs  # 生成分類資料
from sklearn.datasets import make_moons  # 生成非線性資料
from sklearn.datasets import make_classification
from sklearn.datasets import make_hastie_10_2

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import Lasso

from sklearn.cluster import KMeans

from sklearn.metrics import accuracy_score
from sklearn.metrics import r2_score
from sklearn.metrics import confusion_matrix

from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料


def show():
    # return
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 08_06_performance_metrics

# 計算及繪製混淆矩陣

df = pd.read_csv("C:/_git/vcs/_big_files/Scikit-learn_data/creditcard.csv")
cc = df.head()
print(cc)

# 觀察目標變數的各類別筆數

cc = df.Class.value_counts()
print(cc)

sns.countplot(x="Class", data=df)
show()

# 模型訓練與預測

X, y = df.drop(["Time", "Amount", "Class"], axis=1), df["Class"]

# 分割資料
X_train, X_test, y_train, y_test = train_test_split(X, y)

# 模型訓練
clf = LogisticRegression()

clf.fit(X_train, y_train)  # 學習訓練.fit

# 預測
y_pred = clf.predict(X_test)

# 準確率
cc = accuracy_score(y_test, y_pred)
print(cc)

# 計算混淆矩陣

# 取得混淆矩陣的4個格子

tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
print(tn, fp, fn, tp)

# (71072, 10, 40, 80)

# 常用的效能衡量指標計算

print(f"準確率(Accuracy)={(tn+tp) / (tn+fp+fn+tp)}")
print(f"精確率(Precision)={(tp) / (fp+tp)}")
print(f"召回率(Recall)={(tp) / (fn+tp)}")
print(f"F1 score={(2*tp) / (2*tp+fp+fn)}")

"""
準確率(Accuracy)=0.9992977725344794
精確率(Precision)=0.8888888888888888
召回率(Recall)=0.6666666666666666
F1 score=0.7619047619047619
"""

# Scikit-learn 分類報表

from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))

# weighted average 驗算
cc = (1.00 * 71082 + 0.89 * 120) / (71082 + 120)
print(cc)

# 多類別的分類報表

# 3 類別
y_true = [0, 1, 2, 2, 2]
y_pred = [0, 0, 2, 2, 1]
print(classification_report(y_true, y_pred))

# 多類別的分類報表

# 3 類別
y_pred = [1, 2, 0]
y_true = [1, 1, 1]
print(classification_report(y_true, y_pred, labels=[1, 2, 3]))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
ROC曲線
Receiver operating characteristic curve
接收者操作特徵曲線
"""
# 08_07_ draw_roc

# 繪製ROC曲線

# 載入資料

df = pd.read_csv("./data/roc_test_data.csv")
print(df)

"""
繪製ROC曲線
    計算第二欄的真(1)與假(0)的個數，假設分別為P及N，Y軸切成P格，X軸切成N格，如下圖。
    以第一欄降冪排序，從大排到小。
    依序掃描第二欄，若是1，就往『上』畫一格，反之，若是0，就往『右』畫一格，直到最後一列，如下圖。
"""

# 計算P及N個數

# 計算第二欄的真(1)與假(0)的個數，假設分別為P及N
P = df[df["actual"] == 1].shape[0]
N = df[df["actual"] == 0].shape[0]
print(f"P={P}, N={N}")

# X、Y軸每一格的大小
cc = y_unit = 1 / P
print(cc)
cc = X_unit = 1 / N
print(cc)

# P=11, N=7

# 根據第1欄降冪排序

df2 = df.sort_values(by="predict", ascending=False)
print(df2)

# 掃描表格每一列，第二欄若是1，就往『上』畫一格，反之，若是0，就往『右』畫一格

X, y = [], []
current_X, current_y = 0, 0
for row in df2.itertuples():
    # 若是1，Y加1
    if row[2] == 1:
        current_y += y_unit
    else:  # 若是0，X加1
        current_X += X_unit
    # 儲存每一點X/Y座標
    X.append(current_X)
    y.append(current_y)

X = np.array(X)
y = np.array(y)
print(X, y)

# 繪製ROC曲線

plt.title("ROC 曲線")
plt.plot(X, y, color="orange")
plt.plot([0, 1], [0, 1], "r--")
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel("真陽率")
plt.xlabel("偽陽率")
show()

# Scikit-Learn 作法

from sklearn.metrics import roc_curve, roc_auc_score, auc

fpr, tpr, threshold = roc_curve(df["actual"], df["predict"])
print(f"偽陽率:\n{fpr}\n\n真陽率:\n{tpr}\n\n決策門檻:{threshold}")

"""
偽陽率:
[0.         0.         0.         0.14285714 0.14285714 0.28571429
 0.28571429 0.57142857 0.57142857 0.71428571 0.71428571 1.        ]

真陽率:
[0.         0.09090909 0.27272727 0.27272727 0.63636364 0.63636364
 0.81818182 0.81818182 0.90909091 0.90909091 1.         1.        ]

決策門檻:[1.99 0.99 0.8  0.73 0.56 0.48 0.42 0.32 0.22 0.11 0.1  0.03]
"""

# 繪製ROC曲線

auc1 = auc(fpr, tpr)
plt.title("ROC 曲線")
plt.plot(fpr, tpr, color="orange", label="AUC = %0.2f" % auc1)
plt.legend(loc="lower right")
plt.plot([0, 1], [0, 1], "r--")
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel("真陽率")
plt.xlabel("偽陽率")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# 08_09_ credit_card_fraud_detection

# 信用卡詐欺偵測

# 載入資料

df = pd.read_csv("C:/_git/vcs/_big_files/Scikit-learn_data/creditcard.csv")
cc = df.head()
print(cc)

# 觀察目標變數的各類別筆數

cc = df.Class.value_counts()
print(cc)

sns.countplot(x="Class", data=df)
show()

X, y = df.drop(["Time", "Amount", "Class"], axis=1), df["Class"]

# 分割資料
X_train, X_test, y_train, y_test = train_test_split(X, y)

# 模型訓練
clf = LogisticRegression()

clf.fit(X_train, y_train)  # 學習訓練.fit

# 預測
y_pred = clf.predict(X_test)

# 準確率
cc = accuracy_score(y_test, y_pred)
print(cc)

# K折交叉驗證

from sklearn.model_selection import cross_val_score

scores = cross_val_score(estimator=clf, X=X_test, y=y_test, cv=10, n_jobs=-1)
print(f"K折分數: %s" % scores)
print(f"平均值: {np.mean(scores):.3f}, 標準差: {np.std(scores):.3f}")

"""
K折分數: [0.99915742 0.99929785 0.9988764  0.9997191  0.99901685 0.99901685
 0.9991573  0.99957865 0.9988764  0.9994382 ]
平均值: 0.999, 標準差: 0.000
"""

# 分類報告

from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))

# 繪製ROC曲線

from sklearn.metrics import roc_curve, roc_auc_score, auc

y_pred_proba = clf.predict_proba(X_test)[:, 1]
fpr, tpr, threshold = roc_curve(y_test, y_pred_proba)
auc1 = auc(fpr, tpr)
plt.title("ROC 曲線")
plt.plot(fpr, tpr, color="orange", label="AUC = %0.2f" % auc1)
plt.legend(loc="lower right")
plt.plot([0, 1], [0, 1], "r--")
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel("真陽率")
plt.xlabel("偽陽率")
show()

# 從寬認定詐欺行為

y_pred_proba = clf.predict_proba(X_test)[:, 1]
y_pred = y_pred_proba >= 0.3
print(classification_report(y_test, y_pred))

# Over-sampling -- SMOTE

# !pip install -U imbalanced-learn

from imblearn.over_sampling import SMOTE
from imblearn.metrics import classification_report_imbalanced

print(df.Class.value_counts())
smote = SMOTE()
X_new, y_new = smote.fit_resample(X, y)
cc = len(y_new[y_new == 0]), len(y_new[y_new == 1])
print(cc)

# 模型訓練與評估

# 分割資料
X_train, X_test, y_train, y_test = train_test_split(X_new, y_new)

# 模型訓練
clf = LogisticRegression()

clf.fit(X_train, y_train)  # 學習訓練.fit

# 預測
y_pred = clf.predict(X_test)

# 準確率
cc = accuracy_score(y_test, y_pred)
print(cc)

# K折交叉驗證

from sklearn.model_selection import cross_val_score

scores = cross_val_score(estimator=clf, X=X_test, y=y_test, cv=10, n_jobs=-1)
print(f"K折分數: %s" % scores)
print(f"平均值: {np.mean(scores):.3f}, 標準差: {np.std(scores):.3f}")

"""
K折分數: [0.94499156 0.94379572 0.94569499 0.94541362 0.94442881 0.94288126
 0.94231851 0.95040799 0.94336968 0.94379177]
平均值: 0.945, 標準差: 0.002
"""

# 分類報告

from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))

# imbalanced-learn 分類報告

from imblearn.metrics import classification_report_imbalanced

print(classification_report_imbalanced(y_test, y_pred))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 09_01_simple_kmeans_from_scratch
# 自行開發K-Means

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

model = Kmeans()  # K-平均演算法

clusters = model.fit(df)  # 學習訓練.fit
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


X_train, true_labels = make_blobs(n_samples=100, centers=5, random_state=42)
plt.scatter(X_train[:, 0], X_train[:, 1])
show()

# 模型訓練

from sklearn.preprocessing import StandardScaler

# 標準化
X_train = StandardScaler().fit_transform(X_train)

# 訓練
CLUSTERS = 5  # 要分成的群數
clf = KMeans(n_clusters=CLUSTERS)  # K-平均演算法

clf.fit(X_train)  # 學習訓練.fit

# 模型評估

class_centers, classification = clf.evaluate(X_train)

sns.scatterplot(
    x=[X[0] for X in X_train],
    y=[X[1] for X in X_train],
    hue=true_labels,
    style=classification,
    palette="deep",
    legend=None,
)
plt.plot(
    [x for x, _ in clf.centroids],
    [y for _, y in clf.centroids],
    "*",
    markersize=20,
    color="r",
)
plt.title("k-means")
show()

# 鳶尾花資料集測試

X, y = datasets.load_iris(return_X_y=True)

# 標準化
X_train = StandardScaler().fit_transform(X)

# 訓練
CLUSTERS = 3  # 要分成的群數
clf = KMeans(n_clusters=CLUSTERS)  # K-平均演算法

clf.fit(X_train)  # 學習訓練.fit

# 7

# 模型評估
_, y_pred = clf.evaluate(X_train)

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

# 09_06_agglomerative_hierarchical_clustering

# 凝聚階層集群(Agglomerative Hierarchical Clustering, AHC)

# 生成資料
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
show()

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
show()

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

model = model.fit(X)  # 學習訓練.fit

plt.title("Hierarchical Clustering Dendrogram")
plot_dendrogram(model, truncate_mode="level", p=3)  # 限制 3 層
plt.ylabel("歐幾里德距離", fontsize=14)
plt.xlabel("每個集群的筆數", fontsize=14)
show()

# 各種距離衡量方式的比較

from sklearn.cluster import AgglomerativeClustering
from sklearn.neighbors import kneighbors_graph

# Generate sample data
n_samples = 1500
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
            model.fit(X)  # 學習訓練.fit
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

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 09_07_dbscan_simple_test

# 以密度為基礎的集群(Density-based spatial clustering of applications with noise, DBSCAN)

from sklearn.cluster import DBSCAN

# 生成資料
X = np.array([[1, 2], [2, 2], [2, 3], [8, 7], [8, 8], [25, 80]])
print(X)

# 模型訓練

model = DBSCAN(eps=3, min_samples=2)

model.fit(X)  # 學習訓練.fit
print(model.labels_)

X, y = make_moons(n_samples=200, noise=0.05, random_state=9487)
plt.scatter(X[:, 0], X[:, 1])
show()

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
show()

# 另一個範例，參閱Demo of DBSCAN clustering algorithm
from sklearn.preprocessing import StandardScaler

centers = [[1, 1], [-1, -1], [1, -1]]
X, labels_true = make_blobs(
    n_samples=750, centers=centers, cluster_std=0.4, random_state=9487
)

X = StandardScaler().fit_transform(X)

# 繪製資料
plt.figure(figsize=(10, 8))
plt.scatter(X[:, 0], X[:, 1])
show()

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
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 09_08_gmm_test
# GMM測試，程式修改自Python Data Science Handbook 範例05.12-Gaussian-Mixtures.ipynb

sns.set()

X, y_true = make_blobs(n_samples=400, centers=4, cluster_std=0.60, random_state=9487)
X = X[:, ::-1]  # 特徵互調順序，繪圖效果較佳
print(X[:10])

# 進行 K-Means 集群，並繪圖

CLUSTERS = 4  # 要分成的群數
clf = KMeans(CLUSTERS, init="k-means++", n_init=10)  # K-平均演算法

labels = clf.fit(X).predict(X)

plt.scatter(X[:, 0], X[:, 1], c=labels, s=40, cmap="viridis")

show()

# 繪製集群範圍

from scipy.spatial.distance import cdist


def plot_kmeans(clf, X, n_clusters=4, rseed=0, ax=None):
    labels = clf.fit_predict(X)

    # 繪製樣本點
    ax = ax or plt.gca()
    ax.axis("equal")
    ax.scatter(X[:, 0], X[:, 1], c=labels, s=40, cmap="viridis", zorder=2)

    # 以最大半徑繪製集群範圍
    centers = clf.cluster_centers_
    radii = [cdist(X[labels == i], [center]).max() for i, center in enumerate(centers)]
    for c, r in zip(centers, radii):
        ax.add_patch(
            plt.Circle(c, r, fc="#CCCCCC", lw=3, color="k", alpha=0.5, zorder=1)
        )


CLUSTERS = 4  # 要分成的群數
clf = KMeans(n_clusters=CLUSTERS, init="k-means++", n_init=10)  # K-平均演算法
plot_kmeans(clf, X)
show()

# 生成長條型資料

rng = np.random.RandomState(13)
X_stretched = np.dot(X, rng.randn(2, 2))

CLUSTERS = 4  # 要分成的群數
clf = KMeans(n_clusters=CLUSTERS, init="k-means++", n_init=10)  # K-平均演算法
plot_kmeans(clf, X_stretched)
show()

# 改用GMM

from sklearn.mixture import GaussianMixture

gmm = GaussianMixture(n_components=4)

gmm.fit(X)  # 學習訓練.fit

labels = gmm.predict(X)
plt.scatter(X[:, 0], X[:, 1], c=labels, s=40, cmap="viridis")
show()

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
show()

# 使用 GMM對長條型資料進行集群

gmm = GaussianMixture(n_components=4, covariance_type="full", random_state=42)
plot_gmm(gmm, X_stretched)
show()

Xmoon, ymoon = make_moons(200, noise=0.05, random_state=9487)
plt.scatter(Xmoon[:, 0], Xmoon[:, 1])
show()

# GMM 集群：設定2個集群

gmm2 = GaussianMixture(n_components=2, covariance_type="full", random_state=9487)
plot_gmm(gmm2, Xmoon)
show()

# GMM 集群：設定16個集群

gmm16 = GaussianMixture(n_components=16, covariance_type="full", random_state=9487)
plot_gmm(gmm16, Xmoon, label=False)
show()

# 以模型生成資料

Xnew, _ = gmm16.sample(400)
plt.scatter(Xnew[:, 0], Xnew[:, 1])
show()

# 以AIC/BIC決定最佳集群數量

n_components = np.arange(1, 21)
models = [
    GaussianMixture(n, covariance_type="full", random_state=9487).fit(Xmoon)
    for n in n_components
]

plt.plot(n_components, [m.bic(Xmoon) for m in models], label="BIC")
plt.plot(n_components, [m.aic(Xmoon) for m in models], label="AIC")
plt.legend(loc="best")
plt.xlabel("n_components")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 09_10_customer_segmentation
# 客戶區隔(Customer segmentation)

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

# 複製資料
rfm_segmentation = rfm.copy()

# 轉折判斷法
Nc = range(1, 20)
clf = [KMeans(n_clusters=i, init="k-means++", n_init="auto") for i in Nc]
for i in range(len(clf)):
    clf[i].fit(rfm_segmentation)  # 學習訓練.fit
score = [clf[i].score(rfm_segmentation) for i in range(len(clf))]
wcss = [clf[i].inertia_ for i in range(len(clf))]

plt.plot(Nc, score)
plt.xticks(range(0, 20, 2))
plt.xlabel("Number of Clusters")
plt.ylabel("Score")
plt.title("Elbow Curve")
show()

plt.plot(Nc, wcss)
plt.xticks(range(0, 20, 2))
plt.xlabel("Number of Clusters")
plt.ylabel("wcss")
plt.title("Elbow Curve")
show()

# 分成3群

X = rfm_segmentation.copy()
clf = KMeans(n_clusters=3, init="k-means++", n_init=10, max_iter=300)  # K-平均演算法

clf.fit(X)  # 學習訓練.fit

# 新增欄位，加入集群代碼
rfm_segmentation["cluster"] = clf.labels_

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
show()

# 依據輪廓分數找最佳集群數量

# 測試 2~20 群的分數
from sklearn.metrics import silhouette_score

silhouette_score_list = []
print("1輪廓分數:")
for i in range(2, 21):
    clf = KMeans(n_clusters=i, init="k-means++", n_init=10, max_iter=300)  # K-平均演算法
    clf.fit(X)  # 學習訓練.fit
    y_pred = clf.fit_predict(X)
    silhouette_score_list.append(silhouette_score(X, y_km))
    print(f"{i}:{silhouette_score_list[-1]:.2f}")

print(f"最大值 {np.argmax(silhouette_score_list)+2}: {np.max(silhouette_score_list):.2f}")

for i in range(2, 21):
    print(i)
    CLUSTERS = i  # 要分成的群數
    clf = KMeans(
        n_clusters=CLUSTERS, init="k-means++", n_init=10, max_iter=300
    )  # K-平均演算法
    clf.fit(X)  # 學習訓練.fit

    # 新增欄位，加入集群代碼
    y_pred = clf.labels_
    cluster_labels = np.unique(y_pred)
    n_clusters = cluster_labels.shape[0]
    silhouette_vals = silhouette_samples(X, y_pred, metric="euclidean")

    # 輪廓圖
    y_ax_lower, y_ax_upper = 0, 0
    yticks = []
    for i, c in enumerate(cluster_labels):
        c_silhouette_vals = silhouette_vals[y_pred == c]
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
    show()

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
show()

# 依RFM總分作圖，總分 3,4,5 有最高消費次數
rfm_segmentation.groupby("Total_score")["Frequency"].mean().plot(
    kind="bar", colormap="Blues_r"
)
show()

# 依RFM總分作圖，總分 10,11,12 Recency最高
rfm_segmentation.groupby("Total_score")["Recency"].mean().plot(
    kind="bar", colormap="Blues_r"
)
show()

# 依據輪廓分數找最佳集群數量

# 測試 2~20 群的分數
from sklearn.metrics import silhouette_score

X = rfm_segmentation[["R_Quartile", "F_Quartile", "M_Quartile"]]
silhouette_score_list = []
print("2輪廓分數:")
for i in range(2, 21):
    print(i)
    CLUSTERS = i  # 要分成的群數
    clf = KMeans(
        n_clusters=CLUSTERS, init="k-means++", n_init=10, max_iter=300
    )  # K-平均演算法
    clf.fit(X)  # 學習訓練.fit
    y_pred = clf.fit_predict(X)
    silhouette_score_list.append(silhouette_score(X, y_pred))
    print(f"{i}:{silhouette_score_list[-1]:.2f}")

print(f"最大值 {np.argmax(silhouette_score_list)+2}: {np.max(silhouette_score_list):.2f}")

for i in range(2, 21):
    print(i)
    CLUSTERS = i  # 要分成的群數
    clf = KMeans(
        n_clusters=CLUSTERS, init="k-means++", n_init=10, max_iter=300
    )  # K-平均演算法
    clf.fit(X)  # 學習訓練.fit

    # 新增欄位，加入集群代碼
    y_pred = clf.labels_
    cluster_labels = np.unique(y_pred)
    n_clusters = cluster_labels.shape[0]
    silhouette_vals = silhouette_samples(X, y_pred, metric="euclidean")

    # 輪廓圖
    y_ax_lower, y_ax_upper = 0, 0
    yticks = []
    for i, c in enumerate(cluster_labels):
        c_silhouette_vals = silhouette_vals[y_pred == c]
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
    show()

# 分成4個集群

CLUSTERS = 4  # 要分成的群數
clf = KMeans(n_clusters=CLUSTERS)  # K-平均演算法

clf.fit(X)  # 學習訓練.fit

# 新增欄位，加入集群代碼
rfm_segmentation["cluster"] = clf.labels_

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
show()

cc = rfm_segmentation.cluster.value_counts()
print(cc)

cc = rfm_segmentation.groupby("cluster")[
    ["R_Quartile", "F_Quartile", "M_Quartile", "Total_score"]
].mean()
print(cc)

# 結論
# 集群 1為VIP，其他依序為3、2、0。

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 10_01_error_rate

# 整體學習的錯誤率計算

from scipy.special import comb

# 計算整體學習的錯誤率


def ensemble_error(n_classifier, error):
    k_start = int(math.ceil(n_classifier / 2.0))
    probs = [
        comb(n_classifier, k) * error**k * (1 - error) ** (n_classifier - k)
        for k in range(k_start, n_classifier + 1)
    ]
    return sum(probs)


cc = ensemble_error(n_classifier=11, error=0.25)
print(cc)

# 0.03432750701904297

# 測試各種錯誤率，並繪圖

error_range = np.arange(0.0, 1.01, 0.01)
ens_errors = [ensemble_error(n_classifier=11, error=error) for error in error_range]

# 修正中文亂碼
plt.rcParams["font.sans-serif"] = ["Arial Unicode MS"]
plt.rcParams["axes.unicode_minus"] = False

plt.plot(error_range, ens_errors, label="整體學習", linewidth=2)

plt.plot(error_range, error_range, linestyle="--", label="個別模型", linewidth=2)

plt.title("錯誤率比較", fontsize=18)
plt.xlabel("個別模型錯誤率", fontsize=14)
plt.ylabel("整體學習錯誤率", fontsize=14)
plt.legend(loc="upper left", fontsize=14)
plt.grid(alpha=0.5)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 11_02_label_propagation

# 標註傳播(Label propagation)測試

from sklearn.semi_supervised import LabelPropagation

X, y = make_classification(
    n_samples=1000, n_features=2, n_informative=2, n_redundant=0, random_state=9487
)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, stratify=y)

# 設定 50% 資料為沒有標註(-1)
X_train_lab, X_test_unlab, y_train_lab, y_test_unlab = train_test_split(
    X_train, y_train, test_size=0.5, stratify=y_train
)
X_train_mixed = np.concatenate((X_train_lab, X_test_unlab))
nolabel = [-1 for _ in range(len(y_test_unlab))]
y_train_mixed = np.concatenate((y_train_lab, nolabel))
cc = y_train_mixed.shape
print(cc)

# (500,)

# Label propagation 模型訓練與評估

clf = LabelPropagation()

clf.fit(X_train_mixed, y_train_mixed)  # 學習訓練.fit

cc = clf.score(X_test, y_test)
print(cc)

# 0.856

clf2 = LogisticRegression()

clf2.fit(X_train_lab, y_train_lab)  # 學習訓練.fit

cc = clf2.score(X_test, y_test)
print(cc)

# 0.848

# 取得訓練資料標註

tran_labels = clf.transduction_
cc = tran_labels.shape
print(cc)
# (500,)

# 再依Label propagation傳播結果進行模型訓練與評估

clf3 = LogisticRegression()

clf3.fit(X_train_mixed, tran_labels)  # 學習訓練.fit

cc = clf3.score(X_test, y_test)
print(cc)
# 0.862

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 11_03_label_spreading

# LabelSpreading 測試

from sklearn.semi_supervised import LabelSpreading

# 載入資料集
X, y = make_classification(
    n_samples=1000, n_features=2, n_informative=2, n_redundant=0, random_state=9487
)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, stratify=y)

# 設定 50% 資料為沒有標註(-1)

X_train_lab, X_test_unlab, y_train_lab, y_test_unlab = train_test_split(
    X_train, y_train, test_size=0.5, random_state=1, stratify=y_train
)
X_train_mixed = np.concatenate((X_train_lab, X_test_unlab))
nolabel = [-1 for _ in range(len(y_test_unlab))]
y_train_mixed = np.concatenate((y_train_lab, nolabel))
cc = y_train_mixed.shape
print(cc)
# (500,)

# LabelSpreading 模型訓練與評估

clf = LabelSpreading()

clf.fit(X_train_mixed, y_train_mixed)  # 學習訓練.fit

cc = clf.score(X_test, y_test)
print(cc)
# 0.854

clf2 = LogisticRegression()

clf2.fit(X_train_lab, y_train_lab)  # 學習訓練.fit

cc = clf2.score(X_test, y_test)
print(cc)

# 0.848

# 取得訓練資料標註

tran_labels = clf.transduction_
cc = tran_labels.shape
print(cc)
# (500,)

# 再依LabelSpreading傳播結果進行模型訓練與評估

clf3 = LogisticRegression()

clf3.fit(X_train_mixed, tran_labels)  # 學習訓練.fit

cc = clf3.score(X_test, y_test)
print(cc)
# 0.858

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 範例2. 自行計算 Shapley value
# 載入套件

from sklearn.tree import DecisionTreeRegressor, plot_tree

# 載入資料

with open("./data/housing.data", encoding="utf8") as f:
    data = f.readlines()
all_fields = []
for line in data:
    line2 = line[1:].replace("   ", " ").replace("  ", " ")
    fields = []
    for item in line2.split(" "):
        fields.append(float(item.strip()))
        if len(fields) == 14:
            all_fields.append(fields)
df = pd.DataFrame(all_fields)
df.columns = "CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT,MEDV".split(",")
cc = df.head()
print(cc)

# 模型訓練

y = df["MEDV"]
df = df[["RM", "LSTAT", "DIS", "NOX"]]

clf = DecisionTreeRegressor(max_depth=3)

clf.fit(df, y)  # 學習訓練.fit

fig = plt.figure(figsize=(20, 5))
ax = fig.add_subplot(111)
_ = plot_tree(clf, ax=ax, feature_names=df.columns)
show()

# 以 SHAP 套件計算 Shapley value

import shap
import tabulate

explainer = shap.TreeExplainer(clf)
shap_values = explainer.shap_values(df[:1])  # 第一筆資料
print(
    tabulate.tabulate(
        pd.DataFrame(
            {
                "shap_value": shap_values.squeeze(),
                "feature_value": df[:1].values.squeeze(),
            },
            index=df.columns,
        ),
        tablefmt="github",
        headers="keys",
    )
)

# Shapley value + Y平均數 = 預測值

cc = shap_values.sum() + y.mean(), clf.predict(df[:1])[0]
print(cc)

# (22.905200000000004, 22.9052)

# 自行計算 Shapley value

from itertools import combinations
import scipy


# 計算特定組合的邊際貢獻
def pred_tree(clf, coalition, row, node=0):
    left_node = clf.tree_.children_left[node]
    right_node = clf.tree_.children_right[node]
    is_leaf = left_node == right_node

    if is_leaf:
        return clf.tree_.value[node].squeeze()

    feature = row.index[clf.tree_.feature[node]]
    if feature in coalition:
        if row.loc[feature] <= clf.tree_.threshold[node]:
            # go left
            return pred_tree(clf, coalition, row, node=left_node)
        else:  # go right
            return pred_tree(clf, coalition, row, node=right_node)

    # take weighted average of left and right
    wl = clf.tree_.n_node_samples[left_node] / clf.tree_.n_node_samples[node]
    wr = clf.tree_.n_node_samples[right_node] / clf.tree_.n_node_samples[node]
    value = wl * pred_tree(clf, coalition, row, node=left_node)
    value += wr * pred_tree(clf, coalition, row, node=right_node)
    return value


# 計算特定組合的平均邊際貢獻
def make_value_function(clf, row, col):
    def value(c):
        marginal_gain = pred_tree(clf, c + [col], row) - pred_tree(clf, c, row)
        num_coalitions = scipy.special.comb(len(row) - 1, len(c))
        return marginal_gain / num_coalitions

    return value


# 各種組合
def make_coalitions(row, col):
    rest = [x for x in row.index if x != col]
    for i in range(len(rest) + 1):
        for x in combinations(rest, i):
            yield list(x)


# 計算 Shapley value
def compute_shap(clf, row, col):
    v = make_value_function(clf, row, col)
    return sum([v(coal) / len(row) for coal in make_coalitions(row, col)])


# 顯示 Shapley value
print(
    tabulate.tabulate(
        pd.DataFrame(
            {
                "shap_value": shap_values.squeeze(),
                "my_shap": [
                    compute_shap(clf, df[:1].T.squeeze(), x) for x in df.columns
                ],
                "feature_value": df[:1].values.squeeze(),
            },
            index=df.columns,
        ),
        tablefmt="github",
        headers="keys",
    )
)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 11_06_shap_test

# SHAP套件測試
# An introduction to explainable AI with Shapley values

import shap
from sklearn.preprocessing import StandardScaler

# 載入資料集

df = pd.read_csv("./data/ca_housing.csv")
cc = df.head()
print(cc)

# 資料清理

# 刪除 missing value
df.dropna(inplace=True)

X = df.drop(["median_house_value", "ocean_proximity"], axis=1)
y = df["median_house_value"]

# 模型訓練與評估

# scaler = StandardScaler()
# X2 = scaler.fit_transform(X)
# X = pd.DataFrame(X2, columns=X.columns)

linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

linear_regression.fit(X, y)  # 學習訓練.fit

print("Model coefficients:")
print(X.shape)
print(X.shape[1])
for i in range(X.shape[1]):
    print(X.columns[i], "=", linear_regression.coef_[i].round(5))

# 單一特徵影響力

feature_name = "median_income"
X100 = shap.utils.sample(X, 100)
shap.partial_dependence_plot(
    feature_name,
    linear_regression.predict,
    X100,
    ice=False,
    model_expected_value=True,
    feature_expected_value=True,
)

# 衡量特徵Shapley value

sample_ind = 20  # 第 21 筆資料
explainer = shap.Explainer(linear_regression.predict, X100)
shap_values = explainer(X)
shap.partial_dependence_plot(
    feature_name,
    linear_regression.predict,
    X100,
    model_expected_value=True,
    feature_expected_value=True,
    ice=False,
    shap_values=shap_values[sample_ind : sample_ind + 1, :],
)

# Exact explainer: 20434it [01:32, 205.74it/s]

# 以單一特徵所有資料的Shapley value繪製散佈圖

shap.plots.scatter(shap_values[:, feature_name])
show()

# 單一資料的特徵影響力(Local Feature Importance)

cc = X.iloc[sample_ind]
print(cc)

shap.plots.waterfall(shap_values[sample_ind], max_display=14)
show()

# 加法模型(Generalized additive models, GAM)

# !pip install interpret

import interpret.glassbox

# 使用 Boosting 演算法
model_ebm = interpret.glassbox.ExplainableBoostingRegressor(interactions=0)

model_ebm.fit(X, y)  # 學習訓練.fit

# 加法模型 Shapley value
explainer_ebm = shap.Explainer(model_ebm.predict, X100)
shap_values_ebm = explainer_ebm(X)

# 特徵影響力
fig, ax = shap.partial_dependence_plot(
    feature_name,
    model_ebm.predict,
    X100,
    model_expected_value=True,
    feature_expected_value=True,
    show=False,
    ice=False,
    shap_values=shap_values_ebm[sample_ind : sample_ind + 1, :],  # 第 21 筆資料
)
show()

shap.plots.scatter(shap_values_ebm[:, feature_name])
show()

shap.plots.waterfall(shap_values_ebm[sample_ind])
show()

shap.plots.beeswarm(shap_values_ebm)
show()

shap.plots.bar(shap_values_ebm)
show()

shap.initjs()
shap.plots.force(shap_values_ebm[sample_ind])

print("ddddddd")
sys.exit()

"""
Visualization omitted, Javascript library not loaded!
Have you run `initjs()` in this notebook? If this notebook was from another user you must also trust this notebook (File -> Trust notebook). If you are viewing this notebook on github the Javascript has been stripped for security. If you are using JupyterLab this error is because a JupyterLab extension has not yet been written.
"""

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


# sklearn.utils.shuffle 把array打亂
X = np.array([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]])
print(X)

X = sklearn.utils.shuffle(X, random_state=9487)
print(X)
