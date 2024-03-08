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

# 繪製動畫, 這個函數將被重複調用
def animate(i):
    y0data = np.sin(x - i / 50)
    y1data = np.sin(x - i / 50 + 0.2)
    y2data = np.sin(x - i / 50 + 0.4)
    y3data = np.random.randn(100)
    line0.set_ydata(y0data)  # 更新 line0 變數
    line1.set_ydata(y1data)  # 更新 line1 變數
    line2.set_ydata(y2data)  # 更新 line1 變數
    print(i, end = ' ')
    return line0, line1, line2

#fig = plt.figure(figsize = (10, 6))
fig = plt.figure()

# 建立 x 資料
x = np.arange(0, 2 * np.pi, 0.02)
y0 = np.sin(x)
y1 = np.sin(x + 0.2)
y2 = np.sin(x + 0.4)

line0, = plt.plot(x, y0)    # 建立 line0 變數
line1, = plt.plot(x, y1)    # 建立 line1 變數
line2, = plt.plot(x, y2)    # 建立 line2 變數

interval = 20   #每隔 interval msec 執行 animate()動畫
ani = FuncAnimation(fig,
                    animate,
                    frames = 200000,
                    interval = interval)
plt.show()

print('------------------------------------------------------------')	#60個
