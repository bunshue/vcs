"""
WebCam 使用
一般使用
錄影存檔, 兩種存檔格式

目前 webcam 僅 x64 電腦可用
"""

import cv2

ESC = 27
SPACE = 32

print("------------------------------------------------------------")  # 60個

import os
import sys
import time
import math
import random
import numpy as np

print("------------------------------------------------------------")  # 60個

#用XVID格式存avi檔
record_filename_xvid = 'tmp_webcam_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.avi'

#用MP4V格式存mp4檔
record_filename_mp4v = 'tmp_webcam_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.mp4'

"""

視訊編碼的名稱、編碼字串、副檔名

編碼名稱	編碼字串	視訊檔副檔名
YUV		*"I420"		.avi
MPEG-1		*"PIMT"		.avi
MPEG-4		*"XVID"		.avi
MP4		*"MP4V"		.mp4
Ogg Vorbis	*"THEO"		.ogv

"""

print("------------------------------------------------------------")  # 60個

print("錄影1, 按 ESC 離開")

cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))    # 取得影像寬度
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 取得影像高度

#用XVID格式存avi檔
record_filename_xvid = 'tmp1_webcam_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.avi'

#建立視訊編碼 fourcc XVID
fourcc = cv2.VideoWriter_fourcc(*"XVID")

fps = 20
size = (width, height)
out = cv2.VideoWriter(record_filename_xvid, fourcc, fps, size)

while(cap.isOpened()):
  ret, frame = cap.read()
  if ret == True:
    out.write(frame)
    cv2.imshow("WebCam1", frame)
    k = cv2.waitKey(1)
    if k == ESC:     #ESC
      break
  else:
    break

cap.release()
out.release()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

print("錄影2, 按 ESC 離開")

cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))    # 取得影像寬度
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 取得影像高度

# 調整影片大小
ratio = cap.get(cv2.CAP_PROP_FRAME_WIDTH) / cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
WIDTH = 400
HEIGHT = int(WIDTH / ratio)

# 用MP4V格式存mp4檔
record_filename_mp4v = 'tmp2_webcam_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.mp4'

#建立視訊編碼 fourcc MP4V
fourcc = cv2.VideoWriter_fourcc(*'MP4V')

fps = 30
size = (width, height)
out = cv2.VideoWriter(record_filename_mp4v, fourcc, fps, (WIDTH, HEIGHT))

# 解析 Fourcc 格式資料的函數
def decode_fourcc(v):
  v = int(v)
  return "".join([chr((v >> 8 * i) & 0xFF) for i in range(4)])

# 取得影像的尺寸大小
w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("Image Size: %d x %d" % (w, h))

if not cap.isOpened():
    print('Could not open video device')
    sys.exit()
else:
    print('Video device opened')

# 取得 Codec 名稱
fourcc = cap.get(cv2.CAP_PROP_FOURCC)
codec = decode_fourcc(fourcc)
print("Codec: " + codec)

#無效
# 設定影像的尺寸大小
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

while True:
    ret, frame = cap.read()   # 從攝影機擷取一張影像

    if ret == False:
      print('無影像, 離開')
      break

    """ 調整影片大小
    frame = cv2.resize(frame, (WIDTH, HEIGHT))
    frame = cv2.flip(frame, 1)
    """

    #改變圖片大小
    #frame = cv2.resize(frame, None, fx = 1.5, fy = 1.5, interpolation = cv2.INTER_AREA)

    #彩色轉灰階
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('WebCam2', frame)    # 顯示圖片

    # 寫入影格
    out.write(frame)  # 影像大小必須與設定一致，否則會輸出失敗

    k = cv2.waitKey(1)
    if k == ESC:     #ESC
        break
    elif k == ord('s'): # 若按下 s 鍵則存圖
        image_filename = 'Image_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.jpg';
        cv2.imwrite(image_filename, frame)
        print('已存圖, 檔案 :', image_filename)

# 釋放所有資源
out.release()
cap.release()   # 釋放攝影機
cv2.destroyAllWindows() # 關閉所有 OpenCV 視窗

print('已存檔 ' + record_filename_mp4v)

print("------------------------------------------------------------")  # 60個

print("錄影3, 按 ESC 離開")

cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))    # 取得影像寬度
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 取得影像高度

#建立視訊編碼 fourcc MJPG
fourcc = cv2.VideoWriter_fourcc(*'MJPG')          # 設定影片的格式為 MJPG

fps = 20.0
size = (width, height)
out = cv2.VideoWriter('tmp3_output.mp4', fourcc, fps, size)  # 產生空的影片

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    out.write(frame)       # 將取得的每一幀圖像寫入空的影片
    
    cv2.imshow("WebCam3", frame)

    k = cv2.waitKey(1) # 等待按鍵輸入
    if k == ESC:     #ESC
        break

cap.release()
out.release()      # 釋放資源
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("錄影4, 按 ESC 離開 灰階")

cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))    # 取得影像寬度
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 取得影像高度

#建立視訊編碼 fourcc MJPG
fourcc = cv2.VideoWriter_fourcc(*'MJPG')

fps = 20.0
size = (width, height)
out = cv2.VideoWriter('tmp4_output.mov', fourcc, fps, size)

# 如果轉換成黑白影片後如果無法開啟，請加上 isColor=False 參數設定
# out = cv2.VideoWriter('tmp_output.mov', fourcc, fps, size, isColor=False)
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
    
    cv2.imshow("WebCam4", gray)

    k = cv2.waitKey(1) # 等待按鍵輸入
    if k == ESC:     #ESC
        break

cap.release()
out.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("錄影5, 按 ESC 離開")

cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))    # 取得影像寬度
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 取得影像高度

#建立視訊編碼 fourcc MJPG
fourcc = cv2.VideoWriter_fourcc(*'MJPG')          # 設定影片的格式為 MJPG

fps = 20.0
size = (width, height)
out = cv2.VideoWriter('tmp5_output.mp4', fourcc, fps, size)  # 產生空的影片

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    img_1 = frame
    img_2 = cv2.flip(img_1, 0)             # 上下翻轉
    out.write(img_2)                       # 將取得的每一幀圖像寫入空的影片
    
    cv2.imshow("WebCam5", frame)

    k = cv2.waitKey(1) # 等待按鍵輸入
    if k == ESC:     #ESC
        break

cap.release()
out.release()      # 釋放資源
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("錄影6, 按 ESC 離開")

cap = cv2.VideoCapture(0)                 # 讀取攝影鏡頭
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))    # 取得影像寬度
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 取得影像高度

#建立視訊編碼 fourcc MJPG
fourcc = cv2.VideoWriter_fourcc(*'MJPG')  # 設定輸出影片的格式為 MJPG

fps = 20
size = (width, height)
out = cv2.VideoWriter('tmp6_output.mov', fourcc, 20.0, (width, height))  # 產生空的影片

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, img = cap.read()               # 讀取影片的每一個影格
    if not ret:
        print("Cannot receive frame")
        break
        
    k = cv2.waitKey(1) # 等待按鍵輸入

    if k == ESC:
        break
        
    cv2.imshow('WebCam6', img)
    out.write(img)  # 儲存影片

out.release()       # 釋放資源
cap.release()       # 釋放資源
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


