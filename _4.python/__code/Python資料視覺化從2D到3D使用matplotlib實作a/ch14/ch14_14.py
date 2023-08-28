# ch14_14.py
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
np.random.seed(10)
mu = 0                                                  # 平均值
sigma = 1                                               # 標準差
s = np.random.randn(10000)                              # 隨機數
bins = 30
count, bins, ignored = plt.hist(s, bins, density=True)  # 直方圖
sns.kdeplot(s)                                          # 核密度估計圖
plt.title('使用kdeplot()函數繪製常態分布 ' + r'$\mu=0, \sigma=1$',fontsize=16) 
plt.show()












