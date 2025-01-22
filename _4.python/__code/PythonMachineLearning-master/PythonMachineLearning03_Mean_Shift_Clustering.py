"""
Mean_Shift_Clustering

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
from sklearn.datasets import make_blobs  # 集群資料集
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from matplotlib.colors import ListedColormap

from sklearn import tree


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# Mean-shift Clustering Technique

from sklearn.cluster import MeanShift
from sklearn import metrics

# Generate sample data
centers = [[1, 1], [-1, -1], [1, -1]]
X, labels_true = make_blobs(
    n_samples=300, centers=centers, cluster_std=0.4, random_state=101
)

cc = X.shape
print(cc)

plt.figure(figsize=(8, 5))
plt.scatter(X[:, 0], X[:, 1], edgecolors="k", c="orange", s=75)
plt.grid(True)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.show()

# Clustering

ms_model = MeanShift().fit(X)
cluster_centers = ms_model.cluster_centers_
labels = ms_model.labels_
n_clusters = len(cluster_centers)
labels = ms_model.labels_

# Number of detected clusters and their centers

print("Number of clusters detected by the algorithm:", n_clusters)

# Number of clusters detected by the algorithm: 3

print("Cluster centers detected at:\n\n", cluster_centers)

plt.figure(figsize=(8, 5))
plt.scatter(X[:, 0], X[:, 1], edgecolors="k", c=ms_model.labels_, s=75)
plt.grid(True)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.show()

# Homogeneity

print("Homogeneity score:", metrics.homogeneity_score(labels_true, labels))

# Completeness

print("Completeness score:", metrics.completeness_score(labels_true, labels))

# Time complexity and model quality as the data size grows

import time
from tqdm import tqdm

n_samples = [10, 20, 50, 100, 200, 500, 1000, 2000, 3000, 5000, 7500, 10000]
centers = [[1, 1], [-1, -1], [1, -1]]
t_ms = []
homo_ms = []
complete_ms = []

for i in tqdm(n_samples):
    X, labels_true = make_blobs(
        n_samples=i, centers=centers, cluster_std=0.4, random_state=101
    )
    t1 = time.time()
    ms_model = MeanShift().fit(X)
    t2 = time.time()
    t_ms.append(t2 - t1)
    homo_ms.append(metrics.homogeneity_score(labels_true, ms_model.labels_))
    complete_ms.append(metrics.completeness_score(labels_true, ms_model.labels_))

plt.figure(figsize=(8, 5))
plt.title("Time complexity of Mean Shift\n", fontsize=20)
plt.scatter(n_samples, t_ms, edgecolors="k", c="green", s=100)
plt.plot(n_samples, t_ms, "k--", lw=3)
plt.grid(True)
plt.xticks(fontsize=15)
plt.xlabel("Number of samples", fontsize=15)
plt.yticks(fontsize=15)
plt.ylabel("Time taken for model (sec)", fontsize=15)
plt.show()

plt.figure(figsize=(8, 5))
plt.title("Homogeneity score with data set size\n", fontsize=20)
plt.scatter(n_samples, homo_ms, edgecolors="k", c="green", s=100)
plt.plot(n_samples, homo_ms, "k--", lw=3)
plt.grid(True)
plt.xticks(fontsize=15)
plt.xlabel("Number of samples", fontsize=15)
plt.yticks(fontsize=15)
plt.ylabel("Homogeneity score", fontsize=15)
plt.show()

plt.figure(figsize=(8, 5))
plt.title("Completeness score with data set size\n", fontsize=20)
plt.scatter(n_samples, complete_ms, edgecolors="k", c="green", s=100)
plt.plot(n_samples, complete_ms, "k--", lw=3)
plt.grid(True)
plt.xticks(fontsize=15)
plt.xlabel("Number of samples", fontsize=15)
plt.yticks(fontsize=15)
plt.ylabel("Completeness score", fontsize=15)
plt.show()

# How well the cluster detection works in the presence of noise?

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
    ms_model = MeanShift().fit(X)
    n_clusters.append(len(ms_model.cluster_centers_))

print("Detected number of clusters:", n_clusters)
plt.figure(figsize=(8, 5))
plt.title("Cluster detection with noisy data\n", fontsize=20)
plt.scatter(noise, n_clusters, edgecolors="k", c="green", s=100)
plt.grid(True)
plt.xticks(fontsize=15)
plt.xlabel("Noise std.dev", fontsize=15)
plt.yticks(fontsize=15)
plt.ylabel("Number of clusters detected", fontsize=15)
plt.show()

"""
Detected number of clusters: [3, 3, 3, 3, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1]

** We see that the cluster detection works well up to a certain level of noise std. dev, after which the mean of the blobs shifts to the overall centroid and the number of detected clusters tends to 1**
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
