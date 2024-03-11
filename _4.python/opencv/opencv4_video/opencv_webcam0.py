'''
WebCam 使用

一般使用

目前 webcam 僅 x64 電腦可用
'''

ESC = 27

import cv2
import time

print('------------------------------------------------------------')	#60個

print('按Q離開')
print('按S存圖')

#cv2.namedWindow('frame', cv2.WINDOW_NORMAL)

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

    cv2.imshow('WebCam', frame)    # 顯示圖片, 原圖

    time_new = time.time()

    fps = 1 / (time_new - time_old)
    #print('{:.1f}'.format(fps))
    time_old = time_new

    k = cv2.waitKey(1) # 等待按鍵輸入
    if k == ESC:     #ESC
        break
    elif k == ord('Q') or k == ord('q'):  # 按下 Q(q) 結束迴圈
        break
    elif k == ord('S') or k == ord('s'):  # 按下 S(s), 存圖
        image_filename = 'Image_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.jpg'
        cv2.imwrite(image_filename, frame)
        print('已存圖, 檔案 :', image_filename)

# 釋放所有資源
cap.release()   # 釋放攝影機
cv2.destroyAllWindows() # 關閉所有 OpenCV 視窗

print('------------------------------------------------------------')	#60個

print('錄影')




print('------------------------------------------------------------')	#60個


