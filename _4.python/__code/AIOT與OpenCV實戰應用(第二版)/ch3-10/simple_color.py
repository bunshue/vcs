import cv2 
import numpy as np
import time

color = ((16, 59, 0), (47, 255, 255))
lower = np.array(color[0], dtype="uint8")
upper = np.array(color[1], dtype="uint8")

cap = cv2.VideoCapture(0)
ratio = cap.get(cv2.CAP_PROP_FRAME_WIDTH) / \
        cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
WIDTH = 400
HEIGHT = int(WIDTH / ratio)
while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (WIDTH, HEIGHT))
    frame = cv2.flip(frame, 1)

#### 在while中
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv = cv2.GaussianBlur(hsv, (11, 11), 0)

#### 在while中
    mask = cv2.inRange(hsv, lower, upper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

#### 在while中
    contours, hierarchy = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:
        cnt = max(contours, key=cv2.contourArea)
        if cv2.contourArea(cnt) < 100:
            continue
        x, y, w, h = cv2.boundingRect(cnt)
        p1 = (x - 2, y - 2)
        p2 = (x + w + 4, y + h + 4)

        out = cv2.bitwise_and(hsv, hsv, mask=mask)
        cv2.rectangle(frame, p1, p2, (0,255,255), 2)

        cv2.rectangle(hsv, p1, p2, (0,255,255), 2)
        cv2.rectangle(out, p1, p2, (0,255,255), 2)
        frame = cv2.hconcat([frame, hsv, out])

#### 在while中
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows() 
        break


