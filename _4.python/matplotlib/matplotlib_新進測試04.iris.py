import sys
import math

import numpy as np

import matplotlib.pyplot as plt

dataset = np.loadtxt('iris.csv', delimiter=',')

print(dataset)


sys.exit()

fig = plt.figure()
ax = fig.add_subplot(111)

color = ['r','y','b']
species = ['Setosa','Versicolour','Virginica']
Setosa = []
Versicolour = []
Virginica = []

# 不同种类保存为不同的列表
for i in range(len(dataset)):
    if dataset[i][-1] == 0:
        Setosa.append(dataset[i].tolist())
    elif dataset[i][-1] == 1:
        Versicolour.append(dataset[i].tolist())
    elif dataset[i][-1] == 2:
        Virginica.append(dataset[i].tolist())


ax.scatter(x=np.array(Setosa)[:,0], # Setosa种类的花瓣的长度
     y=np.array(Setosa)[:,1], # Setosa种类的花瓣的宽度
     s=35,                    # 散点大小为35
     c=color[0],              # 颜色为红色
     label=species[0])        # 标签为Setosa

ax.scatter(x=np.array(Versicolour)[:,0],    # Versicolour种类的花瓣的长度
     y=np.array(Versicolour)[:,1],    # Versicolour种类的花瓣的宽度
     s=35,                            # 散点大小为35
     c=color[1],                      # 颜色为黄色
     label=species[1])                # 标签为Versicolour

ax.scatter(x=np.array(Virginica)[:,0],  # Virginica种类的花瓣的长度
     y=np.array(Virginica)[:,1],  # Virginica种类的花瓣的宽度
     s=35,                        # 散点大小为35
     c=color[2],                  # 颜色为蓝色
     label=species[2])            # 标签为Virginica

# 添加轴标签和标题
ax.set_title('花瓣长度与宽度的关系',
       fontproperties='SimHei',
       fontsize=20)
ax.set_xlabel('花瓣的长度',
        fontproperties='SimHei',
        fontsize=15)
ax.set_ylabel('花瓣的宽度',
        fontproperties='SimHei',
        fontsize=15)

ax.legend(loc='best') # 添加图例

    
print('------------------------------------------------------------')	#60個

    
print('------------------------------------------------------------')	#60個

    
print('------------------------------------------------------------')	#60個
