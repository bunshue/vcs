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


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個



print('完成')
