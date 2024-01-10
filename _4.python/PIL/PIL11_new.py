'''
PIL 新進

'''

import numpy as np
import torchvision.transforms as transforms
from PIL import Image
import matplotlib.pyplot as plt

print('------------------------------------------------------------')	#60個

'''
from PIL import Image,ImageDraw
image = Image.open("captcha.png").convert("L")	#轉換成灰階圖像
'''


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


#PIL之基本設定


''' not ready
from PIL import Image, ImageDraw, ImageFont

filename1 = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg'

im = Image.open(filename1)



filename2 = 'C:/_git/vcs/_1.data/______test_files2/picture1_partial.jpg'
image3 = image1.resize((100, 500), Image.ANTIALIAS)

image = Image.open(filename)    #PIL讀取本機圖片, 讀取的是RGB格式的圖片


'''

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個


"""
PIL 偽彩色圖像處理

"""

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

print('------------------------------------------------------------')	#60個

#filename = 'C:/_git/vcs/_1.data/______test_files1/pic_256X100.png'
filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

image = Image.open(filename)

#彩色轉黑白
# 轉換為灰度圖像
gray_image = image.convert('L')

#3. 偽彩色處理

#偽彩色處理可以通過將灰度值映射到彩色值來實現。通常，我們使用一個顏色映射表（Color Map）來定義灰度和彩色之間的映射關系。
#在Python中，可以使用matplotlib庫來生成顏色映射表并將灰度圖像轉換為彩色圖像。

# 定義顏色映射表
cmap = plt.get_cmap('jet')

# 將灰度圖像轉換為彩色圖像
color_image = cmap(np.array(gray_image))

# 顯示彩色圖像
plt.imshow(color_image)
plt.axis('off')
plt.show()

#上述代碼中，我們使用get_cmap方法獲取了一個名為’jet’的顏色映射表。然后，將灰度圖像轉換為NumPy數組，再將數組應用于顏色映射表，得到彩色圖像。


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個



filename1 = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/red_300X300.bmp'
filename2 = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/green_300X300.bmp'

filename1 = 'C:/_git/vcs/_1.data/______test_files1/picture2.jpg'
filename2 = 'C:/_git/vcs/_1.data/______test_files1/picture1.bmp'

'''
平均雜湊（aHash）
ahash:          Average hash
hashfunc = imagehash.average_hash
感知雜湊（pHash）
phash:          Perceptual hash
hashfunc = imagehash.phash
差異雜湊（dHash）
dhash:          Difference hash
hashfunc = imagehash.dhash
小波雜湊（wHash）
whash-haar:     Haar wavelet hash
hashfunc = imagehash.whash
whash-db4:      Daubechies wavelet hash
imagehash.whash(img, mode='db4')
colorhash:      HSV color hash
hashmethod == 'crop-resistant':
crop-resistant: Crop-resistant hash
imagehash.crop_resistant_hash
'''

from PIL import Image
import imagehash
hash1 = imagehash.average_hash(Image.open(filename1))
print(hash1)
hash2 = imagehash.average_hash(Image.open(filename2))
print(hash2)

if hash1 == hash2:
    print('兩圖相同')
else:
    print('兩圖不同')



print('------------------------------------------------------------')	#60個

from PIL import Image   # Importing Image class from PIL module

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/green_300X300.bmp'

#純圖片指定座標取得顏色方法
def rgb_of_pixel(img_path, x, y):
    im = Image.open(img_path).convert('RGB')
    r, g, b = im.getpixel((x, y))
    a = (r, g, b)
    return a

print(rgb_of_pixel(filename, 131, 81))


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個



print('完成')
