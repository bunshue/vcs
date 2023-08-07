ESC = 27

import cv2
import time
import numpy as np

def initNet():
    CONFIG = 'yolov4-tiny.cfg'
    WEIGHT = 'yolov4-tiny.weights'
    NAMES = 'coco.names'

    # 讀取物件名稱以及設定外框顏色
    with open(NAMES, 'r') as f:
        names = [line.strip() for line in f.readlines()]
        colors = np.random.uniform(0, 255, size = (len(names), 3))

    # 設定神經網路
    net = cv2.dnn.readNet(CONFIG, WEIGHT)
    model = cv2.dnn_DetectionModel(net)
    model.setInputParams(size = (416, 416), scale = 1 / 255.0)
    # YOLO 要對調顏色
    model.setInputSwapRB(True)

    return model, names, colors
    
def nnProcess(image, model):
    classes, confs, boxes = model.detect(image, 0.6, 0.3)
    return classes, confs, boxes

def drawBox(image, classes, confs, boxes, names, colors):
    new_image = image.copy()
    for (classid, conf, box) in zip(classes, confs, boxes):
        x, y, w , h = box 
        label = '{}: {:.2f}'.format(names[int(classid)], float(conf))
        color = colors[int(classid)]
        cv2.rectangle(new_image, (x, y), (x + w, y + h), color, 2)
        cv2.putText(new_image, label, (x, y - 10), 
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2
        )
    return new_image

model, names, colors = initNet()

cap = cv2.VideoCapture(0)

while True:
    begin_time = time.time()
    ret, frame = cap.read()
    
    classes, confs, boxes = nnProcess(frame, model)
    frame = drawBox(frame, classes, confs, boxes, names, colors)

    fps = 'fps: {:.2f}'.format(1 / (time.time() - begin_time))
    cv2.putText(frame, fps, (10, 30), 
        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 204, 255), 2
    )

### 在 while 內
    cv2.imshow("video", frame)

    k = cv2.waitKey(1)
    if k == ESC:     #ESC
        break

# 釋放所有資源
cap.release()   # 釋放攝影機
cv2.destroyAllWindows() # 關閉所有 OpenCV 視窗

