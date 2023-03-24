# imshow 集合

selected_font = 'C:/_git/vcs/_4.cmpp/_python_test/data/msch.ttf'

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

#plt.figure(figsize=(8,8))	#設定圖片視窗大小
plt.figure(num = 'imshow 集合 2', figsize=[20, 15], dpi=84, facecolor="whitesmoke", edgecolor="r", linewidth=1, frameon=True)
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示


filename = 'C:/______test_files/bug.bmp'
img = np.asarray(Image.open(filename))
#print(repr(img))

#第一張圖
plt.subplot(231)

#原圖(灰階)
imgplot = plt.imshow(img)

#第二張圖
plt.subplot(232)

#1 偽色彩
lum_img = img[:, :, 0]
plt.imshow(lum_img)


#第三張圖
plt.subplot(233)

#2 偽色彩
plt.imshow(lum_img, cmap="hot")


#第四張圖
plt.subplot(234)


#3 偽色彩
imgplot = plt.imshow(lum_img)
imgplot.set_cmap('nipy_spectral')


#第五張圖
plt.subplot(235)


#4 Color scale reference
imgplot = plt.imshow(lum_img)
plt.colorbar()


#第六張圖
plt.subplot(236)



plt.show()






'''



#5
#plt.hist(img.ravel(), bins=range(256), fc='k', ec='k')


#6
plt.imshow(lum_img, clim=(0, 175))

#7
imgplot = plt.imshow(lum_img)
imgplot.set_clim(0, 175)


# Array Interpolation schemes
#8
img = Image.open(filename)
img.thumbnail((64, 64))  # resizes image in-place
imgplot = plt.imshow(img)

#9
imgplot = plt.imshow(img, interpolation="bilinear")

#10
imgplot = plt.imshow(img, interpolation="bicubic")


'''

