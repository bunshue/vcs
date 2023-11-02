# 新進測試06

import sys
import matplotlib.pyplot as plt
import numpy as np
import math

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

'''
# 一個完全乾淨、空白的figure:
fig = plt.figure()

# 增新一個axes（座標軸），以供繪圖和放置資訊:
#axs = fig.add_subplot(1,1,1) # 1x1的座標軸

# 增新很多個axes，以供繪圖和放置資訊:
#fig.delaxes( fig.gca() ) # 順便示範，把剛剛1x1的座標軸刪掉

#fig1 = plt.figure()  # 等價於fig1 = plt.figure(1)
fig2 = plt.figure()  # 等價於fig2 = plt.figure(2)

# 一般的情況下，axes是"hold on"的, 也就是資料不會被覆蓋掉。
# hold on: 好處是一次要輸出一堆函數，可以把圖疊加上去。
# hold off: 可以更新圖的內容，可是全部的資訊會被洗掉（title, legend等）
# 如果要保留這些資訊，可以單獨抓出圖的內容，直接修改：
x = np.linspace(0,1,100)
y = np.sin(x)

axes = fig2.add_subplot(1,1,1)
axes.set_title('y = sin(x)')

line, = axes.plot(x,y) # 這裡回傳的line就是畫在圖上的資料

# 當發現畫錯想修改，可以對line修改：
line.set_ydata(np.cos(x))

fig2.savefig('./sample.png') #將圖片輸出成檔案.

plt.show()

'''
print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


