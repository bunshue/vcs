ESC = 27

import cv2

import sys
import math
import numpy as np

print("------------------------------------------------------------")  # 60個

print("移動偵測")

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("開啟攝影機失敗")
    sys.exit()

frame_pre = None  # 前影像, 預設是空的

while True:
    ret, frame = cap.read()  # 從攝影機擷取一張影像
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 灰階處理
        frame_now = cv2.GaussianBlur(gray, (13, 13), 5)  # 高斯模糊
        if frame_pre is not None:  # ←如果前影像不是空的, 就和前影像比對
            diff = cv2.absdiff(frame_now, frame_pre)  # 此影格與前影格的差異值
            ret, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)  # 門檻值
            contours, _ = cv2.findContours(
                thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE  # 找到輪廓
            )
            if contours:  # 如果有偵測到輪廓
                # print(type(contours))
                print(contours)
                cv2.drawContours(frame, contours, -1, (0, 0, 255), 2)
                print("偵測到移動")
            else:
                print(".", end="")
                pass

        cv2.imshow("WebCam", frame)
        frame_pre = frame_now.copy()
    k = cv2.waitKey(1)
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

cap = cv2.VideoCapture(0)
skip = 1  # 設定不比對的次數, 由於前影像是空的, 略過一次比對

while cap.isOpened():
    success, img = cap.read()
    if success:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 灰階處理
        img_now = cv2.GaussianBlur(gray, (13, 13), 5)  # 高斯模糊
        if skip > 0:  # ←如果 skip 大於 0 就略過不和前影像比對
            skip -= 1  # 將 skip 次數減 1
        else:  # ←如果 skip==0 就和前影像比對
            diff = cv2.absdiff(img_now, img_pre)  # 此影格與前影格的差異值

            # 設定門檻值
            ret, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
            # 找輪廓
            contours, _ = cv2.findContours(
                thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
            )

            # 如果有偵測到輪廓
            if contours:
                cv2.drawContours(img, contours, -1, (0, 0, 255), 2)
                print("偵測到移動")
                skip = 10  # ←略過 N 次不比對
            else:
                print(".", end="")
        cv2.imshow("frame", img)
        img_pre = img_now.copy()

    k = cv2.waitKey(50)  # ←暫停 50 毫秒 (0.05 秒), 並檢查是否有按鍵輸入
    if k == ESC:
        # if k == ord("q"):  # Q 的寫法
        cv2.destroyAllWindows()
        cap.release()
        break

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個
