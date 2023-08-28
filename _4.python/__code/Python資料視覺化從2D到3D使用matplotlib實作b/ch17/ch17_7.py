# ch17_7.py
import matplotlib.pyplot as plt
import numpy as np

radian = np.arange(0,(6 * np.pi),0.01)
for rad in radian:
    r = rad
    plt.polar(rad,r,'b.')
plt.show()





  
      
