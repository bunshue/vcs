# ch6_32.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
x = np.linspace(0, 2*np.pi, 300)
y = np.sin(x**2)
fig, ax = plt.subplots(3, sharex=True, sharey=True)
fig.suptitle('共享 x 和 y 軸', fontsize=18)
ax[0].plot(x, y ** 2, 'b--')
ax[1].plot(x, 0.5 * y, 'go')
ax[2].plot(x, y, 'm+')
plt.show()



