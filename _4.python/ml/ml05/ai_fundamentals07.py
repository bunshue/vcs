import os
import sys
import time
import math
import random
import matplotlib.pyplot as plt
import numpy as np

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示

print("------------------------------------------------------------")  # 60個

from sklearn.datasets import make_blobs

X, y = make_blobs(n_samples=200,
                  n_features=2,
                  centers=4,
                  cluster_std=1,
                  center_box=(-10.0, 10.0),
                  shuffle=True,
                  random_state=1);

plt.figure(figsize=(6,4), dpi=144)
plt.xticks(())
plt.yticks(())
plt.scatter(X[:, 0], X[:, 1], s=20, marker='o');

plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn.cluster import KMeans

n_clusters = 3
kmean = KMeans(n_clusters=n_clusters)
kmean.fit(X);
print("kmean: k={}, cost={}".format(n_clusters, int(kmean.score(X))))

labels = kmean.labels_
centers = kmean.cluster_centers_
markers = ['o', '^', '*']
colors = ['r', 'b', 'y']

plt.figure(figsize=(6,4), dpi=144)
plt.xticks(())
plt.yticks(())

# 画样本
for c in range(n_clusters):
    cluster = X[labels == c]
    plt.scatter(cluster[:, 0], cluster[:, 1], 
                marker=markers[c], s=20, c=colors[c])
# 画出中心点
plt.scatter(centers[:, 0], centers[:, 1],
            marker='o', c="white", alpha=0.9, s=300)
for i, c in enumerate(centers):
    plt.scatter(c[0], c[1], marker='$%d$' % i, s=50, c=colors[i])

plt.show()

print("------------------------------------------------------------")  # 60個

def fit_plot_kmean_model(n_clusters, X):
    plt.xticks(())
    plt.yticks(())

    # 使用 k-均值算法进行拟合
    kmean = KMeans(n_clusters=n_clusters)
    kmean.fit_predict(X)

    labels = kmean.labels_
    centers = kmean.cluster_centers_
    markers = ['o', '^', '*', 's']
    colors = ['r', 'b', 'y', 'k']

    # 计算成本
    score = kmean.score(X)
    plt.title("k={}, score={}".format(n_clusters, (int)(score)))

    # 画样本
    for c in range(n_clusters):
        cluster = X[labels == c]
        plt.scatter(cluster[:, 0], cluster[:, 1], 
                    marker=markers[c], s=20, c=colors[c])
    # 画出中心点
    plt.scatter(centers[:, 0], centers[:, 1],
                marker='o', c="white", alpha=0.9, s=300)
    for i, c in enumerate(centers):
        plt.scatter(c[0], c[1], marker='$%d$' % i, s=50, c=colors[i])

from sklearn.cluster import KMeans

n_clusters = [2, 3, 4]

plt.figure(figsize=(10, 3), dpi=144)
for i, c in enumerate(n_clusters):
    plt.subplot(1, 3, i + 1)
    fit_plot_kmean_model(c, X)

plt.show()

print("------------------------------------------------------------")  # 60個

from time import time
from sklearn.datasets import load_files

""" 無檔案
print("loading documents ...")
t = time()
docs = load_files('datasets/clustering/data')
print("summary: {0} documents in {1} categories.".format(
    len(docs.data), len(docs.target_names)))
print("done in {0} seconds".format(time() - t))

from sklearn.feature_extraction.text import TfidfVectorizer

max_features = 20000
print("vectorizing documents ...")
t = time()
vectorizer = TfidfVectorizer(max_df=0.4, 
                             min_df=2, 
                             max_features=max_features, 
                             encoding='latin-1')
X = vectorizer.fit_transform((d for d in docs.data))
print("n_samples: %d, n_features: %d" % X.shape)
print("number of non-zero features in sample [{0}]: {1}".format(
    docs.filenames[0], X[0].getnnz()))
print("done in {0} seconds".format(time() - t))

print("------------------------------------------------------------")  # 60個

from sklearn.cluster import KMeans

print("clustering documents ...")
t = time()
n_clusters = 4
kmean = KMeans(n_clusters=n_clusters, 
               max_iter=100,
               tol=0.01,
               verbose=1,
               n_init=3)
kmean.fit(X);
print("kmean: k={}, cost={}".format(n_clusters, int(kmean.inertia_)))
print("done in {0} seconds".format(time() - t))

print(len(kmean.labels_))

cc = kmean.labels_[1000:1010]
print(cc)

cc = docs.filenames[1000:1010]
print(cc)

print("------------------------------------------------------------")  # 60個

from __future__ import print_function

print("Top terms per cluster:")

order_centroids = kmean.cluster_centers_.argsort()[:, ::-1]

terms = vectorizer.get_feature_names()
for i in range(n_clusters):
    print("Cluster %d:" % i, end='')
    for ind in order_centroids[i, :10]:
        print(' %s' % terms[ind], end='')
    print()

a = np.array([[20, 10, 30, 40], [100, 300, 200, 400], [1, 5, 3, 2]])
cc = a.argsort()[:, ::-1]
print(cc)

a = np.array([10, 30, 20, 40])
cc = a.argsort()[::-1]
print(cc)

print("------------------------------------------------------------")  # 60個

from sklearn import metrics

label_true = np.random.randint(1, 4, 6)
label_pred = np.random.randint(1, 4, 6)
print("Adjusted Rand-Index for random sample: %.3f"
      % metrics.adjusted_rand_score(label_true, label_pred))
label_true = [1, 1, 3, 3, 2, 2]
label_pred = [3, 3, 2, 2, 1, 1]
print("Adjusted Rand-Index for same structure sample: %.3f"
      % metrics.adjusted_rand_score(label_true, label_pred))

from sklearn import metrics

label_true = [1, 1, 2, 2]
label_pred = [2, 2, 1, 1]
print("Homogeneity score for same structure sample: %.3f"
      % metrics.homogeneity_score(label_true, label_pred))
label_true = [1, 1, 2, 2]
label_pred = [0, 1, 2, 3]
print("Homogeneity score for each cluster come from only one class: %.3f"
      % metrics.homogeneity_score(label_true, label_pred))
label_true = [1, 1, 2, 2]
label_pred = [1, 2, 1, 2]
print("Homogeneity score for each cluster come from two class: %.3f"
      % metrics.homogeneity_score(label_true, label_pred))
label_true = np.random.randint(1, 4, 6)
label_pred = np.random.randint(1, 4, 6)
print("Homogeneity score for random sample: %.3f"
      % metrics.homogeneity_score(label_true, label_pred))

from sklearn import metrics

label_true = [1, 1, 2, 2]
label_pred = [2, 2, 1, 1]
print("Completeness score for same structure sample: %.3f"
      % metrics.completeness_score(label_true, label_pred))
label_true = [0, 1, 2, 3]
label_pred = [1, 1, 2, 2]
print("Completeness score for each class assign to only one cluster: %.3f"
      % metrics.completeness_score(label_true, label_pred))
label_true = [1, 1, 2, 2]
label_pred = [1, 2, 1, 2]
print("Completeness score for each class assign to two class: %.3f"
      % metrics.completeness_score(label_true, label_pred))
label_true = np.random.randint(1, 4, 6)
label_pred = np.random.randint(1, 4, 6)
print("Completeness score for random sample: %.3f"
      % metrics.completeness_score(label_true, label_pred))

from sklearn import metrics

label_true = [1, 1, 2, 2]
label_pred = [2, 2, 1, 1]
print("V-measure score for same structure sample: %.3f"
      % metrics.v_measure_score(label_true, label_pred))
label_true = [0, 1, 2, 3]
label_pred = [1, 1, 2, 2]
print("V-measure score for each class assign to only one cluster: %.3f"
      % metrics.v_measure_score(label_true, label_pred))
print("V-measure score for each class assign to only one cluster: %.3f"
      % metrics.v_measure_score(label_pred, label_true))
label_true = [1, 1, 2, 2]
label_pred = [1, 2, 1, 2]
print("V-measure score for each class assign to two class: %.3f"
      % metrics.v_measure_score(label_true, label_pred))

from sklearn import metrics

labels = docs.target
print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels, kmean.labels_))
print("Completeness: %0.3f" % metrics.completeness_score(labels, kmean.labels_))
print("V-measure: %0.3f" % metrics.v_measure_score(labels, kmean.labels_))
print("Adjusted Rand-Index: %.3f"
      % metrics.adjusted_rand_score(labels, kmean.labels_))
print("Silhouette Coefficient: %0.3f"
      % metrics.silhouette_score(X, kmean.labels_, sample_size=1000))
"""

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
