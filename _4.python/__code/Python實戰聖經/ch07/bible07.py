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
engine.save('ehappy.p')

from face_engine import load_engine

engine = load_engine('ehappy.p')
testimage = 'catch.jpg'
names, boxes = engine.make_prediction(testimage)
print(names, boxes)

print("------------------------------------------------------------")  # 60個

print("face-recognition：效果絕佳的人臉辨識")

#!pip install face_recognition

import face_recognition

filename = 'C:/_git/vcs/_4.python/opencv/data/Bill_Gates/Bill_Gates21.jpg'

image = face_recognition.load_image_file(filename)
boxes = face_recognition.face_locations(image)
print(boxes)

img = Image.open(filename)
drawing = ImageDraw.Draw(img)
for i in range(len(boxes)):
    drawing.rectangle((boxes[i][3],boxes[i][0],boxes[i][1],boxes[i][2]), outline='red', width=2)
plt.imshow(img)
plt.show()

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_4.python/opencv/data/Bill_Gates/Bill_Gates01.jpg'

image = face_recognition.load_image_file(filename)
landmarks = face_recognition.face_landmarks(image)
print(landmarks)
print('鼻樑位置：{}'.format(landmarks[0]['nose_bridge']))

img = Image.open(filename)
drawing = ImageDraw.Draw(img)
for landmark in landmarks:
    for feature in landmark.keys():
        drawing.line(landmark[feature], width=5)
plt.imshow(img)
plt.show()

print("------------------------------------------------------------")  # 60個

print('把人員圖片資料先存起來, 並註記人名')
file1 = 'C:/_git/vcs/_4.python/opencv/data/Bill_Gates/Bill_Gates01.jpg'
file2 = 'C:/_git/vcs/_4.python/opencv/data/Bill_Gates/Elon_Musk01.jpg'
file3 = 'C:/_git/vcs/_4.python/opencv/data/Bill_Gates/Steve_Jobs_01.jpg'
filename1 = face_recognition.load_image_file(file1)
filename2 = face_recognition.load_image_file(file2)
filename3 = face_recognition.load_image_file(file3)
encoding1 = face_recognition.face_encodings(filename1)[0]
encoding2 = face_recognition.face_encodings(filename2)[0]
encoding3 = face_recognition.face_encodings(filename3)[0]
known_faces = [encoding1, encoding2, encoding3]
names = ['Bill Gates', 'Elon Musk', 'Steve Jobs']

file_new = 'C:/_git/vcs/_4.python/opencv/data/Bill_Gates/Bill_Gates32.jpg'
unknown = face_recognition.load_image_file(file_new)
encoding_unknown = face_recognition.face_encodings(unknown)[0]

print('使用辨識功能')
results = face_recognition.compare_faces(known_faces, encoding_unknown)
print(results)

face = ''
for i in range(len(results)):
    if results[i]: face = face + names[i] + '  '
if face == '':
    print('圖片中辨識不到資料庫中人臉！aaa')
else:
    print('圖片中的人臉：' + face)

print()

print('把人員圖片資料先存起來, 並註記人名')
file1 = 'C:/_git/vcs/_4.python/opencv/data/Bill_Gates/Bill_Gates01.jpg'
file2 = 'C:/_git/vcs/_4.python/opencv/data/Bill_Gates/Elon_Musk01.jpg'
file3 = 'C:/_git/vcs/_4.python/opencv/data/Bill_Gates/Steve_Jobs_01.jpg'
filename1 = face_recognition.load_image_file(file1)
filename2 = face_recognition.load_image_file(file2)
filename3 = face_recognition.load_image_file(file3)
encoding1 = face_recognition.face_encodings(filename1)[0]
encoding2 = face_recognition.face_encodings(filename2)[0]
encoding3 = face_recognition.face_encodings(filename3)[0]
known_faces = [encoding1, encoding2, encoding3]
names = ['Bill Gates', 'Elon Musk', 'Steve Jobs']

file_new = 'C:/_git/vcs/_4.python/opencv/data/Bill_Gates/Bill_Gates32.jpg'
unknown = face_recognition.load_image_file(file_new)
encoding_unknown = face_recognition.face_encodings(unknown)[0]

print('使用距離功能')
distances = face_recognition.face_distance(known_faces, encoding_unknown)
print(distances)

face = ''
for i in range(len(distances)):
    if distances[i] < 0.5:
        face = face + names[i] + '  '

if face == '':
    print('圖片中辨識不到資料庫中人臉！bbb')
else:
    print('圖片中的人臉：' + face)

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
detector = FER()

try:
    emotion, score = detector.top_emotion(img)
    print(emotion, score)
except:
    print('未偵測到人臉！')

#happy
filename = 'C:/_git/vcs/_4.python/opencv/data/Bill_Gates/Elon_Musk03.jpg'
img = cv2.imread(filename)
detector = FER(mtcnn=True)

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

print('Deepface：人臉特徵分析工具')

"""
#!pip install deepface
#人臉偵測
下載(488MB)
https://github.com/swghosh/DeepFace/releases/download/weights-vggface2-2d-aligned/VGGFace2_DeepFace_weights_val-0.9034.h5.zip
放到 C:/Users/070601/.deepface/weights 之下
要解壓縮
"""

from deepface import DeepFace

imgpath = 'person1.jpg'
img_sr = cv2.imread(imgpath)
plt.imshow(cv2.cvtColor(img_sr, cv2.COLOR_BGR2RGB))
image = DeepFace.detectFace(img_path=imgpath, enforce_detection=False)
plt.imshow(image)
image.shape
image *= 255.0
cv2.imwrite( "detectFace.jpg", image[:, :, ::-1])
image = DeepFace.detectFace(img_path=imgpath, detector_backend='retinaface', enforce_detection=False)
#image = DeepFace.detectFace(img_path=imgpath, detector_backend='mtcnn'', enforce_detection=False)
#image = DeepFace.detectFace(img_path=imgpath, detector_backend='dlib'', enforce_detection=False)
#image = DeepFace.detectFace(img_path=imgpath, detector_backend='ssd'', enforce_detection=False)  #有錯誤
#plt.imshow(image)
#plt.show()

print('人臉驗證')

filename1 = 'C:/_git/vcs/_4.python/opencv/data/Bill_Gates/Elon_Musk02.jpg'
filename2 = 'C:/_git/vcs/_4.python/opencv/data/Bill_Gates/Elon_Musk03.jpg'

#result = DeepFace.verify(filename1, filename2, model_name='DeepFace', model=DeepFace.build_model('DeepFace'), enforce_detection=False)
result = DeepFace.verify(filename1, filename2, model_name='DeepFace', enforce_detection=False)

print(result)
if result["verified"]:
    print('兩張圖片是同一人！')
else:
    print('兩張圖片不是同一人！')

print("------------------------------------------------------------")  # 60個

"""
下載 566MB
https://github.com/serengil/deepface_models/releases/download/v1.0/vgg_face_weights.h5
放在
C:/Users/070601/.deepface/weights/vgg_face_weights.h5

下載 90MB
https://github.com/serengil/deepface_models/releases/download/v1.0/facenet_weights.h5
放在
C:/Users/070601/.deepface/weights/facenet_weights.h5

下載 15MB
From: https://github.com/serengil/deepface_models/releases/download/v1.0/openface_weights.h5
放在
C:/Users/070601/.deepface/weights/openface_weights.h5


From: http://dlib.net/files/dlib_face_recognition_resnet_model_v1.dat.bz2
To: C:/Users/070601/.deepface/weights/dlib_face_recognition_resnet_model_v1.dat.bz2

下載 131 MB
From: https://github.com/serengil/deepface_models/releases/download/v1.0/arcface_weights.h5
To: C:/Users/070601/.deepface/weights/arcface_weights.h5

"""

from deepface import DeepFace

filename1 = 'bear1.jpg'
filename2 = 'jeng1.jpg'
models = ["VGG-Face", "Facenet", "OpenFace", "DeepFace", "DeepID", "Dlib", "ArcFace"]
result = []
for model in models: 
    ret= DeepFace.verify(filename1, filename2, model_name = model, enforce_detection=False)
    result.append(ret)
print(result)

print('搜尋人臉')

#尋找單一相同人臉
filename1 = 'bear2.jpg'
df = DeepFace.find(img_path = filename1, db_path = 'member', enforce_detection=False)

print(type(df))
print(len(df))
print()
print()
print(df[0])
print()


"""
print("aaa")
cc = str(df)
cc = cc.split()
print("bbb")
print(cc)
print("ccc")
print(len(cc))
print("ddd")
for _ in cc:
    print(_)

"""


sys.exit()

print(df['VGG-Face_cosine'])
print(type(df['VGG-Face_cosine']))

count = np.sum((df['VGG-Face_cosine']<=0.25)!=0) #計算符合的人臉數量

if count > 0:
  split1 = df['identity'][0].split('/')
  print(split1[-1])
else:
  print('沒有符合的人臉！')
#尋找所有相同人臉
filename1 = 'tem.jpg'
df = DeepFace.find(img_path = filename1, db_path = 'member', enforce_detection=False)
#print(df)
count = np.sum((df['VGG-Face_cosine']<=0.25)!=0) #計算符合的人臉數量
if count > 0:
  for i in range(count):
    split1 = df['identity'][i].split('/')
    print(split1[-1])
else:
  print('沒有符合的人臉！')


sys.exit()

print("------------------------------------------------------------")  # 60個

print('範例：攝影機拍攝登入系統')

from IPython.display import display, Javascript
#from google.colab.output import eval_js
from base64 import b64decode
from IPython.display import Image

def take_photo(filename='person.jpg', quality=0.8):
  js = Javascript("""
    async function takePhoto(quality) {
      const div = document.createElement('div');
      const capture = document.createElement('button');
      capture.textContent = '拍攝';
      div.appendChild(capture);
      const video = document.createElement('video');
      video.style.display = 'block';
      const stream = await navigator.mediaDevices.getUserMedia({video: true});
      document.body.appendChild(div);
      div.appendChild(video);
      video.srcObject = stream;
      await video.play();
      google.colab.output.setIframeHeight(document.documentElement.scrollHeight, true);
      await new Promise((resolve) => capture.onclick = resolve);
      const canvas = document.createElement('canvas');
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      canvas.getContext('2d').drawImage(video, 0, 0);
      stream.getVideoTracks()[0].stop();
      div.remove();
      return canvas.toDataURL('image/jpeg', quality);
    }
    """)
  display(js)
  data = eval_js('takePhoto({})'.format(quality))
  binary = b64decode(data.split(',')[1])
  with open(filename, 'wb') as f:
    f.write(binary)
  return filename

try:
  filename = take_photo()
  display(Image(filename))
except Exception as err:
  print('攝影錯誤：{}'.format(str(err)))

df = DeepFace.find(img_path = 'person.jpg', db_path = 'member', enforce_detection=False)
#print(df)
count = np.sum((df['VGG-Face_cosine']<=0.25)!=0) #計算符合的人臉數量
if count > 0:
  print('歡迎登入系統！')
else:
  print('抱歉！你不是會員！')
  
print('人臉屬性分析')

"""
514MB
From: https://github.com/serengil/deepface_models/releases/download/v1.0/age_model_weights.h5
To: C:/Users/070601/.deepface/weights/age_model_weights.h5
"""

filename1 = 'bear1.jpg'
img = cv2.imread(filename1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
obj = DeepFace.analyze(img_path = filename1, actions = ['age', 'gender', 'race', 'emotion'], enforce_detection=False)
#print(obj)
print('年齡：{}'.format(obj['age']))
print('性別：{}'.format(obj['gender']))
print('種族：{}'.format(obj['dominant_race']))
print('情緒：{}'.format(obj['dominant_emotion']))

print("------------------------------------------------------------")  # 60個

print('範例：攝影機拍攝人臉屬性分析')

from IPython.display import display, Javascript
#from google.colab.output import eval_js
from base64 import b64decode
from IPython.display import Image

def take_photo(filename='person.jpg', quality=0.8):
  js = Javascript("""
    async function takePhoto(quality) {
      const div = document.createElement('div');
      const capture = document.createElement('button');
      capture.textContent = '拍攝';
      div.appendChild(capture);
      const video = document.createElement('video');
      video.style.display = 'block';
      const stream = await navigator.mediaDevices.getUserMedia({video: true});
      document.body.appendChild(div);
      div.appendChild(video);
      video.srcObject = stream;
      await video.play();
      google.colab.output.setIframeHeight(document.documentElement.scrollHeight, true);
      await new Promise((resolve) => capture.onclick = resolve);
      const canvas = document.createElement('canvas');
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      canvas.getContext('2d').drawImage(video, 0, 0);
      stream.getVideoTracks()[0].stop();
      div.remove();
      return canvas.toDataURL('image/jpeg', quality);
    }
    """)
  display(js)
  data = eval_js('takePhoto({})'.format(quality))
  binary = b64decode(data.split(',')[1])
  with open(filename, 'wb') as f:
    f.write(binary)
  return filename

try:
  filename = take_photo()
  display(Image(filename))
except Exception as err:
  print('攝影錯誤：{}'.format(str(err)))

obj = DeepFace.analyze(img_path = 'person.jpg', actions = ['age', 'gender', 'race', 'emotion'], enforce_detection=False)
label = {'angry':'生氣', 'disgust':'厭惡', 'fear':'恐懼', 'happy':'開心', 'neutral':'中性', 'sad':'悲傷', 'surprise':'吃驚',
          'Man':'男', 'Woman':'女',
          'asian':'亞洲', 'black':'黑', 'indian':'印第安', 'latino hispanic':'拉丁美洲', 'middle eastern':'中東', 'white':'白'}
print('\n你是{}歲的{}性{}人，目前情緒似乎是{}'.format(obj['age'], label[obj['gender']], label[obj['dominant_race']], label[obj['dominant_emotion']]))

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

