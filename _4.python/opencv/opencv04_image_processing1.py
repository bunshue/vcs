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

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg'
#filename = 'C:/_git/vcs/_1.data/______test_files1/ims01.bmp'

print('------------------------------------------------------------')	#60個
'''
#影像對比與亮度調整
import matplotlib.image as img

# output_image = alpha * imput_image + beta
def modify_contrast_and_brightness(image, alpha=1.0, beta = 0.0):
    array_alpha = np.array([alpha]) #對比度
    array_beta = np.array([beta]) #亮度
    image = cv2.add(image, array_beta)
    image = cv2.multiply(image, array_alpha)
    image = np.clip(image, 0, 255)
    return image

plt.figure(num = '影像對比與亮度調整', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)
image = cv2.imread(filename)	#讀取本機圖片
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('原圖')

modified_image = modify_contrast_and_brightness(image, 1.5, 10.0)
plt.subplot(122)
plt.imshow(cv2.cvtColor(modified_image, cv2.COLOR_BGR2RGB))
plt.title('影像對比與亮度調整')

plt.show()

print('------------------------------------------------------------')	#60個

plt.figure(num = '影像分析工具 影像直方圖', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

#影像分析工具
#影像直方圖

image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)	#讀取本機圖片, 直接轉成灰階

plt.subplot(221)
plt.hist(image.ravel(), 256, [0,256])
plt.title('原圖轉灰階')

plt.subplot(222)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('影像直方圖')

print('------------------------------------------------------------')	#60個

#直方圖影像操作
#直方圖均值化

import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)	#讀取本機圖片, 直接轉成灰階
equa = cv2.equalizeHist(image)

plt.subplot(223)
plt.hist(equa.ravel(), 256, [0,256])
plt.title('原圖轉灰階')

#均值化的影像
#均衡化後的灰度直方圖分布
plt.subplot(224)
plt.imshow(cv2.cvtColor(equa, cv2.COLOR_BGR2RGB))
plt.title('均衡化後的灰度直方圖分布')

plt.show()

'''
print('------------------------------------------------------------')	#60個

plt.figure(num = '將一圖分解成 藍 綠 紅 三通道', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

#filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/rgb256X300.bmp'
filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/rgb512.bmp'

image = cv2.imread(filename)

plt.subplot(331)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('原圖')

"""same
b=image[:,:,0]
g=image[:,:,1]
r=image[:,:,2]
"""

b, g, r = cv2.split(image)

print(image.shape)
#print(image)

print(b.shape)
#print(b)

print(g.shape)
#print(g)

print(r.shape)
#print(r)

print('顯示 ch2 紅 通道 圖')
plt.subplot(334)
plt.imshow(cv2.cvtColor(r, cv2.COLOR_BGR2RGB))
plt.title('紅 第2通道')

print('顯示 ch1 綠 通道 圖')
plt.subplot(335)
plt.imshow(cv2.cvtColor(g, cv2.COLOR_BGR2RGB))
plt.title('綠 第1通道')

print('顯示 ch0 藍 通道 圖')
plt.subplot(336)
plt.imshow(cv2.cvtColor(b, cv2.COLOR_BGR2RGB))
plt.title('藍  第0通道')

print('設定第2通道為0')
image[:,:,2]=0
plt.subplot(337)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('設定第2通道為0')

print('再設定第1通道為0')
image[:,:,1]=0
plt.subplot(338)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('再設定第1通道為0')

print('再設定第0通道為0')
image[:,:,0]=0
plt.subplot(339)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('再設定第0通道為0')

plt.show()

print('------------------------------------------------------------')	#60個

plt.figure(num = '將一圖分解成 藍 綠 紅 三通道', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png'
filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/rgb256X300.bmp'
filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/rgb512.bmp'

image = cv2.imread(filename)

b, g, r = cv2.split(image)

bgr = cv2.merge([b, g, r])
rgb = cv2.merge([r, g, b])

plt.subplot(231)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('原圖')
plt.subplot(232)
plt.imshow(cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB))    #照BGR排列 OK
plt.title('B-G-R OK')
plt.subplot(233)
plt.imshow(cv2.cvtColor(rgb, cv2.COLOR_BGR2RGB))    #照RGB排列 錯相
plt.title('R-G-B NG')

plt.subplot(234)
plt.imshow(cv2.cvtColor(r, cv2.COLOR_BGR2RGB))
plt.title('R分量')
plt.subplot(235)
plt.imshow(cv2.cvtColor(g, cv2.COLOR_BGR2RGB))
plt.title('G分量')
plt.subplot(236)
plt.imshow(cv2.cvtColor(b, cv2.COLOR_BGR2RGB))
plt.title('B分量')

plt.show()

sys.exit()

print('------------------------------------------------------------')	#60個
print('測試 2')

img = cv2.imread('images/girl.bmp')
imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.figure(num = '顯示結果', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

plt.subplot(121)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('原圖BGR OK')

plt.subplot(122)
plt.imshow(cv2.cvtColor(imgRGB, cv2.COLOR_BGR2RGB))
plt.title('原圖RGB NG')

plt.show()

print('------------------------------------------------------------')	#60個

plt.figure(num = '灰度圖像顯示演示', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

o = cv2.imread('images/8.bmp')
g = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)

plt.subplot(221)
plt.imshow(cv2.cvtColor(g, cv2.COLOR_BGR2RGB), cmap = plt.cm.gray)

plt.subplot(222)
plt.imshow(cv2.cvtColor(g, cv2.COLOR_BGR2RGB), cmap = plt.cm.gray_r)

plt.subplot(223)
plt.imshow(cv2.cvtColor(g, cv2.COLOR_BGR2RGB), cmap = 'gray')

plt.subplot(224)
plt.imshow(cv2.cvtColor(g, cv2.COLOR_BGR2RGB), cmap = 'gray_r')

plt.show()

print('------------------------------------------------------------')	#60個

plt.figure(num = '灰度圖像顯示演示', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

o = cv2.imread('images/girl.bmp')
g = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)

plt.figure("灰度圖像顯示演示")
plt.subplot(221)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))

plt.subplot(222)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB), cmap = plt.cm.gray)

plt.subplot(223)
plt.imshow(cv2.cvtColor(g, cv2.COLOR_BGR2RGB))

plt.subplot(224)
plt.imshow(cv2.cvtColor(g, cv2.COLOR_BGR2RGB), cmap = plt.cm.gray)

plt.show()

print('------------------------------------------------------------')	#60個

print('測試 5')

o = cv2.imread("images/boat.bmp")
plt.hist(o.ravel(), 16)

plt.show()

print('------------------------------------------------------------')	#60個

print('測試 6')
o = cv2.imread("images/boat.jpg")
cv2.imshow("original", o)    #有cv2.imshow的, 要對應destroyAllWindows()
cv2.waitKey()
cv2.destroyAllWindows()

plt.hist(o.ravel(), 256)
plt.show()

print('------------------------------------------------------------')	#60個

print('測試 7')

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
img = cv2.imread(filename)
hist = cv2.calcHist([img], [0], None, [256], [0, 255])
print(type(hist))
print(hist.shape)
print(hist.size)
print(hist)
plt.plot(hist)

plt.show()

print('------------------------------------------------------------')	#60個

print('測試 8')

#-----------讀取原始圖像---------------
img = cv2.imread('images/equ.bmp',cv2.IMREAD_GRAYSCALE)
#-----------直方圖均衡化處理---------------
equ = cv2.equalizeHist(img)
#-----------顯示均衡化前后的直方圖---------------
cv2.imshow("original", img)  #有cv2.imshow的, 要對應destroyAllWindows()
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imshow("result", equ)    #有cv2.imshow的, 要對應destroyAllWindows()
cv2.waitKey()
cv2.destroyAllWindows()
#-----------顯示均衡化前后的直方圖---------------
plt.figure("原始圖像直方圖")  #構建窗口
plt.hist(img.ravel(), 256)
plt.figure("均衡化結果直方圖")  #構建新窗口
plt.hist(equ.ravel(), 256)

plt.show()

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個
print('測試 9')

image = cv2.imread("images/girl.bmp", cv2.IMREAD_GRAYSCALE)
mask = np.zeros(image.shape, np.uint8)
mask[200 : 400, 200 : 400] = 255
histImage = cv2.calcHist([image], [0], None, [256], [0, 255])
histMI = cv2.calcHist([image], [0], mask, [256],[0, 255])
plt.plot(histImage)
plt.plot(histMI)

plt.show()

print('------------------------------------------------------------')	#60個
print('測試 10')

o = cv2.imread("images/boatGray.bmp")
histb = cv2.calcHist([o], [0], None, [256], [0, 255])
plt.plot(histb, color = 'b')

plt.show()

print('------------------------------------------------------------')	#60個
print('測試 11')

o = cv2.imread("images/girl.bmp")
histb = cv2.calcHist([o], [0], None, [256], [0, 255])
histg = cv2.calcHist([o], [1], None, [256], [0, 255])
histr = cv2.calcHist([o], [2], None, [256], [0, 255])
plt.plot(histb, color = 'b')
plt.plot(histg, color = 'g')
plt.plot(histr, color = 'r')

plt.show()

print('------------------------------------------------------------')	#60個

plt.figure(num = 'subplot示例', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

img = cv2.imread('images/equ.bmp', cv2.IMREAD_GRAYSCALE)
equ = cv2.equalizeHist(img)

plt.subplot(121)
plt.hist(img.ravel(), 256)

plt.subplot(122)
plt.hist(equ.ravel(), 256)

plt.show()

print('------------------------------------------------------------')	#60個

"""
https://blog.gtwang.org/programming/python-opencv-matplotlib-plot-histogram-tutorial/
https://docs.opencv.org/3.1.0/d1/db7/tutorial_py_histogram_begins.html
"""

#filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg'
filename = 'C:/_git/vcs/_1.data/______test_files1/ims01.bmp'

print('------------------------------------------------------------')	#60個

image = cv2.imread(filename)	#讀取本機圖片

# 轉為灰階圖片
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 計算直方圖每個 bin 的數值
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

# 畫出直方圖
#plt.bar(range(1, 255), hist)

# 畫出分佈圖
plt.plot(hist)

# 使用 ravel 將所有的像素資料轉為一維的陣列，以下是一個簡單的範例：
# 畫出直方圖
#plt.hist(gray.ravel(), 256, [0, 256])

plt.show()

print('------------------------------------------------------------')	#60個

#對於彩色的圖片，
#可以用 OpenCV 的 calcHist 函數分別計算統計值，
#並畫出 RGB 三種顏色的分佈圖：

image = cv2.imread(filename)	#讀取本機圖片

# 畫出 RGB 三種顏色的分佈圖
color = ('b', 'g', 'r')
for i, col in enumerate(color):
  histr = cv2.calcHist([image], [i], None, [256], [0, 256])
  plt.plot(histr, color = col)
  plt.xlim([0, 256])
plt.show()

print('------------------------------------------------------------')	#60個

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

print('------------------------------------------------------------')	#60個


