import sys
import cv2
import numpy as np
import time

print("------------------------------------------------------------")  # 60個

# ch1_1.py

img1 = cv2.imread("jk.jpg")  # 讀取影像
print(f"成功讀取 : {type(img1)}")
img2 = cv2.imread("none.jpg")  # 讀取影像
print(f"讀取失敗 : {type(img2)}")

print("------------------------------------------------------------")  # 60個

# ch1_2.py

img = cv2.imread("jk.jpg")  # 讀取影像
cv2.imshow("MyPicture", img)  # 顯示影像

print("------------------------------------------------------------")  # 60個

# ch1_3.py

img = cv2.imread("jk.jpg")  # 讀取影像
cv2.imshow("MyPicture", img)  # 顯示影像
cv2.destroyWindow("MyPicture")  # 關閉視窗

print("------------------------------------------------------------")  # 60個

# ch1_4.py

img = cv2.imread("jk.jpg")  # 讀取影像
cv2.imshow("MyPicture", img)  # 顯示影像
ret_value = cv2.waitKey(0)  # 無限等待
cv2.destroyWindow("MyPicture")  # 關閉視窗

print("------------------------------------------------------------")  # 60個

# ch1_5.py

img = cv2.imread("jk.jpg")  # 讀取影像
cv2.imshow("MyPicture", img)  # 顯示影像
ret_value = cv2.waitKey(5000)  # 等待 5 秒
cv2.destroyWindow("MyPicture")  # 關閉視窗
print(f"ret_value = {ret_value}")

print("------------------------------------------------------------")  # 60個

# ch1_5_1.py

img = cv2.imread("jk.jpg")  # 讀取影像
cv2.imshow("MyPicture", img)  # 顯示影像
ret_value = cv2.waitKey(0)  # 無限等待
if ret_value == ord("Q") or ret_value == ord("q"):
    cv2.destroyWindow("MyPicture")  # 關閉視窗

print("------------------------------------------------------------")  # 60個

# ch1_6.py

cv2.namedWindow("MyPicture1")  # 使用預設
cv2.namedWindow("MyPicture2", cv2.WINDOW_NORMAL)  # 可以調整大小
img1 = cv2.imread("jk.jpg")  # 彩色讀取
img2 = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)  # 灰色讀取
cv2.imshow("MyPicture1", img1)  # 顯示影像img1
cv2.imshow("MyPicture2", img2)  # 顯示影像img2
cv2.waitKey(3000)  # 等待3秒
cv2.destroyWindow("MyPicture1")  # 刪除MyPicture1
cv2.waitKey(8000)  # 等待8秒
cv2.destroyAllWindows()  # 刪除所有視窗

print("------------------------------------------------------------")  # 60個

# ch1_6_1.py

cv2.namedWindow("MyPicture1")  # 使用預設
cv2.namedWindow("MyPicture2", cv2.WINDOW_NORMAL)  # 可以調整大小
img1 = cv2.imread("jk.jpg")  # 彩色讀取
img2 = cv2.imread("jk.jpg", 0)  # 灰色讀取
cv2.imshow("MyPicture1", img1)  # 顯示影像img1
cv2.imshow("MyPicture2", img2)  # 顯示影像img2
cv2.waitKey(3000)  # 等待3秒
cv2.destroyWindow("MyPicture1")  # 刪除MyPicture1
cv2.waitKey(8000)  # 等待8秒
cv2.destroyAllWindows()  # 刪除所有視窗

print("------------------------------------------------------------")  # 60個

# ch1_7.py

cv2.namedWindow("MyPicture")  # 使用預設
img = cv2.imread("jk.jpg")  # 彩色讀取
cv2.imshow("MyPicture", img)  # 顯示影像img
ret = cv2.imwrite("tmp_out1_7_1.tiff", img)  # 將檔案寫入out1_7_1.tiff
if ret:
    print("儲存檔案成功")
else:
    print("儲存檔案失敗")
ret = cv2.imwrite("tmp_out1_7_2.png", img)  # 將檔案寫入out1_7_2.png
if ret:
    print("儲存檔案成功")
else:
    print("儲存檔案失敗")
cv2.waitKey(3000)  # 等待3秒
cv2.destroyAllWindows()  # 刪除所有視窗

print("------------------------------------------------------------")  # 60個

# ch2_1.py

img = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)  # 灰階讀取
print("列印灰階影像的屬性")
print(f"shape = {img.shape}")
print(f"size  = {img.size}")
print(f"dtype = {img.dtype}")

print("------------------------------------------------------------")  # 60個

# ch2_2.py

img = cv2.imread("jk.jpg")  # 彩色讀取
print("列印彩色影像的屬性")
print(f"shape = {img.shape}")
print(f"size  = {img.size}")
print(f"dtype = {img.dtype}")

print("------------------------------------------------------------")  # 60個

# ch2_3.py

pt_y = 169
pt_x = 118
img = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)  # 灰階讀取
px = img[pt_y, pt_x]  # 讀px點
print(type(px))
print(f"BGR = {px}")

print("------------------------------------------------------------")  # 60個

# ch2_4.py

pt_y = 169
pt_x = 118
img = cv2.imread("jk.jpg")  # 彩色讀取
px = img[pt_y, pt_x]  # 讀px點
print(type(px))
print(f"BGR = {px}")

print("------------------------------------------------------------")  # 60個

# ch2_5.py

pt_y = 169
pt_x = 118
img = cv2.imread("jk.jpg")  # 彩色讀取
blue = img[pt_y, pt_x, 0]  # 讀 B 通道值
green = img[pt_y, pt_x, 1]  # 讀 G 通道值
red = img[pt_y, pt_x, 2]  # 讀 R 通道值
print(f"BGR = {blue}, {green}, {red}")

print("------------------------------------------------------------")  # 60個

# ch2_6.py

pt_y = 169
pt_x = 118
img = cv2.imread("jk.jpg")  # 彩色讀取
px = img[pt_y, pt_x]  # 讀取 px 點
print(f"更改前BGR = {px}")
px = [255, 255, 255]  # 修改 px 點
print(f"更改後BGR = {px}")

print("------------------------------------------------------------")  # 60個

# ch2_7.py

img = cv2.imread("jk.jpg")  # 彩色讀取
cv2.imshow("Before the change", img)
for y in range(img.shape[0] - 50, img.shape[0]):
    for x in range(img.shape[1] - 50, img.shape[1]):
        img[y, x] = [255, 255, 255]
cv2.imshow("After the change", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch3_1.py

row1 = [1, 2, 3]
arr1 = np.array(row1, ndmin=2)
print(f"陣列維度 = {arr1.ndim}")
print(f"陣列外型 = {arr1.shape}")
print(f"陣列大小 = {arr1.size}")
print("陣列內容")
print(arr1)
print("-" * 70)
row2 = [4, 5, 6]
arr2 = np.array([row1, row2], ndmin=2)
print(f"陣列維度 = {arr2.ndim}")
print(f"陣列外型 = {arr2.shape}")
print(f"陣列大小 = {arr2.size}")
print("陣列內容")
print(arr2)

print("------------------------------------------------------------")  # 60個

# ch3_2.py

x = np.array([[1, 2, 3], [4, 5, 6]])
print(f"陣列維度 = {x.ndim}")
print(f"陣列外型 = {x.shape}")
print(f"陣列大小 = {x.size}")
print("陣列內容")
print(x)

print("------------------------------------------------------------")  # 60個

# ch3_3.py

x = np.array([[1, 2, 3], [4, 5, 6]])
print(x[0][2])
print(x[1][2])
# 或是
print(x[0, 2])
print(x[1, 2])

print("------------------------------------------------------------")  # 60個

# ch3_4.py

x1 = np.zeros(3)
print(x1)
print("-" * 70)
x2 = np.zeros((2, 3), dtype=np.uint8)
print(x2)

print("------------------------------------------------------------")  # 60個

# ch3_4_1.py
fig = np.zeros((50, 200), dtype=np.uint8)
print(fig)
cv2.imshow("fig", fig)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch3_5.py

x1 = np.ones(3)
print(x1)
print("-" * 70)
x2 = np.ones((2, 3), dtype=np.uint8)
print(x2)

print("------------------------------------------------------------")  # 60個

# ch3_5_1.py

fig = np.ones((50, 200), dtype=np.uint8) * 255
print(fig)
cv2.imshow("fig", fig)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch3_6.py

x1 = np.empty(3)
print(x1)
print("-" * 70)
x2 = np.empty((2, 3), dtype=np.uint8)
print(x2)

print("------------------------------------------------------------")  # 60個

# ch3_7.py

x1 = np.random.randint(10, 20)
print("回傳值是10(含)至20(不含)的單一隨機數")
print(x1)
print("-" * 70)
print("回傳一維陣列10個元素, 值是1(含)至5(不含)的隨機數")
x2 = np.random.randint(1, 5, 10)
print(x2)
print("-" * 70)
print("回傳單3*5陣列, 值是0(含)至10(不含)的隨機數")
x3 = np.random.randint(10, size=(3, 5))
print(x3)

print("------------------------------------------------------------")  # 60個

# ch3_7_3.py

x = np.arange(16)
print(x)
print(np.reshape(x, (4, -1)))


print("------------------------------------------------------------")  # 60個

# ch3_7_4.py

x = np.arange(16)
print(x)
print(np.reshape(x, (-1, 8)))

print("------------------------------------------------------------")  # 60個

# ch3_8.py

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(f"陣列元素如下 : {x} ")
print(f"x[2:]       = {x[2:]}")
print(f"x[:2]       = {x[:3]}")
print(f"x[0:3]      = {x[0:3]}")
print(f"x[1:4]      = {x[1:4]}")
print(f"x[0:9:2]    = {x[0:9:2]}")
print(f"x[-1]       = {x[-1]}")
print(f"x[::2]      = {x[::2]}")
print(f"x[2::3]     = {x[2::3]}")
print(f"x[:]        = {x[:]}")
print(f"x[::]       = {x[::]}")
print(f"x[-3:-7:-1] = {x[-3:-7:-1]}")

print("------------------------------------------------------------")  # 60個

# ch3_9.py

x1 = np.array([0, 1, 2, 3, 4, 5])
x2 = np.array(x1, copy=True)
print(x1)
print(x2)
print("-" * 70)
x2[0] = 9
print(x1)
print(x2)

print("------------------------------------------------------------")  # 60個

# ch3_10.py

x1 = np.array([0, 1, 2, 3, 4, 5])
x2 = x1.copy()
print(x1)
print(x2)
print("-" * 70)
x2[0] = 9
print(x1)
print(x2)

print("------------------------------------------------------------")  # 60個

# ch3_11.py

x1 = [0, 1, 2, 3, 4]
x2 = [5, 6, 7, 8, 9]
x3 = [10, 11, 12, 13, 14]
x4 = np.array([x1, x2, x3])
print(x4)

print("------------------------------------------------------------")  # 60個

# ch3_12.py

x1 = [0, 1, 2, 3, 4]
x2 = [5, 6, 7, 8, 9]
x3 = [10, 11, 12, 13, 14]
x4 = np.array([x1, x2, x3])
x5 = np.array([x4, x4])
print(x5)

print("------------------------------------------------------------")  # 60個

# ch3_13.py

x1 = [0, 1, 2, 3, 4]
x2 = [5, 6, 7, 8, 9]
x3 = [10, 11, 12, 13, 14]
x4 = np.array([x1, x2, x3])
print(f"x4[2][1] = {x4[2][1]}")
print(f"x4[1][3] = {x4[1][3]}")

print("------------------------------------------------------------")  # 60個

# ch3_13_1.py

x1 = [0, 1, 2, 3, 4]
x2 = [5, 6, 7, 8, 9]
x3 = [10, 11, 12, 13, 14]
x4 = np.array([x1, x2, x3])
print(f"x4[2,1] = {x4[2,1]}")
print(f"x4[1,3] = {x4[1,3]}")

print("------------------------------------------------------------")  # 60個

# ch3_14.py

x1 = [0, 1, 2, 3, 4]
x2 = [5, 6, 7, 8, 9]
x3 = [10, 11, 12, 13, 14]
x4 = np.array([x1, x2, x3])
x5 = np.array([x4, x4])
print(f"x5[0][2][1] = {x5[0][2][1]}")
print(f"x5[0][1][3] = {x5[0][1][3]}")
print(f"x5[1][0][1] = {x5[1][0][1]}")
print(f"x5[1][1][4] = {x5[1][1][4]}")

print("------------------------------------------------------------")  # 60個

# ch3_14_1.py

x1 = [0, 1, 2, 3, 4]
x2 = [5, 6, 7, 8, 9]
x3 = [10, 11, 12, 13, 14]
x4 = np.array([x1, x2, x3])
x5 = np.array([x4, x4])
print(f"x5[0,2,1] = {x5[0,2,1]}")
print(f"x5[0,1,3] = {x5[0,1,3]}")
print(f"x5[1,0,1] = {x5[1,0,1]}")
print(f"x5[1,1,4] = {x5[1,1,4]}")

print("------------------------------------------------------------")  # 60個

# ch3_15.py

x1 = [0, 1, 2, 3, 4]
x2 = [5, 6, 7, 8, 9]
x3 = [10, 11, 12, 13, 14]
x = np.array([x1, x2, x3])
print("x[:,:]   = 結果是二維陣列")  # 結果是二維陣列
print(x[:, :])
print("-" * 70)
print("x[2,:4]  = 結果是一維陣列")  # 結果是一維陣列
print(x[2, :4])
print("-" * 70)
print("x[:2,:1] = 結果是二維陣列")  # 結果是二維陣列
print(x[:2, :1])
print("-" * 70)
print("x[:,4:]  =  結果是二維陣列")  # 結果是二維陣列
print(x[:, 4:])
print("-" * 70)
print("x[:,4]   =  結果是一維陣列")  # 結果是一維陣列
print(x[:, 4])

print("------------------------------------------------------------")  # 60個

# ch3_16.py

x1 = [0, 1, 2, 3, 4]
x2 = [5, 6, 7, 8, 9]
x3 = [10, 11, 12, 13, 14]
x = np.array([x1, x2, x3])
print("x[:2,4]  = 結果是一維陣列")  # 結果是一維陣列
print(x[:2, 4])
print("-" * 70)
print("x[:2][4] = 結果是錯誤")  # 結果是錯誤
print(x[:2][4])

print("------------------------------------------------------------")  # 60個

# ch3_17.py

x1 = np.arange(4).reshape(2, 2)
print(f"陣列 1 \n{x1}")
x2 = np.arange(4, 8).reshape(2, 2)
print(f"陣列 2 \n{x2}")
x = np.vstack((x1, x2))
print(f"合併結果 \n{x}")

print("------------------------------------------------------------")  # 60個

# ch3_18.py

x1 = np.arange(4).reshape(2, 2)
print(f"陣列 1 \n{x1}")
x2 = np.arange(4, 8).reshape(2, 2)
print(f"陣列 2 \n{x2}")
x = np.hstack((x1, x2))
print(f"合併結果 \n{x}")

print("------------------------------------------------------------")  # 60個

# ch4_1.py

img = cv2.imread("view.jpg")  # BGR 讀取
cv2.imshow("view.jpg", img)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # BGR 轉 RBG
cv2.imshow("RGB Color Space", img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch4_2.py

img = cv2.imread("view.jpg")  # BGR讀取
cv2.imshow("view.jpg", img)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # BGR轉RBG
cv2.imshow("RGB Color Space", img_rgb)
img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)  # RGB轉BGR
cv2.imshow("BGR Color Space", img_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch4_3.py

img = cv2.imread("view.jpg")  # BGR讀取
cv2.imshow("view.jpg", img)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # BGR轉RBG
cv2.imshow("RGB Color Space", img_rgb)
img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB)  # RGB轉BGR
cv2.imshow("BGR Color Space", img_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch4_4.py

img = cv2.imread("jk.jpg")  # BGR讀取
cv2.imshow("BGR Color Space", img)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # BGR轉GRAY
cv2.imshow("GRAY Color Space", img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch4_5.py

pt_x = 169
pt_y = 118
img = cv2.imread("jk.jpg")  # BGR讀取
# BGR彩色轉成灰階GRAY
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("GRAY Color Space", img_gray)
px = img_gray[pt_x, pt_y]
print(f"Gray Color 通道值 = {px}")

# 灰階GRAY轉成BGR彩色
img_color = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR)
cv2.imshow("BGR Color Space", img_gray)
px = img_color[pt_x, pt_y]
print(f"BGR Color  通道值 = {px}")

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch4_6.py

img = cv2.imread("mountain.jpg")  # BGR讀取
cv2.imshow("BGR Color Space", img)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # BGR轉HSV
cv2.imshow("HSV Color Space", img_hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch4_7.py

image = cv2.imread("colorbar.jpg")
cv2.imshow("bgr", image)
blue, green, red = cv2.split(image)
cv2.imshow("blue", blue)
cv2.imshow("green", green)
cv2.imshow("red", red)

print(f"B通道影像屬性 shape = {blue.shape}")
print("列印B通道內容")
print(blue)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch4_8.py

image = cv2.imread("mountain.jpg")
cv2.imshow("bgr", image)
blue, green, red = cv2.split(image)
cv2.imshow("blue", blue)
cv2.imshow("green", green)
cv2.imshow("red", red)

print(f"BGR  影像 : {image.shape}")
print(f"B通道影像 : {blue.shape}")
print(f"G通道影像 : {green.shape}")
print(f"R通道影像 : {red.shape}")

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch4_8_1.py

image = cv2.imread("mountain.jpg")
cv2.imshow("bgr", image)
blue, green, red = cv2.split(image)
cv2.imshow("blue", blue)
cv2.imshow("green", green)
cv2.imshow("red", red)

print(f"BGR  影像 : {image.shape}")
print("B通道內容 : ")
print(blue)
print("G通道內容 : ")
print(green)
print("R通道內容 : ")
print(red)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch4_9.py

image = cv2.imread("mountain.jpg")
cv2.imshow("bgr", image)

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
hue, saturation, value = cv2.split(hsv_image)
cv2.imshow("hsv", hue)
cv2.imshow("saturation", saturation)
cv2.imshow("value", value)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch4_10.py

image = cv2.imread("street.jpg")
blue, green, red = cv2.split(image)
bgr_image = cv2.merge([blue, green, red])  # 依據 B G R 順序合併
cv2.imshow("B -> G -> R ", bgr_image)

rgb_image = cv2.merge([red, green, blue])  # 依據 R G B 順序合併
cv2.imshow("R -> G -> B ", rgb_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch4_11.py

image = cv2.imread("street.jpg")
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

hue, saturation, value = cv2.split(hsv_image)
hsv_image = cv2.merge([hue, saturation, value])  # 依據 H S V 順序合併

cv2.imshow("The Image", image)
cv2.imshow("The Merge Image", hsv_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch4_12.py

image = cv2.imread("street.jpg")
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

hsv, saturation, value = cv2.split(hsv_image)
hsv[:, :] = 200  # 修訂 hsv 內容
hsv_image = cv2.merge([hsv, saturation, value])  # 依據H S V順序合併
new_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)  # HSV 轉 BGR

cv2.imshow("The Image", image)
cv2.imshow("The New Image", new_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch4_12_1.py

image = cv2.imread("street.jpg")
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

hsv, saturation, value = cv2.split(hsv_image)
hsv.fill(200)  # 修訂 hsv 內容
hsv_image = cv2.merge([hsv, saturation, value])  # 依據H S V順序合併
new_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)  # HSV 轉 BGR

cv2.imshow("The Image", image)
cv2.imshow("The New Image", new_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch4_13.py

image = cv2.imread("street.jpg")
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

hsv, saturation, value = cv2.split(hsv_image)
saturation.fill(255)  # 修訂 hsv 內容
hsv_image = cv2.merge([hsv, saturation, value])  # 依據H S V順序合併
new_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)  # HSV 轉 BGR

cv2.imshow("The Image", image)
cv2.imshow("The New Image", new_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch4_14.py

image = cv2.imread("street.jpg")
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

hsv, saturation, value = cv2.split(hsv_image)
value.fill(255)  # 修訂 value 內容
hsv_image = cv2.merge([hsv, saturation, value])  # 依據H S V順序合併
new_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)  # HSV 轉 BGR

cv2.imshow("The Image", image)
cv2.imshow("The New Image", new_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch4_15.py

image = cv2.imread("street.jpg")
cv2.imshow("The Image", image)  # 顯示BGR影像

bgra_image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
b, g, r, a = cv2.split(bgra_image)
print("列出轉成含A通道影像物件後的alpha值")
print(a)

a[:, :] = 32  # 修訂alpha內容
a32_image = cv2.merge([b, g, r, a])  # alpha=32影像物件
cv2.imshow("The a32 Image", a32_image)  # 顯示alpha=32影像

a.fill(128)  # 修訂alpha內容
a128_image = cv2.merge([b, g, r, a])  # alpha=128影像物件
cv2.imshow("The a128 Image", a128_image)  # 顯示alpha=128影像

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("a32.png", a32_image)  # 儲存alpha=32影像
cv2.imwrite("a128.png", a128_image)  # 儲存alpha=128影像

print("------------------------------------------------------------")  # 60個

# ch5_1.py

height = 160  # 影像高
width = 280  # 影像寬
# 建立GRAY影像陣列
image = np.zeros((height, width), np.uint8)
cv2.imshow("image", image)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch5_2.py

height = 160  # 影像高
width = 280  # 影像寬
# 建立GRAY影像陣列
image = np.zeros((height, width), np.uint8)
image.fill(255)  # 元素內容改為白色 255
cv2.imshow("image", image)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch5_3.py

height = 160  # 影像高
width = 280  # 影像寬
# 建立GRAY影像陣列
image = np.ones((height, width), np.uint8) * 255
cv2.imshow("image", image)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch5_4.py

height = 160  # 影像高
width = 280  # 影像寬
# 建立GRAY影像陣列
image = np.zeros((height, width), np.uint8)
image[40:120, 70:210] = 255  # 高在40至120之間,寬在70至210之間,設為255
cv2.imshow("image", image)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch5_5.py

height = 160  # 影像高
width = 280  # 影像寬
# 建立GRAY影像陣列
image = np.zeros((height, width), np.uint8)
for y in range(0, height, 20):
    image[y : y + 10, :] = 255  # 白色厚度是10
cv2.imshow("image", image)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch5_6.py

height = 160  # 影像高
width = 280  # 影像寬
# 使用random.randint()建立GRAY影像陣列
image = np.random.randint(256, size=[height, width], dtype=np.uint8)
cv2.imshow("image", image)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch5_7.py

height = 160  # 影像高
width = 280  # 影像寬
# 建立BGR影像陣列
image = np.zeros((height, width, 3), np.uint8)
image[:, :, 0] = 255  # 建立 B 通道像素值
cv2.imshow("image", image)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch5_8.py

height = 160  # 影像高
width = 280  # 影像寬
# 建立BGR影像陣列
image = np.zeros((height, width, 3), np.uint8)
blue_image = image.copy()
blue_image[:, :, 0] = 255  # 建立 B 通道像素值
cv2.imshow("blue image", blue_image)  # 顯示blue image影像

green_image = image.copy()
green_image[:, :, 1] = 255  # 建立 G 通道像素值
cv2.imshow("green image", green_image)  # 顯示green image影像

red_image = image.copy()
red_image[:, :, 2] = 255  # 建立 R 通道像素值
cv2.imshow("red image", red_image)  # 顯示red image影像

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch5_9.py

height = 160  # 影像高
width = 280  # 影像寬
# 使用random.randint()建立GRAY影像陣列
image = np.random.randint(256, size=[height, width, 3], dtype=np.uint8)
cv2.imshow("image", image)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch5_10.py

height = 150  # 影像高
width = 300  # 影像寬
image = np.zeros((height, width, 3), np.uint8)
image[0:50, :, 0] = 255  # blue
image[50:100, :, 1] = 255  # green
image[100:150, :, 2] = 255  # red
cv2.imshow("image", image)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch6_1.py

# 建立GRAY影像陣列
image = np.zeros((5, 12), np.uint8)
print(f"修改前 image=\n{image}")  # 顯示修改前GRAY影像
print(f"image[1,4] = {image[1, 4]}")  # 列出特定像素點的內容

image[1, 4] = 255  # 修改像素點的內容
print(f"修改後 image=\n{image}")  # 顯示修改後的GRAY影像
print(f"image[1,4] = {image[1, 4]}")  # 列出特定像素點的內容

print("------------------------------------------------------------")  # 60個

# ch6_2.py

img = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)  # 灰色讀取
cv2.imshow("Before modify", img)  # 顯示修改前影像img
for y in range(120, 140):  # 修改影像
    for x in range(110, 210):
        img[y, x] = 255
cv2.imshow("After modify", img)  # 顯示修改後影像img

cv2.waitKey(0)
cv2.destroyAllWindows()  # 刪除所有視窗

print("------------------------------------------------------------")  # 60個

# ch6_3.py

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

# ch6_4.py

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

# ch6_5.py

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

# ch6_6.py

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

# ch6_7.py

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

# ch6_7_1.py

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

# ch6_8.py

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

# ch6_8_1.py

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

# ch6_9.py

image = np.random.randint(0, 200, size=[3, 5], dtype=np.uint8)
print(f"image = \n{image}")
print(f"修改前image.item(1,3) = {image.item(1,3)}")
image.itemset((1, 3), 255)  # 修訂內容為 255
print("-" * 70)
print(f"修改後image =\n{image}")
print(f"修改後image.item(1,3) = {image.item(1,3)}")

print("------------------------------------------------------------")  # 60個

# ch6_10.py

img = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)  # 灰色讀取
cv2.imshow("Before modify", img)  # 顯示修改前影像img
for y in range(120, 140):  # 修改影像
    for x in range(110, 210):
        img.itemset((y, x), 255)
cv2.imshow("After modify", img)  # 顯示修改後影像img

cv2.waitKey(0)
cv2.destroyAllWindows()  # 刪除所有視窗

print("------------------------------------------------------------")  # 60個

# ch6_11.py

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

# ch6_12.py

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

# ch6_13.py
img = cv2.imread("jk.jpg")  # 彩色讀取
cv2.imshow("Hung Image", img)  # 顯示影像
face = img[30:220, 80:250]  # ROI
cv2.imshow("Face", face)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()  # 刪除所有視窗

print("------------------------------------------------------------")  # 60個

# ch6_14.py

img = cv2.imread("jk.jpg")  # 彩色讀取
cv2.imshow("Hung Image", img)  # 顯示影像
# ROI大小區塊建立馬賽克
face = np.random.randint(0, 256, size=(190, 170, 3))  # 馬賽克效果
img[30:220, 80:250] = face  # ROI
cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()  # 刪除所有視窗

print("------------------------------------------------------------")  # 60個

# ch6_15.py

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

# ch7_1.py
img = np.ones((350, 500, 3), np.uint8) * 255  # 建立白色底的畫布
cv2.line(img, (1, 1), (300, 1), (255, 0, 0))  # 上方水平直線
cv2.line(img, (300, 1), (300, 300), (255, 0, 0))  # 右邊垂直直線
cv2.line(img, (300, 300), (1, 300), (255, 0, 0))  # 下邊水平直線
cv2.line(img, (1, 300), (1, 1), (255, 0, 0))  # 左邊垂直直線
cv2.imshow("My Draw", img)  # 畫布顯示直線

cv2.waitKey(0)
cv2.destroyAllWindows()  # 刪除所有視窗

print("------------------------------------------------------------")  # 60個

# ch7_2.py

img = np.ones((350, 500, 3), np.uint8) * 255  # 建立白色底的畫布
cv2.line(img, (1, 1), (300, 1), (255, 0, 0))  # 上方水平直線
cv2.line(img, (300, 1), (300, 300), (255, 0, 0))  # 右邊垂直直線
cv2.line(img, (300, 300), (1, 300), (255, 0, 0))  # 下邊水平直線
cv2.line(img, (1, 300), (1, 1), (255, 0, 0))  # 左邊垂直直線
for x in range(150, 300, 10):
    cv2.line(img, (x, 1), (300, x - 150), (255, 0, 0))
for y in range(150, 300, 10):
    cv2.line(img, (1, y), (y - 150, 300), (255, 0, 0))

cv2.imshow("My Draw", img)  # 畫布顯示結果
cv2.waitKey(0)
cv2.destroyAllWindows()  # 刪除所有視窗

print("------------------------------------------------------------")  # 60個

# ch7_3.py

img = np.ones((350, 500, 3), np.uint8) * 255  # 建立白色底的畫布
img[1:300, 1:300] = (0, 255, 255)  # 設定黃色底

cv2.line(img, (1, 1), (300, 1), (255, 0, 0))  # 上方水平直線
cv2.line(img, (300, 1), (300, 300), (255, 0, 0))  # 右邊垂直直線
cv2.line(img, (300, 300), (1, 300), (255, 0, 0))  # 下邊水平直線
cv2.line(img, (1, 300), (1, 1), (255, 0, 0))  # 左邊垂直直線
for x in range(150, 300, 10):
    cv2.line(img, (x, 1), (300, x - 150), (255, 0, 0))
for y in range(150, 300, 10):
    cv2.line(img, (1, y), (y - 150, 300), (255, 0, 0))

cv2.imshow("My Draw", img)  # 畫布顯示結果
cv2.waitKey(0)
cv2.destroyAllWindows()  # 刪除所有視窗

print("------------------------------------------------------------")  # 60個

# ch7_4.py

img = cv2.imread("antarctic.jpg")  # 使用影像當畫布
img[1:300, 1:300] = (0, 255, 255)  # 設定黃色底

cv2.line(img, (1, 1), (300, 1), (255, 0, 0))  # 上方水平直線
cv2.line(img, (300, 1), (300, 300), (255, 0, 0))  # 右邊垂直直線
cv2.line(img, (300, 300), (1, 300), (255, 0, 0))  # 下邊水平直線
cv2.line(img, (1, 300), (1, 1), (255, 0, 0))  # 左邊垂直直線
for x in range(150, 300, 10):
    cv2.line(img, (x, 1), (300, x - 150), (255, 0, 0))
for y in range(150, 300, 10):
    cv2.line(img, (1, y), (y - 150, 300), (255, 0, 0))

cv2.imshow("My Draw", img)  # 畫布顯示結果
cv2.waitKey(0)
cv2.destroyAllWindows()  # 刪除所有視窗

print("------------------------------------------------------------")  # 60個

# ch7_5.py

img = np.ones((350, 500, 3), np.uint8) * 255  # 建立白色底的畫布
cv2.rectangle(img, (1, 1), (300, 300), (255, 0, 0))  # 繪製矩形
for x in range(150, 300, 10):
    cv2.line(img, (x, 1), (300, x - 150), (255, 0, 0))
for y in range(150, 300, 10):
    cv2.line(img, (1, y), (y - 150, 300), (255, 0, 0))

cv2.imshow("My Draw", img)  # 畫布顯示結果
cv2.waitKey(0)
cv2.destroyAllWindows()  # 刪除所有視窗

print("------------------------------------------------------------")  # 60個

# ch7_6.py

img = np.ones((350, 500, 3), np.uint8) * 255  # 建立白色底的畫布
cv2.rectangle(img, (1, 1), (300, 300), (0, 255, 255), -1)  # 設定黃色底
cv2.rectangle(img, (1, 1), (300, 300), (255, 0, 0))  # 繪製矩形
for x in range(150, 300, 10):
    cv2.line(img, (x, 1), (300, x - 150), (255, 0, 0))
for y in range(150, 300, 10):
    cv2.line(img, (1, y), (y - 150, 300), (255, 0, 0))

cv2.imshow("My Draw", img)  # 畫布顯示結果
cv2.waitKey(0)
cv2.destroyAllWindows()  # 刪除所有視窗

print("------------------------------------------------------------")  # 60個

# ch7_7.py

img = cv2.imread("antarctic.jpg")  # 使用影像當畫布
cy = int(img.shape[0] / 2)  # 中心點 y 座標
cx = int(img.shape[1] / 2)  # 中心點 x 座標
red = (0, 0, 255)  # 設定紅色
yellow = (0, 255, 255)  # 設定黃色
cv2.circle(img, (cx, cy), 30, red, -1)  # 繪製實心圓形
for r in range(40, 200, 20):  # 繪製系列空心圓形
    cv2.circle(img, (cx, cy), r, yellow, 2)

cv2.imshow("My Draw", img)  # 畫布顯示結果
cv2.waitKey(0)
cv2.destroyAllWindows()  # 刪除所有視窗

print("------------------------------------------------------------")  # 60個

# ch7_10.py

height = 400  # 畫布高度
width = 600  # 畫布寬度
img = np.zeros((height, width, 3), np.uint8)  # 建立黑底畫布陣列
for i in range(0, 50):
    cx = np.random.randint(0, width)  # 隨機數圓心的 x 軸座標
    cy = np.random.randint(0, height)  # 隨機數圓心的 y 軸座標
    color = np.random.randint(0, 256, size=3).tolist()  # 建立隨機色彩
    r = np.random.randint(5, 100)  # 在5 - 100間的隨機半徑
    cv2.circle(img, (cx, cy), r, color, -1)  # 建立隨機實心圓
cv2.imshow("Random Circle", img)

cv2.waitKey(0)
cv2.destroyAllWindows()  # 刪除所有視窗


print("------------------------------------------------------------")  # 60個

# ch7_11.py

img = cv2.imread("antarctic.jpg")  # 使用影像當畫布
cy = int(img.shape[0] / 2)  # 中心點 y 座標
cx = int(img.shape[1] / 2)  # 中心點 x 座標
red = (0, 0, 255)  # 設定紅色
yellow = (0, 255, 255)  # 設定黃色
blue = (255, 0, 0)  # 設定藍色
size = (200, 100)
angle = 0
cv2.ellipse(img, (cx, cy), size, angle, 0, 360, red, 1)  # 繪製橢圓形
angle = 45
cv2.ellipse(img, (cx, cy), size, angle, 0, 360, yellow, 5)  # 繪製橢圓形
cv2.ellipse(img, (cx, cy), size, angle, 45, 135, blue, 3)  # 繪製橢圓弧

cv2.imshow("My Draw", img)  # 畫布顯示結果
cv2.waitKey(0)
cv2.destroyAllWindows()  # 刪除所有視窗

print("------------------------------------------------------------")  # 60個

# ch7_12.py

img = cv2.imread("antarctic.jpg")  # 使用影像當畫布
cy = int(img.shape[0] / 2)  # 中心點 y 座標
cx = int(img.shape[1] / 2)  # 中心點 x 座標
size = (200, 100)  # 橢圓的x,y軸長度
for i in range(0, 15):
    angle = np.random.randint(0, 361)  # 橢圓偏移的角度
    color = np.random.randint(0, 256, size=3).tolist()  # 橢圓的隨機色彩
    cv2.ellipse(img, (cx, cy), size, angle, 0, 360, color, 1)  # 繪製橢圓形

cv2.imshow("My Draw", img)  # 畫布顯示結果
cv2.waitKey(0)
cv2.destroyAllWindows()  # 刪除所有視窗

print("------------------------------------------------------------")  # 60個

# ch7_13.py

img1 = np.ones((200, 300, 3), np.uint8) * 255  # 畫布1
pts = np.array([[150, 50], [250, 100], [150, 150], [50, 100]])  # 頂點陣列
cv2.polylines(img1, [pts], True, (255, 0, 0), 5)  # 繪製封閉式多邊形

img2 = np.ones((200, 300, 3), np.uint8) * 255  # 畫布2
cv2.polylines(img2, [pts], False, (0, 0, 255), 3)  # 繪製開放式多邊形

cv2.imshow("isClosed_True", img1)  # 畫布顯示封閉式多邊形
cv2.imshow("isClosed_False", img2)  # 畫布顯示開放式多邊形
cv2.waitKey(0)
cv2.destroyAllWindows()  # 刪除所有視窗

print("------------------------------------------------------------")  # 60個

# ch7_14.py

img = np.ones((300, 600, 3), np.uint8) * 255  # 畫布
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "Python", (150, 180), font, 3, (255, 0, 0), 12)

cv2.imshow("Python", img)  # 畫布顯示文字
cv2.waitKey(0)
cv2.destroyAllWindows()  # 刪除所有視窗

print("------------------------------------------------------------")  # 60個

# ch7_15.py

img = np.ones((300, 600, 3), np.uint8) * 255  # 畫布
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "Python", (150, 180), font, 3, (255, 0, 0), 12)
cv2.putText(img, "Python", (150, 180), font, 3, (0, 255, 255), 5)

cv2.imshow("Python", img)  # 畫布顯示文字
cv2.waitKey(0)
cv2.destroyAllWindows()  # 刪除所有視窗

print("------------------------------------------------------------")  # 60個

# ch7_16.py

img = np.ones((300, 600, 3), np.uint8) * 255  # 畫布
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "Python", (120, 120), font, 3, (255, 0, 0), 12)
cv2.putText(img, "Python", (120, 180), font, 3, (0, 255, 0), 12, cv2.LINE_8, True)

cv2.imshow("Python", img)  # 畫布顯示文字
cv2.waitKey(0)
cv2.destroyAllWindows()  # 刪除所有視窗

print("------------------------------------------------------------")  # 60個

# ch7_17.py

img = cv2.imread("antarctic.jpg")
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "Antarctic", (120, 120), font, 3, (255, 0, 0), 12)

cv2.imshow("Antarctic", img)
cv2.waitKey(0)
cv2.destroyAllWindows()  # 刪除所有視窗

print("------------------------------------------------------------")  # 60個

# ch7_17_1.py

from PIL import Image, ImageDraw, ImageFont


def cv2_Chinese_Text(img, text, left, top, textColor, fontSize):
    """建立中文字輸出"""
    # 影像轉成 PIL影像格式
    if isinstance(img, np.ndarray):
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img)  # 建立PIL繪圖物件
    fontText = ImageFont.truetype(  # 建立字型 - 新細明體
        "C:\Windows\Fonts\mingliu.ttc", fontSize, encoding="utf-8"  # 新細明體  # 字型大小
    )  # 編碼方式
    draw.text((left, top), text, textColor, font=fontText)  # 繪製中文字
    # 將PIL影像格式轉成OpenCV影像格式
    return cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)


img = cv2.imread("antarctic.jpg")
img = cv2_Chinese_Text(img, "我在南極", 220, 100, (0, 0, 255), 50)

cv2.imshow("Antarctic", img)
cv2.waitKey(0)
cv2.destroyAllWindows()  # 刪除所有視窗

print("------------------------------------------------------------")  # 60個

# ch7_18.py
from random import *

width = 640  # 反彈球畫布寬度
height = 480  # 反彈球畫布高度
r = 15  # 反彈球半徑
speed = 0.01  # 反彈球移動速度
x = int(width / 2) - r  # 反彈球的最初 x 位置
y = 50  # 反彈球的最初 y 位置
y_step = 5  # 反彈球移動 y 步伐

while cv2.waitKey(1) == -1:
    if y > height - r or y < r:  # 反彈球超出畫布下邊界或是上邊界
        y_step = -y_step
    y += y_step  # 新的反彈球 y 位置
    img = np.ones((height, width, 3), np.uint8) * 255
    cv2.circle(img, (x, y), r, (255, 0, 0), -1)  # 繪製反彈球
    cv2.imshow("Bouncing Ball", img)
    time.sleep(speed)  # 依speed設定休息

cv2.destroyAllWindows()  # 刪除所有視窗

print("------------------------------------------------------------")  # 60個

# ch7_19.py
from random import *

width = 640  # 反彈球畫布寬度
height = 480  # 反彈球畫布高度
r = 15  # 反彈球半徑
speed = 0.01  # 反彈球移動速度
x = 50  # 反彈球的最初 x 位置
y = 50  # 反彈球的最初 y 位置
x_step = 5  # 反彈球移動 x 步伐
y_step = 5  # 反彈球移動 y 步伐

while cv2.waitKey(1) == -1:
    if x > width - r or x < r:  # 反彈球超出畫布右邊界或是左邊界
        x_step = -x_step
    if y > height - r or y < r:  # 反彈球超出畫布下邊界或是上邊界
        y_step = -y_step
    x += x_step  # 新的反彈球 x 位置
    y += y_step  # 新的反彈球 y 位置
    img = np.ones((height, width, 3), np.uint8) * 255
    cv2.circle(img, (x, y), r, (255, 0, 0), -1)  # 繪製反彈球
    cv2.imshow("Bouncing Ball", img)
    time.sleep(speed)  # 依speed設定休息

cv2.destroyAllWindows()  # 刪除所有視窗

print("------------------------------------------------------------")  # 60個

# ch7_20.py
from random import *

width = 640  # 反彈球畫布寬度
height = 480  # 反彈球畫布高度
r = 15  # 反彈球半徑
speed = 0.01  # 反彈球移動速度
x = 50  # 反彈球的最初 x 位置
y = 50  # 反彈球的最初 y 位置
random_step = [3, 4, 5, 6, 7]  # x 步伐串列
shuffle(random_step)  # 隨機產生 x 步伐串列
x_step = random_step[0]  # 反彈球移動 x 步伐
y_step = 5  # 反彈球移動 y 步伐

while cv2.waitKey(1) == -1:
    if x > width - r or x < r:  # 反彈球超出畫布右邊界或是左邊界
        x_step = -x_step
    if y > height - r or y < r:  # 反彈球超出畫布下邊界或是上邊界
        y_step = -y_step
    x += x_step  # 新的反彈球 x 位置
    y += y_step  # 新的反彈球 y 位置
    img = np.ones((height, width, 3), np.uint8) * 255
    cv2.circle(img, (x, y), r, (255, 0, 0), -1)  # 繪製反彈球
    cv2.imshow("Bouncing Ball", img)
    time.sleep(speed)  # 依speed設定休息

cv2.destroyAllWindows()  # 刪除所有視窗

print("------------------------------------------------------------")  # 60個

# ch7_21.py

events = [i for i in dir(cv2) if "EVENT" in i]
for e in events:
    print(e)

print("------------------------------------------------------------")  # 60個

# ch7_22.py


def OnMouseAction(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  # 按一下滑鼠左鍵
        print(f"在x={x}, y={y}, 按一下滑鼠左鍵")
    elif event == cv2.EVENT_RBUTTONDOWN:  # 按一下滑鼠右鍵
        print(f"在x={x}, y={y}, 按一下滑鼠右鍵_")
    elif event == cv2.EVENT_MBUTTONDOWN:  # 按一下滑鼠中間鍵
        print(f"在x={x}, y={y}, 按一下滑鼠中間鍵")
    elif flags == cv2.EVENT_FLAG_LBUTTON:  # 按住滑鼠左鍵拖曳
        print(f"在x={x}, y={y}, 按住滑鼠左鍵拖曳")
    elif flags == cv2.EVENT_FLAG_RBUTTON:  # 按住滑鼠右鍵拖曳
        print(f"在x={x}, y={y}, 按住滑鼠右鍵拖曳")


image = np.ones((200, 300, 3), np.uint8) * 255
cv2.namedWindow("OpenCV Mouse Event")
cv2.setMouseCallback("OpenCV Mouse Event", OnMouseAction)
cv2.imshow("OpenCV Mouse Event", image)

cv2.waitKey(0)
cv2.destroyAllWindows()  # 刪除所有視窗

print("------------------------------------------------------------")  # 60個

# ch7_23.py


def OnMouseAction(event, x, y, flags, param):
    # color可以產生隨機色彩
    color = np.random.randint(0, high=256, size=3).tolist()
    r = np.random.randint(10, 50)  # 隨機10-50半徑的圓
    if event == cv2.EVENT_LBUTTONDOWN:  # 按一下滑鼠左鍵
        cv2.circle(image, (x, y), r, color, -1)  # 隨機的實心圓
    elif event == cv2.EVENT_RBUTTONDOWN:  # 按一下滑鼠右鍵
        cv2.circle(image, (x, y), r, color, 3)  # 隨機的空心圓


height = 400  # 視窗高度
width = 600  # 視窗寬度
image = np.ones((height, width, 3), np.uint8) * 255
cv2.namedWindow("Draw Circle")
cv2.setMouseCallback("Draw Circle", OnMouseAction)
while 1:
    cv2.imshow("Draw Circle", image)
    key = cv2.waitKey(100)  # 0.1秒檢查一次
    if key == ord("Q") or key == ord("q"):  # Q或q則結束
        break

cv2.destroyAllWindows()  # 刪除所有視窗

print("------------------------------------------------------------")  # 60個

# ch7_24.py


def OnMouseAction(event, x, y, flags, param):
    # color可以產生隨機色彩
    color = np.random.randint(0, high=256, size=3).tolist()
    if event == cv2.EVENT_LBUTTONDOWN:  # 按一下滑鼠左鍵
        r = np.random.randint(10, 50)  # 隨機10-50半徑的圓
        if key == ord("s"):
            cv2.circle(image, (x, y), r, color, -1)  # 隨機的實心圓
        else:
            cv2.circle(image, (x, y), r, color, 3)  # 隨機的線寬是 3 的圓
    elif event == cv2.EVENT_RBUTTONDOWN:  # 按一下滑鼠右鍵
        px = np.random.randint(10, 100)
        py = np.random.randint(10, 100)
        if key == ord("s"):
            cv2.rectangle(image, (x, y), (px, py), color, -1)  # 實心矩形
        else:
            cv2.rectangle(image, (x, y), (px, py), color, 3)  # 空心矩形


height = 400  # 視窗高度
width = 600  # 視窗寬度
image = np.ones((height, width, 3), np.uint8) * 255
cv2.namedWindow("MyDraw")
cv2.setMouseCallback("MyDraw", OnMouseAction)
while 1:
    cv2.imshow("MyDraw", image)
    key = cv2.waitKey(100)  # 0.1秒檢查一次
    if key == ord("Q") or key == ord("q"):  # Q或q則結束
        break

cv2.destroyAllWindows()  # 刪除所有視窗

print("------------------------------------------------------------")  # 60個

# ch7_25.py


def onChange(x):
    b = cv2.getTrackbarPos("B", "canvas")  # 建立B通道顏色
    g = cv2.getTrackbarPos("G", "canvas")  # 建立G通道顏色
    r = cv2.getTrackbarPos("R", "canvas")  # 建立R通道顏色
    canvas[:] = [b, g, r]  # 設定背景色


canvas = np.ones((200, 640, 3), np.uint8) * 255  # 寬640,高200
cv2.namedWindow("canvas")
cv2.createTrackbar("B", "canvas", 0, 255, onChange)  # 藍色通道控制
cv2.createTrackbar("G", "canvas", 0, 255, onChange)  # 綠色通道控制
cv2.createTrackbar("R", "canvas", 0, 255, onChange)  # 紅色通道控制
while 1:
    cv2.imshow("canvas", canvas)
    key = cv2.waitKey(100)  # 0.1秒檢查一次
    if key == 27:  # Esc 則結束
        break

cv2.destroyAllWindows()  # 刪除所有視窗

print("------------------------------------------------------------")  # 60個

# ch7_26.py


def onChange(x):
    pass


def OnMouseAction(event, x, y, flags, param):
    # color可以產生隨機色彩
    color = np.random.randint(0, high=256, size=3).tolist()
    r = np.random.randint(10, 50)  # 隨機10-50半徑的圓
    if event == cv2.EVENT_LBUTTONDOWN:  # 按一下滑鼠左鍵
        cv2.circle(image, (x, y), r, color, thickness)  # 隨機的圓


thickness = -1  # 預設寬度是 0
height = 400  # 視窗高度
width = 600  # 視窗寬度
image = np.ones((height, width, 3), np.uint8) * 255
cv2.namedWindow("Draw Circle")
cv2.setMouseCallback("Draw Circle", OnMouseAction)
cv2.createTrackbar("Thickness", "Draw Circle", 0, 1, onChange)
while 1:
    cv2.imshow("Draw Circle", image)
    key = cv2.waitKey(100)  # 0.1秒檢查一次
    num = cv2.getTrackbarPos("Thickness", "Draw Circle")
    if num == 0:
        thickness = -1  # 實心設定
    else:
        thickness = 3  # 寬度是 3
    if key == ord("Q") or key == ord("q"):  # Q或q則結束
        break
cv2.destroyAllWindows()  # 刪除所有視窗

print("------------------------------------------------------------")  # 60個

# ch8_1.py

src1 = np.random.randint(0, 256, size=[3, 3], dtype=np.uint8)
src2 = np.random.randint(0, 256, size=[3, 3], dtype=np.uint8)
res = cv2.add(src1, src2)
print(f"src1 = \n {src1}")
print(f"src2 = \n {src2}")
print(f"dst = \n {src1+src2}")

print("------------------------------------------------------------")  # 60個

# ch8_2.py

img = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)  # 灰色讀取
res = cv2.add(img, img)
cv2.imshow("MyPicture1", img)  # 顯示影像img
cv2.imshow("MyPicture2", res)  # 顯示影像res

cv2.waitKey(0)  # 等待
cv2.destroyAllWindows()  # 刪除所有視窗

print("------------------------------------------------------------")  # 60個

# ch8_3.py

img = cv2.imread("jk.jpg")  # 彩色讀取
res = cv2.add(img, img)  # 調整亮度結果
cv2.imshow("MyPicture1", img)  # 顯示影像img
cv2.imshow("MyPicture2", res)  # 顯示影像res

cv2.waitKey(0)  # 等待
cv2.destroyAllWindows()  # 刪除所有視窗

print("------------------------------------------------------------")  # 60個

# ch8_3_1.py

value = 20  # 亮度調整值
img = cv2.imread("jk.jpg")  # 彩色讀取
coff = np.ones(img.shape, dtype=np.uint8) * value

res = cv2.add(img, coff)  # 調整亮度結果
cv2.imshow("MyPicture1", img)  # 顯示影像img
cv2.imshow("MyPicture2", res)  # 顯示影像res

cv2.waitKey(0)  # 等待
cv2.destroyAllWindows()  # 刪除所有視窗

print("------------------------------------------------------------")  # 60個

# ch8_4.py

src1 = np.random.randint(0, 256, size=[3, 3], dtype=np.uint8)
src2 = np.random.randint(0, 256, size=[3, 3], dtype=np.uint8)
res = src1 + src2
print(f"src1 = \n {src1}")
print(f"src2 = \n {src2}")
print(f"dst = \n {src1+src2}")

print("------------------------------------------------------------")  # 60個

# ch8_5.py

img = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)  # 灰色讀取
res1 = cv2.add(img, img)
res2 = img + img
cv2.imshow("MyPicture1", img)  # 顯示影像img
cv2.imshow("MyPicture2", res1)  # 顯示影像res1
cv2.imshow("MyPicture3", res2)  # 顯示影像res2

cv2.waitKey(0)  # 等待
cv2.destroyAllWindows()  # 刪除所有視窗

print("------------------------------------------------------------")  # 60個

# ch8_6.py

img = cv2.imread("jk.jpg")  # 彩色讀取
res1 = cv2.add(img, img)
res2 = img + img
cv2.imshow("MyPicture1", img)  # 顯示影像img
cv2.imshow("MyPicture2", res1)  # 顯示影像res1
cv2.imshow("MyPicture3", res2)  # 顯示影像res2

cv2.waitKey(0)  # 等待
cv2.destroyAllWindows()  # 刪除所有視窗

print("------------------------------------------------------------")  # 60個

# ch8_7.py

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

# ch8_8.py

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

# ch8_8_1.py

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

# ch8_9.py

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

# ch8_10.py

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

# ch8_11.py

src1 = np.random.randint(0, 255, (3, 5), dtype=np.uint8)
src2 = np.zeros((3, 5), dtype=np.uint8)
src2[0:2, 0:2] = 255
dst = cv2.bitwise_and(src1, src2)
print(f"src1 = \n {src1}")
print(f"src2 = \n {src2}")
print(f"dst = \n {dst}")

print("------------------------------------------------------------")  # 60個

# ch8_12.py

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

# ch8_13.py

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

# ch8_14.py

src1 = np.random.randint(0, 255, (3, 5), dtype=np.uint8)
src2 = np.zeros((3, 5), dtype=np.uint8)
src2[0:2, 0:2] = 255
dst = cv2.bitwise_or(src1, src2)
print(f"src1 = \n {src1}")
print(f"src2 = \n {src2}")
print(f"dst = \n {dst}")

print("------------------------------------------------------------")  # 60個

# ch8_15.py

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

# ch8_16.py

src = cv2.imread("forest.jpg")  # 讀取影像
dst = cv2.bitwise_not(src)  # 執行or運算
cv2.imshow("Forest", src)
cv2.imshow("Not Forest", dst)

cv2.waitKey()
cv2.destroyAllWindows()  # 刪除所有視窗

print("------------------------------------------------------------")  # 60個

# ch8_17.py

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

# ch8_18.py

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

# ch9_1.py

thresh = 127  # 定義閾值
maxval = 255  # 定義像素最大值
src = np.random.randint(0, 256, size=[3, 5], dtype=np.uint8)
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY)
print(f"src =\n {src}")
print(f"threshold = {ret}")
print(f"dst =\n {dst}")

print("------------------------------------------------------------")  # 60個

# ch9_2.py

thresh = 127  # 定義閾值
maxval = 255  # 定義像素最大值
src = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY)
cv2.imshow("Src", src)
cv2.imshow("Dst - 127", dst)  # threshold = 127
thresh = 80  # 修訂所定義的閾值
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY)
cv2.imshow("Dst - 80", dst)  # threshold = 80

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch9_3.py

thresh = 127  # 定義閾值
maxval = 255  # 定義像素最大值
src = cv2.imread("jk.jpg")
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY)
cv2.imshow("Src", src)
cv2.imshow("Dst - 127", dst)  # threshold = 127
thresh = 80  # 修訂所定義的閾值
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY)
cv2.imshow("Dst - 80", dst)  # threshold = 80

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch9_4.py

src = cv2.imread("numbers.jpg")
thresh = 127  # 閾值 = 10
maxval = 255  # 二值化的極大值
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY)
cv2.imshow("Src", src)
cv2.imshow("Dst - 127", dst)  # threshold = 127
thresh = 10  # 更改閾值 = 10
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY)
cv2.imshow("Dst - 10", dst)  # threshold = 10

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch9_5.py

thresh = 127  # 定義閾值
maxval = 255  # 定義像素最大值
src = np.random.randint(0, 256, size=[3, 5], dtype=np.uint8)
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY_INV)
print(f"src =\n {src}")
print(f"threshold = {ret}")
print(f"dst =\n {dst}")

print("------------------------------------------------------------")  # 60個

# ch9_6.py

thresh = 127  # 定義閾值
maxval = 255  # 定義像素最大值
src = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY_INV)
cv2.imshow("Src", src)
cv2.imshow("Dst - 127", dst)  # threshold = 127
thresh = 80  # 修訂所定義的閾值
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY_INV)
cv2.imshow("Dst - 80", dst)  # threshold = 80

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch9_7.py

thresh = 127  # 定義閾值
maxval = 255  # 定義像素最大值
src = cv2.imread("jk.jpg")
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY_INV)
cv2.imshow("Src", src)
cv2.imshow("Dst - 127", dst)  # threshold = 127
thresh = 80  # 修訂所定義的閾值
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY_INV)
cv2.imshow("Dst - 80", dst)  # threshold = 80

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch9_8.py

src = cv2.imread("numbers.jpg")
thresh = 127  # 閾值 = 10
maxval = 255  # 二值化的極大值
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY_INV)
cv2.imshow("Src", src)
cv2.imshow("Dst - 127", dst)  # threshold = 127
thresh = 10  # 更改閾值 = 10
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY_INV)
cv2.imshow("Dst - 10", dst)  # threshold = 10

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch9_9.py

thresh = 127  # 定義閾值
maxval = 255  # 定義像素最大值
src = np.random.randint(0, 256, size=[3, 5], dtype=np.uint8)
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_TRUNC)
print(f"src =\n {src}")
print(f"threshold = {ret}")
print(f"dst =\n {dst}")

print("------------------------------------------------------------")  # 60個

# ch9_10.py

thresh = 127  # 定義閾值
maxval = 255  # 定義像素最大值
src = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_TRUNC)
cv2.imshow("Src", src)
cv2.imshow("Dst - 127", dst)  # threshold = 127
thresh = 80  # 修訂所定義的閾值
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_TRUNC)
cv2.imshow("Dst - 80", dst)  # threshold = 80

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch9_11.py

thresh = 127  # 定義閾值
maxval = 255  # 定義像素最大值
src = cv2.imread("jk.jpg")
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_TRUNC)
cv2.imshow("Src", src)
cv2.imshow("Dst - 127", dst)  # threshold = 127
thresh = 80  # 修訂所定義的閾值
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_TRUNC)
cv2.imshow("Dst - 80", dst)  # threshold = 80

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch9_12.py

thresh = 127  # 定義閾值
maxval = 255  # 定義像素最大值
src = np.random.randint(0, 256, size=[3, 5], dtype=np.uint8)
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_TOZERO)
print(f"src =\n {src}")
print(f"threshold = {ret}")
print(f"dst =\n {dst}")

print("------------------------------------------------------------")  # 60個

# ch9_13.py

thresh = 127  # 定義閾值
maxval = 255  # 定義像素最大值
src = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_TOZERO)
cv2.imshow("Src", src)
cv2.imshow("Dst - 127", dst)  # threshold = 127
thresh = 80  # 修訂所定義的閾值
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_TOZERO)
cv2.imshow("Dst - 80", dst)  # threshold = 80

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch9_14.py

thresh = 127  # 定義閾值
maxval = 255  # 定義像素最大值
src = cv2.imread("jk.jpg")
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_TOZERO)
cv2.imshow("Src", src)
cv2.imshow("Dst - 127", dst)  # threshold = 127
thresh = 80  # 修訂所定義的閾值
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_TOZERO)
cv2.imshow("Dst - 80", dst)  # threshold = 80

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch9_15.py

thresh = 127  # 定義閾值
maxval = 255  # 定義像素最大值
src = np.random.randint(0, 256, size=[3, 5], dtype=np.uint8)
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_TOZERO_INV)
print(f"src =\n {src}")
print(f"threshold = {ret}")
print(f"dst =\n {dst}")

print("------------------------------------------------------------")  # 60個

# ch9_16.py

thresh = 127  # 定義閾值
maxval = 255  # 定義像素最大值
src = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_TOZERO_INV)
cv2.imshow("Src", src)
cv2.imshow("Dst - 127", dst)  # threshold = 127
thresh = 80  # 修訂所定義的閾值
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_TOZERO_INV)
cv2.imshow("Dst - 80", dst)  # threshold = 80

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch9_17.py

thresh = 127  # 定義閾值
maxval = 255  # 定義像素最大值
src = cv2.imread("jk.jpg")
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_TOZERO_INV)
cv2.imshow("Src", src)
cv2.imshow("Dst - 127", dst)  # threshold = 127
thresh = 80  # 修訂所定義的閾值
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_TOZERO_INV)
cv2.imshow("Dst - 80", dst)  # threshold = 80

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch9_18.py

thresh = 127  # 定義閾值
maxval = 255  # 定義像素最大值
src = np.ones((3, 4), dtype=np.uint8) * 120  # 設定陣列是 120
src[0:2, 0:2] = 108  # 設定陣列區間為 0
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY)
print(f"src =\n {src}")
print(f"threshold = {ret}")
print(f"dst =\n {dst}")

print("------------------------------------------------------------")  # 60個

# ch9_19.py

thresh = 0  # 定義閾值
maxval = 255  # 定義像素最大值
src = np.ones((3, 4), dtype=np.uint8) * 120  # 設定陣列是 120
src[0:2, 0:2] = 108  # 設定陣列區間為 0
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
print(f"src =\n {src}")
print(f"threshold = {ret}")
print(f"dst =\n {dst}")

print("------------------------------------------------------------")  # 60個

# ch9_20.py

src = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Src", src)
thresh = 127  # 定義閾值 = 127
maxval = 255  # 定義像素最大值
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY)
cv2.imshow("Src - 127", dst)  # threshold = 127
thresh = 0  # 定義閾值 = 0
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("Dst - Otsu", dst)  # Otsu
print(f"threshold = {ret}")

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch9_21.py

src = cv2.imread("school.jpg", cv2.IMREAD_GRAYSCALE)  # 灰階讀取
thresh = 127  # 閾值
maxval = 255  # 定義像素最大值
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理
# 自適應閾值計算方法為ADAPTIVE_THRESH_MEAN_C
dst_mean = cv2.adaptiveThreshold(
    src, maxval, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 5
)
# 自適應閾值計算方法為ADAPTIVE_THRESH_GAUSSIAN_C
dst_gauss = cv2.adaptiveThreshold(
    src, maxval, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 3, 5
)
cv2.imshow("src", src)  # 顯示原始影像
cv2.imshow("THRESH_BINARY", dst)  # 顯示二值化處理影像
cv2.imshow("ADAPTIVE_THRESH_MEAN_C", dst_mean)  # 顯示自適應閾值結果
cv2.imshow("ADAPTIVE_THRESH_GAUSSIAN_C", dst_gauss)  # 顯示自適應閾值結果

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch9_22.py

img = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("JK Hung", img)

row, column = img.shape
x = np.zeros((row, column, 8), dtype=np.uint8)
for i in range(8):
    x[:, :, i] = 2**i  # 填上權重
result = np.zeros((row, column, 8), dtype=np.uint8)
for i in range(8):
    result[:, :, i] = cv2.bitwise_and(img, x[:, :, i])
    mask = result[:, :, i] > 0  # 影像邏輯值
    result[mask] = 255  # True的位置填255
    cv2.imshow(str(i), result[:, :, i])  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch9_23.py

jk = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("JK Hung", jk)  # 顯示原始影像

row, column = jk.shape  # 取得列高和欄寬
h7 = np.ones((row, column), dtype=np.uint8) * 254  # 建立像素值是254的影像
cv2.imshow("254", h7)  # 顯示像素值是254的影像
new_jk = cv2.bitwise_and(jk, h7)  # 原始影像最低有效位元是 0
cv2.imshow("New JK", new_jk)  # 顯示新影像

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch9_24.py

jk = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("JK Hung", jk)  # 顯示原始影像

row, column = jk.shape  # 取得列高和欄寬
h7 = np.ones((row, column), dtype=np.uint8) * 254  # 建立像素值是254的影像
tmp_jk = cv2.bitwise_and(jk, h7)  # 原始影像最低有效位元是 0
watermark = cv2.imread("copyright.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Copy Right", watermark)  # 顯示浮水印影像
ret, wm = cv2.threshold(watermark, 0, 1, cv2.THRESH_BINARY)
# 浮水印影像嵌入最低有效位元是 0的原始影像
new_jk = cv2.bitwise_or(tmp_jk, wm)
cv2.imshow("New JK", new_jk)  # 顯示新影像

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch9_25.py

jk = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("JK Hung", jk)  # 顯示原始影像

row, column = jk.shape  # 取得列高和欄寬
h7 = np.ones((row, column), dtype=np.uint8) * 254  # 建立像素值是254的影像
tmp_jk = cv2.bitwise_and(jk, h7)  # 原始影像最低有效位元是 0

watermark = cv2.imread("copyright.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("original watermark", watermark)  # 顯示浮水印影像
ret, wm = cv2.threshold(watermark, 0, 1, cv2.THRESH_BINARY)

new_jk = cv2.bitwise_or(tmp_jk, wm)  # 浮水印影像嵌入原始影像
cv2.imshow("New JK", new_jk)  # 顯示新影像
# 擷取浮水印
h0 = np.ones((row, column), dtype=np.uint8)
wm = cv2.bitwise_and(new_jk, h0)
ret, dst = cv2.threshold(wm, 0, 255, cv2.THRESH_BINARY)
cv2.imshow("result Watermark", dst)  # 顯示浮水印

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch10_1.py

src = cv2.imread("southpole.jpg")  # 讀取影像
cv2.imshow("Src", src)  # 顯示原始影像
width = 300  # 新的影像寬度
height = 200  # 新的影像高度
dsize = (width, height)
dst = cv2.resize(src, dsize)  # 重設影像大小
cv2.imshow("Dst", dst)  # 顯示新的影像

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch10_2.py

src = cv2.imread("southpole.jpg")  # 讀取影像
cv2.imshow("Src", src)  # 顯示原始影像
dst = cv2.resize(src, None, fx=0.5, fy=1.1)  # 重設影像大小
cv2.imshow("Dst", dst)  # 顯示新的影像
print(f"src.shape = {src.shape}")
print(f"dst.shape = {dst.shape}")

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch10_3.py

src = cv2.imread("python.jpg")  # 讀取影像
cv2.imshow("Src", src)  # 顯示原始影像
dst1 = cv2.flip(src, 0)  # 垂直翻轉
cv2.imshow("dst1 - Flip Vertically", dst1)  # 顯示垂直影像
dst2 = cv2.flip(src, 1)  # 水平翻轉
cv2.imshow("dst2 - Flip Horizontally", dst2)  # 顯示水平影像
dst3 = cv2.flip(src, -1)  # 水平與垂直翻轉
cv2.imshow("dst3 - Horizontally and Vertically", dst3)  # 顯示水平與垂直影像

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch10_4.py

src = cv2.imread("rural.jpg")  # 讀取影像
cv2.imshow("Src", src)  # 顯示原始影像

height, width = src.shape[0:2]  # 獲得影像大小
dsize = (width, height)  # 建立未來影像大小
x = 50  # 平移 x = 50
y = 100  # 平移 y = 100
M = np.float32([[1, 0, x], [0, 1, y]])  # 建立 M 矩陣
dst = cv2.warpAffine(src, M, dsize)  # 執行仿射
cv2.imshow("Dst", dst)  # 顯示平移結果影像

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch10_5.py

src = cv2.imread("rural.jpg")  # 讀取影像
cv2.imshow("Src", src)  # 顯示原始影像

height, width = src.shape[0:2]  # 獲得影像大小
# 逆時鐘轉 30 度
M = cv2.getRotationMatrix2D((width / 2, height / 2), 30, 1)  # 建立 M 矩陣
dsize = (width, height)  # 建立未來影像大小
dst1 = cv2.warpAffine(src, M, dsize)  # 執行仿射
cv2.imshow("Dst - counterclockwise", dst1)  # 顯示逆時鐘影像

# 順時鐘轉 30 度
M = cv2.getRotationMatrix2D((width / 2, height / 2), -30, 1)  # 建立 M 矩陣
dst = cv2.warpAffine(src, M, dsize)  # 執行仿射
cv2.imshow("Dst clockwise", dst)  # 顯示順時鐘影像

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch10_6.py

src = cv2.imread("rural.jpg")  # 讀取影像
cv2.imshow("Src", src)  # 顯示原始影像

height, width = src.shape[0:2]  # 獲得影像大小
srcp = np.float32([[0, 0], [width - 1, 0], [0, height - 1]])  # src的A,B,C三個點
dstp = np.float32([[30, 0], [width - 1, 0], [0, height - 1]])  # dst的A,B,C三個點
M = cv2.getAffineTransform(srcp, dstp)  # 建立 M 矩陣
dsize = (width, height)
dst = cv2.warpAffine(src, M, dsize)  # 執行仿射
cv2.imshow("Dst", dst)  # 顯示傾斜影像

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch10_7.py

src = cv2.imread("rural.jpg")  # 讀取影像
cv2.imshow("Src", src)  # 顯示原始影像

height, width = src.shape[0:2]  # 獲得影像大小
srcp = np.float32([[0, 0], [width - 1, 0], [0, height - 1]])  # src的A,B,C三個點
dstp = np.float32([[0, 0], [width - 1 - 30, 0], [30, height - 1]])  # dst的A,B,C三個點
M = cv2.getAffineTransform(srcp, dstp)  # 建立 M 矩陣
dsize = (width, height)
dst = cv2.warpAffine(src, M, dsize)  # 執行仿射
cv2.imshow("Dst", dst)  # 顯示傾斜影像

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch10_8.py

src = cv2.imread("rural.jpg")  # 讀取影像
cv2.imshow("Src", src)  # 顯示原始影像

height, width = src.shape[0:2]  # 獲得影像大小
srcp = np.float32([[0, 0], [width - 1, 0], [0, height - 1]])
a = [0, height * 0.2]  # A
b = [width * 0.8, height * 0.2]  # B
c = [width * 0.1, height * 0.9]  # C
dstp = np.float32([a, b, c])  # dst的 A, B, C
M = cv2.getAffineTransform(srcp, dstp)  # 建立 M 矩陣
dsize = (width, height)
dst = cv2.warpAffine(src, M, dsize)  # 執行仿射
cv2.imshow("Dst", dst)  # 顯示傾斜影像

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch10_9.py

src = cv2.imread("rural.jpg")  # 讀取影像
cv2.imshow("Src", src)  # 顯示原始影像

height, width = src.shape[0:2]  # 獲得影像大小
srcp = np.float32([[0, 0], [width - 1, 0], [0, height - 1]])
a = [0, height * 0.4]  # A
b = [width * 0.8, height * 0.2]  # B
c = [width * 0.1, height * 0.9]  # C
dstp = np.float32([a, b, c])  # dst的 A, B, C
M = cv2.getAffineTransform(srcp, dstp)  # 建立 M 矩陣
dsize = (width, height)
dst = cv2.warpAffine(src, M, dsize)  # 執行仿射
cv2.imshow("Dst", dst)  # 顯示傾斜影像

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch10_10.py

src = cv2.imread("tunnel.jpg")  # 讀取影像
cv2.imshow("Src", src)  # 顯示原始影像

height, width = src.shape[0:2]  # 獲得影像大小
a1 = [0, 0]  # 原始影像的 A
b1 = [width, 0]  # 原始影像的 B
c1 = [0, height]  # 原始影像的 C
d1 = [width - 1, height - 1]  # 原始影像的 D
srcp = np.float32([a1, b1, c1, d1])
a2 = [150, 0]  # dst的 A
b2 = [width - 150, 0]  # dst的 B
c2 = [0, height - 1]  # dst的 C
d2 = [width - 1, height - 1]  # dst的 D
dstp = np.float32([a2, b2, c2, d2])
M = cv2.getPerspectiveTransform(srcp, dstp)  # 建立 M 矩陣
dsize = (width, height)
dst = cv2.warpPerspective(src, M, dsize)  # 執行透視
cv2.imshow("Dst", dst)  # 顯示透視影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# ch10_10_1.py

src = np.random.randint(0, 256, size=[3, 4], dtype=np.uint8)
rows, cols = src.shape
mapx = np.ones(src.shape, np.float32) * 3  # 設定 mapx
mapy = np.ones(src.shape, np.float32) * 2  # 設定 mapy
dst = cv2.remap(src, mapx, mapy, cv2.INTER_LINEAR)  # 執行映射
print(f"src =\n {src}")
print(f"mapx =\n {mapx}")
print(f"mapy =\n {mapy}")
print(f"dst =\n {dst}")

print("------------------------------------------------------------")  # 60個

# ch10_11.py

src = np.random.randint(0, 256, size=[3, 5], dtype=np.uint8)
rows, cols = src.shape
mapx = np.zeros(src.shape, np.float32)
mapy = np.zeros(src.shape, np.float32)
for r in range(rows):  # 建立mapx和mapy
    for c in range(cols):
        mapx.itemset((r, c), c)  # 設定mapx
        mapy.itemset((r, c), r)  # 設定mapy
dst = cv2.remap(src, mapx, mapy, cv2.INTER_LINEAR)  # 執行映射
print(f"src =\n {src}")
print(f"mapx =\n {mapx}")
print(f"mapy =\n {mapy}")
print(f"dst =\n {dst}")

print("------------------------------------------------------------")  # 60個

# ch10_12.py

src = cv2.imread("huang.jpg")
rows, cols = src.shape[:2]
mapx = np.zeros(src.shape[:2], np.float32)
mapy = np.zeros(src.shape[:2], np.float32)
for r in range(rows):  # 建立mapx和mapy
    for c in range(cols):
        mapx.itemset((r, c), c)  # 設定mapx
        mapy.itemset((r, c), r)  # 設定mapy
dst = cv2.remap(src, mapx, mapy, cv2.INTER_LINEAR)  # 執行映射

cv2.imshow("src", src)
cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch10_13.py

src = np.random.randint(0, 256, size=[3, 5], dtype=np.uint8)
rows, cols = src.shape
mapx = np.zeros(src.shape, np.float32)
mapy = np.zeros(src.shape, np.float32)
for r in range(rows):  # 建立mapx和mapy
    for c in range(cols):
        mapx.itemset((r, c), c)  # 設定mapx
        mapy.itemset((r, c), rows - 1 - r)  # 設定mapy
dst = cv2.remap(src, mapx, mapy, cv2.INTER_LINEAR)  # 執行映射
print(f"src =\n {src}")
print(f"mapx =\n {mapx}")
print(f"mapy =\n {mapy}")
print(f"dst =\n {dst}")

print("------------------------------------------------------------")  # 60個

# ch10_14.py

src = cv2.imread("huang.jpg")
rows, cols = src.shape[:2]
mapx = np.zeros(src.shape[:2], np.float32)
mapy = np.zeros(src.shape[:2], np.float32)
for r in range(rows):  # 建立mapx和mapy
    for c in range(cols):
        mapx.itemset((r, c), c)  # 設定mapx
        mapy.itemset((r, c), rows - 1 - r)  # 設定mapy
dst = cv2.remap(src, mapx, mapy, cv2.INTER_LINEAR)  # 執行映射

cv2.imshow("src", src)
cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch10_15.py

src = np.random.randint(0, 256, size=[3, 5], dtype=np.uint8)
rows, cols = src.shape
mapx = np.zeros(src.shape, np.float32)
mapy = np.zeros(src.shape, np.float32)
for r in range(rows):  # 建立mapx和mapy
    for c in range(cols):
        mapx.itemset((r, c), cols - 1 - c)  # 設定mapx
        mapy.itemset((r, c), r)  # 設定mapy
dst = cv2.remap(src, mapx, mapy, cv2.INTER_LINEAR)  # 執行映射
print(f"src =\n {src}")
print(f"mapx =\n {mapx}")
print(f"mapy =\n {mapy}")
print(f"dst =\n {dst}")

print("------------------------------------------------------------")  # 60個

# ch10_16.py

src = cv2.imread("huang.jpg")
rows, cols = src.shape[:2]
mapx = np.zeros(src.shape[:2], np.float32)
mapy = np.zeros(src.shape[:2], np.float32)
for r in range(rows):  # 建立mapx和mapy
    for c in range(cols):
        mapx.itemset((r, c), cols - 1 - c)  # 設定mapx
        mapy.itemset((r, c), r)  # 設定mapy
dst = cv2.remap(src, mapx, mapy, cv2.INTER_LINEAR)  # 執行映射

cv2.imshow("src", src)
cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch10_17.py

src = cv2.imread("tunnel.jpg")
rows, cols = src.shape[:2]
mapx = np.zeros(src.shape[:2], np.float32)
mapy = np.zeros(src.shape[:2], np.float32)
for r in range(rows):  # 建立mapx和mapy
    for c in range(cols):
        if 0.25 * rows < r < 0.75 * rows and 0.25 * cols < c < 0.75 * cols:
            mapx.itemset((r, c), 2 * (c - cols * 0.25))  # 計算對應的 x
            mapy.itemset((r, c), 2 * (r - rows * 0.25))  # 計算對應的 y
        else:
            mapx.itemset((r, c), 0)  # 取x座標為 0
            mapy.itemset((r, c), 0)  # 取y座標為 0
dst = cv2.remap(src, mapx, mapy, cv2.INTER_LINEAR)  # 執行映射

cv2.imshow("src", src)
cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch10_18.py

src = cv2.imread("tunnel.jpg")
rows, cols = src.shape[:2]
mapx = np.zeros(src.shape[:2], np.float32)
mapy = np.zeros(src.shape[:2], np.float32)
for r in range(rows):  # 建立mapx和mapy
    for c in range(cols):
        mapx.itemset((r, c), c)
        mapy.itemset((r, c), 2 * r)
dst = cv2.remap(src, mapx, mapy, cv2.INTER_LINEAR)  # 執行映射

cv2.imshow("src", src)
cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
