# ch24_1.py
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets

np.random.seed(3)                           # 設計隨機數種子
x, y = datasets.make_regression(n_features=1, noise=20)
plt.xlim(-3, 3)
plt.ylim(-150, 150)
plt.scatter(x,y)
plt.show()















