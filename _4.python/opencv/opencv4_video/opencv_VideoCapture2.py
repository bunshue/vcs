import cv2

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

        cv2.imshow('frame', img)
        img_pre = img_now.copy()
    k = cv2.waitKey(50)
    if k == ord('q'):
        cv2.destroyAllWindows()
        cap.release()
        break
