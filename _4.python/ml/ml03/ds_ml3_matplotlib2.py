"""

必學！Python 資料科學‧機器學習最強套件 matplotlib 2

"""

import sys
import matplotlib.pyplot as plt
import numpy as np
import math

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

import os
import sys
import time
import random

print('------------------------------------------------------------')	#60個

#10-1-1 設定資料點的樣式及色彩

days = np.arange(1, 11) 

weight = np.array([10, 14, 18, 20, 18, 16, 17, 18, 20, 17])

plt.ylim([0, weight.max()+1])   

plt.xlabel('days')

plt.ylabel('weight')

plt.plot(days, weight, marker='o', markerfacecolor='black') 

plt.show()

print('------------------------------------------------------------')	#60個

#10-1-2 設定折線的樣式、寬度及顏色

days = np.arange(1, 11)

weight = np.array([10, 14, 18, 20, 18, 16, 17, 18, 20, 17])

plt.ylim([0, weight.max()+1])

plt.xlabel('days')

plt.ylabel('weight')

plt.plot(days, weight, marker='o', markerfacecolor='red',
         linestyle='--', linewidth=2.5, color='green')  

plt.show()

print('------------------------------------------------------------')	#60個

#10-2-1 繪製長條圖 – bar()

x = [1, 2, 3, 4, 5, 6]          
y = [12, 41, 32, 36, 21, 17]    
plt.bar(x, y)
plt.show()

print('------------------------------------------------------------')	#60個

#10-2-2 設定長條圖橫軸標籤

x = [1, 2, 3, 4, 5, 6]
y = [12, 41, 32, 36, 21, 17]

labels = ['Apple', 'Orange', 'Banana', 'Pineapple', 'Kiwifruit', 'Strawberry']

plt.bar(x, y, tick_label=labels)

plt.show()

print('------------------------------------------------------------')	#60個​

#10-2-3 繪製堆疊長條圖

x = [1, 2, 3, 4, 5, 6]
y1 = [12, 41, 32, 36, 21, 17]
y2 = [43, 1, 6, 17, 17, 9]

labels = ['Apple', 'Orange', 'Banana', 'Pineapple', 'Kiwifruit', 'Strawberry']
plt.bar(x, y1, tick_label=labels)				#繪製 y1 長條圖
plt.bar(x, y2, tick_label=labels, bottom=y1)	#繪製 y2 長條圖

plt.legend(('y1', 'y2'))			#顯示圖例來識別 y1 與 y2
plt.show()

print('------------------------------------------------------------')	#60個

#10-3-1 繪製直方圖

np.random.seed(0)
data = np.random.randn(10000)
plt.hist(data, bins='auto')

plt.show()


np.random.seed(0)
data = np.random.randn(10000)
plt.hist(data, bins='auto', density=True)

plt.show()

print('------------------------------------------------------------')	#60個

#10-4-1 散佈圖的繪製語法 – scatter()

np.random.seed(0)
x = np.random.randn(100)    
y = np.random.randn(100)
plt.scatter(x, y)

plt.show()

print('------------------------------------------------------------')	#60個

#10-4-2 設定各資料點的樣式

np.random.seed(0)

x = np.random.randn(100)
y = np.random.randn(100)
plt.scatter(x, y, marker='^', color='black')    

plt.show()

print('------------------------------------------------------------')	#60個

#10-4-3 設定資料點的大小

np.random.seed(0)

x = np.random.randn(100)
y = np.random.randn(100)

size = np.random.choice(np.arange(100), 100)

plt.scatter(x, y, s=30)

plt.tight_layout()

plt.show()

print('------------------------------------------------------------')	#60個

#10-4-4 給散佈圖的點套上不同深淺顏色

np.random.seed(0)
x = np.random.randn(100)
y = np.random.randn(100)
c = np.random.choice(np.arange(100), 100)
plt.scatter(x, y, s=c, c=c, cmap='viridis')

plt.show()

print('------------------------------------------------------------')	#60個

#10-5-1 圓餅圖的繪製語法 – pie()

data = [60, 20, 10, 5, 3, 2]        
plt.pie(data)       
plt.show()

print('------------------------------------------------------------')	#60個

#10-5-2 給圓餅圖各區域設定標籤並顯示百分比

data = [60, 20, 10, 5, 3, 2]
labels = ['Apple', 'Orange', 'Banana', 'Pineapple', 'Kiwifruit', 'Strawberry']  
plt.pie(data, labels=labels,autopct="%.2f%%")   
plt.tight_layout()

plt.show()

print('------------------------------------------------------------')	#60個

#10-5-3 將圓餅圖的特定區塊向外推

data = [60, 20, 10, 5, 3, 2]
labels = ['Apple', 'Orange', 'Banana', 'Pineapple', 'Kiwifruit', 'Strawberry']
explode = [0, 0, 0.1, 0.2, 0, 0]    
plt.pie(data, labels=labels, explode=explode,autopct="%.2f%%")
plt.tight_layout()

plt.show()

print('------------------------------------------------------------')	#60個

#10-5-4 給圓餅圖加入立體陰影

data = [60, 20, 10, 5, 3, 2]
labels = ['Apple', 'Orange', 'Banana', 'Pineapple', 'Kiwifruit', 'Strawberry']
explode = [0, 0, 0.2, 0, 0, 0]      
plt.pie(data, labels=labels, explode=explode, shadow=True)  

plt.show()

print('------------------------------------------------------------')	#60個

#10-6-1 匯入 3D 套件並繪製子圖

from mpl_toolkits.mplot3d import Axes3D

t = np.linspace(-2 * np.pi, 2 * np.pi)      
x, y = np.meshgrid(t, t)                
z = np.sin(np.sqrt(x ** 2 + y ** 2))        
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')      #建立 3D 子圖畫布
ax.plot_surface(x, y, z)   #畫出三軸資料所構成的曲面
plt.tight_layout()

plt.show()

print('------------------------------------------------------------')	#60個

#10-6-2 繪製曲面 – plot_surface()

from mpl_toolkits.mplot3d import Axes3D

t = np.linspace(-5, 5, num=50)  
x, y = np.meshgrid(t, t)            
z = x * y                       
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')
ax.plot_surface(x, y, z)

plt.show()
print(z)

print('------------------------------------------------------------')	#60個

#10-6-3 給曲面套上顏色

from mpl_toolkits.mplot3d import Axes3D

t = np.linspace(-5, 5)

x, y = np.meshgrid(t, t)

z = x * y

fig = plt.figure()

ax = fig.add_subplot(1, 1, 1, projection='3d')

ax.plot_surface(x, y, z, cmap='viridis') 

plt.show()

print('------------------------------------------------------------')	#60個

#10-6-4 繪製 3D 長條圖

from mpl_toolkits.mplot3d import Axes3D

#plt.rcParams['font.size'] = 16

#fig = plt.figure(figsize=(12, 8))

fig = plt.figure()

ax = fig.add_subplot(1, 1, 1, projection='3d')

xpos = np.arange(10)        
ypos = np.arange(10)        
zpos = np.zeros(10)

dx = np.ones(10)
dy = np.ones(10)                
dz = np.arange(10) + 1

ax.bar3d(xpos, ypos, zpos, dx, dy, dz)      

plt.show()

print('------------------------------------------------------------')	#60個

#10-6-5 繪製 3D 散佈圖 – scatter3D()

from mpl_toolkits.mplot3d import Axes3D

plt.rcParams['font.size'] = 16

fig = plt.figure(figsize=(12, 8))

ax = fig.add_subplot(1, 1, 1, projection='3d')

x = np.random.randn(1000)       
y = np.random.randn(1000)       
z = np.random.randn(1000)       

ax.scatter3D(x, y, z)

plt.show()

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

