from PIL import Image
from pylab import *
from scipy.ndimage import  filters
import numpy

plt.rcParams['font.sans-serif'] =['SimHei']  #显示中文标签
im=array(Image.open('house2.jpg').convert('L'))
gray()
subplot(141)
axis('off')
title(u'(a)原图')
imshow(im)
# sobel算子
imx=zeros(im.shape)
filters.sobel(im,1,imx)
subplot(142)
axis('off')
title(u'(b)x方向差分')
imshow(imx)
imy=zeros(im.shape)
filters.sobel(im,0,imy)
subplot(143)
axis('off')
title(u'(c)y方向差分')
imshow(imy)
mag=255-numpy.sqrt(imx**2+imy**2)
subplot(144)
title(u'(d)梯度幅值')
axis('off')
imshow(mag)
show()
