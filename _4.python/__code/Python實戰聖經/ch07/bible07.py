#face_engine：簡單易用的臉部辨識

'''
pip install face-engine==2.0.0

'''

'''
from face_engine import FaceEngine
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt



engine = FaceEngine()
filename = 'person1.jpg'
# filename = 'person2.jpg'
# filename = 'person3.jpg'
#try:

_, boxes = engine.find_faces(filename)


#print(boxes)



img = Image.open(filename)
drawing = ImageDraw.Draw(img)
for i in range(len(boxes)):
    drawing.rectangle(boxes[i], outline='white', width=2)
plt.imshow(img)
plt.show()
#except:
#  print('未偵測到人臉！')

'''

print("face-recognition：效果絕佳的人臉辨識")
#!pip install face_recognition

import face_recognition
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt


# filename = 'person1.jpg'
# filename = 'person2.jpg'
# filename = 'person3.jpg'
filename = 'person12.jpg'
image = face_recognition.load_image_file(filename)
boxes = face_recognition.face_locations(image)
print(boxes)

img = Image.open(filename)
drawing = ImageDraw.Draw(img)
for i in range(len(boxes)):
    drawing.rectangle((boxes[i][3],boxes[i][0],boxes[i][1],boxes[i][2]), outline='red', width=2)
plt.imshow(img)
plt.show()


filename = 'obama.jpg'
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


img1 = face_recognition.load_image_file('sample1.jpg')
img2 = face_recognition.load_image_file('sample2.jpg')
img3 = face_recognition.load_image_file('sample3.jpg')
encoding1 = face_recognition.face_encodings(img1)[0]
encoding2 = face_recognition.face_encodings(img2)[0]
encoding3 = face_recognition.face_encodings(img3)[0]
known_faces = [encoding1, encoding2, encoding3]
names = ['jeng', 'chiou', 'david']

unknown = face_recognition.load_image_file("catch.jpg")
# unknown = face_recognition.load_image_file("lily2.jpg")
encoding_unknown = face_recognition.face_encodings(unknown)[0]
results = face_recognition.compare_faces(known_faces, encoding_unknown)
print(results)
face = ''
for i in range(len(results)):
  if results[i]: face = face + names[i] + '  '
if face == '':
    print('圖片中辨識不到資料庫中人臉！')
else:
    print('圖片中的人臉：' + face)



img1 = face_recognition.load_image_file('sample1.jpg')
img2 = face_recognition.load_image_file('sample2.jpg')
img3 = face_recognition.load_image_file('sample3.jpg')
encoding1 = face_recognition.face_encodings(img1)[0]
encoding2 = face_recognition.face_encodings(img2)[0]
encoding3 = face_recognition.face_encodings(img3)[0]
known_faces = [encoding1, encoding2, encoding3]
names = ['jeng', 'chiou', 'david']

unknown = face_recognition.load_image_file("catch.jpg")
#unknown = face_recognition.load_image_file("lily2.jpg")
encoding_unknown = face_recognition.face_encodings(unknown)[0]
distances = face_recognition.face_distance(known_faces, encoding_unknown)
print(distances)
face = ''
for i in range(len(distances)):
  if distances[i] < 0.5: face = face + names[i] + '  '
if face == '': print('圖片中辨識不到資料庫中人臉！')
else: print('圖片中的人臉：' + face)




