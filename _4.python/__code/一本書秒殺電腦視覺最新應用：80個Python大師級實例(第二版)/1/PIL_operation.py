from PIL import Image
from pylab import *
plt.rcParams['font.sans-serif'] =['SimHei']  #显示中文标签
figure()
# 显示原图
pil_im = Image.open('house.jpg')
print(pil_im.mode, pil_im.size, pil_im.format)
subplot(231)
title(u'原图')
axis('off')
imshow(pil_im)
# 显示灰度图
pil_im = Image.open('house.jpg').convert('L')
gray()
subplot(232)
title(u'灰度图')
axis('off')
imshow(pil_im)
# 复制并粘贴区域
pil_im = Image.open('house.jpg')
box = (100, 100, 400, 400)
region = pil_im.crop(box)
region = region.transpose(Image.ROTATE_180)
pil_im.paste(region, box)
subplot(233)
title(u'复制粘贴区域')
axis('off')
imshow(pil_im)

# 缩略图
pil_im = Image.open('house.jpg')
size = 128, 128
pil_im.thumbnail(size)
print(pil_im.size)
subplot(234)
title(u'缩略图')
axis('off')
imshow(pil_im)
pil_im.save('house.jpg')# 保存缩略图

#调整图像尺寸
pil_im=Image.open('house.jpg')
pil_im=pil_im.resize(size)
print(pil_im.size)
subplot(235)
title(u'调整尺寸后的图像')
axis('off')
imshow(pil_im)

#旋转图像45°
pil_im=Image.open('house.jpg')
pil_im=pil_im.rotate(45)
subplot(236)
title(u'旋转45°后的图像')
axis('off')
imshow(pil_im)
show()
