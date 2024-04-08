import numpy as np
import matplotlib.pyplot as plt

# 曲线数据加入噪声

x = np.linspace(-5,5,200);
y = np.sin(x);# 给出y与x的基本关系
yn = y+np.random.rand(1,len(y))*1.5 ;	# 加入噪声的点集

plt.scatter(x,yn,c='blue',marker='o')
plt.plot(x,y+0.75,'r') 

plt.show()

