#webcam

'''
目前 webcam 僅 x64 電腦可用
'''

ESC = 27

import cv2
import sys

print('按 ESC 或 Q 離開')
print('按 S 存圖')

cap = cv2.VideoCapture(0)   # 建立攝影機物件

if cap.isOpened() == False:
    print('開啟攝影機失敗')
    sys.exit()
else:
    print('開啟攝影機 OK')

cnt = 0
while True:
    ret, frame = cap.read()   # 從攝影機擷取一張影像

    cv2.imshow('WebCam', frame)    # 顯示圖片

    k = cv2.waitKey(1) # 等待按鍵輸入
    if k == ESC:     #ESC
        break
    elif k == ord('Q') or k == ord('q'):  # 按下 Q(q) 結束迴圈
        break
    elif k == ord('S') or k == ord('s'):  # 按下 S(s), 存圖
        #filename = 'Image_webcam.jpg'
        filename = 'Image_webcam'+str(cnt)+'.jpg'
        cv2.imwrite(filename, frame)
        print('已存圖, 檔案 :', filename)
        cnt += 1

# 釋放所有資源
cap.release()   # 釋放攝影機
cv2.destroyAllWindows() # 關閉所有 OpenCV 視窗


print("------------------------------------------------------------")  # 60個

print("解讀QR code")

filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_qrcode/QR2.png'

image = cv2.imread(filename)

qrcode = cv2.QRCodeDetector()             # 建立 QRCode 偵測器

status, data, bbox, rectified = qrcode.detectAndDecodeMulti(image)  # 辨識 QRCode

if status == True:
    text = data[0]            # QRCode 內容
    print(text)

cv2.imshow('image', image)

print("------------------------------------------------------------")  # 60個

