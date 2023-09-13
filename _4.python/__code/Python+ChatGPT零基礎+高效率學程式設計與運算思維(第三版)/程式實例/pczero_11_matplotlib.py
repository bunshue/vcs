'''
matplotlib_new



'''

import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib

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

import matplotlib.pyplot as plt

print('------------------------------------------------------------')	#60個

'''
#plt.plot(seq,data1,'g--',seq,data2,'r-.',seq,data3,'y:',seq,data4,'k.')   
#plt.plot(seq,data1,'-*',seq,data2,'-o',seq,data3,'-^',seq,data4,'-s')   
#plt.plot(seq, Benz, '-*', seq, BMW, '-o', seq, Lexus, '-^')   

seq = [2021, 2022, 2023]                # 年度
plt.xticks(seq)

plt.plot(seq, Benz, '-*', seq, BMW, '-o', seq, Lexus, '-^')   

seq = [2021, 2022, 2023]                # 年度
plt.xticks(seq)                         # 設定x軸刻度

plt.plot(seq, Benz, '-*', label='Benz')
plt.plot(seq, BMW, '-o', label='BMW')
plt.plot(seq, Lexus, '-^', label='Lexus')
plt.legend(loc='best')

seq = [2021, 2022, 2023]                # 年度
plt.xticks(seq)                         # 設定x軸刻度

plt.plot(seq, Benz, '-*', label='Benz')
plt.plot(seq, BMW, '-o', label='BMW')
plt.plot(seq, Lexus, '-^', label='Lexus')
plt.legend(loc='best')

plt.savefig('out20_12.jpg')

import matplotlib.pyplot as plt
import matplotlib.image as img

fig = img.imread('out20_12.jpg')
plt.imshow(fig)
plt.show()



plt.title(r'衰減數列 cos($3\pi x * e^{x})$',fontsize=20)
plt.plot(x, y, 'go-')


import matplotlib.pyplot as plt

plt.title(r'$\frac{7}{9}+\sqrt{7}+\alpha\beta$',fontsize=20)


plt.plot(1,0,'bo')                  # 輸出藍點
plt.text(1,0,'sin(x)',fontsize=20)  # 輸出公式
plt.plot(x,y)


plt.plot(x1, y1, 'go-')
plt.plot(x2, y2, 'm.-')

plt.plot(seq, data1, '-*')
plt.plot(seq, data2, 'm-o')                      


plt.subplot(2,2,1)  #四格佔1格
plt.subplot(2,2,2)  #四格佔1格
plt.subplot(2,1,2)  #二格佔1格 = 四格佔2格


'''

'''
print('------------------------------------------------------------')	#60個

print('subplot的另一種寫法')
import matplotlib.pyplot as plt 
import numpy as np

fig, ax = plt.subplots(2, 2)            # 建立4個子圖
x = np.linspace(0, 2*np.pi, 300)
y = np.sin(x**2)
ax[0, 0].plot(x, y,'b')                 # 子圖索引 0,0
ax[0, 0].set_title('子圖[0, 0]')
ax[0, 1].plot(x, y,'g')                 # 子圖索引 0,1
ax[0, 1].set_title('子圖[0, 1]')
ax[1, 0].plot(x, y,'m')                 # 子圖索引 1,0
ax[1, 0].set_title('子圖[1, 0]')
ax[1, 1].plot(x, y,'r')                 # 子圖索引 1,1
ax[1, 1].set_title('子圖[1, 1]') 
fig.suptitle("4個子圖的實作",fontsize=16) # 圖表主標題
plt.tight_layout()                      # 緊縮佈局

plt.show()

print('------------------------------------------------------------')	#60個

print('subplot的另一種寫法')
import matplotlib.pyplot as plt 
import numpy as np

# 繪製半徑 5 的圓
angle = np.linspace(0, 2*np.pi, 100)
fig, ax = plt.subplots(2, 2)    # 建立 2 x 2 子圖

ax[0, 0].plot(5 * np.cos(angle), 5 * np.sin(angle))
ax[0, 0].set_title('繪圓形, 看起來像橢圓')
ax[0, 1].plot(5 * np.cos(angle), 5 * np.sin(angle))
ax[0, 1].axis('equal')
ax[0, 1].set_title('寬高比相同, 是圓形')
ax[1, 0].plot(5 * np.cos(angle), 5 * np.sin(angle))
ax[1, 0].axis('equal')
ax[1, 0].set(xlim=(-5, 5), ylim=(-5, 5))
ax[1, 0].set_title('設定寬和高相同區間')
ax[1, 1].plot(5 * np.cos(angle), 5 * np.sin(angle))
ax[1, 1].set_aspect(2)
ax[1, 1].set_title('設定寬高比是2')
fig.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

print('subplot的另一種寫法')
import matplotlib.pyplot as plt 
import numpy as np

# 繪製半徑 5 的圓
angle = np.linspace(0, 2*np.pi, 100)
fig, ax = plt.subplots(2, 2)    # 建立 2 x 2 子圖

ax[0, 0].plot(5 * np.cos(angle), 5 * np.sin(angle))
ax[0, 0].set_title('繪圓形, 看起來像橢圓')
ax[0, 1].plot(5 * np.cos(angle), 5 * np.sin(angle))
ax[0, 1].axis('equal')
ax[0, 1].set_title('寬高比相同, 是圓形')
ax[1, 0].plot(5 * np.cos(angle), 5 * np.sin(angle))
ax[1, 0].axis('equal')
ax[1, 0].set(xlim=(-5, 5), ylim=(-5, 5))
ax[1, 0].set_title('設定寬和高相同區間')
ax[1, 1].plot(5 * np.cos(angle), 5 * np.sin(angle))
ax[1, 1].set_aspect('equal', 'box')
ax[1, 1].set_title('設定寬高比相同')
fig.tight_layout()

plt.show()
'''

print('------------------------------------------------------------')	#60個

'''
#h = plt.hist(dice,sides,rwidth=0.8)     # 繪製hist圖
h = plt.hist(dice,sides,rwidth=0.5,cumulative=True) # 繪製hist圖


'''

print('------------------------------------------------------------')	#60個

import matplotlib.pyplot as plt 

area = ['大陸','東南亞','東北亞','美國','歐洲','澳紐']
people = [10000,12600,9600,7500,5100,4800]

#case 1
plt.pie(people,labels=area)

#case 2
plt.pie(people,labels=area,autopct="%1.2f%%")

#case 3, 突出一塊
exp = [0.0,0.0,0.0,0.0,0.0,0.1]
plt.pie(people,labels=area,explode=exp,autopct="%1.2f%%")

plt.title('五月份國外旅遊調查表',fontsize=16,color='b')

plt.show()

print('------------------------------------------------------------')	#60個

import matplotlib.pyplot as plt  
import numpy as np  
from matplotlib.animation import FuncAnimation  

# 建立最初化的 line 資料 (x, y)  
def init():  
    line.set_data([], [])  
    return line,
# 繪製 sin 波形, 這個函數將被重複調用
def animate(i):        
    #x = np.linspace(0, 2*np.pi, 500)        # 建立 sin 的 x 值, 點數多
    x = np.linspace(0, 2*np.pi, 10)         # 建立 sin 的 x 值, 點數少
    y = np.sin(2 * np.pi * (x - 0.01 * i))  # 建立 sin 的 y 值  
    line.set_data(x, y)                     # 更新波形的資料
    return line,

# 建立動畫需要的 Figure 物件
fig = plt.figure()   
# 建立軸物件與設定大小
ax = plt.axes(xlim=(0, 2*np.pi), ylim=(-2, 2))    
# 最初化線條 line, 變數, 須留意變數 line 右邊的逗號','是必須的  
line, = ax.plot([], [], lw=3, color='g')  
# interval = 20, 相當於每隔 20 毫秒執行 animate()動畫  
ani = FuncAnimation(fig, animate,
                    frames = 200,          
                    init_func = init,                        
                    interval = 20)          # interval是控制速度
ani.save('sin.gif', writer='pillow')        # 儲存 sin.gif 檔案

plt.show()

print('------------------------------------------------------------')	#60個

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 建立最初化點的位置 
def init():
    dot.set_data(x[0], y[0])        # 更新紅色點的資料
    return dot,
# 繪製 sin 波形, 這個函數將被重複調用
def animate(i):    
    dot.set_data(x[i], y[i])        # 更新紅色點的資料
    return dot,

# 建立動畫需要的 Figure 物件
fig = plt.figure()
N = 200
# 建立軸物件與設定大小
ax = plt.axes(xlim=(0, 2*np.pi), ylim=(-1.5, 1.5))
# 建立和繪製 sin 波形
x = np.linspace(0, 2*np.pi, N)
y = np.sin(x)
line, = ax.plot(x, y, color='g',linestyle='-',linewidth=3)
# 建立和繪製紅點
dot, = ax.plot([],[],color='red',marker='o',
               markersize=15,linestyle='')
# interval = 20, 相當於每隔 20 毫秒執行 animate()動畫
ani = FuncAnimation(fig=fig, func=animate,
                    frames=N,
                    init_func=init,
                    interval=20,
                    blit=True,
                    repeat=True)
ani.save('sinball.gif', writer='pillow')   # 儲存 sinball.gif 檔案

plt.show()

print('------------------------------------------------------------')	#60個

import matplotlib.pyplot as plt 
import numpy as np

x = np.linspace(0.0, np.pi, 500)
y = np.cos(2 * np.pi * x)
plt.plot(x, y, 'm', lw=2)
plt.annotate('局部極大值',
            xy=(2, 1),
            xytext=(2.5, 1.2),           
            arrowprops=dict(arrowstyle='->',
                            facecolor='black'))
plt.annotate('局部極小值',
            xy=(1.5, -1),
            xytext=(2.0, -1.25),           
            arrowprops=dict(arrowstyle='-'))
plt.text(0.8,1.2,'Annotate的應用',fontsize=20,color='b')
plt.ylim(-1.5, 1.5)

plt.show()

print('------------------------------------------------------------')	#60個

