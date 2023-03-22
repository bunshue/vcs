import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

filename = 'C:/______test_files/bug.bmp'

img = np.asarray(Image.open(filename))
#print(repr(img))


#原圖(灰階)
imgplot = plt.imshow(img)

#1 偽色彩
lum_img = img[:, :, 0]
plt.imshow(lum_img)

#2 偽色彩
plt.imshow(lum_img, cmap="hot")

#3 偽色彩
imgplot = plt.imshow(lum_img)
imgplot.set_cmap('nipy_spectral')

#4 Color scale reference
imgplot = plt.imshow(lum_img)
plt.colorbar()

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


plt.show()


