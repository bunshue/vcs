import cv2

x_st = 150
y_st = 150
x_sp = x_st + 200
y_sp = y_st + 100

RECT = ((x_st, y_st), (x_sp, y_sp))
(left, top), (right, bottom) = RECT

def roiarea(frame):
    return frame[top:bottom, left:right]
    
def replaceroi(frame, roi):
    frame[top:bottom, left:right] = roi
    return frame

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

#### 在while內
    # 取出子畫面
    roi = roiarea(frame)
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    # 將處理完的子畫面貼回到原本畫面中
    frame = replaceroi(frame, roi)

#### 在while內
    # 在 ROI 範圍處畫個框
    cv2.rectangle(frame, RECT[0], RECT[1], (0,0,255), 2)
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) == 27: 
        cv2.destroyAllWindows()
        break
