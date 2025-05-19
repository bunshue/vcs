# ch4_1.py
import cv2

img = cv2.imread("view.jpg")  # BGR 讀取
cv2.imshow("view.jpg", img)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # BGR 轉 RBG
cv2.imshow("RGB Color Space", img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch04\ch4_10.py

# ch4_10.py
import cv2

image = cv2.imread("street.jpg")
blue, green, red = cv2.split(image)
bgr_image = cv2.merge([blue, green, red])  # 依據 B G R 順序合併
cv2.imshow("B -> G -> R ", bgr_image)

rgb_image = cv2.merge([red, green, blue])  # 依據 R G B 順序合併
cv2.imshow("R -> G -> B ", rgb_image)

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch04\ch4_11.py

# ch4_11.py
import cv2

image = cv2.imread("street.jpg")
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

hue, saturation, value = cv2.split(hsv_image)
hsv_image = cv2.merge([hue, saturation, value])  # 依據 H S V 順序合併

cv2.imshow("The Image", image)
cv2.imshow("The Merge Image", hsv_image)

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch04\ch4_12.py

# ch4_12.py
import cv2

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch04\ch4_12_1.py

# ch4_12_1.py
import cv2

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch04\ch4_13.py

# ch4_13.py
import cv2

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch04\ch4_14.py

# ch4_14.py
import cv2

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch04\ch4_15.py

# ch4_15.py
import cv2

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch04\ch4_2.py

# ch4_2.py
import cv2

img = cv2.imread("view.jpg")  # BGR讀取
cv2.imshow("view.jpg", img)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # BGR轉RBG
cv2.imshow("RGB Color Space", img_rgb)
img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)  # RGB轉BGR
cv2.imshow("BGR Color Space", img_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch04\ch4_3.py

# ch4_3.py
import cv2

img = cv2.imread("view.jpg")  # BGR讀取
cv2.imshow("view.jpg", img)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # BGR轉RBG
cv2.imshow("RGB Color Space", img_rgb)
img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB)  # RGB轉BGR
cv2.imshow("BGR Color Space", img_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch04\ch4_4.py

# ch4_4.py
import cv2

img = cv2.imread("jk.jpg")  # BGR讀取
cv2.imshow("BGR Color Space", img)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # BGR轉GRAY
cv2.imshow("GRAY Color Space", img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch04\ch4_5.py

# ch4_5.py
import cv2

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch04\ch4_6.py

# ch4_6.py
import cv2

img = cv2.imread("mountain.jpg")  # BGR讀取
cv2.imshow("BGR Color Space", img)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # BGR轉HSV
cv2.imshow("HSV Color Space", img_hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch04\ch4_7.py

# ch4_7.py
import cv2

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch04\ch4_8.py

# ch4_8.py
import cv2

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch04\ch4_8_1.py

# ch4_8_1.py
import cv2

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch04\ch4_9.py

# ch4_9.py
import cv2

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
