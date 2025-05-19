# ch27_1.py
import cv2

pictPath = r"C:\opencv\data\haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(pictPath)  # 建立辨識物件
img = cv2.imread("jk.jpg")  # 讀取影像
faces = face_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
# 標註右下角底色是黃色
cv2.rectangle(
    img,
    (img.shape[1] - 140, img.shape[0] - 20),
    (img.shape[1], img.shape[0]),
    (0, 255, 255),
    -1,
)
# 標註找到多少的人臉
cv2.putText(
    img,
    "Finding " + str(len(faces)) + " face",
    (img.shape[1] - 135, img.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 0, 0),
    1,
)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch27\ch27_10.py

# ch27_10.py
import cv2

pictPath = r"C:\opencv\data\haarcascade_upperbody.xml"
body_cascade = cv2.CascadeClassifier(pictPath)  # 建立辨識物件
img = cv2.imread("people1.jpg")  # 讀取影像
bodies = body_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=9, minSize=(20, 20)
)
# 標註身體
for x, y, w, h in bodies:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住身體
cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch27\ch27_11.py

# ch27_11.py
import cv2

pictPath1 = r"C:\opencv\data\haarcascade_frontalface_default.xml"
pictPath2 = r"C:\opencv\data\haarcascade_eye.xml"

face_cascade = cv2.CascadeClassifier(pictPath1)  # 建立人臉物件
img = cv2.imread("jk.jpg")  # 讀取影像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 偵測人臉
faces = face_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
# 偵測雙眼
eyes_cascade = cv2.CascadeClassifier(pictPath2)  # 建立雙眼物件
eyes = eyes_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
# 將雙眼框起來, 由於有可能找到好幾個眼睛所以用迴圈繪出來
for x, y, w, h in eyes:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # 綠色框住眼睛
cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch27\ch27_12.py

# ch27_12.py
import cv2

pictPath1 = r"C:\opencv\data\haarcascade_frontalface_default.xml"
pictPath2 = r"C:\opencv\data\haarcascade_eye.xml"

face_cascade = cv2.CascadeClassifier(pictPath1)  # 建立人臉物件
img = cv2.imread("jk.jpg")  # 讀取影像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 偵測人臉
faces = face_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
# 偵測雙眼
eyes_cascade = cv2.CascadeClassifier(pictPath2)  # 建立雙眼物件
eyes = eyes_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=7, minSize=(20, 20)
)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
# 將雙眼框起來, 由於有可能找到好幾個眼睛所以用迴圈繪出來
for x, y, w, h in eyes:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # 綠色框住眼睛
cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch27\ch27_13.py

# ch27_13.py
import cv2

pictPath1 = r"C:\opencv\data\haarcascade_frontalface_default.xml"
pictPath2 = r"C:\opencv\data\haarcascade_lefteye_2splits.xml"

face_cascade = cv2.CascadeClassifier(pictPath1)  # 建立人臉物件
img = cv2.imread("jk.jpg")  # 讀取影像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 偵測人臉
faces = face_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
# 偵測左眼
eyes_cascade = cv2.CascadeClassifier(pictPath2)  # 建立左眼物件
eyes = eyes_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=7, minSize=(20, 20)
)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
# 將左眼框起來, 由於有可能找到好幾個眼睛所以用迴圈繪出來
for x, y, w, h in eyes:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # 綠色框住眼睛
cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch27\ch27_14.py

# ch27_14.py
import cv2

pictPath1 = r"C:\opencv\data\haarcascade_frontalface_default.xml"
pictPath2 = r"C:\opencv\data\haarcascade_righteye_2splits.xml"

face_cascade = cv2.CascadeClassifier(pictPath1)  # 建立人臉物件
img = cv2.imread("jk.jpg")  # 讀取影像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 偵測人臉
faces = face_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
# 偵測右眼
eyes_cascade = cv2.CascadeClassifier(pictPath2)  # 建立右眼物件
eyes = eyes_cascade.detectMultiScale(
    img, scaleFactor=1.3, minNeighbors=7, minSize=(20, 20)
)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
# 將右眼框起來, 由於有可能找到好幾個眼睛所以用迴圈繪出來
for x, y, w, h in eyes:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # 綠色框住眼睛
cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch27\ch27_15.py

# ch27_15.py
import cv2

pictPath = r"C:\opencv\data\haarcascade_frontalcatface.xml"
cat_cascade = cv2.CascadeClassifier(pictPath)  # 建立辨識物件
img = cv2.imread("cat1.jpg")  # 讀取影像
faces = cat_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
# 將貓臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住貓臉
cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch27\ch27_16.py

# ch27_16.py
import cv2

pictPath = r"C:\opencv\data\haarcascade_frontalcatface.xml"
cat_cascade = cv2.CascadeClassifier(pictPath)  # 建立辨識物件
img = cv2.imread("cat2.jpg")  # 讀取影像
faces = cat_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=9, minSize=(20, 20)
)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch27\ch27_17.py

# ch27_17.py
import cv2

pictPath = r"C:\opencv\data\haarcascade_russian_plate_number.xml"
car_cascade = cv2.CascadeClassifier(pictPath)  # 建立辨識物件
img = cv2.imread("car.jpg")  # 讀取影像
plates = car_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
# 將車牌框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in plates:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住車牌
cv2.imshow("Car Plate", img)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch27\ch27_18.py

# ch27_18.py
import cv2

pictPath = r"C:\opencv\data\haarcascade_russian_plate_number.xml"
car_cascade = cv2.CascadeClassifier(pictPath)  # 建立辨識物件
img = cv2.imread("car1.jpg")  # 讀取影像
plates = car_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
# 將車牌框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in plates:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住車牌
cv2.imshow("Car Plate", img)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch27\ch27_19.py

# ch27_19.py
import cv2

pictPath = r"C:\opencv\data\haarcascade_russian_plate_number.xml"
car_cascade = cv2.CascadeClassifier(pictPath)  # 建立辨識物件
img = cv2.imread("car2.jpg")  # 讀取影像
plates = car_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
# 將車牌框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in plates:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住車牌
cv2.imshow("Car Plate", img)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch27\ch27_2.py

# ch27_2.py
import cv2

pictPath = r"C:\opencv\data\haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(pictPath)  # 建立辨識物件
img = cv2.imread("g5.jpg")  # 讀取影像
faces = face_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
# 標註右下角底色是黃色
cv2.rectangle(
    img,
    (img.shape[1] - 140, img.shape[0] - 20),
    (img.shape[1], img.shape[0]),
    (0, 255, 255),
    -1,
)
# 標註找到多少的人臉
cv2.putText(
    img,
    "Finding " + str(len(faces)) + " face",
    (img.shape[1] - 135, img.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 0, 0),
    1,
)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch27\ch27_3.py

# ch27_3.py
import cv2

pictPath = r"C:\opencv\data\haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(pictPath)  # 建立辨識物件
img = cv2.imread("solvay1927.jpg")  # 讀取影像
faces = face_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
# 標註右下角底色是黃色
cv2.rectangle(
    img,
    (img.shape[1] - 140, img.shape[0] - 20),
    (img.shape[1], img.shape[0]),
    (0, 255, 255),
    -1,
)
# 標註找到多少的人臉
cv2.putText(
    img,
    "Finding " + str(len(faces)) + " face",
    (img.shape[1] - 135, img.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 0, 0),
    1,
)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch27\ch27_3_1.py

# ch27_3_1.py
import cv2

pictPath = r"C:\opencv\data\haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(pictPath)  # 建立辨識物件
img = cv2.imread("solvay1927.jpg")  # 讀取影像
faces = face_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=5, minSize=(20, 20)
)
# 標註右下角底色是黃色
cv2.rectangle(
    img,
    (img.shape[1] - 140, img.shape[0] - 20),
    (img.shape[1], img.shape[0]),
    (0, 255, 255),
    -1,
)
# 標註找到多少的人臉
cv2.putText(
    img,
    "Finding " + str(len(faces)) + " face",
    (img.shape[1] - 135, img.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 0, 0),
    1,
)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch27\ch27_4.py

# ch27_4.py
import cv2

pictPath = r"C:\opencv\data\haarcascade_frontalface_alt.xml"
face_cascade = cv2.CascadeClassifier(pictPath)  # 建立辨識物件
img = cv2.imread("solvay1927.jpg")  # 讀取影像
faces = face_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
# 標註右下角底色是黃色
cv2.rectangle(
    img,
    (img.shape[1] - 140, img.shape[0] - 20),
    (img.shape[1], img.shape[0]),
    (0, 255, 255),
    -1,
)
# 標註找到多少的人臉
cv2.putText(
    img,
    "Finding " + str(len(faces)) + " face",
    (img.shape[1] - 135, img.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 0, 0),
    1,
)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch27\ch27_4_1.py

# ch27_4_1.py
import cv2

pictPath = r"C:\opencv\data\haarcascade_frontalface_alt.xml"
face_cascade = cv2.CascadeClassifier(pictPath)  # 建立辨識物件
img = cv2.imread("solvay1927.jpg")  # 讀取影像
faces = face_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20), maxSize=(50, 50)
)
# 標註右下角底色是黃色
cv2.rectangle(
    img,
    (img.shape[1] - 140, img.shape[0] - 20),
    (img.shape[1], img.shape[0]),
    (0, 255, 255),
    -1,
)
# 標註找到多少的人臉
cv2.putText(
    img,
    "Finding " + str(len(faces)) + " face",
    (img.shape[1] - 135, img.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 0, 0),
    1,
)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch27\ch27_5.py

# ch27_5.py
import cv2

pictPath = r"C:\opencv\data\haarcascade_frontalface_alt2.xml"
face_cascade = cv2.CascadeClassifier(pictPath)  # 建立辨識物件
img = cv2.imread("solvay1927.jpg")  # 讀取影像
faces = face_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20), maxSize=(50, 50)
)
# 標註右下角底色是黃色
cv2.rectangle(
    img,
    (img.shape[1] - 140, img.shape[0] - 20),
    (img.shape[1], img.shape[0]),
    (0, 255, 255),
    -1,
)
# 標註找到多少的人臉
cv2.putText(
    img,
    "Finding " + str(len(faces)) + " face",
    (img.shape[1] - 135, img.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 0, 0),
    1,
)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch27\ch27_6.py

# ch27_6.py
import cv2

pictPath = r"C:\opencv\data\haarcascade_frontalface_alt_tree.xml"
face_cascade = cv2.CascadeClassifier(pictPath)  # 建立辨識物件
img = cv2.imread("solvay1927.jpg")  # 讀取影像
faces = face_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
# 標註右下角底色是黃色
cv2.rectangle(
    img,
    (img.shape[1] - 140, img.shape[0] - 20),
    (img.shape[1], img.shape[0]),
    (0, 255, 255),
    -1,
)
# 標註找到多少的人臉
cv2.putText(
    img,
    "Finding " + str(len(faces)) + " face",
    (img.shape[1] - 135, img.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 0, 0),
    1,
)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch27\ch27_6_1.py

# ch27_6_1.py
import cv2

pictPath = r"C:\opencv\data\haarcascade_frontalface_alt.xml"
face_cascade = cv2.CascadeClassifier(pictPath)  # 建立辨識物件
img = cv2.imread("s_1927.jpg")  # 讀取影像
faces = face_cascade.detectMultiScale(
    img, scaleFactor=1.02, minNeighbors=3, minSize=(20, 20)
)
# 標註右下角底色是黃色
cv2.rectangle(
    img,
    (img.shape[1] - 140, img.shape[0] - 20),
    (img.shape[1], img.shape[0]),
    (0, 255, 255),
    -1,
)
# 標註找到多少的人臉
cv2.putText(
    img,
    "Finding " + str(len(faces)) + " face",
    (img.shape[1] - 135, img.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 0, 0),
    1,
)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch27\ch27_6_2.py

# ch27_6_2.py
import cv2

pictPath = r"C:\opencv\data\haarcascade_profileface.xml"
face_cascade = cv2.CascadeClassifier(pictPath)  # 建立辨識物件
img = cv2.imread("s_1927.jpg")  # 讀取影像
faces = face_cascade.detectMultiScale(
    img, scaleFactor=1.3, minNeighbors=4, minSize=(20, 20)
)
# 標註右下角底色是黃色
cv2.rectangle(
    img,
    (img.shape[1] - 140, img.shape[0] - 20),
    (img.shape[1], img.shape[0]),
    (0, 255, 255),
    -1,
)
# 標註找到多少的人臉
cv2.putText(
    img,
    "Finding " + str(len(faces)) + " face",
    (img.shape[1] - 135, img.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 0, 0),
    1,
)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch27\ch27_7.py

# ch27_7.py
import cv2

pictPath = r"C:\opencv\data\haarcascade_fullbody.xml"
body_cascade = cv2.CascadeClassifier(pictPath)  # 建立辨識物件
img = cv2.imread("people1.jpg")  # 讀取影像
bodies = body_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
# 標註身體
for x, y, w, h in bodies:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住身體
cv2.imshow("Body", img)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch27\ch27_8.py

# ch27_8.py
import cv2

pictPath = r"C:\opencv\data\haarcascade_fullbody.xml"
body_cascade = cv2.CascadeClassifier(pictPath)  # 建立辨識物件
img = cv2.imread("people2.jpg")  # 讀取影像
bodies = body_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
# 標註身體
for x, y, w, h in bodies:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住身體
cv2.imshow("Body", img)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch27\ch27_9.py

# ch27_9.py
import cv2

pictPath = r"C:\opencv\data\haarcascade_lowerbody.xml"
body_cascade = cv2.CascadeClassifier(pictPath)  # 建立辨識物件
img = cv2.imread("people1.jpg")  # 讀取影像
bodies = body_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
# 標註身體
for x, y, w, h in bodies:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住身體
cv2.imshow("Body", img)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個
