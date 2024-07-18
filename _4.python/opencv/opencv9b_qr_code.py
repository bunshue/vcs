"""

cv2之各種影像處理功能

QR code

"""

import cv2
import numpy as np

ESC = 27
SPACE = 32

red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)
white = (255, 255, 255)

print("------------------------------------------------------------")  # 60個

print("OpenCV_34")

filename = "C:/_git/vcs/_4.python/opencv/data/QR1.png"

# 檔案 => cv2影像
image = cv2.imread(filename)  # 開啟圖片

qrcode = cv2.QRCodeDetector()  # 建立 QRCode 偵測器
data, bbox, rectified = qrcode.detectAndDecode(image)  # 偵測圖片中的 QRCode
# 如果 bbox 是 None 表示圖片中沒有 QRCode
if bbox is not None:
    print(data)  # QRCode 的內容
    print(bbox)  # QRCode 的邊界
    print(rectified)  # 換成垂直 90 度的陣列

cv2.imshow("image", image)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_35")

filename = "C:/_git/vcs/_4.python/opencv/data/QR1.png"

# 檔案 => cv2影像
image = cv2.imread(filename)

qrcode = cv2.QRCodeDetector()
data, bbox, rectified = qrcode.detectAndDecode(image)


# 取得座標的函式
def boxSize(arr):
    global data
    box_roll = np.rollaxis(arr, 1, 0)  # 轉置矩陣，把 x 放在同一欄，y 放在同一欄
    xmax = int(np.amax(box_roll[0]))  # 取出 x 最大值
    xmin = int(np.amin(box_roll[0]))  # 取出 x 最小值
    ymax = int(np.amax(box_roll[1]))  # 取出 y 最大值
    ymin = int(np.amin(box_roll[1]))  # 取出 y 最小值
    return (xmin, ymin, xmax, ymax)


# 如果 bbox 是 None 表示圖片中沒有 QRCode
if bbox is not None:
    print(data)
    print(bbox)
    print(rectified)
    box = boxSize(bbox[0])
    cv2.rectangle(image, (box[0], box[1]), (box[2], box[3]), red, 5)  # 畫矩形

cv2.imshow("image", image)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_36")

from PIL import ImageFont, ImageDraw, Image  # 載入 PIL ( 為了放中文字 )

filename = "C:/_git/vcs/_4.python/opencv/data/QR1.png"

# 檔案 => cv2影像
image = cv2.imread(filename)

qrcode = cv2.QRCodeDetector()
data, bbox, rectified = qrcode.detectAndDecode(image)


# 建立放入文字的函式
def putText(x, y, text, color=(0, 0, 0)):
    global image
    # font_filename = 'NotoSansTC-Regular.otf'      # 字體 ( 從 Google Font 下載 )
    font = ImageFont.truetype(font_filename, 20)  # 設定字型與大小
    imagePil = Image.fromarray(image)  # 將 image 轉換成 PIL 圖片物件
    draw = ImageDraw.Draw(imagePil)  # 建立繪圖物件
    draw.text((x, y), text, fill=color, font=font)  # 寫入文字
    image = np.array(imagePil)  # 轉換回 np array


def boxSize(arr):
    global data
    box_roll = np.rollaxis(arr, 1, 0)
    xmax = int(np.amax(box_roll[0]))
    xmin = int(np.amin(box_roll[0]))
    ymax = int(np.amax(box_roll[1]))
    ymin = int(np.amin(box_roll[1]))
    return (xmin, ymin, xmax, ymax)


if bbox is not None:
    print(data)
    print(bbox)
    print(rectified)
    box = boxSize(bbox[0])
    cv2.rectangle(image, (box[0], box[1]), (box[2], box[3]), red, 5)

cv2.imshow("image", image)
cv2.waitKey()
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個
print("OpenCV_37")

""" many-qr-code
from PIL import ImageFont, ImageDraw, Image

# 檔案 => cv2影像
image = cv2.imread("many-qrcode.jpg")

def putText(x,y,text,color=(0,0,0)):
    global image
    #font_filename = 'NotoSansTC-Regular.otf'
    font = ImageFont.truetype(font_filename, 20)
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

qrcode = cv2.QRCodeDetector()
ok, data, bbox, rectified = qrcode.detectAndDecodeMulti(image)   # 改用 detectAndDecodeMulti
# 如果有偵測到
if ok:
    # 使用 for 迴圈取出每個 QRCode 的資訊
    for i in range(len(data)):
        print(data[i])
        print(bbox[i])
        text = data[i]          # QRCode 內容
        box = boxSize(bbox[i])  # QRCode 左上與右下座標
        cv2.rectangle(image,(box[0],box[1]),(box[2],box[3]),(0,0,255),5)  # 標記外框
        putText(box[0],box[3],text)   # 寫出文字

cv2.imshow('image', image)
cv2.waitKey()
cv2.destroyAllWindows()
"""

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
