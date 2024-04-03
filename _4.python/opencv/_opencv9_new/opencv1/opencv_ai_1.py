"""
一本精通：OpenCV 與 AI 影像辨識

logo_filename = 'C:/_git/vcs/_4.python/opencv/data/opencv_logo.png'

"""

print("------------------------------------------------------------")  # 60個

import cv2
import time

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_01")

img = cv2.imread(filename)   # 預設為彩色 1號
img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # 灰階 2號
img = cv2.imread(filename, 2) # 也可使用數字代表模式
print(img.shape)            # 得到 shape
print(img.dtype)            # uint8

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()

"""
img1 = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
img2 = cv2.imread('test.png', cv2.IMREAD_UNCHANGED)
print(img1.shape)    # (400, 300, 3)  JPG 只有三個色版 BGR
print(img2.shape)    # (400, 300, 4)  PNG 四個色版 GRA

img = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)  # 轉換成 BGRA 色彩模式
print(img.shape)                             # (400, 300, 4)  第三個數值變成 4
"""

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_02")

img = cv2.imread(filename)
b, g, r = cv2.split(img)
#print(b)
#print(g)
#print(r)

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_03")

img_blue = cv2.imread(filename)
img_green = cv2.imread(filename)
img_red = cv2.imread(filename)
img_blue[:,:,1] = 0    # 將綠色設為 0
img_blue[:,:,2] = 0    # 將紅色設為 0
img_green[:,:,0] = 0   # 將藍色設為 0
img_green[:,:,2] = 0   # 將紅色設為 0
img_red[:,:,0] = 0     # 將藍色設為 0
img_red[:,:,1] = 0     # 將綠色設為 0

cv2.imshow('image blue', img_blue)
cv2.imshow('image green', img_green)
cv2.imshow('image red', img_red)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_04")

img = cv2.imread(filename)
print('原圖為彩色')
cv2.imshow('image1', img)
print('彩色轉灰階')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 轉換成灰階影像
cv2.imshow('image2', img)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_05")

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

print('像素操作 底片效果')

img = cv2.imread(filename)
rows = img.shape[0]     # 取得高度的總像素
cols = img.shape[1]     # 取得寬度的總像素

for row in range(int(rows/2)):  # 只取 rows 的一半 ( 使用 int 取整數 )
    for col in range(cols):
        img[row, col, 0] = 255 - img[row, col, 0]   # 255 - 藍色
        img[row, col, 1] = 255 - img[row, col, 1]   # 255 - 綠色
        img[row, col, 2] = 255 - img[row, col, 2]   # 255 - 紅色

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_06")

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

img = cv2.imread(filename)

img = 255-img # 使用 255 減去陣列中所有數值

cv2.imshow('image invert', img)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_07")

img = cv2.imread(filename)

contrast = 200
brightness = 0
output = img * (contrast/127 + 1) - contrast + brightness # 轉換公式
# 轉換公式參考 https://stackoverflow.com/questions/50474302/how-do-i-adjust-brightness-contrast-and-vibrance-with-opencv-python

# 調整後的數值大多為浮點數，且可能會小於 0 或大於 255
# 為了保持像素色彩區間為 0～255 的整數，所以再使用 np.clip() 和 np.uint8() 進行轉換
output = np.clip(output, 0, 255)
output = np.uint8(output)

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_08")

img = cv2.imread(filename)
output = img    # 建立 output 變數

alpha = 1
beta = 10

cv2.convertScaleAbs(img, output, alpha, beta)  # 套用 convertScaleAbs

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_09")

img = cv2.imread(filename)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY); # 轉換前，都先將圖片轉換成灰階色彩
ret, output1 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)     # 如果大於 127 就等於 255，反之等於 0。
ret, output2 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV) # 如果大於 127 就等於 0，反之等於 255。
ret, output3 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TRUNC)      # 如果大於 127 就等於 127，反之數值不變。
ret, output4 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TOZERO)     # 如果大於 127 數值不變，反之數值等於 0。
ret, output5 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TOZERO_INV) # 如果大於 127 等於 0，反之數值不變。

cv2.imshow('image', img)
cv2.imshow('image1', output1)
cv2.imshow('image2', output2)
cv2.imshow('image3', output3)
cv2.imshow('image4', output4)
cv2.imshow('image5', output5)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_10")

img = cv2.imread(filename)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY); # 轉換前，都先將圖片轉換成灰階色彩
ret, output1 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
output2 = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
output3 = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imshow('image', img)
cv2.imshow('image1', output1)
cv2.imshow('image2', output2)
cv2.imshow('image3', output3)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_11")

"""
img_red = cv2.imread('test-red.png')
img_green = cv2.imread('test-green.png')
img_blue = cv2.imread('test-blue.png')

output = cv2.add(img_red, img_green)  # 疊加紅色和綠色
output = cv2.add(output, img_blue)    # 疊加藍色

cv2.imshow('image', output)
cv2.waitKey()
cv2.destroyAllWindows()
"""

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_12")

logo_filename = 'C:/_git/vcs/_4.python/opencv/data/opencv_logo.png'

""" addWeighted
img = cv2.imread(filename)
logo = cv2.imread(logo_filename)
output = cv2.addWeighted(img, 0.5, logo, 0.3, 50)

cv2.imshow('image', output)
cv2.waitKey()
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_13")

"""
print("兩圖相減")
img = cv2.imread('test.png')
img2 = cv2.imread('test2.png')
output = cv2.subtract(img, img2)  # 相減
cv2.waitKey(0)       # 按下任意鍵停止
cv2.destroyAllWindows()
"""

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_14")

w, h = 400, 400
img1 = np.zeros([h,w,3])
for i in range(h):
    img[i,:,1] = int(256*i/400)   # 從上往下填入綠色漸層

img = img.astype('float32')/255   # 轉換內容類型

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_15")

w = 400
h = 400
img = np.zeros([h,w,3])
for i in range(h):
    for j in range(w):
        img[i,j,0] = int(256*(j+i)/(w+h))
        img[i,j,2] = int(256*(j+i)/(w+h))

img = img.astype('float32')/255

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_16")

w = 400
h = 400
img = np.zeros([h,w,4])             # 第三個值為 4
for i in range(h):
    img[i,:,3] = int(256*i/400)     # 設定第四個值 ( 透明度 )

img = img.astype('float32')/255

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_17")

logo_filename = 'C:/_git/vcs/_4.python/opencv/data/opencv_logo.png'

"""
img = cv2.imread(logo_filename, cv2.IMREAD_UNCHANGED)  # 開啟圖片
img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)         # 因為是 jpg，要轉換顏色為 BGRA
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)        # 新增 gray 變數為轉換成灰階的圖片

h = img.shape[0]     # 取得圖片高度
w = img.shape[1]     # 取得圖片寬度

# 依序取出圖片中每個像素
for x in range(w):
    for y in range(h):
        if gray[y, x]>200:
            img[y, x, 3] = 255 - gray[y, x]
            # 如果該像素的灰階度大於 200，調整該像素的透明度
            # 使用 255 - gray[y, x] 可以將一些邊緣的像素變成半透明，避免太過鋸齒的邊緣

cv2.waitKey(0)                        # 按下任意鍵停止
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_18")

logo_filename = 'C:/_git/vcs/_4.python/opencv/data/opencv_logo.png'

img = cv2.imread(logo_filename, cv2.IMREAD_UNCHANGED)
img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

h = img.shape[0]
w = img.shape[1]

for x in range(w):
    for y in range(h):
        if gray[y, x]>200:
            img[y, x] = [0,255,255,255]  # 換成黃色

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_19")

bg = cv2.imread('bg.jpg', cv2.IMREAD_UNCHANGED)     # 開啟背景圖
bg = cv2.cvtColor(bg, cv2.COLOR_BGR2BGRA)           # 轉換成 BGRA

img = cv2.imread('goku.jpg', cv2.IMREAD_UNCHANGED)  # 開啟悟空公仔圖
img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)         # 轉換成 BGRA

h = img.shape[0]           # 取得圖片高度
w = img.shape[1]           # 取得圖片寬度

for x in range(w):
    for y in range(h):
        r = img[y, x, 2]   # 取得該像素的紅色值
        g = img[y, x, 1]   # 取得該像素的綠色值
        b = img[y, x, 0]   # 取得該像素的藍色值
        if r>20 and r<80 and g<190 and g>110 and b<150 and b>60:
            img[y, x] = bg[y, x]   # 如果在範圍內的顏色，換成背景圖的像素值

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_20")

img = cv2.imread('japan.jpeg')

def floodFill(source, mask, seedPoint, newVal, loDiff, upDiff, flags=cv2.FLOODFILL_FIXED_RANGE):
    result = source.copy()
    cv2.floodFill(result, mask=mask, seedPoint=seedPoint, newVal=newVal, loDiff=loDiff, upDiff=upDiff, flags=flags)
    return result

h, w = img.shape[:2]                     # 取得原始影像的長寬
mask = np.zeros((h+2,w+2,1), np.uint8)   # 製作 mask，長寬都要加上 2
output = floodFill(img, mask, (100,10), (0,0,255), (100,100,60), (100,100,100))

cv2.imshow('image', output)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_21")

img = cv2.imread('japan.jpeg')

def floodFill(source, mask, seedPoint, newVal, loDiff, upDiff, flags=cv2.FLOODFILL_FIXED_RANGE):
    result = source.copy()
    cv2.floodFill(result, mask=mask, seedPoint=seedPoint, newVal=newVal, loDiff=loDiff, upDiff=upDiff, flags=flags)
    return result

h, w = img.shape[:2]
mask = np.zeros((h+2,w+2,1), np.uint8)  # 全黑遮罩
mask = 255 - mask                       # 變成全白遮罩
mask[0:100,0:200] = 0                   # 江左上角長方形變成黑色
output = floodFill(img, mask, (100,10), (0,0,255), (100,100,60), (200,200,200))

cv2.imshow('image', output)
cv2.waitKey()
cv2.destroyAllWindows()
"""

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_22")

img = cv2.imread(filename)
output1 = cv2.bilateralFilter(img, 50, 0, 0)
output2 = cv2.bilateralFilter(img, 50, 50, 100)
output3 = cv2.bilateralFilter(img, 50, 100, 1000)
cv2.imshow('image1', output1)
cv2.imshow('image2', output2)
cv2.imshow('image3', output3)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_23")

def convex(src_img, raw, effect):
    col, row, channel = raw[:]      # 取得圖片資訊
    cx, cy, r = effect[:]           # 取得凸透鏡的範圍
    output = np.zeros([row, col, channel], dtype = np.uint8)        # 產生空白畫布
    for y in range(row):
        for x in range(col):
            d = ((x - cx) * (x - cx) + (y - cy) * (y - cy)) ** 0.5  # 計算每個點與中心點的距離
            if d <= r:
                nx = int((x - cx) * d / r + cx)        # 根據不同的位置，產生新的 nx，越靠近中心形變越大
                ny = int((y - cy) * d / r + cy)        # 根據不同的位置，產生新的 ny，越靠近中心形變越大
                output[y, x, :] = src_img[ny, nx, :]   # 產生新的圖
            else:
                output[y, x, :] = src_img[y, x, :]     # 如果在半徑範圍之外，原封不動複製過去
    return output

img = cv2.imread(filename)
img = convex(img, (300, 400, 3), (150, 130, 100))      # 提交參數數值，進行凸透鏡效果

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_24")

img = cv2.imread(filename)                         # 開啟圖片
img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)          # 轉換成 BGRA ( 因為需要 alpha 色版 )
w = img.shape[1]                                     # 取得寬度
h = img.shape[0]                                     # 取得高度
white = 255 - np.zeros((h,w,4), dtype='uint8')       # 建立白色圖
a = 1                                                # 一開始 a 為 1
while True:
    a = a - 0.01                                     # a 不斷減少 0.01
    if a<0: a = 0                                    # 如果 a 小於 0 就讓 a 等於 0
    output = cv2.addWeighted(white, a, img, 1-a, 0)  # 根據 a 套用權重
    cv2.imshow('image', output)                 # 顯示圖片
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_25")

img = cv2.imread(filename)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 轉成灰階
img = cv2.medianBlur(img, 7)                 # 模糊化，去除雜訊
output = cv2.Laplacian(img, -1, 1, 5)        # 偵測邊緣

cv2.imshow('image', output)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_26")

img = cv2.imread(filename)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 轉成灰階
img = cv2.medianBlur(img, 7)                 # 模糊化，去除雜訊
output = cv2.Sobel(img, -1, 1, 1, 1, 7)      # 偵測邊緣

cv2.imshow('image', output)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_27")

img = cv2.imread(filename)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 轉成灰階
img = cv2.medianBlur(img, 7)                 # 模糊化，去除雜訊
output = cv2.Canny(img, 36, 36)              # 偵測邊緣
print(output)

cv2.imshow('image', output)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_28")

img = cv2.imread(filename)
cv2.imshow('image1', img)   # 原始影像

img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))

img = cv2.erode(img, kernel)     # 先侵蝕，將白色小圓點移除
cv2.imshow('image2', img)   # 侵蝕後的影像

img = cv2.dilate(img, kernel)    # 再膨脹，白色小點消失
cv2.imshow('image3', img)   # 膨脹後的影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_29")

"""fail
logo_filename = 'C:/_git/vcs/_4.python/opencv/data/opencv_logo.png'

logo = cv2.imread(logo_filename)                    # 讀取 OpenCV 的 logo
size = logo.shape                                # 讀取 logo 的長寬尺寸

img = np.zeros((360,480,3), dtype='uint8')       # 產生一張 480x360 背景全黑的圖
img[0:360, 0:480] = '255'                        # 將圖片變成白色 ( 配合 logo 是白色底 )
img[0:size[0], 0:size[1]] = logo                 # 將圖片的指定區域，換成 logo 的圖案
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 產生一張灰階的圖片作為遮罩使用
ret, mask1  = cv2.threshold(img_gray, 200, 255, cv2.THRESH_BINARY_INV)  # 使用二值化的方法，產生黑白遮罩圖片
logo = cv2.bitwise_and(img, img, mask = mask1 )  # logo 套用遮罩

bg = cv2.imread(filename)                      # 讀取底圖
ret, mask2  = cv2.threshold(img_gray, 200, 255, cv2.THRESH_BINARY)      # 使用二值化的方法，產生黑白遮罩圖片
bg = cv2.bitwise_and(bg, bg, mask = mask2 )      # 底圖套用遮罩

output = cv2.add(bg, logo)                       # 使用 add 方法將底圖和 logo 合併

cv2.imshow('image', output)

cv2.waitKey()
cv2.destroyAllWindows()

"""
print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_30")

mask = np.zeros((300,300,3), dtype='uint8')      # 建立 300x300 的黑色畫布
cv2.circle(mask,(150,150),100,(255,255,255),-1)  # 在畫布上中心點加入一個半徑 100 的白色圓形
mask = cv2.GaussianBlur(mask, (35, 35), 0)       # 進行高斯模糊

cv2.imshow('image', mask)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_31")

"""fail
mask = np.zeros((300,300,3), dtype='uint8')
cv2.circle(mask,(150,150),100,(255,255,255),-1)
mask = cv2.GaussianBlur(mask, (35, 35), 0)
mask = mask / 255                          # 除以 255，計算每個像素的黑白色彩在 255 中所佔的比例

img = cv2.imread(filename)               # 開啟圖片
bg = np.zeros((300,300,3), dtype='uint8')  # 產生一張黑色背景
bg = 255 - bg                              # 轉換成白色背景
img = img / 255                            # 除以 255，計算每個像素的色彩在 255 中所佔的比例
bg = bg / 255                              # 除以 255，計算每個像素的色彩在 255 中所佔的比例

out  = bg * (1 - mask) + img * mask        # 根據比例混合
out = (out * 255).astype('uint8')          # 乘以 255 之後轉換成整數

cv2.imshow('image',out)
cv2.waitKey()
cv2.destroyAllWindows()
"""

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_32")

filename1 = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg"
filename2 = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"

img1 = cv2.imread(filename1)
img2 = cv2.imread(filename2)
w = img1.shape[1]   # 讀取圖片寬度
h = img1.shape[0]   # 讀取圖片高度

for i in range(w):
    img1[:,i,0] = img1[:,i,0]*((300-i)/300) + img2[:,i,0]*(i/300)  # 藍色按照比例混合
    img1[:,i,1] = img1[:,i,1]*((300-i)/300) + img2[:,i,1]*(i/300)  # 紅色按照比例混合
    img1[:,i,2] = img1[:,i,2]*((300-i)/300) + img2[:,i,2]*(i/300)  # 綠色按照比例混合

#cv2.imwrite('tmp_image.png', img1)

show = img1.astype('float32')/255    # 如果要使用 imshow 必須要轉換類型
#cv2.imshow('tmp_image.png', show)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_33")

logo_filename = 'C:/_git/vcs/_4.python/opencv/data/opencv_logo.png'

mona = cv2.imread(filename)
logo = cv2.imread(logo_filename, cv2.IMREAD_UNCHANGED)  # 使用 cv2.IMREAD_UNCHANGED 讀取 png，保留 alpha 色版
mona_w = mona.shape[1]  # 蒙娜麗莎寬度
mona_h = mona.shape[0]  # 蒙娜麗莎高度
logo_w = logo.shape[1]  # logo 寬度
logo_h = logo.shape[0]  # logo 高度
dh = int((mona_h - logo_h) / 2)  # 如果 logo 要垂直置中，和上方的距離
h = dh + logo_h         # 計算蒙娜麗莎裡，logo 所在的高度位置

# 透過迴圈，根據背景透明度，計算出該像素的顏色
for i in range(logo_w):
    mona[dh:h,i,0] = mona[dh:h,i,0]*(1-logo[:,i,3]/255) + logo[:,i,0]*(logo[:,i,3]/255)
    mona[dh:h,i,1] = mona[dh:h,i,1]*(1-logo[:,i,3]/255) + logo[:,i,1]*(logo[:,i,3]/255)
    mona[dh:h,i,2] = mona[dh:h,i,2]*(1-logo[:,i,3]/255) + logo[:,i,2]*(logo[:,i,3]/255)

#cv2.imwrite('tmp_image.png', mona)

mona = mona.astype('float32')/255    # 如果要使用 imshow 必須要轉換類型
cv2.imshow('image', mona)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_34")

gif_filename = "C:/_git/vcs/_1.data/______test_files1/__pic/_gif/cat.gif"

print("gif轉jpg")
from PIL import Image,ImageSequence

gif = Image.open(gif_filename)                # 讀取動畫圖檔

i = 0                                      # 設定編號變數
for frame in ImageSequence.Iterator(gif):
    frame = frame.convert('RGB')           # 取出每一格轉換成 RGB
    #frame.save(f'tmp_frame{i}.jpg', quality=65, subsampling=0)  # 儲存為 jpg
    i = i + 1                              # 編號增加 1

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_35")

from PIL import Image,ImageSequence

gif = Image.open('dot.gif')

img_list = []                                      # 建立儲存影格的空串列
for frame in ImageSequence.Iterator(gif):
    frame = frame.convert('RGBA')                  # 轉換成 RGBA
    opencv_img = np.array(frame, dtype=np.uint8)   # 轉換成 numpy 陣列
    opencv_img = cv2.cvtColor(opencv_img, cv2.COLOR_RGBA2BGRA)  # 顏色從 RGBA 轉換為 BGRA
    img_list.append(opencv_img)                    # 利用串列儲存該圖片資訊

loop = True                                        # 設定 loop 為 True
while loop:
    for i in img_list:
        cv2.imshow('image', i)                # 不斷讀取並顯示串列中的圖片內容
        if cv2.waitKey(200) == ord('q'):
            loop = False                           # 停止時同時也將 while 迴圈停止
            break

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_36")

from PIL import Image,ImageSequence

gif = Image.open('dot.gif')

img_list = []
for frame in ImageSequence.Iterator(gif):
    frame = frame.convert('RGBA')
    opencv_img = np.array(frame, dtype=np.uint8)
    opencv_img = cv2.cvtColor(opencv_img, cv2.COLOR_RGBA2BGRA)

    # 在圖形中間繪製黑色方塊
    cv2.rectangle(opencv_img,(100,120),(300,180),(0,0,0),-1)

    # 在黑色方塊上方加入文字
    text = 'oxxo.studio'
    org = (110,160)
    fontFace = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    color = (255,255,255)
    thickness = 2
    lineType = cv2.LINE_AA
    cv2.putText(opencv_img, text, org, fontFace, fontScale, color, thickness, lineType)

    img_list.append(opencv_img)

loop = True
while loop:
    for i in img_list:
        cv2.imshow('image', i)
        if cv2.waitKey(200) == ord('q'):
            loop = False
            break
# 建立要輸出的影格串列
output = []
for i in img_list:
    img = i
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA)  # 因為 OpenCV 為 BGRA，要轉換成 RGBA
    img = Image.fromarray(img)    # 轉換成 PIL 格式
    img = img.convert('RGB')      # 轉換成 RGB ( 如果是 RGBA 會自動將黑色白色變成透明色 )
    output.append(img)            # 加入 output
# 儲存為 gif 動畫圖檔
output[0].save("tmp_image.gif", save_all=True, append_images=output[1:], duration=200, loop=0, disposal=0)

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_37")

from PIL import Image,ImageSequence

gif = []
for i in range(4):
    img = Image.open(f'frame{i}.jpg')  # 開啟圖片
    gif.append(img)                    # 加入串列
# 儲存為 gif
gif[0].save("tmp_image.gif", save_all=True, append_images=gif[1:], duration=200, loop=0, disposal=0)

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_38")

n = 0
for i in source:                  # source 為要轉存的所有圖片陣列 ( opencv 格式，色彩為 RGBA )
    img = Image.fromarray(i)      # 轉換成 PIL 格式
    img.save(f'tmp_gif{n}.gif')  # 儲存為 gif
    n = n + 1                     # 改變儲存的檔名編號

output = []                       # 建立空串列
for i in range(n):
    img = Image.open(f'tmp_gif{i}.gif')  # 依序開啟每張 gif
    img = img.convert("RGBA")             # 轉換為 RGBA
    output.append(img)                    # 記錄每張圖片內容

# 轉存為 gif 動畫，設定 disposal=2
output[0].save("tmp_image.gif", save_all=True, append_images=output[1:], duration=100, loop=0, disposal=2)

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_39")

filename = "C:/_git/vcs/_4.python/opencv/data/QR1.png"

img = cv2.imread(filename)                       # 開啟圖片

qrcode = cv2.QRCodeDetector()                        # 建立 QRCode 偵測器
data, bbox, rectified = qrcode.detectAndDecode(img)  # 偵測圖片中的 QRCode
# 如果 bbox 是 None 表示圖片中沒有 QRCode
if bbox is not None:
    print(data)                # QRCode 的內容
    print(bbox)                # QRCode 的邊界
    print(rectified)           # 換成垂直 90 度的陣列

cv2.imshow('image', img)  # 預覽圖片
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_40")

filename = "C:/_git/vcs/_4.python/opencv/data/QR1.png"

img = cv2.imread(filename)

qrcode = cv2.QRCodeDetector()
data, bbox, rectified = qrcode.detectAndDecode(img)

# 取得座標的函式
def boxSize(arr):
    global data
    box_roll = np.rollaxis(arr,1,0)   # 轉置矩陣，把 x 放在同一欄，y 放在同一欄
    xmax = int(np.amax(box_roll[0]))  # 取出 x 最大值
    xmin = int(np.amin(box_roll[0]))  # 取出 x 最小值
    ymax = int(np.amax(box_roll[1]))  # 取出 y 最大值
    ymin = int(np.amin(box_roll[1]))  # 取出 y 最小值
    return (xmin,ymin,xmax,ymax)

# 如果 bbox 是 None 表示圖片中沒有 QRCode
if bbox is not None:
    print(data)
    print(bbox)
    print(rectified)
    box = boxSize(bbox[0])
    cv2.rectangle(img,(box[0],box[1]),(box[2],box[3]),(0,0,255),5)  # 畫矩形

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_41")

from PIL import ImageFont, ImageDraw, Image          # 載入 PIL ( 為了放中文字 )

filename = "C:/_git/vcs/_4.python/opencv/data/QR1.png"
img = cv2.imread(filename)

qrcode = cv2.QRCodeDetector()
data, bbox, rectified = qrcode.detectAndDecode(img)

# 建立放入文字的函式
def putText(x,y,text,color=(0,0,0)):
    global img
    #font_filename = 'NotoSansTC-Regular.otf'      # 字體 ( 從 Google Font 下載 )
    font = ImageFont.truetype(font_filename, 20)  # 設定字型與大小
    imgPil = Image.fromarray(img)            # 將 img 轉換成 PIL 圖片物件
    draw = ImageDraw.Draw(imgPil)            # 建立繪圖物件
    draw.text((x, y), text, fill=color, font=font)  # 寫入文字
    img = np.array(imgPil)                   # 轉換回 np array

def boxSize(arr):
    global data
    box_roll = np.rollaxis(arr,1,0)
    xmax = int(np.amax(box_roll[0]))
    xmin = int(np.amin(box_roll[0]))
    ymax = int(np.amax(box_roll[1]))
    ymin = int(np.amin(box_roll[1]))
    return (xmin,ymin,xmax,ymax)

if bbox is not None:
    print(data)
    print(bbox)
    print(rectified)
    box = boxSize(bbox[0])
    cv2.rectangle(img,(box[0],box[1]),(box[2],box[3]),(0,0,255),5)

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_42")

""" many-qr-code
from PIL import ImageFont, ImageDraw, Image

img = cv2.imread("many-qrcode.jpg")

def putText(x,y,text,color=(0,0,0)):
    global img
    #font_filename = 'NotoSansTC-Regular.otf'
    font = ImageFont.truetype(font_filename, 20)
    imgPil = Image.fromarray(img)
    draw = ImageDraw.Draw(imgPil)
    draw.text((x, y), text, fill=color, font=font)
    img = np.array(imgPil)

def boxSize(arr):
    global data
    box_roll = np.rollaxis(arr,1,0)
    xmax = int(np.amax(box_roll[0]))
    xmin = int(np.amin(box_roll[0]))
    ymax = int(np.amax(box_roll[1]))
    ymin = int(np.amin(box_roll[1]))
    return (xmin,ymin,xmax,ymax)

qrcode = cv2.QRCodeDetector()
ok, data, bbox, rectified = qrcode.detectAndDecodeMulti(img)   # 改用 detectAndDecodeMulti
# 如果有偵測到
if ok:
    # 使用 for 迴圈取出每個 QRCode 的資訊
    for i in range(len(data)):
        print(data[i])
        print(bbox[i])
        text = data[i]          # QRCode 內容
        box = boxSize(bbox[i])  # QRCode 左上與右下座標
        cv2.rectangle(img,(box[0],box[1]),(box[2],box[3]),(0,0,255),5)  # 標記外框
        putText(box[0],box[3],text)   # 寫出文字

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()
"""

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_43")

""" barcode
from PIL import ImageFont, ImageDraw, Image

img = cv2.imread("barcode.jpg")

def putText(x,y,text,color=(0,0,0)):
    global img
    #font_filename = 'NotoSansTC-Regular.otf'
    font = ImageFont.truetype(font_filename, 20)
    imgPil = Image.fromarray(img)
    draw = ImageDraw.Draw(imgPil)
    draw.text((x, y), text, fill=color, font=font)
    img = np.array(imgPil)

def boxSize(arr):
    global data
    box_roll = np.rollaxis(arr,1,0)
    xmax = int(np.amax(box_roll[0]))
    xmin = int(np.amin(box_roll[0]))
    ymax = int(np.amax(box_roll[1]))
    ymin = int(np.amin(box_roll[1]))
    return (xmin,ymin,xmax,ymax)

barcode = cv2.barcode_BarcodeDetector()                   # 建立 BarCode 偵測器
ok, data, data_type, bbox = barcode.detectAndDecode(img)  # 偵測 BarCode
# 如果有 BarCode
if ok:
    # 依序取出所有 BarCode 內容
    for i in range(len(data)):
        box = boxSize(bbox[i])   # 取出座標
        text = data[i]           # 取出內容
        cv2.rectangle(img,(box[0],box[1]),(box[2],box[3]),(0,0,255),5)  # 繪製外框
        putText(box[0],box[3],text,color=(0,0,255))                     # 放入文字

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_44")


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

#cv2.imwrite('tmp_image_2.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 80])  # 存成 jpg
#cv2.imwrite('tmp_image_3.png', img)  # 存成 png



#CCRR



print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)
x = 100
y = 100
w = 200
h = 200
crop_img = img[y:y+h, x:x+w]        # 取出陣列的範圍


print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)
x = 100
y = 100
w = 200
h = 200
crop_img = img[y:y+h, x:x+w]

output = np.zeros((360,480,3), dtype='uint8') # 產生黑色畫布
output[x:x+w, y:y+h]=crop_img


img = cv2.imread(filename)
output_1 = cv2.resize(img, (200, 200))   # 產生 200x200 的圖
output_2 = cv2.resize(img, (100, 300))   # 產生 100x300 的圖

print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)
size = img.shape         # 取得原始圖片的資訊
level = 15               # 縮小比例 ( 可當作馬賽克的等級 )
h = int(size[0]/level)   # 按照比例縮小後的高度 ( 使用 int 去除小數點 )
w = int(size[1]/level)   # 按照比例縮小後的寬度 ( 使用 int 去除小數點 )
mosaic = cv2.resize(img, (w,h), interpolation=cv2.INTER_LINEAR)   # 根據縮小尺寸縮小
mosaic = cv2.resize(mosaic, (size[1],size[0]), interpolation=cv2.INTER_NEAREST) # 放大到原本的大小

cv2.imshow('image', mosaic)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)

x = 135   # 剪裁區域左上 x 座標
y = 90    # 剪裁區域左上 y 座標
cw = 100  # 剪裁區域寬度
ch = 120  # 剪裁區域高度
mosaic = img[y:y+ch, x:x+cw]   # 取得剪裁區域
level = 15         # 馬賽克程度
h = int(ch/level)  # 縮小的高度 ( 使用 int 去除小數點 )
w = int(cw/level)  # 縮小的寬度 ( 使用 int 去除小數點 )
mosaic = cv2.resize(mosaic, (w,h), interpolation=cv2.INTER_LINEAR)
mosaic = cv2.resize(mosaic, (cw,ch), interpolation=cv2.INTER_NEAREST)
img[y:y+ch, x:x+cw] = mosaic   # 將圖片的剪裁區域，換成馬賽克的圖

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

#flip

img = cv2.imread(filename)   # 開啟圖片
output_0 = cv2.flip(img, 0)    # 上下翻轉
output_1 = cv2.flip(img, 1)    # 左右翻轉
output_2 = cv2.flip(img, -1)   # 上下左右翻轉

print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)
output = cv2.transpose(img)    # 逆時針旋轉 90 度。

print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)
output_ROTATE_90_CLOCKWISE = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
output_ROTATE_90_COUNTERCLOCKWISE = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
output_ROTATE_180 = cv2.rotate(img, cv2.ROTATE_180)

print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)
M = np.float32([[1, 0, 100], [0, 1, 100]]) # 2x3 矩陣，x 軸平移 100，y 軸平移 100
output = cv2.warpAffine(img, M, (480, 360))

cv2.imshow('image', output)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)
M = cv2.getRotationMatrix2D((240, 180), 45, 1)    # 中心點 (240, 180)，旋轉 45 度，尺寸 1
output = cv2.warpAffine(img, M, (480, 360))

cv2.imshow('image', output)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)
p1 = np.float32([[100,100],[480,0],[0,360]])
p2 = np.float32([[0,0],[480,0],[0,360]])
M = cv2.getAffineTransform(p1, p2)
output = cv2.warpAffine(img, M, (480, 360))

cv2.imshow('image', output)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

p1 = np.float32([[100,100],[480,0],[0,360],[480,360]])
p2 = np.float32([[0,0],[480,0],[0,360],[480,360]])
m = cv2.getPerspectiveTransform(p1,p2)

img = cv2.imread(filename)
output = cv2.warpPerspective(img, m, (480, 360))

cv2.imshow('image', output)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個

import cv2

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_50")

img = cv2.imread(filename)

def show_xy(event,x,y,flags,userdata):
    print(event,x,y,flags)
    # 印出相關參數的數值，userdata 可透過 setMouseCallback 第三個參數垂遞給函式

cv2.imshow('ImageShow', img)
cv2.setMouseCallback('ImageShow', show_xy)  # 設定偵測事件的函式與視窗

cv2.waitKey(0)     # 按下任意鍵停止
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_51")

img = cv2.imread(filename)

def show_xy(event,x,y,flags,param):
    if event == 0:
        img2 = img.copy()                         # 當滑鼠移動時，複製原本的圖片
        cv2.circle(img2, (x,y), 10, (0,0,0), 1)   # 繪製黑色空心圓
        cv2.imshow('ImageShow', img2)            # 顯示繪製後的影像
    if event == 1:
        color = img[y,x]                          # 當滑鼠點擊時
        print(color)                              # 印出顏色

cv2.imshow('ImageShow', img)
cv2.setMouseCallback('ImageShow', show_xy)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_52")

img = cv2.imread(filename)

dots = []   # 記錄座標的空串列
def show_xy(event,x,y,flags,param):
    if event == 1:
        dots.append([x, y])                          # 記錄座標
        cv2.circle(img, (x, y), 10, (0,0,255), -1)   # 在點擊的位置，繪製圓形
        num = len(dots)                              # 目前有幾個座標
        if num > 1:                                  # 如果有兩個點以上
            x1 = dots[num-2][0]
            y1 = dots[num-2][1]
            x2 = dots[num-1][0]
            y2 = dots[num-1][1]
            cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)  # 取得最後的兩個座標，繪製直線
        cv2.imshow('ImageShow', img)

cv2.imshow('ImageShow', img)
cv2.setMouseCallback('ImageShow', show_xy)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_53")

img = cv2.imread('mona.jpg')

dot1 = []                          # 記錄第一個座標
dot2 = []                          # 記錄第二個座標

# 滑鼠事件發生時要執行的函式
def show_xy(event,x,y,flags,param):
    global dot1, dot2, img         # 在函式內使用全域變數
    # 滑鼠拖曳發生時
    if flags == 1:
        if event == 1:
            dot1 = [x, y]          # 按下滑鼠時記錄第一個座標
        if event == 0:
            img2 = img.copy()      # 拖曳時不斷複製 img
            dot2 = [x, y]          # 拖曳時不斷更新第二個座標
            # 根據兩個座標繪製四邊形
            cv2.rectangle(img2, (dot1[0], dot1[1]), (dot2[0], dot2[1]), (0,0,255), 2)
            # 不斷顯示新圖片 ( 如果不這麼做，會出現一堆四邊形殘影 )
            cv2.imshow('ImageShow', img2)

cv2.imshow('ImageShow', img)
cv2.setMouseCallback('ImageShow', show_xy)

cv2.waitKey(0)   # 按下任意鍵結束
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_54")

img = cv2.imread('mona.jpg')

dot1 = []
dot2 = []
def show_xy(event,x,y,flags,param):
    global dot1, dot2, img, img2    # 因為要讓 img = img2，所以也要宣告 img2 為全域變數
    if flags == 1:
        if event == 1:
            dot1 = [x, y]
        if event == 0:
            img2 = img.copy()
            dot2 = [x, y]
            cv2.rectangle(img2, (dot1[0], dot1[1]), (dot2[0], dot2[1]), (0,0,255), 2)
            cv2.imshow('ImageShow', img2)
        if event == 4:
            img = img2   # 滑鼠放開時 ( event == 4 )，將 img 更新為 img2

cv2.imshow('ImageShow', img)
cv2.setMouseCallback('ImageShow', show_xy)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_55")

img = cv2.imread('mona.jpg')

dot1 = []
dot2 = []
def show_xy(event,x,y,flags,param):
    global dot1, dot2, img, img2
    if flags == 1:
        if event == 1:
            dot1 = [x, y]
        if event == 0:
            img2 = img.copy()
            dot2 = [x, y]
            cv2.rectangle(img2, (dot1[0], dot1[1]), (dot2[0], dot2[1]), (0,0,255), 2)
            cv2.imshow('ImageShow', img2)
        if event == 4:
            level = 8                                         # 縮小比例 ( 可當作馬賽克的等級 )
            h = int((dot2[0] - dot1[0]) / level)              # 按照比例縮小後的高度 ( 使用 int 去除小數點 )
            w = int((dot2[1] - dot1[1]) / level)              # 按照比例縮小後的寬度 ( 使用 int 去除小數點 )
            mosaic = img[dot1[1]:dot2[1], dot1[0]:dot2[0]]    # 取得馬賽克區域
            mosaic = cv2.resize(mosaic, (w, h), interpolation=cv2.INTER_LINEAR)   # 根據縮小尺寸縮小
            mosaic = cv2.resize(mosaic, (dot2[0] - dot1[0], dot2[1] - dot1[1]), interpolation=cv2.INTER_NEAREST) # 放大到原本的大小
            img[dot1[1]:dot2[1], dot1[0]:dot2[0]] = mosaic   # 置換成馬賽克的影像
            cv2.imshow('ImageShow', img)

cv2.imshow('ImageShow', img)
cv2.setMouseCallback('ImageShow', show_xy)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_56")

dots = []   # 建立空串列記錄座標
w = 420
h = 240
draw = np.zeros((h,w,4), dtype='uint8')   # 建立 420x240 的 RGBA 黑色畫布

def show_xy(event,x,y,flags,param):
    global dots, draw                     # 定義全域變數
    if flags == 1:
        if event == 1:
            dots.append([x,y])            # 如果拖曳滑鼠剛開始，記錄第一點座標
        if event == 4:
            dots = []                     # 如果放開滑鼠，清空串列內容
        if event == 0 or event == 4:
            dots.append([x,y])            # 拖曳滑鼠時，不斷記錄座標
            x1 = dots[len(dots)-2][0]     # 取得倒數第二個點的 x 座標
            y1 = dots[len(dots)-2][1]     # 取得倒數第二個點的 y 座標
            x2 = dots[len(dots)-1][0]     # 取得倒數第一個點的 x 座標
            y2 = dots[len(dots)-1][1]     # 取得倒數第一個點的 y 座標
            cv2.line(draw,(x1,y1),(x2,y2),(0,0,255,255),2)  # 畫直線
        cv2.imshow('ImageShow', draw)

cv2.imshow('ImageShow', draw)
cv2.setMouseCallback('ImageShow', show_xy)

while True:
    keyboard = cv2.waitKey(5)                    # 每 5 毫秒偵測一次鍵盤事件
    if keyboard == ord('q'):
        break                                    # 如果按下 q 就跳出
    if keyboard == ord('r'):
        draw = np.zeros((h,w,4), dtype='uint8')  # 如果按下 r 就變成原本全黑的畫布
        cv2.imshow('ImageShow', draw)

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("OpenCV_ai_58")

cv2.namedWindow('ImageShow')  # 建立一個名為 ImageShow 的視窗

while True:
    keycode = cv2.waitKey(0)   # 持續等待，直到按下鍵盤按鍵才會繼續
    c = chr(keycode)           # 將 ASCII 代碼轉換成真實字元
    print(c, keycode)          # 印出結果
    if keycode == 27:
        break                  # 如果代碼等於 27，結束迴圈 ( 27 表示按鍵 ESC )

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_59")

img = cv2.imread('mona.jpg')

# 定義調整亮度對比的函式
def adjust(i, c, b):
    output = i * (c/100 + 1) - c + b    # 轉換公式
    output = np.clip(output, 0, 255)
    output = np.uint8(output)
    return output

contrast = 0    # 初始化要調整對比度的數值
brightness = 0  # 初始化要調整亮度的數值
cv2.imshow('ImageShow', img)

while True:
    keycode = cv2.waitKey(0)
    if keycode == 0:
        brightness = brightness + 5    # 按下鍵盤的「上」，增加亮度
    if keycode == 1:
        brightness = brightness - 5    # 按下鍵盤的「下」，減少亮度
    if keycode == 2:
        contrast = contrast - 5        # 按下鍵盤的「右」，增加對比度
    if keycode == 3:
        contrast = contrast + 5        # 按下鍵盤的「左」，減少對比度
    if keycode == 113:
        contrast, brightness = 0, 0    # 按下鍵盤的「q」，恢復預設值
    if keycode == 27:
        break
    show = img.copy()                  # 複製原始圖片
    show = adjust(show, contrast, brightness)  # 根據亮度和對比度的調整值，輸出新的圖片
    cv2.imshow('ImageShow', show)

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_60")

img = cv2.imread('mona.jpg')
cv2.imshow('ImageShow', img)

def test(val):
    print(val)

cv2.createTrackbar('test', 'ImageShow', 0, 255, test)
cv2.setTrackbarPos('test', 'ImageShow', 50)

keycode = cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_61")

img = cv2.imread('mona.jpg')
cv2.imshow('ImageShow', img)

contrast = 0    # 初始化要調整對比度的數值
brightness = 0  # 初始化要調整亮度的數值
cv2.imshow('ImageShow', img)

# 定義調整亮度對比的函式
def adjust(i, c, b):
    output = i * (c/100 + 1) - c + b    # 轉換公式
    output = np.clip(output, 0, 255)
    output = np.uint8(output)
    cv2.imshow('ImageShow', output)

# 定義調整亮度函式
def brightness_fn(val):
    global img, contrast, brightness
    brightness = val - 100
    adjust(img, contrast, brightness)

# 定義調整對比度函式
def contrast_fn(val):
    global img, contrast, brightness
    contrast = val - 100
    adjust(img, contrast, brightness)

cv2.createTrackbar('brightness', 'ImageShow', 0, 200, brightness_fn)  # 加入亮度調整滑桿
cv2.setTrackbarPos('brightness', 'ImageShow', 100)
cv2.createTrackbar('contrast', 'ImageShow', 0, 200, contrast_fn)      # 加入對比度調整滑桿
cv2.setTrackbarPos('contrast', 'ImageShow', 100)

keycode = cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_62")

img = cv2.imread('mona.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   # 將圖片轉成灰階


# OpenCV 人臉識別分類器
xml_filename = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_default.xml"

face_cascade_classifier = cv2.CascadeClassifier(xml_filename)   # 載入人臉模型
faces = face_cascade_classifier.detectMultiScale(gray)    # 偵測人臉

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)    # 利用 for 迴圈，抓取每個人臉屬性，繪製方框

cv2.imshow('ImageShow', img)
cv2.waitKey(0) # 按下任意鍵停止
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_64")

img = cv2.imread('mona.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 影像轉換成灰階
xml_filename = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_default.xml"
face_cascade_classifier = cv2.CascadeClassifier(xml_filename) # 載入人臉偵測模型
faces = face_cascade_classifier.detectMultiScale(gray,1.2,3)  # 開始辨識影像中的人臉

for (x, y, w, h) in faces:
    mosaic = img[y:y+h, x:x+w]   # 馬賽克區域
    level = 15                   # 馬賽克程度
    mh = int(h/level)            # 根據馬賽克程度縮小的高度
    mw = int(w/level)            # 根據馬賽克程度縮小的寬度
    mosaic = cv2.resize(mosaic, (mw,mh), interpolation=cv2.INTER_LINEAR) # 先縮小
    mosaic = cv2.resize(mosaic, (w,h), interpolation=cv2.INTER_NEAREST)  # 然後放大
    img[y:y+h, x:x+w] = mosaic   # 將指定區域換成馬賽克區域

cv2.imshow('ImageShow', img)
cv2.waitKey(0)   # 按下任意鍵停止
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("OpenCV_ai_66")

""" 缺  xml
img = cv2.imread('mona.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   # 圖片轉灰階
#gray = cv2.medianBlur(gray, 5)                # 如果一直偵測到雜訊，可使用模糊的方式去除雜訊

eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")  # 使用眼睛模型
eyes = eye_cascade.detectMultiScale(gray)                       # 偵測眼睛
for (x, y, w, h) in eyes:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)      # 標記綠色方框

mouth_cascade = cv2.CascadeClassifier("haarcascade_mcs_mouth.xml")  # 使用嘴巴模型
mouths = mouth_cascade.detectMultiScale(gray)                           # 偵測嘴巴
for (x, y, w, h) in mouths:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)              # 標記紅色方框

nose_cascade = cv2.CascadeClassifier("haarcascade_mcs_nose.xml")    # 使用鼻子模型
noses = nose_cascade.detectMultiScale(gray)                             # 偵測鼻子
for (x, y, w, h) in noses:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)              # 標記藍色方框

cv2.imshow('ImageShow', img)
cv2.waitKey(0)   # 按下任意鍵停止
cv2.destroyAllWindows()
"""

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_68")

""" lack xml
img = cv2.imread('cars.jpg')                    # 讀取街道影像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # 轉換成黑白影像

car = cv2.CascadeClassifier("cars.xml")    # 讀取汽車模型
gray = cv2.medianBlur(gray, 5)                  # 模糊化去除雜訊
cars = car.detectMultiScale(gray, 1.1, 3)       # 偵測汽車
for (x, y, w, h) in cars:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)   # 繪製外框

cv2.imshow('ImageShow', img)
cv2.waitKey(0) # 按下任意鍵停止
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_69")

img = cv2.imread('cars.jpg')                    # 讀取街道影像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # 轉換成黑白影像

car = cv2.CascadeClassifier("haarcascade_fullbody.xml")    # 讀取人體模型
gray = cv2.medianBlur(gray, 5)                  # 模糊化去除雜訊
cars = car.detectMultiScale(gray, 1.1, 3)       # 偵測行人
for (x, y, w, h) in cars:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)   # 繪製外框

cv2.imshow('ImageShow', img)
cv2.waitKey(0)     # 按下任意鍵停止
cv2.destroyAllWindows()
"""

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_70")
""" lack test file
xml_filename = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_default.xml"
detector = cv2.CascadeClassifier(xml_filename)  # 載入人臉追蹤模型
recog = cv2.face.LBPHFaceRecognizer_create()      # 啟用訓練人臉模型方法
faces = []   # 儲存人臉位置大小的串列
ids = []     # 記錄該人臉 id 的串列

for i in range(1,31):
    img = cv2.imread(f'face01/{i}.jpg')           # 依序開啟每一張蔡英文的照片
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 色彩轉換成黑白
    img_np = np.array(gray,'uint8')               # 轉換成指定編碼的 numpy 陣列
    face = detector.detectMultiScale(gray)        # 擷取人臉區域
    for(x,y,w,h) in face:
        faces.append(img_np[y:y+h,x:x+w])         # 記錄蔡英文人臉的位置和大小內像素的數值
        ids.append(1)                             # 記錄蔡英文人臉對應的 id，只能是整數，都是 1 表示蔡英文的 id 為 1

for i in range(1,16):
    img = cv2.imread(f'face02/{i}.jpg')           # 依序開啟每一張川普的照片
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 色彩轉換成黑白
    img_np = np.array(gray,'uint8')               # 轉換成指定編碼的 numpy 陣列
    face = detector.detectMultiScale(gray)        # 擷取人臉區域
    for(x,y,w,h) in face:
        faces.append(img_np[y:y+h,x:x+w])         # 記錄川普人臉的位置和大小內像素的數值
        ids.append(2)                             # 記錄川普人臉對應的 id，只能是整數，都是 2 表示川普的 id 為 2

print('training...')                              # 提示開始訓練
recog.train(faces,np.array(ids))                  # 開始訓練
recog.save('face.yml')                            # 訓練完成儲存為 face.yml
print('ok!')
"""

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_76")

lower = np.array([30,40,200])  # 轉換成 NumPy 陣列，範圍稍微變小 ( 55->30, 70->40, 252->200 )
upper = np.array([90,100,255]) # 轉換成 NumPy 陣列，範圍稍微加大 ( 70->90, 80->100, 252->255 )
img = cv2.imread('mona.jpg')
mask = cv2.inRange(img, lower, upper)             # 使用 inRange
output = cv2.bitwise_and(img, img, mask = mask )  # 套用影像遮罩
cv2.imwrite('tmp_output.jpg', output)

cv2.imshow('Image', output)
cv2.waitKey(0)                                    # 按下任意鍵停止
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


