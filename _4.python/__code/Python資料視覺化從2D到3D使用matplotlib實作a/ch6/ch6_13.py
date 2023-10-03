# ch6_13.py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 500)
y = np.sin(x**2)
ax = plt.subplot()      # 回傳子圖物件
ax.plot(x, y)           # 使用子圖物件調用plot()函數
ax.set_title("Sin function")
ax.set_xlabel("x")
ax.set_ylabel("y")

plt.show()
