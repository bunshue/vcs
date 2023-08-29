from PIL import Image
from numpy import *
#measurements模块实现二值图像的计数和度量功能，morphology模块实现形态学操作
from scipy.ndimage import measurements, morphology  
from pylab import *

#plt.rcParams['font.sans-serif'] =['SimHei']  #显示中文标签
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

# 加载图像和阈值，以确保它是二进制的
figure()
gray()
im = array(Image.open('castle3.jpg').convert('L'))
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
