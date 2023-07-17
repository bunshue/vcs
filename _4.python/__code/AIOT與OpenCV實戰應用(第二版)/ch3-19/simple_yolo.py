import cv2
import numpy as np
import time

def initNet():
    CONFIG = 'yolov4-tiny.cfg'
    WEIGHT = 'yolov4-tiny.weights'
    NAMES = 'coco.names'

    # 讀取物件名稱以及設定外框顏色
    with open(NAMES, 'r') as f:
        names = [line.strip() for line in f.readlines()]
        colors = np.random.uniform(0, 255, size=(len(names), 3))

    # 設定神經網路
    net = cv2.dnn.readNet(CONFIG, WEIGHT)
    model = cv2.dnn_DetectionModel(net)
    model.setInputParams(size=(416, 416), scale=1/255.0)
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
ratio = cap.get(cv2.CAP_PROP_FRAME_WIDTH) / cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
WIDTH = 800
HEIGHT = int(WIDTH / ratio)

while True:
    begin_time = time.time()
    ret, frame = cap.read()
    frame = cv2.resize(frame, (WIDTH, HEIGHT))
    
    classes, confs, boxes = nnProcess(frame, model)
    frame = drawBox(frame, classes, confs, boxes, names, colors)

    fps = 'fps: {:.2f}'.format(1 / (time.time() - begin_time))
    cv2.putText(frame, fps, (10, 30), 
        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 204, 255), 2
    )
    cv2.imshow('video', frame)
    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        break
    

