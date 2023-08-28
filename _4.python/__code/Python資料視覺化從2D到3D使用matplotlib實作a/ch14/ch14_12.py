# ch14_12.py
import numpy as np
import matplotlib.pyplot as plt

left = -2
peak = 8                        # mode尖峰值
right = 10
bins = 200
s = np.random.triangular(left,peak,right,10000)
plt.hist(s, bins, density=True)
plt.show()









