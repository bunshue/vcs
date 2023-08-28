# ch4_1.py
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = 1 / (1 + np.exp(-x))

plt.axhline(y=0, color="blue", linestyle="--")
plt.axhline(y=0.5, color="red", linestyle=":")
plt.axhline(y=1.0, color="green", linestyle="--")
plt.plot(x, y, linewidth=2, c='gray')
plt.xlim(-2*np.pi,2*np.pi)
plt.show()




