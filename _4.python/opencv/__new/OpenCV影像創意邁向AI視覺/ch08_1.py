# ch8_1.py
import cv2
import numpy as np

src1 = np.random.randint(0, 256, size=[3, 3], dtype=np.uint8)
src2 = np.random.randint(0, 256, size=[3, 3], dtype=np.uint8)
res = cv2.add(src1, src2)
print(f"src1 = \n {src1}")
print(f"src2 = \n {src2}")
print(f"dst = \n {src1+src2}")


# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch08\ch8_10.py

# ch8_10.py
import cv2
import numpy as np

src1 = cv2.imread("lake.jpg")  # 影像 src1
cv2.imshow("lake", src1)
src2 = cv2.imread("geneva.jpg")  # 影像 src2
cv2.imshow("geneva.jpg", src2)
alpha = 1
beta = 0.2
gamma = 1
dst = cv2.addWeighted(src1, alpha, src2, beta, gamma)  # 加權和
cv2.imshow("lake+geneva", dst)  # 顯示結果

cv2.waitKey()
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch08\ch8_11.py

# ch8_11.py
import cv2
import numpy as np

src1 = np.random.randint(0, 255, (3, 5), dtype=np.uint8)
src2 = np.zeros((3, 5), dtype=np.uint8)
src2[0:2, 0:2] = 255
dst = cv2.bitwise_and(src1, src2)
print(f"src1 = \n {src1}")
print(f"src2 = \n {src2}")
print(f"dst = \n {dst}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch08\ch8_12.py

# ch8_12.py
import cv2
import numpy as np

src1 = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)  # 讀取影像
src2 = np.zeros(src1.shape, dtype=np.uint8)  # 建立mask

src2[30:260, 70:260] = 255
dst = cv2.bitwise_and(src1, src2)  # 執行and運算
cv2.imshow("Hung", src1)
cv2.imshow("Mask", src2)
cv2.imshow("Result", dst)

cv2.waitKey()
cv2.destroyAllWindows()  # 刪除所有視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch08\ch8_13.py

# ch8_13.py
import cv2
import numpy as np

src1 = cv2.imread("jk.jpg")  # 讀取影像
src2 = np.zeros(src1.shape, dtype=np.uint8)  # 建立mask

src2[30:260, 70:260, :] = 255  # 這是3維陣列
dst = cv2.bitwise_and(src1, src2)  # 執行and運算
cv2.imshow("Hung", src1)
cv2.imshow("Mask", src2)
cv2.imshow("Result", dst)

cv2.waitKey()
cv2.destroyAllWindows()  # 刪除所有視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch08\ch8_14.py

# ch8_14.py
import cv2
import numpy as np

src1 = np.random.randint(0, 255, (3, 5), dtype=np.uint8)
src2 = np.zeros((3, 5), dtype=np.uint8)
src2[0:2, 0:2] = 255
dst = cv2.bitwise_or(src1, src2)
print(f"src1 = \n {src1}")
print(f"src2 = \n {src2}")
print(f"dst = \n {dst}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch08\ch8_15.py

# ch8_15.py
import cv2
import numpy as np

src1 = cv2.imread("jk.jpg")  # 讀取影像
src2 = np.zeros(src1.shape, dtype=np.uint8)  # 建立mask

src2[30:260, 70:260, :] = 255  # 這是3維陣列
dst = cv2.bitwise_or(src1, src2)  # 執行or運算
cv2.imshow("Hung", src1)
cv2.imshow("Mask", src2)
cv2.imshow("Result", dst)

cv2.waitKey()
cv2.destroyAllWindows()  # 刪除所有視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch08\ch8_16.py

# ch8_16.py
import cv2
import numpy as np

src = cv2.imread("forest.jpg")  # 讀取影像
dst = cv2.bitwise_not(src)  # 執行or運算
cv2.imshow("Forest", src)
cv2.imshow("Not Forest", dst)

cv2.waitKey()
cv2.destroyAllWindows()  # 刪除所有視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch08\ch8_17.py

# ch8_17.py
import cv2
import numpy as np

src1 = cv2.imread("forest.jpg")  # 讀取影像
src2 = np.zeros(src1.shape, np.uint8)

src2[:, 120:360, :] = 255  # 建立mask白色區塊
dst = cv2.bitwise_xor(src1, src2)  # 執行xor運算
cv2.imshow("Forest", src1)  # forest.jpg
cv2.imshow("Mask", src2)  # mask
cv2.imshow("Forest xor operation", dst)  # 結果

cv2.waitKey()
cv2.destroyAllWindows()  # 刪除所有視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch08\ch8_18.py

# ch8_18.py
import cv2
import numpy as np

src = cv2.imread("forest.jpg")  # 讀取影像
key = np.random.randint(0, 256, src.shape, np.uint8)  # 密鑰影像
print(src.shape)
cv2.imshow("forest", src)  # 原始影像
cv2.imshow("key", key)  # 密鑰影像

img_encry = cv2.bitwise_xor(src, key)  # 加密結果的影像
img_decry = cv2.bitwise_xor(key, img_encry)  # 解密結果的影像
cv2.imshow("encrytion", img_encry)  # 加密結果影像
cv2.imshow("decrytion", img_decry)  # 解密結果影像

cv2.waitKey()
cv2.destroyAllWindows()  # 刪除所有視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch08\ch8_2.py

# ch8_2.py
import cv2
import numpy as np

img = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)  # 灰色讀取
res = cv2.add(img, img)
cv2.imshow("MyPicture1", img)  # 顯示影像img
cv2.imshow("MyPicture2", res)  # 顯示影像res

cv2.waitKey(0)  # 等待
cv2.destroyAllWindows()  # 刪除所有視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch08\ch8_3.py

# ch8_3.py
import cv2
import numpy as np

img = cv2.imread("jk.jpg")  # 彩色讀取
res = cv2.add(img, img)  # 調整亮度結果
cv2.imshow("MyPicture1", img)  # 顯示影像img
cv2.imshow("MyPicture2", res)  # 顯示影像res

cv2.waitKey(0)  # 等待
cv2.destroyAllWindows()  # 刪除所有視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch08\ch8_3_1.py

# ch8_3_1.py
import cv2
import numpy as np

value = 20  # 亮度調整值
img = cv2.imread("jk.jpg")  # 彩色讀取
coff = np.ones(img.shape, dtype=np.uint8) * value

res = cv2.add(img, coff)  # 調整亮度結果
cv2.imshow("MyPicture1", img)  # 顯示影像img
cv2.imshow("MyPicture2", res)  # 顯示影像res

cv2.waitKey(0)  # 等待
cv2.destroyAllWindows()  # 刪除所有視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch08\ch8_4.py

# ch8_4.py
import cv2
import numpy as np

src1 = np.random.randint(0, 256, size=[3, 3], dtype=np.uint8)
src2 = np.random.randint(0, 256, size=[3, 3], dtype=np.uint8)
res = src1 + src2
print(f"src1 = \n {src1}")
print(f"src2 = \n {src2}")
print(f"dst = \n {src1+src2}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch08\ch8_5.py

# ch8_5.py
import cv2
import numpy as np

img = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)  # 灰色讀取
res1 = cv2.add(img, img)
res2 = img + img
cv2.imshow("MyPicture1", img)  # 顯示影像img
cv2.imshow("MyPicture2", res1)  # 顯示影像res1
cv2.imshow("MyPicture3", res2)  # 顯示影像res2

cv2.waitKey(0)  # 等待
cv2.destroyAllWindows()  # 刪除所有視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch08\ch8_6.py

# ch8_6.py
import cv2
import numpy as np

img = cv2.imread("jk.jpg")  # 彩色讀取
res1 = cv2.add(img, img)
res2 = img + img
cv2.imshow("MyPicture1", img)  # 顯示影像img
cv2.imshow("MyPicture2", res1)  # 顯示影像res1
cv2.imshow("MyPicture3", res2)  # 顯示影像res2

cv2.waitKey(0)  # 等待
cv2.destroyAllWindows()  # 刪除所有視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch08\ch8_7.py

# ch8_7.py
import cv2
import numpy as np

b = np.zeros((200, 250, 3), np.uint8)  # b影像
g = np.zeros((200, 250, 3), np.uint8)  # g影像
r = np.zeros((200, 250, 3), np.uint8)  # r影像
b[:, :, 0] = 255  # 設定藍色
g[:, :, 1] = 255  # 設定綠色
r[:, :, 2] = 255  # 設定紅色
cv2.imshow("B channel", b)  # 顯示影像b
cv2.imshow("G channel", g)  # 顯示影像g
cv2.imshow("R channel", r)  # 顯示影像r

img1 = cv2.add(b, g)  # b + g影像
cv2.imshow("B + G", img1)
img2 = cv2.add(g, r)  # g + r影像
cv2.imshow("G + R", img2)
img3 = cv2.add(img1, r)  # b + g + r影像
cv2.imshow("B + G + R", img3)

cv2.waitKey(0)  # 等待
cv2.destroyAllWindows()  # 刪除所有視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch08\ch8_8.py

# ch8_8.py
import cv2
import numpy as np

img1 = np.ones((4, 5), dtype=np.uint8) * 8
img2 = np.ones((4, 5), dtype=np.uint8) * 9
mask = np.zeros((4, 5), dtype=np.uint8)
mask[1:3, 1:4] = 255
dst = np.random.randint(0, 256, (4, 5), np.uint8)
print("img1 = \n", img1)
print("img2 = \n", img2)
print("mask = \n", mask)
print("最初值 dst =\n", dst)
dst = cv2.add(img1, img2, mask=mask)
print("結果值 dst =\n", dst)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch08\ch8_8_1.py

# ch8_8_1.py
import cv2
import numpy as np

img1 = np.zeros((200, 300, 3), np.uint8)  # 建立img1影像
img1[:, :, 1] = 255
cv2.imshow("img1", img1)  # 顯示影像img1
img2 = np.zeros((200, 300, 3), np.uint8)  # 建立img2影像
img2[:, :, 2] = 255
cv2.imshow("img2", img2)  # 顯示影像img2
m = np.zeros((200, 300, 1), np.uint8)  # 建立mask(m)影像
m[50:150, 100:200, :] = 255  # 建立 ROI
cv2.imshow("mask", m)  # 顯示影像m

img3 = cv2.add(img1, img2)  # 不含mask的影像相加
cv2.imshow("img1 + img2", img3)
img4 = cv2.add(img1, img2, mask=m)  # 含mask的影像相加
cv2.imshow("img1 + img2 + mask", img4)

cv2.waitKey(0)
cv2.destroyAllWindows()  # 刪除所有視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch08\ch8_9.py

# ch8_9.py
import cv2
import numpy as np

src1 = np.ones((2, 3), dtype=np.uint8) * 10  # 影像 src1
src2 = np.ones((2, 3), dtype=np.uint8) * 50  # 影像 src2
alpha = 1
beta = 0.5
gamma = 5
print(f"src1 = \n {src1}")
print(f"src2 = \n {src2}")
dst = cv2.addWeighted(src1, alpha, src2, beta, gamma)  # 加權和
print(f"dst = \n {dst}")


print("------------------------------------------------------------")  # 60個
