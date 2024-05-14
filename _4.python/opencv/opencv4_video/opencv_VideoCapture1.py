import cv2

ESC = 27
SPACE = 32

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

print('------------------------------------------------------------')	#60個

video_filename = 'C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4'

cap = cv2.VideoCapture(video_filename)
while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    k = cv2.waitKey(1)
    if k == ESC:     #ESC
        break

cap.release()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

video_filename = 'C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4'

cap = cv2.VideoCapture(video_filename)

while(cap.isOpened()):
    ret, frame = cap.read()
    frame=cv2.Canny(frame,100,200)  #加上Canny處理
    cv2.imshow('frame',frame)
    k = cv2.waitKey(1)
    if k == ESC:     #ESC
        break

cap.release()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

cap = cv2.VideoCapture(0)
fourcc = -1
out = cv2.VideoWriter('output.avi',fourcc, 20, (640,480))
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        out.write(frame)
        cv2.imshow('frame',frame)

        k = cv2.waitKey(1)
        if k == ESC:     #ESC
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#播放檔案
video_filename = 'C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4'
vid = cv2.VideoCapture(video_filename)
#In the [your_file_name] mention the Video File that you want to process and detect the Face in

while True:
    ret, frame = vid.read()
    if ret == True:
        #frame = cv2.resize(frame,(int(frame.shape[1]/2),int(frame.shape[0]/2)))    #調整畫面大小
        cv2.imshow('Video Player', frame)
        k = cv2.waitKey(1)
        if k == ESC:     #ESC
            break
    else:
        break

vid.release()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


