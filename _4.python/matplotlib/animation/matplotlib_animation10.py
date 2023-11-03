import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.animation import FuncAnimation

#fig = plt.figure(figsize = (10, 6))
fig = plt.figure()

# 建立 x 資料
x = np.arange(0, 2 * np.pi, 0.02)
y = np.sin(x)
#y = np.exp(-x) * np.cos(2 * np.pi * x)
line, = plt.plot(x, y, color = "cornflowerblue", lw = 3) # 建立 line 變數

#ax.set_ylim(-1.0, 1.0)

# to clear current frame
def init():
    line.set_ydata([np.nan] * len(x))
    return line,

# to update the data
def animate(i):
    #y = np.exp(-x) * np.cos(2 * np.pi * x + float(i) / 100)
    ydata = np.sin(x - i / 50)
    line.set_ydata(ydata)   # 更新 line 變數
    return line,

interval = 2   #每隔 interval msec 執行 animate()動畫
ani = FuncAnimation(fig,
                    animate,
                    init_func = init,
                    frames = 200,
                    interval = interval,
                    blit = True)

# to save the animation
#ani.save("movie.mp4", fps=20, writer="ffmpeg")

plt.show()

print('------------------------------------------------------------')	#60個
