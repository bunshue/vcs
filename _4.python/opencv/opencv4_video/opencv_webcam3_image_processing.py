import cv2

import sys
import numpy as np
import math

print("------------------------------------------------------------")  # 60個

def image_process(roi):
    """
    print(type(roi))
    print('shape = ', roi.shape)
    print('W = ', roi.shape[1])
    print('H = ', roi.shape[0])
    """
    W = roi.shape[1]
    H = roi.shape[0]
    for j in range(H):
        for i in range(W):
            b = roi[j][i][0]
            g = roi[j][i][1]
            r = roi[j][i][2]
            a = ((np.int16)(b) + (np.int16)(g) + (np.int16)(r)) // 3
            # roi[j][i][0] = roi[j][i][1] = roi[j][i][2] = (np.uint8)(a)
            # roi[j][i][0] = 255    #B
            # roi[j][i][1] = 255    #G
            roi[j][i][2] = 255  # R
    return roi

print('擷取畫面的某一塊 做灰階處理 再貼回主畫面')

x_st, y_st = 0, 0
w, h = 100, 100
RECT = ((x_st, y_st), (x_st + w, y_st + h))
(left, top), (right, bottom) = RECT

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    # 取出子畫面
    roi1 = frame[top:bottom, left:right]

    
    # roi2 = cv2.cvtColor(roi1, cv2.COLOR_BGR2HSV) #做影像處理1
    roi2 = image_process(roi1)  # 做影像處理2

    
    # 貼回原畫面
    frame[top:bottom, left:right] = roi2

    #標示出來    
    cv2.rectangle(frame, RECT[0], RECT[1], (0, 255, 0), 2)

    cv2.imshow("frame", frame)
    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        break

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
