# Python 新進測試 09



#! /usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,360)
y = np.sin( x * np.pi / 180.0)
plt.plot(x,y)
plt.xlim(0,360)
plt.ylim(-1.2,1.2)
plt.title("SIN function")
plt.show()



#! /usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0,360)
y = np.sin( x * np.pi / 180.0)
z = np.cos( x * np.pi / 180.0)
plt.plot(x,y,color="blue")
plt.plot(x,z,color="red")
plt.xlim(0,360)
plt.ylim(-1.2,1.2)
plt.title("SIN & COS function")
plt.show()




#! /usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0,360)
y = np.sin( 2 * x * np.pi / 180.0)
z = np.cos( x * np.pi / 180.0)
plt.plot(x,y,color="blue",label="SIN(2x)")
plt.plot(x,z,color="red",label="COS(x)")
plt.xlim(0,360)
plt.ylim(-1.2,1.2)
plt.xlabel("Degree")
plt.ylabel("Value")
plt.title("SIN & COS function")
plt.legend()
plt.show()

