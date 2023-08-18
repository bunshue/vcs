# ch24_8.py
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

plt.rcParams["font.family"] = ["Microsoft JhengHei"]    # 微軟正黑體
plt.rcParams["axes.unicode_minus"] = False              # 可以顯示負號
# 繪圓點, 圓點用黑色外框, 使用標籤 labels_ 區別顏色, 
plt.scatter(data[:,0], data[:,1], marker="o", c=e.labels_)
# 用紅色標記群集中心
plt.scatter(e.cluster_centers_[:,0], e.cluster_centers_[:,1],marker="*",
            color="red")
plt.title("無監督學習")
plt.show()














