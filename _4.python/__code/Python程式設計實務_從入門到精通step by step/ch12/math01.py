# -*- coding: utf-8 -*- 

import matplotlib.pyplot as plt
import numpy as np
	
x = np.linspace(0, 30, 20)
y = 3*x+2
plt.plot(x,y,color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Unary equation')
plt.grid(b=True, which='major')
plt.show()
