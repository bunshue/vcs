# ch9_9.py
import matplotlib.pyplot as plt
import numpy as np

# 繪製此函數圖形
x = np.linspace(-2, 2, 100)
y = x**3 - x
plt.plot(x, y)
plt.grid()
plt.show()












