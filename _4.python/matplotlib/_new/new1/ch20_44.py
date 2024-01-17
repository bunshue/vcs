# ch20_44.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
# 建立衰減數列.
x = np.linspace(0.0, 5.0, 50)
y = np.cos(3 * np.pi * x) * np.exp(-x)

plt.title(r'衰減數列 cos($3\pi x * e^{x})$',fontsize=20)
plt.plot(x, y, 'go-')
plt.ylabel('衰減值')
plt.show()


