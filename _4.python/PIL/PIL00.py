'''
PIP 基本使用

顯示圖片

#PIL有九種不同模式: 1，L，P，RGB，RGBA，CMYK，YCbCr，I，F。
#呼叫預設程式開啟圖片
'''

import numpy as np
import torchvision.transforms as transforms
from PIL import Image


print('----------------------------------------------------------------------')	#70個

filename = 'C:/_git/vcs/_1.data/______test_files1/sample.jpg'

image = Image.open(filename)    #PIL讀取本機圖片, 讀取的是RGB格式的圖片
#image.show()

'''
print('使用plt顯示圖片')
import matplotlib.pyplot as plt
plt.imshow(image)
plt.show()
'''

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
#image_1.show()

'''
#L
#轉為灰度圖像，每個像素用8個bit表示，0表示黑，255表示白，其他數字表示不同的灰度。
#轉換公式：L = R * 299/1000 + G * 587/1000+ B * 114/1000。
image_L = image.convert('L')	#轉換成灰階圖像
image_L.show()

#P
image_P = image.convert('P')
image_P.show()

#RGB
image_RGB = image.convert('RGB')
image_RGB.show()

#RGBA
image_RGBA = image.convert('RGBA')
image_RGBA.show()

#CMYK
image_CMYK = image.convert('CMYK')
image_CMYK.show()

#YCbCr
image_YCbCr = image.convert('YCbCr')
image_YCbCr.show()

#I
image_I = image.convert('I')
image_I.show()

#F
image_F = image.convert('F')
image_F.show()
'''

'''
#90度旋轉的圖片
image_90 = image.transpose(Image.ROTATE_90)
image_90.show()
'''

#PIL保存圖片的方式，調用方法 Image.save() 即可
print('影像存圖')
print('將二值畫圖像存圖')
image_1.save('image_1.png')


'''  ???
image = Image.open(filename)    #PIL讀取本機圖片
r, g, b = image.split()
convert_image = image.merge('RGB', (b, g, r))
convert_image.save('image_bgr.png')
'''

print('----------------------------------------------------------------------')	#70個

from PIL import Image

print('圖片裁剪縮放')

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
filename2 = 'C:/_git/vcs/_1.data/______test_files2/picture1_partial.jpg'

image = Image.open(filename)    #PIL讀取本機圖片

x = 100
y = 100
w = 100
h = 100

image1 = Image.open(filename)   #PIL讀取本機圖片
image2 = image1.crop((x, y, x + w, y + h))
image3 = image2.resize((100, 300), Image.ANTIALIAS)
image3.save(filename2)

print('----------------------------------------------------------------------')	#70個


# PIL 測試 1

from PIL import Image
from PIL import Image, ImageFilter

filename1 = 'C:/_git/vcs/_1.data/______test_files1/bear.jpg'
filename2 = 'C:/_git/vcs/_1.data/______test_files2/bear_filter.jpg'

image = Image.open(filename1)    #PIL讀取本機圖片, 讀取的是RGB格式的圖片
#image.show()  #顯示圖片

#對圖形套用過濾器
im_sharp = image.filter(ImageFilter.SHARPEN)

#儲存過濾過的圖形到新檔案
im_sharp.save(filename2, 'JPEG')
print("儲存過濾過的圖形, 檔案 : "+filename2);

#分解圖形顏色 例如RGB的紅綠藍
#看不出效果
r,g,b = im_sharp.split()


print('----------------------------------------------------------------------')	#70個

print('完成')
