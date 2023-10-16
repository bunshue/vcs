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

# 繪製 sin/cos 波形, 這個函數將被重複調用
def animate(i):
    line0.set_ydata(np.sin(x - i / 50))  # 更新 line0 變數
    line1.set_ydata(np.cos(x - i / 50))  # 更新 line0 變數
    return line0,

'''
# 兩張子圖，大小為 15x4 inch，dpi 分辨率 為 100 px/inch，故圖大小為 1500x400 px
fig, (ax0, ax1) = plt.subplots(ncols = 2, figsize = (15, 4), dpi = 100)
fig.suptitle('兩張子圖, ncols = 2', fontsize = 16) # 圖表主標題

# 建立 x 資料
x = np.arange(0, 2 * np.pi, 0.01)

# 建立 line0 變數
line0, = ax0.plot(x, np.sin(x))

# 建立 line1 變數
line1, = ax1.plot(x, np.cos(x))

# interval = 20, 相當於每隔 20 毫秒執行 animate()動畫 
ani = FuncAnimation(fig,
                    animate,
                    frames = 200,
                    interval = 20)
plt.show()

'''

#                編號                          圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
fig = plt.figure(num = 'plot 集合 1 函數曲線', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

# 建立 x 資料
x = np.arange(0, 2 * np.pi, 0.01)

#第一張圖
plt.subplot(121)

# 建立 line0 變數
line0, = plt.plot(x, np.sin(x))

#第二張圖
plt.subplot(122)

# 建立 line1 變數
line1, = plt.plot(x, np.cos(x))

# interval = 20, 相當於每隔 20 毫秒執行 animate()動畫 
ani = FuncAnimation(fig,
                    animate,
                    frames = 200,
                    interval = 20)
plt.show()



