# ex20_14.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
x = np.linspace(0, 2*np.pi, 300)
y = np.sin(x)
fig = plt.figure()
ax1 = fig.add_subplot(121,projection='polar')
ax1.plot(x, y)
ax1.set_title("極座標 Sin 圖",fontsize=12)
ax2 = fig.add_subplot(122)
ax2.plot(x, y)
ax2.set_title('一般座標 Sin 圖',fontsize=12)
ax2.set_aspect(2)
plt.tight_layout()                      # 緊縮佈局
plt.show()



