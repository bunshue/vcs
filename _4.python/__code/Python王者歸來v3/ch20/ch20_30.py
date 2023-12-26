# ch20_30.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
# 繪製半徑 5 的圓
angle = np.linspace(0, 2*np.pi, 100)
fig, ax = plt.subplots(2, 2)    # 建立 2 x 2 子圖

ax[0, 0].plot(5 * np.cos(angle), 5 * np.sin(angle))
ax[0, 0].set_title('繪圓形, 看起來像橢圓')
ax[0, 1].plot(5 * np.cos(angle), 5 * np.sin(angle))
ax[0, 1].axis('equal')
ax[0, 1].set_title('寬高比相同, 是圓形')
ax[1, 0].plot(5 * np.cos(angle), 5 * np.sin(angle))
ax[1, 0].axis('equal')
ax[1, 0].set(xlim=(-5, 5), ylim=(-5, 5))
ax[1, 0].set_title('設定寬和高相同區間')
ax[1, 1].plot(5 * np.cos(angle), 5 * np.sin(angle))
ax[1, 1].set_aspect('equal', 'box')
ax[1, 1].set_title('設定寬高比相同')
fig.tight_layout()
plt.show()



     
