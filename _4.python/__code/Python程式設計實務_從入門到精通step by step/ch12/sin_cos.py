# -*- coding: utf-8 -*-
"""
正弦函數 s=sin(x) 
餘弦函數 c=cos(x)
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)
s, c=np.sin(x), np.cos(x)
plt.plot(x, s)
plt.plot(x, c)
plt.xticks([-2*np.pi,-np.pi,0, np.pi, 2*np.pi],['-$2\pi$', '-$\pi$','0', '$\pi$', '$2\pi$'])
plt.legend(['sin','cos'])
plt.show()
