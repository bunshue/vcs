# ch31_1.py
import cv2

pictPath = "haar_carplate.xml"                          # 哈爾特徵檔路徑
img = cv2.imread("testCar/cartest1.jpg")                # 讀辨識的影像
car_cascade = cv2.CascadeClassifier(pictPath)           # 讀哈爾特徵檔
# 執行辨識
plates = car_cascade.detectMultiScale(img, scaleFactor=1.05, minNeighbors=3,
         minSize=(20,20),maxSize=(155,50))  
if len(plates) > 0 :                                    # 有偵測到車牌
    for (x, y, w, h) in plates:                         # 標記車牌  
        carplate = img[y:y+h, x:x+w]                    # 車牌影像
else:
    print("偵測車牌失敗")

cv2.imshow('Car', carplate)                             # 顯示所讀取的車輛
cv2.imwrite("atq9305.jpg", carplate)
cv2.waitKey(0)
cv2.destroyAllWindows()



        




#檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch31\ch31_2.py

# ch31_2.py
from PIL import Image
import pytesseract

config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
text = pytesseract.image_to_string(Image.open('atq9305.jpg'),
                                   config=config)
print(f"車號是 : {text}")



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch31\ch31_3.py

# ch31_3.py
import cv2
import pytesseract

config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
pictPath = "haar_carplate.xml"                          # 哈爾特徵檔路徑
img = cv2.imread("testCar/cartest1.jpg")                # 讀辨識的影像
car_cascade = cv2.CascadeClassifier(pictPath)           # 讀哈爾特徵檔
# 執行辨識
plates = car_cascade.detectMultiScale(img, scaleFactor=1.05,
         minNeighbors=3, minSize=(20,20), maxSize=(155,50))  
if len(plates) > 0 :                                    # 有偵測到車牌
    for (x, y, w, h) in plates:                         # 標記車牌  
        carplate = img[y:y+h, x:x+w]                    # 車牌影像        
else:
    print("偵測車牌失敗")

cv2.imshow('Car', carplate)                             # 顯示所讀取的車輛
text = pytesseract.image_to_string(carplate,config=config)  # OCR辨識
print(f"車號是 : {text}")

cv2.waitKey(0)
cv2.destroyAllWindows()



        












print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch31\ch31_4.py

# ch31_4.py
import cv2
import pytesseract

config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
pictPath = "haar_carplate.xml"                          # 哈爾特徵檔路徑
img = cv2.imread("testCar/cartest3.jpg")                # 讀辨識的影像
car_cascade = cv2.CascadeClassifier(pictPath)           # 讀哈爾特徵檔
# 執行辨識
plates = car_cascade.detectMultiScale(img, scaleFactor=1.05, minNeighbors=3,
         minSize=(20,20),maxSize=(155,50))  
if len(plates) > 0 :                                    # 有偵測到車牌
    for (x, y, w, h) in plates:                         # 標記車牌  
        carplate = img[y:y+h, x:x+w]                    # 車牌影像        
else:
    print("偵測車牌失敗")

cv2.imshow('Car', carplate)                             # 顯示所讀取的車輛
text = pytesseract.image_to_string(carplate,config=config)  # OCR辨識
print(f"車號是 : {text}")

cv2.waitKey(0)
cv2.destroyAllWindows()



        












print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch31\ch31_5.py

# ch31_5.py
import cv2
import pytesseract

carFile = "car_plate.jpg"
config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
pictPath = "haar_carplate.xml"                          # 哈爾特徵檔路徑
img = cv2.imread("testCar/cartest3.jpg")                # 讀辨識的影像
car_cascade = cv2.CascadeClassifier(pictPath)           # 讀哈爾特徵檔
# 執行辨識
plates = car_cascade.detectMultiScale(img, scaleFactor=1.05, minNeighbors=3,
         minSize=(20,20),maxSize=(155,50))  
if len(plates) > 0 :                                    # 有偵測到車牌
    for (x, y, w, h) in plates:                         # 標記車牌  
        carplate = img[y:y+h, x:x+w]                    # 車牌影像        
else:
    print("偵測車牌失敗")

cv2.imshow('Car', carplate)                             # 顯示所讀取的車輛
ret, dst = cv2.threshold(carplate,100,255,cv2.THRESH_BINARY)  # 二值化
cv2.imshow('Car binary', dst)                           # 顯示二值化車牌
text = pytesseract.image_to_string(carplate,config=config)  # OCR辨識
print(f"車號是 : {text}")

cv2.waitKey(0)
cv2.destroyAllWindows()



        












print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch31\ch31_6.py

# ch31_6.py
import cv2
import numpy as np
import pytesseract

carFile = "car_plate.jpg"
config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
pictPath = "haar_carplate.xml"                          # 哈爾特徵檔路徑
img = cv2.imread("testCar/cartest3.jpg")                # 讀辨識的影像
car_cascade = cv2.CascadeClassifier(pictPath)           # 讀哈爾特徵檔
# 執行辨識
plates = car_cascade.detectMultiScale(img, scaleFactor=1.05, minNeighbors=3,
         minSize=(20,20),maxSize=(155,50))  
if len(plates) > 0 :                                    # 有偵測到車牌
    for (x, y, w, h) in plates:                         # 標記車牌  
        carplate = img[y:y+h, x:x+w]                    # 車牌影像        
else:
    print("偵測車牌失敗")

cv2.imshow('Car', carplate)                             # 顯示所讀取的車輛
ret, dst = cv2.threshold(carplate,100,255,cv2.THRESH_BINARY)  # 二值化

cv2.imshow('Car binary', dst)                           # 顯示二值化車牌
kernel = np.ones((3,3), np.uint8)
dst1 = cv2.morphologyEx(dst, cv2.MORPH_OPEN, kernel)    # 執行開運算
text = pytesseract.image_to_string(dst1, config=config) # 執行辨識
print(f"車號是 : {text}")
cv2.imwrite(carFile, dst)                                # 寫入儲存
cv2.waitKey(0)
cv2.destroyAllWindows()



        












print("------------------------------------------------------------")  # 60個









