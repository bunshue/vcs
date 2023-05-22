'''
WebCam 使用
一般使用
錄影存檔

目前 webcam 僅 x64 電腦可用
'''

filename = 'C:/_git/vcs/_1.data/______test_files2/output.avi'

import cv2
import sys
import time

#準備存檔用設定
#使用 XVID 編碼
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# 建立 VideoWriter 物件，輸出影片至檔案
# FPS 值為 20.0，解析度為 640x360
out = cv2.VideoWriter(filename, fourcc, 20.0, (640, 480))

# 解析 Fourcc 格式資料的函數
def decode_fourcc(v):
  v = int(v)
  return "".join([chr((v >> 8 * i) & 0xFF) for i in range(4)])


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
# 設定擷取影像的尺寸大小
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

while True:
    ret, frame = cap.read()   # 從攝影機擷取一張影像

    if ret == False:
      print('無影像, 離開')
      break

    # 彩色轉灰階
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #改變圖片大小
    #frame = cv2.resize(frame, None, fx = 1.5, fy = 1.5, interpolation = cv2.INTER_AREA)

    cv2.imshow('WebCam', frame)    # 顯示圖片, 彩色
    #cv2.imshow('WebCam', gray)    # 顯示圖片, 黑白

    # 寫入影格
    out.write(frame)

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
out.release()
cap.release()   # 釋放攝影機
cv2.destroyAllWindows() # 關閉所有 OpenCV 視窗

print('已存檔 ' + filename)
