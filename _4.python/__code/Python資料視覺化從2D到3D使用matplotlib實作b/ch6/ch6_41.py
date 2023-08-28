# ch6_41.py
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, 1)
x = np.linspace(0, 2*np.pi, 300)
y1 = np.sin(x)
y2 = np.cos(x)
# 繪圖
ax.plot(x, y1)
ax.plot(x, y2, 'g', lw='3')
plt.show()



