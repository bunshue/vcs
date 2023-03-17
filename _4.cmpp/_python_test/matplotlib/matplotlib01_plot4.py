import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,360)
y = np.sin( x * np.pi / 180.0)
plt.plot(x,y)
plt.xlim(0,360)
plt.ylim(-1.2,1.2)
plt.title("SIN function")
plt.show()


import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0,360)
y = np.sin( x * np.pi / 180.0)
z = np.cos( x * np.pi / 180.0)
plt.plot(x,y,color="blue")
plt.plot(x,z,color="red")
plt.xlim(0,360)
plt.ylim(-1.2,1.2)
plt.title("SIN & COS function")
plt.show()


import numpy as np
import matplotlib.pyplot as plt
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
plt.show()


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.sin(x)
z = np.cos(x**2)

plt.figure()
plt.plot(x, y, label="$sin(x)$", color='red', lw=2)
plt.plot(x, z, label="$cos(x^2)$", color='b')
plt.xlabel('Time(s)')
plt.ylabel('Volt')
plt.title('Volt/Time chart')
plt.ylim(-1.2,1.2)
plt.legend()

plt.show()



from matplotlib.font_manager import FontProperties

#selected_font = 'C:/_git/vcs/_4.cmpp/_python_test/data/msch.ttf'
font = FontProperties(fname=r"c:\windows\Fonts\SimSun.ttc", size=20)

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 1000)
y = np.sin(x)
z = np.cos(x**2)

plt.figure(figsize=(8,4))

plt.plot(x, y, label="$sin(x)$", color="red", linewidth=2)
plt.plot(x, z, "b--", label="$cos(x^2)$")

plt.xlabel("Time(s)", fontproperties=font)
plt.ylabel("Amplitude", fontproperties=font)
plt.title(u"中文測試中...", fontproperties=font)

plt.ylim(-1.2, 1.2)
plt.legend()
plt.grid()

plt.show()



import math
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

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
selected_font = 'C:/_git/vcs/_4.cmpp/_python_test/data/msch.ttf'
myfont = matplotlib.font_manager.FontProperties(fname=selected_font)
plt.xlabel(u'橫座標', fontproperties=myfont)
plt.ylabel(u'縱座標', fontproperties=myfont)

plt.show()




import matplotlib.pyplot as plt

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

#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

plt.grid(color='k', ls=':', lw=1, alpha=0.5)    #畫格點

plt.tick_params(axis='both', labelsize=16, color='red')#xy軸多加tick
#plt.tick_params(axis='y', color='red')#y軸多加tick

plt.show()  #將圖表呈現出來







