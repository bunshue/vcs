"""
opencv 集合 新進


"""

import cv2

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

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

img = cv2.imread(filename)
fliped_img = cv2.flip(img, -1)

cv2.imshow("Koala:fliped", fliped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print('播完影片不會有錯誤訊息')

video_filename = 'C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4'

cap = cv2.VideoCapture(video_filename)

while(cap.isOpened()):
  ret, frame = cap.read()
  if ret:
      cv2.imshow("Frame", frame)
  if cv2.waitKey(1) & 0xFF == ord("q"):
      break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

video_filename = 'C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4'

cap = cv2.VideoCapture(video_filename)

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("影格尺寸:", width, "x", height)
fourcc = int(cap.get(cv2.CAP_PROP_FOURCC))
codec = (chr(fourcc&0xFF)+chr((fourcc>>8)&0xFF)+
        chr((fourcc>>16)&0xFF)+chr((fourcc>>24)&0xFF))
print("Codec編碼:", codec)

print("------------------------------------------------------------")  # 60個

video_filename = 'C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4'

cap = cv2.VideoCapture(video_filename)

frame_count = 0
while True:
  ret, frame = cap.read()
  if not ret:
      break
  frame_count = frame_count + 1

print("總影格數 = ", frame_count)
cap.release()

print("------------------------------------------------------------")  # 60個

video_filename = 'C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4'

cap = cv2.VideoCapture(video_filename)

fps = cap.get(cv2.CAP_PROP_FPS)
print("FPS =", fps)

cap.release()

print("------------------------------------------------------------")  # 60個

cap = cv2.VideoCapture(0)

#更改視訊的解析度
#Webcam有支援的模式 以下的設定才會有用
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cap.set(cv2.CAP_PROP_FPS, 30)

while(cap.isOpened()):
  ret, frame = cap.read()
  cv2.imshow("Frame", frame)      
  if cv2.waitKey(1) & 0xFF == ord("q"):
      break
  
cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("錄影")

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("tmp_output.avi", fourcc, 20, (640,480))

while(cap.isOpened()):
  ret, frame = cap.read()
  if ret == True:
    out.write(frame)
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
      break
  else:
    break

cap.release()
out.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

