# ch14_3_2.py
import matplotlib.pyplot as plt
import numpy as np

x = [4,3,3,2,5,4,5,6,9,4,5,5,3,0,1,7,8,7,5,6,4]
plt.hist(x,bins=5,color='g',cumulative=True,rwidth=0.8)    
plt.show()


      
