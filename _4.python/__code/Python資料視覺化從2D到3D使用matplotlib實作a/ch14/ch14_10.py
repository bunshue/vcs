# ch14_10.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
mu = 100                                # 均值
sigma = 15                              # 標準差
np.random.seed(10)
s = np.random.normal(mu, sigma, 10000)  # 隨機數
bins = 30
plt.hist(s, bins, density=True)         # 直方圖

plt.xlabel('智商指數',color='b')
plt.ylabel('機率',color='b')
plt.title('智商IQ指標直方圖',color='m')
plt.text(120,0.02,r'$\mu=100,\ \sigma=15$',color='b')
plt.grid(True)
plt.show()











