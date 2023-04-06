# 目前 webcam 僅 x64 電腦可用

filename = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/output.avi'

import cv2
import sys

cap = cv2.VideoCapture(0)

#無效
# 設定影像的尺寸大小
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 960)


# 解析 Fourcc 格式資料的函數
def decode_fourcc(v):
  v = int(v)
  return "".join([chr((v >> 8 * i) & 0xFF) for i in range(4)])

# 取得影像的尺寸大小
w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("Image Size: %d x %d" % (w, h))

# 取得 Codec 名稱
fourcc = cap.get(cv2.CAP_PROP_FOURCC)
codec = decode_fourcc(fourcc)
print("Codec: " + codec)

if not cap.isOpened():
    print('Could not open video device')
    sys.exit()
else:
    print('Video device opened')

#無效
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 設定擷取影像的尺寸大小
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

# 存檔用
# 使用 XVID 編碼
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# 建立 VideoWriter 物件，輸出影片至檔案
# FPS 值為 20.0，解析度為 640x360
out = cv2.VideoWriter(filename, fourcc, 20.0, (640, 480))

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

    # 寫入影格
    out.write(frame)

    c = cv2.waitKey(1)
    if c == 27:     #ESC
        break
    elif c == ord('q'): # 若按下 q 鍵則離開迴圈
        break
    elif c == ord('s'): # 若按下 s 鍵則存圖
        cv2.imwrite('test.jpg', frame)

# 釋放所有資源
out.release()
cap.release()   # 釋放攝影機
cv2.destroyAllWindows() # 關閉所有 OpenCV 視窗

print('已存檔 ' + filename)
