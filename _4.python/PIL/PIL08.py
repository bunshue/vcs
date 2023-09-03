print('------------------------------------------------------------')	#60個
print('萃取圖片的輪廓')

import matplotlib.pyplot as plt
from PIL import Image

# 讀入圖片
image1 = Image.open('sample.png')
plt.imshow(image1)

plt.show()

# 圖片大小
width, height = image1.size

# 輸出用
image2 = Image.new('RGB', (width, height))

#全彩轉灰階
image1 = image1.convert("L")

# 萃取輪廓
for y in range(0, height - 1):
    for x in range(0, width - 1):
        # 計算亮度差
        diff_x = image1.getpixel((x + 1, y)) - image1.getpixel((x, y))
        diff_y = image1.getpixel((x, y + 1)) - image1.getpixel((x, y))
        diff = diff_x + diff_y
        
        # 輸出
        if diff >= 20:
            image2.putpixel((x, y), (255, 0, 0))   #亮度差較大 著紅色
        else:
            image2.putpixel((x, y), (0, 0, 0))     #亮度差較小 著黑色

plt.imshow(image2)

plt.show()

print('------------------------------------------------------------')	#60個
