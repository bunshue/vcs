"""
PIL 新進



PIL中所涉及的基本概念有如下几个：
通道（bands）
模式（mode）
尺寸（size）
坐标系统（coordinate system）
调色板（palette）
信息（info）
滤波器（filters）

1、  通道
彩色圖片 RGB 3通道
灰階圖片 1通道

2、  模式

图像的模式定义了图像的类型和像素的位宽。当前支持如下模式：

1：1位像素，表示黑和白，但是存储的时候每个像素存储为8bit。
L：8位像素，表示黑和白。
P：8位像素，使用调色板映射到其他模式。
RGB：3x8位像素，为真彩色。
RGBA：4x8位像素，有透明通道的真彩色。
CMYK：4x8位像素，颜色分离。
YCbCr：3x8位像素，彩色视频格式。
I：32位整型像素。
F：32位浮点型像素。

3、  尺寸
4、  坐标系统

PIL使用笛卡尔像素坐标系统，坐标(0，0)位于左上角。
注意：坐标值表示像素的角；位于坐标（0，0）处的像素的中心实际上位于（0.5，0.5）。
坐标经常用于二元组（x，y）。
长方形则表示为四元组，前面是左上角坐标。
例如，一个覆盖800x600的像素图像的长方形表示为（0，0，800，600）。

5、  调色板

调色板模式 ("P")使用一个颜色调色板为每个像素定义具体的颜色值

6、  信息

使用info属性可以为一张图片添加一些辅助信息。这个是字典对象。
加载和保存图像文件时，多少信息需要处理取决于文件格式。

7、  滤波器

对于将多个输入像素映射为一个输出像素的几何操作，PIL提供了4个不同的采样滤波器：

NEAREST：最近滤波。从输入图像中选取最近的像素作为输出像素。它忽略了所有其他的像素。
BILINEAR：双线性滤波。在输入图像的2x2矩阵上进行线性插值。注意：PIL的当前版本，做下采样时该滤波器使用了固定输入模板。
BICUBIC：双立方滤波。在输入图像的4x4矩阵上进行立方插值。注意：PIL的当前版本，做下采样时该滤波器使用了固定输入模板。
ANTIALIAS：平滑滤波。这是PIL 1.1.3版本中新的滤波器。
对所有可以影响输出像素的输入像素进行高质量的重采样滤波，以计算输出像素值。
在当前的PIL版本中，这个滤波器只用于改变尺寸和缩略图方法。

注意：在当前的PIL版本中，ANTIALIAS滤波器是下采样（例如，将一个大的图像转换为小图）时唯一正确的滤波器。
BILIEAR和BICUBIC滤波器使用固定的输入模板，用于固定比例的几何变换和上采样是最好的。

Image模块中的方法resize()和thumbnail()用到了滤波器。

PIL 之 resize()

image.resize(size, filter=None)

>>>im_resize = im.resize((256,256))

对参数filter不赋值的话，方法resize()默认使用NEAREST滤波器。

>>>im_resize0 = im.resize((256,256), Image.BILINEAR)
>>>im_resize1 = im.resize((256,256), Image.BICUBIC)
>>>im_resize2 = im.resize((256,256), Image.ANTIALIAS)

PIL 之 thumbnail()

image.thumbnail(size, filter=None)

>>>im.thumbnail((200,200))

这里需要说明的是，方法thumbnail()需要保持宽高比，对于size=(200,200)的输入参数，其最终的缩略图尺寸为(200, 112)。
对参数filter不赋值的话，方法thumbnail()默认使用NEAREST滤波器。如果要使用其他滤波器可以通过下面的方法来实现：

>>> im.thumbnail((200,200),Image.BILINEAR)
>>> im.thumbnail((200,200), Image.BICUBIC)
>>> im.thumbnail((200,200), Image.ANTIALIAS)






"""

import os
import sys
import numpy as np
import matplotlib.pyplot as plt

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

from PIL import Image   # Importing Image class from PIL module

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

print("------------------------------------------------------------")  # 60個
print('顯示原圖')

#建立Pillow物件 PIL讀取本機圖片, RGB模式, 存成PIL影像格式
img = Image.open(filename)
#img = img.convert('L')  #fail
print(type(img))

print('取得通道與名稱')
cc = img.getbands()
print(cc)
print('共有 :', len(cc), '個通道')
for i in range(len(cc)):
    print("通道", cc[i])

print('模式')
print(img.mode)

print('尺寸')
print(img.size)

print('信息')
print(img.info)



"""
plt.figure('Image')
plt.imshow(img)
plt.show()
"""

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

image = Image.open(filename)

plt.imshow(image)
plt.show()

r, g, b = image.split() # 分離三個通道
image = Image.merge("RGB",(b,g,r))# 將藍色通道和通道互換

plt.imshow(image)
plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

