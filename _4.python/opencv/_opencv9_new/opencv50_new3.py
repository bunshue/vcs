"""
opencv 集合

"""

import cv2

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

plt.figure(num = '將一圖分解成 藍 綠 紅 三通道', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

#filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/rgb256X300.bmp'
#filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/rgb512.bmp'
#filename = 'C:/_git/vcs/_1.data/______test_files1/ims01.jpg'

cut = 50
num_bins = 50  # 直方圖顯示時的束數


filename = 'p1.bmp'

image = cv2.imread(filename)

b, g, r = cv2.split(image)


bb = b[cut:(480-cut*2), cut:(640-cut*2)]
#plt.imshow(cv2.cvtColor(bb, cv2.COLOR_BGR2RGB))
#plt.show()

bbb = bb.reshape(bb.shape[0]*bb.shape[1], 1)
#print(bbb.shape)
plt.hist(bbb, num_bins, color="b", alpha = 0.5)  #alpha調整透明度 給多個直方圖畫在一起用

gg = g[cut:(480-cut*2), cut:(640-cut*2)]
#plt.imshow(cv2.cvtColor(gg, cv2.COLOR_BGR2RGB))
#plt.show()

ggg = gg.reshape(gg.shape[0]*gg.shape[1], 1)
#print(ggg.shape)
plt.hist(ggg, num_bins, color="g", alpha = 0.5)  #alpha調整透明度 給多個直方圖畫在一起用

rr = r[cut:(480-cut*2), cut:(640-cut*2)]
#plt.imshow(cv2.cvtColor(rr, cv2.COLOR_BGR2RGB))
#plt.show()

rrr = rr.reshape(rr.shape[0]*rr.shape[1], 1)
#print(rrr.shape)
rrr = rrr[0:len(rrr):5]
plt.hist(rrr, num_bins, color="r", alpha = 0.5)  #alpha調整透明度 給多個直方圖畫在一起用


filename = 'p2.bmp'

image = cv2.imread(filename)

b, g, r = cv2.split(image)


bb = b[cut:(480-cut*2), cut:(640-cut*2)]
#plt.imshow(cv2.cvtColor(bb, cv2.COLOR_BGR2RGB))
#plt.show()

bbb = bb.reshape(bb.shape[0]*bb.shape[1], 1)
#print(bbb.shape)
plt.hist(bbb, num_bins, color="b", alpha = 0.5)  #alpha調整透明度 給多個直方圖畫在一起用

gg = g[cut:(480-cut*2), cut:(640-cut*2)]
#plt.imshow(cv2.cvtColor(gg, cv2.COLOR_BGR2RGB))
#plt.show()

ggg = gg.reshape(gg.shape[0]*gg.shape[1], 1)
#print(ggg.shape)
plt.hist(ggg, num_bins, color="g", alpha = 0.5)  #alpha調整透明度 給多個直方圖畫在一起用

rr = r[cut:(480-cut*2), cut:(640-cut*2)]
#plt.imshow(cv2.cvtColor(rr, cv2.COLOR_BGR2RGB))
#plt.show()

rrr = rr.reshape(rr.shape[0]*rr.shape[1], 1)
#print(rrr.shape)
rrr = rrr[0:len(rrr):5]
plt.hist(rrr, num_bins, color="r", alpha = 0.5)  #alpha調整透明度 給多個直方圖畫在一起用




plt.show()

sys.exit()



plt.show()




sys.exit()




print(g.shape)
#print(g)

print(r.shape)
#print(r)

print('顯示 ch2 紅 通道 圖')
plt.subplot(234)
plt.imshow(cv2.cvtColor(r, cv2.COLOR_BGR2RGB))
plt.title('紅 第2通道')

print('顯示 ch1 綠 通道 圖')
plt.subplot(235)
plt.imshow(cv2.cvtColor(g, cv2.COLOR_BGR2RGB))
plt.title('綠 第1通道')

print('顯示 ch0 藍 通道 圖')
plt.subplot(236)
plt.imshow(cv2.cvtColor(b, cv2.COLOR_BGR2RGB))
plt.title('藍  第0通道')


#plt.show()


print('------------------------------------------------------------')	#60個

import math

filename = 'p1.bmp'
image1 = cv2.imread(filename)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.show()


filename = 'p2.bmp'
image2 = cv2.imread(filename)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.show()


#image3 = math.fabs(image1-image2)
image3 = image1-image2

plt.imshow(cv2.cvtColor(image3, cv2.COLOR_BGR2RGB))
plt.show()





print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個


