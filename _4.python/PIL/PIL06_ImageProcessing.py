"""

PIL 之 影像處理


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

from PIL import Image
from PIL import ImageColor
from PIL import ImageDraw

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

from PIL import Image, ImageEnhance

img = Image.open("oxxostudio.png")  # 開啟影像
brightness = ImageEnhance.Brightness(img)  # 設定 img 要加強亮度
output = brightness.enhance(factor)  # 調整亮度，factor 為一個浮點數值
# 調整後的數值 = 原始數值 x factor


print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageEnhance

img = Image.open("oxxostudio.jpg")  # 開啟影像
brightness = ImageEnhance.Brightness(img)  # 設定 img 要加強亮度
output = brightness.enhance(1.5)  # 提高亮度
output.save("tmp_oxxostudio_b15.jpg")  # 存檔

output = brightness.enhance(0.5)  # 降低亮度
output.save("tmp_oxxostudio_b05.jpg")  # 存檔



print('------------------------------------------------------------')	#60個


print("------------------------------------------------------------")  # 60個


from PIL import Image, ImageFilter

img = Image.open("oxxostudio.jpg")  # 開啟圖片
output = img.filter(ImageFilter.BLUR)  # 套用基本模糊化
output.save("tmp_output.jpg")
# output.show()  # Colab 不支援直接顯示，如果使用本機環境會開啟圖片檢視器


print("------------------------------------------------------------")  # 60個


from PIL import Image, ImageFilter

img = Image.open("oxxostudio.jpg")
output = img.filter(ImageFilter.BoxBlur(5))  # 套用 BoxBlur，設定模糊半徑為 5
output.save("tmp_output.jpg")


print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageFilter

img = Image.open("oxxostudio.jpg")
output = img.filter(ImageFilter.GaussianBlur(5))  # 套用 GaussianBlur，設定模糊半徑為 5
output.save("tmp_output.jpg")

print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageFilter

img = Image.open("oxxostudio.jpg")
output = img.filter(
    ImageFilter.UnsharpMask(radius=5, percent=-100, threshold=3)
)  # 套用 UnsharpMask
output.show()


print("------------------------------------------------------------")  # 60個


from PIL import Image, ImageFilter

img = Image.open("oxxostudio.jpg")  # 開啟圖片
output = img.filter(ImageFilter.SHARPEN)  # 套用圖片銳利化
output.save("tmp_output.jpg")  # 存檔
# output.show()  # Colab 不支援直接顯示，如果使用本機環境會開啟圖片檢視器


print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageFilter

img = Image.open("oxxostudio.jpg")
for i in range(3):
    img = img.filter(ImageFilter.SHARPEN)

print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageFilter

img = Image.open("oxxostudio.jpg")
output = img.filter(
    ImageFilter.UnsharpMask(radius=5, percent=100, threshold=10)
)  # 套用 UnsharpMask
output.show()



print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個




