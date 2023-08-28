# ch12_4.py
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(10)
data = np.random.random((80, 80))
plt.imshow(data, cmap='cool')
plt.colorbar()
plt.show()


