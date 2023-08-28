# ch6_39.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
x = np.linspace(0, 2*np.pi, 300)
y = np.sin(x**2)
fig = plt.figure()
gs = fig.add_gridspec(3, hspace=0)
ax = gs.subplots(sharex=True, sharey=True)
fig.suptitle('共享 x 和 y 軸', fontsize=18)
ax[0].plot(x, y ** 2, 'b--')
ax[1].plot(x, 0.5 * y, 'go')
ax[2].plot(x, y, 'm+')
# 隱藏內側的刻度標記與標籤
for a in ax.flat:
    a.label_outer()
plt.show()



