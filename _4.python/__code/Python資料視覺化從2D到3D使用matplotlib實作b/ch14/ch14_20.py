# ch14_20.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
np.random.seed(10)
mu = 0                                          # 平均值
sigma1 = 25                                     # x1 資料標準差
x1 = np.random.normal(mu, sigma1, size=100)     # 建立 x1 資料

sigma2 = 10                                     # x2 資料標準差
x2 = np.random.normal(mu, sigma2, size=100)     # 建立 x1 資料

fig, axs = plt.subplots(nrows=2, ncols=2)       # 建立 2 x 2 子圖
# 建立 [0,0]子圖
axs[0,0].hist(x1,15,density=True,histtype='step')
axs[0,0].set_title("histtype = 'step'")
# 建立 [0,1]子圖
axs[0,1].hist(x1,15,density=True,histtype='stepfilled',
              color='m',alpha=0.8)
axs[0,1].set_title("histtype = 'stepfilled'")
# 建立 [1,0]子圖
axs[1,0].hist(x1,density=True,histtype='barstacked',rwidth=0.8)
axs[1,0].hist(x2,density=True,histtype='barstacked',rwidth=0.8)
axs[1,0].set_title("histtype = 'barstacked'")
# 建立 [1,1]子圖, 寬度不相等
bins = [-60, -50, -20, -10, 30, 50]
axs[1,1].hist(x1,bins,density=True,histtype='bar',rwidth=0.8,color='g')
axs[1,1].set_title("histtype = 'bar' 不相等寬度的 bins")
fig.tight_layout()
plt.show()


      
