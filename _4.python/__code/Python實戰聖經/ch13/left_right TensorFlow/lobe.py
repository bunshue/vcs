import json
import numpy as np
import tensorflow as tf
from PIL import Image
import cv2

with open("signature.json", "r") as f:
    signature = json.load(f)
inputs = signature.get('inputs')
labels = signature.get('classes')['Label']
#print(labels)

input_width, input_height = inputs["Image"]["shape"][1:3]
image = cv2.imread('example/right1.jpg')
image = Image.fromarray(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
image = image.resize((input_width, input_height))
image = np.asarray(image, dtype=np.float32) / 255.0
image = np.expand_dims(image, axis=0)

model = tf.saved_model.load('.')
predict = model.signatures["serving_default"](tf.constant(image))['Confidences'][0]
index = np.argmax(predict, axis=-1)
classname = labels[index]
print(classname)

