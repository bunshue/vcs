# plot 集合 動畫

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

print('------------------------------------------------------------')	#60個

import matplotlib.pyplot as plt  
import numpy as np  
from matplotlib.animation import FuncAnimation  


print('------------------------------------------------------------')	#60個

"""
python學習之matplotlib繪制動圖（FuncAnimation()參數）

1、函數FuncAnimation(fig,func,frames,init_func,interval,blit)是繪制動圖的主要函數，其參數如下：

　　a.fig 繪制動圖的畫布名稱

　　b.func自定義動畫函數，即下邊程序定義的函數update

　　c.frames動畫長度，一次循環包含的幀數，在函數運行時，其值會傳遞給函數update(n)的形參“n”

　　d.init_func自定義開始幀，即傳入剛定義的函數init,初始化函數

　　e.interval更新頻率，以ms計

　　f.blit選擇更新所有點，還是僅更新產生變化的點。應選擇True，但mac用戶請選擇False，否則無法顯
"""

print('------------------------------------------------------------')	#60個

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()   #生成子圖，相當於fig = plt.figure(),ax = fig.add_subplot(),其中ax的函數參數表示把當前畫布進行分割，例：fig.add_subplot(2,2,2).表示將畫布分割為兩行兩列　　　　　　　　　　　　　　　　#ax在第2個子圖中繪制，其中行優先，
xdata, ydata = [], []      #初始化兩個數組
ln, = ax.plot([], [], 'r-', animated=False)  #第三個參數表示畫曲線的顏色和線型，具體參見：https://blog.csdn.net/tengqingyong/article/details/78829596

def init():
    ax.set_xlim(0, 2*np.pi)  #設置x軸的範圍pi代表3.14...圓周率，
    ax.set_ylim(-1, 1)          #設置y軸的範圍
    return ln,               #返回曲線

def update(n):  #n就是 FuncAnimation 裡面的 frames
    print(n)
    xdata.append(n)         #將每次傳過來的n追加到xdata中
    ydata.append(np.sin(n))
    ln.set_data(xdata, ydata)    #重新設置曲線的值
    return ln,

ani = FuncAnimation(fig,
                    update,
                    frames = np.linspace(0, 2 * np.pi, 10),     #這里的frames在調用update函數是會將frames作為實參傳遞給“n”
                    init_func = init,
                    interval = 100,
                    blit = True)
plt.show()

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


