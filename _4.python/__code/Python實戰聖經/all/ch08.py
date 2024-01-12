import sys

"""
圖片內容偵測


#ImageAI：物體偵測

!pip uninstall tensorflow
!pip install tensorflow==2.7
!pip install imageai


!wget -O yolo.h5 https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5
!wget -O resnet50_imagenet_tf.2.0.h5 https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/resnet50_imagenet_tf.2.0.h5

"""

""" fail in sugar
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
"""

print('------------------------------------------------------------')	#60個


""" fail in sugar
from imageai.Detection import VideoObjectDetection

detector = VideoObjectDetection()
detector.setModelTypeAsYOLOv3()


#detector.setModelPath("yolo.h5")

detector.loadModel()

detector.detectObjectsFromVideo(
    input_file_path="traffic-mini.mp4",
    output_file_path= "traffic_detected",
    frames_per_second=20, 
    log_progress=True)
"""

print('------------------------------------------------------------')	#60個

"""
安裝 imageai.Prediction

下載 ImageAI whl file
https://github.com/OlafenwaMoses/ImageAI/releases/download/2.0.2/imageai-2.0.2-py3-none-any.whl

pip install imageai-2.0.2-py3-none-any.whl
.whl在放在prompt所在地


"""

""" fail in sugar
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
"""

print('------------------------------------------------------------')	#60個


