"""
# DeepFace


"""

import cv2
import time

from deepface import DeepFace

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

print('Deepface：人臉特徵分析工具')

"""
#!pip install deepface
#人臉偵測
下載(488MB)
https://github.com/swghosh/DeepFace/releases/download/weights-vggface2-2d-aligned/VGGFace2_DeepFace_weights_val-0.9034.h5.zip
放到 C:/Users/070601/.deepface/weights 之下
要解壓縮
"""

imgpath = 'person1.jpg'
img_sr = cv2.imread(imgpath)
plt.imshow(cv2.cvtColor(img_sr, cv2.COLOR_BGR2RGB))

image = DeepFace.detectFace(img_path=imgpath, enforce_detection=False)
plt.imshow(image)

image.shape
image *= 255.0
cv2.imwrite( "tmp_detectFace.jpg", image[:, :, ::-1])
image = DeepFace.detectFace(img_path=imgpath, detector_backend='retinaface', enforce_detection=False)
#image = DeepFace.detectFace(img_path=imgpath, detector_backend='mtcnn'', enforce_detection=False)
#image = DeepFace.detectFace(img_path=imgpath, detector_backend='dlib'', enforce_detection=False)
#image = DeepFace.detectFace(img_path=imgpath, detector_backend='ssd'', enforce_detection=False)  #有錯誤
#plt.imshow(image)
#plt.show()

print("------------------------------------------------------------")  # 60個

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


""" 這一種特殊串列還不會分析出來
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


""" TBD
print(df['VGG-Face_cosine'])
print(type(df['VGG-Face_cosine']))

count = np.sum((df['VGG-Face_cosine']<=0.25)!=0) #計算符合的人臉數量

if count > 0:
  split1 = df['identity'][0].split('/')
  print(split1[-1])
else:
  print('沒有符合的人臉！')

#尋找所有相同人臉
filename1 = 'find_person.jpg'
df = DeepFace.find(img_path = filename1, db_path = 'member', enforce_detection=False)
#print(df)
count = np.sum((df['VGG-Face_cosine']<=0.25)!=0) #計算符合的人臉數量
if count > 0:
  for i in range(count):
    split1 = df['identity'][i].split('/')
    print(split1[-1])
else:
  print('沒有符合的人臉！')
"""

print("------------------------------------------------------------")  # 60個

''' TBD
print('範例：攝影機拍攝登入系統')

from IPython.display import display, Javascript
#from google.colab.output import eval_js
from base64 import b64decode
#from IPython.display import Image

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
'''

print("------------------------------------------------------------")  # 60個
"""
514MB
From: https://github.com/serengil/deepface_models/releases/download/v1.0/age_model_weights.h5
To: C:/Users/070601/.deepface/weights/age_model_weights.h5
"""

filename = 'C:/_git/vcs/_4.python/opencv/data/Bill_Gates/Bill_Gates02.jpg'

img = cv2.imread(filename)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

obj = DeepFace.analyze(img_path = filename, actions = ['age', 'gender', 'race', 'emotion'], enforce_detection=False)

print(obj)
print(type(obj))
print(len(obj))

""" 這一種特殊串列還不會分析出來
print('年齡：{}'.format(obj['age']))
print('性別：{}'.format(obj['gender']))
print('種族：{}'.format(obj['dominant_race']))
print('情緒：{}'.format(obj['dominant_emotion']))
"""

print("------------------------------------------------------------")  # 60個

'''TBD
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

'''

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

