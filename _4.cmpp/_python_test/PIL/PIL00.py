#PIL有九種不同模式: 1，L，P，RGB，RGBA，CMYK，YCbCr，I，F。
#呼叫預設程式開啟圖片

'''
PIL保存圖片的方式，調用方法 Image.save() 即可，保存的是RGB格式的圖片。

'''

from PIL import Image

filename = 'C:/_git/vcs/_4.cmpp/_python_test/data/sample.jpg'

image = Image.open(filename)    #讀取的是RGB格式的圖片
image.show()

    
# 輸出圖片維度
print("image_shape: ", image.size)
w, h = image.size
print(w)
print(h)

#轉為二值圖像，非黑即白。每個像素用8個bit表示，0表示黑，255表示白。
image_1 = image.convert('1')	#轉換成二值化圖像
image_1.show()

#轉為灰度圖像，每個像素用8個bit表示，0表示黑，255表示白，其他數字表示不同的灰度。
#轉換公式：L = R * 299/1000 + G * 587/1000+ B * 114/1000。
image_L = image.convert('L')	#轉換成灰階圖像
image_L.show()

'''
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

print('OK')
