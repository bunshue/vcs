"""
機器學習 K-Means

K-平均演算法（英文：k-means clustering）

K-Means 自動分類

# K-Means 會自動分類!
# 我們介紹一個很好用的 unsupervised learning, 叫 K-Means。
# 我們可以指定把我們資料分成幾類, 然後它就會快速分好!

K-means Clustering 集群分析

k-平均演算法（英文：k-means clustering，以下簡稱為 k-means ）
是一種非監督式的學習方法，其主要的目標是對未標記的資料進行分群。

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

from sklearn.cluster import KMeans

print("------------------------------------------------------------")  # 60個

print("聚類算法 KMeans")

from sklearn.datasets import make_blobs

N = 10
GROUPS = 3

print("make_blobs,", N, "個樣本, 分成", GROUPS, "群")
X, y, centers = make_blobs(
    n_samples=N, centers=GROUPS, random_state=9487, return_centers=True
)

print(GROUPS, "群 的中心點 :")
print(centers)
print(X.shape)

color = "b"
plt.scatter(X[:, 0], X[:, 1], c=color)
plt.show()

"""
X, y, centers = make_blobs(
    n_samples=N, centers=GROUPS, cluster_std=1, n_features=2, return_centers=True
)
"""

from sklearn.cluster import KMeans  # 聚類方法

y_pred = KMeans(n_clusters=3, random_state=9487).fit_predict(X)  # 訓練

plt.scatter(X[:, 0], X[:, 1], c=y_pred)

plt.show()

print("------------------------------------------------------------")  # 60個

# 隨機生成 N 個點，然後用 k-means 將他們分成 5 群
N = 50
x = np.random.rand(N, 2)  # N X 2 亂數陣列

clf = KMeans(n_clusters=5)  # K-平均演算法, 分成5群

clf.fit(x)  # 學習訓練.fit

# 訓練好的結果, 放在神秘的 labels_ 之下
cc = clf.labels_
print("訓練好的結果 :\n", cc)

# 將點逐一染色
for i in range(0, N):
    if cc[i] == 0:
        plt.scatter(x[i][0], x[i][1], color="red")
    elif cc[i] == 1:
        plt.scatter(x[i][0], x[i][1], color="blue")
    elif cc[i] == 2:
        plt.scatter(x[i][0], x[i][1], color="green")
    elif cc[i] == 3:
        plt.scatter(x[i][0], x[i][1], color="pink")
    elif cc[i] == 4:
        plt.scatter(x[i][0], x[i][1], color="orange")

plt.grid()

plt.show()

print("------------------------------------------------------------")  # 60個

plt.figure(num="K-平均演算法", figsize=(12, 6))

# 隨機生成 N 個點，然後用 k-means 將他們分成 5 群
N = 100
x = np.random.rand(N, 2)  # N X 2 亂數陣列

plt.subplot(131)
plt.scatter(x[:, 0], x[:, 1], s=50)
plt.title("原始資料")

clf = KMeans(n_clusters=3)  # K-平均演算法, 分成3群

clf.fit(x)  # 學習訓練.fit

# 訓練好的結果, 放在神秘的 labels_ 之下
cc = clf.labels_
print("訓練好的結果 :\n", cc)

print("預測.predict, 這電腦自己分的, 答案自然 100% 相同")
y_pred = clf.predict(x)  # 預測.predict
print(y_pred)

# clf.labels_ 與 clf.predict(x) 必相同

plt.subplot(132)
plt.scatter(x[:, 0], x[:, 1], s=50, c=cc)
plt.title("訓練好的結果")

x0 = y0 = np.arange(-0.2, 1.2, 0.02)
xm, ym = np.meshgrid(x0, y0)

P = np.c_[xm.ravel(), ym.ravel()]
z = clf.predict(P)  # 預測.predict
Z = z.reshape(xm.shape)
plt.subplot(133)
plt.contourf(xm, ym, Z, alpha=0.3)
plt.scatter(x[:, 0], x[:, 1], s=50, c=cc, cmap="Paired")
plt.title("訓練好的結果")

plt.show()

print("------------------------------------------------------------")  # 60個

plt.figure(num="Means Shift", figsize=(12, 8))

# Mean Shift 自動分類
# 有時我們甚至不想告訴電腦, 你自動分類應該分成幾類。這時 Mean Shift 可以幫我們。

# 隨機生成 N 個點，然後用 Mean Shift 將他們分成 ? 群
N = 100
x = np.random.rand(N, 2)  # N X 2 亂數陣列

from sklearn.cluster import MeanShift

# 打開 MeanShift 函數學習機, 這裡的 bandwidth 是控制分類要寬鬆一點, 還是嚴一點

clf = MeanShift(bandwidth=0.2)

clf.fit(x)  # 學習訓練.fit
cc = clf.labels_  # 訓練好的結果

x0 = y0 = np.arange(-0.2, 1.2, 0.02)
xm, ym = np.meshgrid(x0, y0)

P = np.c_[xm.ravel(), ym.ravel()]
z = clf.predict(P)  # 預測.predict
Z = z.reshape(xm.shape)

plt.subplot(231)
plt.scatter(x[:, 0], x[:, 1], s=50, c=cc, cmap="Paired")
plt.contourf(xm, ym, Z, alpha=0.3, cmap="Paired")
plt.title("標準 Mean Shift分類")

print("------------------------------")  # 30個

# 畫完整分類

gd = np.array([[i, j] for i in np.arange(-4, 4, 0.4) for j in np.arange(-3, 3, 0.4)])
gdc = clf.predict(gd)  # 預測.predict

plt.subplot(232)
plt.scatter(gd[:, 0], gd[:, 1], s=50, cmap=plt.cm.coolwarm, c=gdc)
# plt.scatter(gd[:, 0], gd[:, 1], s=50, cmap=plt.cm.prism, c=gdc)  # cmap
# plt.scatter(gd[:, 0], gd[:, 1], s=50, cmap=plt.cm.Set1, c=gdc)  # cmap
plt.title("訓練好的結果")

print("------------------------------")  # 30個


# 觀察 bandwidth 對分類的影響
def my_mean_shift(bw=0.2):
    clf = MeanShift(bandwidth=bw)
    clf.fit(x)  # 學習訓練.fit
    cc = clf.labels_  # 訓練好的結果

    x0 = y0 = np.arange(-0.2, 1.2, 0.02)
    xm, ym = np.meshgrid(x0, y0)

    P = np.c_[xm.ravel(), ym.ravel()]
    z = clf.predict(P)  # 預測.predict
    Z = z.reshape(xm.shape)

    plt.scatter(x[:, 0], x[:, 1], c=cc, cmap="Paired")
    plt.contourf(xm, ym, Z, alpha=0.3, cmap="Paired")
    plt.title("Mean Shift, bw =" + str(bw))


plt.subplot(233)
my_mean_shift(0.1)

plt.subplot(234)
my_mean_shift(0.3)

plt.subplot(235)
my_mean_shift(0.4)

plt.subplot(236)
my_mean_shift(0.05)

plt.show()

print("------------------------------------------------------------")  # 60個

import pickle

print("把模型儲存起來")

f = open("tmp_clf.pkl", "wb")
pickle.dump(clf, f)
f.close()

print("把模型讀出來")
f = open("tmp_clf.pkl", "rb")
clf2 = pickle.load(f)

# 預測
print(clf2.predict([[3, 4]]))  # 預測.predict

f.close()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

cl_num = 3
data_num = 20
thr = [0.00001, 0.00001, 0.00001]


def dist(x, y, mu_x, mu_y):
    return (mu_x - x) ** 2 + (mu_y - y) ** 2


def cluster(x, y, mu_x, mu_y):
    cls_ = dict()
    for i in range(data_num):
        dists = []
        for j in range(cl_num):
            distant = dist(x[i], y[i], mu_x[j], mu_y[j])
            dists.append(distant)
        cl = dists.index(min(dists))
        if cl not in cls_:
            cls_[cl] = [(x[i], y[i])]
        elif cl in cls_:
            cls_[cl].append((x[i], y[i]))

    return cls_


def re_mu(cls_, mu_x, mu_y):
    new_muX = []
    new_muY = []

    for key, values in cls_.items():
        if len(values) == 0:
            values.append([mu_x[key], mu_y[key]])

        sum_x = 0
        sum_y = 0
        for v in values:
            sum_x += v[0]
            sum_y += v[1]

        new_mu_x = sum_x / len(values)
        new_mu_y = sum_y / len(values)

        new_muX.append(round(new_mu_x, 2))
        new_muY.append(round(new_mu_y, 2))
    return new_muX, new_muY


def do_k_means():
    x = np.random.randint(0, 500, data_num)
    y = np.random.randint(0, 500, data_num)

    mu_x = np.random.randint(0, 500, cl_num)
    mu_y = np.random.randint(0, 500, cl_num)

    cls_ = cluster(x, y, mu_x, mu_y)

    new_muX, new_muY = re_mu(cls_, mu_x, mu_y)

    while (
        any((abs(np.array(new_muX) - np.array(mu_x)) > thr)) != False
        or any((abs(np.array(new_muY) - np.array(mu_y)) > thr)) != False
    ):
        mu_x = new_muX
        mu_y = new_muY
        cls_ = cluster(x, y, mu_x, mu_y)
        new_muX, new_muY = re_mu(cls_, mu_x, mu_y)

    print("Done")

    plt.subplot(121)

    plt.scatter(x, y)
    plt.scatter(new_muX, new_muY)
    # plt.show()

    plt.subplot(122)
    colors = ["r", "b", "g"]
    for key, values in cls_.items():
        cx = []
        cy = []
        for v in values:
            cx.append(v[0])
            cy.append(v[1])
        plt.scatter(cx, cy, color=colors[key])

    plt.show()


print("自己做 K-Means")
do_k_means()

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
"""
#plt.autoscale()

# 我們可以檢查一下, 確認答案是不是真的一樣!
print(np.array_equal(clf.labels_, clf.predict(x)))  # 預測.predict



"""
