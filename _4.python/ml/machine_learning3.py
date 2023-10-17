import os
import sys
import time
import random

import matplotlib.pyplot as plt
import numpy as np

print('------------------------------------------------------------')	#60個
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

from sklearn.datasets import make_blobs

data, label = make_blobs(n_samples=5,n_features=2,
                         centers=2,random_state=0)
print(data)
print(f"分類 : {label}")

print('------------------------------------------------------------')	#60個

from sklearn.datasets import make_blobs

data, label = make_blobs(n_samples=200,n_features=2,
                         centers=2,random_state=0)
plt.scatter(data[:,0], data[:,1], c=label, cmap='bwr')
plt.grid(True)

plt.show()

print('------------------------------------------------------------')	#60個

from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler

data, label = make_blobs(n_samples=200,n_features=2,
                         centers=2,random_state=0)
d_sta = StandardScaler().fit_transform(data)    # 標準化
plt.scatter(d_sta[:,0], d_sta[:,1], c=label, cmap='bwr')
plt.grid(True)

plt.show()

print('------------------------------------------------------------')	#60個

from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

data, label = make_blobs(n_samples=200,n_features=2,
                         centers=2,random_state=0)
d_sta = StandardScaler().fit_transform(data)    # 標準化
# 分割數據為訓練數據和測試數據
dx_train, dx_test, label_train, label_test = train_test_split(d_sta,
                   label,test_size=0.2,random_state=0)
                                             
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

data, label = make_blobs(n_samples=200,n_features=2,
                         centers=2,random_state=0)
d_sta = StandardScaler().fit_transform(data)    # 標準化
# 分割數據為訓練數據和測試數據
dx_train, dx_test, label_train, label_test = train_test_split(d_sta,
                   label,test_size=0.2,random_state=0)
# 建立分類模型                                             
k_model = KNeighborsClassifier(n_neighbors=5)       # k = 5
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

data, label = make_blobs(n_samples=200,n_features=2,
                         centers=2,random_state=0)
d_sta = StandardScaler().fit_transform(data)    # 標準化
# 分割數據為訓練數據和測試數據
dx_train, dx_test, label_train, label_test = train_test_split(d_sta,
                   label,test_size=0.2,random_state=0)
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

data, label = make_blobs(n_samples=200,n_features=2,
                         centers=2,random_state=0)
d_sta = StandardScaler().fit_transform(data)    # 標準化
# 分割數據為訓練數據和測試數據
dx_train, dx_test, label_train, label_test = train_test_split(d_sta,
                   label,test_size=0.2,random_state=0)
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

data, label = make_moons(n_samples=200,noise=0.2,random_state=0)

d_sta = StandardScaler().fit_transform(data)    # 標準化
# 分割數據為訓練數據和測試數據
dx_train, dx_test, label_train, label_test = train_test_split(d_sta,
                   label,test_size=0.2,random_state=0)
# 線性SVM 建立分類模型, 建立訓練數據模型, 對測試數據做預測                                             
svm_model = LinearSVC()
svm_model.fit(dx_train, label_train)
pred = svm_model.predict(dx_test)
# 輸出線性SVM準確性
print(f"線性訓練資料的準確性 = {svm_model.score(dx_train, label_train)}")
print(f"線性測試資料的準確性 = {svm_model.score(dx_test, label_test)}")
print("="*50)
# 非線性SVM 建立分類模型, 建立訓練數據模型, 對測試數據做預測                                             
svm = SVC()
svm.fit(dx_train, label_train)
pred = svm.predict(dx_test)
# 輸出非線性SVM準確性
print(f"非線性訓練資料的準確性 = {svm.score(dx_train, label_train)}")
print(f"非線性測試資料的準確性 = {svm.score(dx_test, label_test)}")

print('------------------------------------------------------------')	#60個

from sklearn import datasets

data, label = datasets.load_iris(return_X_y=True)
print("鳶尾花花萼和花瓣數據")
print(data[0:5])
print(f"分類 : {label[0:5]}")

print('------------------------------------------------------------')	#60個

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

data, label = datasets.load_iris(return_X_y=True)
# 分割數據為訓練數據和測試數據
dx_train, dx_test, label_train, label_test = train_test_split(data,
                   label,test_size=0.2,random_state=0)
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

data, label = datasets.load_iris(return_X_y=True)
# 分割數據為訓練數據和測試數據
dx_train, dx_test, label_train, label_test = train_test_split(data,
                   label,test_size=0.2,random_state=0)
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

# 建立 300 個點, n_features=2, centers=3
data, label = datasets.make_blobs(n_samples=300, n_features=2,
                                  centers=3, random_state=10)                                

# 繪圓點, 圓點用黑色外框 
plt.scatter(data[:,0], data[:,1], marker="o", edgecolor="black")

plt.title("無監督學習",fontsize=16)

plt.show()

print('------------------------------------------------------------')	#60個

from sklearn import datasets
from sklearn import cluster

# 建立 300 個點, n_features=2, centers=3
data, label = datasets.make_blobs(n_samples=300, n_features=2,
                                  centers=3, random_state=10)
                                  
e = cluster.KMeans(n_clusters=3)    # k-mean方法建立 3 個群集中心物件
e.fit(data)                         # 將數據帶入物件, 做群集分析
print(e.labels_)                    # 列印群集類別標籤
print(e.cluster_centers_)           # 列印群集中心

print('------------------------------------------------------------')	#60個

from sklearn import datasets
from sklearn import cluster

# 建立 300 個點, n_features=2, centers=3
data, label = datasets.make_blobs(n_samples=300, n_features=2,
                                  centers=3, random_state=10)
                                  
e = cluster.KMeans(n_clusters=3)        # k-mean方法建立 3 個群集中心物件
e.fit(data)                             # 將數據帶入物件, 做群集分析
print(e.labels_)                        # 列印群集類別標籤
print(e.cluster_centers_)               # 列印群集中心

# 繪圓點, 圓點用黑色外框, 使用標籤 labels_ 區別顏色, 
plt.scatter(data[:,0], data[:,1], marker="o", c=e.labels_)
# 用紅色標記群集中心
plt.scatter(e.cluster_centers_[:,0], e.cluster_centers_[:,1],marker="*",
            color="red")
plt.title("無監督學習",fontsize=16)

plt.show()

print('------------------------------------------------------------')	#60個

