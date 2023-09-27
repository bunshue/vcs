'''
圖片內容偵測


#ImageAI：物體偵測

!pip uninstall tensorflow
!pip install tensorflow==2.7
!pip install imageai


!wget -O yolo.h5 https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5
!wget -O resnet50_imagenet_tf.2.0.h5 https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/resnet50_imagenet_tf.2.0.h5

'''

'''
from imageai.Detection import ObjectDetection
detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("yolo.h5")
detector.loadModel()
detections = detector.detectObjectsFromImage(
    input_image="img3.jpg", 
    output_image_path="detect.jpg", 
    minimum_percentage_probability=30)
#print(detections)

for eachObject in detections:
    print("{} ： {} ： {}".format(eachObject["name"], eachObject["percentage_probability"], eachObject["box_points"]))
'''

print('------------------------------------------------------------')	#60個



from imageai.Detection import VideoObjectDetection

detector = VideoObjectDetection()
detector.setModelTypeAsYOLOv3()


#detector.setModelPath("yolo.h5")

'''
detector.loadModel()


detector.detectObjectsFromVideo(
    input_file_path="traffic-mini.mp4",
    output_file_path= "traffic_detected",
    frames_per_second=20, 
    log_progress=True)

'''


print('------------------------------------------------------------')	#60個

'''
from imageai.Prediction import ImagePrediction
prediction = ImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath("resnet50_imagenet_tf.2.0.h5")
prediction.loadModel()
predictions, probabilities = prediction.predictImage("img3.jpg")
# predictions, probabilities = prediction.predictImage("img3.jpg", result_count=10 )
# print(predictions)
# print(probabilities)
for i in range(len(predictions)):
  print('{} ： {}'.format(predictions[i], probabilities[i]))
'''

print('------------------------------------------------------------')	#60個

print('pyocr：簡單易用OCR')

'''
!apt install tesseract-ocr libtesseract-dev tesseract-ocr
!pip install pyocr
'''

'''
import pyocr
from PIL import Image
tools = pyocr.get_available_tools()
# print(tools)
if len(tools) == 0:
    print("沒有可用的OCR！")
else:
  tool = tools[0]
  txt = tool.image_to_string(
      Image.open('text1.jpg'),
      builder=pyocr.builders.TextBuilder()
  )
  print("辨識文字：{}".format(txt))
'''

print('------------------------------------------------------------')	#60個

print('keras-ocr模組：效果強大OCR')
'''
import keras_ocr
import matplotlib.pyplot as plt
pipeline = keras_ocr.pipeline.Pipeline()
images = []
imgfiles = [
    'ad1.jpg',
    # 'ad02.jpg',
]
for imgfile in imgfiles:
    images.append(keras_ocr.tools.read(imgfile))
prediction_groups = pipeline.recognize(images)
# print(prediction_groups)
_, axs = plt.subplots(ncols=len(images), figsize=(10, 10))
for i in range(len(prediction_groups)):
    if len(prediction_groups) == 1:
        keras_ocr.tools.drawAnnotations(image=images[i], predictions=prediction_groups[i], ax=axs)
    else:
        keras_ocr.tools.drawAnnotations(image=images[i], predictions=prediction_groups[i], ax=axs[i])

'''


print('------------------------------------------------------------')	#60個

'''
print('應用：車牌辨識')

import keras_ocr
import re

def checkcharnum(str1):
    if re.match("^[a-z0-9]*$", str1): 
        return True
    else:
        return False

pipeline = keras_ocr.pipeline.Pipeline()
images = []
imgfiles = [
    '1710YC.jpg',
    # '0655VN.jpg',
]
for imgfile in imgfiles:
    images.append(keras_ocr.tools.read(imgfile))
prediction_groups = pipeline.recognize(images)
for n in range(len(prediction_groups)):
    result = ''
    if len(prediction_groups[n]) == 1:
        result = prediction_groups[n][0][0]
    else:
        txt = []
        xpos = []
        for i in range(len(prediction_groups[n])):
          temstr = prediction_groups[n][i][0]
          if checkcharnum(temstr) and len(temstr)<=7:
              txt.append(temstr) 
              xpos.append(prediction_groups[n][i][1][0][0])
        xtem = xpos.copy()
        xtem.sort()
        for i in range(len(xpos)):
            result += txt[xpos.index(xtem[i])]
    result = result.upper()
    print('第 {} 個車牌號碼：{}'.format(n+1, result)) 

'''

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



