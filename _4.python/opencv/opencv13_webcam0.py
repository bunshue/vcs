'''
WebCam 使用

一般使用

目前 webcam 僅 x64 電腦可用
'''

import cv2
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

while(True):
    ret, frame = cap.read()   # 從攝影機擷取一張影像

    if ret == False:
      print('無影像, 離開')
      break

    cv2.imshow('WebCam', frame)    # 顯示圖片, 彩色

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

