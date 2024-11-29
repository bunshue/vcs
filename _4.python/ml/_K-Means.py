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

from common1 import *
from sklearn import datasets
from sklearn.cluster import KMeans  # 聚類方法, K-平均演算法

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("無 sklearn之kmeans 1")


def kmeans(x, y, cx, cy):
    # 目前功能只是繪群集元素點
    plt.scatter(x, y, color="b")  # 繪製元素點
    plt.scatter(cx, cy, color="r")  # 用紅色繪群集中心
    plt.title("無 sklearn之kmeans 1")
    show()


# 群集中心, 元素的數量, 數據最大範圍
cluster_number = 3  # 群集中心數量
seeds = 50  # 元素數量
limits = 100  # 值在(100, 100)內
# 使用隨機數建立seeds數量的種子元素
x = np.random.randint(0, limits, seeds)
y = np.random.randint(0, limits, seeds)
# 使用隨機數建立cluster_number數量的群集中心
cluster_x = np.random.randint(0, limits, cluster_number)
cluster_y = np.random.randint(0, limits, cluster_number)

kmeans(x, y, cluster_x, cluster_y)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("無 sklearn之kmeans 2")


def length(x1, y1, x2, y2):
    # 計算2點之間的距離
    return int(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)


def clustering(x, y, cx, cy):
    # 對元素執行分群
    clusters = []
    for i in range(cluster_number):  # 建立群集
        clusters.append([])
    for i in range(seeds):  # 為每個點找群集
        distance = INF  # 設定最初距離
        for j in range(cluster_number):  # 計算每個點與群集中心的距離
            dist = length(x[i], y[i], cx[j], cy[j])
            if dist < distance:
                distance = dist
                cluster_index = j  # 分群的索引
        clusters[cluster_index].append([x[i], y[i]])  # 此點加入此索引的群集
    return clusters


def kmeans(x, y, cx, cy):
    # 建立群集和繪製各群集點和線條
    clusters = clustering(x, y, cx, cy)
    plt.scatter(x, y, color="b")  # 繪製元素點
    plt.scatter(cx, cy, color="r")  # 用紅色繪群集中心

    c = ["r", "g", "y"]  # 群集的線條顏色
    for index, node in enumerate(clusters):  # 為每個群集中心建立線條
        linex = []  # 線條的 x 座標
        liney = []  # 線條的 y 座標
        for n in node:
            linex.append([n[0], cx[index]])  # 建立線條x座標串列
            liney.append([n[1], cy[index]])  # 建立線條y座標串列
        color_c = c[index]  # 選擇顏色
        for i in range(len(linex)):
            plt.plot(linex[i], liney[i], color=color_c)  # 為第i群集繪線條
    plt.title("無 sklearn之kmeans 2")
    show()


# 群集中心, 元素的數量, 數據最大範圍
INF = 999  # 假設最大距離
cluster_number = 3  # 群集中心數量
seeds = 50  # 元素數量
limits = 100  # 值在(100, 100)內
# 使用隨機數建立seeds數量的種子元素
x = np.random.randint(0, limits, seeds)
y = np.random.randint(0, limits, seeds)
# 使用隨機數建立cluster_number數量的群集中心
cluster_x = np.random.randint(0, limits, cluster_number)
cluster_y = np.random.randint(0, limits, cluster_number)

kmeans(x, y, cluster_x, cluster_y)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("無 sklearn之kmeans 3")


def length(x1, y1, x2, y2):
    # 計算2點之間的距離
    return int(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)


def clustering(x, y, cx, cy):
    # 對元素執行分群
    clusters = []
    for i in range(cluster_number):  # 建立群集
        clusters.append([])
    for i in range(seeds):  # 為每個點找群集
        distance = INF  # 設定最初距離
        for j in range(cluster_number):  # 計算每個點與群集中心的距離
            dist = length(x[i], y[i], cx[j], cy[j])
            if dist < distance:
                distance = dist
                cluster_index = j  # 分群的索引
        clusters[cluster_index].append([x[i], y[i]])  # 此點加入此索引的群集
    return clusters


def kmeans(x, y, cx, cy):
    # 建立群集和繪製各群集點和線條
    clusters = clustering(x, y, cx, cy)
    plt.scatter(x, y, color="b")  # 繪製元素點
    plt.scatter(cx, cy, color="r")  # 用紅色繪群集中心

    c = ["r", "g", "y"]  # 群集的線條顏色
    for index, node in enumerate(clusters):  # 為每個群集中心建立線條
        linex = []  # 線條的 x 座標
        liney = []  # 線條的 y 座標
        for n in node:
            linex.append([n[0], cx[index]])  # 建立線條x座標串列
            liney.append([n[1], cy[index]])  # 建立線條y座標串列
        color_c = c[index]  # 選擇顏色
        for i in range(len(linex)):
            plt.plot(linex[i], liney[i], color=color_c)  # 為第i群集繪線條
    plt.title("無 sklearn之kmeans 3")
    show()
    return clusters


def get_new_cluster(clusters):
    # 計算各群集中心的點
    new_x = []  # 新群集中心 x 座標
    new_y = []  # 新群集中心 y 座標
    for index, node in enumerate(clusters):  # 逐步計算各群集
        nx, ny = 0, 0
        for n in node:
            nx += n[0]
            ny += n[1]
        new_x.append([])
        new_x[index] = int(nx / len(node))  # 計算群集中心 x 座標
        new_y.append([])
        new_y[index] = int(ny / len(node))  # 計算群集中心 y 座標
    return new_x, new_y


# 群集中心, 元素的數量, 數據最大範圍
INF = 999  # 假設最大距離
cluster_number = 3  # 群集中心數量

seeds = 50  # 元素數量
limits = 100  # 值在(100, 100)內
# 或
seeds = 100  # 元素數量
limits = 500  # 值在(300, 300)內

# 使用隨機數建立seeds數量的種子元素
x = np.random.randint(0, limits, seeds)
y = np.random.randint(0, limits, seeds)
# 使用隨機數建立cluster_number數量的群集中心
cluster_x = np.random.randint(0, limits, cluster_number)
cluster_y = np.random.randint(0, limits, cluster_number)

clusters = kmeans(x, y, cluster_x, cluster_y)

while True:  # 收斂迴圈
    new_x, new_y = get_new_cluster(clusters)
    x_list = list(cluster_x)  # 將np.array轉成串列
    y_list = list(cluster_y)  # 將np.array轉成串列
    print("目前x :", new_x)
    print("目前y :", new_y)
    print("目標x :", x_list)
    print("目標y :", y_list)
    if new_x == x_list and new_y == y_list:  # 如果相同代表收斂完成
        print("收斂完成")
        break
    else:
        cluster_x = new_x  # 否則重新收斂
        cluster_y = new_y
        clusters = kmeans(x, y, cluster_x, cluster_y)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("無 sklearn之kmeans 4")

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
    show()

    plt.subplot(122)
    colors = ["r", "b", "g"]
    for key, values in cls_.items():
        cx = []
        cy = []
        for v in values:
            cx.append(v[0])
            cy.append(v[1])
        plt.scatter(cx, cy, color=colors[key])

    show()


do_k_means()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("聚類算法 KMeans")

from sklearn.datasets import make_blobs

N = 100
GROUPS = 3

print("make_blobs,", N, "個樣本, 分成", GROUPS, "群")
X, y, centers = make_blobs(
    n_samples=N,
    centers=GROUPS,
    cluster_std=1,
    n_features=2,
    random_state=9487,
    return_centers=True,
)
# cluster_std 為 資料標準差
# n_features 為 資料的維度

print(GROUPS, "群 的中心點 :")
print(centers)
print("資料的維度", X.shape, y.shape)
# print(y.shape)

clf = KMeans(n_clusters=3, random_state=9487)  # K-平均演算法, 分成3群

y_pred = clf.fit_predict(X)  # 訓練

print("真實答案 :", y)
print("預測結果 :", y_pred)
print("預測差值 :", y_pred - y)

cc = np.sum(y_pred.reshape(-1, 1) == y.reshape(-1, 1))
print(cc)
cc = cc * 1.0 / len(y)
print("正確率 :", cc)

plt.figure(figsize=(12, 6))
plt.subplot(121)
plt.scatter(X[:, 0], X[:, 1], c="b")
plt.title("原始資料 3 群")

plt.subplot(122)
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.title("KMeans分群結果")

show()

print("------------------------------------------------------------")  # 60個

# 隨機生成 N 個點，然後用 k-means 將他們分成 5 群
N = 50
x = np.random.rand(N, 2)  # N X 2 亂數陣列

clf = KMeans(n_clusters=5)  # K-平均演算法, 分成5群

clf.fit(x)  # 學習訓練.fit

# 訓練好的結果, 放在神秘的 labels_ 之下
cc = clf.labels_
print("訓練好的結果 :\n", cc)

plt.figure(figsize=(12, 6))
plt.subplot(121)
plt.scatter(x[:, 0], x[:, 1], c="b")
plt.title("原始資料")

plt.subplot(122)
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
plt.title("KMeans分群結果")

show()

print("------------------------------------------------------------")  # 60個

# 隨機生成 N 個點，然後用 k-means 將他們分成 5 群
N = 100
x = np.random.rand(N, 2)  # N X 2 亂數陣列


clf = KMeans(n_clusters=3)  # K-平均演算法, 分成3群

clf.fit(x)  # 學習訓練.fit

# 訓練好的結果, 放在神秘的 labels_ 之下
cc = clf.labels_
print("訓練好的結果 :\n", cc)

print("預測.predict, 這電腦自己分的, 答案自然 100% 相同")
y_pred = clf.predict(x)  # 預測.predict
print(y_pred)

# clf.labels_ 與 clf.predict(x) 必相同

x0 = y0 = np.arange(-0.2, 1.2, 0.02)
xm, ym = np.meshgrid(x0, y0)

P = np.c_[xm.ravel(), ym.ravel()]
z = clf.predict(P)  # 預測.predict
Z = z.reshape(xm.shape)

plt.figure(figsize=(12, 6))
plt.subplot(131)
plt.scatter(x[:, 0], x[:, 1], s=50)
plt.title("原始資料")
plt.subplot(132)
plt.scatter(x[:, 0], x[:, 1], s=50, c=cc)  # 自動配色
plt.title("KMeans分群結果")
plt.subplot(133)
plt.contourf(xm, ym, Z, alpha=0.3)
plt.scatter(x[:, 0], x[:, 1], s=50, c=cc, cmap="Paired")
plt.title("KMeans分群結果")
show()

print("------------------------------------------------------------")  # 60個
"""
Mean Shift 自動分類
有時我們甚至不想告訴電腦, 你自動分類應該分成幾類。
這時 Mean Shift 可以幫我們
"""

plt.figure(num="Means Shift 自動分類", figsize=(12, 8))

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

show()

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

print("KMeans")

filename = "data/Iris2.csv"
df = pd.read_csv(filename)

df = df.drop("Id", axis=1)
print(df.head())
print(df.info())

df = df.drop_duplicates()  # 刪除重複列

df.reset_index(drop=True)  # 將列索引重新編號

s = {"Iris-setosa": 0, "Iris-versicolor": 1, "Iris-virginica": 2}

df["Species"] = df["Species"].map(s)

print(df.head())
print(df.info())

df_X = df[["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]]
k = 1

clf = KMeans(n_clusters=k)  # K-平均演算法, 分成k群

clf.fit(df_X)  # 學習訓練.fit

print("分群準確性:", clf.inertia_)

# 分群準確性: 663.895238095238

s = []
for k in range(1, 15):
    clf = KMeans(n_clusters=k)  # K-平均演算法, 分成k群
    clf.fit(df_X)  # 學習訓練.fit
    s.append(clf.inertia_)

print(s)

# [663.895238095238, 151.77145833333336, 77.91989035087718, 56.64237065018315, 45.816421929824564, 38.380978808131445, 34.1150969785575, 29.771330051212402, 27.730401211361738, 25.771261585636587, 24.236889472455648, 22.68941452991453, 21.258278047116285, 19.7686452991453]

# 看視覺化圖表決定參數K值
df_kmeans = pd.DataFrame()
df_kmeans["inertia_"] = s
df_kmeans.index = list(range(1, 15))
df_kmeans.plot(grid=True)
show()

k = 3
clf = KMeans(n_clusters=k)  # K-平均演算法, 分成k群

clf.fit(df_X)  # 學習訓練.fit

print("分群的預測結果：")
pred = clf.fit_predict(df_X)
print(pred)

# 決定模型
# 進行分群預測

df1 = df_X.copy()
df1["pred"] = pred

c = {0: "r", 1: "g", 2: "b"}

df1["colors"] = df1["pred"].map(c)
df1.plot(kind="scatter", x="SepalLengthCm", y="SepalWidthCm", c=df1["colors"])

show()

# 給一朵鳶尾花的4個特徵值：「花萼長度 6.6公分、花萼寬度 3.1公分、花瓣長度 5.2公分、花寬度 2.4公分」

new = [[6.6, 3.1, 5.2, 2.4]]

v = clf.predict(new)  # 預測.predict

print("預測結果為：", v)

# 預測結果為： [0]

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

df = pd.DataFrame(
    {
        "length": [51, 46, 51, 45, 51, 50, 33, 38, 37, 33, 33, 21, 23, 24],
        "weight": [
            10.2,
            8.8,
            8.1,
            7.7,
            9.8,
            7.2,
            4.8,
            4.6,
            3.5,
            3.3,
            4.3,
            2.0,
            1.0,
            2.0,
        ],
    }
)
k = 3

clf = KMeans(n_clusters=k, random_state=9487)  # K-平均演算法, 分成k群

clf.fit(df)  # 學習訓練.fit

print(clf.labels_)

colmap = np.array(["r", "g", "y"])
plt.scatter(df["length"], df["weight"], color=colmap[clf.labels_])

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 建立 300 個點, n_features = 2
data, label = datasets.make_blobs(n_samples=300, n_features=2)

clf = KMeans(n_clusters=3)  # K-平均演算法, 分成3群

clf.fit(data)  # 將數據帶入物件, 做群集分析  # 學習訓練.fit
print(clf.labels_)  # 列印群集類別標籤
print(clf.cluster_centers_)  # 列印群集中心

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 建立 300 個點, n_features = 2
data, label = datasets.make_blobs(n_samples=300, n_features=2)

clf = KMeans(n_clusters=3)  # K-平均演算法, 分成3群
clf.fit(data)  # 將數據帶入物件, 做群集分析  # 學習訓練.fit
print(clf.labels_)  # 列印群集類別標籤
print(clf.cluster_centers_)  # 列印群集中心

# 繪圓點, 圓點用黑色外框, 使用標籤 labels_ 區別顏色,
plt.scatter(data[:, 0], data[:, 1], marker="o", c=clf.labels_)
# 用紅色標記群集中心
plt.scatter(
    clf.cluster_centers_[:, 0], clf.cluster_centers_[:, 1], marker="*", color="red"
)
plt.title("無監督學習")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 建立 300 個點, n_features = 2, centers = 3
data, label = datasets.make_blobs(
    n_samples=300, n_features=2, centers=3, random_state=9487
)

clf = KMeans(n_clusters=3)  # K-平均演算法, 分成3群
clf.fit(data)  # 將數據帶入物件, 做群集分析
print(clf.labels_)  # 列印群集類別標籤
print(clf.cluster_centers_)  # 列印群集中心

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 建立 300 個點, n_features = 2, centers = 3
data, label = datasets.make_blobs(
    n_samples=300, n_features=2, centers=3, random_state=9487
)

clf = KMeans(n_clusters=3)  # K-平均演算法, 分成3群
clf.fit(data)  # 將數據帶入物件, 做群集分析
print(clf.labels_)  # 列印群集類別標籤
print(clf.cluster_centers_)  # 列印群集中心

# 繪圓點, 圓點用黑色外框, 使用標籤 labels_ 區別顏色,
plt.scatter(data[:, 0], data[:, 1], marker="o", c=clf.labels_)
# 用紅色標記群集中心
plt.scatter(
    clf.cluster_centers_[:, 0], clf.cluster_centers_[:, 1], marker="*", color="red"
)
plt.title("無監督學習", fontsize=16)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

# 01-kmeans-Mat.py

import numpy as np
import matplotlib.pyplot as plt

X = np.array([[1, 1], [1.1, 1.1], [1.2, 1.2], [2, 2], [2.1, 2.1], [2.2, 2.2]])
y = [1, 1, 1, 0, 0, 0]

plt.axis([0, 3, 0, 3])
plt.plot(X[:3, 0], X[:3, 1], "yx")
plt.plot(X[3:, 0], X[3:, 1], "g.")
plt.ylabel("H cm")
plt.xlabel("W cm")
plt.legend(("A", "B"), loc="upper right")
plt.show()


print("------------------------------------------------------------")  # 60個

# 02-kmeans-Lemon.py

import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn import metrics

X = np.array([[1, 1], [1.1, 1.1], [1.2, 1.2], [2, 2], [2.1, 2.1], [2.2, 2.2]])
y = [1, 1, 1, 0, 0, 0]
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
print("集群中心的坐標:", kmeans.cluster_centers_)
print("預測:", kmeans.predict(X))
print("實際:", y)
print("預測[1, 1],[2.3,2.1]:", kmeans.predict([[1, 1], [2.3, 2.1]]))

plt.axis([0, 3, 0, 3])
plt.plot(X[:3, 0], X[:3, 1], "yx")
plt.plot(X[3:, 0], X[3:, 1], "g.")
plt.plot(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], "ro")
plt.xticks(())
plt.yticks(())
plt.show()

print("------------------------------------------------------------")  # 60個

# 03-Iris-kmeans.py

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn import metrics

# Load the diabetes dataset
iris = datasets.load_iris()

iris_X_train, iris_X_test, iris_y_train, iris_y_test = train_test_split(
    iris.data, iris.target, test_size=0.2
)

# KMeans 演算法
kmeans = KMeans(n_clusters=3)
kmeans_fit = kmeans.fit(iris_X_train)

print("實際", iris_y_train)
print("預測", kmeans_fit.labels_)
# 調整標籤的數字
iris_y_train[iris_y_train == 1] = 11
iris_y_train[iris_y_train == 0] = 1
iris_y_train[iris_y_train == 11] = 0
print("調整", iris_y_train)

score = metrics.accuracy_score(iris_y_train, kmeans.predict(iris_X_train))
print("準確率:{0:f}".format(score))

print("------------------------------------------------------------")  # 60個

# 04-Iris-kmeans-Slipt.py

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn import metrics

# Load the diabetes dataset
iris = datasets.load_iris()

iris_X_train, iris_X_test, iris_y_train, iris_y_test = train_test_split(
    iris.data, iris.target, test_size=0.2
)

# KMeans 演算法
kmeans = KMeans(n_clusters=3)
kmeans.fit(iris_X_train)
y_predict = kmeans.predict(iris_X_train)


x1 = iris_X_train[:, 0]
y1 = iris_X_train[:, 1]
plt.scatter(x1, y1, c=y_predict, cmap="viridis")

centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c="black", s=200, alpha=0.5)
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


"""
#plt.autoscale()
# 我們可以檢查一下, 確認答案是不是真的一樣!
print(np.array_equal(clf.labels_, clf.predict(x)))  # 預測.predict
"""
