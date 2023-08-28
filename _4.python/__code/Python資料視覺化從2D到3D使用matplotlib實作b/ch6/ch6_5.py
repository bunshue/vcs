# ch6_5.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
# 建立衰減數列.
x1 = np.linspace(0.0, 5.0, 50)
y1 = np.cos(3 * np.pi * x1) * np.exp(-x1)
# 建立非衰減數列
x2 = np.linspace(0.0, 2.0, 50)
y2 = np.cos(3 * np.pi * x2)

plt.subplot(2,1,1)
plt.title('衰減數列')
plt.plot(x1, y1, 'go-')
plt.ylabel('衰減值')

plt.subplot(2,1,2)
plt.plot(x2, y2, 'm.-')
plt.xlabel('時間(秒)')
plt.ylabel('非衰減值')

plt.show()



