# ch17_1.py
import matplotlib.pyplot as plt
import numpy as np

pts = 12
theta = np.linspace(0,2*np.pi,pts,endpoint=False)
r = 50*np.random.rand(pts)
plt.polar(theta,r)
plt.show()





  
      
