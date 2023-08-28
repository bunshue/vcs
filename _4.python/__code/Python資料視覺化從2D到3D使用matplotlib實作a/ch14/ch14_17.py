# ch14_17.py
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
np.random.seed(10)
bins = 20
x = np.random.randn(10000, 3)   
colors = ['red', 'green', 'blue'] 
plt.hist(x,bins,density=True,color=colors,label=colors) 
plt.legend()  
plt.title('3 組數據的常態分佈隨機數',fontsize=16)
plt.show()


