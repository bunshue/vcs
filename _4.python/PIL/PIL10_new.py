"""
PIL 基本使用

顯示圖片

顯示圖片訊息

"""

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'

import sys
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image   # Importing Image class from PIL module

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

print('顯示原圖')

image1 = Image.open(filename)    #建立Pillow物件 PIL讀取本機圖片, RGB模式
plt.imshow(image1)
plt.show()

print('------------------------------------------------------------')	#60個

"""
使用python进行数字图片处理，还得安装Pillow包。
虽然python里面自带一个PIL（python images library), 但这个库现在已经停止更新了，
所以使用Pillow, 它是由PIL发展而来的。

pip install Pillow
"""

print('------------------------------------------------------------')	#60個

"""
图像通道\几何变换\裁剪

一、图像通道

1、彩色图像转灰度图
"""

img=Image.open(filename)
gray=img.convert('L')
plt.figure('Peony')
plt.imshow(gray,cmap='gray')
plt.axis('off')
plt.show()

"""
使用函数convert()来进行转换，它是图像实例对象的一个方法，接受一个 mode 参数，用以指定一种色彩模式，mode 的取值可以是如下几种：
· 1 (1-bit pixels, black and white, stored with one pixel per byte)
· L (8-bit pixels, black and white)
· P (8-bit pixels, mapped to any other mode using a colour palette)
· RGB (3x8-bit pixels, true colour)
· RGBA (4x8-bit pixels, true colour with transparency mask)
· CMYK (4x8-bit pixels, colour separation)
· YCbCr (3x8-bit pixels, colour video format)
· I (32-bit signed integer pixels)
· F (32-bit floating point pixels)

2、通道分离与合并
"""

img=Image.open(filename)  #打开图像
gray=img.convert('L')   #转换成灰度
r,g,b=img.split()   #分离三通道
pic=Image.merge('RGB',(r,g,b)) #合并三通道
plt.figure('Peony')
plt.subplot(2,3,1), plt.title('origin')
plt.imshow(img),plt.axis('off')
plt.subplot(2,3,2), plt.title('gray')
plt.imshow(gray,cmap='gray'),plt.axis('off')
plt.subplot(2,3,3), plt.title('merge')
plt.imshow(pic),plt.axis('off')
plt.subplot(2,3,4), plt.title('r')
plt.imshow(r,cmap='gray'),plt.axis('off')
plt.subplot(2,3,5), plt.title('g')
plt.imshow(g,cmap='gray'),plt.axis('off')
plt.subplot(2,3,6), plt.title('b')
plt.imshow(b,cmap='gray'),plt.axis('off')
plt.show()

"""

二、裁剪图片

从原图片中裁剪感兴趣区域（roi),裁剪区域由4-tuple决定，该tuple中信息为(left, upper, right, lower)。 Pillow左边系统的原点（0，0）为图片的左上角。坐标中的数字单位为像素点。
"""

img=Image.open(filename)  #打开图像
plt.figure('Peony')
plt.subplot(1,2,1)
plt.title('origin')
plt.imshow(img),plt.axis('off')

box=(80,100,260,300)
roi=img.crop(box)
plt.subplot(1,2,2)
plt.title('roi')
plt.imshow(roi),plt.axis('off')

plt.show()


"""

用plot绘制显示出图片后，将鼠标移动到图片上，会在右下角出现当前点的坐标，以及像素值。

三、几何变换 

Image类有resize()、rotate()和transpose()方法进行几何变换。

　1、图像的缩放和旋转

dst = img.resize((128, 128))
dst = img.rotate(45) # 顺时针角度表示

2、转换图像

dst = im.transpose(Image.FLIP_LEFT_RIGHT) #左右互换
dst = im.transpose(Image.FLIP_TOP_BOTTOM) #上下互换
dst = im.transpose(Image.ROTATE_90)  #顺时针旋转
dst = im.transpose(Image.ROTATE_180)
dst = im.transpose(Image.ROTATE_270)

transpose()和rotate()没有性能差别。
"""


print('------------------------------------------------------------')	#60個

#添加水印
#一、添加文字水印

from PIL import Image, ImageDraw,ImageFont
im = Image.open(filename).convert('RGBA')
txt=Image.new('RGBA', im.size, (0,0,0,0))
fnt=ImageFont.truetype("c:/Windows/fonts/Tahoma.ttf", 20)
d=ImageDraw.Draw(txt)
d.text((txt.size[0]-80,txt.size[1]-30), 'Peony', font=fnt, fill=(255,0,255,255))
out=Image.alpha_composite(im, txt)
#out.show()
plt.imshow(out)
plt.show()


'''
#二、添加小图片水印

im = Image.open(filename)
mark=Image.open("logo_small.gif")
layer=Image.new('RGBA', im.size, (0,0,0,0))
layer.paste(mark, (im.size[0]-150,im.size[1]-60))
out=Image.composite(layer,im,layer)
#out.show()
plt.imshow(out)
plt.show()

'''

print('------------------------------------------------------------')	#60個

"""
图像中的像素访问

前面的一些例子中，我们都是利用Image.open（）来打开一幅图像，然后直接对这个PIL对象进行操作。如果只是简单的操作还可以，但是如果操作稍微复杂一些，就比较吃力了。因此，通常我们加载完图片后，都是把图片转换成矩阵来进行更加复杂的操作。

python中利用numpy库和scipy库来进行各种数据操作和科学计算。我们可以通过pip来直接安装这两个库

pip install numpy
pip install scipy

"""

img=np.array(Image.open(filename))  #打开图像并转化为数字矩阵
plt.figure('Peony')
plt.imshow(img)
plt.axis('off')
plt.show()

"""

调用numpy中的array（）函数就可以将PIL对象转换为数组对象。

查看图片信息，可用如下的方法：

print img.shape  
print img.dtype 
print img.size 
print type(img)

如果是RGB图片，那么转换为array之后，就变成了一个rows*cols*channels的三维矩阵,因此，我们可以使用

img[i,j,k]

来访问像素值。

例1：打开图片，并随机添加一些椒盐噪声
"""

img=np.array(Image.open(filename))

#随机生成5000个椒盐
rows,cols,dims=img.shape
for i in range(5000):
    x=np.random.randint(0,rows)
    y=np.random.randint(0,cols)
    img[x,y,:]=255
    
plt.figure('Peony')
plt.imshow(img)
plt.axis('off')
plt.show()

"""

 

例2：将lena图像二值化，像素值大于128的变为1，否则变为0
"""

img=np.array(Image.open(filename).convert('L'))

rows,cols=img.shape
for i in range(rows):
    for j in range(cols):
        if (img[i,j]<=128):
            img[i,j]=0
        else:
            img[i,j]=1
            
plt.figure('Peony')
plt.imshow(img,cmap='gray')
plt.axis('off')
plt.show()

"""

 

如果要对多个像素点进行操作，可以使用数组切片方式访问。切片方式返回的是以指定间隔下标访问 该数组的像素值。下面是有关灰度图像的一些例子：
复制代码

img[i,:] = im[j,:] # 将第 j 行的数值赋值给第 i 行

img[:,i] = 100 # 将第 i 列的所有数值设为 100

img[:100,:50].sum() # 计算前 100 行、前 50 列所有数值的和

img[50:100,50:100] # 50~100 行，50~100 列（不包括第 100 行和第 100 列）

img[i].mean() # 第 i 行所有数值的平均值

img[:,-1] # 最后一列

img[-2,:] (or im[-2]) # 倒数第二行

"""




print('------------------------------------------------------------')	#60個


"""
图像直方图

我们先来看两个函数reshape和flatten:

假设我们先生成一个一维数组：

vec=np.arange(15)
print vec

显示为：

[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]

如果我们要把这个一维数组，变成一个3*5二维矩阵，我们可以使用reshape来实现

mat= vec.reshape(3,5)
print mat

显示为

[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]]

现在如果我们返过来，知道一个二维矩阵，要变成一个一维数组，就不能用reshape了，只能用flatten. 我们来看两者的区别

a1=mat.reshape(1,-1)  #-1表示为任意，让系统自动计算
print a1
a2=mat.flatten()
print a2

显示为：

a1:  [[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]]
a2:  [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]

可以看出，用reshape进行变换，实际上变换后还是二维数组，两个方括号，因此只能用flatten.

我们要对图像求直方图，就需要先把图像矩阵进行flatten操作，使之变为一维数组，然后再进行统计。

一、画灰度图直方图

绘图都可以调用matplotlib.pyplot库来进行，其中的hist函数可以直接绘制直方图。

调用方式：

n, bins, patches = plt.hist(arr, bins=50, density = True, facecolor='green', alpha=0.75)

hist的参数非常多，但常用的就这五个，只有第一个是必须的，后面四个可选

arr: 需要计算直方图的一维数组

bins: 直方图的柱数，可选项，默认为10

density: 是否将得到的直方图向量归一化。默认为False

facecolor: 直方图颜色

alpha: 透明度

返回值 ：

n: 直方图向量，是否归一化由参数设定

bins: 返回各个bin的区间范围

patches: 返回每个bin里面包含的数据，是一个list
"""

img=np.array(Image.open(filename).convert('L'))

plt.figure('Peony')
arr=img.flatten()
n, bins, patches = plt.hist(arr, bins=256, density = True, facecolor='green', alpha=0.75)

plt.show()

"""

二、彩色图片直方图

实际上是和灰度直方图一样的，只是分别画出三通道的直方图，然后叠加在一起。
"""

src=Image.open(filename)
r,g,b=src.split()

plt.figure('Peony')
ar=np.array(r).flatten()
plt.hist(ar, bins=256, density = True,facecolor='r',edgecolor='r',stacked=1)
ag=np.array(g).flatten()
plt.hist(ag, bins=256, density = True, facecolor='g',edgecolor='g',stacked=1)
ab=np.array(b).flatten()
plt.hist(ab, bins=256, density = True, facecolor='b',edgecolor='b')
plt.show()

print('------------------------------------------------------------')	#60個



