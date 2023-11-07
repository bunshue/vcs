import cv2

cap = cv2.VideoCapture(0)
if cap.isOpened():
    success, img = cap.read()
    if success:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   # 灰階處理
        img_pre = cv2.GaussianBlur(gray, (13, 13), 15)      # 高斯模糊
while cap.isOpened():
    success, img = cap.read()
    if success:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)        # 灰階處理
        img_now = cv2.GaussianBlur(gray, (13, 13), 15)       # 高斯模糊
        diff = cv2.absdiff(img_now, img_pre)    # 現在影像與前影像相減
        cv2.imshow('frame', diff)              # 顯示相減後的影像
        img_pre = img_now.copy()    # 將現在影像設為前影像
    k = cv2.waitKey(500)
    if k == ord('q'):   # 按 「q」 結束程式
        cv2.destroyAllWindows()
        cap.release()
        break
