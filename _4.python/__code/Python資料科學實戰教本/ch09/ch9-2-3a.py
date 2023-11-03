import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(1000)
num_bins = 50
plt.hist(x, num_bins)
plt.show()

