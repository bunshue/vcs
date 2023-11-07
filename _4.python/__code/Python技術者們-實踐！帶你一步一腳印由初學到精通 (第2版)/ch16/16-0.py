import cv2

# 建立臉部辨識物件
face_detector = cv2.CascadeClassifier(
    'haarcascade_frontalface_default.xml')
capture = cv2.VideoCapture(0)                   # 開啟標號 0 的攝影機
while capture.isOpened():
    sucess, img = capture.read()            # 讀取攝影機影像
    if sucess:
        faces = face_detector.detectMultiScale(img,
                                               scaleFactor=1.1,
                                               minNeighbors=5,
                                               minSize=(200, 200))    # 從攝影機影像中偵測人臉
        for (x, y, w, h) in faces:          # 畫出人臉位置
            cv2.rectangle(img, (x, y), (x+w, y+h),
                          (0, 255, 255), 2)    # 繪製黃色線寬為 2 的矩形
        cv2.imshow('Frame', img)
    k = cv2.waitKey(1)          # 讀取按鍵輸入 (若無會傳回 -1)
    if k == ord('q') or k == ord('Q'):     # 若按下 q 結束迴圈
        print('exit')
        cv2.destroyAllWindows()
        capture.release()
        break
else:
    print('開啟攝影機失敗')
