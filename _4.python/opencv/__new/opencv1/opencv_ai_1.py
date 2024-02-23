"""
一本精通：OpenCV 與 AI 影像辨識

"""

import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個

import cv2
import numpy as np

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)   # 開啟圖片，預設使用 cv2.IMREAD_COLOR 模式
cv2.imshow('oxxostudio', img)  # 使用名為 oxxostudio 的視窗開啟圖片
cv2.waitKey(0)                 # 按下任意鍵停止
cv2.destroyAllWindows()        # 結束所有圖片視窗

print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # 使用 cv2.IMREAD_GRAYSCALE 模式
# img = cv2.imread(filename, 2) # 也可使用數字代表模式
cv2.imshow('oxxostudio', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # 使用 cv2.IMREAD_GRAYSCALE 模式
cv2.imshow('oxxostudio', img)
cv2.waitKey(2000)       # 等待兩秒 ( 2000 毫秒 ) 後關閉圖片視窗
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)   # 以灰階模式開啟圖片
cv2.imwrite('tmp_oxxostudio_2.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 80])  # 存成 jpg
cv2.imwrite('tmp_oxxostudio_3.png', img)  # 存成 png

print("------------------------------------------------------------")  # 60個

img = np.zeros((500,500,3), dtype='uint8')   # 快速產生 500x500，每個項目為 [0,0,0] 的三維陣列
img[150:350, 150:350] = [0,0,255]  # 將中間 200x200 的每個項目內容，改為 [0,0,255]
cv2.imwrite('tmp_oxxostudio.jpg', img)       # 存成 jpg
cv2.imshow('oxxostudio', img)            # 顯示圖片
cv2.waitKey(0)                           # 按下任意鍵停止
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

""" webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

print("------------------------------------------------------------")  # 60個

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()             # 讀取影片的每一幀
    if not ret:
        print("Cannot receive frame")   # 如果讀取錯誤，印出訊息
        break
    cv2.imshow('oxxostudio', frame)     # 如果讀取成功，顯示該幀的畫面
    if cv2.waitKey(1) == ord('q'):      # 每一毫秒更新一次，直到按下 q 結束
        break
cap.release()                           # 所有作業都完成後，釋放資源
cv2.destroyAllWindows()                 # 結束所有視窗

print("------------------------------------------------------------")  # 60個

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 轉換成灰階
    # gray = cv2.cvtColor(frame, 6)  # 也可以用數字對照 6 表示轉換成灰階
    cv2.imshow('oxxostudio', gray)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

cap = cv2.VideoCapture(0)                         # 讀取電腦攝影機鏡頭影像。
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))    # 取得影像寬度
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 取得影像高度
fourcc = cv2.VideoWriter_fourcc(*'MJPG')          # 設定影片的格式為 MJPG
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (width,  height))  # 產生空的影片
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    out.write(frame)       # 將取得的每一幀圖像寫入空的影片
    cv2.imshow('oxxostudio', frame)
    if cv2.waitKey(1) == ord('q'):
        break             # 按下 q 鍵停止
cap.release()
out.release()      # 釋放資源
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('output.mov', fourcc, 20.0, (width,  height))
# 如果轉換成黑白影片後如果無法開啟，請加上 isColor=False 參數設定
# out = cv2.VideoWriter('output.mov', fourcc, 20.0, (width,  height), isColor=False)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 轉換成灰階
    out.write(gray)
    cv2.imshow('oxxostudio', gray)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)
print(img.shape)            # 得到 (360, 480, 3)
cv2.imshow('oxxostudio', img)
cv2.waitKey(0)              # 按下任意鍵停止
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)
print(img.size)            # 518400 ( 360x480x3 )
cv2.imshow('oxxostudio', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)
print(img.dtype)            # uint8
cv2.imshow('oxxostudio', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)
b, g, r = cv2.split(img)
print(b)
print(g)
print(r)
cv2.imshow('oxxostudio', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img_blue = cv2.imread(filename)
img_green = cv2.imread(filename)
img_red = cv2.imread(filename)
img_blue[:,:,1] = 0    # 將綠色設為 0
img_blue[:,:,2] = 0    # 將紅色設為 0
img_green[:,:,0] = 0   # 將藍色設為 0
img_green[:,:,2] = 0   # 將紅色設為 0
img_red[:,:,0] = 0     # 將藍色設為 0
img_red[:,:,1] = 0     # 將綠色設為 0
cv2.imshow('oxxostudio blue', img_blue)
cv2.imshow('oxxostudio green', img_green)
cv2.imshow('oxxostudio red', img_red)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 轉換成灰階影像
cv2.imwrite('tmp_oxxo', img)
cv2.waitKey(0)                               # 按下任意鍵停止
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

""" webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 轉換成灰階影像
    cv2.imshow('oxxostudio', gray)
    if cv2.waitKey(1) == ord('q'):
        break      # 按下 q 鍵停止
cap.release()
cv2.destroyAllWindows()
"""

print("------------------------------------------------------------")  # 60個

img = cv2.imread('mona.jpg')
rows = img.shape[0]     # 取得高度的總像素
cols = img.shape[1]     # 取得寬度的總像素

for row in range(rows):
    for col in range(cols):
        img[row, col, 0] = 255 - img[row, col, 0]   # 255 - 藍色
        img[row, col, 1] = 255 - img[row, col, 1]   # 255 - 綠色
        img[row, col, 2] = 255 - img[row, col, 2]   # 255 - 紅色

cv2.imshow('oxxostudio', img)
cv2.waitKey(0)          # 按下任意鍵停止
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = cv2.imread('mona.jpg')
rows = img.shape[0]
cols = img.shape[1]

for row in range(int(rows/2)):  # 只取 rows 的一半 ( 使用 int 取整數 )
    for col in range(cols):
        img[row, col, 0] = 255 - img[row, col, 0]
        img[row, col, 1] = 255 - img[row, col, 1]
        img[row, col, 2] = 255 - img[row, col, 2]

cv2.imshow('oxxostudio', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = cv2.imread('mona.jpg')

img = 255-img # 使用 255 減去陣列中所有數值

cv2.imshow('oxxostudio', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = cv2.imread('mona.jpg')

contrast = 200
brightness = 0
output = img * (contrast/127 + 1) - contrast + brightness # 轉換公式
# 轉換公式參考 https://stackoverflow.com/questions/50474302/how-do-i-adjust-brightness-contrast-and-vibrance-with-opencv-python

# 調整後的數值大多為浮點數，且可能會小於 0 或大於 255
# 為了保持像素色彩區間為 0～255 的整數，所以再使用 np.clip() 和 np.uint8() 進行轉換
output = np.clip(output, 0, 255)
output = np.uint8(output)

cv2.imshow('oxxostudio1', img)    # 原始圖片
cv2.imshow('oxxostudio2', output) # 調整亮度對比的圖片
cv2.waitKey(0)                    # 按下任意鍵停止
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = cv2.imread('mona.jpg')
output = img    # 建立 output 變數

alpha = 1
beta = 10

cv2.convertScaleAbs(img, output, alpha, beta)  # 套用 convertScaleAbs
cv2.imshow('oxxostudio', output)
cv2.waitKey(0)      # 按下任意鍵停止
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = cv2.imread('gradient.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY); # 轉換前，都先將圖片轉換成灰階色彩
ret, output1 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)     # 如果大於 127 就等於 255，反之等於 0。
ret, output2 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV) # 如果大於 127 就等於 0，反之等於 255。
ret, output3 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TRUNC)      # 如果大於 127 就等於 127，反之數值不變。
ret, output4 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TOZERO)     # 如果大於 127 數值不變，反之數值等於 0。
ret, output5 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TOZERO_INV) # 如果大於 127 等於 0，反之數值不變。

cv2.imshow('oxxostudio', img)
cv2.imshow('oxxostudio1', output1)
cv2.imshow('oxxostudio2', output2)
cv2.imshow('oxxostudio3', output3)
cv2.imshow('oxxostudio4', output4)
cv2.imshow('oxxostudio5', output5)
cv2.waitKey(0)    # 按下任意鍵停止
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = cv2.imread('test.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY); # 轉換前，都先將圖片轉換成灰階色彩
ret, output1 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
output2 = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
output3 = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imshow('oxxostudio', img)
cv2.imshow('oxxostudio1', output1)
cv2.imshow('oxxostudio2', output2)
cv2.imshow('oxxostudio3', output3)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = cv2.imread('test.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
output1 = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
img_gray2 = cv2.medianBlur(img_gray, 5)   # 模糊化
output2 = cv2.adaptiveThreshold(img_gray2, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imshow('oxxostudio1', output1)
cv2.imshow('oxxostudio2', output2)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

""" webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    # 套用自適應二值化黑白影像
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY);
    img_gray = cv2.medianBlur(img_gray, 5)
    output = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    cv2.imshow('oxxostudio', output)
    if cv2.waitKey(1) == ord('q'):
        break       # 按下 q 鍵停止
cap.release()
cv2.destroyAllWindows()
"""

print("------------------------------------------------------------")  # 60個

img_red = cv2.imread('test-red.png')
img_green = cv2.imread('test-green.png')
img_blue = cv2.imread('test-blue.png')

output = cv2.add(img_red, img_green)  # 疊加紅色和綠色
output = cv2.add(output, img_blue)    # 疊加藍色

cv2.imshow('oxxostudio', output)
cv2.waitKey(0)     # 按下任意鍵停止
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)
logo = cv2.imread('opencv-logo.jpg')
output = cv2.addWeighted(img, 0.5, logo, 0.3, 50)

cv2.imshow('oxxostudio', output)
cv2.waitKey(0)      # 按下任意鍵停止
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = cv2.imread('test.png')
img2 = cv2.imread('test2.png')
output = cv2.subtract(img, img2)  # 相減
cv2.imwrite('tmp_output.png', output)
cv2.waitKey(0)       # 按下任意鍵停止
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

""" webcam
cap = cv2.VideoCapture(0)
logo = cv2.imread('opencv-logo.jpg')
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    img_1 = cv2.resize(frame,(480, 360))    # 改變影像尺寸，符合疊加的圖片
    output = cv2.addWeighted(img_1, 0.5, logo, 0.3, 50)  # 疊加圖片
    cv2.imshow('oxxostudio', output)
    if cv2.waitKey(1) == ord('q'):
        break      # 按下 q 鍵停止
cap.release()
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個

w, h = 400, 400
img1 = np.zeros([h,w,3])
for i in range(h):
    img[i,:,1] = int(256*i/400)   # 從上往下填入綠色漸層

img = img.astype('float32')/255   # 轉換內容類型

cv2.imshow('oxxostudio', img)
cv2.waitKey(0)                    # 按下任意鍵停止
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

w = 400
h = 400
img = np.zeros([h,w,3])
for i in range(h):
    for j in range(w):
        img[i,j,0] = int(256*(j+i)/(w+h))
        img[i,j,2] = int(256*(j+i)/(w+h))

img = img.astype('float32')/255

cv2.imshow('oxxostudio', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

w = 400
h = 400
img = np.zeros([h,w,4])             # 第三個值為 4
for i in range(h):
    img[i,:,3] = int(256*i/400)     # 設定第四個值 ( 透明度 )

img = img.astype('float32')/255

cv2.imwrite('tmp_oxxostudio.png', img)  # 儲存為 png

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img1 = cv2.imread('test.jpg', cv2.IMREAD_UNCHANGED)
img2 = cv2.imread('test.png', cv2.IMREAD_UNCHANGED)
print(img1.shape)    # (400, 300, 3)  JPG 只有三個色版 BGR
print(img2.shape)    # (400, 300, 4)  PNG 四個色版 GRA

print("------------------------------------------------------------")  # 60個

img = cv2.imread('test.jpg', cv2.IMREAD_UNCHANGED)
img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)  # 轉換成 BGRA 色彩模式
print(img.shape)                             # (400, 300, 4)  第三個數值變成 4

print("------------------------------------------------------------")  # 60個

img = cv2.imread('logo.jpg', cv2.IMREAD_UNCHANGED)  # 開啟圖片
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

cv2.imwrite('tmp_oxxostudio.png', img)    # 存檔儲存為 png

cv2.waitKey(0)                        # 按下任意鍵停止
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = cv2.imread('logo.jpg', cv2.IMREAD_UNCHANGED)
img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

h = img.shape[0]
w = img.shape[1]

for x in range(w):
    for y in range(h):
        if gray[y, x]>200:
            img[y, x] = [0,255,255,255]  # 換成黃色

cv2.imwrite('tmp_oxxostudio.png', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

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

cv2.imwrite('tmp_oxxostudio.png', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = cv2.imread('japan.jpeg')

def floodFill(source, mask, seedPoint, newVal, loDiff, upDiff, flags=cv2.FLOODFILL_FIXED_RANGE):
    result = source.copy()
    cv2.floodFill(result, mask=mask, seedPoint=seedPoint, newVal=newVal, loDiff=loDiff, upDiff=upDiff, flags=flags)
    return result

h, w = img.shape[:2]                     # 取得原始影像的長寬
mask = np.zeros((h+2,w+2,1), np.uint8)   # 製作 mask，長寬都要加上 2
output = floodFill(img, mask, (100,10), (0,0,255), (100,100,60), (100,100,100))

cv2.imshow('oxxostudio', output)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

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

cv2.imshow('oxxostudio', output)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)   # 開啟圖片
output_0 = cv2.flip(img, 0)    # 上下翻轉
output_1 = cv2.flip(img, 1)    # 左右翻轉
output_2 = cv2.flip(img, -1)   # 上下左右翻轉

cv2.imwrite('tmp_meme_0.jpg', output_0)
cv2.imwrite('tmp_meme_1.jpg', output_1)
cv2.imwrite('tmp_meme_2.jpg', output_2)

print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)
output = cv2.transpose(img)    # 逆時針旋轉 90 度。
cv2.imwrite('tmp_output.jpg', output)

print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)
output_ROTATE_90_CLOCKWISE = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
output_ROTATE_90_COUNTERCLOCKWISE = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
output_ROTATE_180 = cv2.rotate(img, cv2.ROTATE_180)
cv2.imwrite('tmp_output_1.jpg', output_ROTATE_90_CLOCKWISE)
cv2.imwrite('tmp_output_2.jpg', output_ROTATE_90_COUNTERCLOCKWISE)
cv2.imwrite('tmp_output_3.jpg', output_ROTATE_180)

print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)
output_1 = cv2.resize(img, (200, 200))   # 產生 200x200 的圖
output_2 = cv2.resize(img, (100, 300))   # 產生 100x300 的圖
cv2.imwrite('tmp_output_1.jpg', output_1)
cv2.imwrite('tmp_output_2.jpg', output_2)

print("------------------------------------------------------------")  # 60個

""" webcam
cap = cv2.VideoCapture(0)                         # 讀取電腦攝影機鏡頭影像。
fourcc = cv2.VideoWriter_fourcc(*'MJPG')          # 設定影片的格式為 MJPG
out = cv2.VideoWriter('output_1.mp4', fourcc, 20.0, (640,  360))  # 產生空的影片，尺寸為 640x360
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    img_1 = cv2.resize(frame,(640, 360))   # 改變圖片尺寸
    img_2 = cv2.flip(img_1, 0)             # 上下翻轉
    out.write(img_2)                       # 將取得的每一幀圖像寫入空的影片
    cv2.imshow('oxxostudio', frame)
    if cv2.waitKey(1) == ord('q'):
        break                              # 按下 q 鍵停止
cap.release()
out.release()      # 釋放資源
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)
M = np.float32([[1, 0, 100], [0, 1, 100]]) # 2x3 矩陣，x 軸平移 100，y 軸平移 100
output = cv2.warpAffine(img, M, (480, 360))
cv2.imshow('oxxostudio', output)

print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)
M = cv2.getRotationMatrix2D((240, 180), 45, 1)    # 中心點 (240, 180)，旋轉 45 度，尺寸 1
output = cv2.warpAffine(img, M, (480, 360))
cv2.imshow('oxxostudio', output)

print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)
p1 = np.float32([[100,100],[480,0],[0,360]])
p2 = np.float32([[0,0],[480,0],[0,360]])
M = cv2.getAffineTransform(p1, p2)
output = cv2.warpAffine(img, M, (480, 360))
cv2.imshow('oxxostudio', output)

print("------------------------------------------------------------")  # 60個

p1 = np.float32([[100,100],[480,0],[0,360],[480,360]])
p2 = np.float32([[0,0],[480,0],[0,360],[480,360]])
m = cv2.getPerspectiveTransform(p1,p2)

img = cv2.imread(filename)
output = cv2.warpPerspective(img, m, (480, 360))
cv2.imshow('oxxostudio', output)

print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)
x = 100
y = 100
w = 200
h = 200
crop_img = img[y:y+h, x:x+w]        # 取出陣列的範圍
cv2.imwrite('tmp_output.jpg', crop_img) # 儲存圖片
cv2.imshow('oxxostudio', crop_img)
cv2.waitKey(0)                      # 按下任意鍵停止
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)
x = 100
y = 100
w = 200
h = 200
crop_img = img[y:y+h, x:x+w]

output = np.zeros((360,480,3), dtype='uint8') # 產生黑色畫布
output[x:x+w, y:y+h]=crop_img

cv2.imwrite('tmp_output.jpg', output)
cv2.imshow('oxxostudio', output)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = np.zeros((300,300,3), dtype='uint8')   # 繪製 300x300 的黑色畫布
cv2.line(img,(50,50),(250,250),(0,0,255),5)  # 繪製線條
cv2.imshow('oxxostudio', img)
cv2.waitKey(0)                               # 按下任意鍵停止
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = np.zeros((300,300,3), dtype='uint8')
cv2.arrowedLine(img,(50,50),(250,250),(0,0,255),5)  # 繪製箭頭線條
cv2.imshow('oxxostudio', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = np.zeros((300,300,3), dtype='uint8')
cv2.rectangle(img,(50,50),(250,250),(0,0,255),5)  # 繪製正方形
cv2.imshow('oxxostudio', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = np.zeros((300,300,3), dtype='uint8')
cv2.rectangle(img,(50,50),(250,250),(0,0,255),-1)  # 設定 -1
cv2.imshow('oxxostudio', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = np.zeros((300,300,3), dtype='uint8')
img[50:250, 50:250] = [0,0,255] # 將中間 200x200 的陣列內容改成 [0,0,255]
cv2.imshow('oxxostudio', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = np.zeros((300,300,3), dtype='uint8')
cv2.circle(img,(150,150),100,(0,0,255),5)  # 繪製圓形
cv2.imshow('oxxostudio', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = np.zeros((300,300,3), dtype='uint8')
cv2.circle(img,(150,150),100,(0,0,255),-1)  # 設定 -1
cv2.imshow('oxxostudio', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = np.zeros((300,300,3), dtype='uint8')
cv2.ellipse(img,(150,150),(100,50),45,0,360,(0,0,255),5)
cv2.ellipse(img,(150,150),(30,100),90,0,360,(255,150,0),5)
cv2.ellipse(img,(150,150),(20,120),30,0,360,(0,255,255),5)
cv2.imshow('oxxostudio', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = np.zeros((300,300,3), dtype='uint8')
pts = np.array([[150,50],[250,100],[150,250],[50,100]])   # 產生座標陣列
cv2.polylines(img,[pts],True,(0,0,255),5)   # 繪製多邊形
cv2.imshow('oxxostudio', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = np.zeros((300,300,3), dtype='uint8')
pts = np.array([[150,50],[250,100],[150,250],[50,100]])
cv2.fillPoly(img,[pts],(0,0,255))
cv2.imshow('oxxostudio', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = np.zeros((150,300,3), dtype='uint8')   # 建立 300x150 的黑色畫布
text = 'Hello'
org = (20,90)
fontFace = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 2.5
color = (0,0,255)
thickness = 5
lineType = cv2.LINE_AA
cv2.putText(img, text, org, fontFace, fontScale, color, thickness, lineType)
cv2.imshow('oxxostudio', img)
cv2.waitKey(0)      # 按下任意鍵停止
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

from PIL import ImageFont, ImageDraw, Image    # 載入 PIL 相關函式庫

img = np.zeros((150,300,3), dtype='uint8')   # 繪製黑色畫布
fontpath = 'NotoSansTC-Regular.otf'          # 設定字型路徑
font = ImageFont.truetype(fontpath, 50)      # 設定字型與文字大小
imgPil = Image.fromarray(img)                # 將 img 轉換成 PIL 影像
draw = ImageDraw.Draw(imgPil)                # 準備開始畫畫
draw.text((0, 0), '大家好～\n嘿嘿嘿～', fill=(255, 255, 255), font=font)  # 畫入文字，\n 表示換行
img = np.array(imgPil)                       # 將 PIL 影像轉換成 numpy 陣列
cv2.imshow('oxxostudio', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)
output1 = cv2.blur(img, (5, 5))     # 指定區域單位為 (5, 5)
output2 = cv2.blur(img, (25, 25))   # 指定區域單位為 (25, 25)
cv2.imshow('oxxostudio1', output1)
cv2.imshow('oxxostudio2', output2)
cv2.waitKey(0)                      # 按下任意鍵停止
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)
output1 = cv2.GaussianBlur(img, (5, 5), 0)   # 指定區域單位為 (5, 5)
output2 = cv2.GaussianBlur(img, (25, 25), 0) # 指定區域單位為 (25, 25)
cv2.imshow('oxxostudio1', output1)
cv2.imshow('oxxostudio2', output2)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)
output1 = cv2.medianBlur(img, 5)   # 模糊程度為 5
output2 = cv2.medianBlur(img, 25)  # 模糊程度為 25
cv2.imshow('oxxostudio1', output1)
cv2.imshow('oxxostudio2', output2)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)
output1 = cv2.bilateralFilter(img, 50, 0, 0)
output2 = cv2.bilateralFilter(img, 50, 50, 100)
output3 = cv2.bilateralFilter(img, 50, 100, 1000)
cv2.imshow('oxxostudio1', output1)
cv2.imshow('oxxostudio2', output2)
cv2.imshow('oxxostudio3', output3)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

""" webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    # 套用 medianBlur() 中值模糊
    img = cv2.medianBlur(frame, 25)
    cv2.imshow('oxxostudio', img)
    if cv2.waitKey(1) == ord('q'):
        break     # 按下 q 鍵停止
cap.release()
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個

img = cv2.imread('mona.jpg')
size = img.shape         # 取得原始圖片的資訊
level = 15               # 縮小比例 ( 可當作馬賽克的等級 )
h = int(size[0]/level)   # 按照比例縮小後的高度 ( 使用 int 去除小數點 )
w = int(size[1]/level)   # 按照比例縮小後的寬度 ( 使用 int 去除小數點 )
mosaic = cv2.resize(img, (w,h), interpolation=cv2.INTER_LINEAR)   # 根據縮小尺寸縮小
mosaic = cv2.resize(mosaic, (size[1],size[0]), interpolation=cv2.INTER_NEAREST) # 放大到原本的大小
cv2.imshow('oxxostudio', mosaic)
cv2.waitKey(0)           # 按下任意鍵停止
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = cv2.imread('mona.jpg')

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
cv2.imshow('oxxostudio', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

""" webcam
cap1 = cv2.VideoCapture(0)           # 讀取第一個影片來源
cap2 = cv2.VideoCapture(1)           # 讀取第二個影片來源

if not cap1.isOpened():
    print("Cannot open camera1")
    exit()
if not cap2.isOpened():
    print("Cannot open camera2")
    exit()

while True:
    ret1, img1 = cap1.read()         # 讀取第一個來源影片的每一幀
    ret2, img2 = cap2.read()         # 讀取第一個來源影片的每一幀

    cv2.imshow('oxxostudio1', img1)  # 如果讀取成功，顯示該幀的畫面
    cv2.imshow('oxxostudio2', img2)  # 如果讀取成功，顯示該幀的畫面
    if cv2.waitKey(1) == ord('q'):
        break
cap1.release()
cap2.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

cap1 = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)

if not cap1.isOpened():
    print("Cannot open camera1")
    exit()
if not cap2.isOpened():
    print("Cannot open camera2")
    exit()

while True:
    ret1, img1 = cap1.read()
    ret2, img2 = cap2.read()
    img1 = cv2.resize(img1,(200,150))  # 縮小尺寸
    img2 = cv2.resize(img2,(540,320))  # 縮小尺寸
    img2[160:310,330:530] = img1       # 將 img2 的特定區域換成 img1

    cv2.rectangle(img2, (330,160), (530,310), (255,255,255), 5)  # 繪製子影片的外框

    cv2.imshow('oxxostudio', img2)
    if cv2.waitKey(1) == ord('q'):
        break
cap1.release()
cap2.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

cap = cv2.VideoCapture(0)
output = np.zeros((360,640,3), dtype='uint8')   # 產生 640x360 的黑色背景

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, img = cap.read()
    img = cv2.resize(img, (640, 360))   # 改變影像尺寸為 640x360
    img = img[:360, :320]               # 取出 320x360 的影像
    img2 = cv2.flip(img, 1)             # 左右翻轉影像
    output[:, :320] = img               # 將 output 左邊內容換成 img
    output[:, 320:640] = img2           # 將 output 右邊內容換成 img2

    cv2.imshow('oxxostudio', output)
    if cv2.waitKey(50) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

cap = cv2.VideoCapture(0)
output = np.zeros((640,640,3), dtype='uint8')

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, img = cap.read()
    img = cv2.resize(img,(640, 360))
    img = img[:320, :320]             # 取出 320x320 的區域
    img2 = cv2.flip(img, 1)           # 左右翻轉
    img3 = cv2.flip(img, 0)           # 上下翻轉
    img4 = cv2.flip(img, -1)          # 上下左右翻轉
    output[:320, :320] = img          # 左上
    output[:320, 320:640] = img2      # 右上
    output[320:640, :320] = img3      # 左下
    output[320:640, 320:640] = img4   # 右下

    cv2.imshow('oxxostudio', output)
    if cv2.waitKey(50) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

cap = cv2.VideoCapture(0)                      # 讀取攝影鏡頭
output = np.zeros((360,640,3), dtype='uint8')  # 產生 640x360 的黑色背景

if not cap.isOpened():
    print("Cannot open camera")
    exit()

n = 5                                  # 設定要分成幾格
w = 640//n                             # 計算分格之後的影像寬度 ( // 取整數 )
h = 360//n                             # 計算分格之後的影像高度 ( // 取整數 )
while True:
    ret, img = cap.read()              # 讀取影像
    img = cv2.resize(img,(w, h))       # 縮小尺寸
    output[0:h, 0:w] = img             # 將 output 的特定區域置換為 img
    cv2.imshow('oxxostudio', output)
    if cv2.waitKey(50) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

cap = cv2.VideoCapture(0)
output = np.zeros((360,640,3), dtype='uint8')

if not cap.isOpened():
    print("Cannot open camera")
    exit()

n = 5
w = 640//n
h = 360//n
img_list = []        # 設定空串列，記錄每一格的影像
while True:
    ret, img = cap.read()
    img = cv2.resize(img,(w, h))
    img_list.append(img)                    # 每次擷取影像時，將影像存入串列
    if len(img_list)>n*n: del img_list[0]   # 如果串列長度超過可容納的影像數量，移除第一個項目
    for i in range(len(img_list)):
        x = i%n      # 根據串列計算影像的 x 座標 ( 取餘數 )
        y = i//n     # 根據串列計算影像的 y 座標 ( 取整數 )
        output[h*y:h*y+h, w*x:w*x+w] = img_list[i]  # 更新畫面

    cv2.imshow('oxxostudio', output)
    if cv2.waitKey(50) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

w, h = 640, 360                                   # 定義長寬
x = 0                                             # 定義 x 從 0 開始
while True:
    ret, img = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    img = cv2.resize(img,(w,h))                   # 縮小尺寸加快速度
    img = cv2.flip(img, 1)                        # 翻轉影像，使其如同鏡子
    img = img[:, int((w-h)/2):int((h+(w-h)/2))]   # 將影像變成正方形
    cv2.line(img,(x,0),(x,h),(0,0,255),5)         # 畫線
    cv2.imshow('oxxostudio',img)                  # 正常狀況下，一直顯示即時影像
    x = x + 2
    if x > h:
        x = 0
    keyCode = cv2.waitKey(10)                     # 等待鍵盤事件
    if keyCode == ord('q'):
        break                                     # 按下 q 就全部結束

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

w, h = 640, 360                                   # 定義長寬
a = 1                                             # 存檔的檔名編號從 1 開始
run = 0                                           # 是否開始，0 表示尚未開始，1 表示開始
output = np.zeros((h,h,3), dtype='uint8')         # 設定合成的影像為一張全黑的畫布 ( 長寬使用正方形 )
while True:
    ret, img = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    img = cv2.resize(img,(w,h))                   # 縮小尺寸加快速度
    img = cv2.flip(img, 1)                        # 翻轉影像，使其如同鏡子
    img = img[:, int((w-h)/2):int((h+(w-h)/2))]   # 將影像變成正方形

    keyCode = cv2.waitKey(10)                     # 等待鍵盤事件
    if keyCode == ord('a') and run == 0:
        x = 0                                     # 如果按下 a，設定 x 為 0
        run = 1                                   # 開始合成
    elif keyCode == ord('q'):
        break                                     # 按下 q 就全部結束

    if run == 1:
        output[0:h, x:x+2] = img[0:h, x:x+2]      # 設定 output 的某個區域為即時影像 img 的某區域
        cv2.line(img,(x+5,0),(x+5,h),(0,0,255),5) # 畫線 ( 因為線條寬度 5，所以位移 5 )
        x = x + 2                                 # 改變 x 位置
        img[0:h,0:x] = output[0:h,0:x]            # 設定即時影像 img 的某區域為 output
        cv2.imshow('oxxostudio',img)              # 顯示即時影像
        if x > h:
            keyCode = cv2.waitKey() == ord('s')   # 如果寬度抵達正方形邊緣，等待鍵盤事件按下 s
            cv2.imwrite(f'tmp_oxxo-{a}.jpg',img)      # 存檔
            a = a + 1                             # 檔名編號增加 1
            run = 0                               # 停止合成
    else:
        cv2.imshow('oxxostudio',img)              # 正常狀況下，一直顯示即時影像

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

w, h = 640, 360                                   # 定義長寬
a = 1                                             # 存檔的檔名編號從 1 開始
run = 0                                           # 是否開始，0 表示尚未開始，1 表示開始
output = np.zeros((h,h,3), dtype='uint8')         # 設定合成的影像為一張全黑的畫布
while True:
    ret, img = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    img = cv2.resize(img,(w,h))                   # 縮小尺寸加快速度
    img = cv2.flip(img, 1)                        # 翻轉影像，使其如同鏡子
    img = img[:, int((w-h)/2):int((h+(w-h)/2))]   # 將影像變成正方形

    keyCode = cv2.waitKey(10)                     # 等待鍵盤事件
    if keyCode == ord('a') and run == 0:
        y = 0                                     # 如果按下 a，設定 y 為 0
        run = 1                                   # 開始合成
    elif keyCode == ord('q'):
        break                                     # 按下 q 就全部結束

    if run == 1:
        output[y:y+2, 0:h] = img[y:y+2, 0:h]      # 設定 output 的某個區域為即時影像 img 的某區域
        cv2.line(img,(0,y+5),(h,y+5),(0,0,255),5) # 畫線
        y = y + 2                                 # 改變 x 位置
        img[0:y,0:h] = output[0:y,0:h]            # 設定即時影像 img 的某區域為 output
        cv2.imshow('oxxostudio',img)              # 顯示即時影像
        if y > h:
            keyCode = cv2.waitKey() == ord('s')   # 如果寬度抵達正方形邊緣，等待鍵盤事件按下 s
            cv2.imwrite(f'tmp_oxxo-{a}.jpg',img)      # 存檔
            a = a + 1                             # 檔名編號增加 1
            run = 0                               # 停止合成
    else:
        cv2.imshow('oxxostudio',img)              # 正常狀況下，一直顯示即時影像

cap.release()
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個

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

img = cv2.imread('mona.jpg')
img = convex(img, (300, 400, 3), (150, 130, 100))      # 提交參數數值，進行凸透鏡效果
cv2.imshow('oxxostudio', img)
cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

""" webcam
def convex(src_img, raw, effect):
    col, row, channel = raw[:]
    cx, cy, r = effect[:]
    output = np.zeros([row, col, channel], dtype = np.uint8)
    for y in range(row):
        for x in range(col):
            d = ((x - cx) * (x - cx) + (y - cy) * (y - cy)) ** 0.5
            if d <= r:
                nx = int((x - cx) * d / r + cx)
                ny = int((y - cy) * d / r + cy)
                output[y, x, :] = src_img[ny, nx, :]
            else:
                output[y, x, :] = src_img[y, x, :]
    return output

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, img = cap.read()               # 讀取影片的每一幀
    if not ret:
        print("Cannot receive frame")   # 如果讀取錯誤，印出訊息
        break
    scale = 0.75
    w, h = int(640*scale), int(320*scale)
    cw, ch = int(w/2), int(h/2)            # 取得中心點
    img = cv2.resize(img,(w, h))           # 調整尺寸，加快速度
    img = convex(img, (w, h, 3), (cw, ch, 100))
    cv2.imshow('oxxostudio', img)
    if cv2.waitKey(100) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個

img = cv2.imread('mona.jpg')                         # 開啟圖片
img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)          # 轉換成 BGRA ( 因為需要 alpha 色版 )
w = img.shape[1]                                     # 取得寬度
h = img.shape[0]                                     # 取得高度
white = 255 - np.zeros((h,w,4), dtype='uint8')       # 建立白色圖
a = 1                                                # 一開始 a 為 1
while True:
    a = a - 0.01                                     # a 不斷減少 0.01
    if a<0: a = 0                                    # 如果 a 小於 0 就讓 a 等於 0
    output = cv2.addWeighted(white, a, img, 1-a, 0)  # 根據 a 套用權重
    cv2.imshow('oxxostudio', output)                 # 顯示圖片
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()                           # 所有作業都完成後，釋放資源
cv2.destroyAllWindows()                 # 結束所有視窗

print("------------------------------------------------------------")  # 60個

""" webcam
cap = cv2.VideoCapture(0)

img = cv2.imread('mona.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
w = img.shape[1]
h = img.shape[0]
white = 255 - np.zeros((h,w,4), dtype='uint8')
a = 0                       # 開始時 a 等於 0
while True:

    key = cv2.waitKey(1)    # 偵測按鍵
    if key == 32:
        a = 1               # 如果按下空白鍵，讓 a 等於 1
    elif key == ord('q'):
        break

    if a == 0:
        output = img.copy() # 如果 a 等於 0，複製來源圖片為 output
    else:
        output = cv2.addWeighted(white, a, img, 1-a, 0)  # 如果 a 等於 1，根據 a 套用權重
        a = a - 0.01        # a 不斷減少 0.01
        if a<0: a = 0       # 如果 a 小於 0 就讓 a 等於 0

    cv2.imshow('oxxostudio', output)

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

cap = cv2.VideoCapture(0)

a = 0    # 白色圖片透明度
n = 0    # 檔名編號

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, img = cap.read()               # 讀取影片的每一幀
    if not ret:
        print("Cannot receive frame")   # 如果讀取錯誤，印出訊息
        break
    img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)  # 轉換顏色為 BGRA
    w = int(img.shape[1]*0.5)           # 縮小寬度為一半
    h = int(img.shape[0]*0.5)           # 縮小高度為一半
    img = cv2.resize(img,(w,h))         # 縮放尺寸
    white = 255 - np.zeros((h,w,4), dtype='uint8')   # 產生全白圖片

    key = cv2.waitKey(1)
    if key == 32:            # 按下空白將 a 等於 1
        a = 1
    elif key == ord('q'):    # 按下 q 結束
        break

    if a == 0:
        output = img.copy()  # 如果 a 為 0，設定 output 變數為來源圖片的拷貝
    else:
        photo = img.copy()   # 如果 a 不為 0，設定 photo 變數為來源圖片的拷貝
        output = cv2.addWeighted(white, a, photo, 1-a, 0)  # 計算權重，產生白色慢慢消失效果
        a = a - 0.1
        if a<0:
            a = 0
            n = n + 1
            cv2.imwrite(f'tmp_photo-{n}.jpg', photo)   # 存檔

    cv2.imshow('oxxostudio', output)               # 顯示圖片

cap.release()                           # 所有作業都完成後，釋放資源
cv2.destroyAllWindows()                 # 結束所有視窗

print("------------------------------------------------------------")  # 60個

cap = cv2.VideoCapture(0)

# 定義加入文字的函式
def putText(source, x, y, text, scale=2.5, color=(255,255,255)):
    org = (x,y)
    fontFace = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = scale
    thickness = 5
    lineType = cv2.LINE_AA
    cv2.putText(source, text, org, fontFace, fontScale, color, thickness, lineType)

a = 0
n = 0

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, img = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
    w = int(img.shape[1]*0.5)
    h = int(img.shape[0]*0.5)
    img = cv2.resize(img,(w,h))
    white = 255 - np.zeros((h,w,4), dtype='uint8')

    key = cv2.waitKey(1)
    if key == 32:
        a = 1
        sec = 4  # 加入倒數秒數
    elif key == ord('q'):
        break
    if a == 0:
        output = img.copy()
    else:
        output = img.copy()  # 設定 output 和 photo 變數
        photo = img.copy()
        sec = sec - 0.05     # sec 不斷減少 0.05 ( 根據個人電腦效能設定，使其搭配 while 迴圈看起來像倒數一秒 )
        putText(output, 10, 70, str(int(sec)))  # 加入文字
        # 如果秒數小於 1
        if sec < 1:
            output = cv2.addWeighted(white, a, photo, 1-a, 0)
            a = a - 0.1
            if a<0:
                a = 0
                n = n + 1
                cv2.imwrite(f'tmp_photo-{n}.jpg', photo)
    cv2.imshow('oxxostudio', output)

cap.release()
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個

img = cv2.imread('mona.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 轉成灰階
img = cv2.medianBlur(img, 7)                 # 模糊化，去除雜訊
output = cv2.Laplacian(img, -1, 1, 5)        # 偵測邊緣
cv2.imshow('oxxostudio', output)
cv2.waitKey(0)                               # 按下任意鍵停止
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = cv2.imread('mona.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 轉成灰階
img = cv2.medianBlur(img, 7)                 # 模糊化，去除雜訊
output = cv2.Sobel(img, -1, 1, 1, 1, 7)      # 偵測邊緣
cv2.imshow('oxxostudio', output)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = cv2.imread('mona.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 轉成灰階
img = cv2.medianBlur(img, 7)                 # 模糊化，去除雜訊
output = cv2.Canny(img, 36, 36)              # 偵測邊緣
print(output)
cv2.imshow('oxxostudio', output)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
""" webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 轉成灰階
    img = cv2.medianBlur(img, 7)                   # 模糊化，去除雜訊
    img = cv2.Canny(img, 36, 36)                   # 偵測邊緣
    cv2.imshow('oxxostudio', img)
    if cv2.waitKey(1) == ord('q'):
        break                                      # 按下 q 鍵停止
cap.release()
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個

img = cv2.imread('test.jpg')
cv2.imshow('oxxostudio1', img)   # 原始影像

img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))

img = cv2.erode(img, kernel)     # 先侵蝕，將白色小圓點移除
cv2.imshow('oxxostudio2', img)   # 侵蝕後的影像

img = cv2.dilate(img, kernel)    # 再膨脹，白色小點消失
cv2.imshow('oxxostudio3', img)   # 膨脹後的影像

cv2.waitKey(0)                   # 按下 q 鍵停止
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img1 = cv2.imread('test1.png')
img2 = cv2.imread('test2.png')
output = cv2.bitwise_and(img1, img2)  # 使用 bitwise_and
cv2.imshow('oxxostudio', output)
cv2.waitKey(0)                        # 按下任意鍵停止
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img1 = cv2.imread('test1.png')
img2 = cv2.imread('test2.png')
output = cv2.bitwise_or(img1, img2)  # 使用 bitwise_or
cv2.imshow('oxxostudio', output)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img1 = cv2.imread('test1.png')
img2 = cv2.imread('test2.png')
output = cv2.bitwise_xor(img1, img2)  # 使用 bitwise_xor
cv2.imshow('oxxostudio', output)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img1 = cv2.imread('test1.png')
output = cv2.bitwise_not(img1)  # 使用 bitwise_not
cv2.imshow('oxxostudio', output)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img1 = cv2.imread('test1.png')
img2 = cv2.imread('test2.png')
mask = cv2.imread('mask.png')                    # 遮罩圖片
mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)    # 轉換成灰階模式
output = cv2.bitwise_xor(img1, img2, mask=mask)  # 加入 mask 參數
cv2.imshow('oxxostudio', output)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

logo = cv2.imread('logo.jpg')                    # 讀取 OpenCV 的 logo
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
cv2.imshow('oxxostudio', output)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

"""
logo = cv2.imread('logo.jpg')
size = logo.shape
img = np.zeros((360,600,3), dtype='uint8')
img[0:360, 0:600] = '255'
img[0:size[0], 0:size[1]] = logo
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, mask1  = cv2.threshold(img_gray, 200, 255, cv2.THRESH_BINARY_INV)
logo = cv2.bitwise_and(img, img, mask = mask1 )
ret, mask2  = cv2.threshold(img_gray, 200, 255, cv2.THRESH_BINARY)

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    frame = cv2.resize(frame,(600, 360))   # 調整圖片尺寸
    bg = cv2.bitwise_and(frame, frame, mask = mask2 )
    output = cv2.add(bg, logo)
    cv2.imshow('oxxostudio', output)
    if cv2.waitKey(1) == ord('q'):
        break      # 按下 q 鍵停止
cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

logo = cv2.imread('logo.jpg')
size = logo.shape
img = np.zeros((360,600,3), dtype='uint8')
img[0:360, 0:600] = '255'
img[30:30+size[0], 155:155+size[1]] = logo         # 將 logo 置中
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, mask1  = cv2.threshold(img_gray, 200, 255, cv2.THRESH_BINARY_INV)

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    frame = cv2.resize(frame,(600, 360))
    output = cv2.bitwise_not(frame, mask = mask1 )      # 套用 not 和遮罩
    output = cv2.bitwise_not(output, mask = mask1 )     # 再次套用 not 和遮罩，將色彩轉成原來的顏色
    cv2.imshow('oxxostudio', output)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個

mask = np.zeros((300,300,3), dtype='uint8')      # 建立 300x300 的黑色畫布
cv2.circle(mask,(150,150),100,(255,255,255),-1)  # 在畫布上中心點加入一個半徑 100 的白色圓形
mask = cv2.GaussianBlur(mask, (35, 35), 0)       # 進行高斯模糊

cv2.imshow('oxxostudio', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

mask = np.zeros((300,300,3), dtype='uint8')
cv2.circle(mask,(150,150),100,(255,255,255),-1)
mask = cv2.GaussianBlur(mask, (35, 35), 0)
mask = mask / 255                          # 除以 255，計算每個像素的黑白色彩在 255 中所佔的比例

img = cv2.imread('mona.jpg')               # 開啟圖片
bg = np.zeros((300,300,3), dtype='uint8')  # 產生一張黑色背景
bg = 255 - bg                              # 轉換成白色背景
img = img / 255                            # 除以 255，計算每個像素的色彩在 255 中所佔的比例
bg = bg / 255                              # 除以 255，計算每個像素的色彩在 255 中所佔的比例

out  = bg * (1 - mask) + img * mask        # 根據比例混合
out = (out * 255).astype('uint8')          # 乘以 255 之後轉換成整數

cv2.imshow('oxxostudio',out)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img1 = cv2.imread('mona.jpg')
img2 = cv2.imread('girl.jpg')
w = img1.shape[1]   # 讀取圖片寬度
h = img1.shape[0]   # 讀取圖片高度

for i in range(w):
    img1[:,i,0] = img1[:,i,0]*((300-i)/300) + img2[:,i,0]*(i/300)  # 藍色按照比例混合
    img1[:,i,1] = img1[:,i,1]*((300-i)/300) + img2[:,i,1]*(i/300)  # 紅色按照比例混合
    img1[:,i,2] = img1[:,i,2]*((300-i)/300) + img2[:,i,2]*(i/300)  # 綠色按照比例混合

cv2.imwrite('tmp_oxxostudio.png', save)

show = img1.astype('float32')/255    # 如果要使用 imshow 必須要轉換類型
cv2.imshow('oxxostudio.png', show)

cv2.waitKey(0)       # 按下任意鍵停止
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

mona = cv2.imread('mona.jpg')
logo = cv2.imread('logo.png', cv2.IMREAD_UNCHANGED)  # 使用 cv2.IMREAD_UNCHANGED 讀取 png，保留 alpha 色版
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

cv2.imwrite('tmp_oxxostudio.png', mona)

mona = mona.astype('float32')/255    # 如果要使用 imshow 必須要轉換類型
cv2.imshow('oxxostudio', mona)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

from PIL import Image,ImageSequence

gif = Image.open('dot.gif')                # 讀取動畫圖檔

i = 0                                      # 設定編號變數
for frame in ImageSequence.Iterator(gif):
    frame = frame.convert('RGB')           # 取出每一格轉換成 RGB
    frame.save(f'frame{i}.jpg', quality=65, subsampling=0)  # 儲存為 jpg
    i = i + 1                              # 編號增加 1

print("------------------------------------------------------------")  # 60個

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
        cv2.imshow('oxxostudio', i)                # 不斷讀取並顯示串列中的圖片內容
        if cv2.waitKey(200) == ord('q'):
            loop = False                           # 停止時同時也將 while 迴圈停止
            break
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

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
        cv2.imshow('oxxostudio', i)
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
output[0].save("oxxostudio.gif", save_all=True, append_images=output[1:], duration=200, loop=0, disposal=0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

from PIL import Image,ImageSequence

gif = []
for i in range(4):
    img = Image.open(f'frame{i}.jpg')  # 開啟圖片
    gif.append(img)                    # 加入串列
# 儲存為 gif
gif[0].save("oxxostudio.gif", save_all=True, append_images=gif[1:], duration=200, loop=0, disposal=0)

print("------------------------------------------------------------")  # 60個

""" webcam
from PIL import Image,ImageSequence

output = []                       # 建立輸出的空串列

cap = cv2.VideoCapture(0)         # 從攝影鏡頭取得影像
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, img = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    img = cv2.resize(img, (450,240))    # 調整影片大小

    # 加上黑色區塊
    cv2.rectangle(img,(10,10),(200,42),(0,0,0),-1)

    # 加上文字
    text = 'oxxo.studio'
    org = (15,35)
    fontFace = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    color = (255,255,255)
    thickness = 2
    lineType = cv2.LINE_AA
    cv2.putText(img, text, org, fontFace, fontScale, color, thickness, lineType)

    gif = cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA)  # 轉換顏色
    gif = Image.fromarray(gif)                    # 轉換成 PIL 格式
    gif = gif.convert('RGB')                      # 轉換顏色
    output.append(gif)                            # 添加到 output

    cv2.imshow('oxxostudio', img)
    if cv2.waitKey(250) == ord('q'):
        break
cap.release()
# 儲存為 gif 動畫
output[0].save("test2.gif", save_all=True, append_images=output[1:], duration=250, loop=0, disposal=2)
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個

n = 0
for i in source:                  # source 為要轉存的所有圖片陣列 ( opencv 格式，色彩為 RGBA )
    img = Image.fromarray(i)      # 轉換成 PIL 格式
    img.save(f'temp/gif{n}.gif')  # 儲存為 gif
    n = n + 1                     # 改變儲存的檔名編號

output = []                       # 建立空串列
for i in range(n):
    img = Image.open(f'temp/gif{i}.gif')  # 依序開啟每張 gif
    img = img.convert("RGBA")             # 轉換為 RGBA
    output.append(img)                    # 記錄每張圖片內容

# 轉存為 gif 動畫，設定 disposal=2
output[0].save("oxxostudio.gif", save_all=True, append_images=output[1:], duration=100, loop=0, disposal=2)

print("------------------------------------------------------------")  # 60個

from PIL import Image,ImageSequence

cap = cv2.VideoCapture('video.mov')   # 開啟影片
source = []                           # 建立 source 空串列，記錄影格內容
frame = 0                             # frame 從 0 開始

print('loading...')
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, img = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    if frame%30 == 0:                                # 每 30 格取一格
        img = cv2.resize(img, (400,300))             # 改變尺寸，加快處理效率
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)  # 修改顏色為 RGBA
        source.append(img)                           # 記錄該圖片
    frame = frame + 1
    if cv2.waitKey(1) == ord('q'):
        break                                        # 按下 q 鍵停止
cap.release()

print('start...')
for i in range(len(source)):
    for x in range(400):
        for y in range(300):
            r = source[i][y,x,0]   # 該像素的紅色數值
            g = source[i][y,x,1]   # 該像素的綠色數值
            b = source[i][y,x,2]   # 該像素的藍色數值
            if r>35 and r<100 and g>110 and g<200 and b>60 and b< 130:
                source[i][y,x,3] = 0    # 如果在顏色範圍內，將透明度設為 0

print('export single frame to gif...')
n = 0
for i in source:
    img = Image.fromarray(i)
    img.save(f'temp/gif{n}.gif')
    n = n + 1

print('loading gifs...')
output = []
for i in range(n):
    img = Image.open(f'temp/gif{i}.gif')
    img = img.convert("RGBA")
    output.append(img)

output[0].save("test2.gif", save_all=True, append_images=output[1:], duration=100, loop=0, disposal=2)
print('ok...')

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = cv2.imread("qrcode.jpg")                       # 開啟圖片

qrcode = cv2.QRCodeDetector()                        # 建立 QRCode 偵測器
data, bbox, rectified = qrcode.detectAndDecode(img)  # 偵測圖片中的 QRCode
# 如果 bbox 是 None 表示圖片中沒有 QRCode
if bbox is not None:
    print(data)                # QRCode 的內容
    print(bbox)                # QRCode 的邊界
    print(rectified)           # 換成垂直 90 度的陣列

cv2.imshow('oxxostudio', img)  # 預覽圖片
cv2.waitKey(0)                 # 按下任意鍵停止
cv2.destroyAllWindows()        # 結束所有圖片視窗

print("------------------------------------------------------------")  # 60個

img = cv2.imread("qrcode.jpg")

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

cv2.imshow('oxxostudio', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

from PIL import ImageFont, ImageDraw, Image          # 載入 PIL ( 為了放中文字 )
img = cv2.imread("qrcode.jpg")

qrcode = cv2.QRCodeDetector()
data, bbox, rectified = qrcode.detectAndDecode(img)

# 建立放入文字的函式
def putText(x,y,text,color=(0,0,0)):
    global img
    fontpath = 'NotoSansTC-Regular.otf'      # 字體 ( 從 Google Font 下載 )
    font = ImageFont.truetype(fontpath, 20)  # 設定字型與大小
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

cv2.imshow('oxxostudio', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

from PIL import ImageFont, ImageDraw, Image
img = cv2.imread("many-qrcode.jpg")

def putText(x,y,text,color=(0,0,0)):
    global img
    fontpath = 'NotoSansTC-Regular.otf'
    font = ImageFont.truetype(fontpath, 20)
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

cv2.imshow('oxxostudio', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

from PIL import ImageFont, ImageDraw, Image
img = cv2.imread("barcode.jpg")

def putText(x,y,text,color=(0,0,0)):
    global img
    fontpath = 'NotoSansTC-Regular.otf'
    font = ImageFont.truetype(fontpath, 20)
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

cv2.imshow('oxxostudio', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

from PIL import ImageFont, ImageDraw, Image
""" webcam
cap = cv2.VideoCapture(0)

def putText(x,y,text,color=(0,0,0)):
    global img
    fontpath = 'NotoSansTC-Regular.otf'
    font = ImageFont.truetype(fontpath, 20)
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

qrcode = cv2.QRCodeDetector()             # QRCode 偵測器

while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    img = cv2.resize(frame,(720,420))     # 縮小尺寸，加快速度
    ok, data, bbox, rectified = qrcode.detectAndDecodeMulti(img)  # 辨識 QRCode
    if ok:
        for i in range(len(data)):
            text = data[i]            # QRCode 內容
            box = boxSize(bbox[i])    # QRCode 座標
            cv2.rectangle(img,(box[0],box[1]),(box[2],box[3]),(0,0,255),5)  # 繪製外框
            putText(box[0],box[3],text,color=(0,0,255))                     # 顯示文字
    cv2.imshow('oxxostudio', img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

from PIL import ImageFont, ImageDraw, Image

cap = cv2.VideoCapture(0)     # 讀取攝影鏡頭

# 定義加入文字函式
def putText(x,y,text,size=20,color=(0,0,0)):
    global img
    fontpath = 'NotoSansTC-Regular.otf'            # 字型
    font = ImageFont.truetype(fontpath, size)      # 定義字型與文字大小
    imgPil = Image.fromarray(img)                  # 轉換成 PIL 影像物件
    draw = ImageDraw.Draw(imgPil)                  # 定義繪圖物件
    draw.text((x, y), text, fill=color, font=font) # 加入文字
    img = np.array(imgPil)                         # 轉換成 np.array

# 定義馬賽克函式
def mosaic(image, level):
    size = image.shape       # 取得原始圖片的資訊
    h = int(size[0]/level)   # 按照比例縮小後的高度 ( 使用 int 去除小數點 )
    w = int(size[1]/level)   # 按照比例縮小後的寬度 ( 使用 int 去除小數點 )
    output = cv2.resize(image, (w,h), interpolation=cv2.INTER_LINEAR)   # 根據縮小尺寸縮小
    output = cv2.resize(output, (size[1],size[0]), interpolation=cv2.INTER_NEAREST) # 放大到原本的大小
    return output

qrcode = cv2.QRCodeDetector()    # QRCode 偵測器

while True:
    ret, frame = cap.read()      # 讀取攝影鏡頭影像
    if not ret:
        print("Cannot receive frame")
        break
    img = cv2.resize(frame,(720,420))   # 縮小尺寸加快速度
    ok, data, bbox, rectified = qrcode.detectAndDecodeMulti(img)  # 偵測並辨識 QRCode
    # 如果偵測到 QRCode
    if ok:
        for i in range(len(data)):
            text = data[i]           # 取出內容
            # 如果內容是 a1，套用模糊效果
            if text=='a1':
                img = cv2.blur(img, (20, 20))
                putText(0,0,'模糊效果',100,(255,255,255))
            # 如果內容是 a2，套用馬賽克效果
            elif text == 'a2':
                img = mosaic(img, 15)
                putText(0,0,'馬賽克效果',100,(255,255,255))
            # 如果內容是 a2，套用片效果
            elif text == 'a3':
                img = 255-img
                putText(0,0,'負片效果',100,(0,0,0))

    cv2.imshow('oxxostudio', img)     # 預覽影像
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
"""


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

