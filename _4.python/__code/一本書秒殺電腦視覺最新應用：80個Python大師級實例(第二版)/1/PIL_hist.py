from PIL import Image
from pylab import *
plt.rcParams['font.sans-serif'] =['SimHei']  #显示中文标签
import matplotlib.pyplot as plt
# 打开图像，并转成灰度图像
im = array(Image.open('house2.jpg').convert('L'))

# 新建一个图像
figure()
subplot(121)
# 不使用颜色信息
gray()
# 在原点的左上角显示轮廓图像
contour(im, origin='image')
axis('equal')
axis('off')
title(u'图像轮廓图')

subplot(122)
# 利用hist来绘制直方图
# 第一个参数为一个一维数组
# 因为hist只接受一维数组作为输入，所以要用flatten()方法将任意数组按照行优先准则转化成一个一维数组
# 第二个参数指定bin的个数
hist(im.flatten(), 128)
title(u'图像直方图')
#刻度
plt.xlim([0,250])
plt.ylim([0,12000])

show()
