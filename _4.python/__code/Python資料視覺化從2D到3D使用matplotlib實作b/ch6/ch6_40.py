# ch6_40.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
x = np.linspace(0, 2*np.pi, 300)
y = np.sin(x**2)
fig = plt.figure()
gs = fig.add_gridspec(2, 2, hspace=0, wspace=0)
(ax1, ax2), (ax3, ax4) = gs.subplots(sharex='col', sharey='row')
fig.suptitle('共享 x(column) 和 y(row) 軸', fontsize=18)
ax1.plot(x, y, 'b')
ax2.plot(x, y ** 2, 'g')
ax3.plot(x+1, y, 'm')
ax4.plot(x+2, y ** 2, 'r')
plt.show()



