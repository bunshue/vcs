from PIL import Image
from pylab import *
from numpy import *
from numpy import random
from scipy.ndimage import filters
from scipy.misc import imsave
from PCV.tools import rof
plt.rcParams['font.sans-serif'] =['SimHei']  #显示中文标签
im = array(Image.open('gril.jpg').convert('L'))
U,T = rof.denoise(im,im)
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
imshow(U)
#axis('equal')
axis('off')
title(u'ROF降噪后的图像')
show()
