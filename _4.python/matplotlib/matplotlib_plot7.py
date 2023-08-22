# plot 集合

'''
有 numpy 的 matplotlib

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

#          編號                          圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(num = 'plot 集合 1 函數曲線', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

#第一張圖
plt.subplot(231)

x = np.linspace(0, 10, 50)
sinus = np.sin(x)
cosinus = np.cos(x)
plt.plot(x, sinus, x, cosinus)

#plt.plot(x, sinus, "r-o", x, cosinus, "g--")

#plt.plot(x, sinus, "r-o", label="sin(x)")
#plt.plot(x, cosinus, "g--", label="cos(x)")
#plt.plot(x, sinus, "r-o")
#plt.plot(x, cosinus, "g--")
#plt.plot(x, np.sin(x), "r-o")
#plt.plot(x, np.cos(x), "g--")

#plt.legend(loc=1)

#plt.plot(x, np.sin(x))
#plt.plot(x, np.cos(x))
#plt.plot(x, np.tan(x))
#plt.plot(x, np.sinh(x))
#plt.plot(x, np.cosh(x))
#plt.plot(x, np.tanh(x))


#第二張圖
plt.subplot(232)

plt.plot(np.random.randn(100))


#第三張圖
plt.subplot(233)

print('繪製移動平均圖')

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_csv/vcs_ReadWrite_CSV_temperature.csv'

# 讀入氣溫資料
dat= pd.read_csv(filename, encoding='UTF-8')

n = len(dat)       # 資料筆數
x = range(1, n+1)  #  x軸的值（1～資料筆數）

# 氣溫
y = dat['平均氣溫']  # y軸的值（平均氣溫）
plt.plot(x, y)       # 繪圖

# 區間大小:9 的移動平均
v = np.ones(9)/9.0
y2 = np.convolve(y, v, mode='same')  # 計算移動平均
plt.plot(x[4:n-4], y2[4:n-4])        # 繪圖






#第四張圖
plt.subplot(234)




#描點畫圓
# 角度
th = np.arange(0, 360)

# 圓周上的點P座標 
x = np.cos(np.radians(th))
y = np.sin(np.radians(th))

# 繪圖
plt.plot(x, y)
plt.axis('equal')       #軸比例



#第五張圖
plt.subplot(235)

#繪製半徑300的圓（y >= 0）

# 圓的方程式
r = 300  # 半徑
x = np.arange(-r, r + 1)    # x: -300～300
y = np.sqrt(r ** 2 - x ** 2)  # y

# 繪圖
plt.plot(x, y)
plt.axis('equal')       #軸比例



#第六張圖
plt.subplot(236)


import matplotlib.pyplot as plt
import numpy as np

xpt = np.linspace(0, 10, 500)           # 建立含500個元素的陣列
ypt1 = np.sin(xpt)                      # y陣列的變化
ypt2 = np.cos(xpt)

plt.plot(xpt, ypt1, label='sin')        # 預設顏色
plt.plot(xpt, ypt2, label='cos')        # 預設顏色
plt.xlabel('rad')
plt.ylabel('value')
plt.title('Sin and Cos function')
plt.grid()
plt.legend(loc='best')




plt.show()


print('------------------------------------------------------------')	#60個

#          編號                          圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(num = 'plot 集合 2 函數曲線', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)


#第一張圖
plt.subplot(231)


pi = 3.14159
r = 3
t = np.linspace(-1 * pi, 1 * pi, 50)

x = r * np.cos(t)
y = r * np.sin(t)


r = 3 * (1 - np.sin(t))
x = r * np.cos(t)
y = r * np.sin(t)

plt.plot(x, y, lw=3)




#第二張圖
plt.subplot(232)


x = np.linspace(-5, 5, 200)
siny = np.sin(x)

y = siny + np.random.rand(1, len(siny)) * 1.5 #加入雜訊的點集
y = y.tolist()[0]

plt.plot(x, siny, c = 'r', label = 'sin(x)', linewidth = 1)
plt.plot(x, y, c = 'g', label = 'sin(x)', linewidth = 1)

plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('')
plt.legend()




#第三張圖
plt.subplot(233)



#第四張圖
plt.subplot(234)




#第五張圖
plt.subplot(235)


#第六張圖
plt.subplot(236)



plt.show()

print('------------------------------------------------------------')	#60個

#          編號                          圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(num = 'plot 集合 3 函數曲線', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

#第一張圖
plt.subplot(231)



#第二張圖
plt.subplot(232)



#第三張圖
plt.subplot(233)


#第四張圖
plt.subplot(234)


#第五張圖
plt.subplot(235)



#第六張圖
plt.subplot(236)



plt.show()

