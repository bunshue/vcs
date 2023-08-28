# ch14_9.py
import matplotlib.pyplot as plt
import numpy as np

mu = 0                                  # 均值
sigma = 1                               # 標準差
np.random.seed(10)
s = np.random.normal(mu, sigma, 10000)  # 隨機數
bins = 30
plt.hist(s, bins, density=True)         # 直方圖
plt.show()











