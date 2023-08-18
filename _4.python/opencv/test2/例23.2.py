import cv2
import numpy as np

images=[]
images.append(cv2.imread("a1.png",cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread("a2.png",cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread("b1.png",cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread("b2.png",cv2.IMREAD_GRAYSCALE))
labels=[0,0,1,1]
#print(labels)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(images, np.array(labels))  
predict_image=cv2.imread("a3.png",cv2.IMREAD_GRAYSCALE)
label,confidence= recognizer.predict(predict_image) 
print("label=",label)
print("confidence=",confidence)
