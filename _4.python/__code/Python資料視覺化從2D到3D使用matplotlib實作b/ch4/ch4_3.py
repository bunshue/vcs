# ch4_3.py
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = 1 / (1 + np.exp(-x))

plt.axhline(y=0, c="blue", ls="--")
plt.axhline(y=0.5, c="red", ls=":")
plt.axhline(y=1.0, c="green", ls="--")
plt.axvline(c="gray", ls="-.")              # 垂直的灰色線條
plt.axline((-2,0),(2,1), c='cyan', lw=3)    # 兩個點的連線
plt.axline((-1,0), slope=0.5,c='y', lw=2)   # 點和斜率的線條
plt.plot(x, y, linewidth=2, c='gray')
plt.xlim(-2*np.pi,2*np.pi)
plt.show()




