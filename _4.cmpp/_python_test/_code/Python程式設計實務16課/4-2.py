#! /usr/bin/python

import numpy as np
import matplotlib.pyplot as pt
x = np.arange(0,360)
y = np.sin( x * np.pi / 180.0)
z = np.cos( x * np.pi / 180.0)
pt.plot(x,y,color="blue")
pt.plot(x,z,color="red")
pt.xlim(0,360)
pt.ylim(-1.2,1.2)
pt.title("SIN & COS function")
pt.show()

