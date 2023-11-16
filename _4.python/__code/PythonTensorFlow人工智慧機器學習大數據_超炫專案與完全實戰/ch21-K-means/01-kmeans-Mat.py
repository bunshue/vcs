#!/usr/bin/python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

X= np.array([[1,1],[1.1,1.1],[1.2,1.2],
   [2,2], [2.1,2.1], [2.2,2.2]])
y=[1,1,1,
   0,0,0]

plt.axis([0, 3, 0, 3])
plt.plot(X[:3,0], X[:3,1], 'yx' )
plt.plot(X[3:,0], X[3:,1], 'g.' )
plt.ylabel('H cm')
plt.xlabel('W cm')
plt.legend(('A','B'),
           loc='upper right')
plt.show()