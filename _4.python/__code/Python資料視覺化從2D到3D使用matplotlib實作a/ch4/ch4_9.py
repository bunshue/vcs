# ch4_9.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False  
x = np.arange(0.0, 3, 0.01)
y = np.sin(2 * np.pi * x)
plt.plot(x, y)                  # 繪製 sin(2 * pi * x)

plt.fill(x, y, 'y', alpha=0.3)  # 黃色填充
plt.xlabel('角度')
plt.ylabel('Sin波形值')
plt.title('Sin波形')
plt.show()



