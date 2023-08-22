print('------------------------------------------------------------')	#60個
print('萃取圖片的輪廓')

import matplotlib.pyplot as plt
from PIL import Image

# 讀入圖片
src_img = Image.open('sample.png')
plt.imshow(src_img)
plt.show()

# 圖片大小
width, height = src_img.size

# 輸出用
dst_img = Image.new('RGB', (width, height))

# 彩色 -> 單色
src_img = src_img.convert("L")

# 萃取輪廓
for y in range(0, height-1):
    for x in range(0, width-1):
        # 計算亮度差
        diff_x = src_img.getpixel((x+1, y)) - src_img.getpixel((x, y))
        diff_y = src_img.getpixel((x, y+1)) - src_img.getpixel((x, y))
        diff = diff_x + diff_y
        
        # 輸出
        if diff >= 20:
            dst_img.putpixel((x, y), (255, 255, 255))
        else:
            dst_img.putpixel((x, y), (0, 0, 0))
plt.imshow(dst_img)
plt.show()




print('------------------------------------------------------------')	#60個


