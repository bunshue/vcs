# ch14_15.py
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

s = np.random.uniform(size=10000)   # 隨機數
plt.hist(s, 30, density=True)       # 直方圖
sns.kdeplot(s)                      # 核密度估計圖
plt.show()











