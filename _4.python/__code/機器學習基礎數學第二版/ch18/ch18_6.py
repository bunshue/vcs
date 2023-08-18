# ch18_6.py
import matplotlib.pyplot as plt
import numpy as np

degrees = np.arange(0, 360)
x = np.cos(np.radians(degrees))
y = np.sin(np.radians(degrees))

plt.plot(x,y)
plt.axis('equal')
plt.grid()
plt.show()
