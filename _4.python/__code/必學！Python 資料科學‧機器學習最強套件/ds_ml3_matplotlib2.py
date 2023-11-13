"""

必學！Python 資料科學‧機器學習最強套件 matplotlib 2

"""

import os
import sys
import time
import random


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


10-1-1 設定資料點的樣式及色彩

import numpy as np

import matplotlib.pyplot as plt

​

days = np.arange(1, 11) 

weight = np.array([10, 14, 18, 20, 18, 16, 17, 18, 20, 17])

​

plt.ylim([0, weight.max()+1])   

plt.xlabel('days')

plt.ylabel('weight')

​

plt.plot(days, weight, marker='o', markerfacecolor='black') 

​

plt.show()

​

#10-1-2 設定折線的樣式、寬度及顏色

import numpy as np

import matplotlib.pyplot as plt

​

days = np.arange(1, 11)

weight = np.array([10, 14, 18, 20, 18, 16, 17, 18, 20, 17])

​

plt.ylim([0, weight.max()+1])

plt.xlabel('days')

plt.ylabel('weight')

​

plt.plot(days, weight, marker='o', markerfacecolor='red',

         linestyle='--', linewidth=2.5, color='green')  

​

plt.show()

​

#10-2-1 繪製長條圖 – bar()

import numpy as np

import matplotlib.pyplot as plt

​

x = [1, 2, 3, 4, 5, 6]          

y = [12, 41, 32, 36, 21, 17]    

plt.bar(x, y)

plt.show()

​

#10-2-2 設定長條圖橫軸標籤

import numpy as np

import matplotlib.pyplot as plt

​

x = [1, 2, 3, 4, 5, 6]

y = [12, 41, 32, 36, 21, 17]

labels = ['Apple', 'Orange', 'Banana', 'Pineapple', 'Kiwifruit', 'Strawberry']

​

plt.bar(x, y, tick_label=labels)

plt.show()

​

#10-2-3 繪製堆疊長條圖

import numpy as np

import matplotlib.pyplot as plt

​

x = [1, 2, 3, 4, 5, 6]

y1 = [12, 41, 32, 36, 21, 17]

y2 = [43, 1, 6, 17, 17, 9]

​

labels = ['Apple', 'Orange', 'Banana', 'Pineapple', 'Kiwifruit', 'Strawberry']

plt.bar(x, y1, tick_label=labels)               #繪製 y1 長條圖

plt.bar(x, y15, tick_label=labels, bottom=y1)   #繪製 y2 長條圖

​

plt.legend(('y1', 'y2'))            #顯示圖例來識別 y1 與 y2

plt.show()

​

---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-1-c4267aa4556e> in <module>()
      8 labels = ['Apple', 'Orange', 'Banana', 'Pineapple', 'Kiwifruit', 'Strawberry']
      9 plt.bar(x, y1, tick_label=labels)                               #繪製 y1 長條圖
---> 10 plt.bar(x, y15, tick_label=labels, bottom=y1)   #繪製 y2 長條圖
     11 
     12 plt.legend(('y1', 'y2'))                        #顯示圖例來識別 y1 與 y2

NameError: name 'y15' is not defined

#10-3-1 繪製直方圖

import numpy as np

import matplotlib.pyplot as plt

​

np.random.seed(0)

data = np.random.randn(10000)

​

plt.hist(data, bins='auto')

plt.show()

​

import numpy as np

import matplotlib.pyplot as plt

​

np.random.seed(0)

data = np.random.randn(10000)

​

plt.hist(data, bins='auto', density=True)

plt.show()

#10-4-1 散佈圖的繪製語法 – scatter()

import numpy as np

import matplotlib.pyplot as plt

​

np.random.seed(0)

x = np.random.randn(100)    

y = np.random.randn(100)

​

plt.scatter(x, y)

plt.show()

​

#10-4-2 設定各資料點的樣式

import numpy as np

import matplotlib.pyplot as plt

​

np.random.seed(0)

x = np.random.randn(100)

y = np.random.randn(100)

​

plt.scatter(x, y, marker='^', color='black')    

plt.show()

​

#10-4-3 設定資料點的大小

import numpy as np

import matplotlib.pyplot as plt

​

np.random.seed(0)

x = np.random.randn(100)

y = np.random.randn(100)

size = np.random.choice(np.arange(100), 100)

​

plt.scatter(x, y, s=30)

plt.tight_layout()

plt.show()

​

#10-4-4 給散佈圖的點套上不同深淺顏色

import numpy as np

import matplotlib.pyplot as plt

​

np.random.seed(0)

x = np.random.randn(100)

y = np.random.randn(100)

c = np.random.choice(np.arange(100), 100)

​

plt.scatter(x, y, s=c, c=c, cmap='viridis')

​

​

plt.show()

#10-5-1 圓餅圖的繪製語法 – pie()

import numpy as np

import matplotlib.pyplot as plt

​

data = [60, 20, 10, 5, 3, 2]        

​

plt.pie(data)       

plt.show()

​

​

​

#10-5-2 給圓餅圖各區域設定標籤並顯示百分比

import numpy as np

import matplotlib.pyplot as plt

data = [60, 20, 10, 5, 3, 2]

labels = ['Apple', 'Orange', 'Banana', 'Pineapple', 'Kiwifruit', 'Strawberry']  

​

plt.pie(data, labels=labels,autopct="%.2f%%")   

plt.tight_layout()

plt.show()

​

#10-5-3 將圓餅圖的特定區塊向外推

import numpy as np

import matplotlib.pyplot as plt

​

data = [60, 20, 10, 5, 3, 2]

labels = ['Apple', 'Orange', 'Banana', 'Pineapple', 'Kiwifruit', 'Strawberry']

explode = [0, 0, 0.1, 0.2, 0, 0]    

​

plt.pie(data, labels=labels, explode=explode,autopct="%.2f%%")

plt.tight_layout()

plt.show()

​

​

#10-5-4 給圓餅圖加入立體陰影

import numpy as np

import matplotlib.pyplot as plt

​

data = [60, 20, 10, 5, 3, 2]

labels = ['Apple', 'Orange', 'Banana', 'Pineapple', 'Kiwifruit', 'Strawberry']

explode = [0, 0, 0.2, 0, 0, 0]      

​

plt.pie(data, labels=labels, explode=explode, shadow=True)  

plt.show()

​

#10-6-1 匯入 3D 套件並繪製子圖

import numpy as np

import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

​

t = np.linspace(-2 * np.pi, 2 * np.pi)      

x, y = np.meshgrid(t, t)                

z = np.sin(np.sqrt(x ** 2 + y ** 2))        

​

​

fig = plt.figure()

ax = fig.add_subplot(1, 1, 1, projection='3d')      #建立 3D 子圖畫布

​

ax.plot_surface(x, y, z)   #畫出三軸資料所構成的曲面

​

plt.tight_layout()

plt.show()

​

#10-6-2 繪製曲面 – plot_surface()

import numpy as np

import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

​

t = np.linspace(-5, 5, num=50)  

x, y = np.meshgrid(t, t)            

z = x * y                       

​

fig = plt.figure()

ax = fig.add_subplot(1, 1, 1, projection='3d')

ax.plot_surface(x, y, z)

plt.show()

​

z

array([[ 25.        ,  23.97959184,  22.95918367, ..., -22.95918367,
,        -23.97959184, -25.        ],
,       [ 23.97959184,  23.00083299,  22.02207414, ..., -22.02207414,
,        -23.00083299, -23.97959184],
,       [ 22.95918367,  22.02207414,  21.0849646 , ..., -21.0849646 ,
,        -22.02207414, -22.95918367],
,       ...,
,       [-22.95918367, -22.02207414, -21.0849646 , ...,  21.0849646 ,
,         22.02207414,  22.95918367],
,       [-23.97959184, -23.00083299, -22.02207414, ...,  22.02207414,
,         23.00083299,  23.97959184],
,       [-25.        , -23.97959184, -22.95918367, ...,  22.95918367,
,         23.97959184,  25.        ]])

#10-6-3 給曲面套上顏色

import numpy as np

import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

​

t = np.linspace(-5, 5)

x, y = np.meshgrid(t, t)

z = x * y

​

fig = plt.figure()

ax = fig.add_subplot(1, 1, 1, projection='3d')

ax.plot_surface(x, y, z, cmap='viridis') 

plt.show()

​

#10-6-4 繪製 3D 長條圖

import numpy as np

import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

#plt.rcParams['font.size'] = 16

#fig = plt.figure(figsize=(12, 8))

fig = plt.figure()

ax = fig.add_subplot(1, 1, 1, projection='3d')

​

xpos = np.arange(10)        

ypos = np.arange(10)        

zpos = np.zeros(10)

​

dx = np.ones(10)

dy = np.ones(10)                

dz = np.arange(10) + 1

​

​

ax.bar3d(xpos, ypos, zpos, dx, dy, dz)      

plt.show()

​

#10-6-5 繪製 3D 散佈圖 – scatter3D()

import numpy as np

import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

plt.rcParams['font.size'] = 16

fig = plt.figure(figsize=(12, 8))

ax = fig.add_subplot(1, 1, 1, projection='3d')

​

x = np.random.randn(1000)       

y = np.random.randn(1000)       

z = np.random.randn(1000)       

ax.scatter3D(x, y, z)

plt.show()

​





print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


