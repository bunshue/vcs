from PIL import Image
from numpy import *
from pylab import *
from scipy.ndimage import filters
from matplotlib.font_manager import FontProperties
plt.rcParams['font.sans-serif'] =['SimHei']  #显示中文标签

im=array(Image.open('house2.jpg').convert('L'))
figure()
gray()
axis('off')
subplot(141)
axis('off')
title(u'原图')
imshow(im)
for bi,blur in enumerate([2,4,8]):
    im2=zeros(im.shape)
    im2=filters.gaussian_filter(im,blur)
    im2=np.uint8(im2)
    imNum=str(blur)
    subplot(1,4,2+bi)
    axis('off')
    title(u'标准差为'+imNum)
    imshow(im2)

#如果是彩色图像，则分别对三个通道进行模糊
#for bi, blur in enumerate([2,4,8]):
#  im2 = zeros(im.shape)
#  for i in range(3):
#    im2[:, :, i] = filters.gaussian_filter(im[:, :, i], blur)
#  im2 = np.uint8(im2)
#  subplot(1, 4,  2 + bi)
#  axis('off')
#  imshow(im2)

show()
