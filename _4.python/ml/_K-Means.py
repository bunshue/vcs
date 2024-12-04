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
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn import metrics


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("無 sklearn之kmeans 1")


def kmeans(x, y, cx, cy):
    # 目前功能只是繪群集元素點
    plt.scatter(x, y, color="b")  # 繪製元素點
    plt.scatter(cx, cy, color="r")  # 標記群集中心
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
    plt.scatter(cx, cy, color="r")  # 標記群集中心

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
    plt.scatter(cx, cy, color="r")  # 標記群集中心

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

print("最簡易 K-平均演算法(KMeans) 任意資料分四群並畫圖")

print("任意隨機資料")
X = np.random.rand(50, 2)

# 畫出來
plt.scatter(X[:, 0], X[:, 1], s=50)
show()

CLUSTERS = 4  # 要分成的群數
clf = KMeans(n_clusters=CLUSTERS)  # K-平均演算法

clf.fit(X)  # 學習訓練.fit

# 畫出來看一下結果，好像還真得有模有樣的
plt.scatter(X[:, 0], X[:, 1], c=clf.labels_)
show()

# 放一些新的資料進去看看，點變多了！
a = np.random.rand(20, 2)
X_add = np.row_stack((X, a))
plt.scatter(X_add[:, 0], X_add[:, 1])
show()

# 看一看我們的 k-Means 分的怎麼樣
predict_label = clf.predict(X_add)
plt.scatter(X_add[:, 0], X_add[:, 1], c=predict_label)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("聚類算法 KMeans")

from sklearn.datasets import make_blobs

# 建立資料一, 使用 random
# 隨機生成 N 個點
N = 100
X = np.random.rand(N, 2)  # N X 2 亂數陣列

# 建立資料二, 使用 make_blobs
N = 100
M = 2  # n_features, 特徵數(資料的維度)
GROUPS = 3  # centers, 分群數

print("make_blobs,", N, "個樣本, ", M, "個特徵, 分成", GROUPS, "群")
X, y, centers = make_blobs(
    n_samples=N,
    centers=GROUPS,
    cluster_std=1,
    n_features=M,
    random_state=9487,
    return_centers=True,
)
# cluster_std 為 資料標準差
# n_features 為 資料的維度

print(GROUPS, "群 的中心點 :")
print(centers)
print("資料的維度", X.shape, y.shape)

CLUSTERS = 3  # 要分成的群數
clf = KMeans(n_clusters=CLUSTERS, random_state=9487)  # K-平均演算法

clf.fit(X)  # 學習訓練.fit

print("群集類別標籤(訓練好的結果) :\n", clf.labels_)
print("集群中心的坐標:", clf.cluster_centers_)
print("分群準確性:", clf.inertia_)

y_pred = clf.predict(X)  # 預測.predict
# 預測.predict 會與 clf.labels_ 相同
print("檢查是否相同")
print(np.array_equal(clf.labels_, clf.predict(X)))

# 一次做完訓練+預測 same
# y_pred = clf.fit_predict(X)  # 學習訓練 + 預測 .fit_predict

print("真實答案 :", y)
print("預測結果 :", y_pred)
print("預測差值 :", y_pred - y)

cc = np.sum(y_pred.reshape(-1, 1) == y.reshape(-1, 1))
print(cc)
cc = cc * 1.0 / len(y)
print("正確率 :", cc)

plt.figure(figsize=(12, 6))

plt.subplot(131)
plt.scatter(X[:, 0], X[:, 1], c="b")
plt.axis([-15, 15, -15, 15])
plt.title("原始資料 3 群")

plt.subplot(132)
# 繪圓點, 圓點用黑色外框, 使用標籤 labels_ 區別顏色,
plt.scatter(X[:, 0], X[:, 1], marker="o", c=clf.labels_)
# 標記群集中心
plt.scatter(
    clf.cluster_centers_[:, 0],
    clf.cluster_centers_[:, 1],
    marker="*",
    s=200,
    c="r",
    alpha=0.8,
)
plt.axis([-15, 15, -15, 15])
plt.title("KMeans分群結果")

plt.subplot(133)

# 畫分區域ST
x0 = y0 = np.arange(-15, 15, 0.1)
xm, ym = np.meshgrid(x0, y0)
P = np.c_[xm.ravel(), ym.ravel()]
z = clf.predict(P)  # 預測.predict
Z = z.reshape(xm.shape)
plt.contourf(xm, ym, Z, alpha=0.3)  # 畫分區域
# 畫分區域SP

# 繪圓點, 圓點用黑色外框, 使用標籤 labels_ 區別顏色,
plt.scatter(X[:, 0], X[:, 1], marker="o", c=clf.labels_)
# 標記群集中心
plt.scatter(
    clf.cluster_centers_[:, 0],
    clf.cluster_centers_[:, 1],
    marker="*",
    s=200,
    c="r",
    alpha=0.8,
)
plt.axis([-15, 15, -15, 15])
plt.title("KMeans分群結果")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("Mean Shift 自動分類, 電腦自己決定要分成幾類")

plt.figure(num="Means Shift 自動分類", figsize=(12, 8))

# 隨機生成 N 個點，然後用 Mean Shift 將他們分成 ? 群
N = 100
X = np.random.rand(N, 2)  # N X 2 亂數陣列

from sklearn.cluster import MeanShift

# 打開 MeanShift 函數學習機, 這裡的 bandwidth 是控制分類要寬鬆一點, 還是嚴一點

clf = MeanShift(bandwidth=0.2)

clf.fit(X)  # 學習訓練.fit

print("群集類別標籤(訓練好的結果) :\n", clf.labels_)
print("集群中心的坐標:", clf.cluster_centers_)

y_pred = clf.predict(X)  # 預測.predict
# 預測.predict 會與 clf.labels_ 相同

plt.subplot(231)
plt.scatter(X[:, 0], X[:, 1], s=50)  # 畫點
plt.axis([-0.1, 1.1, -0.1, 1.1])
plt.title("原始資料")

plt.subplot(232)
# 畫分區域ST
x0 = y0 = np.arange(-0.2, 1.2, 0.02)
xm, ym = np.meshgrid(x0, y0)
P = np.c_[xm.ravel(), ym.ravel()]
z = clf.predict(P)  # 預測.predict
Z = z.reshape(xm.shape)
plt.contourf(xm, ym, Z, alpha=0.3, cmap="Paired")
# 畫分區域SP
plt.scatter(X[:, 0], X[:, 1], s=50, c=clf.labels_, cmap="Paired")  # 畫點
plt.axis([-0.1, 1.1, -0.1, 1.1])
plt.title("標準 Mean Shift分類, bw=0.2")

print("------------------------------")  # 30個

# 畫完整分類
plt.subplot(233)

gd = np.array([[i, j] for i in np.arange(-4, 4, 0.4) for j in np.arange(-3, 3, 0.4)])
gdc = clf.predict(gd)  # 預測.predict

plt.scatter(gd[:, 0], gd[:, 1], s=50, cmap=plt.cm.coolwarm, c=gdc)
# plt.scatter(gd[:, 0], gd[:, 1], s=50, cmap=plt.cm.prism, c=gdc)  # cmap
# plt.scatter(gd[:, 0], gd[:, 1], s=50, cmap=plt.cm.Set1, c=gdc)  # cmap
plt.axis([-4.5, 4.2, -3.4, 3.2])
plt.title("訓練好的結果")

print("------------------------------")  # 30個


# 觀察 bandwidth 對分類的影響
def my_mean_shift(bw=0.2):
    clf = MeanShift(bandwidth=bw)
    clf.fit(X)  # 學習訓練.fit
    # 畫分區域ST
    x0 = y0 = np.arange(-0.2, 1.2, 0.02)
    xm, ym = np.meshgrid(x0, y0)
    P = np.c_[xm.ravel(), ym.ravel()]
    z = clf.predict(P)  # 預測.predict
    Z = z.reshape(xm.shape)
    plt.contourf(xm, ym, Z, alpha=0.3, cmap="Paired")
    # 畫分區域SP
    plt.scatter(X[:, 0], X[:, 1], c=clf.labels_, cmap="Paired")
    plt.axis([-0.1, 1.1, -0.1, 1.1])
    plt.title("Mean Shift, bw=" + str(bw))


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

filename = "data/Iris2.csv"
df = pd.read_csv(filename)
"""
print(df)
print(df.head())
print(df.info())
"""
df = df.drop("Id", axis=1)  # 刪除 Id 欄位

df = df.drop_duplicates()  # 刪除重複列
df.reset_index(drop=True)  # 將列索引重新編號

s = {"Iris-setosa": 0, "Iris-versicolor": 1, "Iris-virginica": 2}
df["Species"] = df["Species"].map(s)  # 將 Species 欄位的 字串 對應 數值
# print(df.head())

# 取前四欄位當作訓練資料
df_X = df[["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]]
# print(df_X.head())

# 轉折判斷法(Elbow)

distortions = []
# 測試 分群 1~15 群的失真
for k in range(1, 15):
    CLUSTERS = k  # 要分成的群數
    clf = KMeans(n_clusters=CLUSTERS)  # K-平均演算法
    clf.fit(df_X)  # 學習訓練.fit
    print("k =", k, ", 分群準確性:", clf.inertia_)
    distortions.append(clf.inertia_)

print("分1~14群的 分群準確性 clf.inertia_ :\n", distortions)

# 看視覺化圖表決定參數K值
plt.plot(range(1, 15), distortions, color="r", marker="o", markersize=8, label="分群準確性")
plt.xlabel("集群數量")
plt.ylabel("失真")
plt.grid()
plt.legend()

show()

CLUSTERS = 3  # 要分成的群數
clf = KMeans(n_clusters=CLUSTERS)  # K-平均演算法

clf.fit(df_X)  # 學習訓練.fit

print("群集類別標籤(訓練好的結果) :\n", clf.labels_)
print("集群中心的坐標:", clf.cluster_centers_)
print("分群準確性:", clf.inertia_)

y_pred = clf.predict(df_X)  # 預測.predict
# 預測.predict 會與 clf.labels_ 相同
# print("分群的預測結果：", y_pred)

print("預測")
# 給一朵鳶尾花的4個特徵值
# 「花萼長度 6.6 公分、花萼寬度 3.1 公分、花瓣長度 5.2 公分、花寬度 2.4 公分」
xx = [[6.6, 3.1, 5.2, 2.4]]
y_pred = clf.predict(xx)  # 預測.predict
print("預測結果為：", y_pred)

colmap = np.array(["r", "g", "b"])
plt.scatter(df_X["SepalLengthCm"], df_X["SepalWidthCm"], color=colmap[clf.labels_])
# 畫預測點
plt.scatter(6.6, 3.1, s=300, c="m")
plt.xlabel("花萼長度(公分)")
plt.ylabel("花萼寬度(公分)")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

iris = datasets.load_iris()
# print(iris.feature_names)

X = iris.data
y = iris.target

CLUSTERS = 3  # 要分成的群數
clf = KMeans(n_clusters=CLUSTERS)  # K-平均演算法

clf.fit(X)  # 學習訓練.fit

print("群集類別標籤(訓練好的結果) :\n", clf.labels_)
print("集群中心的坐標:", clf.cluster_centers_)
print("分群準確性:", clf.inertia_)

# y_pred = clf.predict(X)  # 預測.predict
# 其實就是 clf.labels_
# y_pred = clf.labels_

# 修正標籤錯誤
y_pred = np.choose(clf.labels_, [2, 1, 0]).astype(np.int64)

print("真實答案 :", y)
print("預測結果 :", y_pred)
print("預測差值 :", y_pred - y)

score = metrics.accuracy_score(y, y_pred)
print("準確率:{0:f}".format(score))

# 績效矩陣
import sklearn.metrics as sm

print(sm.accuracy_score(y, y_pred))

# 混淆矩陣
print(sm.confusion_matrix(y, y_pred))

colmap = np.array(["r", "g", "b"])

plt.figure(figsize=(10, 5))

plt.subplot(121)
plt.scatter(X[:, 0], X[:, 1], color=colmap[y])
plt.xlabel("花萼長度(公分)")
plt.ylabel("花萼寬度(公分)")
plt.title("真實分類")

plt.subplot(122)
plt.scatter(X[:, 0], X[:, 1], color=colmap[y_pred])
# plt.scatter(X[:, 0], X[:, 1], c=y_pred, cmap="viridis")
# 標記群集中心
plt.scatter(
    clf.cluster_centers_[:, 0],
    clf.cluster_centers_[:, 1],
    marker="*",
    s=200,
    c="r",
    alpha=0.8,
)
plt.xlabel("花萼長度(公分)")
plt.ylabel("花萼寬度(公分)")
plt.title("K-means分類")

show()

# 花瓣長和花瓣寬對結果的影響分布
plt.scatter(X[:, 2], X[:, 3], c=clf.labels_)
show()

# 花萼長和花萼寬對結果的影響分布
plt.scatter(X[:, 0], X[:, 1], c=clf.labels_)
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 鳶尾花資料集

from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

X, y = datasets.load_iris(return_X_y=True)

print("資料分割")
# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

# 特徵縮放
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

CLUSTERS = 3  # 要分成的群數
clf = KMeans(n_clusters=CLUSTERS, init="k-means++", n_init="auto")  # K-平均演算法

# 有目標的訓練
clf.fit(X_train_std, y_train)  # 學習訓練.fit

# 模型評估

# 計算準確率
y_pred = clf.predict(X_test_std)
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

score = metrics.accuracy_score(y_test, y_pred)
print("準確率:{0:f}".format(score))

print("y_test :\n", y_test)
print("y_pred :\n", y_pred)

print("分群準確性:", clf.inertia_)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 轉折判斷法(Elbow)

# 生成分類資料

from sklearn.datasets import make_blobs

X, y = make_blobs(
    n_samples=150,
    n_features=2,
    centers=3,
    cluster_std=0.5,
    shuffle=True,
    random_state=9487,
)

CLUSTERS = 3  # 要分成的群數
clf = KMeans(
    n_clusters=CLUSTERS,
    init="random",
    n_init=10,
    max_iter=300,
    tol=1e-04,
    random_state=9487,
)  # K-平均演算法

# 顯示失真(Distortion)的程度
y_km = clf.fit_predict(X)  # 學習訓練 + 預測 .fit_predict

print("分群準確性:", clf.inertia_)
print("Distortion: %.2f" % clf.inertia_)

# 轉折判斷法(Elbow)

distortions = []
# 測試 分群 1~15 群的失真
for k in range(1, 15):
    CLUSTERS = k  # 要分成的群數
    clf = KMeans(
        n_clusters=CLUSTERS,
        init="k-means++",
        n_init=10,
        max_iter=300,
        random_state=9487,
    )  # K-平均演算法
    clf.fit(X)  # 學習訓練.fit
    print("k =", k, ", 分群準確性:", clf.inertia_)
    distortions.append(clf.inertia_)

print("分1~14群的 分群準確性 clf.inertia_ :\n", distortions)

# 看視覺化圖表決定參數K值
plt.plot(range(1, 15), distortions, color="r", marker="o", markersize=8, label="分群準確性")
plt.xlabel("集群數量")
plt.ylabel("失真")
plt.grid()
plt.legend()

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# kmeans_optimization_silhouette

# 輪廓圖分析(Silhouette Analysis)

from matplotlib import cm
from sklearn.metrics import silhouette_samples
from sklearn.datasets import make_blobs

# 生成分類資料

X, y = make_blobs(
    n_samples=150,
    n_features=2,
    centers=3,
    cluster_std=0.5,
    shuffle=True,
    random_state=9487,
)

# 訓練模型

CLUSTERS = 2  # 要分成的群數
clf = KMeans(
    n_clusters=CLUSTERS,
    init="k-means++",
    n_init=10,
    max_iter=300,
    tol=1e-04,
    random_state=9487,
)  # K-平均演算法

y_km = clf.fit_predict(X)  # 學習訓練 + 預測 .fit_predict

# 輪廓係數

cluster_labels = np.unique(y_km)
n_clusters = cluster_labels.shape[0]
print("n_clusters =", n_clusters)
silhouette_vals = silhouette_samples(X, y_km, metric="euclidean")
print("silhouette_vals =", silhouette_vals)

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
plt.ylabel("集群")
plt.xlabel("輪廓係數")
plt.title("aaaa1")

show()

# 使用3個集群訓練模型

CLUSTERS = 3  # 要分成的群數
clf = KMeans(
    n_clusters=CLUSTERS,
    init="k-means++",
    n_init=10,
    max_iter=300,
    tol=1e-04,
    random_state=9487,
)  # K-平均演算法

y_km = clf.fit_predict(X)  # 學習訓練 + 預測 .fit_predict

# 繪製輪廓圖

cluster_labels = np.unique(y_km)
n_clusters = cluster_labels.shape[0]
print("n_clusters =", n_clusters)
silhouette_vals = silhouette_samples(X, y_km, metric="euclidean")
print("silhouette_vals =", silhouette_vals)

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
plt.ylabel("集群")
plt.xlabel("輪廓係數")
plt.title("aaaa2")

show()

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
    CLUSTERS = i  # 要分成的群數
    clf = KMeans(
        n_clusters=CLUSTERS,
        init="k-means++",
        n_init=10,
        max_iter=300,
        random_state=9487,
    )  # K-平均演算法
    clf.fit(X)  # 學習訓練.fit
    y_km = clf.fit_predict(X)  # 學習訓練 + 預測 .fit_predict
    silhouette_score_list.append(silhouette_score(X, y_km))
    print(f"{i}:{silhouette_score_list[-1]:.2f}")

print(f"最大值 {np.argmax(silhouette_score_list)+2}: {np.max(silhouette_score_list):.2f}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


"""
#plt.autoscale()


plt.subplots_adjust(hspace=0.5)
plt.subplots_adjust(hspace=0.5)



# 模型評估：資料點與所屬質心距離的平方和
print("分群準確性:", clf.inertia_)



"""
