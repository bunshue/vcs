# ch19_24.py
import matplotlib.pyplot as plt
import numpy as np

s = np.random.uniform(0.0,5.0,size=250)     # 隨機數
plt.hist(s, 5)                              # 直方圖
plt.show()











