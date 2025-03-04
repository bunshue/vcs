"""
WebCam 使用

一般使用

目前 webcam 僅 win10/x64 電腦可用
"""

ESC = 27

import cv2
import sys
import time

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("最簡易, 按 ESC 離開")

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("開啟攝影機失敗")
    sys.exit()

while True:
    ret, frame = cap.read()  # 從攝影機擷取一張影像

    if ret == False:
        print("無影像, 離開")
        break

    # 加上文字 ST
    cv2.rectangle(frame, (10, 10), (200, 42), (0, 0, 0), -1)  # 加上黑色區塊
    text = "English Only"
    org = (15, 35)
    fontFace = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    color = (255, 255, 255)
    thickness = 2
    lineType = cv2.LINE_AA
    cv2.putText(frame, text, org, fontFace, fontScale, color, thickness, lineType)
    # 加上文字 SP

    cv2.imshow("WebCam", frame)

    k = cv2.waitKey(1)
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("最簡易, 按 ESC 離開 + 裁出一塊, 另外顯示之")

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("開啟攝影機失敗")
    sys.exit()

while True:
    ret, frame = cap.read()  # 從攝影機擷取一張影像

    if ret == False:
        print("無影像, 離開")
        break

    cv2.imshow("WebCam", frame)

    # 裁出一塊, 另外顯示之
    x_st = 0
    y_st = 0
    W = 320
    H = 240
    x1 = x_st
    x2 = x_st + W
    y1 = y_st
    y2 = y_st + H
    # print(x1, x2, y1, y2)
    frame2 = frame[y1:y2, x1:x2]  # 取出一塊
    cv2.imshow("WebCam_Cut", frame2)

    k = cv2.waitKey(1)
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("按 ESC 離開")
print("按 S 存圖")

cap = cv2.VideoCapture(0)  # 建立攝影機物件
if not cap.isOpened():
    print("開啟攝影機失敗")
    sys.exit()
else:
    ret, frame = cap.read()  # 從攝影機擷取一張影像

    if ret == False:
        print("無影像, 離開")
    else:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_blur_pre = cv2.GaussianBlur(gray, (13, 13), 15)  # 高斯模糊

"""
#調整影像大小
ratio = cap.get(cv2.CAP_PROP_FRAME_WIDTH) / cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
WIDTH = 320
HEIGHT = int(WIDTH / ratio)
"""

time_old = time.time()
while True:
    # begin_time = time.time()  # 計算fps
    ret, frame = cap.read()  # 從攝影機擷取一張影像

    if ret == False:
        print("無影像, 離開")
        break

    """
    #調整影像大小
    frame = cv2.resize(frame, (WIDTH, HEIGHT))
    frame = cv2.flip(frame, 1)
    """

    # 原圖
    cv2.imshow("WebCam1", frame)

    # 灰階處理
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("WebCam2", gray)

    # 高斯模糊
    frame_blur = cv2.GaussianBlur(gray, (13, 13), 15)
    cv2.imshow("WebCam3", frame_blur)

    # 比較影像
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 灰階處理
    frame_blur_now = cv2.GaussianBlur(gray, (13, 13), 15)  # 高斯模糊
    diff = cv2.absdiff(frame_blur_now, frame_blur_pre)  # 現在影像與前影像相減
    cv2.imshow("WebCam4", diff)  # 顯示相減後的影像
    frame_blur_pre = frame_blur_now.copy()  # 將現在影像設為前影像

    time_new = time.time()

    fps = 1 / (time_new - time_old)
    # print('{:.1f}'.format(fps))
    time_old = time_new

    k = cv2.waitKey(1)
    if k == ESC:
        break
    elif k == ord("S") or k == ord("s"):  # 按下 S(s), 存圖
        image_filename = (
            "Image_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".jpg"
        )
        cv2.imwrite(image_filename, frame)
        print("已存圖, 檔案 :", image_filename)

# 釋放所有資源
cap.release()  # 釋放攝影機
cv2.destroyAllWindows()  # 關閉所有 OpenCV 視窗

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("更改視訊的解析度")

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("開啟攝影機失敗")
    sys.exit()

# Webcam有支援的模式 以下的設定才會有用
# 設定影像的尺寸大小
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cap.set(cv2.CAP_PROP_FPS, 30)

while True:
    ret, frame = cap.read()  # 從攝影機擷取一張影像
    if ret == False:
        print("無影像, 離開")
        break
    cv2.imshow("WebCam", frame)
    k = cv2.waitKey(1)
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個


# 取得影像的尺寸大小
w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("Image Size: %d x %d" % (w, h))


"""
WINDOW_NORMAL – Allows to manually change window size
WINDOW_AUTOSIZE(Default) – Automatically sets the window size
WINDOW_FULLSCREEN – Changes the window size to fullscreen
"""
cv2.namedWindow("WebCam", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("WebCam", cv2.WINDOW_NORMAL)
