# imshow 集合

selected_font = 'C:/_git/vcs/_4.cmpp/_python_test/data/msch.ttf'

import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from PIL import Image

#plt.figure(figsize=(8,8))	#設定圖片視窗大小
plt.figure(num = 'imshow 集合 3', figsize=[20, 15], dpi=84, facecolor="whitesmoke", edgecolor="r", linewidth=1, frameon=True)
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示


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
filename = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/image.svg'
fig.savefig(filename)
print('已存圖' + filename)
'''

#第二張圖
plt.subplot(232)

#Layer Images

import matplotlib.pyplot as plt
import numpy as np

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




#第四~五張圖

# Subplots spacings and margins
import matplotlib.pyplot as plt
import numpy as np

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

