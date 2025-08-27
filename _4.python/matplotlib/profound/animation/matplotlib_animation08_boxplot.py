import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

font_filename = 'D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

import matplotlib.animation as animation

fig, ax = plt.subplots()
ax.set_ylim(-5, 5)

def animate(data):
    ax.cla()  # <-- clear the subplot otherwise boxplot shows previous frame
    ax.set_ylim(-5, 5)
    ax.boxplot(x=data)  

def data_gen():
    i = 0
    while True:
        #yield np.arange(10) + i
        yield np.random.randn(100)
        i += .1

interval = 100   #每隔 interval msec 執行 animate()動畫
ani = animation.FuncAnimation(fig,
                              animate,
                              data_gen,
                              interval = interval)
plt.show()

''' default
ani = FuncAnimation(fig,
                    animate,
                    frames = 200000,
                    interval = interval)
plt.show()
'''
print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

