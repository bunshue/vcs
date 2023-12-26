# ch20_26.py
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(100)
y = x
t = x
plt.scatter(x, y, c=t, cmap='rainbow')
plt.show()




