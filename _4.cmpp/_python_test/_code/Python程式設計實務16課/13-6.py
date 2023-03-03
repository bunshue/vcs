# _*_ coding: utf-8 _*_
# 程式 13-6 (Python 3 Version)

import matplotlib.pyplot as pt
import numpy as np

degree = np.linspace(0, 2*np.pi, 200)
x = np.cos(degree)
y = np.sin(degree)

pt.xlim(-1.5, 1.5)
pt.ylim(-1.5, 1.5)
pt.plot(x, y, 'bo')
pt.plot(0.5*x, 1.5*y, 'ro')

pt.show()