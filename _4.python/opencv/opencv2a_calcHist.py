"""

用直方圖分析一張圖片的顏色組成


"""

"""

hist = cv2.calcHist(img, channels, mask, histSize, ranges, accumulate) 函數統計直方圖
參數都要加［］括起來
img：原圖像
channels：如果輸入的圖像是灰度圖，它的值就是[0]，如果是彩色圖像，傳入的參數可以是[0]、[1]、[2],分布對應著b,g,r。
mask：掩膜圖像。要統計整幅圖像的直方圖就把這個參數設為None，如果要統計掩膜部分的圖像的直方圖，就需要這個參數。
histSize：bins的個數,就是分多少個組距。例如[256]或者[16]，都要用方括號括起來。
ranges：像素值范圍，通常為[0, 256]
accumulate：累計(累積、疊加)標識，默認值是False。
這個函數返回的對象hist是一個一維數組，數組內的元素是各個灰度級的像素個數。


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



'''
#對於彩色的圖片，
#可以用 OpenCV 的 calcHist 函數分別計算統計值，
#並畫出 RGB 三種顏色的分佈圖：

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'
filename = 'pic.bmp'

image = cv2.imread(filename)	#讀取本機圖片

# 計算直方圖每個 bin 的數值
hist_b = cv2.calcHist([image], [0], None, [256], [0, 256])
hist_g = cv2.calcHist([image], [1], None, [256], [0, 256])
hist_r = cv2.calcHist([image], [2], None, [256], [0, 256])

# RGB畫在一起
# 使用 ravel 將所有的像素資料轉為一維的陣列
# 畫出直方圖
num_bins = 64  # 直方圖顯示時的束數
plt.hist(image.ravel(), 64, [0, 256], color="gray")
#plt.hist(image.ravel(), bins = num_bins, color="lime", alpha = 0.3, density=False)

# RGB分開畫
# 畫出 RGB 三種顏色的分佈圖
plt.plot(hist_r, color = 'r')
plt.plot(hist_g, color = 'g')
plt.plot(hist_b, color = 'b')

plt.xlim([0 - 10, 256 + 10])

plt.show()
'''

print('測試 14------------------------------------------------------------')	#60個

filename = 'data/pic_brightness1.bmp'

image = cv2.imread(filename)
print(image.shape)

histb = cv2.calcHist([image], [0], None, [256], [0, 256])
histg = cv2.calcHist([image], [1], None, [256], [0, 256])
histr = cv2.calcHist([image], [2], None, [256], [0, 256])

plt.plot(histb, 'r', label="b1")
plt.plot(histg, 'r', label="g1")
plt.plot(histr, 'r', label="r1")

filename = 'data/pic_brightness2.bmp'

image = cv2.imread(filename)
print(image.shape)

histb = cv2.calcHist([image], [0], None, [256], [0, 256])
histg = cv2.calcHist([image], [1], None, [256], [0, 256])
histr = cv2.calcHist([image], [2], None, [256], [0, 256])

plt.plot(histb, 'g', label="b2")
plt.plot(histg, 'g', label="g2")
plt.plot(histr, 'g', label="r2")



filename = 'data/pic_brightness3.bmp'

image = cv2.imread(filename)
print(image.shape)

histb = cv2.calcHist([image], [0], None, [256], [0, 256])
histg = cv2.calcHist([image], [1], None, [256], [0, 256])
histr = cv2.calcHist([image], [2], None, [256], [0, 256])

plt.plot(histb, 'b', label="b3")
plt.plot(histg, 'b', label="g3")
plt.plot(histr, 'b', label="r3")

plt.legend(loc="best")
plt.xlim([0 - 10, 256 + 10])
plt.ylim([0, 4000])



plt.show()

print('測試 11------------------------------------------------------------')	#60個

print('使用mask, 因為目前mask只能用1維的 所以圖片要先轉成灰階')

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'
filename = 'C:/_git/vcs/_1.data/______test_files1/ims01.bmp'
filename = 'data/pic_brightness1.bmp'

image = cv2.imread(filename)
print(image.shape)


image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
print(image.shape)

mask = np.zeros(image.shape, np.uint8)
print(image.shape)
print(mask.shape)
H = image.shape[0]
W = image.shape[1]
border = 20

mask[border : H - border * 2, border : W - border * 2] = 255

#全圖
hist1 = cv2.calcHist([image], [0], None, [256], [0, 256])

#部分圖
hist2 = cv2.calcHist([image], [0], mask, [256], [0, 256])

plt.plot(hist1, 'r', label="全圖")
plt.plot(hist2, 'g', label="部分圖")

plt.legend(loc="best")

plt.show()

print('測試 16------------------------------------------------------------')	#60個

plt.figure(num = '配合圖形遮罩計算直方圖', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

image = cv2.imread(filename)	#讀取本機圖片

# 轉為灰階圖片
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 建立圖形遮罩
mask = np.zeros(gray.shape, np.uint8)
#mask[300:780, 300:1620] = 255
W = 640
H = 480
x_st = int(W / 4)
y_st = int(H / 4)
w = int(W / 2)
h = int(H / 2)

mask[y_st : y_st + h, x_st : x_st + w] = 255    #先h 後 w
#mask[0:240, 0:320] = 255

# 計算套用遮罩後的圖形
masked_gray = cv2.bitwise_and(gray, gray, mask = mask)

# 以原圖計算直方圖
hist_full = cv2.calcHist([image], [0], None, [256], [0, 256])

# 以套用遮罩後的圖計算直方圖
hist_mask = cv2.calcHist([image], [0], mask, [256], [0, 256])

# 繪製結果
plt.subplot(221)
plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB), 'gray')

plt.subplot(222)
plt.imshow(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB), 'gray')

plt.subplot(223)
plt.imshow(cv2.cvtColor(masked_gray, cv2.COLOR_BGR2RGB), 'gray')

plt.subplot(224)
plt.plot(hist_full)
plt.plot(hist_mask)
plt.xlim([0,256])

plt.show()


print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



