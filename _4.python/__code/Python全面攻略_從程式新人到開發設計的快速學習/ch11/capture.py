import cv2

cap = cv2.VideoCapture(0)
cv2.namedWindow('show')

while(True):
    ret,img = cap.read()		#擷取一張影像
    if ret:
        cv2.imshow('show',img)
        key_pressed = cv2.waitKey(1)
        if key_pressed == 27:  #若按Esc鍵
            cv2.imwrite('picture.bmp', img)
            break
    else:
        break

cap.release()           #關閉攝影機
cv2.destroyAllWindows() #關閉視窗


