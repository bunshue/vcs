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

# mpl.use("Qt5Agg")

#mpl.rcParams['font.sans-serif'] = ['SimHei']
#mpl.rcParams['font.serif'] = ['SimHei']
#mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题,或者转换负号为字符串

fig, ax = plt.subplots(1, 1)

x = np.linspace(0, 2 * np.pi, 5000)
y = np.exp(-x) * np.cos(2 * np.pi * x)
line, = ax.plot(x, y, color="cornflowerblue", lw=3)
ax.set_ylim(-1.0, 1.0)


# to clear current frame
def init():
    line.set_ydata([np.nan] * len(x))
    return line,


# to update the data
def animate(data):
    line.set_ydata(np.exp(-x) * np.cos(2 * np.pi * x + float(data) / 100))
    return line,


# to call class FuncAnimation which connects animate and init
ani = FuncAnimation(fig, animate, init_func=init, frames=200, interval=2, blit=True)

# to save the animation
#ani.save("movie.mp4", fps=20, writer="ffmpeg")

plt.show()

print('------------------------------------------------------------')	#60個
