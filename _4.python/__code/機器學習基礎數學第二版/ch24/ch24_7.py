# ch24_7.py
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import cluster
import numpy as np

np.random.seed(3)                       # 設定隨機數種子值
# 建立 300 個點, n_features = 2
data, label = datasets.make_blobs(n_samples=300, n_features=2)
                                  
e = cluster.KMeans(n_clusters=3)        # k-mean方法建立 3 個群集中心物件
e.fit(data)                             # 將數據帶入物件, 做群集分析
print(e.labels_)                        # 列印群集類別標籤
print(e.cluster_centers_)               # 列印群集中心
















