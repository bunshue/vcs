# ch11_3.py
import matplotlib.pyplot as plt
import numpy as np

N= 5000
x = np.random.rand(N)
y = np.random.rand(N)
plt.scatter(x, y, c=y)
plt.colorbar()                  # 建立色彩條
plt.show()








