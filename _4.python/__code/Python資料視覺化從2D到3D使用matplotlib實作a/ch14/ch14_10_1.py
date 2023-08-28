# ch14_10_1.py
import numpy as np
import matplotlib.pyplot as plt

x1 = np.random.normal(50,5,10000)
x2 = np.random.normal(60,5,50000)
plt.hist(x1,range=(30,80),bins=20,color='g',alpha=0.8)
plt.hist(x2,range=(30,80),bins=20,color='m',alpha=0.8)
plt.show()


