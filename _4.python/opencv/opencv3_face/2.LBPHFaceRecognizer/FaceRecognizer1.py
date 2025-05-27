"""
FaceRecognizer1

"""

import cv2
import os
import numpy as np

print("------------------------------------------------------------")  # 60個

images = []
images.append(cv2.imread("data/a1.png", cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread("data/a2.png", cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread("data/b1.png", cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread("data/b2.png", cv2.IMREAD_GRAYSCALE))
labels = [0, 0, 1, 1]
# print(labels)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(images, np.array(labels))
predict_image = cv2.imread("data/a3.png", cv2.IMREAD_GRAYSCALE)
label, confidence = recognizer.predict(predict_image)
print("label=", label)
print("confidence=", confidence)

print("------------------------------------------------------------")  # 60個

images = []
images.append(cv2.imread("data/e01.png", cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread("data/e02.png", cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread("data/e11.png", cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread("data/e12.png", cv2.IMREAD_GRAYSCALE))
labels = [0, 0, 1, 1]
# print(labels)
recognizer = cv2.face.EigenFaceRecognizer_create()
recognizer.train(images, np.array(labels))
predict_image = cv2.imread("data/eTest.png", cv2.IMREAD_GRAYSCALE)
label, confidence = recognizer.predict(predict_image)
print("label=", label)
print("confidence=", confidence)

print("------------------------------------------------------------")  # 60個

images = []
images.append(cv2.imread("data/f01.png", cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread("data/f02.png", cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread("data/f11.png", cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread("data/f12.png", cv2.IMREAD_GRAYSCALE))
labels = [0, 0, 1, 1]
# print(labels)
recognizer = cv2.face.FisherFaceRecognizer_create()
recognizer.train(images, np.array(labels))
predict_image = cv2.imread("data/fTest.png", cv2.IMREAD_GRAYSCALE)
label, confidence = recognizer.predict(predict_image)
print("label=", label)
print("confidence=", confidence)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個




