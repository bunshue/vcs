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

image = cv2.imread(filename)   # 預設為彩色 1號
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # 灰階 2號
image = cv2.imread(filename, 2) # 也可使用數字代表模式
print(image.shape)            # 得到 shape
print(image.dtype)            # uint8

cv2.imshow('image', image)
cv2.waitKey()
cv2.destroyAllWindows()

"""
image1 = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
image2 = cv2.imread('test.png', cv2.IMREAD_UNCHANGED)
print(image1.shape)    # (400, 300, 3)  JPG 只有三個色版 BGR
print(image2.shape)    # (400, 300, 4)  PNG 四個色版 GRA

image = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)  # 轉換成 BGRA 色彩模式
print(image.shape)                             # (400, 300, 4)  第三個數值變成 4
"""

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_02")

image = cv2.imread(filename)
b, g, r = cv2.split(image)
#print(b)
#print(g)
#print(r)

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_03")

image_blue = cv2.imread(filename)
image_green = cv2.imread(filename)
image_red = cv2.imread(filename)
image_blue[:,:,1] = 0    # 將綠色設為 0
image_blue[:,:,2] = 0    # 將紅色設為 0
image_green[:,:,0] = 0   # 將藍色設為 0
image_green[:,:,2] = 0   # 將紅色設為 0
image_red[:,:,0] = 0     # 將藍色設為 0
image_red[:,:,1] = 0     # 將綠色設為 0

cv2.imshow('image blue', image_blue)
cv2.imshow('image green', image_green)
cv2.imshow('image red', image_red)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_04")

image = cv2.imread(filename)
print('原圖為彩色')
cv2.imshow('image1', image)
print('彩色轉灰階')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉換成灰階影像

cv2.imshow('image', image)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_05")

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

print('像素操作 底片效果 半張負片')

image = cv2.imread(filename)
rows = image.shape[0]     # 取得高度的總像素
cols = image.shape[1]     # 取得寬度的總像素

for row in range(int(rows/2)):  # 只取 rows 的一半 ( 使用 int 取整數 )
    for col in range(cols):
        image[row, col, 0] = 255 - image[row, col, 0]   # 255 - 藍色
        image[row, col, 1] = 255 - image[row, col, 1]   # 255 - 綠色
        image[row, col, 2] = 255 - image[row, col, 2]   # 255 - 紅色

cv2.imshow('image', image)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_06")

print('像素操作 全張負片')

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

image = cv2.imread(filename)

image = 255-image # 使用 255 減去陣列中所有數值

cv2.imshow('image', image)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_07")

image = cv2.imread(filename)

contrast = 200
brightness = 0
output = image * (contrast/127 + 1) - contrast + brightness # 轉換公式
# 轉換公式參考 https://stackoverflow.com/questions/50474302/how-do-i-adjust-brightness-contrast-and-vibrance-with-opencv-python

# 調整後的數值大多為浮點數，且可能會小於 0 或大於 255
# 為了保持像素色彩區間為 0～255 的整數，所以再使用 np.clip() 和 np.uint8() 進行轉換
output = np.clip(output, 0, 255)
output = np.uint8(output)

cv2.imshow('image', output)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_08")

image = cv2.imread(filename)
output = image    # 建立 output 變數

alpha = 1
beta = 10

cv2.convertScaleAbs(image, output, alpha, beta)  # 套用 convertScaleAbs

cv2.imshow('image', image)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_09 各種二值化")

image = cv2.imread(filename)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY); # 轉換前，都先將圖片轉換成灰階色彩
ret, output1 = cv2.threshold(image_gray, 127, 255, cv2.THRESH_BINARY)     # 如果大於 127 就等於 255，反之等於 0。
ret, output2 = cv2.threshold(image_gray, 127, 255, cv2.THRESH_BINARY_INV) # 如果大於 127 就等於 0，反之等於 255。
ret, output3 = cv2.threshold(image_gray, 127, 255, cv2.THRESH_TRUNC)      # 如果大於 127 就等於 127，反之數值不變。
ret, output4 = cv2.threshold(image_gray, 127, 255, cv2.THRESH_TOZERO)     # 如果大於 127 數值不變，反之數值等於 0。
ret, output5 = cv2.threshold(image_gray, 127, 255, cv2.THRESH_TOZERO_INV) # 如果大於 127 等於 0，反之數值不變。

cv2.imshow('image', image)
cv2.imshow('image1', output1)
cv2.imshow('image2', output2)
cv2.imshow('image3', output3)
cv2.imshow('image4', output4)
cv2.imshow('image5', output5)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_10")

image = cv2.imread(filename)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY); # 轉換前，都先將圖片轉換成灰階色彩
ret, output1 = cv2.threshold(image_gray, 127, 255, cv2.THRESH_BINARY)
output2 = cv2.adaptiveThreshold(image_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
output3 = cv2.adaptiveThreshold(image_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imshow('image', image)
cv2.imshow('image1', output1)
cv2.imshow('image2', output2)
cv2.imshow('image3', output3)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_11 三原色疊加")

filename1 = 'C:/_git/vcs/_4.python/opencv/data/RGB_R.png'
filename2 = 'C:/_git/vcs/_4.python/opencv/data/RGB_G.png'
filename3 = 'C:/_git/vcs/_4.python/opencv/data/RGB_B.png'

image_red = cv2.imread(filename1)
image_green = cv2.imread(filename2)
image_blue = cv2.imread(filename3)

output = cv2.add(image_red, image_green)  # 疊加紅色和綠色
output = cv2.add(output, image_blue)    # 疊加藍色

cv2.imshow('image', output)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_12 addWeighted 要一樣大的圖")

filename1 = 'C:/_git/vcs/_4.python/opencv/data/RGB_R.png'
filename2 = 'C:/_git/vcs/_4.python/opencv/data/RGB_G.png'

image1 = cv2.imread(filename1)
image2 = cv2.imread(filename2)
output = cv2.addWeighted(image1, 0.5, image2, 0.3, 50)

cv2.imshow('image', output)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_13 subtract 兩圖相減")

filename1 = 'C:/_git/vcs/_4.python/opencv/data/RGB_R.png'
filename2 = 'C:/_git/vcs/_4.python/opencv/data/RGB_G.png'

image1 = cv2.imread(filename1)
image2 = cv2.imread(filename2)
output = cv2.subtract(image1, image2)  # 相減

cv2.waitKey(0)       # 按下任意鍵停止
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_14")

image = cv2.imread(filename)

w, h = 400, 400
image1 = np.zeros([h,w,3])
for i in range(h):
    image[i,:,1] = int(256*i/400)   # 從上往下填入綠色漸層

image = image.astype('float32')/255   # 轉換內容類型

cv2.imshow('image', image)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_15")

w = 400
h = 400
image = np.zeros([h,w,3])
for i in range(h):
    for j in range(w):
        image[i,j,0] = int(256*(j+i)/(w+h))
        image[i,j,2] = int(256*(j+i)/(w+h))

image = image.astype('float32')/255

cv2.imshow('image', image)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_16")

w = 400
h = 400
image = np.zeros([h,w,4])             # 第三個值為 4
for i in range(h):
    image[i,:,3] = int(256*i/400)     # 設定第四個值 ( 透明度 )

image = image.astype('float32')/255

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_17")

logo_filename = 'C:/_git/vcs/_4.python/opencv/data/opencv_logo.png'

image = cv2.imread(logo_filename, cv2.IMREAD_UNCHANGED)  # 開啟圖片
image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)         # 因為是 jpg，要轉換顏色為 BGRA
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)        # 新增 gray 變數為轉換成灰階的圖片

h = image.shape[0]     # 取得圖片高度
w = image.shape[1]     # 取得圖片寬度

# 依序取出圖片中每個像素
for x in range(w):
    for y in range(h):
        if gray[y, x]>200:
            image[y, x, 3] = 255 - gray[y, x]
            # 如果該像素的灰階度大於 200，調整該像素的透明度
            # 使用 255 - gray[y, x] 可以將一些邊緣的像素變成半透明，避免太過鋸齒的邊緣

cv2.waitKey(0)                        # 按下任意鍵停止
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_18")

logo_filename = 'C:/_git/vcs/_4.python/opencv/data/opencv_logo.png'

image = cv2.imread(logo_filename, cv2.IMREAD_UNCHANGED)
image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

h = image.shape[0]
w = image.shape[1]

for x in range(w):
    for y in range(h):
        if gray[y, x]>200:
            image[y, x] = [0,255,255,255]  # 換成黃色

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_19")

filename1 = 'C:/_git/vcs/_4.python/opencv/data/RGB_R.png'
filename2 = 'C:/_git/vcs/_4.python/opencv/data/RGB_G.png'

bg = cv2.imread(filename1, cv2.IMREAD_UNCHANGED)     # 開啟背景圖
bg = cv2.cvtColor(bg, cv2.COLOR_BGR2BGRA)           # 轉換成 BGRA

img = cv2.imread(filename2, cv2.IMREAD_UNCHANGED)  # 開啟悟空公仔圖
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

cv2.imshow('image', bg)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_20")

img = cv2.imread(filename)

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

img = cv2.imread(filename)

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
print("OpenCV_ai_30")

mask = np.zeros((300,300,3), dtype='uint8')      # 建立 300x300 的黑色畫布
cv2.circle(mask,(150,150),100,(255,255,255),-1)  # 在畫布上中心點加入一個半徑 100 的白色圓形
mask = cv2.GaussianBlur(mask, (35, 35), 0)       # 進行高斯模糊

cv2.imshow('image', mask)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_31")

""" TBD
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
print("OpenCV_ai_35")

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
print("OpenCV_ai_36")

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
print("OpenCV_ai_37")

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
print("OpenCV_ai_38")

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
print("OpenCV_ai_40 按上下調整亮度 按左右調整對比度 按ESC離開")

filename = 'C:/_git/vcs/_4.python/_data/elephant.jpg'
img = cv2.imread(filename)

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
print("OpenCV_ai_41")

filename = 'C:/_git/vcs/_4.python/_data/elephant.jpg'
img = cv2.imread(filename)

cv2.imshow('ImageShow', img)

def test(val):
    print(val)

cv2.createTrackbar('test', 'ImageShow', 0, 255, test)
cv2.setTrackbarPos('test', 'ImageShow', 50)

keycode = cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_42")

filename = 'C:/_git/vcs/_4.python/_data/elephant.jpg'
img = cv2.imread(filename)

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

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("OpenCV_ai_39 按ESC離開")

cv2.namedWindow('ImageShow')  # 建立一個名為 ImageShow 的視窗

while True:
    keycode = cv2.waitKey(0)   # 持續等待，直到按下鍵盤按鍵才會繼續
    c = chr(keycode)           # 將 ASCII 代碼轉換成真實字元
    print(c, keycode)          # 印出結果
    if keycode == 27:
        break                  # 如果代碼等於 27，結束迴圈 ( 27 表示按鍵 ESC )

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
