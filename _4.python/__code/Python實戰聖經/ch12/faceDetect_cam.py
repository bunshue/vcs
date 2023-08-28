import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils 
face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.5)
while cap.isOpened():
    success, image = cap.read()
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)  #水平翻轉
    results = face_detection.process(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.detections:
        for detection in results.detections:
            mp_drawing.draw_detection(image, detection)
    cv2.imshow('image', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

cap.release()
cv2.destroyAllWindows()

