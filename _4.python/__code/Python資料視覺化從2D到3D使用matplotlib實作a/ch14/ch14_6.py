# ch14_6.py
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(10)
s = np.random.uniform(0.0,5.0,size=250) # 隨機數
plt.hist(s, 5)                          # bin=5的直方圖
plt.show()











