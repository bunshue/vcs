# ch6_1.py
import cv2
import numpy as np

# 建立GRAY影像陣列
image = np.zeros((5, 12), np.uint8)
print(f"修改前 image=\n{image}")  # 顯示修改前GRAY影像
print(f"image[1,4] = {image[1, 4]}")  # 列出特定像素點的內容

image[1, 4] = 255  # 修改像素點的內容
print(f"修改後 image=\n{image}")  # 顯示修改後的GRAY影像
print(f"image[1,4] = {image[1, 4]}")  # 列出特定像素點的內容


# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch06\ch6_10.py

# ch6_10.py
import cv2

img = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)  # 灰色讀取
cv2.imshow("Before modify", img)  # 顯示修改前影像img
for y in range(120, 140):  # 修改影像
    for x in range(110, 210):
        img.itemset((y, x), 255)
cv2.imshow("After modify", img)  # 顯示修改後影像img

cv2.waitKey(0)
cv2.destroyAllWindows()  # 刪除所有視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch06\ch6_11.py

# ch6_11.py
import cv2
import numpy as np

# 建立藍色blue底的彩色影像陣列
blue = np.zeros((2, 3, 3), np.uint8)
blue[:, :, 0] = 255  # 填滿藍色
print(f"blue =\n{blue}")  # 列印影像陣列
# 列印修訂前的像素點
print(f"blue[0,1,2] = {blue.item(0,1,2)}")

blue.itemset((0, 1, 2), 50)  # 修訂像素點的單一通道
print("修訂後")
# 列印修訂後的像素點
print(f"blue =\n{blue}")  # 列印影像陣列
print(f"blue[0,1,2] = {blue.item(0,1,2)}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch06\ch6_12.py

# ch6_12.py
import cv2

img = cv2.imread("jk.jpg")  # 彩色讀取
cv2.imshow("Before modify", img)  # 顯示修改前影像img
print(f"修改前img[115,110,1] = {img.item(115,110,1)}")
print(f"修改前img[125,110,1] = {img.item(125,110,1)}")
print(f"修改前img[135,110,1] = {img.item(135,110,1)}")
# 白色長條
for z in range(115, 145):  # 修改影像:一次一個通道值
    for y in range(110, 210):
        for x in range(0, 3):  # 一次一個通道值
            img.itemset((z, y, x), 255)  # 白色取代
cv2.imshow("After modify", img)  # 顯示修改後影像img
print(f"修改後img[115,110,1] = {img.item(115,110,1)}")
print(f"修改後img[125,110,1] = {img.item(125,110,1)}")
print(f"修改後img[135,110,1] = {img.item(135,110,1)}")
cv2.waitKey(0)
cv2.destroyAllWindows()  # 刪除所有視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch06\ch6_13.py

# ch6_13.py
import cv2

img = cv2.imread("jk.jpg")  # 彩色讀取
cv2.imshow("Hung Image", img)  # 顯示影像
face = img[30:220, 80:250]  # ROI
cv2.imshow("Face", face)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()  # 刪除所有視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch06\ch6_14.py

# ch6_14.py
import cv2
import numpy as np

img = cv2.imread("jk.jpg")  # 彩色讀取
cv2.imshow("Hung Image", img)  # 顯示影像
# ROI大小區塊建立馬賽克
face = np.random.randint(0, 256, size=(190, 170, 3))  # 馬賽克效果
img[30:220, 80:250] = face  # ROI
cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()  # 刪除所有視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch06\ch6_15.py

# ch6_15.py
import cv2
import numpy as np

img = cv2.imread("jk.jpg")  # 彩色讀取
cv2.imshow("Hung Image", img)  # 顯示影像
usa = cv2.imread("money.jpg")  # 彩色讀取
cv2.imshow("Money Image", usa)  # 顯示影像
face = img[30:220, 80:250]  # ROI
usa[30:220, 120:290] = face  # 複製到usa影像
cv2.imshow("Image", usa)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()  # 刪除所有視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch06\ch6_2.py

# ch6_2.py
import cv2

img = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)  # 灰色讀取
cv2.imshow("Before modify", img)  # 顯示修改前影像img
for y in range(120, 140):  # 修改影像
    for x in range(110, 210):
        img[y, x] = 255
cv2.imshow("After modify", img)  # 顯示修改後影像img

cv2.waitKey(0)
cv2.destroyAllWindows()  # 刪除所有視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch06\ch6_3.py

# ch6_3.py
import cv2
import numpy as np

# 建立藍色blue底的彩色影像陣列
blue_img = np.zeros((2, 3, 3), np.uint8)
blue_img[:, :, 0] = 255  # 填滿藍色
print(f"blue image =\n{blue_img}")  # 顯示blue_img影像陣列

# 建立綠色green底的彩色影像陣列
green_img = np.zeros((2, 3, 3), np.uint8)
green_img[:, :, 1] = 255  # 填滿綠色
print(f"green image =\n{green_img}")  # 顯示green_img影像陣列

# 建立紅色red底的彩色影像陣列
red_img = np.zeros((2, 3, 3), np.uint8)
red_img[:, :, 2] = 255  # 填滿紅色
print(f"red image =\n{red_img}")  # 顯示red_img影像陣列


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch06\ch6_4.py

# ch6_4.py
import cv2
import numpy as np

# 建立藍色blue底的彩色影像陣列
blue_img = np.zeros((100, 150, 3), np.uint8)
blue_img[:, :, 0] = 255  # 填滿藍色
print(f"blue image =\n{blue_img}")  # 顯示blue_img影像陣列
cv2.imshow("Blue Image", blue_img)  # 顯示藍色影像

# 建立綠色green底的彩色影像陣列
green_img = np.zeros((100, 150, 3), np.uint8)
green_img[:, :, 1] = 255  # 填滿綠色
print(f"green image =\n{green_img}")  # 顯示green_img影像陣列
cv2.imshow("Green Image", green_img)  # 顯示綠色影像

# 建立紅色red底的彩色影像陣列
red_img = np.zeros((100, 150, 3), np.uint8)
red_img[:, :, 2] = 255  # 填滿紅色
print(f"red image =\n{red_img}")  # 顯示red_img影像陣列
cv2.imshow("Red Image", red_img)  # 顯示紅色影像

cv2.waitKey(0)
cv2.destroyAllWindows()  # 刪除所有視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch06\ch6_5.py

# ch6_5.py
import cv2
import numpy as np

# 建立藍色blue底的彩色影像陣列
blue = np.zeros((2, 3, 3), np.uint8)
blue[:, :, 0] = 255  # 填滿藍色
print(f"blue =\n{blue}")  # 列印影像陣列
# 列印修訂前的像素點
print(f"blue[0,1] = {blue[0,1]}")

blue[0, 1] = [50, 100, 150]  # 修訂像素點
print("修訂後")
# 列印修訂後的像素點
print(f"blue =\n{blue}")  # 列印影像陣列


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch06\ch6_6.py

# ch6_6.py
import cv2
import numpy as np

# 建立藍色blue底的彩色影像陣列
blue = np.zeros((2, 3, 3), np.uint8)
blue[:, :, 0] = 255  # 填滿藍色
print(f"blue =\n{blue}")  # 列印影像陣列
# 列印修訂前的像素點
print(f"blue[0,1,2] = {blue[0,1,2]}")

blue[0, 1, 2] = 50  # 修訂像素點的單一通道
print("修訂後")
# 列印修訂後的像素點
print(f"blue =\n{blue}")  # 列印影像陣列
print(f"blue[0,1,2] = {blue[0,1,2]}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch06\ch6_7.py

# ch6_7.py
import cv2

img = cv2.imread("jk.jpg")  # 彩色讀取
cv2.imshow("Before modify", img)  # 顯示修改前影像img
print(f"修改前img[115,110] = {img[115,110]}")
print(f"修改前img[125,110] = {img[125,110]}")
print(f"修改前img[135,110] = {img[135,110]}")
# 紫色長條
for y in range(115, 125):  # 修改影像
    for x in range(110, 210):
        img[y, x] = [255, 0, 255]  # 紫色取代
# 白色長條
for z in range(125, 135):  # 修改影像:一次一個通道值
    for y in range(110, 210):
        for x in range(0, 3):  # 一次一個通道值
            img[z, y, x] = 255  # 白色取代
# 黃色長條
for y in range(135, 145):  # 修改影像
    for x in range(110, 210):
        img[y, x] = [0, 255, 255]  # 黃色取代
cv2.imshow("After modify", img)  # 顯示修改後影像img
print(f"修改後img[115,110] = {img[115,110]}")
print(f"修改後img[125,110] = {img[125,110]}")
print(f"修改後img[135,110] = {img[135,110]}")
cv2.waitKey(0)
cv2.destroyAllWindows()  # 刪除所有視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch06\ch6_7_1.py

# ch6_7_1.py
import cv2

img = cv2.imread("jk.jpg")  # 彩色讀取
cv2.imshow("Before modify", img)  # 顯示修改前影像img
print(f"修改前img[115,110] = {img[115,110]}")
print(f"修改前img[125,110] = {img[125,110]}")
print(f"修改前img[135,110] = {img[135,110]}")
# 紫色長條
img[115:125, 110:210] = [255, 0, 255]
# 白色長條
for z in range(125, 135):  # 修改影像:一次一個通道值
    for y in range(110, 210):
        for x in range(0, 3):  # 一次一個通道值
            img[z, y, x] = 255  # 白色取代
# 黃色長條
for y in range(135, 145):  # 修改影像
    for x in range(110, 210):
        img[y, x] = [0, 255, 255]  # 黃色取代
cv2.imshow("After modify", img)  # 顯示修改後影像img
print(f"修改後img[115,110] = {img[115,110]}")
print(f"修改後img[125,110] = {img[125,110]}")
print(f"修改後img[135,110] = {img[135,110]}")
cv2.waitKey(0)
cv2.destroyAllWindows()  # 刪除所有視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch06\ch6_8.py

# ch6_8.py
import cv2

img = cv2.imread("street.png", cv2.IMREAD_UNCHANGED)  # PNG讀取
cv2.imshow("Before modify", img)  # 顯示修改前影像img
print(f"修改前img[10,50] = {img[10,50]}")
print(f"修改前img[50,99] = {img[50,99]}")
print("-" * 70)
for z in range(0, 200):  # 一次一個修改alpha通道值
    for y in range(0, 200):
        img[z, y, 3] = 128  # 修改alpha通道值
print(f"修改後img[10,50] = {img[10,50]}")
print(f"修改後img[50,99] = {img[50,99]}")
cv2.imwrite("street128.png", img)  # 儲存含alpha通道的檔案

cv2.waitKey(0)
cv2.destroyAllWindows()  # 刪除所有視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch06\ch6_8_1.py

# ch6_8_1.py
import cv2

img = cv2.imread("street.png", cv2.IMREAD_UNCHANGED)  # PNG讀取
cv2.imshow("Before modify", img)  # 顯示修改前影像img
print(f"修改前img[10,50] = {img[10,50]}")
print(f"修改前img[50,99] = {img[50,99]}")
print("-" * 70)
img[0:200, 0:200, 3] = 128
print(f"修改後img[10,50] = {img[10,50]}")
print(f"修改後img[50,99] = {img[50,99]}")
cv2.imwrite("street128_1.png", img)  # 儲存含alpha通道的檔案

cv2.waitKey(0)
cv2.destroyAllWindows()  # 刪除所有視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch06\ch6_9.py

# ch6_9.py
import numpy as np

image = np.random.randint(0, 200, size=[3, 5], dtype=np.uint8)
print(f"image = \n{image}")
print(f"修改前image.item(1,3) = {image.item(1,3)}")
image.itemset((1, 3), 255)  # 修訂內容為 255
print("-" * 70)
print(f"修改後image =\n{image}")
print(f"修改後image.item(1,3) = {image.item(1,3)}")


print("------------------------------------------------------------")  # 60個
