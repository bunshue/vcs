import cv2

# 開啟影片檔案
filename = 'vtest.avi'

cap = cv2.VideoCapture(filename)

bg = None

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (17, 17), 0)

    if bg is None:
        bg = gray
        continue

#### 在while內
    diff = cv2.absdiff(gray, bg)
    diff = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)[1]
    diff = cv2.erode(diff, None, iterations = 2)
    diff = cv2.dilate(diff, None, iterations = 2)

#### 在while內
    cnts, hierarchy = cv2.findContours(
        diff, 
        cv2.RETR_EXTERNAL, 
        cv2.CHAIN_APPROX_SIMPLE)
    
    for c in cnts:
        if cv2.contourArea(c) < 500:
            continue
            
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

#### 在while內        
    cv2.imshow("frame", frame)
    if cv2.waitKey(100) == 27:
        cv2.destroyAllWindows()
        break

