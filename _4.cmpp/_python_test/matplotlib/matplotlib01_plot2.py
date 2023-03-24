# plot 集合

selected_font = 'C:/_git/vcs/_4.cmpp/_python_test/data/msch.ttf'

import matplotlib.pyplot as plt
import numpy as np

#plt.figure(figsize=(8,8))	#設定圖片視窗大小
plt.figure(num = 'plot 集合 2', figsize=[20, 15], dpi=84, facecolor="whitesmoke", edgecolor="r", linewidth=1, frameon=True)
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

x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y = np.sinc(x)
plt.plot(x, y)
plt.margins(0.2, 0.2)
plt.title('多了margins設定 ')

#第五~六張圖

#x, y 承上

xx, yy = np.meshgrid(x, x)
zz = np.sinc(np.sqrt((xx - 1)**2 + (yy - 1)**2))

#第五張圖
plt.subplot(235)
plt.imshow(zz)
plt.title('default margins')

#第六張圖
plt.subplot(236)
plt.imshow(zz)
plt.margins(0.2)
plt.title('margins(0.2)')

#第六張圖
plt.subplot(236)





plt.show()




