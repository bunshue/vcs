'''
WebCam 使用
一般使用
偵測特定顏色 紅色

目前 webcam 僅 x64 電腦可用
'''

import cv2

import sys
import matplotlib.pyplot as plt
import numpy as np
import math

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

import time

cap = cv2.VideoCapture(0)

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

count = 0
background = 0

## Capture the background in range of 60
for i in range(60):
    ret,background = cap.read()
background = np.flip(background, axis = 1)

while True:
    ret, frame = cap.read()   # 從攝影機擷取一張影像
    
    if ret == False:
      print('無影像, 離開')
      break

    count+=1
    #frame = np.flip(frame, axis=1)  #左右顛倒
    
    ## Convert the color space from BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #偵測特定顏色 紅色
    ## Generate masks to detect red color
    lower_red = np.array([0,100,0])
    upper_red = np.array([9,255,255])
    mask1 = cv2.inRange(hsv,lower_red,upper_red)

    lower_red = np.array([170,100,00])
    upper_red = np.array([180,255,255])
    mask2 = cv2.inRange(hsv,lower_red,upper_red)

    mask1 = mask1 + mask2

    ## Open and Dilate the mask image
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3),np.uint8))
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3,3),np.uint8))
  
    ## Create an inverted mask to segment out the red color from the frame
    mask2 = cv2.bitwise_not(mask1)
 
    ## Segment the red color part out of the frame using bitwise and with the inverted mask
    res1 = cv2.bitwise_and(frame, frame, mask=mask2)

    ## Create image showing static background frame pixels only for the masked region
    res2 = cv2.bitwise_and(background, background, mask = mask1)
  
    ## Generating the final output and writing
    finalOutput = cv2.addWeighted(res1,1,res2,1,0)
    cv2.imshow('WebCam', finalOutput)
    
    k = cv2.waitKey(1)
    if k == 27:     #ESC
        break
    elif k == ord('q'): # 若按下 q 鍵則離開迴圈
        break
    elif k == ord('s'): # 若按下 s 鍵則存圖
        image_filename = 'Image_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.jpg';
        cv2.imwrite(image_filename, frame)
        print('已存圖')

# 釋放所有資源
cap.release()   # 釋放攝影機
cv2.destroyAllWindows() # 關閉所有 OpenCV 視窗
