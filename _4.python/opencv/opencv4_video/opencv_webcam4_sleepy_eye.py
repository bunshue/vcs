# 目前 webcam 僅 x64 電腦可用

import cv2

import sys
import numpy as np
import math

print("------------------------------------------------------------")  # 60個

print("按 ESC 離開")

from functools import wraps
import time

lastsave = 0


def counter(func):
    @wraps(func)
    def tmp(*args, **kwargs):
        tmp.count += 1
        global lastsave
        if time.time() - lastsave > 3:
            # this is in seconds, so 5 minutes = 300 seconds
            lastsave = time.time()
            tmp.count = 0
        return func(*args, **kwargs)

    tmp.count = 0
    return tmp


xml_filename1 = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_default.xml"
face_cascade_classifier = cv2.CascadeClassifier(xml_filename1)

xml_filename2 = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_eye.xml"
eye_cascade_classifier = cv2.CascadeClassifier(xml_filename2)

cap = cv2.VideoCapture(0)


@counter
def closed():
    print("Eye Closed")


def openeye():
    print("Eye is Open")


def warning():
    print("Sleeping~~~~")


while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade_classifier.detectMultiScale(gray, 1.3, 5)

    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y : y + h, x : x + w]
        roi_color = img[y : y + h, x : x + w]

        eyes = eye_cascade_classifier.detectMultiScale(roi_gray)

        if eyes is not ():
            for ex, ey, ew, eh in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
                openeye()
        else:
            closed()
            if closed.count == 3:
                warning()

    cv2.imshow("WebCam", img)
    k = cv2.waitKey(1)
    if k == 27:  # ESC
        break
    elif k == ord("s"):  # 若按下 s 鍵則存圖
        image_filename = (
            "Image_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".jpg"
        )
        cv2.imwrite(image_filename, frame)
        print("已存圖")

# 釋放所有資源
cap.release()  # 釋放攝影機
cv2.destroyAllWindows()  # 關閉所有 OpenCV 視窗


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
