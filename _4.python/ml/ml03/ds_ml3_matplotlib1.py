"""

必學！Python 資料科學‧機器學習最強套件 matplotlib 1

"""

import os
import sys
import time
import random

print('------------------------------------------------------------')	#60個

#9-2-1 繪製折線圖

import numpy as np

import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi)   

y = np.sin(x)       

plt.plot(x, y)      

plt.show()      

print('------------------------------------------------------------')	#60個

#9-2-2 指定圖表的座標軸範圍 – xlim()、ylim()

import numpy as np

import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi)

y = np.sin(x)

plt.ylim(0, 1)

plt.plot(x, y)

plt.show()

print('------------------------------------------------------------')	#60個

#9-2-3 設定圖表標題與兩軸名稱–title()、xlabel()、ylabel()

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi)
y = np.sin(x)
plt.title('y = sin(x) (0<y<1)')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.ylim(0, 1)
plt.plot(x, y)
plt.show()

print('------------------------------------------------------------')	#60個

#9-2-4 在圖表上顯示網格 – grid()

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi)

y = np.sin(x)

plt.title('y = sin(x)')

plt.xlabel('X-axis')

plt.ylabel('Y-axis')

plt.grid(True)

plt.plot(x, y)

plt.show()

print('------------------------------------------------------------')	#60個

#9-2-5 自訂座標軸的刻度及標籤–xticks()、yticks()

import numpy as np

import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi)

y = np.sin(x)

plt.title('y = sin(x)')

plt.xlabel('X-axis')

plt.ylabel('Y-axis')

plt.grid(True)

ticks = [0, np.pi * 0.5, np.pi, np.pi * 1.5, np.pi * 2]

labels = ['0°', '90°', '180°', '270°', '360°']

plt.xticks(ticks, labels)
plt.plot(x, y)
plt.show()

print('------------------------------------------------------------')	#60個

#9-3-1 在同一張圖表繪製多筆資料並指定不同顏色

import numpy as np

import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi)   

y1 = np.sin(x)               

y2 = np.cos(x)               

plt.title('sin(x) and cos(x)')

plt.xlabel('X-axis')

plt.ylabel('Y-axis')

plt.grid(True)

ticks = [0, np.pi * 0.5, np.pi, np.pi * 1.5, np.pi * 2]

labels = ['0°', '90°', '180°', '270°', '360°']

plt.xticks(ticks, labels)

plt.plot(x, y1, color='orange')     

plt.plot(x, y2, color='purple')     

plt.show()


print('------------------------------------------------------------')	#60個

#9-3-2 設定圖例 – legend()

import numpy as np

import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi)

y1 = np.sin(x)

y2 = np.cos(x)

plt.title('sin(x) and cos(x)')

plt.xlabel('X-axis')

plt.ylabel('Y-axis')

plt.grid(True)

ticks = [0, np.pi * 0.5, np.pi, np.pi * 1.5, np.pi * 2]

labels = ['0°', '90°', '180°', '270°', '360°']

plt.xticks(ticks, labels)

plt.plot(x, y1, color='orange', label='y=sin(x)')   

plt.plot(x, y2, color='purple', label='y=cos(x)')   

plt.legend()        

plt.show()


import numpy as np

import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi)

y1 = np.sin(x)

y2 = np.cos(x)

plt.title('sin(x) and cos(x)')

plt.xlabel('X-axis')

plt.ylabel('Y-axis')

plt.grid(True)

ticks = [0, np.pi * 0.5, np.pi, np.pi * 1.5, np.pi * 2]

labels = ['0°', '90°', '180°', '270°', '360°']

plt.xticks(ticks, labels)

plt.plot(x, y1, color='orange')

plt.plot(x, y2, color='purple')

plt.legend([ 'y=sin(x)', 'y=cos(x)'])

plt.show()

print('------------------------------------------------------------')	#60個

#9-4-1 設定整張圖表的尺寸 – fgure()

import numpy as np

import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi)
y = np.sin(x)

plt.figure(figsize=(6, 8))
plt.plot(x, y)
plt.show()

print('------------------------------------------------------------')	#60個

#9-4-2 在畫布切出子圖區 , 並繪製內容–add_subplot()

import numpy as np

import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi)

y1 = np.sin(x)

y5 = np.cos(x)

y6 = np.tan(x)

fig = plt.figure(figsize=(8, 6))        #整個圖表大小為 8 x 6 英吋

ax1 = fig.add_subplot(2, 3, 1)      #←編號 1 的子圖

ax1.plot(x, y1)

ax5 = fig.add_subplot(2, 3, 5)      #←編號 5 的子圖

ax5.plot(x, y5)

ax6 = fig.add_subplot(2, 3, 6)      #←編號 6 的子圖

ax6.plot(x, y6)

ax3 = fig.add_subplot(2, 3, 3)      #← 編號 3 的子圖

plt.show()

print('------------------------------------------------------------')	#60個


#9-4-3 調整子圖間距

import numpy as np

import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi)

y1 = np.sin(x)

y5 = np.cos(x)

y6 = np.tan(x)

fig = plt.figure(figsize=(8, 6))

fig.subplots_adjust(wspace=0.5, hspace=0.75)

for i in range(6):
    ax = fig.add_subplot(2, 3, i + 1)
    if i == 0:  
        ax.plot(x, y1)
    elif i == 4:
        ax.plot(x, y5)
    elif i == 5:    
        ax.plot(x, y6)

plt.show()

print('------------------------------------------------------------')	#60個

#9-4-4 設定子圖的座標範圍、座標說明文字與子圖標題

import numpy as np

import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi)

y1 = np.sin(x)

y5 = np.cos(x)

y6 = np.tan(x)

fig = plt.figure(figsize=(8, 6))

fig.subplots_adjust(wspace=0.5, hspace=0.75)

for i in range(6):
    ax = fig.add_subplot(2, 3, i + 1)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xlabel('x-axis')
    ax.set_ylabel('y-axis')
    if i == 0:
        ax.set_title('y=sin(x)')
        ax.plot(x, y1)
    elif i == 4:
        ax.set_title('y=cos(x)')
        ax.plot(x, y5)
    elif i == 5:
        ax.set_title('y=tan(x)')
        ax.plot(x, y6)


plt.show()

print('------------------------------------------------------------')	#60個
