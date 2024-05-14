'''
WebCam 使用

一般使用

目前 webcam 僅 x64 電腦可用
'''

ESC = 27

import cv2
import sys
import time

print('------------------------------------------------------------')	#60個

print('最簡易, 按 ESC 離開')

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('開啟攝影機失敗')
    sys.exit()
else:
    print('Video device opened')

while True:
    ret, frame = cap.read()   # 從攝影機擷取一張影像

    if ret == False:
      print('無影像, 離開')
      break

    cv2.imshow('WebCam', frame)

    k = cv2.waitKey(1)
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

print('按 ESC 離開')
print('按 S 存圖')

cv2.namedWindow('WebCam', cv2.WINDOW_NORMAL)

cap = cv2.VideoCapture(0)   # 建立攝影機物件

# 取得影像的尺寸大小
w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("Image Size: %d x %d" % (w, h))

if not cap.isOpened():
    print('開啟攝影機失敗')
    sys.exit()
else:
    print('Video device opened')
    ret, frame = cap.read()   # 從攝影機擷取一張影像
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_blur_pre = cv2.GaussianBlur(gray, (13, 13), 15)      # 高斯模糊

'''
# 取得 Codec 名稱
fourcc = cap.get(cv2.CAP_PROP_FOURCC)
codec = decode_fourcc(fourcc)
print("Codec: " + codec)
'''

#無效
# 設定影像的尺寸大小
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

'''
#調整影像大小
ratio = cap.get(cv2.CAP_PROP_FRAME_WIDTH) / cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
WIDTH = 320
HEIGHT = int(WIDTH / ratio)
'''

time_old =time.time()
while True:
    #begin_time = time.time()  # 計算fps
    ret, frame = cap.read()   # 從攝影機擷取一張影像

    if ret == False:
      print('無影像, 離開')
      break

    '''
    #調整影像大小
    frame = cv2.resize(frame, (WIDTH, HEIGHT))
    frame = cv2.flip(frame, 1)
    '''

    # 原圖
    cv2.imshow('WebCam1', frame)

    # 灰階處理
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('WebCam2', gray)

    # 高斯模糊
    frame_blur = cv2.GaussianBlur(gray, (13, 13), 15)
    cv2.imshow('WebCam3', frame_blur)

    # 比較影像
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)        # 灰階處理
    frame_blur_now = cv2.GaussianBlur(gray, (13, 13), 15)       # 高斯模糊
    diff = cv2.absdiff(frame_blur_now, frame_blur_pre)    # 現在影像與前影像相減
    cv2.imshow('WebCam4', diff)              # 顯示相減後的影像
    frame_blur_pre = frame_blur_now.copy()    # 將現在影像設為前影像

    time_new = time.time()

    fps = 1 / (time_new - time_old)
    #print('{:.1f}'.format(fps))
    time_old = time_new

    k = cv2.waitKey(1)
    if k == ESC:
        break
    elif k == ord('S') or k == ord('s'):  # 按下 S(s), 存圖
        image_filename = 'Image_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.jpg'
        cv2.imwrite(image_filename, frame)
        print('已存圖, 檔案 :', image_filename)

# 釋放所有資源
cap.release()   # 釋放攝影機
cv2.destroyAllWindows() # 關閉所有 OpenCV 視窗

print('------------------------------------------------------------')	#60個

print('更改視訊的解析度')

cap = cv2.VideoCapture(0)

#Webcam有支援的模式 以下的設定才會有用
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cap.set(cv2.CAP_PROP_FPS, 30)

while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow("WebCam", frame)
    k = cv2.waitKey(1)
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print('移動偵測')

cap = cv2.VideoCapture(0)

img_pre = None   # 前影像, 預設是空的
while cap.isOpened():
    success, img = cap.read()
    if success:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)        # 灰階處理
        img_now = cv2.GaussianBlur(gray, (13, 13), 5)       # 高斯模糊
        if img_pre is not None:  # ←如果前影像不是空的, 就和前影像比對
            diff = cv2.absdiff(img_now, img_pre)   # 此影格與前影格的差異值
            ret, thresh = cv2.threshold(diff, 25, 255,  # 門檻值
                                        cv2.THRESH_BINARY)
            contours, _ = cv2.findContours(thresh,    # 找到輪廓
                                           cv2.RETR_EXTERNAL,
                                           cv2.CHAIN_APPROX_SIMPLE)
            if contours:    # 如果有偵測到輪廓
                #print(type(contours))
                print(contours)
                cv2.drawContours(img, contours, -1, (0, 0, 255), 2)
                print('偵測到移動')
            else:
                print('靜止畫面', end = ' ')
                pass

        cv2.imshow('WebCam', img)
        img_pre = img_now.copy()
    k = cv2.waitKey(1)
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

