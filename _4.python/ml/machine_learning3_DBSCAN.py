"""
DBSCAN Clustering

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

font_filename = "D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

import tensorflow as tf
from sklearn import metrics
from sklearn import datasets
from sklearn import preprocessing
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.callbacks import TensorBoard
from tensorflow.keras.models import model_from_json
from sklearn.metrics import accuracy_score
from sklearn.datasets import make_blobs  # 生成分類資料
from sklearn.datasets import make_moons  # 生成非線性資料 上/下弦月資料


def show():
    plt.show()
    pass


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

X, y = make_moons(n_samples=200, noise=0.05)
plt.scatter(X[:, 0], X[:, 1])
show()

# 模型訓練，繪製結果

db = DBSCAN(eps=0.2, min_samples=5, metric="euclidean")

y_pred = db.fit_predict(X)
print("預測結果 :\n", y_pred, sep="")

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

centers = [[1, 1], [-1, -1], [1, -1]]
X, labels_true = make_blobs(n_samples=750, centers=centers, cluster_std=0.4)

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
print(f"Homogeneity: {metrics.homogeneity_score(labels_true, labels):.3f}")
print(f"Completeness: {metrics.completeness_score(labels_true, labels):.3f}")
print(f"V-measure: {metrics.v_measure_score(labels_true, labels):.3f}")
print(f"Adjusted Rand Index: {metrics.adjusted_rand_score(labels_true, labels):.3f}")
print(
    "Adjusted Mutual Information:"
    f" {metrics.adjusted_mutual_info_score(labels_true, labels):.3f}"
)

# [平均]輪廓係數 silhouette_score
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

# DBSCAN Clustering

# Clustering

# Make moon-shaped and doughnut-shaped data

from sklearn import cluster
from sklearn import datasets

n_samples = 1500
noisy_circles, circle_labels = datasets.make_circles(
    n_samples=n_samples, factor=0.5, noise=0.05
)
noisy_moons, moon_labels = datasets.make_moons(n_samples=n_samples, noise=0.1)

noisy_moons = np.array(noisy_moons)
noisy_circles = np.array(noisy_circles)

plt.figure(figsize=(8, 5))
plt.title("Half-moon shaped data")
plt.scatter(noisy_moons[:, 0], noisy_moons[:, 1])
show()

plt.figure(figsize=(8, 5))
plt.title("Concentric circles of data points")
plt.scatter(noisy_circles[:, 0], noisy_circles[:, 1])
show()

# Can k-means identify the right clusters?

km = cluster.KMeans(n_clusters=2)

km.fit(noisy_moons)

plt.figure(figsize=(8, 5))
plt.title("Half-moon shaped data")
plt.scatter(noisy_moons[:, 0], noisy_moons[:, 1], c=km.labels_)
show()

km.fit(noisy_circles)

plt.figure(figsize=(8, 5))
plt.title("Concentric circles of data points")
plt.scatter(noisy_circles[:, 0], noisy_circles[:, 1], c=km.labels_)
show()

# How does DBSCAN perform?

dbs = cluster.DBSCAN(eps=0.1)

dbs.fit(noisy_moons)

plt.figure(figsize=(8, 5))
plt.title("Half-moon shaped data")
plt.scatter(noisy_moons[:, 0], noisy_moons[:, 1], c=dbs.labels_)
show()

dbs.fit(noisy_circles)

plt.figure(figsize=(8, 5))
plt.title("Concentric circles of data points")
plt.scatter(noisy_circles[:, 0], noisy_circles[:, 1], c=dbs.labels_)
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
