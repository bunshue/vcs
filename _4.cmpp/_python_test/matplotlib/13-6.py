# plot 畫兩條線

import matplotlib.pyplot as plt
import numpy as np

degree = np.linspace(0, 2*np.pi, 200)
x = np.cos(degree)
y = np.sin(degree)

plt.plot(x, y, 'bo')
plt.plot(0.5*x, 1.5*y, 'ro')


plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

plt.show()
