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
from matplotlib.colors import ListedColormap

from sklearn import tree


def show():
    plt.show()
    pass


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
plt.title("Half-moon shaped data", fontsize=18)
plt.grid(True)
plt.scatter(noisy_moons[:, 0], noisy_moons[:, 1])
plt.show()

plt.figure(figsize=(8, 5))
plt.title("Concentric circles of data points", fontsize=18)
plt.grid(True)
plt.scatter(noisy_circles[:, 0], noisy_circles[:, 1])
plt.show()

# Can k-means identify the right clusters?

km = cluster.KMeans(n_clusters=2)

km.fit(noisy_moons)
"""
KMeans(algorithm='auto', copy_x=True, init='k-means++', max_iter=300,
    n_clusters=2, n_init=10, n_jobs=1, precompute_distances='auto',
    random_state=None, tol=0.0001, verbose=0)
"""
plt.figure(figsize=(8, 5))
plt.title("Half-moon shaped data", fontsize=18)
plt.grid(True)
plt.scatter(noisy_moons[:, 0], noisy_moons[:, 1], c=km.labels_)
plt.show()

km.fit(noisy_circles)
"""
KMeans(algorithm='auto', copy_x=True, init='k-means++', max_iter=300,
    n_clusters=2, n_init=10, n_jobs=1, precompute_distances='auto',
    random_state=None, tol=0.0001, verbose=0)
"""
plt.figure(figsize=(8, 5))
plt.title("Concentric circles of data points", fontsize=18)
plt.grid(True)
plt.scatter(noisy_circles[:, 0], noisy_circles[:, 1], c=km.labels_)
plt.show()

# How does DBSCAN perform?

dbs = cluster.DBSCAN(eps=0.1)

dbs.fit(noisy_moons)
"""
DBSCAN(algorithm='auto', eps=0.1, leaf_size=30, metric='euclidean',
    min_samples=5, n_jobs=1, p=None)
"""
plt.figure(figsize=(8, 5))
plt.title("Half-moon shaped data", fontsize=18)
plt.grid(True)
plt.scatter(noisy_moons[:, 0], noisy_moons[:, 1], c=dbs.labels_)
plt.show()

dbs.fit(noisy_circles)
"""
DBSCAN(algorithm='auto', eps=0.1, leaf_size=30, metric='euclidean',
    min_samples=5, n_jobs=1, p=None)
"""
plt.figure(figsize=(8, 5))
plt.title("Concentric circles of data points", fontsize=18)
plt.grid(True)
plt.scatter(noisy_circles[:, 0], noisy_circles[:, 1], c=dbs.labels_)
plt.show()


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
