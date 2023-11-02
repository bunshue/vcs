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

x_st = 150
y_st = 150
x_sp = x_st + 300
y_sp = y_st + 200

RECT = ((x_st, y_st), (x_sp, y_sp))
(left, top), (right, bottom) = RECT

def roiarea(frame):
    return frame[top:bottom, left:right]
    
def replaceroi(frame, roi):
    frame[top:bottom, left:right] = roi
    return frame

def image_process(roi):
    '''
    print(type(roi))
    print('shape = ', roi.shape)
    print('W = ', roi.shape[1])
    print('H = ', roi.shape[0])
    '''
    W = roi.shape[1]
    H = roi.shape[0]
    for j in range(H):
        for i in range(W):
            b = roi[j][i][0]
            g = roi[j][i][1]
            r = roi[j][i][2]
            a = ((np.int16)(b) + (np.int16)(g) + (np.int16)(r))//3
            #roi[j][i][0] = roi[j][i][1] = roi[j][i][2] = (np.uint8)(a)
            #roi[j][i][0] = 255    #B
            #roi[j][i][1] = 255    #G
            roi[j][i][2] = 255     #R
    return roi

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    roi1 = roiarea(frame)    #取出子畫面
    #roi2 = cv2.cvtColor(roi1, cv2.COLOR_BGR2HSV) #做影像處理1
    roi2 = image_process(roi1) #做影像處理2
    frame = replaceroi(frame, roi2)  #貼回原畫面
    cv2.rectangle(frame, RECT[0], RECT[1], (0, 255, 0), 2)#畫一個框 (BGR), linewidth
   
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) == 27:
        roi2 = image_process(roi1) #做影像處理
        cv2.destroyAllWindows()
        break
