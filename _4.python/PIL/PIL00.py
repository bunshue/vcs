'''
PIL 基本使用

顯示圖片

顯示圖片訊息

'''

import sys
import matplotlib.pyplot as plt
from PIL import Image   # Importing Image class from PIL module

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

print('------------------------------------------------------------')	#60個

print('顯示原圖')

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

image1 = Image.open(filename)    #建立Pillow物件 PIL讀取本機圖片, RGB模式

plt.imshow(image1)

plt.show()

print('------------------------------------------------------------')	#60個

print('顯示原圖 + 圖片訊息')

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

image1 = Image.open(filename)    #建立Pillow物件 PIL讀取本機圖片, RGB模式
print("列出物件檔名 : ", image1.filename)
print("列出物件型態 : ", type(image1))
print("列出物件副檔名 : ", image1.format)
print("列出物件描述   : ", image1.format_description)

W, H = image1.size
print('原圖大小 W =', W, ', H =', H)

print('圖片維度 圖片資訊')
print('Size : ', image1.size, 'Mode : ', image1.mode, 'Format : ', image1.format)

print('圖片另存新檔')
image1.save('image_to_file.jpg')
image1.save('image_to_file.png')
image1.save('image_to_file.bmp') 

print('顯示原圖')
plt.imshow(image1)

plt.show()

print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個



