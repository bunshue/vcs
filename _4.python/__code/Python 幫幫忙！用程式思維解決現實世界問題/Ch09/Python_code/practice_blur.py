import cv2

path = "C:/Users/Admin/AppData/Local/Programs/Python/Python310/Lib/site-packages/cv2/data/"
face_cascade = cv2.CascadeClassifier(path + 'haarcascade_frontalface_alt.xml')

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    face_rects = face_cascade.detectMultiScale(frame, scaleFactor = 1.2, minNeighbors = 3)

    for (x, y, w, h) in face_rects:
        face = cv2.blur(frame[y:y + h, x:x + w], (25, 25))
        frame[y:y + h, x: x + w] = face
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
        
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
