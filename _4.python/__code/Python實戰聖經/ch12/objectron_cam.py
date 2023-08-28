import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

mp_drawing = mp.solutions.drawing_utils
mp_objectron = mp.solutions.objectron
objectron = mp_objectron.Objectron(static_image_mode=False, max_num_objects=5, min_detection_confidence=0.5,
                            min_tracking_confidence=0.99, model_name='Chair')

while cap.isOpened():
    success, image = cap.read()
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)  #水平翻轉
    results = objectron.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.detected_objects:
        for detected_object in results.detected_objects:
            mp_drawing.draw_landmarks(image, detected_object.landmarks_2d, mp_objectron.BOX_CONNECTIONS)
            mp_drawing.draw_axis(image, detected_object.rotation, detected_object.translation)
    cv2.imshow('MediaPipe Objectron', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

cap.release()
cv2.destroyAllWindows()

