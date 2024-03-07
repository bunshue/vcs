'''
PIL 基本使用

顯示圖片

顯示圖片訊息

'''

import sys
import matplotlib.pyplot as plt
from PIL import Image   # Importing Image class from PIL module

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

print('------------------------------------------------------------')	#60個

import PIL
print('查詢 PIL 版本')
print(PIL.__version__)

print('------------------------------------------------------------')	#60個

print('顯示原圖')

image1 = Image.open(filename)    #建立Pillow物件 PIL讀取本機圖片, RGB模式
plt.imshow(image1)

plt.show()

print('顯示圖片訊息')
print("列出物件檔名 : ", image1.filename)
print("列出物件型態 : ", type(image1))
print("列出物件副檔名 : ", image1.format)
print("列出物件描述   : ", image1.format_description)
print("列出物件模式   : ", image1.mode)

W, H = image1.size
print('原圖大小 W =', W, ', H =', H)

print('圖片維度 圖片資訊')
print('Size : ', image1.size, 'Mode : ', image1.mode, 'Format : ', image1.format)

image1.close()

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

"""
#PIL 存圖
print('圖片另存新檔')
image1.save('tmp_image1.jpg')
image1.save('tmp_image2.jpg', 'JPEG')
image1.save('tmp_image3.png')
image1.save('tmp_image4.png', 'PNG')
image1.save('tmp_image5.bmp') 

"""




print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個





from PIL import Image

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

im = Image.open(filename)
print("%s:" % filename, im.format, "%dx%d" % im.size, im.mode)
print(im.info, im.tile)



