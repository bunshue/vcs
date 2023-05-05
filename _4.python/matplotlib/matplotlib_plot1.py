# plot 集合

selected_font = 'C:/_git/vcs/_1.data/______test_files1/msch.ttf'

import matplotlib.pyplot as plt
import numpy as np

#plt.figure(figsize=(8,8))	#設定圖片視窗大小
plt.figure(num = 'plot 集合 1 函數曲線', figsize=[20, 15], dpi=84, facecolor="whitesmoke", edgecolor="r", linewidth=1, frameon=True)
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

#第一張圖
plt.subplot(231)

x = np.linspace(0, 6.28, 10)
y = np.sin(x / 2)

dx = 0.3
#連線
plt.plot(x + dx * 0, y, color='red')

#linestyle 虛線樣式
plt.plot(x + dx * 1, y, color='red', linestyle="--")

#linestyle 虛點樣式
plt.plot(x + dx * 2, y, color='red', linestyle="-.")

#linestyle 虛點樣式「:」
plt.plot(x + dx * 3, y, color='red', linestyle=":")

#marker 點「.」標記
#因為需要展示出效果，因此把 linestyle 設為實線，linewidth 為 2.0，markersize 設為 8
plt.plot(x + dx * 4, y, color='red', linestyle="-", linewidth="2", markersize="8", marker=".")

#marker 圓「o」標記
plt.plot(x + dx * 5, y, color='red', linestyle="-", linewidth="2", markersize="8", marker="o")

#marker 星「*」標記
plt.plot(x + dx * 6, y, color='red', linestyle="-", linewidth="2", markersize="8", marker="*")

#marker 矩形「s」標記
plt.plot(x + dx * 7, y, color='red', linestyle="-", linewidth="2", markersize="8", marker="s")

plt.plot(x + dx * 8, y, color='red', linestyle="-", linewidth="2", markersize="8", marker=".", label="Test")

# 繪製折線圖，顏色「紅色」，線條樣式「-」，線條寬度「2」，標記大小「16」，標記樣式「.」，圖例名稱「Plot 1」
plt.plot(x + dx * 9, y, color='red', linestyle="-", linewidth="2", markersize="8", marker=".", label="Plot 1")

# 繪製折線圖，顏色「藍色」，線條樣式「-」，線條寬度「2」，標記大小「16」，標記樣式「.」，圖例名稱「Plot 2」
plt.plot(x + dx * 9, y, color='blue', linestyle="-", linewidth="2", markersize="8", marker=".", label="Plot 2")

plt.xlabel('x label', fontsize="10") # 設定 x 軸標題內容及大小
plt.ylabel('y label', fontsize="10") # 設定 y 軸標題內容及大小
plt.title('Plot title', fontsize="18") # 設定圖表標題內容及大小

#設定 x, y 軸座標範圍
#plt.xlim(0, 30) # 設定 x 軸座標範圍
#plt.ylim(0, 50) # 設定 y 軸座標範圍

plt.legend()


#第二張圖
plt.subplot(232)

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

plt.xlabel('Time(s)', fontproperties=font)
plt.ylabel('Amplitude', fontproperties=font)
plt.title(u'三角函數', fontproperties=font, fontsize=24)

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




# plot 集合

selected_font = 'C:/_git/vcs/_1.data/______test_files1/msch.ttf'

import matplotlib.pyplot as plt
import numpy as np

#plt.figure(figsize=(8,8))	#設定圖片視窗大小
plt.figure(num = 'plot 集合 2 函數曲線', figsize=[20, 15], dpi=84, facecolor="whitesmoke", edgecolor="r", linewidth=1, frameon=True)
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

#第一張圖
plt.subplot(231)

x = np.arange(0,360)
y = np.sin( 2 * x * np.pi / 180.0)
z = np.cos( x * np.pi / 180.0)
plt.plot(x,y,color="blue",label="SIN(2x)")
plt.plot(x,z,color="red",label="COS(x)")
plt.xlim(0,360)
plt.ylim(-1.2,1.2)
plt.xlabel("Degree")
plt.ylabel("Value")
plt.title("SIN & COS function")
plt.legend()


#第二張圖
plt.subplot(232)

t = np.arange(0.0, 1.0, 0.01)
s = np.sin(2*np.pi*t)
plt.plot(t, s, color='blue', lw=2)

#第三張圖
plt.subplot(233)

x1 = np.linspace(0.0, 5.0, 100)
y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
plt.plot(x1, y1*10000)

#第四張圖
plt.subplot(234)

#第五張圖
plt.subplot(235)




#第六張圖
plt.subplot(236)




plt.show()


# plot 集合

selected_font = 'C:/_git/vcs/_1.data/______test_files1/msch.ttf'

import matplotlib.pyplot as plt
import numpy as np

#plt.figure(figsize=(8,8))	#設定圖片視窗大小
plt.figure(num = 'plot 集合 3 直線連線', figsize=[20, 15], dpi=84, facecolor="whitesmoke", edgecolor="r", linewidth=1, frameon=True)
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

#第一張圖
plt.subplot(231)

listx = [1,5,7,9,13,16]
listy = [15,50,80,40,70,50]
plt.plot(listx, listy, 'g--*', markersize=12)


#第二張圖
plt.subplot(232)

listx = [1,5,7,9,13,16]
listy = [15,50,80,40,70,50]
plt.plot(listx, listy, color="red", lw="2.0", ls="--", label="label")
plt.title("Chart Title", fontsize=20)	#圖表標題
plt.xlabel("X-Label", fontsize=14)		#x座標標題
plt.ylabel("Y-Label", fontsize=14)		#y座標標題
plt.legend()


#第三張圖
plt.subplot(233)


listx = [1,5,7,9,13,16]
listy = [15,50,80,40,70,50]
plt.plot(listx, listy, color="red", lw="2.0", ls="--", label="label")
plt.title("Chart Title")	#圖表標題
plt.xlabel("X-Label")		#x座標標題
plt.ylabel("Y-Label")		#y座標標題
plt.xlim(0, 20)            #設定x座標範圍
plt.ylim(0, 100)             #設定y座標範圍
plt.legend()


#第四張圖
plt.subplot(234)
listx = [1,5,7,9,13,18]
listy = [15,50,80,40,70,50]
plt.plot(listx, listy, color="red", lw="2.0", ls="--", label="label")
plt.title("Chart Title")	#圖表標題
plt.xlabel("X-Label")		#x座標標題
plt.ylabel("Y-Label")		#y座標標題
plt.xlim(0, 20)            #設定x座標範圍
plt.ylim(0, 100)             #設定y座標範圍
plt.grid(color='black', linestyle=":", linewidth='1', alpha=0.5)
plt.legend()

#第五張圖
plt.subplot(235)

listx1 = [1,5,7,9,13,16]
listy1 = [15,50,80,40,70,50]
plt.plot(listx1, listy1, label="Male")

listx2 = [2,6,8,11,14,16]
listy2 = [10,40,30,50,80,60]
plt.plot(listx2, listy2, color="red", linewidth=5, linestyle="--", label="Female")
plt.legend()
plt.xlim(0, 20)
plt.ylim(0, 100)
plt.title("零用金統計")
plt.xlabel("年齡")
plt.ylabel("零用金數目")


#第六張圖
plt.subplot(236)

x1 = [1, 2, 3, 4, 5, 6]
y1 = [20, 30, 14, 67, 42, 12]
plt.plot(x1, y1, lw=2, label='Mary')

x2 = [1, 3, 4, 5, 9, 11]
y2 = [12, 33, 43, 22, 34, 20]
plt.plot(x2, y2, lw=2, label='Tom')

plt.show()


# plot 集合

selected_font = 'C:/_git/vcs/_1.data/______test_files1/msch.ttf'

import matplotlib.pyplot as plt
import numpy as np

#plt.figure(figsize=(8,8))	#設定圖片視窗大小
plt.figure(num = 'plot 集合 4 測試畫點畫線', figsize=[20, 15], dpi=84, facecolor="whitesmoke", edgecolor="r", linewidth=1, frameon=True)

#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

x = np.linspace(0, 6.28, 20)
y = np.sin(x)

#第一張圖
plt.subplot(231)
#plt.subplot(2, 3, 1)   same
#plt.title('231')   same

plt.title(label='231')
plt.plot(x, y, 'ro-')

#第二張圖
plt.subplot(232)

plt.title(label='232')
plt.plot(x, y, 'g.-')

#第三張圖
plt.subplot(233)

plt.title(label='233')
plt.plot(x, y, 'b:o')

#第四張圖
plt.subplot(234)

plt.title(label='234')
plt.plot(x, y, 'y--o')

#第五張圖
plt.subplot(235)

plt.title(label='235')
plt.plot(x, y, 'm.-')

#第六張圖
plt.subplot(236)

plt.title(label='236')
plt.plot(x, y, 'c.-')
#plt.axes([0.2,0.2,0.4,0.4]) #設定顯示位置

plt.show()






plt.figure(num = 'plot 集合 5 不使用subplot畫多圖', figsize=[20, 15], dpi=84, facecolor="whitesmoke", edgecolor="r", linewidth=1, frameon=True)

import matplotlib.pyplot as plt

print("在圖表的指定地方畫圖, 不用subplot")

listx = [1,2,3,4,5]
listy = [15,50,80,40,70]

print("1左下開始(0.1, 0.1), w = 0.3, h = 0.3, 左下圖")
plt.axes([0.1, 0.1, 0.3, 0.3])
plt.plot(listx, listy, 'r-s')

print("2左下開始(0.6, 0.1), w = 0.3, h = 0.3, 右下圖")
plt.axes([0.6, 0.1, 0.3, 0.3])
plt.plot(listx, listy, 'g--o')

print("3左下開始(0.1, 0.6), w = 0.3, h = 0.3, 左上圖")
plt.axes([0.1, 0.6, 0.3, 0.3])
plt.plot(listx, listy, 'b-s')

print("4左下開始(0.6, 0.6), w = 0.3, h = 0.3, 右上圖")
plt.axes([0.6, 0.6, 0.3, 0.3])
plt.plot(listx, listy, 'y--o')

plt.show()







