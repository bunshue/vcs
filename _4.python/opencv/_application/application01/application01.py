"""
#臉部辨識分析


"""

import cv2
import time

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小
'''
print("------------------------------------------------------------")  # 60個

"""
安裝 face-engine
pip install face-engine==2.0.0

將兩個dat檔 "dlib_face_recognition_resnet_model_v1.dat" "shape_predictor_5_face_landmarks.dat"
拷貝到 face_engine 所在地

#sugar
C:/Users/070601/AppData/Local/Programs/Python/Python311/Lib/site-packages/face_engine/resources/data

"""

from face_engine import FaceEngine
from PIL import Image, ImageDraw

print("face_engine：簡單易用的臉部辨識")
print("把人臉框出來")

filename = 'C:/_git/vcs/_4.python/opencv/data/Bill_Gates/Bill_Gates02.jpg'

engine = FaceEngine()

try:
    _, boxes = engine.find_faces(filename)
    print(boxes)

    img = Image.open(filename)
    drawing = ImageDraw.Draw(img)
    for i in range(len(boxes)):
        drawing.rectangle(boxes[i], outline='white', width=2)

    plt.imshow(img)
    plt.show()
except:
    print('未偵測到人臉！')

print("------------------------------------------------------------")  # 60個

print('在圖片中找出某人')

#單人圖片
filename1 = 'C:/_git/vcs/_4.python/opencv/data/Bill_Gates/Bill_Gates01.jpg'

#多人圖片
filename2 = 'C:/_git/vcs/_4.python/opencv/data/Bill_Gates/Bill_Gates21.jpg'

engine = FaceEngine()

score, box = engine.compare_faces(filename1, filename2)
print(score, box)

img = Image.open(filename2)
drawing = ImageDraw.Draw(img)
drawing.rectangle(box, outline='white', width=2)
plt.imshow(img)
plt.show()

print("------------------------------------------------------------")  # 60個

engine = FaceEngine()
filename1 = 'sample1.jpg'
filename2 = 'sample2.jpg'
filename3 = 'sample3.jpg'
engine.fit([filename1, filename2, filename3], ['jeng', 'chiou', 'david'])

testimage = 'catch.jpg'
# testimage = 'person2.jpg'
names, boxes = engine.make_prediction(testimage)
print(names, boxes)
img = Image.open(testimage)
drawing = ImageDraw.Draw(img)
for i in range(len(boxes)):
    drawing.rectangle(boxes[i], outline='white', width=2)
plt.imshow(img)
plt.show()

engine = FaceEngine()
filename1 = 'sample1.jpg'
filename2 = 'sample2.jpg'
filename3 = 'sample3.jpg'
engine.fit([filename1, filename2, filename3], ['jeng', 'chiou', 'david'])
engine.save('tmp_ehappy.p')

from face_engine import load_engine

engine = load_engine('tmp_ehappy.p')
testimage = 'catch.jpg'
names, boxes = engine.make_prediction(testimage)
print(names, boxes)
'''
print("------------------------------------------------------------")  # 60個

print('fer：偵測臉部表情')
#!pip install fer

from fer import FER

#angry
filename = 'C:/_git/vcs/_4.python/opencv/data/Bill_Gates/Elon_Musk05.jpg'
img = cv2.imread(filename)
detector = FER()
emotion = detector.detect_emotions(img)
print(emotion)

img = cv2.imread(filename)
detector = FER()#使用OpenCV之Haar方法偵測人臉

print('圖片 :', filename)
try:
    emotion, score = detector.top_emotion(img)
    print(emotion, score)
except:
    print('未偵測到人臉！')

plt.imshow(img)
plt.show()

print("------------------------------")  # 30個

#happy
filename = 'C:/_git/vcs/_4.python/opencv/data/Bill_Gates/Elon_Musk03.jpg'
img = cv2.imread(filename)
detector = FER(mtcnn=True)#使用MTCNN神經網路偵測人臉

print('圖片 :', filename)
try:
    emotion, score = detector.top_emotion(img)
    print(emotion, score)
except:
    print('未偵測到人臉！')

print("------------------------------------------------------------")  # 60個

print('facemask_detection：偵測是否戴口罩')

"""
#!pip install facemask_detection

下載
https://github.com/ternaus/facemask_detection/releases/download/0.0.1/tf_efficientnet_b0_ns_2020-07-29-ffdde352.zip
放到 C:/Users/070601/.cache/torch/hub/checkpoints/ 之下

"""

from facemask_detection.pre_trained_models import get_model as get_classifier
import albumentations as A
import torch

filename = 'C:/_git/vcs/_4.python/opencv/data/Bill_Gates/Bill_Gates19.jpg'

model = get_classifier("tf_efficientnet_b0_ns_2020-07-29")
model.eval()
image1 = cv2.cvtColor(cv2.imread(filename), cv2.COLOR_BGR2RGB)
# image1 = cv2.cvtColor(cv2.imread("person1.jpg"), cv2.COLOR_BGR2RGB)
transform = A.Compose([A.SmallestMaxSize(max_size=256, p=1), 
                       A.CenterCrop(height=224, width=224, p=1),
                       A.Normalize(p=1)])
trans_image = transform(image=image1)['image']
input = torch.from_numpy(np.transpose(trans_image, (2, 0, 1))).unsqueeze(0)

prob = model(input)[0].item()
if prob > 0.9:
    print('有戴口罩')
elif prob < 0.1:
    print('沒有戴口罩')
else:
    print('無法分辨')

print("------------------------------------------------------------")  # 60個

# """ 安裝模組失敗
print('facemask_detection：標示人物是否戴口罩')

"""
# !pip install facemask_detection
# !pip install retinaface_pytorch

下載(97MB)
https://github.com/ternaus/retinaface/releases/download/0.01/retinaface_resnet50_2020-07-20-f168fae3c.zip
放到 C:/Users/070601/.cache/torch/hub/checkpoints/之下
"""

from retinaface.pre_trained_models import get_model as get_detector
from facemask_detection.pre_trained_models import get_model as get_classifier
import albumentations as A
import torch
from matplotlib import pyplot as plt

face_detector = get_detector("resnet50_2020-07-20", max_size=800)
face_detector.eval()
image1 = cv2.cvtColor(cv2.imread("mask3.jpg"), cv2.COLOR_BGR2RGB)
plt.rcParams["figure.figsize"] = (10, 10)
plt.imshow(image1)
with torch.no_grad():
    annotations = face_detector.predict_jsons(image1)
print(annotations)
mask_classifier = get_classifier("tf_efficientnet_b0_ns_2020-07-29")
mask_classifier.eval()
transform = A.Compose([A.SmallestMaxSize(max_size=256, p=1),
                       A.CenterCrop(height=224, width=224, p=1),
                       A.Normalize(p=1)])
predictions = []
with torch.no_grad():
  for annotation in annotations:
    x_min, y_min, x_max, y_max = annotation['bbox']
    x_min = np.clip(x_min, 0, x_max)
    y_min = np.clip(y_min, 0, y_max)
    crop = image1[y_min:y_max, x_min:x_max]
    crop_transformed = transform(image=crop)['image']
    model_input = torch.from_numpy(np.transpose(crop_transformed, (2, 0, 1)))  
    predictions += [mask_classifier(model_input.unsqueeze(0))[0].item()] 
vis_image = image1.copy()
for prediction_id, annotation in enumerate(annotations):
    is_mask = predictions[prediction_id] > 0.5
    if is_mask:
      color = (255, 0, 0)    
      text = "mask"
    else:
      color = (0, 255, 0)
      text = "no mask"
    x_min, y_min, x_max, y_max = annotation["bbox"]
    x_min = np.clip(x_min, 0, x_max - 1)
    y_min = np.clip(y_min, 0, y_max - 1)
    vis_image = cv2.rectangle(vis_image, (x_min, y_min), (x_max, y_max), color=color, thickness=2)
    vis_image = cv2.putText(vis_image, text, (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX,  0.4, color, 2, cv2.LINE_AA) 
plt.imshow(vis_image)

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

