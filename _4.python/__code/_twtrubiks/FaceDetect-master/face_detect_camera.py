import cv2


def main():
    face_detect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    name = "twtrubiks"
    number = 0
    cam = cv2.VideoCapture(0)
    while True:
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # faces = face_detect.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(200, 200))
        faces = face_detect.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
        for (x, y, w, h) in faces:
            number += 1
            cv2.imwrite("camera/{}.{}.jpg".format(name, number), gray[y:y + h, x:x + w])
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.waitKey(100)
        cv2.imshow("Face", img)
        cv2.waitKey(1)
        if number >= 10:
            break
    cam.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
