# ch6_50.py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 500)
y = np.sin(2 * np.pi * x) + 1
fig = plt.figure()
ax = plt.axes()
#ax.set_xlim([1, 5])
#ax.set_ylim([-0.5, 2.5])
plt.plot(x, y)
plt.show()



