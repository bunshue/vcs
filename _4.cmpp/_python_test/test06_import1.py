# 各種import

import sys
print("打印系統路徑")
print(sys.path)


import math

print("pi = ",math.pi)
print("pi = " + str(math.pi))

for count in range(20):
    print("sin(" + str(count) + ") = " + str(math.sin(2*math.pi*count/360)) + ", cos(" + str(count) + ") = " + str(math.cos(2*math.pi*count/360)))



import math
nums = [1,2,3,4,5,6,7,8,9,10]
result = math.fsum(nums)
print(result)

n = 16
r = math.sqrt(n)
print(r)


import math
content = dir(math)
print(content)




import os
os.system("ls")
os.system("pause")


import my_print  #把整個 my_print.py 都引進來
print("測試導入自定義模組")
my_print.print_func("Python")


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

