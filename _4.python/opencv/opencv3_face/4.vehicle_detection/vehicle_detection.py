import cv2


# 汽車模型
cars_xml_filename = "cars.xml"

video_filename = "data/video1.avi"
# video_filename = "data/video2.avi"

print("------------------------------------------------------------")  # 60個

car_cascade_classifier = cv2.CascadeClassifier(cars_xml_filename)  # 建立辨識物件 汽車

cap = cv2.VideoCapture(video_filename)

while True:
    ret, img = cap.read()
    if type(img) == type(None):
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cars = car_cascade_classifier.detectMultiScale(gray, 1.1, 1)

    for x, y, w, h in cars:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow("video", img)

    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
img = cv2.imread("cars.jpg")# 彩色讀取
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#轉灰階
gray = cv2.medianBlur(gray, 5)                  # 模糊化去除雜訊

car_cascade_classifier = cv2.CascadeClassifier(cars_xml_filename)  # 建立辨識物件 汽車

cars = car_cascade_classifier.detectMultiScale(gray, 1.1, 3)       # 偵測汽車

# 把汽車框起來
for x, y, w, h in cars:
    cv2.rectangle(img, (x, y), (x + w, y + h), GREEN, 2)   # 繪製外框

cv2.imshow("ImageShow", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
