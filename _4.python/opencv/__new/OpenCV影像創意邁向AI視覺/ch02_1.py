# ch2_1.py
import cv2

img = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)  # 灰階讀取
print("列印灰階影像的屬性")
print(f"shape = {img.shape}")
print(f"size  = {img.size}")
print(f"dtype = {img.dtype}")


# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch02\ch2_2.py

# ch2_2.py
import cv2

img = cv2.imread("jk.jpg")  # 彩色讀取
print("列印彩色影像的屬性")
print(f"shape = {img.shape}")
print(f"size  = {img.size}")
print(f"dtype = {img.dtype}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch02\ch2_3.py

# ch2_3.py
import cv2

pt_y = 169
pt_x = 118
img = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)  # 灰階讀取
px = img[pt_y, pt_x]  # 讀px點
print(type(px))
print(f"BGR = {px}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch02\ch2_4.py

# ch2_4.py
import cv2

pt_y = 169
pt_x = 118
img = cv2.imread("jk.jpg")  # 彩色讀取
px = img[pt_y, pt_x]  # 讀px點
print(type(px))
print(f"BGR = {px}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch02\ch2_5.py

# ch2_5.py
import cv2

pt_y = 169
pt_x = 118
img = cv2.imread("jk.jpg")  # 彩色讀取
blue = img[pt_y, pt_x, 0]  # 讀 B 通道值
green = img[pt_y, pt_x, 1]  # 讀 G 通道值
red = img[pt_y, pt_x, 2]  # 讀 R 通道值
print(f"BGR = {blue}, {green}, {red}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch02\ch2_6.py

# ch2_6.py
import cv2

pt_y = 169
pt_x = 118
img = cv2.imread("jk.jpg")  # 彩色讀取
px = img[pt_y, pt_x]  # 讀取 px 點
print(f"更改前BGR = {px}")
px = [255, 255, 255]  # 修改 px 點
print(f"更改後BGR = {px}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch02\ch2_7.py

# ch2_7.py
import cv2

img = cv2.imread("jk.jpg")  # 彩色讀取
cv2.imshow("Before the change", img)
for y in range(img.shape[0] - 50, img.shape[0]):
    for x in range(img.shape[1] - 50, img.shape[1]):
        img[y, x] = [255, 255, 255]
cv2.imshow("After the change", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個
