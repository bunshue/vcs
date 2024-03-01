import cv2

import sys
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
import math

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

filename = 'mola_1024x512_200mp.jpg'
filename = 'C:/_git/vcs/_1.data/______test_files1/_material/ims3.bmp'

IMG_GRAY = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

plt.title('使用 matplotlib 顯示圖片, 需先BGR轉RGB')
plt.imshow(cv2.cvtColor(IMG_GRAY, cv2.COLOR_BGR2RGB))
plt.show()

print('image.shape內容 :', IMG_GRAY.shape)

H, W = IMG_GRAY.shape

x = np.linspace(W - 1, 0, W)
y = np.linspace(0, H - 1, H)

X, Y = np.meshgrid(x, y)
Z = IMG_GRAY[0 : H, 0 : W]

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='gist_earth')  # 150為剖面採樣數
ax.auto_scale_xyz([W - 1, 0], [0, H - 1], [0, 300])
plt.show()
