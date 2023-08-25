import sys

import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0, 10, num=11)     # 使用linspace()產生陣列
print(type(x1), x1)
x2 = np.arange(0,11,1)              # 使用arange()產生陣列
print(type(x2), x2)
x3 = np.arange(11)                  # 簡化語法產生陣列
print(type(x3), x3)

print('------------------------------------------------------------')	#60個

#scatter 顏色
#plt.scatter(xpt, ypt1, color=(0, 1, 0)) # 綠色
#plt.scatter(xpt, ypt2)                  # 預設顏色

print('------------------------------------------------------------')	#60個

xpt = np.linspace(0, 5, 25)                        # 建立含500個元素的陣列
ypt = 1 - 0.5*np.abs(xpt-2)                         # y陣列的變化
lwidths = (1+xpt)**2                                # 寬度陣列  
#plt.scatter(xpt, ypt, s=lwidths, color=(0, 1, 0))   # 綠色
#plt.show()

print('------------------------------------------------------------')	#60個
#使用 fill_between

left = -np.pi
right = np.pi
x = np.linspace(left, right, 100)
y = np.sin(3*x)                  # y陣列的變化

plt.plot(x, y) 
plt.fill_between(x, 0, y, color='green', alpha=0.1)
plt.show()

print('------------------------------------------------------------')	#60個
#使用 fill_between

left = -np.pi
right = np.pi
x = np.linspace(left, right, 100)
y = np.sin(3*x)                  # y陣列的變化

plt.plot(x, y) 
plt.fill_between(x, -1, y, color='yellow', alpha=0.3)
plt.show()

print('------------------------------------------------------------')	#60個

plt.rcParams["font.family"] = ["Microsoft JhengHei"]    # 微軟正黑體

pts = np.arange(-2, 2, 0.01)
x, y = np.meshgrid(pts, pts)
z = np.sqrt(x**2 + y**2)

ticks = np.arange(0, 500, 100)
seq = np.arange(-2, 3)

plt.imshow(z, cmap='rainbow')
plt.xticks(ticks, seq)
plt.yticks(ticks, seq)

plt.colorbar()
plt.title(r"建立$\sqrt{x^2 + y^2}$網格影像")
plt.show()

print('------------------------------------------------------------')	#60個

plt.rcParams["font.family"] = ["Microsoft JhengHei"]    # 微軟正黑體
plt.title('Latex使用')
plt.text(0.4, 0.6,r"$\int_0^5 f(x)\mathrm{d}x$",fontsize=20,color="blue")
plt.text(0.4, 0.3,r"$\sum_{n=1}^\infty\frac{-e^{2\pi}}{3^n}!$",fontsize=20)
plt.show()

print('------------------------------------------------------------')	#60個

from skimage import data

img = data.astronaut()              
plt.imshow(img)
plt.show()



print('------------------------------------------------------------')	#60個

plt.rcParams["font.family"] = ["Microsoft JhengHei"]    # 微軟正黑體

Benz = [3367, 4120, 5539]               # Benz線條
BMW = [4000, 3590, 4423]                # BMW線條
Lexus = [5200, 4930, 5350]              # Lexus線條

seq = [2021, 2022, 2023]                # 年度
plt.xticks(seq)                         # 設定x軸刻度
plt.plot(seq, Benz, '-*', label='Benz')
plt.plot(seq, BMW, '-o', label='BMW')
plt.plot(seq, Lexus, '-^', label='Lexus')
plt.legend(loc='best')
plt.title("銷售報表", fontsize=24)
plt.xlabel("年度", fontsize=14)
plt.ylabel("銷售量", fontsize=14)
plt.tick_params(axis='both', labelsize=12, color='red')
plt.show()



print('------------------------------------------------------------')	#60個

plt.rcParams["font.family"] = ["Microsoft JhengHei"]    # 微軟正黑體

votes = [135, 412, 397]         # 得票數
N = len(votes)                  # 計算長度
x = np.arange(N)                # 長條圖x軸座標
width = 0.35                    # 長條圖寬度
plt.bar(x, votes, width)        # 繪製長條圖

plt.ylabel('票數')
plt.title('選舉結果')
plt.xticks(x, ('James', 'Peter', 'Norton'))
plt.yticks(np.arange(0, 450, 30))
plt.show()



print('------------------------------------------------------------')	#60個

from random import randint

plt.rcParams["font.family"] = ["Microsoft JhengHei"]    # 微軟正黑體

def dice_generator(times, sides):
    ''' 處理隨機數 '''
    for i in range(times):              
        ranNum = randint(1, sides)              # 產生1-6隨機數
        dice.append(ranNum)
          
times = 10000                                   # 擲骰子次數
sides = 6                                       # 骰子有幾面
dice = []                                       # 建立擲骰子的串列
dice_generator(times, sides)                    # 產生擲骰子的串列

h = plt.hist(dice, sides)                       # 繪製hist圖
print("bins的y軸 ",h[0])
print("bins的x軸 ",h[1])
plt.ylabel('頻率')
plt.title('測試 10000 次')
plt.show()

print('------------------------------------------------------------')	#60個

from sympy import Symbol, solve
                                
a = Symbol('a')                 # 定義公式中使用的變數
b = Symbol('b')                 # 定義公式中使用的變數
eq1 = a + b - 1                 # 方程式 1
eq2 = 5 * a + b - 2             # 方程式 2
ans = solve((eq1, eq2))
print(type(ans))
print(ans)
print('a = {}'.format(ans[a]))
print('b = {}'.format(ans[b]))

print('------------------------------------------------------------')	#60個

import matplotlib.pyplot as plt
from sympy import Symbol, solve
import numpy as np
                                
a = Symbol('a')                 # 定義公式中使用的變數
b = Symbol('b')                 # 定義公式中使用的變數
eq1 = a + b - 1                 # 方程式 1
eq2 = 5 * a + b - 2             # 方程式 2
ans = solve((eq1, eq2))
print('a = {}'.format(ans[a]))
print('b = {}'.format(ans[b]))

pt_x1 = 600                             
pt_y1 = ans[a] * pt_x1 + ans[b]         # 計算x=600時的y值
pt_x2 = 1000
pt_y2 = ans[a] * pt_x2 + ans[b]         # 計算x=1000時的y值

x = np.linspace(0, 2500, 250)
y = ans[a] * x + ans[b]
plt.plot(x, y)                          # 繪函數直線
plt.plot(pt_x1, pt_y1, '-o')            # 繪點 pt1
plt.text(pt_x1+60, pt_y1-10, 'pt1')      # 輸出文字pt1
plt.plot(pt_x2, pt_y2, '-o')            # 繪點 pt2
plt.text(pt_x2+60, pt_y2-10, 'pt2')      # 輸出文字pt2
plt.xlabel("Customers")
plt.ylabel("Profit")
plt.grid()                              # 加格線
plt.show()







print('------------------------------------------------------------')	#60個

import matplotlib.pyplot as plt
import numpy as np

a = 0.03
b = -18
x = np.linspace(0, 2500, 250)
y = a * x + b
pt_x = 1500
pt_y = a * pt_x + b
print('f(1500) = {}'.format(pt_y))
plt.plot(x, y)                          # 繪函數直線
plt.plot(pt_x, pt_y, '-o')              # 繪點 f(1500)
plt.text(pt_x-150, pt_y+3, 'f(1500)')   # 輸出文字f(1500)
plt.xlabel("Customers")
plt.ylabel("Profit")
plt.grid()                              # 加格線
plt.show()

print('------------------------------------------------------------')	#60個

import matplotlib.pyplot as plt
import numpy as np

a = 0.03
b = -18
x = np.linspace(0, 2500, 250)
y = a * x + b
pt_y = 48
pt_x = (pt_y + 18) / 0.03 
print('獲利48萬需有 {} 來客數'.format(int(pt_x)))
plt.plot(x, y)                                      # 繪函數直線
plt.plot(pt_x, pt_y, '-o')                          # 繪點
plt.text(pt_x-150, pt_y+3, '('+str(int(pt_x))+','+str(pt_y)+')')   
plt.xlabel("Customers")
plt.ylabel("Profit")
plt.grid()                                          # 加格線
plt.show()

print('------------------------------------------------------------')	#60個

import matplotlib.pyplot as plt
from sympy import Symbol, solve
import numpy as np
                                
x = Symbol('x')                         # 定義公式中使用的變數
y = Symbol('y')                         # 定義公式中使用的變數
eq1 = x + y - 35                        # 方程式 1
eq2 = 2 * x + 4 * y - 100               # 方程式 2
ans = solve((eq1, eq2))
print('雞 = {}'.format(ans[x]))
print('兔 = {}'.format(ans[y]))

line1_x = np.linspace(0, 100, 100)
line1_y = [35 - y for y in line1_x]
line2_x = np.linspace(0, 100, 100)
line2_y = [25 - 0.5 * y for y in line2_x]

plt.plot(line1_x, line1_y)              # 繪函數直線公式 1
plt.plot(line2_x, line2_y)              # 繪函數直線公式 2

plt.plot(ans[x], ans[y], '-o')          # 繪交叉點
plt.text(ans[x]-5, ans[y]+5, '('+str(ans[x])+','+str(ans[y])+')')
plt.xlabel("Chicken")
plt.ylabel("Rabbit")
plt.grid()                              # 加格線
plt.show()







print('------------------------------------------------------------')	#60個

import matplotlib.pyplot as plt
from sympy import Symbol, solve
import numpy as np
                                
x = Symbol('x')                         # 定義公式中使用的變數
y = Symbol('y')                         # 定義公式中使用的變數
eq1 = x + y - 100                       # 方程式 1
eq2 = 2 * x + 4 * y - 350               # 方程式 2
ans = solve((eq1, eq2))
print('菜鳥業務員須外出天數 = {}'.format(ans[x]))
print('資深業務員須外出天數 = {}'.format(ans[y]))

line1_x = np.linspace(0, 100, 100)
line1_y = [100 - y for y in line1_x]
line2_x = np.linspace(0, 100, 100)
line2_y = [(350 - 2 * y) / 4 for y in line2_x]

plt.plot(line1_x, line1_y)              # 繪函數直線公式 1
plt.plot(line2_x, line2_y)              # 繪函數直線公式 2

plt.plot(ans[x], ans[y], '-o')          # 繪交叉點
plt.text(ans[x]-5, ans[y]+5, '('+str(ans[x])+','+str(ans[y])+')')
plt.xlabel("Junior Salesman")
plt.ylabel("Senior Salesman")
plt.grid()                              # 加格線
plt.show()

print('------------------------------------------------------------')	#60個

import matplotlib.pyplot as plt
from sympy import Symbol, solve
import numpy as np

x = Symbol('x')                         # 定義公式中使用的變數
y = Symbol('y')                         # 定義公式中使用的變數
eq1 = x - y                             # 方程式 1
eq2 = -x -y + 2                         # 方程式 2
ans = solve((eq1, eq2))
print('x = {}'.format(ans[x]))
print('y = {}'.format(ans[y]))


line1_x = np.linspace(-5, 5, 10)
line1_y = [y for y in line1_x]
line2_x = np.linspace(-5, 5, 10)
line2_y = [-y + 2 for y in line2_x]

plt.plot(line1_x, line1_y)              # 繪函數直線公式 1
plt.plot(line2_x, line2_y)              # 繪函數直線公式 2

plt.plot(ans[x], ans[y], '-o')          # 繪交叉點
plt.text(ans[x]-0.5, ans[y]+0.3, '('+str(ans[x])+','+str(ans[y])+')')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()                              # 加格線
plt.axis('equal')                       # 讓x, y軸距長度一致
plt.show()

print('------------------------------------------------------------')	#60個

import matplotlib.pyplot as plt
from sympy import Symbol, solve
import numpy as np

x = Symbol('x')                         # 定義公式中使用的變數
y = Symbol('y')                         # 定義公式中使用的變數
eq1 = 0.5 * x - y - 0.5                 # 方程式 1
eq2 = -2 * x - y + 7                    # 方程式 2
ans = solve((eq1, eq2))
print('x = {}'.format(ans[x]))
print('y = {}'.format(ans[y]))


line1_x = np.linspace(-5, 5, 10)
line1_y = [(0.5 * y - 0.5) for y in line1_x]
line2_x = np.linspace(-5, 5, 10)
line2_y = [(-2 * y + 7) for y in line2_x]

plt.plot(line1_x, line1_y)              # 繪函數直線公式 1
plt.plot(line2_x, line2_y)              # 繪函數直線公式 2

plt.plot(ans[x], ans[y], '-o')          # 繪交叉點
plt.text(ans[x]-0.7, ans[y]+0.5, '('+str(int(ans[x]))+','+str(int(ans[y]))+')')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()                              # 加格線
plt.axis('equal')                       # 讓x, y軸距長度一致
plt.show()

print('------------------------------------------------------------')	#60個

import matplotlib.pyplot as plt
from sympy import Symbol, solve
import numpy as np
                                
x = Symbol('x')                         # 定義公式中使用的變數
y = Symbol('y')                         # 定義公式中使用的變數
eq1 = 8 - 0.6 * x - y                   # 方程式 1
eq2 = 17.5 - 2.5 * x - y                # 方程式 2
ans = solve((eq1, eq2))
print('x = {}'.format(int(ans[x])))
print('y = {}'.format(int(ans[y])))

z = 50 * int(ans[x]) + 50 * int(ans[y])
print('最大獲利 = {} 萬'.format(z))

print('------------------------------------------------------------')	#60個

import matplotlib.pyplot as plt
import numpy as np

plt.plot([0, 0], [20, 0])              # 繪函數直線公式 1
plt.plot([0, 0], [0, 20])              # 繪函數直線公式 2
                                
line3_x = np.linspace(0, 20, 20)
line3_y = [(8 - 0.6 * y) for y in line3_x]

line4_x = np.linspace(0, 20, 20)
line4_y = [(17.5 - 2.5 * y) for y in line4_x]

lineobj_x = np.linspace(0, 20, 20)
lineobj_y = [10 - y for y in lineobj_x]

plt.axis([0, 20, 0, 20])

plt.plot(line3_x, line3_y)              # 繪函數直線公式 3
plt.plot(line4_x, line4_y)              # 繪函數直線公式 4
plt.plot(lineobj_x, lineobj_y)          # 繪目標函數直線公式

plt.plot(5, 5, '-o')                    # 繪交叉點
plt.text(4.5, 5.5, '(5, 5)')            # 輸出(5, 5)
plt.xlabel("Research")
plt.ylabel("UI")
plt.grid()                              # 加格線
plt.show()









print('------------------------------------------------------------')	#60個






print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個

