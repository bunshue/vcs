import time
import keras

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print('------------------------------------------------------------')	#60個

#迭代次數
ITERATIONS = 50

print('------------------------------------------------------------')	#60個

model = keras.Sequential([keras.layers.Dense(units = 1, input_shape = [1])])
model.compile(optimizer = 'sgd', loss = 'mean_squared_error')

# y = x
xs = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0], dtype = float)
ys = np.array([0.0, 1.0, 2.0, 5.0, 4.0, 5.0], dtype = float)
print(type(xs))
print(xs)
print(type(ys))
print(ys)

model.fit(xs, ys, epochs = ITERATIONS)

print('keras 預測')
xx = np.linspace(0.0, 10.0, 21)
yy = model.predict(xx)

"""
print(model.predict([2.5]))
print(model.predict([4.5]))
print(model.predict([6.0]))
print(model.predict([10.0]))
print(xx)
print(yy)
"""

x = np.linspace(0, 10, 100)
plt.plot(x, x, 'b', lw = 2, label = 'y = x')
plt.plot(xs, ys, 'g-o', lw = 1, ms = 10, label = '實驗點')
plt.scatter(xx, yy, c = 'red', marker = 'o', lw = 4, label = '預測點')

xmin, xmax, ymin, ymax = -1, 11, -1, 11
plt.axis([xmin, xmax, ymin, ymax])  #設定各軸顯示範圍
plt.legend()

plt.show()

print('------------------------------------------------------------')	#60個

from sklearn.datasets import make_blobs

data, label = make_blobs(n_samples = 5,
                         n_features = 2,
                         centers = 2,
                         random_state = 0)
print(data)
print(f"分類 : {label}")

print('------------------------------------------------------------')	#60個

from sklearn.datasets import make_blobs

data, label = make_blobs(n_samples = 200,
                         n_features = 2,
                         centers = 2,
                         random_state = 0)
plt.scatter(data[:, 0], data[:, 1], c = label, cmap = 'bwr')
plt.grid(True)

plt.show()

print('------------------------------------------------------------')	#60個

from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler

data, label = make_blobs(n_samples = 200,
                         n_features = 2,
                         centers = 2,
                         random_state = 0)
d_sta = StandardScaler().fit_transform(data)    # 標準化
plt.scatter(d_sta[:, 0], d_sta[:, 1], c = label, cmap = 'bwr')
plt.grid(True)

plt.show()

print('------------------------------------------------------------')	#60個

from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

data, label = make_blobs(n_samples = 200,
                         n_features = 2,
                         centers = 2,
                         random_state = 0)
d_sta = StandardScaler().fit_transform(data)    # 標準化
# 分割數據為訓練數據和測試數據
dx_train, dx_test, label_train, label_test = train_test_split(d_sta,
                                                              label,
                                                              test_size = 0.2,
                                                              random_state = 0)
                                             
print(f"特徵數據外形 : {d_sta.shape}")
print(f"訓練數據外形 : {dx_train.shape}")
print(f"測試數據外形 : {dx_test.shape}")
print(f"標籤數據外形 : {label.shape}")
print(f"訓練數據外形 : {label_train.shape}")
print(f"測試數據外形 : {label_test.shape}")

print('------------------------------------------------------------')	#60個

from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

data, label = make_blobs(n_samples = 200,
                         n_features = 2,
                         centers = 2,
                         random_state = 0)
d_sta = StandardScaler().fit_transform(data)    # 標準化
# 分割數據為訓練數據和測試數據
dx_train, dx_test, label_train, label_test = train_test_split(d_sta,
                                                              label,
                                                              test_size = 0.2,
                                                              random_state = 0)
# 建立分類模型                                             
k_model = KNeighborsClassifier(n_neighbors = 5)       # k = 5
# 建立訓練數據模型
k_model.fit(dx_train, label_train)
# 對測試數據做預測
pred = k_model.predict(dx_test)
# 輸出測試數據的 label
print(label_test)
# 輸出預測數據的 label
print(pred)
# 輸出準確性
print(f"訓練資料的準確性 = {k_model.score(dx_train, label_train)}")
print(f"測試資料的準確性 = {k_model.score(dx_test, label_test)}")

print('------------------------------------------------------------')	#60個

from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

data, label = make_blobs(n_samples = 200,
                         n_features = 2,
                         centers = 2,
                         random_state = 0)
d_sta = StandardScaler().fit_transform(data)    # 標準化
# 分割數據為訓練數據和測試數據
dx_train, dx_test, label_train, label_test = train_test_split(d_sta,
                                                              label,
                                                              test_size = 0.2,
                                                              random_state = 0)
# 建立分類模型                                             
lo_model = LogisticRegression()
# 建立訓練數據模型
lo_model.fit(dx_train, label_train)
# 對測試數據做預測
pred = lo_model.predict(dx_test)
# 輸出測試數據的 label
print(label_test)
# 輸出預測數據的 label
print(pred)
# 輸出準確性
print(f"訓練資料的準確性 = {lo_model.score(dx_train, label_train)}")
print(f"測試資料的準確性 = {lo_model.score(dx_test, label_test)}")

print('------------------------------------------------------------')	#60個

from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC

data, label = make_blobs(n_samples = 200,
                         n_features = 2,
                         centers = 2,
                         random_state = 0)
d_sta = StandardScaler().fit_transform(data)    # 標準化
# 分割數據為訓練數據和測試數據
dx_train, dx_test, label_train, label_test = train_test_split(d_sta,
                                                              label,
                                                              test_size = 0.2,
                                                              random_state = 0)
# 建立分類模型                                             
svm_model = LinearSVC()
# 建立訓練數據模型
svm_model.fit(dx_train, label_train)
# 對測試數據做預測
pred = svm_model.predict(dx_test)
# 輸出測試數據的 label
print(label_test)
# 輸出預測數據的 label
print(pred)
# 輸出準確性
print(f"訓練資料的準確性 = {svm_model.score(dx_train, label_train)}")
print(f"測試資料的準確性 = {svm_model.score(dx_test, label_test)}")

print('------------------------------------------------------------')	#60個

from sklearn.datasets import make_moons
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC, SVC

data, label = make_moons(n_samples = 200, noise = 0.2, random_state = 0)

d_sta = StandardScaler().fit_transform(data)    # 標準化
# 分割數據為訓練數據和測試數據
dx_train, dx_test, label_train, label_test = train_test_split(d_sta,
                                                              label,
                                                              test_size = 0.2,
                                                              random_state = 0)
# 線性SVM 建立分類模型, 建立訓練數據模型, 對測試數據做預測                                             
svm_model = LinearSVC()
svm_model.fit(dx_train, label_train)
pred = svm_model.predict(dx_test)
# 輸出線性SVM準確性
print(f"線性訓練資料的準確性 = {svm_model.score(dx_train, label_train)}")
print(f"線性測試資料的準確性 = {svm_model.score(dx_test, label_test)}")
print('=' * 50)
# 非線性SVM 建立分類模型, 建立訓練數據模型, 對測試數據做預測                                             
svm = SVC()
svm.fit(dx_train, label_train)
pred = svm.predict(dx_test)
# 輸出非線性SVM準確性
print(f"非線性訓練資料的準確性 = {svm.score(dx_train, label_train)}")
print(f"非線性測試資料的準確性 = {svm.score(dx_test, label_test)}")

print('------------------------------------------------------------')	#60個

from sklearn import datasets

data, label = datasets.load_iris(return_X_y = True)
print("鳶尾花花萼和花瓣數據")
print(data[0 : 5])
print(f"分類 : {label[0:5]}")

print('------------------------------------------------------------')	#60個

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

data, label = datasets.load_iris(return_X_y = True)
# 分割數據為訓練數據和測試數據
dx_train, dx_test, label_train, label_test = train_test_split(data,
                                                              label,
                                                              test_size = 0.2,
                                                              random_state = 0)
# 建立分類模型                                             
tree_model = DecisionTreeClassifier()
# 建立訓練數據模型
tree_model.fit(dx_train, label_train)
# 對測試數據做預測
pred = tree_model.predict(dx_test)
# 輸出準確性
print(f"訓練資料的準確性 = {tree_model.score(dx_train, label_train)}")
print(f"測試資料的準確性 = {tree_model.score(dx_test, label_test)}")

print('------------------------------------------------------------')	#60個

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

data, label = datasets.load_iris(return_X_y = True)
# 分割數據為訓練數據和測試數據
dx_train, dx_test, label_train, label_test = train_test_split(data, label, test_size = 0.2, random_state = 0)
# 建立分類模型                                             
forest_model = RandomForestClassifier()
# 建立訓練數據模型
forest_model.fit(dx_train, label_train)
# 對測試數據做預測
pred = forest_model.predict(dx_test)
# 輸出準確性
print(f"訓練資料的準確性 = {forest_model.score(dx_train, label_train)}")
print(f"測試資料的準確性 = {forest_model.score(dx_test, label_test)}")

print('------------------------------------------------------------')	#60個

from sklearn import datasets

# 建立 300 個點, n_features = 2, centers = 3
data, label = datasets.make_blobs(n_samples = 300, n_features = 2,
                                  centers = 3, random_state = 10)                                

# 繪圓點, 圓點用黑色外框 
plt.scatter(data[:,0], data[:,1], marker = "o", edgecolor = "black")

plt.title("無監督學習",fontsize = 16)

plt.show()

print('------------------------------------------------------------')	#60個

from sklearn import datasets
from sklearn import cluster

# 建立 300 個點, n_features = 2, centers = 3
data, label = datasets.make_blobs(n_samples = 300, n_features = 2,
                                  centers = 3, random_state = 10)
                                  
e = cluster.KMeans(n_clusters = 3)    # k-mean方法建立 3 個群集中心物件
e.fit(data)                         # 將數據帶入物件, 做群集分析
print(e.labels_)                    # 列印群集類別標籤
print(e.cluster_centers_)           # 列印群集中心

print('------------------------------------------------------------')	#60個

from sklearn import datasets
from sklearn import cluster

# 建立 300 個點, n_features = 2, centers = 3
data, label = datasets.make_blobs(n_samples = 300, n_features = 2,
                                  centers = 3, random_state = 10)
                                  
e = cluster.KMeans(n_clusters = 3)      # k-mean方法建立 3 個群集中心物件
e.fit(data)                             # 將數據帶入物件, 做群集分析
print(e.labels_)                        # 列印群集類別標籤
print(e.cluster_centers_)               # 列印群集中心

# 繪圓點, 圓點用黑色外框, 使用標籤 labels_ 區別顏色, 
plt.scatter(data[:, 0], data[:, 1], marker = "o", c = e.labels_)
# 用紅色標記群集中心
plt.scatter(e.cluster_centers_[:, 0], e.cluster_centers_[:, 1],marker = "*", color = "red")
plt.title("無監督學習",fontsize = 16)

plt.show()

print('------------------------------------------------------------')	#60個

#統率, 武力, 智力, 政治, 魅力
main_features = [87, 86, 82, 78, 100]             # 劉備 特徵值
people_names = [                     # 比較人物人名
    '諸葛亮',
    '關羽',
    '張飛',
    '趙雲',
    '曹操',
    '司馬懿',
    '孫權',
    '周瑜',
    '呂布',
]

people_features = [                   # 比較人物特徵值
    [99, 42, 100, 100, 92],
    [92, 100, 74, 51, 83],
    [86, 99, 78, 36, 57],
    [79, 94, 77, 82, 91],
    [100, 85, 93, 96, 95],
    [95, 62, 98, 95, 84],
    [72, 84, 76, 85, 93],
    [93, 71, 94, 81, 92],
    [84, 98, 61, 12, 55],
]

dist = []                           # 儲存人物相似度值
for feature in people_features:
    distances = 0
    for i in range(len(feature)):
        distances += (main_features[i] - feature[i]) ** 2
    dist.append(math.sqrt(distances))
    
min_ = min(dist)                    # 求最小值
min_index = dist.index(min_)        # 最小值的索引

print(f"與 劉備 最相似的人物 : {people_names[min_index]}")
print(f"相似度值 : {dist[min_index]}")
for i in range(len(dist)):
    print(f"人物 : {people_names[i]}, 相似度 : {dist[i]:6.2f}")

print('------------------------------------------------------------')	#60個

df = pd.read_csv('iris.csv')

print(df.shape)

print(df.head(5))

print(df.describe())

target_mapping = {"setosa": 0,
          "versicolor": 1,
          "virginica": 2}
Y = df["target"].map(target_mapping)
colmap = np.array(["r", "g", "y"])
plt.figure(figsize=(10,5))

plt.subplot(1, 2, 1)
plt.subplots_adjust(hspace = .5)
plt.scatter(df["sepal_length"], df["sepal_width"], color=colmap[Y])
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")

plt.subplot(1, 2, 2)
plt.scatter(df["petal_length"], df["petal_width"], color=colmap[Y])
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")

plt.show()

print('------------------------------------------------------------')	#60個

from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical
from sklearn import preprocessing

np.random.seed(7)   #固定亂數種子

df = pd.read_csv('iris.csv')

label_encoder = preprocessing.LabelEncoder()
df["target"] = label_encoder.fit_transform(df["target"])


dataset = df.values
np.random.shuffle(dataset)
X = dataset[:,0:4].astype(float)
Y = to_categorical(dataset[:,4])

scaler = preprocessing.StandardScaler()
X = scaler.fit_transform(X)

X_train, Y_train = X[:120], Y[:120]
X_test, Y_test = X[120:], Y[120:]

model = Sequential()
model.add(Dense(6, input_shape=(4,), activation="relu"))
model.add(Dense(6, activation="relu"))
model.add(Dense(3, activation="softmax"))

print(model.summary())


model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])


model.fit(X_train, Y_train, epochs = 100, batch_size = 5)


loss, accuracy = model.evaluate(X_test, Y_test)
print("Accuracy = {:.2f}".format(accuracy))

#Y_pred = model.predict_classes(X_test)
Y_pred = model.predict_step(X_test)
print(Y_pred)
Y_target = dataset[:,4][120:].astype(int)
print(Y_target)


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個



