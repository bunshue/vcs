# ch17_5.py
import matplotlib.pyplot as plt
import numpy as np

radian = np.arange(0, (2 * np.pi), 0.01)
for r in range(1,3):
    for rad in radian:
        plt.polar(rad,r,'b.')
plt.show()





  
      
