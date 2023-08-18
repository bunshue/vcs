# ch1_29_1.py
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["font.family"] = ["Microsoft JhengHei"]    # 微軟正黑體

pts = np.arange(-2, 2, 0.01)
x, y = np.meshgrid(pts, pts)
z = np.sqrt(x**2 + y**2)

ticks = np.arange(0, 500, 100)
seq = np.arange(-2, 3)

plt.imshow(z, cmap='rainbow')
plt.xticks(ticks, seq)
plt.yticks(ticks, seq)

plt.colorbar()
plt.title(r"建立$\sqrt{x^2 + y^2}$網格影像")
plt.show()


