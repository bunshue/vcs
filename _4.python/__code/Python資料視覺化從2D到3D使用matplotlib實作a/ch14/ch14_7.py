# ch14_7.py
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(10)
# 平均值 = 0.0, 標準差 = 1 的隨機數
s = np.random.randn(10000)              # 隨機數
bins = 30
plt.hist(s, bins, density=True)         # 直方圖
plt.show()












