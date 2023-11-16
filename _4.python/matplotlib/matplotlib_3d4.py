
# 3D plot 集合

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'

import matplotlib.pyplot as plt
import numpy as np

#          編號                          圖像大小             解析度    背景色                      邊框顏色                      邊框有無
#fig = plt.figure(num = '3D繪圖 集合 2', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

"""

#XXXXXXX1
ax = fig.add_subplot(231, projection='3d')  #第一張圖


ax.set_title('XXXXXXX1')



#XXXXXXX2
ax = fig.add_subplot(232, projection='3d')  #第二張圖




#XXXXXXX3
ax = fig.add_subplot(233, projection='3d')  #第三張圖

ax.set_title('XXXXXXX3')

#XXXXXXX4
ax = fig.add_subplot(234, projection='3d')  #第四張圖

#
#
#
ax.set_title('XXXXXXX4')

#XXXXXXX5
ax = fig.add_subplot(235, projection='3d')  #第五張圖

#
#
#
ax.set_title('XXXXXXX5')

#XXXXXXX6
ax = fig.add_subplot(236, projection='3d')  #第六張圖

#
#
#
ax.set_title('XXXXXXX6')


plt.show()

"""


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


