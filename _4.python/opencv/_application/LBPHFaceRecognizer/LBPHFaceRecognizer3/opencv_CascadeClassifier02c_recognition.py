import cv2

model = cv2.face.LBPHFaceRecognizer_create()
model.read("faces.data")

print("load training data done")

# OpenCV 人臉識別分類器
xml_filename = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_frontalface_default.xml"
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)

cap = cv2.VideoCapture(0)
cv2.namedWindow("video", cv2.WINDOW_NORMAL)
# 可識別化名稱
names = ["david"]

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (600, 336))
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #### 在while內
    faces = face_cascade_classifier.detectMultiScale(gray, 1.1, 3)
    for x, y, w, h in faces:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        face_img = gray[y : y + h, x : x + w]
        face_img = cv2.resize(face_img, (400, 400))

        val = model.predict(face_img)

        print("label:{}, conf:{:.1f}".format(val[0], val[1]))
        if val[1] < 50:
            print("找到人臉, val =", val)
            print("找到人臉, val[0] =", val[0], "val[1] =", val[1], "name =", names[val[0]])
            cv2.putText(
                frame,
                names[val[0]],
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 255, 0),
                3,
            )

    #### 在while內
    cv2.imshow("video", frame)
    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        break
