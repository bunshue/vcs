ESC = 27

import cv2
import time

net = cv2.dnn.readNet(
    'opencv_face_detector.pbtxt',
    'opencv_face_detector_uint8.pb'
)

#net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
#net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
#net.setPreferableBackend(cv2.dnn.DNN_BACKEND_INFERENCE_ENGINE)
#net.setPreferableTarget(cv2.dnn.DNN_TARGET_MYRIAD)
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(300, 300), scale=1.0)

cap = cv2.VideoCapture(0)

# 取得影像的尺寸大小
w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("Image Size: %d x %d" % (w, h))

if not cap.isOpened():
    print('Could not open video device')
    sys.exit()
else:
    print('Video device opened')

ratio = cap.get(cv2.CAP_PROP_FRAME_WIDTH) / cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

WIDTH = 600
HEIGHT = int(WIDTH / ratio)
FONT = cv2.FONT_HERSHEY_SIMPLEX

while True:
    begin_time = time.time()
    ret, frame = cap.read()
    frame = cv2.resize(frame, (WIDTH, HEIGHT))
    frame = cv2.flip(frame, 1)

### 在 while 內
    classes, confs, boxes = model.detect(frame, 0.5)
    for (classid, conf, box) in zip(classes, confs, boxes):
        x, y, w , h = box 
        text = '%2f' % conf

        if y - 20 < 0:
            y1 = y + 20
        else:
            y1 = y - 10

        fps = 1 / (time.time() - begin_time)
        text = "fps: {:.1f} {:.2f}%".format(fps, float(conf) * 100)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0,255,255), 2)
        cv2.putText(frame, text, (x, y - 10), FONT, 0.5, (0,204,255), 2)

### 在 while 內
    cv2.imshow("video", frame)

    k = cv2.waitKey(1)
    if k == ESC:     #ESC
        break

# 釋放所有資源
cap.release()   # 釋放攝影機
cv2.destroyAllWindows() # 關閉所有 OpenCV 視窗


