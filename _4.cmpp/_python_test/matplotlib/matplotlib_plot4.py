# plot 集合

selected_font = 'C:/_git/vcs/_4.cmpp/_python_test/data/msch.ttf'

import matplotlib.pyplot as plt
import numpy as np

#plt.figure(figsize=(8,8))	#設定圖片視窗大小
plt.figure(num = 'plot 集合', figsize=[20, 15], dpi=84, facecolor="whitesmoke", edgecolor="r", linewidth=1, frameon=True)

#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

x = np.linspace(0, 6.28, 20)
y = np.sin(x)

#第一張圖
plt.subplot(231)
#plt.subplot(2, 3, 1)   same
#plt.title('231')   same

plt.title(label='231')
plt.plot(x, y, 'ro-')

#第二張圖
plt.subplot(232)

plt.title(label='232')
plt.plot(x, y, 'g.-')

#第三張圖
plt.subplot(233)

plt.title(label='233')
plt.plot(x, y, 'b:o')

#第四張圖
plt.subplot(234)

plt.title(label='234')
plt.plot(x, y, 'y--o')

#第五張圖
plt.subplot(235)

plt.title(label='235')
plt.plot(x, y, 'm.-')

#第六張圖
plt.subplot(236)

plt.title(label='236')
plt.plot(x, y, 'c.-')
#plt.axes([0.2,0.2,0.4,0.4]) #設定顯示位置

plt.show()


