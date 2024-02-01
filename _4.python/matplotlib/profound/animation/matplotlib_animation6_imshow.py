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

# 輸出矩陣影像, 這個函數將被重複調用
def animate(i):
    pict = np.random.rand(8,8)
    ax.imshow(pict, cmap='jet')

# 建立動畫需要的 Figure 物件和軸物件       
fig, ax = plt.subplots()

interval = 100   #每隔 interval msec 執行 animate()動畫
anim = FuncAnimation(fig,
                     animate,
                     frames = 50,
                     interval = interval)

ax.set_axis_off()

plt.show()

print('------------------------------------------------------------')	#60個


