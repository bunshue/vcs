# ch23_7.py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 20)
y = np.sin(x) * 2
dy = 0.5
plt.errorbar(x,y,yerr=dy,ecolor='r',uplims=True,lolims=True)
plt.title('uplims, lolims = True',color='b')
plt.show()


      
