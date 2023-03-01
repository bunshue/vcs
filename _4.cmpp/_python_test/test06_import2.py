# 各種import


#圖形操作
#需先 pip install pillow
from PIL import Image, ImageFilter
#讀取圖形
im = Image.open('bear.jpg')
#顯示圖形
#im.show()

#對圖形套用過濾器
im_sharp = im.filter(ImageFilter.SHARPEN)

#儲存過濾過的圖形到新檔案
im_sharp.save('bear_sharpen.jpg', 'JPEG')

#分解圖形顏色 例如RGB的紅綠藍
r,g,b = im_sharp.split()

#檢視圖形內嵌的EXIF資料
exif_data = im._getexif()
print(exif_data)



import os.path
filesize = os.path.getsize(filename_r)
print("filesize : " , filesize)

print("檔案時間 : ", os.path.getmtime(filename_r))
import time
print("檔案時間 : ", time.ctime(os.path.getmtime(filename_r)))


print("檔案是否存在 : ", os.path.isfile(filename_r))

import os
files = os.listdir('.')
print("列出所有檔案", files)


