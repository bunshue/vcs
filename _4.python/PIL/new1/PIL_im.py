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

from PIL import Image
#from numpy import *
from pylab import *

im=array(Image.open('house2.jpg').convert('L'))
print(int(im.min()),int(im.max()))

im2=255-im               #对图像进行反向处理
print('对图像进行反向处理:\n',int(im2.min()),int(im2.max())) #查看最大/最小元素

im3=(100.0/255)*im+100   #将图像像素值变换到100...200区间
print('将图像像素值变换到100...200区间:\n',int(im3.min()),int(im3.max()))

im4=255.0*(im/255.0)**2  #对像素值求平方后得到的图像
print('对像素值求平方后得到的图像:\n',int(im4.min()),int(im4.max()))

plt.figure('影像處理2', figsize = (10, 6))
gray()

subplot(131)
imshow(im2)
axis('off')
title(r'$f(x)=255-x$')

subplot(132)
imshow(im3)
axis('off')
title(r'$f(x)=\frac{100}{255}x+100$')

subplot(133)
imshow(im4)
axis('off')
title(r'$f(x)=255(\frac{x}{255})^2$')

show()
