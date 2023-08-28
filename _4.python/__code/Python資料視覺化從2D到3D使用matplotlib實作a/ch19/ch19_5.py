# ch19_5.py
import matplotlib.pyplot as plt
import numpy as np

x = [1, 3, 5, 7, 9]
y = [1, 9, 25, 49, 81]
plt.bar(x,y,color='yellow')
plt.step(x,y,'*-',where='pre',color='g')
plt.xticks(np.arange(0,10,step=1))
plt.show()


      
