import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

filename = 'C:/_git/vcs/_1.data/______test_files1/sample.jpg'

image = Image.open(filename)    #PIL讀取本機圖片, 讀取的是RGB格式的圖片

im = image.convert('L')	#轉換成灰階圖像

#plt.imshow(image)  #原圖
plt.imshow(im)      #灰階圖
plt.show()

w, h = im.size
print('寬 : ', w, '高 : ', h)

crop = im.crop((w / 2 - 300, h / 2 - 300, w / 2 + 300, h / 2 + 300))

print(w / 2 - 300)
print(h / 2 - 300)
print(w / 2 + 300)
print(h / 2 + 300)

crop_hist = crop.histogram()

ori = image.resize((600, 600))  #修改圖像大小

print('ori')
print(ori)

im = ori.convert('L')	#轉換成灰階圖像
hist = im.histogram()

r, g, b = ori.split()   #r, g, b為三個通道的list
print('r', r)
print('g', g)
print('b', b)
r_hist = r.histogram()
g_hist = g.histogram()
b_hist = b.histogram()

ind = np.arange(0, len(crop_hist))

plt.plot(ind, crop_hist, color='cyan', label='cropped')
plt.plot(ind, hist, color='black', lw=2, label='original')
plt.plot(ind, r_hist, color='red', label='Red Plane')
plt.plot(ind, g_hist, color='green', label='Green Plane')
plt.plot(ind, g_hist, color='blue', label='Blue Plane')
plt.xlim(0, 255)
plt.ylim(0, 8000)
plt.legend()

plt.show()


