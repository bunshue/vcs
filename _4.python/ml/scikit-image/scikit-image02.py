"""
skimage : scikit-image SciKit (toolkit for SciPy)

pip install scikit-image

子模块名称　 	主要实现功能
io 	        读取、保存和显示图片或视频
data    	提供一些测试图片和样本数据
color 	        颜色空间变换
filters 	图像增强、边缘检测、排序滤波器、自动阈值等
draw  	        操作于numpy数组上的基本图形绘制，包括线条、矩形、圆和文本等
transform 	几何变换或其它变换，如旋转、拉伸和拉东变换等
morphology 	形态学操作，如开闭运算、骨架提取等
exposure 	图片强度调整，如亮度调整、直方图均衡等
feature 	特征检测与提取等
measure 	图像属性的测量，如相似性或等高线等
segmentation 	图像分割
restoration 	图像恢复
util 	        通用函数

skimage 內建圖片位置
astronaut	      宇航员图片      coffee	            一杯咖啡图片
lena(x)               lena美女图片    camera	            拿相机的人图片
coins	              硬币图片        moon	            月亮图片
checkerboard	      棋盘图片        horse	            马图片
page	              书页图片        chelsea	            小猫图片
hubble_deep_field     星空图片        text	            文字图片
clock	              时钟图片        immunohistochemistry  结肠图片

"""

import sys
import matplotlib.pyplot as plt
import numpy as np
import math

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個


filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

from skimage import io
img=io.imread(filename)
io.imshow(img)

plt.show()


from skimage import io
img=io.imread(filename, True)   #True:轉為灰階
io.imshow(img)
plt.show()


from skimage import data    #圖片資料模組
from skimage import color   #色彩處理模組

img = data.astronaut()
io.imshow(img)
plt.show()

img =color.rgb2gray(img)
io.imshow(img)
plt.show()

from skimage import data_dir
print('skimage內建圖片位置 :', data_dir)

'''
#存圖
from skimage import io,data
img = data.astronaut()
img = data.chelsea()
io.imshow(img)
plt.show()
io.imsave('mmmm.jpg',img)  #依副檔名轉換圖片格式存檔

print('------------------------------------------------------------')	#60個

print('打印圖片訊息')
from skimage import io,data
img=data.chelsea()
io.imshow(img)
print('显示类型 :', type(img))
print('显示尺寸 :', img.shape)
print('图片宽度 :', img.shape[0])
print('图片高度 :', img.shape[1])
print('图片通道数 :', img.shape[2])
print('显示总像素个数 :', img.size)
print('最大像素值 :', img.max())
print('最小像素值 :', img.min())
print('像素平均值 :', img.mean())

print('------------------------------------------------------------')	#60個

#输出小猫图片的G通道中的第20行30列的像素值

from skimage import io,data
img=data.chelsea()
pixel=img[20,30,1]
print(pixel)


#显示红色单通道图片

from skimage import io,data
img=data.chelsea()
R=img[:,:,0]
io.imshow(R)


#修改像素值
#对小猫图片随机添加椒盐噪声

from skimage import io,data
import numpy as np
img=data.chelsea()

#随机生成5000个椒盐
rows,cols,dims=img.shape
for i in range(5000):
    x=np.random.randint(0,rows)
    y=np.random.randint(0,cols)
    img[x,y,:]=255
    
io.imshow(img)
plt.show()



print('------------------------------------------------------------')	#60個

#通过对数组的裁剪，就可以实现对图片的裁剪。
#对小猫图片进行裁剪

from skimage import io,data
img=data.chelsea()
roi=img[80:180,100:200,:]
io.imshow(roi)
plt.show()

print('------------------------------------------------------------')	#60個

#对多个像素点进行操作，使用数组切片方式访问。
#切片方式返回的是以指定间隔下标访问 该数组的像素值。
#下面是有关灰度图像的一些例子：
"""
img[i,:] = im[j,:] # 将第 j 行的数值赋值给第 i 行

img[:,i] = 100 # 将第 i 列的所有数值设为 100

img[:100,:50].sum() # 计算前 100 行、前 50 列所有数值的和

img[50:100,50:100] # 50~100 行，50~100 列（不包括第 100 行和第 100 列）

img[i].mean() # 第 i 行所有数值的平均值

img[:,-1] # 最后一列

img[-2,:] (or im[-2]) # 倒数第二行
"""

#最后我们再看两个对像素值进行访问和改变的例子：
#例5：将astronaut图片进行二值化，像素值大于128的变为1，否则变为0

from skimage import io,data,color
#img = data.astronaut()
img = data.chelsea()
img_gray=color.rgb2gray(img)
rows,cols=img_gray.shape
for i in range(rows):
    for j in range(cols):
        if (img_gray[i,j]<=0.5):
            img_gray[i,j]=0
        else:
            img_gray[i,j]=1
io.imshow(img_gray)
plt.show()

#这个例子，使用了color模块的rgb2gray（）函数，将彩色三通道图片转换成灰度图。转换结果为float64类型的数组，范围为[0,1]之间。

from skimage import io, data
img = data.chelsea()
reddish = img[:, :, 0] >170
img[reddish] = [0, 255, 0]
io.imshow(img)
plt.show()

#这个例子先对R通道的所有像素值进行判断，如果大于170，则将这个地方的像素值变为[0,255,0], 即G通道值为255，R和B通道值为0。


'''


print('------------------------------------------------------------')	#60個

#图像数据类型及颜色空间转换


#数据类型
from skimage import io,data
img=data.chelsea()
print(img.dtype.name)


#颜色空间及其转换
#通过图像的颜色空间转换来改变数据类型。
#常用的颜色空间有灰度空间、rgb空间、hsv空间和cmyk空间。颜色空间转换以后，图片类型都变成了float型。
#所有的颜色空间转换函数，都放在skimage的color模块内。

#rgb转灰度图

from skimage import io,data,color
img=data.chelsea()
gray=color.rgb2gray(img)
io.imshow(gray)
plt.show()

"""

其它的转换，用法都是一样的，列举常用的如下：
skimage.color.rgb2grey(rgb)
skimage.color.rgb2hsv(rgb)
skimage.color.rgb2lab(rgb)
skimage.color.gray2rgb(image)
skimage.color.hsv2rgb(hsv)
skimage.color.lab2rgb(lab)

实际上，上面的所有转换函数，都可以用一个函数来代替
skimage.color.convert_colorspace(arr, fromspace, tospace)
表示将arr从fromspace颜色空间转换到tospace颜色空间。
例：rgb转hsv
from skimage import io,data,color
img=data.chelsea()
hsv=color.convert_colorspace(img,'RGB','HSV')
io.imshow(hsv)

"""


print('------------------------------------------------------------')	#60個

#在color模块的颜色空间转换函数中，还有一个比较有用的函数是
#skimage.color.label2rgb(arr), 可以根据标签值对图片进行着色。以后的图片分类后着色就可以用这个函数。
#例：将astronaut图片分成三类，然后用默认颜色对三类进行着色

from skimage import io,data,color
import numpy as np
img=data.astronaut()
gray=color.rgb2gray(img)
rows,cols=gray.shape
labels=np.zeros([rows,cols])
for i in range(rows):
    for j in range(cols):
        if(gray[i,j]<0.4):
            labels[i,j]=0
        elif(gray[i,j]<0.75):
            labels[i,j]=1
        else:
            labels[i,j]=2
dst=color.label2rgb(labels)
io.imshow(dst)
plt.show()

print('------------------------------------------------------------')	#60個

