# 新進測試04

import os
import sys
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


#檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python2\matplotlib\m01.py

# python 3+ 請複製以下在 terminal 中執行
# pip3 install matplotlib

# python 2+ 請複製以下在 terminal 中執行
# pip install matplotlib

import numpy as np
from matplotlib import pyplot as plt 
 
x = np.arange(1,11, dtype=int) 
y =  2 * x
plt.title("demo") 
plt.xlabel("x") 
plt.ylabel("y") 
plt.plot(x,y) 
plt.show()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python2\matplotlib\m02.py

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties as font

# 連結中文字體，範例為微軟正黑體
zhfont1 = font(fname = font_filename)

x = np.arange(1, 10, dtype=int)
y = x * 0.2
a = np.arange(1, 10, 0.1)
b = np.sin(a)
plt.title("哈囉", fontproperties=zhfont1)
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x, y, 'or')  # 第三個為參數，o 表示原點，r 表示紅色
plt.plot(a, b, ':b')  # 第三個為參數，o 表示原點，r 表示紅色
plt.show()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python2\matplotlib\m03.py

import numpy as np
from matplotlib import pyplot as plt

ax = np.linspace(1,100,20)
bx = np.linspace(1,20,200)

ay = ax
by = np.sin(bx)

# 產生子圖表，第一個數值為縱軸要有幾張圖，第二個數值為橫軸，第三個數值為排在哪裡
plt.subplot(2,  1,  1) 
plt.plot(ax, ay) 
plt.title('a') 
plt.xlabel("ax")
plt.ylabel("ay") 


plt.subplot(2,  1,  2) 
plt.plot(bx, by) 
plt.title('b') 
plt.xlabel("bx")
plt.ylabel("by") 

plt.show()



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python2\matplotlib\m04.py

import numpy as np
from matplotlib import pyplot as plt

ax = np.linspace(0, 20, 100)
ay = ax*0.5
by = np.sin(ax)

# 產生子圖表，第一個數值為縱軸要有幾張圖，第二個數值為橫軸，第三個數值為排在哪裡
# label 可以設定圖例標籤
#  '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'
plt.plot(ax, ay, color='red', linewidth=8.0, linestyle='dotted', label='x0.5')
plt.plot(ax, by, color='blue', linewidth=2.0, linestyle='-', label='sin')
plt.title('demo')
# 設定圖例標籤位置 ( best, upper, lower, right,left,center )
plt.legend(loc='lower center')
plt.xlabel("ax")
plt.ylabel("ay")
plt.ylim((-5, 10))  # y 軸上下最大和最小區間
plt.xlim((0, 20))  # y 軸上下最大和最小區間
plt.yticks([-5, 0, 10], ['min(-5)', '0', 'max(10)'])  # 可以設置座標軸上特定文字

xx = plt.gca()
xx.spines['right'].set_color('none')  # 設置邊框樣式
xx.spines['top'].set_color('none')
xx.spines['bottom'].set_position(('data', 0))  # 設置邊框位置

plt.show()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python2\matplotlib\m05.py

import numpy as np
from matplotlib import pyplot as plt

ax = np.linspace(-20, 20, 100)
ay = ax*0.5
by = np.sin(ax)
cx = 10
cy = cx*0.5

plt.plot(ax, ay, color='red', linewidth=3.0, linestyle='dashed', label='x0.5', zorder=2)
plt.plot(ax, by, color='blue', linewidth=2.0, linestyle='solid', label='sin', zorder=2)
# 繪製垂直虛線
plt.plot([cx, cx,],[cy, 0,], color='black', linewidth=1.0, linestyle='dashed', zorder=1, alpha=0.5)

# 加上單一圓點
# https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.scatter.html
plt.scatter(cx, cy, s=100, color='red', zorder=2)

# 繪製 annotate
# https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.annotate.html
plt.annotate('test', xy=(cx+0.5, cy-0.2), xycoords='data', xytext=(+36, -36),
             textcoords='offset points', fontsize=12,
             arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))


plt.legend(loc='best')

plt.ylim((-10, 10))  # 設定 x 和 y 的邊界值
plt.xlim((-20, 20))

xx = plt.gca()  # 設定座標軸位置
xx.spines['right'].set_color('none')
xx.spines['top'].set_color('none')
xx.spines['bottom'].set_position(('data', 0))
xx.spines['left'].set_position(('data', 0))



plt.show()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python2\matplotlib\m06.py

import numpy as np
from matplotlib import pyplot as plt

n = 100
ax = np.random.normal(0,1,n)
ay = np.random.normal(0,1,n)
bx = np.random.normal(0,1,n)
by = np.random.normal(0,1,n)

plt.scatter(ax, ay, alpha=0.5, s=100, color='red')
plt.scatter(bx, by, alpha=0.5, s=100, color='blue')
plt.xlim = (0 , 1)
plt.ylim = (0 , 1)

plt.show()




print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個






print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



