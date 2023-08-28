# ch12_3.py
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(10)
data = np.random.random((10, 10))
plt.imshow(data)
plt.colorbar()
plt.show()


