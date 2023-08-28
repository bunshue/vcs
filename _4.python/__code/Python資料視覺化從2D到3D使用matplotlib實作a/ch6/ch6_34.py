# ch6_34.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
x = np.linspace(0, 2*np.pi, 300)
y = np.sin(x)
fig, (ax1,ax2) = plt.subplots(1,2,subplot_kw=dict(projection='polar'))
ax1.plot(x, y)
ax1.set_title("極座標 Sin 圖",fontsize=12)
ax2.plot(x, y ** 2)
ax2.set_title('極座標 Sin 平方圖',fontsize=12)
plt.tight_layout()                      # 緊縮佈局
plt.show()



