from matplotlib.animation import ArtistAnimation  
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

# 建立動畫需要的 Figure 物件和軸物件
fig, ax = plt.subplots()
# 建立影像數值
def f(x, y):
    return np.sin(x) + np.cos(y) * 2    # 數值相加變成矩陣
# 建立 x 和 y 陣列
x = np.linspace(0, 2 * np.pi, 120)
y = np.linspace(0, 2 * np.pi, 120).reshape(-1, 1)
# 建立影像串列 pict, 每一列皆是一個frame
picts = []
# for 迴圈填滿 60 個影像
for i in range(60):
    x += np.pi / 2                      # 建立影像陣列 x
    y += np.pi / 25                     # 建立影像陣列 y
    pict = ax.imshow(f(x, y), cmap = 'hsv')
    if i == 0:                          # 繪製索引 0
        ax.imshow(f(x, y), cmap = 'hsv')  
    picts.append([pict])                # 影像儲存到串列

interval = 100   #每隔 interval msec 執行 animate()動畫
ani = ArtistAnimation(fig,
                      picts,
                      interval = interval,
                      repeat_delay = 500,
                      repeat = False)   #和True比較看看
plt.axis('off')

plt.show()

print('------------------------------------------------------------')	#60個
