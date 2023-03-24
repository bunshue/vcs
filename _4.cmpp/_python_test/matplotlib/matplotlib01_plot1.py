# plot 集合

selected_font = 'C:/_git/vcs/_4.cmpp/_python_test/data/msch.ttf'

import matplotlib.pyplot as plt
import numpy as np

#plt.figure(figsize=(8,8))	#設定圖片視窗大小
plt.figure(num = 'plot 集合 1', figsize=[20, 15], dpi=84, facecolor="whitesmoke", edgecolor="r", linewidth=1, frameon=True)
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

#t = np.linspace(0,1,100)
t = np.linspace(-360,360,100)
#b = np.exp(-a)
a = np.sin(2*math.pi*t/360)
b = np.cos(2*math.pi*t/360)
c = np.sinc(2*math.pi*t/360)

'''另一種製造資料的方法
# Data for plotting
t = np.arange(-2.0*np.pi, 2.0*np.pi, 0.01)
a = np.sin(t)
b = np.cos(t)
c = np.sinc(t)
'''

plt.plot(t, a)
plt.plot(t, b)
plt.plot(t, c)
#plt.fill(t, c)

#plt.axis('off') #座標軸關閉
myfont = matplotlib.font_manager.FontProperties(fname=selected_font)
plt.xlabel(u'橫座標', fontproperties=myfont)
plt.ylabel(u'縱座標', fontproperties=myfont)
#plt.title('三角函數')
plt.title(u'三角函數', fontproperties=myfont)
plt.grid()



#第四張圖
plt.subplot(234)

x = np.linspace(0, 10, 100)
y = np.sin(x)
z = np.cos(x**2)

plt.plot(x, y, label="$sin(x)$", color='red', lw=2)
plt.plot(x, z, label="$cos(x^2)$", color='b')
plt.xlabel('Time(s)')
plt.ylabel('Volt')
plt.title('Volt/Time chart')
plt.ylim(-1.2,1.2)
plt.legend()


#第五張圖
plt.subplot(235)
from matplotlib.font_manager import FontProperties

font = FontProperties(fname=r"c:\windows\Fonts\SimSun.ttc", size=20)

x = np.linspace(0, 10, 1000)
y = np.sin(x)
z = np.cos(x**2)

plt.plot(x, y, label="$sin(x)$", color="red", linewidth=2)
plt.plot(x, z, "b--", label="$cos(x^2)$")

plt.xlabel("Time(s)", fontproperties=font)
plt.ylabel("Amplitude", fontproperties=font)
plt.title(u"中文測試中...", fontproperties=font)

plt.ylim(-1.2, 1.2)
plt.legend()
plt.grid()



#第六張圖
plt.subplot(236)

#在同一張圖 畫 兩條曲線

month1 = [1,2,3,4,5,6,7,8,9,10,11,12]
month2 = [1,2,3,4,5,6,7,8,9,10,11,12]

listy1 = [128,210,199,121,105,98,152,107,150,122,180,220]
listy2 = [150,200,180,110,100,80,80,100,130,120,110,200]

plt.plot(month1, listy1) #直線連線
plt.plot(month1, listy1, 'r-.s')#少參數
plt.plot(month1, listy1, 'r-.s', lw=2, ms=10, label="台北")#多參數

plt.plot(month2, listy2) #直線連線
plt.plot(month2, listy2, 'g--*')#少參數
plt.plot(month2, listy2, 'g--*', lw=2, ms=10, label="台中")#多參數

#同一個指令畫兩條線
#plt.plot(month1, listy1, 'r-.s', month2, listy2, 'y-s')

plt.legend()
plt.xticks(month1)
plt.xlim(0.5, 12.5)     #x軸顯示邊界
plt.ylim(50, 250)   #y軸顯示邊界
plt.title("Sales Report", fontsize=18)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Million", fontsize=12)
plt.title("銷售報表", fontsize=18)
plt.xlabel("月", fontsize=12)
plt.ylabel("百萬", fontsize=12)

plt.grid(color='k', ls=':', lw=1, alpha=0.5)    #畫格點

plt.tick_params(axis='both', labelsize=16, color='red')#xy軸多加tick
#plt.tick_params(axis='y', color='red')#y軸多加tick





plt.show()




