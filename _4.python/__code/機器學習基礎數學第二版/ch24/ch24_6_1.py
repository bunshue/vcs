# ch24_6.py
import matplotlib.pyplot as plt
from sklearn import datasets
import numpy as np

np.random.seed(3)                                       # 設定隨機數種子值
# 建立 300 個點, n_features = 2
data, label = datasets.make_blobs(n_samples=300, n_features=2)                                

plt.rcParams["font.family"] = ["Microsoft JhengHei"]    # 微軟正黑體
plt.rcParams["axes.unicode_minus"] = False              # 可以顯示負號
# 繪圓點, 圓點用黑色外框 
plt.scatter(data[:,0], data[:,1], marker="o", edgecolor="black")

plt.title("無監督學習")
plt.show()















