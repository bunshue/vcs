import cv2 
from PIL import Image
casc_path = "C:\\Users\\jeng\\AppData\\Local\\conda\\conda\\pkgs\\opencv3-3.1.0-py34_0\\Library\\etc\\haarcascades\\haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(casc_path)
imagename = "media\\person3.jpg"
image = cv2.imread(imagename)
faces = faceCascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30,30), flags = cv2.CASCADE_SCALE_IMAGE)
count = 1
for (x,y,w,h) in faces:
    cv2.rectangle(image, (x,y), (x+w,y+h), (128,255,0), 2)
    filename = "media\\face" + str(count)+ ".jpg"
    image1 = Image.open(imagename)
    image2 = image1.crop((x, y, x+w, y+h))
    image3 = image2.resize((200, 200), Image.ANTIALIAS)
    image3.save(filename)
    count += 1
cv2.namedWindow("facedetect")
cv2.imshow("facedetect", image)
cv2.waitKey(0)  
cv2.destroyWindow("facedetect")