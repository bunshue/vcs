# plot 集合

selected_font = 'C:/_git/vcs/_4.cmpp/_python_test/data/msch.ttf'

import matplotlib.pyplot as plt
import numpy as np

#plt.figure(figsize=(8,8))	#設定圖片視窗大小
plt.figure(figsize=[12, 10], dpi=84, facecolor="whitesmoke", edgecolor="r", linewidth=1, frameon=True)
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

#第一張圖
plt.subplot(231)

degree = np.linspace(0, 2*np.pi, 36)    #共 36 個點
 
#print(degree)
x = degree
y1 = np.sin(degree)
#y1 = np.exp(-degree)   #指數
y2 = np.cos(degree)
y3 = np.tan(degree)
#plt.plot(x, y1)    #無其他參數
plt.plot(x, y1, color='red', lw=2)
plt.plot(x, y2, color='green', lw=2)
plt.plot(x, y3, color='blue', lw=2)
plt.plot(x, y3, 'ro')

plt.xlim(-0.1, 6.4)
plt.ylim(-1.1, 1.1)

plt.xlabel('角度(弧度)')
plt.ylabel('sin cos tan')
#plt.legend()
plt.title('三角函數')

#第二張圖
plt.subplot(232)

x1 = [1, 2, 3, 4, 5, 6]
y1 = [20, 30, 14, 67, 42, 12]
plt.plot(x1, y1, lw=2, label='Mary')

x2 = [1, 3, 4, 5, 9, 11]
y2 = [12, 33, 43, 22, 34, 20]
plt.plot(x2, y2, lw=2, label='Tom')

#第三張圖
plt.subplot(233)

import math
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#a = np.linspace(0,1,100)
a = np.linspace(-360,360,100)
#b = np.exp(-a)
b = np.sin(2*math.pi*a/360)
c = np.cos(2*math.pi*a/360)
d = np.sinc(2*math.pi*a/360)
plt.plot(a,b)
plt.plot(a,c)
plt.plot(a,d)

#plt.axis('off') #座標軸關閉
myfont = matplotlib.font_manager.FontProperties(fname=selected_font)
plt.xlabel(u'橫座標', fontproperties=myfont)
plt.ylabel(u'縱座標', fontproperties=myfont)
#plt.title('三角函數')
plt.title(u'三角函數', fontproperties=myfont)
plt.grid()

#第四~六張圖
plt.subplot(234)

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(-2.0*np.pi, 2.0*np.pi, 0.01)
a = np.sin(t)
b = np.cos(t)
c = np.sinc(t)

#第四張圖
plt.subplot(234)

plt.plot(t, a)

#第五張圖
plt.subplot(235)

plt.plot(t, b)

#第六張圖
plt.subplot(236)

#plt.plot(t, c)
plt.fill(t, c)

#plt.plot(t, a)
#plt.plot(t, b)
#plt.plot(t, c)

#plt.axis('off') #座標軸關閉

myfont = matplotlib.font_manager.FontProperties(fname=selected_font)

plt.xlabel(u'橫座標', fontproperties=myfont)
plt.ylabel(u'縱座標', fontproperties=myfont)
#plt.title('三角函數')
plt.title(u'三角函數', fontproperties=myfont)
plt.grid()

plt.show()




