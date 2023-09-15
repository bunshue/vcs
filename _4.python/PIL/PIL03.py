import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/sample.jpg'
filename = r'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
image1 = Image.open(filename)    #PIL讀取本機圖片, 讀取的是RGB格式的圖片
plt.imshow(image1)  #原圖
plt.show()

image1g = image1.convert('L')	#轉換成灰階圖像
plt.imshow(image1g)      #灰階圖
plt.show()

width, height = image1g.size
print('原圖大小 W =', width, ', H =', height)

x_st = 100
y_st = 200
w = 200
h = 200
image2 = image1g.crop((x_st, y_st, x_st + w, y_st + h))

plt.imshow(image2)
plt.show()

image2_hist = image2.histogram()

print('把圖轉成 100X500 大小')
image3 = image1.resize((100, 500), Image.ANTIALIAS)

plt.imshow(image3)
plt.show()

image1g = image3.convert('L')	#轉換成灰階圖像
hist = image1g.histogram()

r, g, b = image3.split()   #r, g, b為三個通道的list
print('r', r)
print('g', g)
print('b', b)
r_hist = r.histogram()
g_hist = g.histogram()
b_hist = b.histogram()

ind = np.arange(0, len(image2_hist))

plt.plot(ind, image2_hist, color='cyan', label='cropped')
plt.plot(ind, hist, color='black', lw=2, label='original')
plt.plot(ind, r_hist, color='red', label='Red Plane')
plt.plot(ind, g_hist, color='green', label='Green Plane')
plt.plot(ind, g_hist, color='blue', label='Blue Plane')
plt.xlim(0, 255)
plt.ylim(0, 8000)
plt.legend()

plt.show()

print('------------------------------------------------------------')	#60個

print('萃取圖片的輪廓')

import matplotlib.pyplot as plt
from PIL import Image

# 讀入圖片
filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/sample2.png'
filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

image1 = Image.open(filename)    #PIL讀取本機圖片, 讀取的是RGB格式的圖片
plt.imshow(image1)
plt.show()

#全彩轉灰階
image1 = image1.convert("L")
plt.imshow(image1)
plt.show()

# 圖片大小
width, height = image1.size

# 輸出用
image2 = Image.new('RGB', (width, height))

# 萃取輪廓
for y in range(0, height - 1):
    for x in range(0, width - 1):
        # 計算亮度差
        diff_x = image1.getpixel((x + 1, y)) - image1.getpixel((x, y))
        diff_y = image1.getpixel((x, y + 1)) - image1.getpixel((x, y))
        diff = diff_x + diff_y
        
        # 輸出
        if diff >= 20:
            image2.putpixel((x, y), (255, 0, 0))   #亮度差較大 著紅色
        else:
            image2.putpixel((x, y), (0, 0, 0))     #亮度差較小 著黑色

plt.imshow(image2)

plt.show()

print('------------------------------------------------------------')	#60個


import sys

import matplotlib.pyplot as plt
from PIL import Image

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/flower.jpg'
filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

print('------------------------------------------------------------')	#60個

from PIL import Image

image = Image.open(filename)

r, g, b = image.split()

convert_image = Image.merge('RGB', (b, g, r))

plt.imshow(convert_image)
plt.show()

#convert_image.save('rgb_to_bgr.jpg')

print('------------------------------------------------------------')	#60個

from PIL import Image

image = Image.open(filename)

black_and_white = image.convert('1')

plt.imshow(black_and_white)
plt.show()

#black_and_white.save('b_and_w.jpg')

print('------------------------------------------------------------')	#60個

from PIL import Image

image = Image.open(filename)

gray_iamge = image.convert('L')

plt.imshow(gray_iamge)
plt.show()

#gray_iamge.save('gray_image.jpg') 

print('------------------------------------------------------------')	#60個

from PIL import Image

image = Image.open(filename)

rotate_image = image.transpose(Image.ROTATE_90)
plt.imshow(rotate_image)
plt.show()

#rotate_image.save('rotate_90.jpg')#儲存90度旋轉的圖片

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個




