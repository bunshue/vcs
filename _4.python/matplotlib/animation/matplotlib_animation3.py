import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# 繪製 cos 波形, 這個函數將被重複調用
def animate(i):
    line.set_ydata(np.cos(x - i / 50))  # 更新 line 變數
    return line,

# 建立動畫需要的 Figure 物件和軸物件 ax
fig, ax = plt.subplots()
# 建立 x 資料
x = np.arange(0, 2*np.pi, 0.01)
# 建立 line 變數
line, = ax.plot(x, np.cos(x))

# interval = 20, 相當於每隔 20 毫秒執行 animate()動畫 
ani = FuncAnimation(fig,
                    animate,
                    frames = 200,
                    interval = 20)
plt.show()


