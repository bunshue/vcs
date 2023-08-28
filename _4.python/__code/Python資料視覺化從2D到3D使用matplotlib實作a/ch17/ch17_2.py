# ch17_2.py
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(15)
pts = 12
theta = np.linspace(0,2*np.pi,pts,endpoint=False)
r = 50*np.random.rand(pts)
plt.polar(theta,r,'-',marker='*',color='g')
plt.show()





  
      
