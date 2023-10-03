# ch6_8.py
import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t) * np.sin(2*np.pi*t)

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False

x = np.linspace(0.0, np.pi, 100)

plt.subplot(2,2,1)          # 子圖 1
plt.plot(x, f(x))
plt.title('子圖 1')

plt.subplot(2,2,2)          # 子圖 2
plt.plot(x, f(x))
plt.title('子圖 2')

plt.subplot(2,1,2)          # 子圖 3
plt.plot(x, f(x))
plt.title('子圖 3')

plt.show()
