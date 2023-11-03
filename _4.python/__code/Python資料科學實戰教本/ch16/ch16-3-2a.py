import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn import cluster
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

iris = datasets.load_iris()

X = pd.DataFrame(iris.data, columns=iris.feature_names)
X.columns = ["sepal_length","sepal_width","petal_length","petal_width"]
y = iris.target
k = 3

kmeans = cluster.KMeans(n_clusters=k, random_state=12)
kmeans.fit(X)
print("K-means分類(K-means Classification):")
print(kmeans.labels_)
# 修正標籤錯誤
pred_y = np.choose(kmeans.labels_, [2,0,1]).astype(np.int64)
print("K-means修正分類(K-means Fix Classification):")
print(pred_y) 
print("真實分類(Real Classification):")
print(y)

colmap = np.array(["r", "g", "y"])
plt.figure(figsize=(10,5))
plt.subplot(1, 2, 1)
plt.subplots_adjust(hspace = .5)
plt.scatter(X["petal_length"], X["petal_width"],
            color=colmap[y])
plt.xlabel("花瓣長度(Petal Length)")
plt.ylabel("花瓣寬度(Petal Width)")
plt.title("真實分類(Real Classification)")
plt.subplot(1, 2, 2)
plt.scatter(X["petal_length"], X["petal_width"], 
            color=colmap[pred_y])
plt.xlabel("花瓣長度(Petal Length)")
plt.ylabel("花瓣寬度(Petal Width)")
plt.title("K-means分類(K-means Classification)")
plt.show()
