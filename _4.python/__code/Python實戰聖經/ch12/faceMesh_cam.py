import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)

while cap.isOpened():
    success, image = cap.read()
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)  #水平翻轉
    results = face_mesh.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            mp_drawing.draw_landmarks(image=image, landmark_list=face_landmarks, 
                connections=mp_face_mesh.FACE_CONNECTIONS, landmark_drawing_spec=drawing_spec,
                connection_drawing_spec=drawing_spec)
    cv2.imshow('image', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

cap.release()
cv2.destroyAllWindows()

