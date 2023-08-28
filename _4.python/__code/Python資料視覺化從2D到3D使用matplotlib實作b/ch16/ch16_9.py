# ch16_9.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
np.random.seed(10) 
data = np.random.randn(500) 
labels = ['data']
mean_mark = dict(markerfacecolor='b',
                 markeredgecolor='b',
                 marker='D')
plt.boxplot(data,labels=labels,vert=False,
            showmeans=True,meanprops=mean_mark)
plt.title("隨機數據的水平箱線圖",fontsize=16,color='b')
plt.show() 



      
