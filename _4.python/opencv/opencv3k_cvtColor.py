"""
Color Space Conversions

RGB、灰階、HLS、HSV 轉換

會用到的轉換

BGR轉RGB

BGR轉GRAY
BGR轉BGRA
BGR轉HSV
HSV轉BGR
BGR轉Lab
"""

from opencv_common import *

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/barbara.bmp"

print("------------------------------------------------------------")  # 60個

print("圖片色彩空間的轉換")

image1 = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

plt.figure(
    num="",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(231)
plt.title("未轉換 BGR")
plt.imshow(image1)

image2 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)

plt.subplot(232)
plt.title("BGR轉RGB")
plt.imshow(image2)


image3 = cv2.cvtColor(image1, cv2.COLOR_BGR2Lab)

plt.subplot(233)
plt.title("BGR轉LAB")
plt.imshow(image3)

plt.subplot(234)
plt.imshow(cv2.cvtColor(image3, cv2.COLOR_BGR2RGB))
plt.title("BGR轉LAB再轉RGB")


plt.show()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
