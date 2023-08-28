from PIL import Image
from pylab import *
plt.rcParams['font.sans-serif'] =['SimHei']  #显示中文标签
figure()
pil_im = Image.open('house.jpg')
gray()
subplot(121)
title(u'原图')
axis('off')
imshow(pil_im)
pil_im = Image.open('house.jpg').convert('L')
subplot(122)
title(u'灰度图')
axis('off')
imshow(pil_im)
show()
