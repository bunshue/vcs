# ch6_42.py
import matplotlib.pyplot as plt
import numpy as np

fig, ax1 = plt.subplots(1, 1)
ax2 = ax1.twinx()               # 使用相同的 x 軸
# y1 = sin(x)
x = np.linspace(0, 2*np.pi, 300)
y1 = np.sin(x)
# y2 = cos(x)
y2 = np.cos(x)
# 繪圖
ax1.plot(x, y1)
ax2.plot(x, y2, 'g', lw='3')
plt.show()



