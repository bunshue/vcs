"""
machine_learning3_AffinityPropagation

Affinity_Propagation

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
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.callbacks import TensorBoard
from tensorflow.keras.models import model_from_json
from sklearn.metrics import accuracy_score

import sklearn.linear_model
from sklearn import datasets
from sklearn.datasets import make_blobs  # 集群資料集
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn import metrics
from matplotlib.colors import ListedColormap

from sklearn import tree


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Affinity Propagation Clustering Technique

from sklearn.cluster import AffinityPropagation
from sklearn import metrics
from sklearn.datasets import make_blobs  # 集群資料集

"""
# Generate sample data
centers = [[1, 1], [-1, -1], [1, -1]]
X, labels_true = make_blobs(
    n_samples=300, centers=centers, cluster_std=0.5, random_state=0
)

X.shape

plt.figure(figsize=(8, 5))
plt.scatter(X[:, 0], X[:, 1], edgecolors="k", c="orange", s=75)
plt.grid(True)
plt.xticks()
plt.yticks()
show()

# Clustering

# Compute Affinity Propagation
af_model = AffinityPropagation(preference=-50).fit(X)
cluster_centers_indices = af_model.cluster_centers_indices_
labels = af_model.labels_
n_clusters_ = len(cluster_centers_indices)

# Number of detected clusters and their centers

print("Number of clusters detected by the algorithm:", n_clusters_)

print("Cluster centers detected at:\n\n", X[cluster_centers_indices])

plt.figure(figsize=(8, 5))
plt.scatter(X[:, 0], X[:, 1], edgecolors="k", c=af_model.labels_, s=75)
plt.grid(True)
plt.xticks()
plt.yticks()
show()

# Homogeneity

print("Homogeneity score:", metrics.homogeneity_score(labels_true, labels))

# Completeness

print("Completeness score:", metrics.completeness_score(labels_true, labels))

# Prediction

x_new = [0.5, 0.4]
x_pred = af_model.predict([x_new])[0]

print("New point ({},{}) will belong to cluster {}".format(x_new[0], x_new[1], x_pred))

x_new = [-0.5, 0.4]
x_pred = af_model.predict([x_new])[0]

print("New point ({},{}) will belong to cluster {}".format(x_new[0], x_new[1], x_pred))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
# Time complexity and model quality as the data size grows

n_samples = [10, 20, 50, 100, 200, 500, 1000, 2000, 3000, 5000, 7500, 10000]
centers = [[1, 1], [-1, -1], [1, -1]]
t_aff = []
homo_aff = []
complete_aff = []

for i in n_samples:
    X, labels_true = make_blobs(
        n_samples=i, centers=centers, cluster_std=0.5, random_state=0
    )
    t1 = time.time()
    af_model = AffinityPropagation(preference=-50, max_iter=50).fit(X)
    t2 = time.time()
    t_aff.append(t2 - t1)
    homo_aff.append(metrics.homogeneity_score(labels_true, af_model.labels_))
    complete_aff.append(metrics.completeness_score(labels_true, af_model.labels_))

plt.figure(figsize=(8, 5))
plt.title("Time complexity of Affinity Propagation")
plt.scatter(n_samples, t_aff, edgecolors="k", c="green", s=100)
plt.plot(n_samples, t_aff, "k--", lw=3)
plt.grid(True)
plt.xticks()
plt.xlabel("Number of samples")
plt.yticks()
plt.ylabel("Time taken for model (sec)")
show()

plt.figure(figsize=(8, 5))
plt.title("Homogeneity score with data set size")
plt.scatter(n_samples, homo_aff, edgecolors="k", c="green", s=100)
plt.plot(n_samples, homo_aff, "k--", lw=3)
plt.grid(True)
plt.xticks()
plt.xlabel("Number of samples")
plt.yticks()
plt.ylabel("Homogeneity score")
show()

plt.figure(figsize=(8, 5))
plt.title("Completeness score with data set size")
plt.scatter(n_samples, complete_aff, edgecolors="k", c="green", s=100)
plt.plot(n_samples, complete_aff, "k--", lw=3)
plt.grid(True)
plt.xticks()
plt.xlabel("Number of samples")
plt.yticks()
plt.ylabel("Completeness score")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# How well the cluster detection works in the presence of noise? Can damping help?

noise = [
    0.01,
    0.05,
    0.1,
    0.2,
    0.3,
    0.4,
    0.5,
    0.6,
    0.7,
    0.8,
    0.9,
    1.0,
    1.25,
    1.5,
    1.75,
    2.0,
]
n_clusters = []
for i in noise:
    centers = [[1, 1], [-1, -1], [1, -1]]
    X, labels_true = make_blobs(
        n_samples=200, centers=centers, cluster_std=i, random_state=101
    )
    af_model = AffinityPropagation(
        preference=-50, max_iter=500, convergence_iter=15, damping=0.5
    ).fit(X)
    n_clusters.append(len(af_model.cluster_centers_indices_))

print("Detected number of clusters:", n_clusters)
plt.figure(figsize=(8, 5))
plt.title("Cluster detection with noisy data for low damping=0.5")
plt.scatter(noise, n_clusters, edgecolors="k", c="green", s=100)
plt.grid(True)
plt.xticks()
plt.xlabel("Noise std.dev")
plt.yticks()
plt.ylabel("Number of clusters detected")
show()

# Detected number of clusters: [200, 67, 1, 68, 60, 3, 3, 3, 4, 4, 5, 6, 6, 7, 9, 9]

noise = [
    0.01,
    0.05,
    0.1,
    0.2,
    0.3,
    0.4,
    0.5,
    0.6,
    0.7,
    0.8,
    0.9,
    1.0,
    1.25,
    1.5,
    1.75,
    2.0,
]
n_clusters = []
for i in noise:
    centers = [[1, 1], [-1, -1], [1, -1]]
    X, labels_true = make_blobs(
        n_samples=200, centers=centers, cluster_std=i, random_state=101
    )
    af_model = AffinityPropagation(
        preference=-50, max_iter=500, convergence_iter=15, damping=0.9
    ).fit(X)
    n_clusters.append(len(af_model.cluster_centers_indices_))

print("Detected number of clusters:", n_clusters)
plt.figure(figsize=(8, 5))
plt.title("Cluster detection with noisy data for high damping=0.9")
plt.scatter(noise, n_clusters, edgecolors="k", c="green", s=100)
plt.grid(True)
plt.xticks()
plt.xlabel("Noise std.dev")
plt.yticks([i for i in range(2, 10)])
plt.ylabel("Number of clusters detected")
show()

# Detected number of clusters: [3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 5, 5, 5, 6, 6, 7]

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Affinity Propagation Clustering Technique

from sklearn.cluster import AffinityPropagation
from sklearn import metrics

# Generate sample data
centers = [[1, 1], [-1, -1], [1, -1]]
X, labels_true = make_blobs(
    n_samples=300, centers=centers, cluster_std=0.5, random_state=0
)

X.shape

# (300, 2)

plt.figure(figsize=(8, 5))
plt.scatter(X[:, 0], X[:, 1], edgecolors="k", c="orange", s=75)
plt.xticks()
plt.yticks()
show()

# Clustering

# Compute Affinity Propagation
af_model = AffinityPropagation(preference=-50).fit(X)
cluster_centers_indices = af_model.cluster_centers_indices_
labels = af_model.labels_
n_clusters_ = len(cluster_centers_indices)

# Number of detected clusters and their centers

print("Number of clusters detected by the algorithm:", n_clusters_)

# Number of clusters detected by the algorithm: 3

print("Cluster centers detected at:\n\n", X[cluster_centers_indices])

plt.figure(figsize=(8, 5))
plt.scatter(X[:, 0], X[:, 1], edgecolors="k", c=af_model.labels_, s=75)
plt.xticks()
plt.yticks()
show()

# Homogeneity

print("Homogeneity score:", metrics.homogeneity_score(labels_true, labels))

# Homogeneity score: 0.871559529839

# Completeness

print("Completeness score:", metrics.completeness_score(labels_true, labels))

# Completeness score: 0.871585975337

# Prediction

x_new = [0.5, 0.4]
x_pred = af_model.predict([x_new])[0]

print("New point ({},{}) will belong to cluster {}".format(x_new[0], x_new[1], x_pred))

# New point (0.5,0.4) will belong to cluster 0

x_new = [-0.5, 0.4]
x_pred = af_model.predict([x_new])[0]

print("New point ({},{}) will belong to cluster {}".format(x_new[0], x_new[1], x_pred))

# New point (-0.5,0.4) will belong to cluster 2

# Time complexity and model quality as the data size grows

n_samples = [10, 20, 50, 100, 200, 500, 1000, 2000, 3000, 5000, 7500, 10000]
centers = [[1, 1], [-1, -1], [1, -1]]
t_aff = []
homo_aff = []
complete_aff = []

for i in n_samples:
    X, labels_true = make_blobs(
        n_samples=i, centers=centers, cluster_std=0.5, random_state=0
    )
    t1 = time.time()
    af_model = AffinityPropagation(preference=-50, max_iter=50).fit(X)
    t2 = time.time()
    t_aff.append(t2 - t1)
    homo_aff.append(metrics.homogeneity_score(labels_true, af_model.labels_))
    complete_aff.append(metrics.completeness_score(labels_true, af_model.labels_))

plt.figure(figsize=(8, 5))
plt.title("Time complexity of Affinity Propagation")
plt.scatter(n_samples, t_aff, edgecolors="k", c="green", s=100)
plt.plot(n_samples, t_aff, "k--", lw=3)
plt.xticks()
plt.xlabel("Number of samples")
plt.yticks()
plt.ylabel("Time taken for model (sec)")
show()

plt.figure(figsize=(8, 5))
plt.title("Homogeneity score with data set size")
plt.scatter(n_samples, homo_aff, edgecolors="k", c="green", s=100)
plt.plot(n_samples, homo_aff, "k--", lw=3)
plt.xticks()
plt.xlabel("Number of samples")
plt.yticks()
plt.ylabel("Homogeneity score")
show()

plt.figure(figsize=(8, 5))
plt.title("Completeness score with data set size")
plt.scatter(n_samples, complete_aff, edgecolors="k", c="green", s=100)
plt.plot(n_samples, complete_aff, "k--", lw=3)
plt.xticks()
plt.xlabel("Number of samples")
plt.yticks()
plt.ylabel("Completeness score")
show()

# How well the cluster detection works in the presence of noise? Can damping help?

noise = [
    0.01,
    0.05,
    0.1,
    0.2,
    0.3,
    0.4,
    0.5,
    0.6,
    0.7,
    0.8,
    0.9,
    1.0,
    1.25,
    1.5,
    1.75,
    2.0,
]
n_clusters = []
for i in noise:
    centers = [[1, 1], [-1, -1], [1, -1]]
    X, labels_true = make_blobs(
        n_samples=200, centers=centers, cluster_std=i, random_state=101
    )
    af_model = AffinityPropagation(
        preference=-50, max_iter=500, convergence_iter=15, damping=0.5
    ).fit(X)
    n_clusters.append(len(af_model.cluster_centers_indices_))

print("Detected number of clusters:", n_clusters)
plt.figure(figsize=(8, 5))
plt.title("Cluster detection with noisy data for low damping=0.5\n")
plt.scatter(noise, n_clusters, edgecolors="k", c="green", s=100)
plt.xticks()
plt.xlabel("Noise std.dev")
plt.yticks()
plt.ylabel("Number of clusters detected")
show()

# Detected number of clusters: [200, 67, 1, 68, 60, 3, 3, 3, 4, 4, 5, 6, 6, 7, 9, 9]

noise = [
    0.01,
    0.05,
    0.1,
    0.2,
    0.3,
    0.4,
    0.5,
    0.6,
    0.7,
    0.8,
    0.9,
    1.0,
    1.25,
    1.5,
    1.75,
    2.0,
]
n_clusters = []
for i in noise:
    centers = [[1, 1], [-1, -1], [1, -1]]
    X, labels_true = make_blobs(
        n_samples=200, centers=centers, cluster_std=i, random_state=101
    )
    af_model = AffinityPropagation(
        preference=-50, max_iter=500, convergence_iter=15, damping=0.9
    ).fit(X)
    n_clusters.append(len(af_model.cluster_centers_indices_))

print("Detected number of clusters:", n_clusters)

plt.figure(figsize=(8, 5))
plt.title("Cluster detection with noisy data for high damping=0.9\n")
plt.scatter(noise, n_clusters, edgecolors="k", c="green", s=100)
plt.xticks()
plt.xlabel("Noise std.dev")
plt.yticks([i for i in range(2, 10)])
plt.ylabel("Number of clusters detected")
show()

# Detected number of clusters: [3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 5, 5, 5, 6, 6, 7]

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
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
