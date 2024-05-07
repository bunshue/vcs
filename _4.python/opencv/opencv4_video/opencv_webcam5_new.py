import os
import sys
import time
import math
import random

print("------------------------------------------------------------")  # 60個

ESC = 27

import cv2
import numpy as np

print("------------------------------------------------------------")  # 60個

print("OpenCV VideoCapture 04 兩個camera")
print('按 ESC 離開')

ratio = 3
border = 30
W = 640
H = 480

w = W//ratio
h = H//ratio
x_st = W - w - border
y_st = H - h - border

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
    img1 = cv2.resize(img1,(w, h))  # 縮小尺寸 小圖
    #img2 = cv2.resize(img2,(W, H))  # 縮小尺寸 大圖

    img2[y_st:y_st+h,x_st:x_st+w] = img1       # 將 img2 的特定區域換成 img1

    cv2.rectangle(img2, (x_st, y_st), (x_st+w,y_st+h), (255,255,255), 5)  # 繪製子影片的外框

    cv2.imshow("OpenCV 04", img2)

    k = cv2.waitKey(1) # 等待按鍵輸入
    if k == ESC:     #ESC
        break

cap1.release()
cap2.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("OpenCV VideoCapture 05 N X N")
print('按 ESC 離開')

N = 2 # 設定要分成幾格, N X N
W = 640*2
H = 480*2
cap = cv2.VideoCapture(0)                      # 讀取攝影鏡頭
output = np.zeros((H, W, 3), dtype='uint8')  # 產生 WxH 的黑色背景

if not cap.isOpened():
    print("Cannot open camera")
    exit()

w = W // N                             # 計算分格之後的影像寬度
h = H // N                             # 計算分格之後的影像高度
img_list = []        # 設定空串列，記錄每一格的影像
while True:
    ret, img = cap.read()              # 讀取影像
    img = cv2.resize(img,(w, h))       # 縮小尺寸
    """ 2X2的寫法
    output[0:h, 0:w] = img             # 將 output 的特定區域置換為 img, 左上
    output[0:h, w:w*2] = img             # 將 output 的特定區域置換為 img, 右上
    output[h:h*2, 0:w] = img             # 將 output 的特定區域置換為 img, 左下
    output[h:h*2, w:w*2] = img             # 將 output 的特定區域置換為 img, 右下

    #左右相反
    img = cv2.flip(img, 1)

    """
    img_list.append(img)                    # 每次擷取影像時，將影像存入串列
    if len(img_list) > N*N: del img_list[0]   # 如果串列長度超過可容納的影像數量，移除第一個項目
    for i in range(len(img_list)):
        x = i % N      # 根據串列計算影像的 x 座標
        y = i // N     # 根據串列計算影像的 y 座標
        output[h*y:h*y+h, w*x:w*x+w] = img_list[i]  # 更新畫面

    cv2.imshow("OpenCV 05", output)

    k = cv2.waitKey(1) # 等待按鍵輸入
    if k == ESC:     #ESC
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("OpenCV VideoCapture 10 Covex效果")
print('按 ESC 離開')

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
    w, h = 640, 480
    cw, ch = int(w/2), int(h/2)            # 取得中心點
    img = convex(img, (w, h, 3), (cw, ch, 100))
    
    cv2.imshow("OpenCV 10", img)

    k = cv2.waitKey(1) # 等待按鍵輸入
    if k == ESC:     #ESC
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("OpenCV VideoCapture 11 按鍵 慢慢顯示出一圖的效果")
print('按 ESC 離開')

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

img = cv2.imread(filename)
img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
w = img.shape[1]
h = img.shape[0]
white = 255 - np.zeros((h,w,4), dtype='uint8')

a = 0                       # 開始時 a 等於 0
while True:
    k = cv2.waitKey(1) # 等待按鍵輸入
    if k == ESC:     #ESC
        break
    elif k == 32:
        a = 1               # 如果按下空白鍵，讓 a 等於 1

    if a == 0:
        output = img.copy() # 如果 a 等於 0，複製來源圖片為 output
    else:
        #111
        output = cv2.addWeighted(white, a, img, 1-a, 0)  # 如果 a 等於 1，根據 a 套用權重
        a = a - 0.01        # a 不斷減少 0.01
        if a<0: a = 0       # 如果 a 小於 0 就讓 a 等於 0

    cv2.imshow("OpenCV 11", output)               # 顯示圖片

cv2.destroyAllWindows()                 # 結束所有視窗

print("------------------------------------------------------------")  # 60個

print("OpenCV VideoCapture 12 存圖 製作一個閃光燈拍照的效果")
print('按 ESC 離開')

cap = cv2.VideoCapture(0)

a = 0    # 白色圖片透明度

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, img = cap.read()               # 讀取影片的每一幀
    if not ret:
        print("Cannot receive frame")   # 如果讀取錯誤，印出訊息
        break
    img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)  # 轉換顏色為 BGRA
    w = img.shape[1]
    h = img.shape[0]
    img = cv2.resize(img,(w,h))         # 縮放尺寸
    white = 255 - np.zeros((h,w,4), dtype='uint8')   # 產生全白圖片

    k = cv2.waitKey(1) # 等待按鍵輸入
    if k == ESC:     #ESC
        break
    elif k == 32:            # 按下空白將 a 等於 1
        a = 1

    if a == 0:
        output = img.copy()  # 如果 a 為 0，設定 output 變數為來源圖片的拷貝
    else:
        photo = img.copy()   # 如果 a 不為 0，設定 photo 變數為來源圖片的拷貝
        #222
        output = cv2.addWeighted(white, a, photo, 1-a, 0)  # 計算權重，產生白色慢慢消失效果
        a = a - 0.1
        if a<0:
            a = 0
            image_filename = 'tmp3_Image_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.jpg';
            cv2.imwrite(image_filename, photo)
            print('已存圖, 檔案 :', image_filename)

    cv2.imshow("OpenCV 12", output)               # 顯示圖片

cap.release()                           # 所有作業都完成後，釋放資源
cv2.destroyAllWindows()                 # 結束所有視窗

print("------------------------------------------------------------")  # 60個

print("OpenCV VideoCapture 13 存圖 製作一個閃光燈拍照的效果 + 倒數三秒")
print('按 ESC 離開')

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

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, img = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
    w = img.shape[1]
    h = img.shape[0]
    img = cv2.resize(img,(w,h))
    white = 255 - np.zeros((h,w,4), dtype='uint8')

    k = cv2.waitKey(1) # 等待按鍵輸入
    if k == ESC:     #ESC
        break
    elif k == 32:
        a = 1
        sec = 4  # 加入倒數秒數

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
                image_filename = 'tmp4_Image_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.jpg';
                cv2.imwrite(image_filename, photo)
                print('已存圖, 檔案 :', image_filename)

    cv2.imshow("OpenCV 13", output)

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("OpenCV VideoCapture 14 加 logo")
print('按 ESC 離開')

logo_filename = 'C:/_git/vcs/_4.python/_data/logo1.png'

logo = cv2.imread(logo_filename)
logo = cv2.resize(logo, (128,128))

size = logo.shape
img = np.zeros((480,640,3), dtype='uint8')
img[0:480, 0:640] = '255'
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
    frame = cv2.resize(frame,(640, 480))   # 調整圖片尺寸
    bg = cv2.bitwise_and(frame, frame, mask = mask2 )
    output = cv2.add(bg, logo)
    
    cv2.imshow("OpenCV 14", output)

    k = cv2.waitKey(1) # 等待按鍵輸入
    if k == ESC:     #ESC
        break
    
cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("OpenCV VideoCapture 15")
print('按 ESC 離開')

logo_filename = 'C:/_git/vcs/_4.python/opencv/data/opencv_logo.png'
logo = cv2.imread(logo_filename)
size = logo.shape
img = np.zeros((480,640,3), dtype='uint8')
img[0:480, 0:640] = '255'
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
    frame = cv2.resize(frame,(640, 480))
    output = cv2.bitwise_not(frame, mask = mask1 )      # 套用 not 和遮罩
    output = cv2.bitwise_not(output, mask = mask1 )     # 再次套用 not 和遮罩，將色彩轉成原來的顏色
    
    cv2.imshow("OpenCV 15", output)

    k = cv2.waitKey(1) # 等待按鍵輸入
    if k == ESC:     #ESC
        break
    
cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("OpenCV VideoCapture 16 Webcam影像轉成gif")
print('按 ESC 離開')

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
    img = cv2.resize(img, (640,480))    # 調整影片大小

    # 加上黑色區塊
    cv2.rectangle(img,(10,10),(200,42),(0,0,0),-1)

    # 加上文字
    text = 'English Only'
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

    cv2.imshow("OpenCV 16", img)

    k = cv2.waitKey(1) # 等待按鍵輸入
    if k == ESC:     #ESC
        break

cap.release()
# 儲存為 gif 動畫
output[0].save("tmp_webcam_image.gif", save_all=True, append_images=output[1:], duration=250, loop=0, disposal=2)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("OpenCV VideoCapture 17 處理影片")
print('按 ESC 離開')

video_filename = 'C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4'

from PIL import Image,ImageSequence

cap = cv2.VideoCapture(video_filename)   # 開啟影片
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

    k = cv2.waitKey(1) # 等待按鍵輸入
    if k == ESC:     #ESC
        break

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
    img.save(f'tmp_gif{n}.gif')
    n = n + 1

print('loading gifs...')
output = []
for i in range(n):
    img = Image.open(f'tmp_gif{i}.gif')
    img = img.convert("RGBA")
    output.append(img)

output[0].save("tmp_test2.gif", save_all=True, append_images=output[1:], duration=100, loop=0, disposal=2)
print('ok...')

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("OpenCV VideoCapture 18 QRCode 偵測器")
print('按 ESC 離開')

from PIL import ImageFont, ImageDraw, Image

cap = cv2.VideoCapture(0)

def putText(x,y,text,color=(0,0,0)):
    global img
    font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'      #有中文
    font_size = 20
    font = ImageFont.truetype(font_filename, font_size)
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
    img = cv2.resize(frame,(640,480))
    ok, data, bbox, rectified = qrcode.detectAndDecodeMulti(img)  # 辨識 QRCode
    if ok:
        for i in range(len(data)):
            text = data[i]            # QRCode 內容
            box = boxSize(bbox[i])    # QRCode 座標
            cv2.rectangle(img,(box[0],box[1]),(box[2],box[3]),(0,0,255),5)  # 繪製外框
            putText(box[0],box[3],text,color=(0,0,255))                     # 顯示文字

    cv2.imshow("OpenCV 18", img)

    k = cv2.waitKey(1) # 等待按鍵輸入
    if k == ESC:     #ESC
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("OpenCV VideoCapture 19 QRCode 偵測器")
print('按 ESC 離開')

from PIL import ImageFont, ImageDraw, Image

cap = cv2.VideoCapture(0)     # 讀取攝影鏡頭

# 定義加入文字函式
def putText(x,y,text,size=20,color=(0,0,0)):
    global img
    font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'      #有中文
    font_size = 20
    font = ImageFont.truetype(font_filename, font_size)
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
    img = cv2.resize(frame,(640,480))
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

    cv2.imshow("OpenCV 19", img)     # 預覽影像

    k = cv2.waitKey(1) # 等待按鍵輸入
    if k == ESC:     #ESC
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("OpenCV VideoCapture 20 讀取 QR code 圖檔")
print('按 ESC 離開')

from PIL import ImageFont, ImageDraw, Image

filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_qrcode/QR1.png'

image = cv2.imread(filename)

# 定義加入文字函式
def putText(x,y,text,color=(0,0,0)):
    global image
    font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'      #有中文
    font_size = 20
    font = ImageFont.truetype(font_filename, font_size)
    imagePil = Image.fromarray(image)
    draw = ImageDraw.Draw(imagePil)
    draw.text((x, y), text, fill=color, font=font)
    image = np.array(imagePil)

def boxSize(arr):
    global data
    box_roll = np.rollaxis(arr,1,0)
    xmax = int(np.amax(box_roll[0]))
    xmin = int(np.amin(box_roll[0]))
    ymax = int(np.amax(box_roll[1]))
    ymin = int(np.amin(box_roll[1]))
    return (xmin,ymin,xmax,ymax)

qrcode = cv2.QRCodeDetector()             # QRCode 偵測器

status, data, bbox, rectified = qrcode.detectAndDecodeMulti(image)  # 辨識 QRCode
print('OK', status)
print('len', len(data))
print('data', data)
print('bbox', bbox)
print('rectified', rectified)

if status == True:
    for i in range(len(data)):
        text = data[i]            # QRCode 內容
        
        box = boxSize(bbox[i])    # QRCode 座標
        cv2.rectangle(image,(box[0],box[1]),(box[2],box[3]),(0,0,255),2)  # 繪製外框
        print(box)
        print(text)
        #putText(10,10,"aaa",color=(0,0,255))                     # 顯示文字
        putText(box[0],box[3],text,color=(0,0,255))                     # 顯示文字

cv2.imshow("OpenCV 20", image)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[height//2:, :width//2] = smaller_frame
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[height//2:, width//2:] = smaller_frame

    cv2.imshow('frame', image)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', result)
    cv2.imshow('mask', mask)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
        roi_gray = gray[y:y+w, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

