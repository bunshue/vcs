"""

新進  未歸類


"""

import cv2
import os
import sys
import time
import math
import random
import numpy as np
import pandas as pd

print("------------------------------------------------------------")  # 60個

ESC = 27
SPACE = 32

print("------------------------------------------------------------")  # 60個
"""
print("OpenCV VideoCapture 04 兩個camera")
print("按 ESC 離開")

ratio = 3
border = 30
W = 640
H = 480

w = W // ratio
h = H // ratio
x_st = W - w - border
y_st = H - h - border

cap1 = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)

if not cap1.isOpened():
    print("開啟攝影機1失敗")
    exit()
if not cap2.isOpened():
    print("開啟攝影機2失敗")
    exit()

while True:
    ret1, img1 = cap1.read()  # 從攝影機擷取一張影像
    ret2, img2 = cap2.read()  # 從攝影機擷取一張影像
    img1 = cv2.resize(img1, (w, h))  # 縮小尺寸 小圖
    # img2 = cv2.resize(img2,(W, H))  # 縮小尺寸 大圖

    img2[y_st : y_st + h, x_st : x_st + w] = img1  # 將 img2 的特定區域換成 img1

    cv2.rectangle(
        img2, (x_st, y_st), (x_st + w, y_st + h), (255, 255, 255), 5
    )  # 繪製子影片的外框

    cv2.imshow("OpenCV 01", img2)

    k = cv2.waitKey(1)
    if k == ESC:  # ESC
        break

cap1.release()
cap2.release()
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個

print("OpenCV VideoCapture 05 N X N")
print("按 ESC 離開")

N = 2  # 設定要分成幾格, N X N
W = 640 * 2
H = 480 * 2
cap = cv2.VideoCapture(0)
output = np.zeros((H, W, 3), dtype="uint8")  # 產生 WxH 的黑色背景

if not cap.isOpened():
    print("開啟攝影機失敗")
    exit()

w = W // N  # 計算分格之後的影像寬度
h = H // N  # 計算分格之後的影像高度
img_list = []  # 設定空串列，記錄每一格的影像
while True:
    ret, frame = cap.read()  # 從攝影機擷取一張影像
    frame = cv2.resize(frame, (w, h))  # 縮小尺寸
    """ 2X2的寫法
    output[0:h, 0:w] = frame             # 將 output 的特定區域置換為 frame, 左上
    output[0:h, w:w*2] = frame             # 將 output 的特定區域置換為 frame, 右上
    output[h:h*2, 0:w] = frame             # 將 output 的特定區域置換為 frame, 左下
    output[h:h*2, w:w*2] = frame             # 將 output 的特定區域置換為 frame, 右下

    #左右相反
    frame = cv2.flip(frame, 1)
    """
    img_list.append(frame)  # 每次擷取影像時，將影像存入串列
    if len(img_list) > N * N:
        del img_list[0]  # 如果串列長度超過可容納的影像數量，移除第一個項目
    for i in range(len(img_list)):
        x = i % N  # 根據串列計算影像的 x 座標
        y = i // N  # 根據串列計算影像的 y 座標
        output[h * y : h * y + h, w * x : w * x + w] = img_list[i]  # 更新畫面

    cv2.imshow("OpenCV 02", output)

    k = cv2.waitKey(1)
    if k == ESC:  # ESC
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("OpenCV VideoCapture 10 Covex效果")
print("按 ESC 離開")


def convex(src_img, raw, effect):
    col, row, channel = raw[:]
    cx, cy, r = effect[:]
    output = np.zeros([row, col, channel], dtype=np.uint8)
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
    print("開啟攝影機失敗")
    exit()

while True:
    ret, frame = cap.read()  # 從攝影機擷取一張影像
    if not ret:
        print("Cannot receive frame")  # 如果讀取錯誤，印出訊息
        break
    w, h = 640, 480
    cw, ch = int(w / 2), int(h / 2)  # 取得中心點
    frame = convex(frame, (w, h, 3), (cw, ch, 100))

    cv2.imshow("OpenCV 03", frame)

    k = cv2.waitKey(1)
    if k == ESC:  # ESC
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("OpenCV VideoCapture 11 按鍵 慢慢顯示出一圖的效果")
print("按 ESC 離開")

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

img = cv2.imread(filename)
img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
w = img.shape[1]
h = img.shape[0]
white = 255 - np.zeros((h, w, 4), dtype="uint8")

a = 0  # 開始時 a 等於 0
while True:
    k = cv2.waitKey(1)
    if k == ESC:  # ESC
        break
    elif k == SPACE:
        a = 1  # 如果按下空白鍵，讓 a 等於 1

    if a == 0:
        output = img.copy()  # 如果 a 等於 0，複製來源圖片為 output
    else:
        # 111
        output = cv2.addWeighted(white, a, img, 1 - a, 0)  # 如果 a 等於 1，根據 a 套用權重
        a = a - 0.01  # a 不斷減少 0.01
        if a < 0:
            a = 0  # 如果 a 小於 0 就讓 a 等於 0

    cv2.imshow("OpenCV 04", output)  # 顯示圖片

cv2.destroyAllWindows()  # 結束所有視窗

print("------------------------------------------------------------")  # 60個

print("OpenCV VideoCapture 12 存圖 按 SPACE 製作一個閃光燈拍照的效果")
print("按 ESC 離開")

cap = cv2.VideoCapture(0)

a = 0  # 白色圖片透明度

if not cap.isOpened():
    print("開啟攝影機失敗")
    exit()

while True:
    ret, frame = cap.read()  # 從攝影機擷取一張影像
    if not ret:
        print("Cannot receive frame")  # 如果讀取錯誤，印出訊息
        break
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)  # 轉換顏色為 BGRA
    w = frame.shape[1]
    h = frame.shape[0]
    frame = cv2.resize(frame, (w, h))  # 縮放尺寸
    white = 255 - np.zeros((h, w, 4), dtype="uint8")  # 產生全白圖片

    k = cv2.waitKey(1)
    if k == ESC:  # ESC
        break
    elif k == SPACE:  # 按下空白將 a 等於 1
        a = 1

    if a == 0:
        output = frame.copy()  # 如果 a 為 0，設定 output 變數為來源圖片的拷貝
    else:
        photo = frame.copy()  # 如果 a 不為 0，設定 photo 變數為來源圖片的拷貝
        # 222
        output = cv2.addWeighted(white, a, photo, 1 - a, 0)  # 計算權重，產生白色慢慢消失效果
        a = a - 0.1
        if a < 0:
            a = 0
            image_filename = (
                "tmp3_Image_"
                + time.strftime("%Y%m%d_%H%M%S", time.localtime())
                + ".jpg"
            )
            cv2.imwrite(image_filename, photo)
            print("已存圖, 檔案 :", image_filename)

    cv2.imshow("OpenCV 05", output)  # 顯示圖片

cap.release()  # 所有作業都完成後，釋放資源
cv2.destroyAllWindows()  # 結束所有視窗

print("------------------------------------------------------------")  # 60個

print("OpenCV VideoCapture 13 存圖 按 SPACE 製作一個閃光燈拍照的效果 + 倒數三秒")
print("按 ESC 離開")

cap = cv2.VideoCapture(0)


# 定義加入文字的函式
def putText(source, x, y, text, scale=2.5, color=(255, 255, 255)):
    org = (x, y)
    fontFace = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = scale
    thickness = 5
    lineType = cv2.LINE_AA
    cv2.putText(source, text, org, fontFace, fontScale, color, thickness, lineType)


a = 0

if not cap.isOpened():
    print("開啟攝影機失敗")
    exit()

while True:
    ret, frame = cap.read()  # 從攝影機擷取一張影像
    if not ret:
        print("Cannot receive frame")
        break
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    w = frame.shape[1]
    h = frame.shape[0]
    frame = cv2.resize(frame, (w, h))
    white = 255 - np.zeros((h, w, 4), dtype="uint8")

    k = cv2.waitKey(1)
    if k == ESC:  # ESC
        break
    elif k == SPACE:
        a = 1
        sec = 4  # 加入倒數秒數

    if a == 0:
        output = frame.copy()
    else:
        output = frame.copy()  # 設定 output 和 photo 變數
        photo = frame.copy()
        sec = sec - 0.05  # sec 不斷減少 0.05 ( 根據個人電腦效能設定，使其搭配 while 迴圈看起來像倒數一秒 )
        putText(output, 10, 70, str(int(sec)))  # 加入文字
        # 如果秒數小於 1
        if sec < 1:
            output = cv2.addWeighted(white, a, photo, 1 - a, 0)
            a = a - 0.1
            if a < 0:
                a = 0
                image_filename = (
                    "tmp4_Image_"
                    + time.strftime("%Y%m%d_%H%M%S", time.localtime())
                    + ".jpg"
                )
                cv2.imwrite(image_filename, photo)
                print("已存圖, 檔案 :", image_filename)

    cv2.imshow("OpenCV 06", output)

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("OpenCV VideoCapture 14 加 logo")
print("按 ESC 離開")

logo_filename = "C:/_git/vcs/_4.python/opencv/data/opencv_logo.png"

logo_filename = "C:/_git/vcs/_4.python/_data/logo1.png"

logo = cv2.imread(logo_filename)
logo = cv2.resize(logo, (100, 100))

size = logo.shape
img = np.zeros((480, 640, 3), dtype="uint8")
img[0:480, 0:640] = "255"

x_st, y_st = 10, 50  # logo貼上位置
img[y_st : y_st + size[0], x_st : x_st + size[1]] = logo

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, mask1 = cv2.threshold(img_gray, 200, 255, cv2.THRESH_BINARY_INV)
logo = cv2.bitwise_and(img, img, mask=mask1)
ret, mask2 = cv2.threshold(img_gray, 200, 255, cv2.THRESH_BINARY)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("開啟攝影機失敗")
    exit()

while True:
    ret, frame = cap.read()  # 從攝影機擷取一張影像
    if not ret:
        print("Cannot receive frame")
        break
    frame = cv2.resize(frame, (640, 480))  # 調整圖片尺寸
    bg = cv2.bitwise_and(frame, frame, mask=mask2)
    output = cv2.add(bg, logo)

    # output = cv2.bitwise_not(frame, mask=mask1)  # 套用 not 和遮罩
    # output = cv2.bitwise_not(output, mask=mask1)  # 再次套用 not 和遮罩，將色彩轉成原來的顏色

    cv2.imshow("OpenCV 07", output)

    k = cv2.waitKey(1)
    if k == ESC:  # ESC
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

""" many
print("OpenCV VideoCapture 16 Webcam影像轉成gif")
print("按 ESC 離開")

from PIL import Image, ImageSequence

output = []  # 建立輸出的空串列

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("開啟攝影機失敗")
    exit()

while True:
    ret, frame = cap.read()  # 從攝影機擷取一張影像
    if not ret:
        print("Cannot receive frame")
        break
    frame = cv2.resize(frame, (640, 480))  # 調整影片大小

    gif = cv2.cvtColor(frame, cv2.COLOR_BGRA2RGBA)  # 轉換顏色
    gif = Image.fromarray(gif)  # 轉換成 PIL 格式
    gif = gif.convert("RGB")  # 轉換顏色
    output.append(gif)  # 添加到 output

    cv2.imshow("OpenCV 08", frame)

    k = cv2.waitKey(1)
    if k == ESC:  # ESC
        break

cap.release()

# 儲存為 gif 動畫
output[0].save(
    "tmp_webcam_image.gif",
    save_all=True,
    append_images=output[1:],
    duration=250,
    loop=0,
    disposal=2,
)
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個

print("OpenCV VideoCapture 17 處理影片")
print("按 ESC 離開")

video_filename = "C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4"

from PIL import Image, ImageSequence

cap = cv2.VideoCapture(video_filename)  # 開啟影片

source = []  # 建立 source 空串列，記錄影格內容
cnt = 0

# 以迴圈從影片檔案讀取影格，並顯示出來
while cap.isOpened():
    ret, frame = cap.read()  # 從影片擷取一張影像
    if ret == True:
        cv2.imshow("Video Player", frame)
        if cnt % 30 == 0:  # 每 30 格取一格
            frame = cv2.resize(frame, (400, 300))  # 改變尺寸，加快處理效率
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)  # 修改顏色為 RGBA
            source.append(frame)  # 記錄該圖片
        cnt = cnt + 1
    else:
        break

    k = cv2.waitKey(1)
    if k == ESC:  # ESC
        break

cap.release()
cv2.destroyAllWindows()

print("轉換成 gif")

for i in range(len(source)):
    for x in range(400):
        for y in range(300):
            r = source[i][y, x, 0]  # 該像素的紅色數值
            g = source[i][y, x, 1]  # 該像素的綠色數值
            b = source[i][y, x, 2]  # 該像素的藍色數值
            if r > 35 and r < 100 and g > 110 and g < 200 and b > 60 and b < 130:
                source[i][y, x, 3] = 0  # 如果在顏色範圍內，將透明度設為 0

print("frame 轉 gif")

n = 0
for i in source:
    frame = Image.fromarray(i)
    frame.save(f"tmp_gif{n}.gif")
    n = n + 1

print("讀取 gif")

output = []
for i in range(n):
    frame = Image.open(f"tmp_gif{i}.gif")
    frame = frame.convert("RGBA")
    output.append(frame)

print("儲存 gif")

output[0].save(
    "tmp_test2.gif",
    save_all=True,
    append_images=output[1:],
    duration=100,
    loop=0,
    disposal=2,
)
print("OK")

print("------------------------------------------------------------")  # 60個

print("OpenCV VideoCapture 18 QRCode 偵測器")
print("按 ESC 離開")

from PIL import ImageFont, ImageDraw, Image

cap = cv2.VideoCapture(0)


def putText(x, y, text, color=(0, 0, 0)):
    global img
    font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"  # 有中文
    font_size = 20
    font = ImageFont.truetype(font_filename, font_size)
    imgPil = Image.fromarray(img)
    draw = ImageDraw.Draw(imgPil)
    draw.text((x, y), text, fill=color, font=font)
    img = np.array(imgPil)


def boxSize(arr):
    global data
    box_roll = np.rollaxis(arr, 1, 0)
    xmax = int(np.amax(box_roll[0]))
    xmin = int(np.amin(box_roll[0]))
    ymax = int(np.amax(box_roll[1]))
    ymin = int(np.amin(box_roll[1]))
    return (xmin, ymin, xmax, ymax)


qrcode = cv2.QRCodeDetector()  # QRCode 偵測器

while True:
    ret, frame = cap.read()  # 從攝影機擷取一張影像
    if not ret:
        print("Cannot receive frame")
        break
    img = cv2.resize(frame, (640, 480))
    ok, data, bbox, rectified = qrcode.detectAndDecodeMulti(img)  # 辨識 QRCode
    if ok:
        for i in range(len(data)):
            text = data[i]  # QRCode 內容
            box = boxSize(bbox[i])  # QRCode 座標
            cv2.rectangle(
                img, (box[0], box[1]), (box[2], box[3]), (0, 0, 255), 5
            )  # 繪製外框
            putText(box[0], box[3], text, color=(0, 0, 255))  # 顯示文字

    cv2.imshow("OpenCV 09", img)

    k = cv2.waitKey(1)
    if k == ESC:  # ESC
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("OpenCV VideoCapture 19 QRCode 偵測器")
print("按 ESC 離開")

from PIL import ImageFont, ImageDraw, Image

cap = cv2.VideoCapture(0)


# 定義加入文字函式
def putText(x, y, text, size=20, color=(0, 0, 0)):
    global img
    font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"  # 有中文
    font_size = 20
    font = ImageFont.truetype(font_filename, font_size)
    imgPil = Image.fromarray(img)  # 轉換成 PIL 影像物件
    draw = ImageDraw.Draw(imgPil)  # 定義繪圖物件
    draw.text((x, y), text, fill=color, font=font)  # 加入文字
    img = np.array(imgPil)  # 轉換成 np.array


# 定義馬賽克函式
def mosaic(image, level):
    size = image.shape  # 取得原始圖片的資訊
    h = int(size[0] / level)  # 按照比例縮小後的高度 ( 使用 int 去除小數點 )
    w = int(size[1] / level)  # 按照比例縮小後的寬度 ( 使用 int 去除小數點 )
    output = cv2.resize(image, (w, h), interpolation=cv2.INTER_LINEAR)  # 根據縮小尺寸縮小
    output = cv2.resize(
        output, (size[1], size[0]), interpolation=cv2.INTER_NEAREST
    )  # 放大到原本的大小
    return output


qrcode = cv2.QRCodeDetector()  # QRCode 偵測器

while True:
    ret, frame = cap.read()  # 從攝影機擷取一張影像
    if not ret:
        print("Cannot receive frame")
        break
    img = cv2.resize(frame, (640, 480))
    ok, data, bbox, rectified = qrcode.detectAndDecodeMulti(img)  # 偵測並辨識 QRCode
    # 如果偵測到 QRCode
    if ok:
        for i in range(len(data)):
            text = data[i]  # 取出內容
            # 如果內容是 a1，套用模糊效果
            if text == "a1":
                img = cv2.blur(img, (20, 20))
                putText(0, 0, "模糊效果", 100, (255, 255, 255))
            # 如果內容是 a2，套用馬賽克效果
            elif text == "a2":
                img = mosaic(img, 15)
                putText(0, 0, "馬賽克效果", 100, (255, 255, 255))
            # 如果內容是 a2，套用片效果
            elif text == "a3":
                img = 255 - img
                putText(0, 0, "負片效果", 100, (0, 0, 0))

    cv2.imshow("OpenCV 10", img)  # 預覽影像

    k = cv2.waitKey(1)
    if k == ESC:  # ESC
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("OpenCV VideoCapture 20 讀取 QR code 圖檔")
print("按 ESC 離開")

from PIL import ImageFont, ImageDraw, Image

filename = "C:/_git/vcs/_1.data/______test_files1/__pic/_qrcode/QR1.png"

image = cv2.imread(filename)


# 定義加入文字函式
def putText(x, y, text, color=(0, 0, 0)):
    global image
    font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"  # 有中文
    font_size = 20
    font = ImageFont.truetype(font_filename, font_size)
    imagePil = Image.fromarray(image)
    draw = ImageDraw.Draw(imagePil)
    draw.text((x, y), text, fill=color, font=font)
    image = np.array(imagePil)


def boxSize(arr):
    global data
    box_roll = np.rollaxis(arr, 1, 0)
    xmax = int(np.amax(box_roll[0]))
    xmin = int(np.amin(box_roll[0]))
    ymax = int(np.amax(box_roll[1]))
    ymin = int(np.amin(box_roll[1]))
    return (xmin, ymin, xmax, ymax)


qrcode = cv2.QRCodeDetector()  # QRCode 偵測器

status, data, bbox, rectified = qrcode.detectAndDecodeMulti(image)  # 辨識 QRCode
print("OK", status)
print("len", len(data))
print("data", data)
print("bbox", bbox)
print("rectified", rectified)

if status == True:
    for i in range(len(data)):
        text = data[i]  # QRCode 內容

        box = boxSize(bbox[i])  # QRCode 座標
        cv2.rectangle(image, (box[0], box[1]), (box[2], box[3]), (0, 0, 255), 2)  # 繪製外框
        print(box)
        print(text)
        # putText(10,10,"aaa",color=(0,0,255))                     # 顯示文字
        putText(box[0], box[3], text, color=(0, 0, 255))  # 顯示文字

cv2.imshow("OpenCV 11", image)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  # 從攝影機擷取一張影像
    width = int(cap.get(3))
    height = int(cap.get(4))

    image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    image[: height // 2, : width // 2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[height // 2 :, : width // 2] = smaller_frame
    image[: height // 2, width // 2 :] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[height // 2 :, width // 2 :] = smaller_frame

    cv2.imshow("OpenCV 12", image)

    k = cv2.waitKey(1)
    if k == ESC:  # ESC
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  # 從攝影機擷取一張影像
    width = int(cap.get(3))
    height = int(cap.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("OpenCV 13a", result)
    cv2.imshow("OpenCV 13b_mask", mask)

    k = cv2.waitKey(1)
    if k == ESC:  # ESC
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("OpenCV_ai_72 追蹤功能 按a開始 選取ROI, 按Enter確定")

tracker = cv2.TrackerCSRT_create()  # 創建追蹤器
tracking = False  # 設定 False 表示尚未開始追蹤

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("開啟攝影機失敗")
    sys.exit()

while True:
    ret, frame = cap.read()  # 從攝影機擷取一張影像
    # frame = cv2.resize(frame, (640//2, 480//2))  # 縮小尺寸，加快速度

    k = cv2.waitKey(1)
    if k == ESC:
        break

    # 按下 a 開始選取
    if k == ord("a"):
        # 選取區域
        area = cv2.selectROI("ImageShow", frame, showCrosshair=False, fromCenter=False)
        print("選取區域 :", area)
        tracker.init(frame, area)  # 初始化追蹤器
        tracking = True  # 設定可以開始追蹤
    if tracking:
        success, point = tracker.update(frame)  # 追蹤成功後，不斷回傳左上和右下的座標
        if success:
            p1 = [int(point[0]), int(point[1])]
            p2 = [int(point[0] + point[2]), int(point[1] + point[3])]
            cv2.rectangle(frame, p1, p2, (0, 0, 255), 3)  # 根據座標，繪製四邊形，框住要追蹤的物件

    cv2.imshow("OpenCV 14", frame)

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
"""
print("OpenCV_ai_74 影片")

video_filename = "C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4"

tracker_list = []
for i in range(3):
    tracker = cv2.TrackerCSRT_create()  # 創建三組追蹤器
    tracker_list.append(tracker)
colors = [(0, 0, 255), (0, 255, 255), (255, 255, 0)]  # 設定三個外框顏色
tracking = False  # 設定 False 表示尚未開始追蹤

cap = cv2.VideoCapture(video_filename)  # 開啟影片

if not cap.isOpened():
    print("開啟影片失敗")
    sys.exit()

a = 0  # 刪減影片影格使用

while True:
    ret, frame = cap.read()  # 從攝影機擷取一張影像
    #frame = cv2.resize(frame, (640//2, 480//2))  # 縮小尺寸，加快速度

    k = cv2.waitKey(1)
    if k == ESC:
        break

    # 為了避免影片影格太多，所以採用 10 格取一格，加快處理速度
    if a % 10 == 0:
        if tracking == False:
            # 如果尚未開始追蹤，就開始標記追蹤物件的外框
            for i in tracker_list:
                area = cv2.selectROI(
                    "ImageShow", frame, showCrosshair=False, fromCenter=False
                )
                i.init(frame, area)  # 初始化追蹤器
            tracking = True  # 設定可以開始追蹤
        if tracking:
            for i in range(len(tracker_list)):
                success, point = tracker_list[i].update(frame)  # 追蹤成功後，不斷回傳左上和右下的座標
                if success:
                    p1 = [int(point[0]), int(point[1])]
                    p2 = [int(point[0] + point[2]), int(point[1] + point[3])]
                    cv2.rectangle(frame, p1, p2, colors[i], 3)  # 根據座標，繪製四邊形，框住要追蹤的物件

        cv2.imshow("OpenCV 15", frame)
    a = a + 1

cap.release()
cv2.destroyAllWindows()

"""

print("------------------------------------------------------------")  # 60個

print("OpenCV_ai_75")

multiTracker = cv2.legacy.MultiTracker_create()  # 建立多物件追蹤器
tracking = False  # 設定追蹤尚未開始
colors = [(0, 0, 255), (0, 255, 255)]  # 建立外框色彩清單

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("開啟攝影機失敗")
    sys.exit()

while True:
    ret, frame = cap.read()  # 從攝影機擷取一張影像
    # frame = cv2.resize(frame, (640//2, 480//2))  # 縮小尺寸加快速度

    k = cv2.waitKey(1)
    if k == ESC:
        break

    # 按下 a 的時候開始標記物件外框
    if k == ord("a"):
        for i in range(2):
            area = cv2.selectROI(
                "ImageShow", frame, showCrosshair=False, fromCenter=False
            )
            # 標記外框後設定該物件的追蹤演算法
            tracker = cv2.legacy.TrackerCSRT_create()
            # 將該物件加入 multiTracker
            multiTracker.add(tracker, frame, area)
        # 設定 True 開始追蹤
        tracking = True
    if tracking:
        # 更新 multiTracker
        success, points = multiTracker.update(frame)
        a = 0
        if success:
            for i in points:
                p1 = (int(i[0]), int(i[1]))
                p2 = (int(i[0] + i[2]), int(i[1] + i[3]))
                # 標記物件外框
                cv2.rectangle(frame, p1, p2, colors[a], 3)
                a = a + 1
    cv2.imshow("OpenCV 16", frame)

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

# simple color
"""
色彩辨識與追蹤
"""
color = ((16, 59, 0), (47, 255, 255))
lower = np.array(color[0], dtype="uint8")
upper = np.array(color[1], dtype="uint8")

cap = cv2.VideoCapture(0)

# 取得影像的尺寸大小
w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("Image Size: %d x %d" % (w, h))

if not cap.isOpened():
    print("開啟攝影機失敗")
    sys.exit()

ratio = w / h
WIDTH = 320
HEIGHT = int(WIDTH / ratio)

while True:
    ret, frame = cap.read()  # 從攝影機擷取一張影像
    frame = cv2.resize(frame, (WIDTH, HEIGHT))
    frame = cv2.flip(frame, 1)

    #### 在while中
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv = cv2.GaussianBlur(hsv, (11, 11), 0)  # 執行高斯模糊化

    #### 在while中
    mask = cv2.inRange(hsv, lower, upper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    #### 在while中
    contours, hierarchy = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    if len(contours) > 0:
        cnt = max(contours, key=cv2.contourArea)
        if cv2.contourArea(cnt) < 100:
            continue
        x, y, w, h = cv2.boundingRect(cnt)
        p1 = (x - 2, y - 2)
        p2 = (x + w + 4, y + h + 4)

        out = cv2.bitwise_and(hsv, hsv, mask=mask)

        cv2.rectangle(frame, p1, p2, (0, 0, 255), 2)  # B G R
        cv2.rectangle(hsv, p1, p2, (0, 255, 0), 2)
        cv2.rectangle(out, p1, p2, (255, 0, 0), 2)

        frame = cv2.hconcat([frame, hsv, out])

    #### 在while中
    cv2.imshow("OpenCV 17", frame)

    k = cv2.waitKey(1)
    if k == ESC:  # ESC
        break

# 釋放所有資源
cap.release()  # 釋放攝影機
cv2.destroyAllWindows()  # 關閉所有 OpenCV 視窗

print("------------------------------------------------------------")  # 60個

print("按 ESC 離開")

cap = cv2.VideoCapture(0)

logo_filename = "C:/_git/vcs/_4.python/_data/panda.jpg"
logo = cv2.imread(logo_filename)
logo = cv2.resize(logo, (640, 480))  # 改變影像尺寸，符合疊加的圖片

if not cap.isOpened():
    print("開啟攝影機失敗")
    exit()

while True:
    ret, img = cap.read()  # 從攝影機擷取一張影像
    if not ret:
        print("Cannot receive frame")  # 如果讀取錯誤，印出訊息
        break
    # cv2.imshow("OpenCV 18", img) 原圖顯示

    # addWeighted
    output = cv2.addWeighted(img, 0.6, logo, 0.4, 50)  # 疊加圖片
    cv2.imshow("OpenCV 19", output)

    k = cv2.waitKey(1)
    if k == ESC:  # ESC
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

video = cv2.VideoCapture("data/iceocean.mov")  # 開啟影片檔案

while video.isOpened():
    ret, frame = video.read()  # 讀取影片檔案
    if ret:
        cv2.namedWindow("myVideo", 0)
        cv2.resizeWindow("myVideo", 300, 200)
        cv2.imshow("myVideo", frame)  # 顯示影片
    else:
        break
    c = cv2.waitKey(50)  # 可以控制撥放速度
    if c == 27:  # 按 Esc 键, 結束
        break

video.release()  # 關閉輸出物件
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

capture = cv2.VideoCapture(0)  # 初始化攝影功能
while capture.isOpened():
    ret, frame = capture.read()  # 讀取設請鏡頭的影像
    cv2.imshow("Frame", frame)  # 顯示攝影鏡頭的影像
    width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)  # 寬度
    height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)  # 高度
    c = cv2.waitKey(1)  # 等待時間 1 毫秒 ms
    if c == 27:  # 按 Esc 键
        break
print(f"Frame 的寬度 = {width}")  # 輸出Frame 的寬度
print(f"Frame 的高度 = {height}")  # 輸出Frame 的高度
capture.release()  # 關閉攝影功能
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

video = cv2.VideoCapture("data/iceocean.mov")  # 開啟影片檔案

while video.isOpened():
    ret, frame = video.read()  # 讀取影片檔案
    cv2.imshow("Frame", frame)  # 顯示影像
    width = video.get(cv2.CAP_PROP_FRAME_WIDTH)  # 寬度
    height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)  # 高度
    video_fps = video.get(cv2.CAP_PROP_FPS)  # 速度
    video_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)  # 幀數
    c = cv2.waitKey(50)  # 等待時間
    if c == 27:  # 按 Esc 键
        break
print(f"Video 的寬度    = {width}")  # 輸出 Video 的寬度
print(f"Video 的高度    = {height}")  # 輸出 Video 的高度
print(f"Video 的速度    = {video_fps}")  # 輸出 Video 的速度
print(f"Video 的幀數    = {video_frames}")  # 輸出 Video 的幀數
video.release()  # 關閉攝影功能
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

capture = cv2.VideoCapture(0)  # 初始化攝影功能
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # 設定寬度
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 960)  # 設定高度
while capture.isOpened():
    ret, frame = capture.read()  # 讀取設請鏡頭的影像
    cv2.imshow("Frame", frame)  # 顯示攝影鏡頭的影像
    c = cv2.waitKey(1)  # 等待時間 1 毫秒 ms
    if c == 27:  # 按 Esc 键
        break
capture.release()  # 關閉攝影功能
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

video = cv2.VideoCapture("data/iceocean.mov")  # 開啟影片檔案

video_fps = video.get(cv2.CAP_PROP_FPS)  # 計算速度
height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)  # 影片高度
counter = 1  # 幀數計數器
font = cv2.FONT_HERSHEY_SIMPLEX  # 字型
while video.isOpened():
    ret, frame = video.read()  # 讀取影片檔案
    if ret:
        y = int(height - 50)  # Frames計數器位置
        cv2.putText(
            frame, "Frames  : " + str(counter), (0, y), font, 1, (255, 0, 0), 2
        )  # 顯示幀數
        seconds = round(counter / video_fps, 2)  # 計算秒數
        y = int(height - 10)  # Seconds計數器位置
        cv2.putText(
            frame, "Seconds : " + str(seconds), (0, y), font, 1, (255, 0, 0), 2
        )  # 顯示秒數
        cv2.imshow("myVideo", frame)  # 顯示影片
    else:
        break
    c = cv2.waitKey(50)  # 可以控制撥放速度
    counter += 1  # 幀數加 1
    if c == 27:  # 按 Esc 键, 結束
        break

video.release()  # 關閉輸出物件
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

video = cv2.VideoCapture("data/iceocean.mov")  # 開啟影片檔案

video_fps = video.get(cv2.CAP_PROP_FPS)  # 計算速度
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))  # 寬度
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 高度

# 建立裁剪影片物件
fourcc = cv2.VideoWriter_fourcc(*"I420")  # 編碼

new_video = cv2.VideoWriter("tmp_movie_b.avi", fourcc, video_fps, (width, height))
counter = video_fps * 5  # 影片長度
while video.isOpened() and counter >= 0:
    ret, frame = video.read()  # 讀取影片檔案
    if ret:
        new_video.write(frame)  # 寫入新影片
        counter -= 1  # 幀數減 1

video.release()  # 關閉輸出物件
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

capture = cv2.VideoCapture(0)  # 初始化攝影功能
while capture.isOpened():
    ret, frame = capture.read()  # 讀取設請鏡頭的影像
    cv2.imshow("Frame", frame)  # 顯示彩色影像
    # 轉灰階顯示
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray Frame", gray_frame)  # 顯示灰階影像
    c = cv2.waitKey(1)  # 等待時間 1 毫秒 ms
    if c == 27:  # 按 Esc 键, 結束
        break
capture.release()  # 關閉攝影功能
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

capture = cv2.VideoCapture(0)  # 初始化攝影功能
while capture.isOpened():
    ret, frame = capture.read()  # 讀取設請鏡頭的影像
    cv2.imshow("Frame", frame)  # 顯示彩色影像

    h_frame = cv2.flip(frame, 1)  # 水平翻轉
    cv2.imshow("Flip Frame", h_frame)  # 顯示水平翻轉
    c = cv2.waitKey(1)  # 等待時間 1 毫秒 ms
    if c == 27:  # 按 Esc 键, 結束
        break
capture.release()  # 關閉攝影功能
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

capture = cv2.VideoCapture(0)  # 初始化攝影功能
while capture.isOpened():
    ret, frame = capture.read()  # 讀取設請鏡頭的影像
    cv2.imshow("Frame", frame)  # 顯示攝影鏡頭的影像
    c = cv2.waitKey(1)  # 等待時間 1 毫秒 ms
    if c == 13:  # 按 Enter 鍵
        cv2.imwrite("mypict.png", frame)  # 拍照
        cv2.imshow("My Picture", frame)  # 開視窗顯示
    if c == 27:  # 按 Esc 键
        break
capture.release()  # 關閉攝影功能
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

capture = cv2.VideoCapture(0)  # 初始化攝影功能

fourcc = cv2.VideoWriter_fourcc(*"XVID")  # MPEG-4

# 建立輸出物件
video_out = cv2.VideoWriter("tmp_movie_a.avi", fourcc, 20.0, (640, 480))
while capture.isOpened():
    ret, frame = capture.read()
    if ret:
        video_out.write(frame)  # 寫入影片物件
        cv2.imshow("frame", frame)  # 顯示攝影鏡頭的影像
    c = cv2.waitKey(1)  # 等待時間 1 毫秒 ms
    if c == 27:  # 按 Esc 键, 結束
        break
capture.release()  # 關閉攝影功能
video_out.release()  # 關閉輸出物件
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

video = cv2.VideoCapture("tmp_movie_a.avi")  # 開啟影片檔案

while video.isOpened():
    ret, frame = video.read()  # 讀取影片檔案
    if ret:
        cv2.imshow("frame", frame)  # 顯示影片
    else:
        break
    c = cv2.waitKey(50)  # 可以控制撥放速度
    if c == 27:  # 按 Esc 键, 結束
        break

video.release()  # 關閉輸出物件
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

video = cv2.VideoCapture("data/iceocean.mov")  # 開啟影片檔案

while video.isOpened():
    ret, frame = video.read()  # 讀取影片檔案
    if ret:
        cv2.imshow("frame", frame)  # 顯示影片
    else:
        break
    c = cv2.waitKey(50)  # 可以控制撥放速度
    if c == 27:  # 按 Esc 键, 結束
        break

video.release()  # 關閉輸出物件
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

video = cv2.VideoCapture("data/iceocean2.mov")  # 開啟影片檔案

while video.isOpened():
    ret, frame = video.read()  # 讀取影片檔案
    if ret == True:
        cv2.imshow("frame", frame)  # 顯示彩色影片
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("gray_frame", gray_frame)  # 顯示灰階影片
    else:
        break
    c = cv2.waitKey(50)  # 可以控制撥放速度
    if c == 27:  # 按 Esc 键, 結束
        break

video.release()  # 關閉輸出物件
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

video = cv2.VideoCapture("data/iceocean.mov")  # 開啟影片檔案

while video.isOpened():
    ret, frame = video.read()  # 讀取影片檔案
    if ret:
        cv2.imshow("frame", frame)  # 顯示影片
        c = cv2.waitKey(50)  # 可以控制撥放速度
    else:
        break
    if c == 32:  # 是否按 空白鍵
        cv2.waitKey()  # 等待按鍵發生
        continue
    if c == 27:  # 按 Esc 键, 結束
        break

video.release()  # 關閉輸出物件
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個
