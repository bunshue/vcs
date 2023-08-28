# ch17_6.py
import matplotlib.pyplot as plt
import numpy as np

a = 6           # 主軸半徑
b = 3           # 次軸半徑

radian = np.arange(0, (2 * np.pi), 0.01)
for rad in radian:
    r = (a*b)/np.sqrt((a*np.sin(rad))**2 + (b*np.cos(rad))**2)
    plt.polar(rad,r,'b.')
plt.show()





  
      
