
#ch15-2-1.py

import cv2
import numpy as np

model_path = "models/DenseNet_121.caffemodel"
config_path = "models/DenseNet_121.prototxt.txt"
class_path = "models/classification_classes_ILSVRC2012.txt"
class_names = []
with open(class_path, "r") as f:
    for line in f.readlines():
        class_names.append(line.split(",")[0].strip())
model = cv2.dnn.readNet(model=model_path, config=config_path,
                        framework="Caffe")
img = cv2.imread("images/dog.jpg")
blob = cv2.dnn.blobFromImage(image=img, scalefactor=0.01,
                             size=(224, 224), mean=(104, 117, 123))
model.setInput(blob)
outputs = model.forward()
final_outputs = outputs[0].reshape(1000, 1)
def softmax(x):
    return np.exp(x)/np.sum(np.exp(x))
probs = softmax(final_outputs)
final_prob = np.round(np.max(probs)*100, 2)
label_id = np.argmax(probs)
out_name = class_names[label_id]
cv2.putText(img, out_name, (25, 50),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
out_msg = str(final_prob) + "%"
cv2.putText(img, out_msg, (25, 100),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

#ch15-2-2.py

from tflite_runtime.interpreter import Interpreter 
import cv2
import numpy as np

model_path = "models/mobilenet_v1_1.0_224_quantized_1_metadata_1.tflite"
label_path = "models/labels.txt"
label_names = []
with open(label_path, "r") as f:
    for line in f.readlines():
        label_names.append(line.strip())
interpreter = Interpreter(model_path)
print("成功載入模型...")
interpreter.allocate_tensors()
_, height, width, _ = interpreter.get_input_details()[0]["shape"]
print("影像尺寸: (", width, ",", height, ")")
image = cv2.imread("images/dog.jpg")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_resized = cv2.resize(image_rgb, (width, height))
input_data = np.expand_dims(image_resized, axis=0)
interpreter.set_tensor(
    interpreter.get_input_details()[0]["index"],input_data)
interpreter.invoke()
output_details = interpreter.get_output_details()[0]
output = np.squeeze(interpreter.get_tensor(output_details["index"]))
label_id = np.argmax(output)
scale, zero_point = output_details["quantization"]
prob = scale * (output[label_id] - zero_point)
classification_label = label_names[label_id]
print("分類名稱 =", classification_label)
print("影像可能性 =", np.round(prob*100, 2), "%")

print("------------------------------------------------------------")  # 60個

#ch15-3-1.py

import numpy as np
import cv2

model_path = "models/MobileNetSSD_deploy.caffemodel"
config_path = "models/MobileNetSSD_deploy.prototxt.txt"
class_path = "models/MobileNetSSD_labels.txt"
class_names = []
with open(class_path, "r") as f:
    class_names = f.read().split("\n")
net = cv2.dnn.readNet(config_path, model_path)    
img = cv2.imread("images/people.jpg")
h, w = img.shape[:2]
blob = cv2.dnn.blobFromImage(img, 0.007843, (300, 300), 127.5)
net.setInput(blob)
detections = net.forward()
print(detections.shape)
detections = np.squeeze(detections)
print(len(detections))  # 偵測到幾個
for i in range(0, detections.shape[0]):
   confidence = detections[i, 2]
   if confidence > 0.5:
       idx = int(detections[i, 1])
       box = detections[i, 3:7] * np.array([w, h, w, h])
       (startX, startY, endX, endY) = box.astype("int")
       cv2.rectangle(img, (startX, startY), (endX, endY),
                     (10, 255, 0), 2)       
       prob = np.round(confidence*100, 2)
       label = class_names[idx] + ": " + str(prob) + "%"
       y = startY - 15 if startY - 15 > 15 else startY + 15
       cv2.putText(img, label, (startX, y),
                   cv2.FONT_HERSHEY_SIMPLEX,
                   0.5, (10, 255, 0), 2)
       print(label) 

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

#ch15-3-1a.py

import numpy as np
import cv2

model_path = "models/MobileNetSSD_deploy.caffemodel"
config_path = "models/MobileNetSSD_deploy.prototxt.txt"
class_path = "models/MobileNetSSD_labels.txt"
class_names = []
with open(class_path, "r") as f:
    class_names = f.read().split("\n")
net = cv2.dnn.readNet(config_path, model_path)     
cap = cv2.VideoCapture("media/motor_bike.mp4")
while True:
    ret, frame = cap.read()
    if not ret:
       break
    h, w = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frame, 0.007843, (300, 300), 127.5)
    net.setInput(blob)
    detections = net.forward()
    detections = np.squeeze(detections)
    for i in range(detections.shape[0]):
       confidence = detections[i, 2]
       if confidence > 0.5:
           idx = int(detections[i, 1])
           box = detections[i, 3:7] * np.array([w, h, w, h])
           (startX, startY, endX, endY) = box.astype("int")
           cv2.rectangle(frame, (startX, startY), (endX, endY),
                         (10, 255, 0), 2)           
           prob = np.round(confidence*100, 2)
           label = class_names[idx] + ": " + str(prob) + "%" 
           y = startY - 15 if startY - 15 > 15 else startY + 15
           cv2.putText(frame, label, (startX, y),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                       (10, 255, 0), 2)
           print(label)
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows() 

print("------------------------------------------------------------")  # 60個

#ch15-3-2.py

from tflite_runtime.interpreter import Interpreter
import cv2
import numpy as np

model_path = "models/lite-model_ssd_mobilenet_v1_1_metadata_2.tflite"
label_path = "models/labelmap.txt"
label_names = []
with open(label_path, "r") as f:
    for line in f.readlines():
        label_names.append(line.strip())
interpreter = Interpreter(model_path=model_path)
print("成功載入模型...")
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
_, height, width, _ = input_details[0]["shape"]
print("圖片資訊: (", width, ",", height, ")")
img = cv2.imread("images/people.jpg")
imgHeight, imgWidth, _ = img.shape
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_resized = cv2.resize(img_rgb, (width, height))
input_data = np.expand_dims(img_resized, axis=0)
interpreter.set_tensor(input_details[0]["index"],input_data)
interpreter.invoke()
boxes = interpreter.get_tensor(output_details[0]["index"])[0]
classes = interpreter.get_tensor(output_details[1]["index"])[0]
scores = interpreter.get_tensor(output_details[2]["index"])[0] 
for i in range(len(scores)):
    if ((scores[i] > 0.5) and (scores[i] <= 1.0)):
         startY = int(max(1,(boxes[i][0] * imgHeight)))
         startX = int(max(1,(boxes[i][1] * imgWidth)))
         endY = int(min(imgHeight,(boxes[i][2] * imgHeight)))
         endX = int(min(imgWidth,(boxes[i][3] * imgWidth)))              
         cv2.rectangle(img, (startX, startY), (endX, endY),
                       (10, 255, 0), 2)  
         object_name = label_names[int(classes[i])]
         prob = np.round(scores[i]*100, 2)
         label = object_name + ": " + str(prob) + "%"
         y = startY - 15 if startY - 15 > 15 else startY + 15
         cv2.putText(img, label, (startX, y),
                     cv2.FONT_HERSHEY_SIMPLEX,
                     0.5, (10, 255, 0), 2)
         
cv2.imshow("Object Detector", img)
cv2.waitKey(0)
cv2.destroyAllWindows()         
         
         
         

print("------------------------------------------------------------")  # 60個

#ch15-3-2a.py

from tflite_runtime.interpreter import Interpreter
import cv2
import numpy as np

model_path = "models/lite-model_ssd_mobilenet_v1_1_metadata_2.tflite"
label_path = "models/labelmap.txt"
label_names = []
with open(label_path, "r") as f:
    for line in f.readlines():
        label_names.append(line.strip())
interpreter = Interpreter(model_path=model_path)
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
_, height, width, _ = input_details[0]["shape"]
cap = cv2.VideoCapture("media/motor_bike.mp4")
imWidth  = cap.get(cv2.CAP_PROP_FRAME_WIDTH) 
imHeight = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
while cap.isOpened():
    success, frame = cap.read()
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_resized = cv2.resize(frame_rgb, (width, height))
    input_data = np.expand_dims(frame_resized, axis=0)
    interpreter.set_tensor(input_details[0]["index"],input_data)
    interpreter.invoke()
    boxes = interpreter.get_tensor(output_details[0]["index"])[0]
    classes = interpreter.get_tensor(output_details[1]["index"])[0]
    scores = interpreter.get_tensor(output_details[2]["index"])[0] 
    for i in range(len(scores)):
        if ((scores[i] > 0.5) and (scores[i] <= 1.0)):
         startY = int(max(1,(boxes[i][0] * imHeight)))
         startX = int(max(1,(boxes[i][1] * imWidth)))
         endY = int(min(imHeight,(boxes[i][2] * imHeight)))
         endX = int(min(imWidth,(boxes[i][3] * imWidth)))              
         cv2.rectangle(frame, (startX, startY), (endX, endY),
                       (10, 255, 0), 2)  
         object_name = label_names[int(classes[i])]
         prob = np.round(scores[i]*100, 2)
         label = object_name + ": " + str(prob) + "%"
         y = startY - 15 if startY - 15 > 15 else startY + 15
         cv2.putText(frame, label, (startX, y),
                     cv2.FONT_HERSHEY_SIMPLEX,
                     0.5, (10, 255, 0), 2)
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

#ch15-4.py

import cv2
import numpy as np
from imutils.object_detection import non_max_suppression

model_path = "models/frozen_east_text_detection.pb"
img = cv2.imread("images/car.jpg")
model = cv2.dnn.readNet(model_path)
outputLayers = []
outputLayers.append("feature_fusion/Conv_7/Sigmoid")
outputLayers.append("feature_fusion/concat_3")
height,width,colorch = img.shape
new_height = (height//32+1)*32
new_width = (width//32+1)*32
h_ratio = height/new_height
w_ratio = width/new_width
blob = cv2.dnn.blobFromImage(img ,1 ,(new_width, new_height),
                            (123.68,116.78,103.94), True)
model.setInput(blob)
(scores, geometry) = model.forward(outputLayers)
rectangles=[]
confidence_score=[]
rows = geometry.shape[2]
cols = geometry.shape[3]
for y in range(0, rows):
    for x in range(0, cols):
        if scores[0][0][y][x] < 0.5:
            continue
        offset_x = x*4
        offset_y = y*4
        bottom_x = int(offset_x + geometry[0][1][y][x])
        bottom_y = int(offset_y + geometry[0][2][y][x])
        top_x = int(offset_x - geometry[0][3][y][x])
        top_y = int(offset_y - geometry[0][0][y][x])
        rectangles.append((top_x, top_y, bottom_x, bottom_y))
        confidence_score.append(float(scores[0][0][y][x]))        
final_boxes = non_max_suppression(np.array(rectangles),
                                  probs=confidence_score,
                                  overlapThresh=0.5)
for (x1,y1,x2,y2) in final_boxes:
    area = abs(x2-x1) * abs(y2-y1)
    if area > 4000:
        x1 = int(x1*w_ratio)
        y1 = int(y1*h_ratio)
        x2 = int(x2*w_ratio)
        y2 = int(y2*h_ratio)
        cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), 2)    
cv2.imshow("EAST", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

#ch15-5-2.py

import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
img = cv2.imread("images/number.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
text = pytesseract.image_to_string(img, lang="eng")
print(text.strip())
img = cv2.imread("images/traditional.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
text = pytesseract.image_to_string(img, lang="chi_tra")
print(text.strip())
img = cv2.imread("images/simple.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
text = pytesseract.image_to_string(img, lang="chi_sim")
print(text.strip())

print("------------------------------------------------------------")  # 60個

#ch15-5-2a.py

import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
img = cv2.imread("images/traditional2.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
text = pytesseract.image_to_string(img, lang="chi_tra_vert")
print(text.strip())


print("------------------------------------------------------------")  # 60個

#ch15-5-2b.py

import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
img = cv2.imread("images/number.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_w = img.shape[1]
img_h = img.shape[0]
boxes = pytesseract.image_to_boxes(img)
print(boxes)
for box in boxes.splitlines():
    box = box.split(" ")
    character = box[0]
    x = int(box[1])
    y = int(box[2])
    x2 = int(box[3])
    y2 = int(box[4])
    cv2.rectangle(img, (x, img_h - y),
                  (x2, img_h - y2), (0, 255, 0), 1)
    cv2.putText(img, character, (x, img_h - y2 - 10),
                cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個


