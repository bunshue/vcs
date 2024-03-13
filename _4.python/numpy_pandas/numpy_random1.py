"""

使用numpy裡面的random函數

"""
import os
import sys
import time
import random

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print('------------------------------------------------------------')	#60個




#mu + sigma * np.random.standard_normal(size=...)
#np.random.normal(mu, sigma, size=...)

for _ in range(10):
    cc = np.random.standard_normal()
    print(cc)

s = np.random.standard_normal(8000)
print(s)
print(s.shape)

s = np.random.standard_normal(size=(3, 4, 2))
print(s)
print(s.shape)


#mean 3 and standard deviation 2.5:
mu = 3
sigma = 2.5

s = mu + sigma * np.random.standard_normal(size=(2, 4))
print(s)
print(s.shape)



print('------------------------------------------------------------')	#60個

#numpy.random.normal

mu, sigma = 0, 0.1 # mean and standard deviation
s = np.random.normal(mu, sigma, 1000)


"""
Verify the mean and the variance:
abs(mu - np.mean(s))
0.0  # may vary

abs(sigma - np.std(s, ddof=1))
0.1  # may vary

"""
import matplotlib.pyplot as plt

count, bins, ignored = plt.hist(s, 30, density=True)

plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
               np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
         linewidth=2, color='r')

plt.show()

s = np.random.normal(3, 2.5, size=(2, 4))
print(s)



print('------------------------------------------------------------')	#60個

#numpy.random.randn
#sigma * np.random.randn(...) + mu

s = 3 + 2.5 * np.random.randn(2, 4)
print(s)

print('------------------------------------------------------------')	#60個

#numpy.random.uniform
#random.uniform(low=0.0, high=1.0, size=None)

s = np.random.uniform(-1,0,10)
print(s)


import matplotlib.pyplot as plt

count, bins, ignored = plt.hist(s, 15, density=True)

plt.plot(bins, np.ones_like(bins), linewidth=2, color='r')

plt.show()

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個



