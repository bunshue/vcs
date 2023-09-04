'''
PIP 基本使用

顯示圖片

#PIL有九種不同模式: 1，L，P，RGB，RGBA，CMYK，YCbCr，I，F。
#呼叫預設程式開啟圖片
'''

import numpy as np
import torchvision.transforms as transforms
from PIL import Image
import matplotlib.pyplot as plt

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/sample.jpg'

image = Image.open(filename)    #PIL讀取本機圖片, 讀取的是RGB格式的圖片

plt.imshow(image)
plt.show()

print('圖片維度 圖片資訊')
print('Size : ', image.size, 'Mode : ', image.mode, 'Format : ', image.format)
w, h = image.size
print('寬 : ', w, '高 : ', h)

print("RGB圖像的維度：", np.array(image).shape)
image_dim_len = len(np.array(image).shape)
print("The dim of Image: ", image_dim_len)

# RGB轉換成灰階圖像
image_transforms = transforms.Compose([transforms.Grayscale(1)])

image = image_transforms(image)
# 輸出灰度圖像的維度
print("灰度圖像維度： ", np.array(image).shape)
image_dim_len = len(np.array(image).shape)
print("The dim of Image: ", image_dim_len)


#1
#轉為二值圖像，非黑即白。每個像素用8個bit表示，0表示黑，255表示白。
image_1 = image.convert('1')	#轉換成二值化圖像
plt.imshow(image_1)
plt.show()


'''
#L
#轉為灰度圖像，每個像素用8個bit表示，0表示黑，255表示白，其他數字表示不同的灰度。
#轉換公式：L = R * 299/1000 + G * 587/1000+ B * 114/1000。
image_L = image.convert('L')	#轉換成灰階圖像
plt.imshow(image_L)
plt.show()

#P
image_P = image.convert('P')
plt.imshow(image_P)
plt.show()

#RGB
image_RGB = image.convert('RGB')
plt.imshow(image_RGB)
plt.show()

#RGBA
image_RGBA = image.convert('RGBA')
plt.imshow(image_RGBA)
plt.show()

#CMYK
image_CMYK = image.convert('CMYK')
plt.imshow(image_CMYK)
plt.show()

#YCbCr
image_YCbCr = image.convert('YCbCr')
plt.imshow(image_YCbCr)
plt.show()

#I
image_I = image.convert('I')
plt.imshow(image_I)
plt.show()

#F
image_F = image.convert('F')
plt.imshow(image_F)
plt.show()

'''

'''
#90度旋轉的圖片
image_90 = image.transpose(Image.ROTATE_90)
plt.imshow(image_90)
plt.show()

'''

'''  ???
image = Image.open(filename)    #PIL讀取本機圖片
r, g, b = image.split()
convert_image = image.merge('RGB', (b, g, r))
convert_image.save('image_bgr.png')
'''

print('------------------------------------------------------------')	#60個

# PIL 測試 1

from PIL import Image
from PIL import Image, ImageFilter

filename1 = 'C:/_git/vcs/_1.data/______test_files1/bear.jpg'
filename2 = 'C:/_git/vcs/_1.data/______test_files2/bear_filter.jpg'

image = Image.open(filename1)    #PIL讀取本機圖片, 讀取的是RGB格式的圖片
plt.imshow(image)
plt.show()

#對圖形套用過濾器
im_sharp = image.filter(ImageFilter.SHARPEN)

plt.imshow(im_sharp)
plt.show()

#分解圖形顏色 例如RGB的紅綠藍
#看不出效果
r,g,b = im_sharp.split()

plt.imshow(r)
plt.show()

plt.imshow(g)
plt.show()

plt.imshow(b)
plt.show()

print('------------------------------------------------------------')	#60個

print('完成')
