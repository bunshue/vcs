"""
cv2 物體移動追蹤


"""

import cv2

cap = cv2.VideoCapture('vtest.avi')

tracker = cv2.TrackerCSRT_create()


roi = None
while True:
    ret, frame = cap.read()

    # 指定追蹤物體
    if roi is None:
        roi = (227, 202, 82, 129)
        tracker.init(frame, roi)
    
    """
    # 人為設定追蹤物體
    if roi is None:
        roi = cv2.selectROI('frame', frame)
        if roi != (0, 0, 0, 0):
            tracker.init(frame, roi)
            print(roi)
    """

#### 在while內
    success, rect = tracker.update(frame)
    if success: 
        (x, y, w, h) = [int(i) for i in rect]
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 0, 255), 2) # 紅框

#### 在while內
    cv2.imshow('frame', frame)
    if cv2.waitKey(66) == 27:
        cv2.destroyAllWindows()
        break
