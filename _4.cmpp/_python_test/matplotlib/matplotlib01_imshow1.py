# imshow 集合

selected_font = 'C:/_git/vcs/_4.cmpp/_python_test/data/msch.ttf'

import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np
from PIL import Image, ImageEnhance

#plt.figure(figsize=(10,10))    # 改變圖表尺寸 單位是英吋
#plt.figure(figsize=(8,8))	#設定圖片視窗大小
plt.figure(num = 'imshow 集合 1', figsize=[12, 10], dpi=84, facecolor="whitesmoke", edgecolor="r", linewidth=1, frameon=True)
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示


filename = 'C:/______test_files/_emgu/lena.jpg'

image1 = Image.open(filename)              # 開啟圖片
enhancer = ImageEnhance.Brightness(image1)   # 建立調整亮度的方法


#第一張圖
plt.subplot(231)

# 顯示原圖
plt.imshow(image1)                  # 在子圖表中繪製圖片

#第二張圖
plt.subplot(232)

# 顯示亮度 x0.5 的圖片
image2 = enhancer.enhance(0.5)  # 顯示亮度 x0.5 的圖片
plt.imshow(image2)                  # 在子圖表中繪製圖片


#第三張圖
plt.subplot(233)

image3 = enhancer.enhance(1.5)  # 顯示亮度 x1.5 的圖片
plt.imshow(image3)                  # 在子圖表中繪製圖片


#第四張圖
plt.subplot(234)


image4 = enhancer.enhance(3)    # 顯示亮度 x3 的圖片
plt.imshow(image4)                  # 在子圖表中繪製圖片


#第五張圖
plt.subplot(235)




#第六張圖
plt.subplot(236)



plt.show()




