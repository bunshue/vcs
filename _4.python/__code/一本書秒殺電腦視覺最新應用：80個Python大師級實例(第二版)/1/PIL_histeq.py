from PIL import Image
from pylab import *
from PCV.tools import imtools

# 添加中文字体支持
from matplotlib.font_manager import FontProperties
plt.rcParams['font.sans-serif'] =['SimHei']  #显示中文标签

im = array(Image.open('house2.jpg').convert('L'))
# 打开图像，并转成灰度图像
im2, cdf = imtools.histeq(im)
figure()
subplot(2, 2, 1)
axis('off')
gray()
title(u'原始图像')
imshow(im)
subplot(2, 2, 2)
axis('off')
title(u'直方图均衡化后的图像')
imshow(im2)
subplot(2, 2, 3)
axis('off')
title(u'原始直方图')
hist(im.flatten(), 128, normed=True)
subplot(2, 2, 4)
axis('off')
title(u'均衡化后的直方图')
hist(im2.flatten(), 128, normed=True)
show()



