'''
參考 使用Matplotlib绘制3D图形
https://paul.pub/matplotlib-3d-plotting/

參考 Python 使用 Matplotlib 繪製 3D 資料圖形教學與範例
https://officeguide.cc/python-matplotlib-three-dimensional-plotting-tutorial-examples/
'''

# 3D plot 集合

selected_font = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'

import matplotlib.pyplot as plt
import numpy as np

#plt.figure(figsize=(8,8))	#設定圖片視窗大小
fig = plt.figure(num = '3D繪圖 集合 2', figsize=[20, 15], dpi=84, facecolor="whitesmoke", edgecolor="r", linewidth=1, frameon=True)
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

#XXXXXXX1
ax = fig.add_subplot(231, projection='3d')  #第一張圖


ax.set_title('XXXXXXX1')



#XXXXXXX2
ax = fig.add_subplot(232, projection='3d')  #第二張圖




#XXXXXXX3
ax = fig.add_subplot(233, projection='3d')  #第三張圖

ax.set_title('XXXXXXX3')

#XXXXXXX4
ax = fig.add_subplot(234, projection='3d')  #第四張圖

#
#
#
ax.set_title('XXXXXXX4')

#XXXXXXX5
ax = fig.add_subplot(235, projection='3d')  #第五張圖

#
#
#
ax.set_title('XXXXXXX5')

#XXXXXXX6
ax = fig.add_subplot(236, projection='3d')  #第六張圖

#
#
#
ax.set_title('XXXXXXX6')


plt.show()




