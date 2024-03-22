"""
cv2.medianBlur



"""

import cv2

import sys
import matplotlib.pyplot as plt
import numpy as np
import math

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示

print("------------------------------------------------------------")  # 60個


filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_noise.png"
image = cv2.imread(filename)

print("medianBlur 效果 1")
image_medianBlur = cv2.medianBlur(image, 3)

plt.figure("new23 medianBlur 效果 1", figsize=(16, 12))

plt.subplot(121)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title("medianBlur 效果 1")
plt.imshow(cv2.cvtColor(image_medianBlur, cv2.COLOR_BGR2RGB))

plt.show()


print("------------------------------------------------------------")  # 60個


print("median 跑一陣子")


def get_median(data):
    data.sort()
    half = len(data) // 2
    return data[half]


# 計算灰度圖像的中值濾波
def my_median_blur_gray(image, size):
    data = []
    sizepart = int(size / 2)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            for ii in range(size):
                for jj in range(size):
                    # 首先判斷所以是否超出范圍，也可以事先對圖像進行零填充
                    if (i + ii - sizepart) < 0 or (i + ii - sizepart) >= image.shape[0]:
                        pass
                    elif (j + jj - sizepart) < 0 or (j + jj - sizepart) >= image.shape[
                        1
                    ]:
                        pass
                    else:
                        data.append(image[i + ii - sizepart][j + jj - sizepart])
            # 取每個區域內的中位數
            image[i][j] = int(get_median(data))
            data = []
    return image


# 計算彩色圖像的中值濾波
def my_median_blur_RGB(image, size):
    (b, r, g) = cv2.split(image)
    blur_b = my_median_blur_gray(b, size)
    blur_r = my_median_blur_gray(r, size)
    blur_g = my_median_blur_gray(g, size)
    result = cv2.merge((blur_b, blur_r, blur_g))
    return result


image_test1 = cv2.imread("data/worm.jpg")
# 調用自定義函數
my_image_blur_median = my_median_blur_RGB(image_test1, 5)
# 調用庫函數
computer_image_blur_median = cv2.medianBlur(image_test1, 5)
fig = plt.figure("new41")
fig.add_subplot(131)
plt.title("原圖")
plt.imshow(image_test1)
fig.add_subplot(132)
plt.title("自定義函數濾波")
plt.imshow(my_image_blur_median)
fig.add_subplot(133)
plt.title("庫函數濾波")
plt.imshow(computer_image_blur_median)
plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
