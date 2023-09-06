# plot 集合

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

#          編號                          圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(num = 'plot 集合 1 函數曲線', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

#第一張圖
plt.subplot(231)


#第二張圖
plt.subplot(232)

# 資料
x = [1, 2, 3, 4, 5, 6, 7]
y = [64.3, 63.8, 63.6, 64.0, 63.5, 63.2, 63.1]

# y = 3 * x - 24
y = []
for x in range(1, 11):
    y.append(3 * x - 24)
print(type(y))
print(y)

# 資料
x = np.arange(-1.0, 1.01, 0.01)

y = x ** 2

# 繪圖
plt.plot(x, y)        # 描繪折線
plt.grid(color='0.8') # 顯示格線


#第三張圖
plt.subplot(233)

print('畫出函數與導函數的圖')

import matplotlib.pyplot as plt
import numpy as np

# x的值
x = np.arange(-10, 10, 0.1)

# 原來的函數 f(x) = x**3 + 3x**2 + 3x + 1
y = x**3 + 3*x**2 + 3*x + 1
plt.plot(x, y)
plt.grid(color='0.8')

#第四張圖
plt.subplot(234)

# 導函數 f'(x) = 3x**2 + 6x + 3
y2 = 3*x**2 + 6*x + 3
plt.plot(x, y2)
plt.grid(color='0.8')

#第五張圖
plt.subplot(235)

print('畫出年收入圖')

import matplotlib.pyplot as plt
import pandas as pd

# 讀入csv檔
filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_csv/python_ReadWrite_CSV7_salary.csv'
dat = pd.read_csv(filename, encoding='UTF-8')

# 設定資料
x = dat['年齡']
y = dat['年收入']

# 繪圖
plt.plot(x, y)
plt.grid(color='0.8')

#第六張圖
plt.subplot(236)


print('描繪差額圖')
# 資料筆數
cnt = len(dat)

# 取差額
diff_y = []
for i in range(0, cnt-1):
    diff_y.append(y[i+1] - y[i])

# 繪圖
plt.plot(x[1:], diff_y)
plt.grid(color='0.8')



plt.show()

print('------------------------------------------------------------')	#60個

#          編號                          圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(num = 'plot 集合 2 函數曲線', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)


#第一張圖
plt.subplot(231)

print('描繪切線')

import matplotlib.pyplot as plt
import numpy as np

# x的值
x = np.arange(-1, 1, 0.1)

# 原來的函數
y = 2*x*x + 3

# 切線
a = 4*0.25            # 導函數 f'(x)= 4x（斜率）
b = 3.125 - a * 0.25  # 截距 b = y - ax
y2 = a*x + b          # 切線的式子

# 繪圖
plt.plot(x, y)   # 原來的函數
plt.plot(x, y2)  # 切線
plt.grid(color='0.8')


#第二張圖
plt.subplot(232)


#第三張圖
plt.subplot(233)

import matplotlib.pyplot as plt

Benz = [3367, 4120, 5539]               # Benz線條
BMW = [4000, 3590, 4423]                # BMW線條
Lexus = [5200, 4930, 5350]              # Lexus線條

seq = [2021, 2022, 2023]                # 年度
plt.xticks(seq)                         # 設定x軸刻度
plt.plot(seq, Benz, '-*', label='Benz')
plt.plot(seq, BMW, '-o', label='BMW')
plt.plot(seq, Lexus, '-^', label='Lexus')


plt.title("Sales Report", fontsize=24)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Number of Sales", fontsize=14)


seq = [2021, 2022, 2023]                # 年度
plt.xticks(seq)                         # 設定x軸刻度


#第四張圖
plt.subplot(234)


#第五張圖
plt.subplot(235)


import matplotlib.pyplot as plt

Benz = [3367, 4120, 5539]               # Benz線條
BMW = [4000, 3590, 4423]                # BMW線條
Lexus = [5200, 4930, 5350]              # Lexus線條

seq = [2021, 2022, 2023]                # 年度
plt.xticks(seq)                         # 設定x軸刻度
plt.plot(seq, Benz, '-*', label='Benz')
plt.plot(seq, BMW, '-o', label='BMW')
plt.plot(seq, Lexus, '-^', label='Lexus')
plt.legend(loc='best')
plt.title("Sales Report", fontsize=24)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Number of Sales", fontsize=14)

#後面要用
plt.savefig('out1_14.jpg', bbox_inches='tight')


#第六張圖
plt.subplot(236)


import matplotlib.pyplot as plt
import matplotlib.image as img

fig = img.imread('out1_14.jpg')
plt.imshow(fig)


plt.show()

print('------------------------------------------------------------')	#60個

