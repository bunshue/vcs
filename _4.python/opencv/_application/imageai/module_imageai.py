"""
module_imageai

ImageAI：物體偵測

!pip uninstall tensorflow
!pip install tensorflow==2.7

!pip install imageai

!wget -O yolo.h5 https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5
!wget -O resnet50_imagenet_tf.2.0.h5 https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/resnet50_imagenet_tf.2.0.h5

"""
print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個

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

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from imageai.Detection import VideoObjectDetection

detector = VideoObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("yolo.h5")
detector.loadModel()
detector.detectObjectsFromVideo(
    input_file_path="traffic-mini.mp4",
    output_file_path= "traffic_detected",
    frames_per_second=20, 
    log_progress=True)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
安裝 imageai.Prediction

下載 ImageAI whl file
https://github.com/OlafenwaMoses/ImageAI/releases/download/2.0.2/imageai-2.0.2-py3-none-any.whl

pip install imageai-2.0.2-py3-none-any.whl
.whl在放在prompt所在地

"""

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

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
