# ch16_12.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
np.random.seed(10) 
data = np.random.randn(500) 
labels = ['data']
plt.boxplot(data,labels=labels,showfliers=False)
plt.title("隱藏箱線圖的異常值",fontsize=16,color='b')
plt.show() 



      
