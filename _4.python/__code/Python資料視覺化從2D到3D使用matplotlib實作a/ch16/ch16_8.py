# ch16_8.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
np.random.seed(10) 
data = np.random.randn(500) 
labels = ['data']
plt.boxplot(data,labels=labels,vert=False,showmeans=True)
plt.title("隨機數據的水平箱線圖",fontsize=16,color='b')
plt.show() 



      
