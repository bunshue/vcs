# ch17_9.py
import matplotlib.pyplot as plt
import numpy as np

a = 1
radian = np.arange(0,(6 * np.pi),0.01)
for rad in radian:
    r =  a - (a*np.sin(rad))
    plt.polar(rad,r,'r.')
plt.show()





  
      
