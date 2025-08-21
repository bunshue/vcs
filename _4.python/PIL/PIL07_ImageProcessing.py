"""

各種影像處理

"""

print("------------------------------------------------------------")  # 60個

from PIL import Image
from PIL import ImageFilter

filename2 = "C:/_git/vcs/_1.data/______test_files1/elephant.jpg"
filename_lena_color =  "C:/_git/vcs/_4.python/_data/lena_color.jpg"
filename_lena_gray = "C:/_git/vcs/_4.python/_data/lena_gray.jpg"

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

"""
調用numpy中的array（）函數就可以將PIL對象轉換為數組對象。
如果是RGB圖片，那么轉換為array之後，就變成了一個rows*cols*channels的三維矩陣,因此，我們可以使用
image[i,j,k]
來訪問像素值。
例：打開圖片，並隨機添加一些椒鹽噪聲
"""

# 檔案 => PIL影像 => numpy陣列
image = np.array(Image.open(filename2))

# 隨機生成5000個椒鹽
rows, cols, dims = image.shape
for i in range(5000):
    x = np.random.randint(0, rows)
    y = np.random.randint(0, cols)
    image[x, y, :] = 255

plt.imshow(image)
plt.title("椒鹽效果")
plt.show()

print("------------------------------------------------------------")  # 60個

print("將圖像二值化，像素值大于 threshold 的變為1，否則變為0")

# 檔案 => PIL影像 => 灰階 => numpy陣列
image = np.array(Image.open(filename2).convert("L"))

print("圖像二值化, 要灰階圖像")

threshold = 128

rows, cols = image.shape
for i in range(rows):
    for j in range(cols):
        if image[i, j] <= threshold:
            image[i, j] = 0
        else:
            image[i, j] = 1

plt.imshow(image, cmap="gray")
plt.title("二值化, threshold =" + str(threshold))
plt.show()

"""
如果要對多個像素點進行操作，可以使用數組切片方式訪問。切片方式返回的是以指定間隔下標訪問 該數組的像素值。下面是有關灰度圖像的一些例子：

image[i,:] = im[j,:] # 將第 j 行的數值賦值給第 i 行
image[:,i] = 100 # 將第 i 列的所有數值設為 100
image[:100,:50].sum() # 計算前 100 行、前 50 列所有數值的和
image[50:100,50:100] # 50~100 行，50~100 列（不包括第 100 行和第 100 列）
image[i].mean() # 第 i 行所有數值的平均值
image[:,-1] # 最後一列
image[-2,:] (or im[-2]) # 倒數第二行
"""
print("------------------------------------------------------------")  # 60個

print("偽色彩圖像處理")

# filename = 'C:/_git/vcs/_1.data/______test_files1/pic_256X100.png'
# filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
filename_lena_gray = (
    "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"
)

# 檔案 => PIL影像
image = Image.open(filename_lena_gray)

# 彩色轉黑白
# 轉換為灰度圖像
# PIL影像 => 灰階
gray_image = image.convert("L")

# 3. 偽色彩處理

# 偽色彩處理可以通過將灰度值映射到彩色值來實現。通常，我們使用一個顏色映射表（Color Map）來定義灰度和彩色之間的映射關系。
# 在Python中，可以使用matplotlib庫來生成顏色映射表並將灰度圖像轉換為彩色圖像。

# 定義顏色映射表
cmap = plt.get_cmap("jet")

# 將灰度圖像轉換為彩色圖像
# 灰階 => numpy陣列 => cmap
color_image = cmap(np.array(gray_image))

# 顯示彩色圖像
plt.imshow(color_image)
plt.title("偽色彩")

plt.show()

# 上述代碼中，我們使用get_cmap方法獲取了一個名為’jet’的顏色映射表。然後，將灰度圖像轉換為NumPy數組，再將數組應用于顏色映射表，得到彩色圖像。

print("------------------------------------------------------------")  # 60個

# 檔案 => PIL影像
image0 = Image.open(filename2)

# PIL影像 => 灰階
image0 = image0.convert("L")

# 灰階 => numpy陣列
image1 = np.array(image0)

print("原圖 灰階最小值 :", int(image1.min()), ", 灰階最大值 :", int(image1.max()))

image2 = 255 - image1  # 對圖像進行反向處理
print("反相 灰階最小值 :", int(image2.min()), ", 灰階最大值 :", int(image2.max()))

image3 = (100.0 / 255) * image1 + 100  # 將圖像像素值變換到100...200區間
print("壓縮到100~200 灰階最小值 :", int(image3.min()), ", 灰階最大值 :", int(image3.max()))

image4 = 255.0 * (image1 / 255.0) ** 2  # 對像素值求平方後得到的圖像
print("相素值平方 灰階最小值 :", int(image4.min()), ", 灰階最大值 :", int(image4.max()))

plt.figure(
    num="影像處理2",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.gray()  # 不使用顏色信息, 將圖像以灰階方式顯示

plt.subplot(221)
plt.imshow(image0)
plt.title("原圖轉灰階")

plt.subplot(222)
plt.imshow(image2)
plt.title(r"反相 $f(x)=255-x$")

plt.subplot(223)
plt.imshow(image3)
plt.title(r"壓縮到100~200 $f(x)=\frac{100}{255}x+100$")

plt.subplot(224)
plt.imshow(image4)
plt.title(r"相素值平方 $f(x)=255(\frac{x}{255})^2$")

plt.show()

print("------------------------------------------------------------")  # 60個

print("PIL_mean")

# PIL影像.getpixel 取得該點之像素值
# PIL影像.putpixel 設定該點之像素值

from PIL import ImageStat


def darkchannel(input_image, h, w):
    dark_image = Image.new("L", (h, w), 0)
    for x in range(0, h - 1):
        for y in range(0, w - 1):
            dark_image.putpixel((x, y), min(input_image.getpixel((x, y))))
    return dark_image


def airlight(input_image, h, w):
    nMinDistance = 65536
    w = int(round(w / 2))
    h = int(round(h / 2))
    if h * w > 200:
        lu_box = (0, 0, w, h)
        ru_box = (w, 0, 2 * w, h)
        lb_box = (0, h, w, 2 * h)
        rb_box = (w, h, 2 * h, 2 * w)

        lu = input_image.crop(lu_box)
        ru = input_image.crop(ru_box)
        lb = input_image.crop(lb_box)
        rb = input_image.crop(rb_box)
        lu_m = ImageStat.Stat(lu)
        ru_m = ImageStat.Stat(ru)
        lb_m = ImageStat.Stat(lb)
        rb_m = ImageStat.Stat(rb)
        lu_mean = lu_m.mean
        ru_mean = ru_m.mean
        lb_mean = lb_m.mean
        rb_mean = rb_m.mean
        lu_stddev = lu_m.stddev
        ru_stddev = ru_m.stddev
        lb_stddev = lb_m.stddev
        rb_stddev = rb_m.stddev
        score0 = (
            lu_mean[0]
            + lu_mean[1]
            + lu_mean[2]
            - lu_stddev[0]
            - lu_stddev[1]
            - lu_stddev[2]
        )
        score1 = (
            ru_mean[0]
            + ru_mean[1]
            + lu_mean[2]
            - ru_stddev[0]
            - ru_stddev[1]
            - ru_stddev[2]
        )
        score2 = (
            lb_mean[0]
            + lb_mean[1]
            + lb_mean[2]
            - lb_stddev[0]
            - lb_stddev[1]
            - lb_stddev[2]
        )
        score3 = (
            rb_mean[0]
            + rb_mean[1]
            + rb_mean[2]
            - rb_stddev[0]
            - rb_stddev[1]
            - rb_stddev[2]
        )
        x = max(score0, score1, score2, score3)
        if x == score0:
            air = airlight(lu, h, w)
        if x == score1:
            air = airlight(ru, h, w)
        if x == score2:
            air = airlight(lb, h, w)
        if x == score3:
            air = airlight(rb, h, w)
    else:
        for i in range(0, h - 1):
            for j in range(0, w - 1):
                temp = input_image.getpixel((i, j))
                distance = (
                    (255 - temp[0]) ** 2 + (255 - temp[1]) ** 2 + (255 - temp[2]) ** 2
                ) ** 0.5
                if nMinDistance > distance:
                    nMinDistance = distance
                    air = temp
    return air


def transmssion(air, dark_image, h, w, OMIGA):
    trans_map = np.zeros((h, w))
    A = max(air)
    for i in range(0, h - 1):
        for j in range(0, w - 1):
            temp = 1 - OMIGA * dark_image.getpixel((i, j)) / A
            trans_map[i, j] = max(0.1, temp)
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            tempup = (
                trans_map[i - 1][j - 1]
                + 2 * trans_map[i][j - 1]
                + trans_map[i + 1][j - 1]
            )
            tempmid = 2 * (
                trans_map[i - 1][j] + 2 * trans_map[i][j] + trans_map[i + 1][j]
            )
            tempdown = (
                trans_map[i - 1][j + 1]
                + 2 * trans_map[i][j + 1]
                + trans_map[i + 1][j + 1]
            )
            trans_map[i, j] = (tempup + tempmid + tempdown) / 16
    return trans_map


def defog(image, t_map, air, h, w):
    dehaze_image = Image.new("RGB", (h, w), 0)
    for i in range(0, h - 1):
        for j in range(0, w - 1):
            R, G, B = image.getpixel((i, j))
            R = int((R - air[0]) / t_map[i, j] + air[0])
            G = int((G - air[1]) / t_map[i, j] + air[1])
            B = int((B - air[2]) / t_map[i, j] + air[2])
            dehaze_image.putpixel((i, j), (R, G, B))
    return dehaze_image


# 檔案 => PIL影像
image = Image.open(filename1)

[h, w] = image.size
OMIGA = 0.8
dark_image = darkchannel(image, h, w)
air = airlight(image, h, w)
T_map = transmssion(air, dark_image, h, w, OMIGA)
fogfree_image = defog(image, T_map, air, h, w)

# 把結果顯示出來
plt.imshow(fogfree_image)

plt.show()

print("------------------------------------------------------------")  # 60個

print("PIL_save")


def IsValidImage(image_path):
    """
    判斷文件是否為有效（完整）的圖片
    :param image_path:圖片路徑
    :return:True：有效 False：無效
    """
    bValid = True
    try:
        Image.open(image_path).verify()
    except:
        bValid = False
    return bValid


def transimage(image_path):
    """
    轉換圖片格式
    :param image_path:圖片路徑
    :return: True：成功 False：失敗
    """
    if IsValidImage(image_path):
        try:
            str = image_path.rsplit(".", 1)
            output_image_path = "tmp_" + str[0] + ".jpg"
            print(output_image_path)
            im = Image.open(image_path)
            # im.save(output_image_path)
            return True
        except:
            return False
    else:
        return False


image_path = "lena.png"
print(transimage(image_path))

print("------------------------------------------------------------")  # 60個

print("二值化")
image1 = Image.open(open(filename2, "rb"))
image2 = image1.point(lambda x: 0 if x < 128 else 255)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


"""


image2.save(open('tmp_elephant_binary.png', 'wb'))

"""
