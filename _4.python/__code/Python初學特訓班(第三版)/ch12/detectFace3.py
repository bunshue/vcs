import cv2 
casc_path = "C:\\Users\\jeng\\AppData\\Local\\conda\\conda\\pkgs\\opencv3-3.1.0-py34_0\\Library\\etc\\haarcascades\\haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(casc_path)
image = cv2.imread("media\\person3.jpg")
faces = faceCascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30,30), flags = cv2.CASCADE_SCALE_IMAGE)
#image.shape[0]:圖片高度，image.shape[1]:圖片寬度
cv2.rectangle(image, (10,image.shape[0]-20), (110,image.shape[0]), (0,0,0), -1)
cv2.putText(image,"Find " + str(len(faces)) + " face!", (10,image.shape[0]-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)
for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w, y+h),(128,255,0),2)
cv2.namedWindow("facedetect")
cv2.imshow("facedetect", image)
cv2.waitKey(0)  
cv2.destroyWindow("facedetect")