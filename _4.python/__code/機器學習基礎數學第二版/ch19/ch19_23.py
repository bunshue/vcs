# ch19_23.py
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

mu = 0                                                  # 均值
sigma = 1                                               # 標準差
s = np.random.normal(mu, sigma, 10000)                  # 隨機數

count, bins, ignored = plt.hist(s, 30, density=True)    # 直方圖
# 繪製曲線圖
sns.kdeplot(s)
plt.show()











