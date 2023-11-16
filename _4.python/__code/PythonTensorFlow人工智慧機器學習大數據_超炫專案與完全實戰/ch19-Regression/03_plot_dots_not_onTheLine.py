#!/usr/bin/env python
# author: Powen Ko      www.powenko.com
import matplotlib.pyplot as plt
import numpy as np
plt.plot([1,2,3,4], [0,0.3,0.6,0.9], 'gx')
plt.plot([1,2,3,4], [0,0.3,0.6,0.9], 'r--')


X = 1+np.arange(30)/10
delta = np.random.uniform(low=-0.1,high=0.1, size=(30,))
Y=0.3*X- 0.3  + delta
plt.plot(X, Y, 'bo')
plt.ylabel('Y')
plt.xlabel('X')
plt.show()
