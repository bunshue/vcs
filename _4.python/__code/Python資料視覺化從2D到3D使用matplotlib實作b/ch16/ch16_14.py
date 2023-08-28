# ch16_14.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
np.random.seed(10) 
data1 = np.random.randn(1000) 
data2 = np.random.randn(1000) 
data3 = np.random.randn(1000) 
data = [data1, data2, data3] 
labels = ['data1','data2','data3']
plt.boxplot(data,labels=labels,notch=True)
plt.title("notch=True 的箱線圖",fontsize=16,color='b')
plt.show() 



      
