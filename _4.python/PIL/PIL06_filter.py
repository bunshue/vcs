"""

濾鏡效果


"""

import os
import sys
import time
import random
import matplotlib.pyplot as plt
import numpy as np
import math

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'

print('------------------------------------------------------------')	#60個

print("濾鏡效果")

from PIL import Image, ImageFilter

image = Image.open(filename)
image.filter(ImageFilter.CONTOUR).show()


print("------------------------------------------------------------")  # 60個

from PIL import ImageFilter

image = Image.open(filename)       # 建立Pillow物件
filterPict = image.filter(ImageFilter.BLUR)
filterPict.save("tmp_pic20_BLUR.jpg")

filterPict = image.filter(ImageFilter.CONTOUR)
filterPict.save("tmp_pic21_CONTOUR.jpg")

filterPict = image.filter(ImageFilter.EMBOSS)
filterPict.save("tmp_pic22_EMBOSS.jpg")

filterPict = image.filter(ImageFilter.FIND_EDGES)
filterPict.save("tmp_pic23_FIND_EDGES.jpg")

print("------------------------------------------------------------")  # 60個



from PIL import Image, ImageFilter

image = Image.open(filename)
width, height = image.size

"""
image.show()
image.transpose(Image.FLIP_LEFT_RIGHT).show()
image.filter(ImageFilter.GaussianBlur(4)).show()
image.filter(ImageFilter.EMBOSS).show()
image.thumbnail((width // 4, height // 4))
image.show()
"""

print('------------------------------------------------------------')	#60個

#filter
from PIL import Image,ImageFilter
image=Image.open(filename)
image2=image.filter(ImageFilter.EDGE_ENHANCE)
#image2.show()

print('------------------------------------------------------------')	#60個

from PIL import Image,ImageFilter

image = Image.open(filename)
image_new = image.filter(ImageFilter.EDGE_ENHANCE)
#image_new.show()

print("------------------------------------------------------------")  # 60個



from PIL import Image, ImageFilter

image = Image.open(filename)
plt.imshow(image)
plt.title('原圖')
plt.show()

new = image.filter(ImageFilter.EDGE_ENHANCE)
plt.imshow(new)
plt.title('after filter')
plt.show()

print('------------------------------------------------------------')	#60個


from PIL import Image,ImageFilter

image=Image.open(filename)
image_new=image.filter(ImageFilter.EDGE_ENHANCE)
#image_new.show()

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'

from PIL import Image
from PIL import ImageFilter
rushMore = Image.open(filename)       # 建立Pillow物件
filterPict = rushMore.filter(ImageFilter.BLUR)
filterPict.save("tmp_pic_4_BLUR.png")
filterPict = rushMore.filter(ImageFilter.CONTOUR)
filterPict.save("tmp_pic_4_CONTOUR.png")
filterPict = rushMore.filter(ImageFilter.DETAIL)
filterPict.save("tmp_pic_4_DETAIL.png")
filterPict = rushMore.filter(ImageFilter.EDGE_ENHANCE)
filterPict.save("tmp_pic_4_EDGE_ENHANCE.png")
filterPict = rushMore.filter(ImageFilter.EDGE_ENHANCE_MORE)
filterPict.save("tmp_pic_4_EDGE_ENHANCE_MORE.png")
filterPict = rushMore.filter(ImageFilter.EMBOSS)
filterPict.save("tmp_pic_4_EMBOSS.png")
filterPict = rushMore.filter(ImageFilter.FIND_EDGES)
filterPict.save("tmp_pic_4_FIND_EDGES.png")
filterPict = rushMore.filter(ImageFilter.SMOOTH)
filterPict.save("tmp_pic_4_SMOOTH.png")
filterPict = rushMore.filter(ImageFilter.SMOOTH_MORE)
filterPict.save("tmp_pic_4_SMOOTH_MORE.png")
filterPict = rushMore.filter(ImageFilter.SHARPEN)
filterPict.save("tmp_pic_4_SHARPEN.png")

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'

from PIL import Image,ImageFilter

img = Image.open(filename)

imgFilter=img.filter(ImageFilter.BLUR)   #模擬

imgFilter=img.filter(ImageFilter.CONTOUR)#輪廓

imgFilter=img.filter(ImageFilter.EMBOSS) #浮雕

imgFilter=img.filter(ImageFilter.SHARPEN)#銳化

print("------------------------------------------------------------")  # 60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個




