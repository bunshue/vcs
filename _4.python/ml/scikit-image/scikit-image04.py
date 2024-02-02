"""
skimage : scikit-image SciKit (toolkit for SciPy)


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

"""
图像的批量处理

有些时候，我们不仅要对一张图片进行处理，可能还会对一批图片处理。这时候，我们可以通过循环来执行处理，也可以调用程序自带的图片集合来处理。

图片集合函数为：

skimage.io.ImageCollection(load_pattern,load_func=None)

这个函数是放在io模块内的，带两个参数，第一个参数load_pattern, 表示图片组的路径，可以是一个str字符串。第二个参数load_func是一个回调函数，我们对图片进行批量处理就可以通过这个回调函数实现。回调函数默认为imread(),即默认这个函数是批量读取图片。

"""
'''
import skimage.io as io
from skimage import data_dir
string = data_dir + '/*.png'
string = 'C:/_git/vcs/_1.data/______test_files1/__pic/_angry_bird/*.jpg'
coll = io.ImageCollection(string)
print(len(coll))


#表示資料夾內有 23 張圖

"""
显示结果为25, 说明

系统自带了23张png的示例图片，这些图片都读取了出来，放在图片集合coll里。
如果我们想显示其中一张图片，则可以在后加上一行代码：
io.imshow(coll[10])

如果一个文件夹里，我们既存放了一些jpg格式的图片，又存放了一些png格式的图片，现在想把它们全部读取出来，该怎么做呢?
"""
import skimage.io as io
from skimage import data_dir
#string='d:/pic/*.jpg:d:/pic/*.png'
string = data_dir + '/*.png'
string = 'C:/_git/vcs/_1.data/______test_files1/__pic/_angry_bird/*.jpg'
coll = io.ImageCollection(string)
print(len(coll))

print('------------------------------------------------------------')	#60個

"""
注意这个地方'd:/pic/*.jpg:d:/pic/*.png' ，是两个字符串合在一起的，第一个是'd:/pic/*.jpg', 第二个是'd:/pic/*.png' ，合在一起后，中间用冒号来隔开，这样就可以把d:/pic/文件夹下的jpg和png格式的图片都读取出来。如果还想读取存放在其它地方的图片，也可以一并加进去，只是中间同样用冒号来隔开。

io.ImageCollection()这个函数省略第二个参数，就是批量读取。如果我们不是想批量读取，而是其它批量操作，如批量转换为灰度图，那又该怎么做呢？

那就需要先定义一个函数，然后将这个函数作为第二个参数，如：
"""

from skimage import data_dir,io,color

def convert_gray(f):
    rgb=io.imread(f)
    return color.rgb2gray(rgb)
    
string = data_dir+'/*.png'
string = 'C:/_git/vcs/_1.data/______test_files1/__pic/_angry_bird/*.jpg'
coll = io.ImageCollection(string,load_func=convert_gray)
io.imshow(coll[8])
plt.show()



print('------------------------------------------------------------')	#60個


#这种批量操作对视频处理是极其有用的，因为视频就是一系列的图片组合


from skimage import data_dir, io,color

class AVILoader:
    video_file = 'myvideo.avi'

    def __call__(self, frame):
        return video_read(self.video_file, frame)

avi_load = AVILoader()

frames = range(0, 1000, 10) # 0, 10, 20, ...
ic =io.ImageCollection(frames, load_func=avi_load)


print('------------------------------------------------------------')	#60個


"""
这段代码的意思，就是将myvideo.avi这个视频中每隔10帧的图片读取出来，放在图片集合中。

得到图片集合以后，我们还可以将这些图片连接起来，构成一个维度更高的数组，连接图片的函数为：

skimage.io.concatenate_images(ic)

带一个参数，就是以上的图片集合，如：
"""
"""
from skimage import data_dir,io,color

coll = io.ImageCollection('C:/_git/vcs/_1.data/______test_files1/__pic/_angry_bird/*.jpg')
#coll = io.ImageCollection(data_dir + '/*.png')
mat=io.concatenate_images(coll)

#使用concatenate_images(ic)函数的前提是读取的这些图片尺寸必须一致，否则会出错。我们看看图片连接前后的维度变化：

from skimage import data_dir,io,color

coll = io.ImageCollection('C:/_git/vcs/_1.data/______test_files1/__pic/_angry_bird/*.jpg')
#coll = io.ImageCollection(data_dir + '/*.png')
print(len(coll))      #连接的图片数量
print(coll[0].shape)   #连接前的图片尺寸，所有的都一样
mat=io.concatenate_images(coll)
print(mat.shape)  #连接后的数组尺寸
"""



"""

显示结果：

2
(870, 580, 3)
(2, 870, 580, 3)

可以看到，将2个3维数组，连接成了一个4维数组

如果我们对图片进行批量操作后，想把操作后的结果保存起来，也是可以办到的。

例：把系统自带的所有png示例图片，全部转换成256*256的jpg格式灰度图，保存在d:/data/文件夹下

改变图片的大小，我们可以使用tranform模块的resize()函数，后续会讲到这个模块。
"""

from skimage import data_dir,io,transform,color
import numpy as np

def convert_gray(f):
     rgb=io.imread(f)    #依次读取rgb图片
     gray=color.rgb2gray(rgb)   #将rgb图片转换成灰度图
     dst=transform.resize(gray,(256,256))  #将灰度图片大小转换为256*256
     return dst
    
#string = data_dir+'/*.png'
string = 'C:/_git/vcs/_1.data/______test_files1/__pic/_angry_bird/*.jpg'
coll = io.ImageCollection(string,load_func=convert_gray)
print(len(coll))

for i in range(len(coll)):
    print(i)
    #io.imsave(str(i)+'.jpg', coll[i])  #循环保存图片  fail
    print(str(i)+'.jpg')
    #print(str(i)+'.jpg')
    #print(i)
plt.show()

print('------------------------------------------------------------')	#60個

'''


"""
图像的形变与缩放

图像的形变与缩放，使用的是skimage的transform模块，函数比较多，功能齐全。

1、改变图片尺寸resize

函数格式为：

skimage.transform.resize(image, output_shape)

image: 需要改变尺寸的图片

output_shape: 新的图片尺寸
"""

from skimage import transform,data
import matplotlib.pyplot as plt
img = data.camera()
dst=transform.resize(img, (80, 60))
plt.figure('resize')

plt.subplot(121)
plt.title('before resize')
plt.imshow(img,plt.cm.gray)

plt.subplot(122)
plt.title('before resize')
plt.imshow(dst,plt.cm.gray)

plt.show()

#将camera图片由原来的512*512大小，变成了80*60大小。从下图中的坐标尺，我们能够看出来：

"""
2、按比例缩放rescale

函数格式为：

skimage.transform.rescale(image, scale[, ...])

scale参数可以是单个float数，表示缩放的倍数，也可以是一个float型的tuple，如[0.2,0.5],表示将行列数分开进行缩放
"""

from skimage import transform,data
img = data.camera()
print(img.shape)  #图片原始大小 
print(transform.rescale(img, 0.1).shape)  #缩小为原来图片大小的0.1倍
print(transform.rescale(img, [0.5,0.25]).shape)  #缩小为原来图片行数一半，列数四分之一
print(transform.rescale(img, 2).shape)   #放大为原来图片大小的2倍
"""
结果为：
(512, 512)
(51, 51)
(256, 128)
(1024, 1024)

3、旋转 rotate

skimage.transform.rotate(image, angle[, ...],resize=False)

angle参数是个float类型数，表示旋转的度数

resize用于控制在旋转时，是否改变大小 ，默认为False
"""
from skimage import transform,data
import matplotlib.pyplot as plt
img = data.camera()
print(img.shape)  #图片原始大小
img1=transform.rotate(img, 60) #旋转90度，不改变大小 
print(img1.shape)
img2=transform.rotate(img, 30,resize=True)  #旋转30度，同时改变大小
print(img2.shape)   

plt.figure('resize')

plt.subplot(121)
plt.title('rotate 60')
plt.imshow(img1,plt.cm.gray)

plt.subplot(122)
plt.title('rotate  30')
plt.imshow(img2,plt.cm.gray)

plt.show()





"""
4、图像金字塔

以多分辨率来解释图像的一种有效但概念简单的结构就是图像金字塔。图像金字塔最初用于机器视觉和图像压缩，一幅图像的金字塔是一系列以金字塔形状排列的分辨率逐步降低的图像集合。金字塔的底部是待处理图像的高分辨率表示，而顶部是低分辨率的近似。当向金字塔的上层移动时，尺寸和分辨率就降低。

在此，我们举一个高斯金字塔的应用实例，函数原型为：

skimage.transform.pyramid_gaussian(image, downscale=2)
downscale控制着金字塔的缩放比例
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage import data,transform

image = data.astronaut()  #载入宇航员图片
rows, cols, dim = image.shape  #获取图片的行数，列数和通道数
pyramid = tuple(transform.pyramid_gaussian(image, downscale=2))  #产生高斯金字塔图像
#共生成了log(512)=9幅金字塔图像，加上原始图像共10幅，pyramid[0]-pyramid[1]

"""
#composite_image = np.ones((rows, cols + cols / 2, 3), dtype=np.double)  #生成背景
composite_image = np.ones((rows, cols + 256, 3), dtype=np.double)  #生成背景
"""

"""
除了高斯金字塔外，还有其它的金字塔，如：
skimage.transform.pyramid_laplacian(image, downscale=2)
"""

