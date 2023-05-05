#PIL有九種不同模式: 1，L，P，RGB，RGBA，CMYK，YCbCr，I，F。
#呼叫預設程式開啟圖片

import numpy as np
import torchvision.transforms as transforms
from PIL import Image

filename = 'C:/_git/vcs/_1.data/______test_files1/sample.jpg'

image = Image.open(filename)    #讀取的是RGB格式的圖片
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
image_file = Image.open(filename)
r, g, b = image_file.split()
convert_image = image_file.merge('RGB', (b, g, r))
convert_image.save('image_bgr.png')
'''




print('OK')
