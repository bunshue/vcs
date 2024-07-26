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

# 輸出文字, 這個函數將被重複調用
def animate(i):
    label.set_text(string[:i + 1])      # 顯示字串

# 建立動畫需要的 Figure 物件和軸物件
fig, ax = plt.subplots()
# 建立軸物件與設定大小
ax.set(xlim = (-1, 1), ylim = (-1, 1))
string = '歡迎來到美國'  # 設定字串
# 使用水平與垂直置中在座標 0,0 位置顯示字串
label = ax.text(0, 0, string[0], ha = 'center', va = 'center',
                fontsize = 20, color = 'b')

interval = 300   #每隔 interval msec 執行 animate()動畫
anim = FuncAnimation(fig,animate,
                     frames = len(string),# 字串長度當作frames數
                     interval = interval)
ax.axis('off')

plt.show()

print('------------------------------------------------------------')	#60個
