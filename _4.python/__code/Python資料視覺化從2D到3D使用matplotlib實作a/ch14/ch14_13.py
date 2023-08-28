# ch14_13.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
np.random.seed(10)
mu = 0                                                  # 平均值
sigma = 1                                               # 標準差
s = np.random.randn(10000)                              # 隨機數
bins = 30
count, bins, ignored = plt.hist(s, bins, density=True)  # 直方圖
# 繪製折線圖
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
         np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
         linewidth=2, color='r')
plt.title('常態分布 ' + r'$\mu=0, \sigma=1$',fontsize=16) 
plt.show()












