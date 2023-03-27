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

#第一張圖
plt.subplot(231)


from pylab import *
from numpy import NaN

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
	return NaN

X = arange(xmin, xmax + res, res)
Y = arange(ymin, ymax + res, res)
Z = zeros((len(Y), len(X)))

for iy, y in enumerate(Y):
	#print (iy + 1, "of", len(Y))
	for ix, x in enumerate(X):
		Z[-iy - 1, ix] = m(x + 1j * y)

save("mandel", Z)	# save array to file

imshow(Z, cmap = plt.cm.prism, interpolation = 'none',
  extent = (X.min(), X.max(), Y.min(), Y.max()))
xlabel("Re(c)")
ylabel("Im(c)")


#第二張圖
plt.subplot(232)



#第三張圖
plt.subplot(233)



#第四張圖
plt.subplot(234)



#第五張圖
plt.subplot(235)



#第六張圖
plt.subplot(236)



plt.show()
