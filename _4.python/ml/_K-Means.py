"""
機器學習 K-Means 自動分類

聚類算法 KMeans

K-平均演算法（k-means clustering）

# 無監督學習
# 我們介紹一個很好用的 unsupervised learning, 叫 K-Means。
# 我們可以指定把我們資料分成幾類, 然後它就會快速分好!

K-means Clustering 集群分析

k-平均演算法（k-means clustering，以下簡稱為 k-means）
是一種非監督式的學習方法，其主要的目標是對未標記的資料進行分群。

Silhouette 黑色剪影

輪廓係數（Silhouette Coefficient），是聚類效果好壞的一種評價方式。
    最佳值為1，最差值為-1。接近0的值表示重疊的群集。
    負值通常表示樣本已分配給錯誤的聚類，因為不同的聚類更為相​​似

silhouette_score   所有樣本的 [平均]輪廓係數
silhouette_samples 所有樣本的       輪廓係數

"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import sklearn
from common1 import *
from sklearn import datasets
from sklearn.cluster import KMeans  # 聚類方法, K-平均演算法
from sklearn.cluster import MeanShift  # 均值偏移_聚類演算法
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn import metrics
from sklearn.datasets import make_blobs  # 集群資料集
from sklearn.datasets import make_moons
from sklearn.metrics import accuracy_score
from sklearn.metrics import silhouette_score
from sklearn.metrics import silhouette_samples


def show():
    plt.show()
    pass


colors = np.array(["r", "g", "b", "y", "m", "c"])
# colors = np.array(["r", "g", "b"])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
""" # 無 sklearn ST
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
print("無 sklearn之kmeans 5")
# kmeans_from_scratch
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

    def evaluate(self, X):
        centroids = []
        centroid_idxs = []
        for x in X:
            dists = euclidean(x, self.centroids)
            centroid_idx = np.argmin(dists)
            centroids.append(self.centroids[centroid_idx])
            centroid_idxs.append(centroid_idx)

        return centroids, centroid_idxs


# 建立資料, 使用 make_blobs
N = 100  # n_samples, 樣本數
M = 2  # n_features, 特徵數(資料的維度)
GROUPS = 5  # centers, 分群數
STD = 0.3  # cluster_std, 資料標準差
print("make_blobs,", N, "個樣本, ", M, "個特徵, 分成", GROUPS, "群")
X_train, true_labels = make_blobs(n_samples=N, centers=GROUPS, random_state=9487)

# 標準化
X_train = sklearn.preprocessing.StandardScaler().fit_transform(X_train)

plt.subplot(121)
# plt.scatter(X_train[:, 0], X_train[:, 1], s=50, c=true_labels)  # 無法指定顏色
for i in range(N):
    plt.scatter(X_train[i, 0], X_train[i, 1], s=50, c=colors[true_labels[i]])

plt.title("原始資料" + str(N) + "點" + str(GROUPS) + "群, 標準化")


CLUSTERS = 5  # 要分成的群數
print("使用KMeans分成", CLUSTERS, "群")
clf = KMeans(n_clusters=CLUSTERS)  # K-平均演算法

clf.fit(X_train)  無答案 無監督學習 群集分析 random  # 學習訓練.fit

class_centers, classification = clf.evaluate(X_train)

plt.subplot(122)

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

X, y = datasets.load_iris(return_X_y=True)

# 標準化
X_train = sklearn.preprocessing.StandardScaler().fit_transform(X)

CLUSTERS = 3  # 要分成的群數
print("使用KMeans分成", CLUSTERS, "群")
clf = KMeans(n_clusters=CLUSTERS)  # K-平均演算法

clf.fit(X_train)  # 學習訓練.fit

# 7

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

print("無 sklearn之kmeans 6")
# simple_kmeans_from_scratch
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
cc = model.predict(10)  # 預測.predict  # 第一組
print(cc)

"""  # 無 sklearn SP
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("無答案 無監督學習 K-means 群集分析 random")

print("K-平均演算法(KMeans) 資料分成3群並畫圖")

# 建立資料, 使用 random, 隨機生成 NX2 個點
N = 100
X = np.random.rand(N, 2)  # N X 2 亂數陣列

CLUSTERS = 3  # 要分成的群數
print("使用KMeans分成", CLUSTERS, "群")
clf = KMeans(n_clusters=CLUSTERS, random_state=9487)  # K-平均演算法

clf.fit(X)  # 學習訓練.fit

plt.figure(figsize=(12, 6))

plt.subplot(131)
plt.scatter(X[:, 0], X[:, 1], s=50, c="r")
plt.title("原始隨機資料100點")

plt.subplot(132)
plt.scatter(X[:, 0], X[:, 1], c=clf.labels_)
# 標記群集中心
plt.scatter(
    clf.cluster_centers_[:, 0],
    clf.cluster_centers_[:, 1],
    marker="*",
    s=200,
    c="r",
    alpha=0.8,
)
plt.title("用KMeans分成3群")

# 再預測500點
N = 500
X_test = np.random.rand(N, 2)
y_pred = clf.predict(X_test)  # 預測.predict

plt.subplot(133)
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred)
# 標記群集中心
plt.scatter(
    clf.cluster_centers_[:, 0],
    clf.cluster_centers_[:, 1],
    marker="*",
    s=200,
    c="r",
    alpha=0.8,
)

# 劃分區域ST
x0 = y0 = np.arange(0, 1.02, 0.02)
xm, ym = np.meshgrid(x0, y0)
P = np.c_[xm.ravel(), ym.ravel()]
z = clf.predict(P)  # 預測.predict
Z = z.reshape(xm.shape)
plt.contourf(xm, ym, Z, alpha=0.3, cmap="Paired")  # 劃分區域, contourf 等高線面積圖
# 劃分區域SP
plt.title("再預測500點+劃分區域")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("有答案 無監督學習 K-means 群集分析 + 準確率分析 make_ dataset")
print("K-平均演算法(KMeans) 資料分成4群並畫圖")

# 建立資料, 使用 make_blobs
N = 100
M = 2  # n_features, 特徵數(資料的維度)
GROUPS = 4  # centers, 分群數
STD = 1  # cluster_std, 資料標準差
print("make_blobs,", N, "個樣本, ", M, "個特徵, 分成", GROUPS, "群")
X, y, centers = make_blobs(
    n_samples=N,
    centers=GROUPS,
    n_features=M,
    cluster_std=STD,
    random_state=9487,
    return_centers=True,
)

print(GROUPS, "群 的中心點 :")
print(centers)
print("資料的維度", X.shape, y.shape)

CLUSTERS = 4  # 要分成的群數
print("使用KMeans分成", CLUSTERS, "群")
clf = KMeans(n_clusters=CLUSTERS, random_state=9487)  # K-平均演算法

clf.fit(X)  # 學習訓練.fit

y_pred = clf.predict(X)  # 預測.predict
# 預測.predict, 其實就是 clf.labels_
# y_pred = clf.labels_

print("檢查是否相同")
print(np.array_equal(clf.labels_, clf.predict(X)))

# 一次做完訓練+預測 same
# y_pred = clf.fit_predict(X)  # 學習訓練 + 預測 .fit_predict

print("真實答案 :\n", y, sep="")
print("預測結果 :\n", y_pred, sep="")
print("預測差值 :\n", y_pred - y, sep="")

cc = np.sum(y_pred.reshape(-1, 1) == y.reshape(-1, 1))
print(cc)
cc = cc * 1.0 / len(y)
print("正確率 :", cc)

plt.figure(figsize=(12, 6))

plt.subplot(131)
plt.scatter(X[:, 0], X[:, 1], s=50, c="b")
# 標記 make_blobs 中心
plt.scatter(
    centers[:, 0],
    centers[:, 1],
    marker=".",
    s=200,
    c="r",
    alpha=0.8,
)
plt.axis([-15, 15, -15, 15])
plt.title("原始資料 4 群+資料中心")

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
plt.title("KMeans分群結果+預測中心")

plt.subplot(133)
# 劃分區域ST
x0 = y0 = np.arange(-15, 15, 0.1)
xm, ym = np.meshgrid(x0, y0)
P = np.c_[xm.ravel(), ym.ravel()]
z = clf.predict(P)  # 預測.predict
Z = z.reshape(xm.shape)
plt.contourf(xm, ym, Z, alpha=0.3, cmap="Paired")  # 劃分區域, contourf 等高線面積圖
# 劃分區域SP
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

print("Mean Shift 自動分類, 電腦自己決定要分成幾類 鳶尾花")

iris = datasets.load_iris()
X = iris.data
y = iris.target

clf = MeanShift()  # 均值偏移_聚類演算法

clf.fit(X)  # 學習訓練.fit

plt.figure(figsize=(10, 6))

plt.subplot(121)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap="viridis")
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.title("真實資料")

plt.subplot(122)
plt.scatter(X[:, 0], X[:, 1], c=clf.labels_, cmap="viridis")
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.title("Mean Shift自動分類")

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("Mean Shift 自動分類, 電腦自己決定要分成幾類 a")

plt.figure(figsize=(12, 8))

# 隨機生成 N 個點，然後用 Mean Shift 將他們分成 ? 群
N = 100
X = np.random.rand(N, 2)  # N X 2 亂數陣列

# 打開 MeanShift 函數學習機, 這裡的 bandwidth 是控制分類要寬鬆一點, 還是嚴一點

clf = MeanShift(bandwidth=0.2)  # 均值偏移_聚類演算法

clf.fit(X)  # 學習訓練.fit

y_pred = clf.predict(X)  # 預測.predict
# 預測.predict, 其實就是 clf.labels_
# y_pred = clf.labels_

plt.subplot(231)
plt.scatter(X[:, 0], X[:, 1], s=50)  # 畫點
plt.axis([-0.1, 1.1, -0.1, 1.1])
plt.title("原始資料")

plt.subplot(232)
# 劃分區域ST
x0 = y0 = np.arange(-0.2, 1.2, 0.02)
xm, ym = np.meshgrid(x0, y0)
P = np.c_[xm.ravel(), ym.ravel()]
z = clf.predict(P)  # 預測.predict
Z = z.reshape(xm.shape)
plt.contourf(xm, ym, Z, alpha=0.3, cmap="Paired")  # 劃分區域, contourf 等高線面積圖
# 劃分區域SP
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
    clf = MeanShift(bandwidth=bw)  # 均值偏移_聚類演算法
    clf.fit(X)  # 學習訓練.fit
    # 劃分區域ST
    x0 = y0 = np.arange(-0.2, 1.2, 0.02)
    xm, ym = np.meshgrid(x0, y0)
    P = np.c_[xm.ravel(), ym.ravel()]
    z = clf.predict(P)  # 預測.predict
    Z = z.reshape(xm.shape)
    plt.contourf(xm, ym, Z, alpha=0.3, cmap="Paired")  # 劃分區域, contourf 等高線面積圖
    # 劃分區域SP
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
y_pred = clf2.predict([[3, 4]])  # 預測.predict
print(y_pred)

f.close()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("轉折判斷法(Elbow)")

iris = datasets.load_iris()

X = iris.data
y = iris.target

distortions = []
# 測試 分群 1~11 群的失真
for k in range(1, 11):
    CLUSTERS = k  # 要分成的群數
    print("使用KMeans分成", CLUSTERS, "群")
    clf = KMeans(n_clusters=CLUSTERS)  # K-平均演算法
    clf.fit(X)  # 學習訓練.fit
    print("分", k, "群, 分群準確性 :", clf.inertia_)
    distortions.append(clf.inertia_)

# 看視覺化圖表決定參數K值
plt.plot(range(1, 11), distortions, color="r", marker="o", markersize=8, label="分群準確性")
plt.xlabel("集群數量")
plt.ylabel("失真")
plt.title("轉折判斷法(Elbow)")
plt.grid()
plt.legend()

# 看圖決定要分成幾群

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("Mean Shift 自動分類, 電腦自己決定要分成幾類 b")

centers = [[1, 1], [-1, -1], [1, -1]]

# 建立資料, 使用 make_blobs
N = 300  # n_samples, 樣本數
M = 2  # n_features, 特徵數(資料的維度)
GROUPS = 5  # centers, 分群數
STD = 0.4  # cluster_std, 資料標準差
print("make_blobs,", N, "個樣本, ", M, "個特徵, 分成", GROUPS, "群")
X, labels_true = make_blobs(
    n_samples=N, centers=centers, cluster_std=STD, random_state=9487
)
cc = X.shape
print(cc)

plt.figure(figsize=(8, 5))
plt.scatter(X[:, 0], X[:, 1], edgecolors="k", c="orange", s=75)
plt.grid(True)
plt.xticks()
plt.yticks()
show()

clf = MeanShift()  # 均值偏移_聚類演算法

clf.fit(X)  # 學習訓練.fit

cluster_centers = clf.cluster_centers_  # 群集中心
labels = clf.labels_
n_clusters = len(cluster_centers)
labels = clf.labels_

# Number of detected clusters and their centers

print("Number of clusters detected by the algorithm:", n_clusters)

# Number of clusters detected by the algorithm: 3

print("Cluster centers detected at:\n\n", cluster_centers)

plt.figure(figsize=(8, 5))
plt.scatter(X[:, 0], X[:, 1], edgecolors="k", c=clf.labels_, s=75)
plt.grid(True)
plt.xticks()
plt.yticks()
show()

# Homogeneity
print("Homogeneity score:", metrics.homogeneity_score(labels_true, labels))

# Completeness
print("Completeness score:", metrics.completeness_score(labels_true, labels))

# Time complexity and model quality as the data size grows

n_samples = [10, 20, 50, 100, 200, 500, 1000, 2000, 3000, 5000, 7500, 10000]
centers = [[1, 1], [-1, -1], [1, -1]]
t_ms = []
homo_ms = []
complete_ms = []

for i in n_samples:
    X, labels_true = make_blobs(
        n_samples=i, centers=centers, cluster_std=0.4, random_state=9487
    )
    t1 = time.time()
    clf = MeanShift()  # 均值偏移_聚類演算法
    clf.fit(X)  # 學習訓練.fit
    t2 = time.time()
    t_ms.append(t2 - t1)
    homo_ms.append(metrics.homogeneity_score(labels_true, clf.labels_))
    complete_ms.append(metrics.completeness_score(labels_true, clf.labels_))

plt.figure(figsize=(8, 5))
plt.title("Time complexity of Mean Shift\n")
plt.scatter(n_samples, t_ms, edgecolors="k", c="green", s=100)
plt.plot(n_samples, t_ms, "k--", lw=3)
plt.grid(True)
plt.xticks()
plt.xlabel("Number of samples")
plt.yticks()
plt.ylabel("Time taken for model (sec)")
show()

plt.figure(figsize=(8, 5))
plt.title("Homogeneity score with data set size\n")
plt.scatter(n_samples, homo_ms, edgecolors="k", c="green", s=100)
plt.plot(n_samples, homo_ms, "k--", lw=3)
plt.grid(True)
plt.xticks()
plt.xlabel("Number of samples")
plt.yticks()
plt.ylabel("Homogeneity score")
show()

plt.figure(figsize=(8, 5))
plt.title("Completeness score with data set size\n")
plt.scatter(n_samples, complete_ms, edgecolors="k", c="green", s=100)
plt.plot(n_samples, complete_ms, "k--", lw=3)
plt.grid(True)
plt.xticks()
plt.xlabel("Number of samples")
plt.yticks()
plt.ylabel("Completeness score")
show()

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
        n_samples=200, centers=centers, cluster_std=i, random_state=9487
    )
    clf = MeanShift()  # 均值偏移_聚類演算法
    clf.fit(X)  # 學習訓練.fit
    n_clusters.append(len(clf.cluster_centers_))

print("Detected number of clusters:", n_clusters)
plt.figure(figsize=(8, 5))
plt.title("Cluster detection with noisy data\n")
plt.scatter(noise, n_clusters, edgecolors="k", c="green", s=100)
plt.grid(True)
plt.xticks()
plt.xlabel("Noise std.dev")
plt.yticks()
plt.ylabel("Number of clusters detected")
show()

"""
Detected number of clusters: [3, 3, 3, 3, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1]
We see that the cluster detection works well up to a certain level of noise std. dev, after which the mean of the blobs shifts to the overall centroid and the number of detected clusters tends to 1**
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("對四維的資料 iris 做 KMeans分類")

iris = datasets.load_iris()

X = iris.data
y = iris.target

CLUSTERS = 3  # 要分成的群數
print("使用KMeans分成", CLUSTERS, "群")
clf = KMeans(n_clusters=CLUSTERS)  # K-平均演算法

clf.fit(X)  # 學習訓練.fit

y_pred = clf.predict(X)  # 預測.predict
# 預測.predict, 其實就是 clf.labels_
# y_pred = clf.labels_
# print("分群的預測結果：", y_pred)

print("預測")
# 給一朵鳶尾花的4個特徵值
# 花萼長度 6.6 公分、花萼寬度 3.1 公分、花瓣長度 5.2 公分、花寬度 2.4 公分
xx = [[6.6, 3.1, 5.2, 2.4]]
y_pred = clf.predict(xx)  # 預測.predict
print("預測結果 :\n", y_pred, sep="")

plt.figure(figsize=(12, 6))

plt.subplot(131)
plt.scatter(X[:, 0], X[:, 1], color="b")
plt.xlabel("花萼長度")
plt.ylabel("花萼寬度")
plt.title("原始資料")

plt.subplot(132)
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.xlabel("花萼長度")
plt.ylabel("花萼寬度")
plt.title("原始資料之正確分類")

plt.subplot(133)
# 畫所有資料
plt.scatter(X[:, 0], X[:, 1], color=colors[clf.labels_])

# 標記群集中心
plt.scatter(
    clf.cluster_centers_[:, 0],
    clf.cluster_centers_[:, 1],
    marker="*",
    s=200,
    c="r",
    alpha=0.8,
)
# 畫預測點
plt.scatter(6.6, 3.1, s=300, c="m")
plt.xlabel("花萼長度")
plt.ylabel("花萼寬度")
plt.title("使用 KMeans 分3群")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("對四維的資料 iris 做 KMeans分類")

iris = datasets.load_iris()

X = iris.data
y = iris.target

CLUSTERS = 3  # 要分成的群數
print("使用KMeans分成", CLUSTERS, "群")
clf = KMeans(n_clusters=CLUSTERS)  # K-平均演算法

clf.fit(X)  # 學習訓練.fit

# y_pred = clf.predict(X)  # 預測.predict
# 預測.predict, 其實就是 clf.labels_
# y_pred = clf.labels_

# 修正標籤錯誤
y_pred = np.choose(clf.labels_, [2, 1, 0]).astype(np.int64)

"""
print("真實答案 :\n", y, sep="")
print("預測結果 :\n", y_pred, sep="")
print("預測差值 :\n", y_pred - y, sep="")
"""

score = accuracy_score(y, y_pred)
print("準確率:{0:f}".format(score))

# 績效矩陣
import sklearn.metrics as sm

print(sm.accuracy_score(y, y_pred))

# 混淆矩陣
cm = sm.confusion_matrix(y, y_pred)
print("混淆矩陣 :\n", cm, sep="")

plt.figure(figsize=(12, 6))

plt.subplot(131)
plt.scatter(X[:, 0], X[:, 1], color=colors[y])
plt.xlabel("花萼長度")
plt.ylabel("花萼寬度")
plt.title("真實分類")

plt.subplot(132)
plt.scatter(X[:, 0], X[:, 1], color=colors[y_pred])
# plt.scatter(X[:, 0], X[:, 1], c=clf.labels_) # same
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
plt.xlabel("花萼長度")
plt.ylabel("花萼寬度")
plt.title("使用 KMeans 分3群")

plt.subplot(133)
plt.scatter(X[:, 2], X[:, 3], c=clf.labels_)
plt.xlabel("花瓣長度")
plt.ylabel("花瓣寬度")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("計算準確率, 要先有答案")

iris = datasets.load_iris()

X = iris.data
y = iris.target

CLUSTERS = 3  # 要分成的群數
print("使用KMeans分成", CLUSTERS, "群")
clf = KMeans(n_clusters=CLUSTERS)  # K-平均演算法

clf.fit(X)  # 學習訓練.fit

y_pred = clf.predict(X)  # 預測.predict

print(f"{accuracy_score(y, y_pred)*100:.2f}%")
score = accuracy_score(y, y_pred)
print("準確率:{0:f}".format(score))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("使用 Silhouette 輪廓分析 找出最佳分群數目K")

# Kmeans分群演算法 與 Silhouette 輪廓分析

print("使用較漂亮的資料 6群")

# 建立資料, 使用 make_blobs
N = 1000  # n_samples, 樣本數
M = 2  # n_features, 特徵數(資料的維度)
GROUPS = 6  # centers, 分群數
STD = 0.3  # cluster_std, 資料標準差
print("make_blobs,", N, "個樣本, ", M, "個特徵, 分成", GROUPS, "群")
X, y = make_blobs(
    n_samples=N,
    n_features=M,
    centers=GROUPS,
    cluster_std=STD,
    center_box=(-10.0, 10.0),
    random_state=9487,
)

plt.subplot(221)
plt.scatter(*zip(*X), c=y)  # 頗高檔的寫法
plt.axis([-10, 10, -10, 10])
plt.title("使用較漂亮的資料 6群")

silhouette_avg = []
for i in range(2, 11):
    clf = KMeans(n_clusters=i)  # K-平均演算法
    clf.fit(X)  # 學習訓練.fit
    # y_pred = clf.predict(X)  # 預測.predict same
    y_pred = clf.labels_  # 群集類別標籤
    cc = silhouette_score(X, y_pred)  # 計算輪廓係數
    silhouette_avg.append(cc)

plt.subplot(222)
plt.plot(range(2, 11), silhouette_avg)
plt.axis([1, 12, 0.3, 1.0])

# 由圖可以找到最佳的 n_clusters 值

print("使用較不漂亮的資料 6群")

# 建立資料, 使用 make_blobs
N = 1000  # n_samples, 樣本數
M = 2  # n_features, 特徵數(資料的維度)
GROUPS = 6  # centers, 分群數
STD = 1.3  # cluster_std, 資料標準差
print("make_blobs,", N, "個樣本, ", M, "個特徵, 分成", GROUPS, "群")
X, y = make_blobs(
    n_samples=N,
    n_features=M,
    centers=GROUPS,
    cluster_std=STD,
    center_box=(-10.0, 10.0),
    random_state=9487,
)

plt.subplot(223)
plt.scatter(*zip(*X), c=y)  # 頗高檔的寫法
plt.axis([-10, 10, -10, 10])
plt.title("使用較不漂亮的資料 6群")

silhouette_avg = []
for i in range(2, 11):
    kmeans_fit = KMeans(n_clusters=i)  # K-平均演算法
    kmeans_fit.fit(X)  # 學習訓練.fit
    cc = silhouette_score(X, kmeans_fit.labels_)  # 計算輪廓係數
    silhouette_avg.append(cc)

plt.subplot(224)
plt.plot(range(2, 11), silhouette_avg)
plt.axis([1, 12, 0.3, 1.0])

plt.suptitle("使用 Silhouette 輪廓分析 找出最佳分群數目K")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# kmeans_optimization_silhouette

# 輪廓圖分析(Silhouette Analysis)

# 建立資料, 使用 make_blobs
N = 30  # n_samples, 樣本數
M = 2  # n_features, 特徵數(資料的維度)
GROUPS = 3  # centers, 分群數
STD = 0.5  # cluster_std, 資料標準差
print("make_blobs,", N, "個樣本, ", M, "個特徵, 分成", GROUPS, "群")
X, y = make_blobs(
    n_samples=N,
    n_features=M,
    centers=GROUPS,
    cluster_std=STD,
    shuffle=True,
    random_state=9487,
)
"""
print("X")
print(X)
print("y")
print(y)
"""
plt.subplot(231)
# plt.scatter(X[:, 0], X[:, 1], s=50, c=y)  # 無法指定顏色
for i in range(N):
    plt.scatter(X[i, 0], X[i, 1], s=50, c=colors[y[i]])

plt.title("原始資料" + str(N) + "點" + str(GROUPS) + "群")

print("------------------------------")  # 30個

CLUSTERS = 2  # 要分成的群數
print("使用KMeans分成", CLUSTERS, "群")
clf = KMeans(
    n_clusters=CLUSTERS,
    init="k-means++",
    n_init=10,
    max_iter=300,
    tol=1e-04,
    random_state=9487,
)  # K-平均演算法

# 一次做完訓練+預測
y_pred = clf.fit_predict(X)  # 學習訓練 + 預測 .fit_predict

plt.subplot(232)
# plt.scatter(X[:, 0], X[:, 1], s=50, c=y_pred)  # 無法指定顏色
for i in range(N):
    plt.scatter(X[i, 0], X[i, 1], s=50, c=colors[y_pred[i]])

plt.title("原始資料" + str(N) + "點 用 KMeans分成" + str(CLUSTERS) + "群")

# 輪廓係數
cluster_labels = np.unique(y_pred)  # 尋找不同的數值出來

print("y_pred :", y_pred)
print("cluster_labels :", cluster_labels)

n_clusters = cluster_labels.shape[0]
print("n_clusters =", n_clusters)

silhouette_vals = silhouette_samples(X, y_pred, metric="euclidean")
print("每個點的輪廓係數 silhouette_samples :")
print(silhouette_vals)
print("共", len(y_pred), "點")
print("平均輪廓係數 :", silhouette_vals.mean())

plt.subplot(233)
for i, c in enumerate(silhouette_vals):
    plt.scatter(i, silhouette_vals[i], c=colors[y_pred[i]])

# 輪廓係數平均數的水平線(紅線水平線)
silhouette_avg = np.mean(silhouette_vals)
plt.axhline(silhouette_avg, color="red", linestyle="--")
# axvline垂直, axhline水平
plt.ylabel("輪廓係數")
plt.title("每個點的輪廓係數")

print("------------------------------")  # 30個

CLUSTERS = 3  # 要分成的群數
print("使用KMeans分成", CLUSTERS, "群")
clf = KMeans(
    n_clusters=CLUSTERS,
    init="k-means++",
    n_init=10,
    max_iter=300,
    tol=1e-04,
    random_state=9487,
)  # K-平均演算法

# 一次做完訓練+預測
y_pred = clf.fit_predict(X)  # 學習訓練 + 預測 .fit_predict

plt.subplot(234)
# plt.scatter(X[:, 0], X[:, 1], s=50, c=y_pred)  # 無法指定顏色
for i in range(N):
    plt.scatter(X[i, 0], X[i, 1], s=50, c=colors[y_pred[i]])

plt.title("原始資料" + str(N) + "點 用 KMeans分成" + str(CLUSTERS) + "群")

# 輪廓係數
cluster_labels = np.unique(y_pred)  # 尋找不同的數值出來

print("y_pred :", y_pred)
print("cluster_labels :", cluster_labels)

n_clusters = cluster_labels.shape[0]
print("n_clusters =", n_clusters)

silhouette_vals = silhouette_samples(X, y_pred, metric="euclidean")
print("每個點的輪廓係數 silhouette_samples :")
print(silhouette_vals)
print("共", len(y_pred), "點")
print("平均輪廓係數 :", silhouette_vals.mean())

plt.subplot(235)
for i, c in enumerate(silhouette_vals):
    plt.scatter(i, silhouette_vals[i], c=colors[y_pred[i]])

# 輪廓係數平均數的水平線(紅線水平線)
silhouette_avg = np.mean(silhouette_vals)
plt.axhline(silhouette_avg, color="red", linestyle="--")
# axvline垂直, axhline水平
plt.ylabel("輪廓係數")
plt.title("每個點的輪廓係數")

plt.subplot(236)

cc = silhouette_score(X, y)  # 計算輪廓係數
print("分", CLUSTERS, "群, 計算輪廓係數:", cc)

# 依據輪廓係數找最佳集群數量

# 測試 2~10 群的分數
silhouette_score_list = []
print("輪廓係數:")
for k in range(2, 11):
    CLUSTERS = k  # 要分成的群數
    print("使用KMeans分成", CLUSTERS, "群")
    clf = KMeans(
        n_clusters=CLUSTERS,
        init="k-means++",
        n_init=10,
        max_iter=300,
        random_state=9487,
    )  # K-平均演算法
    clf.fit(X)  # 學習訓練.fit
    y_pred = clf.fit_predict(X)  # 學習訓練 + 預測 .fit_predict
    cc = silhouette_score(X, y_pred)  # 計算輪廓係數
    silhouette_score_list.append(cc)
    print(f"{k}:{silhouette_score_list[-1]:.2f}")
    print("分", k, "群, 計算輪廓係數:", cc)

print(f"最大值 {np.argmax(silhouette_score_list)+2}: {np.max(silhouette_score_list):.2f}")

print("分2~10群的 silhouette_score :\n", silhouette_score_list)

plt.plot(
    range(2, 11),
    silhouette_score_list,
    color="r",
    marker="o",
    markersize=8,
    label="silhouette_score",
)
plt.xlabel("集群數量")
plt.ylabel("silhouette_score輪廓係數")
plt.grid()
plt.legend()

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 集群的應用 : 影像壓縮(Image Compression)
# 利用集群將相近的顏色以質心取代，就可以達到減色的效果，
# 減色後可以較少的位元來儲存或傳輸影像，達到影像壓縮的效益。

print("對圖片做 KMeans(), 目前彩色圖片還有問題")

# 重建影像的函數


def reconstruct_image(cluster_centers, y_pred, w, h):
    d = cluster_centers.shape[1]
    image = np.zeros((w, h, d))
    label_index = 0
    for i in range(w):
        for j in range(h):
            # 以質心取代原圖像顏色
            image[i][j] = cluster_centers[y_pred[label_index]]
            label_index += 1
    return image


from sklearn.datasets import load_sample_image

print("使用 sklearn 內建圖片")
image = load_sample_image("china.jpg")
"""
print("使用 本地圖片")
# filename = 'C:/_git/vcs/_1.data/______test_files1/ims01.bmp'
filename = "data/circle.bmp"
import cv2
# 檔案 => cv2影像
image = cv2.imread(filename, 1)
"""
print(type(image))
print(len(image))
print(image.shape)

"""
# 存檔
plt.imsave("tmp_flower.jpg", image)

# 目前還不能使用本地檔案
#filename = 'C:/_git/vcs/_1.data/______test_files1/ims01.bmp'
filename = "tmp_flower.jpg"
import cv2
# 檔案 => cv2影像
image = cv2.imread(filename, 1)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
#plt.imshow(image)
plt.axis("off")

show()
"""
print(image.shape)
w, h, d = image.shape  # 取得圖片寬高及顏色維度
print(w, h, d)

# 正規化、取得圖片寬高及顏色維度、將寬高轉為一維
# 正規化
image = np.array(image, dtype=np.float64) / 255
# 將寬高轉為一維
image_array = np.reshape(image, (w * h, d))

# 模型訓練及預測

# 隨機抽樣1000個像素, 把image_array打亂, 取出前1000個
image_sample = sklearn.utils.shuffle(image_array, random_state=9487)[:1000]

# K-Means模型訓練， 設定64個集群
CLUSTERS = 16  # 要分成的群數
print("使用KMeans分成", CLUSTERS, "群")
clf = KMeans(n_clusters=CLUSTERS)  # K-平均演算法

clf.fit(image_sample)  # 學習訓練.fit

# 對所有像素進行集群
y_pred = clf.predict(image_array)  # 預測.predict

image2 = reconstruct_image(clf.cluster_centers_, y_pred, w, h)

plt.figure(num="比較原圖與減色後的圖片", figsize=(10, 12))

plt.subplot(211)
plt.imshow(image)
plt.axis("off")
plt.title("原圖")

plt.subplot(212)
plt.imshow(image2)
plt.axis("off")
plt.title("重建的影像")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.utils import shuffle
from skimage import io

filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"

original = plt.imread(filename)
width, height, depth = original.shape
temp = original.reshape(width * height, depth)
temp = np.array(temp, dtype=np.float64) / 255

original_sample = shuffle(temp, random_state=0)[:1000]  # 随机取1000个RGB值作为训练集


def cluster(k):
    estimator = KMeans(n_clusters=k, random_state=9487)  # K-平均演算法, 分成k群
    kmeans = estimator.fit(original_sample)  # 聚类  # 學習訓練.fit
    return kmeans


def recreate_image(codebook, labels, w, h):
    d = codebook.shape[1]
    image = np.zeros((w, h, d))
    label_idx = 0
    for i in range(w):
        for j in range(h):
            image[i][j] = codebook[labels[label_idx]]
            label_idx += 1
    return image


kmeans = cluster(32)
labels = kmeans.predict(temp)  # 預測.predict
kmeans_32 = recreate_image(kmeans.cluster_centers_, labels, width, height)

kmeans = cluster(64)
labels = kmeans.predict(temp)  # 預測.predict
kmeans_64 = recreate_image(kmeans.cluster_centers_, labels, width, height)

kmeans = cluster(128)
labels = kmeans.predict(temp)  # 預測.predict
kmeans_128 = recreate_image(kmeans.cluster_centers_, labels, width, height)

plt.figure(figsize=(15, 10))

plt.subplot(221)
plt.imshow(original.reshape(width, height, depth))
plt.title("原始图像")
plt.axis("off")

plt.subplot(222)
plt.imshow(kmeans_128)
# NG io.imsave('kmeans_128.png',kmeans_128)
plt.title("量化的图像(128颜色, K-Means)")
plt.axis("off")

plt.subplot(223)
plt.imshow(kmeans_64)
# NG io.imsave('kmeans_64.png',kmeans_64)
plt.title("量化的图像(64颜色, K-Means)")
plt.axis("off")

plt.subplot(224)
plt.imshow(kmeans_32)
# NG io.imsave('kmeans_32.png',kmeans_32)
plt.title("量化的图像(32颜色, K-Means)")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# GMM測試

from scipy.spatial.distance import cdist


# 繪製集群範圍
def plot_kmeans(clf, X, n_clusters=4, rseed=0, ax=None):
    labels = clf.fit_predict(X)

    # 繪製樣本點
    ax = ax or plt.gca()
    ax.axis("equal")
    # ax.scatter(X[:, 0], X[:, 1], c=labels, s=40, cmap="viridis", zorder=2)  # 無法指定顏色
    for i in range(N):
        ax.scatter(X[i, 0], X[i, 1], s=50, c=colors[labels[i]])

    # 以最大半徑繪製集群範圍
    centers = clf.cluster_centers_
    radii = [cdist(X[labels == i], [center]).max() for i, center in enumerate(centers)]
    print("取得半徑 :", radii)
    for c, r in zip(centers, radii):
        print("畫圓 :", c, r)
        ax.add_patch(
            plt.Circle(c, r, fc="#CCCCCC", lw=3, color="k", alpha=0.5, zorder=1)
        )


# 建立資料, 使用 make_blobs
N = 400  # n_samples, 樣本數
M = 2  # n_features, 特徵數(資料的維度)
GROUPS = 4  # centers, 分群數
STD = 0.60  # cluster_std, 資料標準差
print("make_blobs,", N, "個樣本, ", M, "個特徵, 分成", GROUPS, "群")
X, y_true = make_blobs(n_samples=N, centers=GROUPS, cluster_std=STD, random_state=9487)

X = X[:, ::-1]  # 特徵互調順序，繪圖效果較佳 ???
print(X[:10])

# 進行 K-Means 集群，並繪圖

CLUSTERS = 4  # 要分成的群數
print("使用KMeans分成", CLUSTERS, "群")
clf = KMeans(CLUSTERS, init="k-means++", n_init=10)  # K-平均演算法

clf.fit(X)  # 學習訓練.fit

labels = clf.predict(X)

plt.subplot(121)
# plt.scatter(X[:, 0], X[:, 1], c=labels, s=50, cmap="viridis")  # 無法指定顏色
for i in range(N):
    plt.scatter(X[i, 0], X[i, 1], s=50, c=colors[labels[i]])

plt.axis([-10, 10, -10, 10])
plt.title("原始資料" + str(N) + "點" + str(GROUPS) + "群, 標準化")

plt.subplot(122)
CLUSTERS = 4  # 要分成的群數
print("使用KMeans分成", CLUSTERS, "群")
clf = KMeans(n_clusters=CLUSTERS, init="k-means++", n_init=10)  # K-平均演算法
plot_kmeans(clf, X)
plt.axis([-10, 10, -10, 10])

show()  #  2

print("------------------------------")  # 30個

rng = np.random.RandomState(13)
X_stretched = np.dot(X, rng.randn(2, 2))

CLUSTERS = 4  # 要分成的群數
print("使用KMeans分成", CLUSTERS, "群")
clf = KMeans(n_clusters=CLUSTERS, init="k-means++", n_init=10)  # K-平均演算法
plot_kmeans(clf, X_stretched)
show()  # 3

# 改用GMM

from sklearn.mixture import GaussianMixture


print("設定要分的群數")
n_components = 4

clf = GaussianMixture(n_components=n_components)

clf.fit(X)  # 學習訓練.fit

labels = clf.predict(X)  # 預測.predict

plt.scatter(X[:, 0], X[:, 1], c=labels, s=40, cmap="viridis")
show()  # 4

# 屬於各集群的機率

probs = clf.predict_proba(X)
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
def plot_gmm(clf, X, label=True, ax=None):
    ax = ax or plt.gca()
    clf.fit(X)  # 學習訓練.fit
    labels = clf.predict(X)
    if label:
        ax.scatter(X[:, 0], X[:, 1], c=labels, s=40, cmap="viridis", zorder=2)
    else:
        ax.scatter(X[:, 0], X[:, 1], s=40, zorder=2)
    ax.axis("equal")

    # soft-edged sphere
    w_factor = 0.2 / clf.weights_.max()
    for pos, covar, w in zip(clf.means_, clf.covariances_, clf.weights_):
        draw_ellipse(pos, covar, alpha=w * w_factor)


clf = GaussianMixture(n_components=4, random_state=9487)
plot_gmm(clf, X)
show()  # 5

# 使用 GMM對長條型資料進行集群

clf = GaussianMixture(n_components=4, covariance_type="full", random_state=9487)
plot_gmm(clf, X_stretched)
show()  # 6

Xmoon, ymoon = make_moons(200, noise=0.05, random_state=9487)
plt.scatter(Xmoon[:, 0], Xmoon[:, 1])
show()  # 7

# GMM 集群：設定2個集群

gmm2 = GaussianMixture(n_components=2, covariance_type="full", random_state=9487)
plot_gmm(gmm2, Xmoon)
show()  # 8

# GMM 集群：設定16個集群

gmm16 = GaussianMixture(n_components=16, covariance_type="full", random_state=9487)
plot_gmm(gmm16, Xmoon, label=False)
show()  # 9

# 以模型生成資料

Xnew, _ = gmm16.sample(400)
plt.scatter(Xnew[:, 0], Xnew[:, 1])
show()  # 10

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
show()  # 11

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 客戶區隔(Customer segmentation)

df = pd.read_csv(
    "D:/_git/vcs/_big_files/Scikit-learn_data/invoice.csv", encoding="ISO-8859-1"
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

# 複製資料
rfm_segmentation = rfm.copy()

print("轉折判斷法(Elbow)")

Nc = range(1, 20)
clf = [KMeans(n_clusters=i, init="k-means++", n_init="auto") for i in Nc]  # K-平均演算法
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

CLUSTERS = 3  # 要分成的群數
print("使用KMeans分成", CLUSTERS, "群")
clf = KMeans(n_clusters=CLUSTERS, init="k-means++", n_init=10, max_iter=300)  # K-平均演算法

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
y_km = rfm_segmentation["cluster"]
cluster_labels = np.unique(y_km)
n_clusters = cluster_labels.shape[0]

silhouette_vals = silhouette_samples(X, y_km, metric="euclidean")
print("每個點的輪廓係數 silhouette_samples :")
# many print(silhouette_vals)

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
plt.ylabel("集群")
plt.xlabel("輪廓係數")
plt.tight_layout()
show()

# 依據輪廓分數找最佳集群數量

# 測試 2~20 群的分數

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
    print("使用KMeans分成", CLUSTERS, "群")
    clf = KMeans(
        n_clusters=CLUSTERS, init="k-means++", n_init=10, max_iter=300
    )  # K-平均演算法
    clf.fit(X)  # 學習訓練.fit

    # 新增欄位，加入集群代碼
    y_pred = clf.labels_
    cluster_labels = np.unique(y_pred)
    n_clusters = cluster_labels.shape[0]
    silhouette_vals = silhouette_samples(X, y_pred, metric="euclidean")
    # print('每個點的輪廓係數 silhouette_samples :')
    # many print(silhouette_vals)

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
    plt.ylabel("集群")
    plt.xlabel("輪廓係數")
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

X = rfm_segmentation[["R_Quartile", "F_Quartile", "M_Quartile"]]
silhouette_score_list = []
print("2輪廓分數:")
for i in range(2, 21):
    print(i)
    CLUSTERS = i  # 要分成的群數
    print("使用KMeans分成", CLUSTERS, "群")
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
    print("使用KMeans分成", CLUSTERS, "群")
    clf = KMeans(
        n_clusters=CLUSTERS, init="k-means++", n_init=10, max_iter=300
    )  # K-平均演算法
    clf.fit(X)  # 學習訓練.fit

    # 新增欄位，加入集群代碼
    y_pred = clf.labels_
    cluster_labels = np.unique(y_pred)
    n_clusters = cluster_labels.shape[0]
    silhouette_vals = silhouette_samples(X, y_pred, metric="euclidean")
    # print('每個點的輪廓係數 silhouette_samples :')
    # many print(silhouette_vals)

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
    plt.ylabel("集群")
    plt.xlabel("輪廓係數")
    plt.tight_layout()
    show()

# 分成4個集群

CLUSTERS = 4  # 要分成的群數
print("使用KMeans分成", CLUSTERS, "群")
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

dx.set_xlabel("Recency")
dx.set_ylabel("Frequency")
dx.set_zlabel("Monetary")
dx.legend()
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

# 建立資料, 使用 make_blobs
N = 200  # n_samples, 樣本數
M = 2  # n_features, 特徵數(資料的維度)
GROUPS = 4  # centers, 分群數
STD = 1  # cluster_std, 資料標準差
print("make_blobs,", N, "個樣本, ", M, "個特徵, 分成", GROUPS, "群")
X, y = make_blobs(
    n_samples=N,
    n_features=M,
    centers=GROUPS,
    cluster_std=STD,
    center_box=(-10.0, 10.0),
    shuffle=True,
    random_state=9487,
)

plt.figure(figsize=(6, 4))
plt.xticks(())
plt.yticks(())
plt.scatter(X[:, 0], X[:, 1], s=20, marker="o")

show()

print("------------------------------")  # 30個

CLUSTERS = 3  # 要分成的群數
print("使用KMeans分成", CLUSTERS, "群")
clf = KMeans(n_clusters=CLUSTERS)  # K-平均演算法

clf.fit(X)  # 學習訓練.fit

print("kmean: k={}, cost={}".format(n_clusters, int(clf.score(X))))

labels = clf.labels_
centers = clf.cluster_centers_  # 群集中心
markers = ["o", "^", "*"]
colors = ["r", "b", "y"]

plt.figure(figsize=(6, 4))
plt.xticks(())
plt.yticks(())

# 畫樣本
for c in range(n_clusters):
    cluster = X[labels == c]
    plt.scatter(cluster[:, 0], cluster[:, 1], marker=markers[c], s=20, c=colors[c])
# 畫出中心點
plt.scatter(centers[:, 0], centers[:, 1], marker="o", c="white", alpha=0.9, s=300)
for i, c in enumerate(centers):
    plt.scatter(c[0], c[1], marker="$%d$" % i, s=50, c=colors[i])

show()

print("------------------------------")  # 30個


def fit_plot_kmean_model(n_clusters, X):
    plt.xticks(())
    plt.yticks(())

    # 使用 k-均值算法進行擬合
    clf = KMeans(n_clusters=n_clusters)  # K-平均演算法
    clf.fit_predict(X)

    labels = clf.labels_
    centers = clf.cluster_centers_  # 群集中心
    markers = ["o", "^", "*", "s"]
    colors = ["r", "b", "y", "k"]

    # 計算成本
    score = clf.score(X)
    plt.title("k={}, score={}".format(n_clusters, (int)(score)))

    # 畫樣本
    for c in range(n_clusters):
        cluster = X[labels == c]
        plt.scatter(cluster[:, 0], cluster[:, 1], marker=markers[c], s=20, c=colors[c])
    # 畫出中心點
    plt.scatter(centers[:, 0], centers[:, 1], marker="o", c="white", alpha=0.9, s=300)
    for i, c in enumerate(centers):
        plt.scatter(c[0], c[1], marker="$%d$" % i, s=50, c=colors[i])


n_clusters = [2, 3, 4]

plt.figure(figsize=(10, 3))
for i, c in enumerate(n_clusters):
    plt.subplot(1, 3, i + 1)
    fit_plot_kmean_model(c, X)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/College_Data", index_col=0)

# Check the head of the data

cc = df.head()
print(cc)

cc = df.info()
print(cc)

cc = df.describe()
print(cc)

# Exploratory Analysis

sns.set_style("whitegrid")
sns.lmplot(
    x="Room.Board",
    y="Grad.Rate",
    data=df,
    hue="Private",
    palette="coolwarm",
    aspect=1,
    fit_reg=True,
)
show()

sns.set_style("whitegrid")
sns.lmplot(
    x="Outstate",
    y="F.Undergrad",
    data=df,
    hue="Private",
    palette="coolwarm",
    aspect=1,
    fit_reg=False,
)
show()

sns.boxplot(x="Private", y="S.F.Ratio", data=df)
show()

sns.boxplot(x="Private", y="perc.alumni", data=df)
show()

sns.set_style("darkgrid")
g = sns.FacetGrid(df, hue="Private", palette="coolwarm", aspect=2)
g = g.map(plt.hist, "Outstate", bins=20, alpha=0.7)
show()

# Create a similar histogram for the Grad.Rate column.

sns.set_style("darkgrid")
g = sns.FacetGrid(df, hue="Private", palette="coolwarm", aspect=2)
g = g.map(plt.hist, "Grad.Rate", bins=20, alpha=0.7)
show()

# There seems to be a private school with a graduation rate of higher than 100%

cc = df[df["Grad.Rate"] > 100]
print(cc)


cc = df["Grad.Rate"]["Cazenovia College"] = 100
print(cc)

cc = df[df["Grad.Rate"] > 100]
print(cc)

sns.set_style("darkgrid")
g = sns.FacetGrid(df, hue="Private", palette="coolwarm", aspect=2)
g = g.map(plt.hist, "Grad.Rate", bins=20, alpha=0.7)
show()

# K Means Cluster Creation

from sklearn.cluster import KMeans

clf = KMeans(n_clusters=2, verbose=0, tol=1e-3, max_iter=300, n_init=20)  # K-平均演算法

clf.fit(df.drop("Private", axis=1))  # 學習訓練.fit

clus_cent = clf.cluster_centers_  # 群集中心
print(clus_cent)

cc = df[df["Private"] == "Yes"].describe()  # Statistics for private colleges only
print(cc)

cc = df[df["Private"] == "No"].describe()  # Statistics for public colleges only
print(cc)

df_desc = pd.DataFrame(df.describe())
feat = list(df_desc.columns)
kmclus = pd.DataFrame(clus_cent, columns=feat)
print(kmclus)

# What are the cluster labels?

print(clf.labels_)

# Evaluation


def converter(cluster):
    if cluster == "Yes":
        return 1
    else:
        return 0


df1 = df  # Create a copy of data frame so that original data frame does not get 'corrupted' with the cluster index
df1["Cluster"] = df["Private"].apply(converter)

cc = df1.head()
print(cc)

from sklearn.metrics import confusion_matrix, classification_report

print(confusion_matrix(df1["Cluster"], clf.labels_))
print(classification_report(df1["Cluster"], clf.labels_))

# Clustering performance (e.g. distance between centroids)

df_pvt = df[df["Private"] == "Yes"]
df_pub = df[df["Private"] == "No"]

clf = KMeans(n_clusters=2, verbose=0, tol=1e-3, max_iter=50, n_init=10)  # K-平均演算法

clf.fit(df.drop("Private", axis=1))  # 學習訓練.fit

clus_cent = clf.cluster_centers_  # 群集中心
df_desc = pd.DataFrame(df.describe())
feat = list(df_desc.columns)
kmclus = pd.DataFrame(clus_cent, columns=feat)
a = np.array(kmclus.diff().iloc[1])

centroid_diff = pd.DataFrame(
    a, columns=["K-means cluster centroid-distance"], index=df_desc.columns
)

""" NG
centroid_diff['Mean of corresponding entity (private)']=np.array(df_pvt.mean())
centroid_diff['Mean of corresponding entity (public)']=np.array(df_pub.mean())
print(centroid_diff)
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


"""
#plt.autoscale()

plt.subplots_adjust(hspace=0.5)

"""

# 共同抽出
# 在 clf.fit(X)  # 學習訓練.fit 之後
print("群集類別標籤(訓練好的結果) :\n", clf.labels_)
print("集群中心的坐標 :", clf.cluster_centers_)
print("分群準確性 :", clf.inertia_)
print("Distortion : %.2f" % clf.inertia_)

# KMeans其他參數:

class_centers, classification = clf.evaluate(X_train)
_, y_pred = clf.evaluate(X_train)

plt.plot(
    [x for x, _ in clf.centroids],
    [y for _, y in clf.centroids],
    "*",
    markersize=20,
    color="r",
)

w_factor = 0.2 / clf.weights_.max()
for pos, covar, w in zip(clf.means_, clf.covariances_, clf.weights_):
    draw_ellipse(pos, covar, alpha=w * w_factor)

print("kmean: k={}, cost={}".format(n_clusters, int(clf.score(X))))

score = clf.score(X)
plt.title("k={}, score={}".format(n_clusters, (int)(score)))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("演算法 計算分群準確性 :", clf.inertia_)
print("自己   計算分群準確性")  # 資料點與所屬質心距離的平方和

C = clf.cluster_centers_  # 集群中心的座標, CLUSTERS個座標
y = clf.labels_  # 群集類別標籤
ss = 0
for i in range(len(X)):
    d = (X[i, 0] - C[y[i], 0]) ** 2 + (X[i, 1] - C[y[i], 1]) ** 2
    ss += d
print("自己   計算分群準確性 :", ss)

print("------------------------------------------------------------")  # 60個
print("------------------------------")  # 30個


CLUSTERS = 3  # 要分成的群數
print("使用KMeans分成", CLUSTERS, "群")
clf = KMeans(
    n_clusters=CLUSTERS,
    init="random",
    n_init=10,
    max_iter=300,
    tol=1e-04,
    random_state=9487,
)  # K-平均演算法


"""
    clf = KMeans(
        n_clusters=CLUSTERS,
        init="k-means++",
        n_init=10,
        max_iter=300,
        random_state=9487,
    )  # K-平均演算法


make_blobs 多了 shuffle 參數
            X, y = make_blobs(
                n_samples=N,
                n_features=M,
                centers=GROUPS,
                cluster_std=STD,
                shuffle=True,
                random_state=9487,
            )

"""


X, y = datasets.load_iris(return_X_y=True)

iris = datasets.load_iris()

X = iris.data
y = iris.target
