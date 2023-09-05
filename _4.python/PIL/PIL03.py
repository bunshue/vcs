import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

filename = 'C:/_git/vcs/_1.data/______test_files1/sample.jpg'
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


