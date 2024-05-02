#ch16-1-2.py

from tflite_runtime.interpreter import Interpreter 
import cv2
import numpy as np

model_path = "models/model.tflite"
label_path = "models/labels.txt"
label_names = []
with open(label_path, "r") as f:
    for line in f.readlines():
        class_name = line.split(" ")
        label_names.append(class_name[1].strip())
interpreter = Interpreter(model_path)
print("成功載入模型...")
interpreter.allocate_tensors()
_, height, width, _ = interpreter.get_input_details()[0]["shape"]
print("影像尺寸: (", width, ",", height, ")")
image = cv2.imread("images/Paper.png")
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
final_prob = np.round(prob*100, 2)
print("影像可能性 =", final_prob, "%")
cv2.putText(image, classification_label, (25, 50),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
out_msg = str(final_prob) + "%"
cv2.putText(image, out_msg, (25, 100),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

#ch16-1-2a.py

from tflite_runtime.interpreter import Interpreter 
import cv2
import numpy as np

model_path = "models/model.tflite"
label_path = "models/labels.txt"
label_names = []
with open(label_path, "r") as f:
    for line in f.readlines():
        class_name = line.split(" ")
        label_names.append(class_name[1].strip())
interpreter = Interpreter(model_path)
print("成功載入模型...")
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
_, height, width, _ = input_details[0]["shape"]
print("影像尺寸: (", width, ",", height, ")")
cap = cv2.VideoCapture(0)
while cap.isOpened():
    success, frame = cap.read()
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_resized = cv2.resize(frame_rgb, (width, height))
    input_data = np.expand_dims(frame_resized, axis=0)
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
    final_prob = np.round(prob*100, 2)
    print("影像可能性 =", final_prob, "%")
    cv2.putText(frame, classification_label, (25, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    out_msg = str(final_prob) + "%"
    cv2.putText(frame, out_msg, (25, 100),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

#ch16-2-1.py

import cv2
import numpy as np
from imutils.object_detection import non_max_suppression
import pytesseract
 
pytesseract.pytesseract.tesseract_cmd="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
img = cv2.imread("images/car.jpg")
model = cv2.dnn.readNet("models/frozen_east_text_detection.pb")
outputLayers = []
outputLayers.append("feature_fusion/Conv_7/Sigmoid")
outputLayers.append("feature_fusion/concat_3")
height,width,colorch = img.shape
new_height = (height//32+1)*32
new_width = (width//32+1)*32
h_ratio = height/new_height
w_ratio = width/new_width
blob=cv2.dnn.blobFromImage(img, 1, (new_width,new_height),
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
    w = abs(x2-x1)
    h = abs(y2-y1)
    area = w * h
    if area > 4000:
        x1 = int(x1*w_ratio)
        y1 = int(y1*h_ratio)
        x2 = int(x2*w_ratio)
        y2 = int(y2*h_ratio)
        print("偵測和辨識出車牌文字!")
        result = img[y1-10:y1+h+13,x1-10:x1+w+1]        
        cv2.imshow("Plate", result)
        text = pytesseract.image_to_string(result, lang="eng")
        print(text.strip())
        cv2.waitKey(0)

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

#ch16-2-1a.py

import cv2
import numpy as np
from imutils.object_detection import non_max_suppression
import pytesseract
 
pytesseract.pytesseract.tesseract_cmd="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
img = cv2.imread("images/car1.jpg")
model = cv2.dnn.readNet("models/frozen_east_text_detection.pb")
outputLayers = []
outputLayers.append("feature_fusion/Conv_7/Sigmoid")
outputLayers.append("feature_fusion/concat_3")
height,width,colorch = img.shape
new_height = (height//32+1)*32
new_width = (width//32+1)*32
h_ratio = height/new_height
w_ratio = width/new_width
blob = cv2.dnn.blobFromImage(img, 1, (new_width,new_height),
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
    w = abs(x2-x1)
    h = abs(y2-y1)
    area = w * h
    if area > 4000:
        x1 = int(x1*w_ratio)
        y1 = int(y1*h_ratio)
        x2 = int(x2*w_ratio)
        y2 = int(y2*h_ratio)
        print("偵測和辨識出車牌文字!")
        result = img[y1-5:y1+h+5,x1-1:x1+w+1]        
        cv2.imshow("Plate", result)        
        text = pytesseract.image_to_string(result, lang="eng")
        print(text.strip())
        cv2.waitKey(0)

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

#ch16-2-2.py

import easyocr
import cv2

reader = easyocr.Reader(["en"]) 
result = reader.readtext("images/number.jpg")
print(result)
reader = easyocr.Reader(["ch_sim", "en"])
img = cv2.imread("images/simple.jpg")
result = reader.readtext(img)
print(result)
reader = easyocr.Reader(["ch_tra", "en"])
with open("images/traditional.jpg", "rb") as f:
    img = f.read()
result = reader.readtext(img)
print(result)

print("------------------------------------------------------------")  # 60個

#ch16-2-2a.py

import easyocr
import numpy as np
import cv2
 
img = cv2.imread("images/sample.jpg")
reader = easyocr.Reader(["ch_tra", "en"]) 
horizontal_list, free_list = reader.detect(img)
for box in horizontal_list[0]:
    print(box)
    cv2.rectangle(img, (box[0], box[2]), (box[1], box[3]),
                  (0, 0, 255), 3)
cv2.imshow("Detection", img) 
cv2.waitKey(0)
cv2.destroyAllWindows()




print("------------------------------------------------------------")  # 60個

#ch16-2-2b.py

import easyocr
import numpy as np
import cv2
 
img = cv2.imread("images/sample.jpg")
reader = easyocr.Reader(["ch_tra", "en"]) 
results = reader.readtext("images/sample.jpg")
for result in results:
    box = result[0]
    cv2.rectangle(img, box[0], box[2], (0, 0, 255), 3)
cv2.imshow("Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()




print("------------------------------------------------------------")  # 60個

#ch16-2-2c.py

import easyocr
import numpy as np
import cv2

boxes = [[32, 159, 8, 47],  # horizontal_list[0]
         [6, 191, 43, 81],
         [30, 178, 86, 118]]

img = cv2.imread("images/sample.jpg")
reader = easyocr.Reader(["ch_tra", "en"]) 
results = reader.recognize(img, horizontal_list=boxes,
                           free_list=[])
for result in results:
    print(result[0])
    print(result[1])
    print(result[2])





print("------------------------------------------------------------")  # 60個

#ch16-2-3.py

import easyocr
import numpy as np
import cv2
 
img = cv2.imread("images/car1.jpg")
reader = easyocr.Reader(["en"])
result = reader.readtext(img)
y = 0
for box in result:
    points = box[0]
    points = np.array(points, np.int32)
    print(points)
    print(box[1])
    cv2.polylines(img, pts=[points], isClosed=True,
                  color=(0, 0, 255), thickness=3)
    y = y + 30
    cv2.putText(img, box[1], (10, y),
                cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    
cv2.imshow("Car", img) 
cv2.waitKey(0)
cv2.destroyAllWindows()




print("------------------------------------------------------------")  # 60個



