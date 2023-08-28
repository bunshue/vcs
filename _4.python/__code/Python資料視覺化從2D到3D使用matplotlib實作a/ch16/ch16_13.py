# ch16_13.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
np.random.seed(10) 
data = np.random.randn(500) 
labels = ['data']
caps_line = dict(linestyle='--',
                 linewidth=2.5,
                 color='b')
plt.boxplot(data,labels=labels,vert=False,capprops=caps_line)
plt.title("設計水平箱線圖的caps",fontsize=16,color='b')
plt.show() 



      
