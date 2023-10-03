'''
imshow
'''

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg'

import sys
import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np
from PIL import Image, ImageEnhance
import matplotlib.cm as cm
import pylab

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

#          編號                          圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(num = 'imshow 集合 1', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

image1 = Image.open(filename)              # 開啟圖片
enhancer = ImageEnhance.Brightness(image1)   # 建立調整亮度的方法

#第一張圖
plt.subplot(231)

# 顯示原圖
plt.imshow(image1)                  # 在子圖表中繪製圖片

#第二張圖
plt.subplot(232)


# 顯示亮度 x0.5 的圖片
image2 = enhancer.enhance(0.5)  # 顯示亮度 x0.5 的圖片
plt.imshow(image2)                  # 在子圖表中繪製圖片

#第三張圖
plt.subplot(233)

image3 = enhancer.enhance(1.5)  # 顯示亮度 x1.5 的圖片
plt.imshow(image3)                  # 在子圖表中繪製圖片

#第四張圖
plt.subplot(234)

image4 = enhancer.enhance(3)    # 顯示亮度 x3 的圖片
plt.imshow(image4)                  # 在子圖表中繪製圖片

#第五張圖
plt.subplot(235)

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

#裁剪圖片 plt


import matplotlib.pyplot as plt
import matplotlib.image as img

print('使用 matplotlib 顯示一圖')
image = img.imread(filename)
image = img.imread(filename)

plt.imshow(image)	#顯示圖片, 兩行都要
#plt.show()              #顯示圖片, 兩行都要



#第六張圖
plt.subplot(236)

x_l, x_r = 150, 350 #保留的部分，由左而右
y_u, y_d = 150, 400 #保留的部分，由上而下
cut_img = image[y_u:y_d, x_l:x_r]

plt.imshow(cut_img)	#顯示圖片, 兩行都要
#plt.show()              #顯示圖片, 兩行都要


plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/bug.bmp'

#          編號                  圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(num = 'imshow 集合 2', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

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

import matplotlib.image as img

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
pict = img.imread(filename)
plt.axis('off')
plt.title('牡丹亭', fontsize = 24)
plt.imshow(pict)



plt.show()

print('------------------------------------------------------------')	#60個

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

print('------------------------------------------------------------')	#60個

#          編號                   圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(num = 'imshow 集合 3', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

#第一張圖
plt.subplot(231)

delta = 0.025
x = y = np.arange(-3.0, 3.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2

im = plt.imshow(Z, interpolation='bilinear', cmap=cm.gray,
                origin='lower', extent=[-3, 3, -3, 3])
'''
im.set_url('https://www.google.com/')
filename = 'C:/_git/vcs/_1.data/______test_files2/image.svg'
fig.savefig(filename)
print('已存圖' + filename)
'''

#第二張圖
plt.subplot(232)

#Layer Images

def func3(x, y):
    return (1 - x / 2 + x**5 + y**3) * np.exp(-(x**2 + y**2))

# make these smaller to increase the resolution
dx, dy = 0.05, 0.05

x = np.arange(-3.0, 3.0, dx)
y = np.arange(-3.0, 3.0, dy)
X, Y = np.meshgrid(x, y)

# when layering multiple images, the images need to have the same
# extent.  This does not mean they need to have the same shape, but
# they both need to render to the same coordinate system determined by
# xmin, xmax, ymin, ymax.  Note if you use different interpolations
# for the images their apparent extent could be different due to
# interpolation edge effects

extent = np.min(x), np.max(x), np.min(y), np.max(y)

Z1 = np.add.outer(range(8), range(8)) % 2  # chessboard
im1 = plt.imshow(Z1, cmap=plt.cm.gray, interpolation='nearest', extent=extent)

Z2 = func3(X, Y)

im2 = plt.imshow(Z2, cmap=plt.cm.viridis, alpha=.9, interpolation='bilinear', extent=extent)



#第三張圖
plt.subplot(233)

import matplotlib.image as img

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

pict = img.imread(filename)
h, w, c = pict.shape
print(f"圖檔高度   = {h}")
print(f"圖檔寬度   = {w}")
print(f"圖檔通道數 = {c}")
plt.axis('off')
plt.title('牡丹亭', fontsize=24)
plt.imshow(pict)




#第四~五張圖

# Subplots spacings and margins

# Fixing random state for reproducibility
np.random.seed(19680801)

#第四張圖
plt.subplot(234)
plt.imshow(np.random.random((100, 100)))
#第五張圖
plt.subplot(235)
plt.imshow(np.random.random((100, 100)))

plt.subplots_adjust(bottom=0.1, right=0.8, top=0.9)
cax = plt.axes([0.85, 0.1, 0.075, 0.8]) #設定位置
plt.colorbar(cax=cax)








#第六張圖
plt.subplot(236)



plt.show()

print('------------------------------------------------------------')	#60個

#          編號               圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(num = 'imshow 集合 4', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

#第一張圖
plt.subplot(231)

xmin, xmax, ymin, ymax = -2, 0.8, -1.5, 1.5
max_it = 3    # maximum number of iterations
px     = 300	# vertical lines
res    = (ymax - ymin) / px   # grid resolution

def m(c):
	z = 0
	for n in range(1, max_it + 1):
		z = z**2 + c
		if abs(z) > 2:
			return n
	return np.NaN

X = pylab.arange(xmin, xmax + res, res)
Y = pylab.arange(ymin, ymax + res, res)
Z = pylab.zeros((len(Y), len(X)))

for iy, y in enumerate(Y):
	#print (iy + 1, "of", len(Y))
	for ix, x in enumerate(X):
		Z[-iy - 1, ix] = m(x + 1j * y)

#影像存圖
#pylab.save("mandel", Z)	# save array to file

plt.imshow(Z, cmap = plt.cm.prism, interpolation = 'none', extent = (X.min(), X.max(), Y.min(), Y.max()))
plt.xlabel("Re(c)")
plt.ylabel("Im(c)")

#第二張圖
plt.subplot(232)

xmin, xmax, ymin, ymax = -2, 0.8, -1.5, 1.5
max_it = 3    # maximum number of iterations
px     = 30	# vertical lines
res    = (ymax - ymin) / px   # grid resolution

def m(c):
	z = 0
	for n in range(1, max_it + 1):
		z = z**2 + c
		if abs(z) > 2:
			return n
	return np.NaN

X = pylab.arange(xmin, xmax + res, res)
Y = pylab.arange(ymin, ymax + res, res)
Z = pylab.zeros((len(Y), len(X)))

for iy, y in enumerate(Y):
	#print (iy + 1, "of", len(Y))
	for ix, x in enumerate(X):
		Z[-iy - 1, ix] = m(x + 1j * y)

plt.imshow(Z, cmap = plt.cm.prism, interpolation = 'none', extent = (X.min(), X.max(), Y.min(), Y.max()))
plt.xlabel("Re(c)")
plt.ylabel("Im(c)")

#第三張圖
plt.subplot(233)

pts = np.arange(-2, 2, 0.01)
x, y = np.meshgrid(pts, pts)
z = np.sqrt(x**2 + y**2)

ticks = np.arange(0, 500, 100)
seq = np.arange(-2, 3)

plt.imshow(z, cmap='rainbow')
plt.xticks(ticks, seq)
plt.yticks(ticks, seq)

plt.colorbar()
plt.title(r"建立$\sqrt{x^2 + y^2}$網格影像")

#第四張圖
plt.subplot(234)

x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y = np.sinc(x)
plt.plot(x, y)
plt.margins(0.2, 0.2)
plt.title('多了margins設定 ')

#第五~六張圖

#x, y 承上

xx, yy = np.meshgrid(x, x)
zz = np.sinc(np.sqrt((xx - 1)**2 + (yy - 1)**2))

#第五張圖
plt.subplot(235)
plt.imshow(zz)
plt.title('default margins')

#第六張圖
plt.subplot(236)
plt.imshow(zz)
plt.margins(0.2)
plt.title('margins(0.2)')


plt.show()


print('------------------------------------------------------------')	#60個

#          編號               圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(num = 'imshow 集合 5', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

#第一張圖
plt.subplot(231)


print('imshow 顯示 numpy 資料')
plt.rcParams['savefig.facecolor'] = "0.8"

arr = np.arange(256).reshape((16, 16))

plt.imshow(arr, interpolation="none")

plt.tight_layout()


#第二張圖
plt.subplot(232)

print('imshow 顯示 numpy 資料')

arr = np.arange(256).reshape((16, 16))

im = plt.imshow(arr, interpolation="none")

plt.colorbar(im)

plt.tight_layout()

#第三張圖
plt.subplot(233)

from mpl_toolkits.axes_grid1 import make_axes_locatable

arr = np.arange(256).reshape((16, 16))
im = plt.imshow(arr, interpolation="none")

divider = make_axes_locatable(plt.gca())
cax = divider.append_axes("right", "5%", pad="3%")
plt.colorbar(im, cax=cax)

plt.tight_layout()


#第四張圖
plt.subplot(234)


img = np.array([[0, 1, 2, 3],
                [4, 5, 6, 7],
                [8, 9 , 10, 11],
                [12, 13, 14, 15]])
                
plt.imshow(img, cmap='Blues')
plt.colorbar()


#第五張圖
plt.subplot(235)



#第六張圖
plt.subplot(236)




plt.show()


