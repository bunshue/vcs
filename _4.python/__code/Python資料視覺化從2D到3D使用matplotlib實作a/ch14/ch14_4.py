# ch14_4.py
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(10)
x = np.random.rand(1000)
plt.hist(x)
plt.title('np.random.rand()')
plt.show()



