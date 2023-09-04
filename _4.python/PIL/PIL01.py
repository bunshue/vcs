'''

裁剪圖片

'''

print('------------------------------------------------------------')	#60個

import matplotlib.pyplot as plt
from PIL import Image   # Importing Image class from PIL module

print('圖片裁剪縮放')

filename = r'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
image1 = Image.open(filename)    #PIL讀取本機圖片, RGB模式
 
width, height = image1.size
print('原圖大小 W =', width, ', H =', height)

x_st = 100
y_st = 200
w = 200
h = 200
image2 = image1.crop((x_st, y_st, x_st + w, y_st + h))

plt.imshow(image1)
plt.show()

plt.imshow(image2)
plt.show()

print('把圖轉成 100X500 大小')
image3 = image1.resize((100, 500), Image.ANTIALIAS)

plt.imshow(image3)
plt.show()

print('------------------------------------------------------------')	#60個

#在圖上寫字 OK, 只能英文字

from PIL import Image, ImageDraw, ImageFont

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/ubuntu.ttf'    #無中文
font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'      #有中文

filename = r'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
image1 = Image.open(filename)    #PIL讀取本機圖片, RGB模式

print("在圖上寫字")
dw = ImageDraw.Draw(image1)

mesg = '牡丹亭'
font = ImageFont.truetype(font_filename, 60)
#fn_w, fn_h = dw.textsize(unicode(mesg, 'utf-8'), font=font)
fn_w, fn_h = dw.textsize(str(mesg), font=font)

x = 100
y = 200
dw.text((x+5, y+5), str(mesg), font=font, fill=(25,25,25))
dw.text((x, y), str(mesg), font=font, fill=(128,255,255))

plt.imshow(image1)
plt.show()

print('------------------------------------------------------------')	#60個



