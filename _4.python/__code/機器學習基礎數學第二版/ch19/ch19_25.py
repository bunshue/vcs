# ch19_25.py
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

s = np.random.uniform(size=10000)           # 隨機數

plt.hist(s, 30, density=True)               # 直方圖
# 繪製曲線圖
sns.kdeplot(s)
plt.show()











