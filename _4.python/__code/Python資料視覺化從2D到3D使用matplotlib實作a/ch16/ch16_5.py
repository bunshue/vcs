# ch16_5.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
np.random.seed(10) 
data1 = np.random.normal(80, 30, 250) 
data2 = np.random.normal(90, 50, 250) 
data3 = np.random.normal(100, 20, 250) 
data4 = np.random.normal(75, 40, 250) 
data5 = np.random.normal(60, 35, 250)
data = [data1, data2, data3, data4, data5] 
labels = ['data1','data2','data3','data4','data5']
my_mark = dict(markerfacecolor='r',marker='o')
plt.boxplot(data,labels=labels,flierprops=my_mark)
plt.title("5 組數據的箱線圖",fontsize=16,color='b')
plt.show() 



      
