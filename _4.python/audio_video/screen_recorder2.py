"""
螢幕錄影 無聲音

# 每一秒截一張圖 用 1 fps 錄製

是否任意停止皆可成檔案?

"""

RECORD_TIME_MINUTE = 120

import os
import sys
import time
import random

import cv2
import numpy as np
from PIL import ImageGrab

print('------------------------------------------------------------')	#60個

image = ImageGrab.grab() # 取得目前的螢幕畫面
width = image.size[0]
height = image.size[1]
print("width:", width, "height:", height)
print("image mode:",image.mode)
k=np.zeros((width,height),np.uint8)
fourcc = cv2.VideoWriter_fourcc(*'XVID')#编码格式

import datetime
now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
print("現在時間 :", now)

fps = 1
record_filename = 'tmp_screen_recording2_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.avi'
video = cv2.VideoWriter(record_filename, fourcc, fps, (width, height))

cnt = 0
while True:
    #print(cnt, end = " ")
    img_rgb = ImageGrab.grab()
    img_bgr = cv2.cvtColor(np.array(img_rgb), cv2.COLOR_RGB2BGR)#转为opencv的BGR格式
    video.write(img_bgr)
    cnt += 1
    if cnt > 60 * RECORD_TIME_MINUTE:
        break
    time.sleep(1)

print('OK')
video.release()
cv2.destroyAllWindows()

import datetime
now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
print("現在時間 :", now)

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個

