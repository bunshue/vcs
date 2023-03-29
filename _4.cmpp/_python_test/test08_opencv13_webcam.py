import cv2
import sys

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Could not open video device')
    sys.exit()
else:
    print('Video device opened')


''' 無效
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
'''
while(True):
    ret, frame = cap.read()   # 從攝影機擷取一張影像

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # 彩色轉灰階
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #改變圖片大小
    #frame = cv2.resize(frame, None, fx = 1.5, fy = 1.5, interpolation = cv2.INTER_AREA)

    cv2.imshow('WebCam', frame)    # 顯示圖片, 彩色
    #cv2.imshow('WebCam', gray)    # 顯示圖片, 黑白

    c = cv2.waitKey(1)
    if c == 27:     #ESC
        break
    elif c == ord('q'): # 若按下 q 鍵則離開迴圈
        break
    elif c == ord('s'): # 若按下 s 鍵則存圖
        cv2.imwrite('test.jpg', frame)


cap.release()   # 釋放攝影機
cv2.destroyAllWindows() # 關閉所有 OpenCV 視窗
