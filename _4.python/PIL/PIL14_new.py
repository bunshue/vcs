"""
PIL 新進


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

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

print("------------------------------------------------------------")  # 60個

print("PIL_opening")

from numpy import *
#measurements模块实现二值图像的计数和度量功能，morphology模块实现形态学操作
from scipy.ndimage import measurements, morphology  
from pylab import *

# 加载图像和阈值，以确保它是二进制的
figure()
gray()
im = array(Image.open('data/castle.jpg').convert('L'))
subplot(221)
imshow(im)
axis('off')
title(u'原图')
im = (im < 128)
labels, nbr_objects = measurements.label(im) #图像的灰度值表示对象的标签
print ("Number of objects:", nbr_objects)
subplot(222)
imshow(labels)
axis('off')
title(u'标记后的图')
#形态学——使物体分离更好
im_open = morphology.binary_opening(im, ones((9, 5)), iterations=4) #开操作，第二个参数为结构元素，iterations觉定执行该操作的次数
subplot(223)
imshow(im_open)
axis('off')
title(u'开运算后的图像')
labels_open, nbr_objects_open = measurements.label(im_open)
print ("Number of objects:", nbr_objects_open)
subplot(224)
imshow(labels_open)
axis('off')
title(u'开运算后进行标记后的图像')

show()

print("------------------------------------------------------------")  # 60個

print("PIL_PCA")

from numpy import *
#measurements模块实现二值图像的计数和度量功能，morphology模块实现形态学操作
from scipy.ndimage import measurements, morphology  
from pylab import *

# 加载图像和阈值，以确保它是二进制的
figure()
gray()
im = array(Image.open('data/castle.jpg').convert('L'))
subplot(221)
imshow(im)
axis('off')
title(u'原图')
im = (im < 128)
labels, nbr_objects = measurements.label(im) #图像的灰度值表示对象的标签
print ("Number of objects:", nbr_objects)
subplot(222)
imshow(labels)
axis('off')
title(u'标记后的图')
#形态学——使物体分离更好
im_open = morphology.binary_opening(im, ones((9, 5)), iterations=4) #开操作，第二个参数为结构元素，iterations觉定执行该操作的次数
subplot(223)
imshow(im_open)
axis('off')
title(u'开运算后的图像')
labels_open, nbr_objects_open = measurements.label(im_open)
print ("Number of objects:", nbr_objects_open)
subplot(224)
imshow(labels_open)
axis('off')
title(u'开运算后进行标记后的图像')

show()

print("------------------------------------------------------------")  # 60個

print("PIL_realROF")

from pylab import *
from numpy import *
from numpy import random
from scipy.ndimage import filters
#from scipy.misc import imsave
#from PCV.tools import rof

im = array(Image.open('data/gril.jpg').convert('L'))
#U,T = rof.denoise(im,im)
G = filters.gaussian_filter(im,10)
figure()
gray()
subplot(1,3,1)
imshow(im)
#axis('equal')
axis('off')
title(u'原噪声图像')
subplot(1,3,2)
imshow(G)
#axis('equal')
axis('off')
title(u'高斯模糊后的图像')
subplot(1,3,3)
#imshow(U)
#axis('equal')
axis('off')
title(u'ROF降噪后的图像')

show()

print("------------------------------------------------------------")  # 60個

print("PIL_ROF")

from pylab import *
from numpy import *
from numpy import random
from scipy.ndimage import filters
#from scipy.misc import imsave
#from PCV.tools import rof

# 创建合成图像与噪声
im = zeros((500,500))
im[100:400,100:400] = 128
im[200:300,200:300] = 255
im = im + 30*random.standard_normal((500,500))
#roll()函数：循环滚动数组中的元素，计算领域元素的差异。linalg.norm()函数可以衡量两个数组见得差异
#U,T = rof.denoise(im,im)  
G = filters.gaussian_filter(im,10)
figure()
gray()
subplot(1,3,1)
imshow(im)
#axis('equal')
axis('off')
title(u'原噪声图像')

subplot(1,3,2)
imshow(G)
#axis('equal')
axis('off')
title(u'高斯模糊后的图像')

subplot(1,3,3)
#imshow(U)
#axis('equal')
axis('off')
title(u'ROF降噪后的图像')

show()

print("------------------------------------------------------------")  # 60個

print("PIL_save")

def IsValidImage(img_path):
    """
    判断文件是否为有效（完整）的图片
    :param img_path:图片路径
    :return:True：有效 False：无效
    """
    bValid = True
    try:
        Image.open(img_path).verify()
    except:
        bValid = False
    return bValid


def transimg(img_path):
    """
    转换图片格式
    :param img_path:图片路径
    :return: True：成功 False：失败
    """
    if IsValidImage(img_path):
        try:
            str = img_path.rsplit(".", 1)
            output_img_path = "tmp_" + str[0] + ".jpg"
            print(output_img_path)
            im = Image.open(img_path)
            im.save(output_img_path)
            return True
        except:
            return False
    else:
        return False


img_path = 'lena.png'
print(transimg(img_path))

print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個




print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


