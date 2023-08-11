filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'


#裁剪圖片 plt

import matplotlib.pyplot as plt
import matplotlib.image as img

image = img.imread(filename)

plt.imshow(image)	#顯示圖片, 兩行都要
plt.show()              #顯示圖片, 兩行都要

x_l, x_r = 150, 350 #保留的部分，由左而右
y_u, y_d = 150, 400 #保留的部分，由上而下
cut_img = image[y_u:y_d, x_l:x_r]

plt.imshow(cut_img)	#顯示圖片, 兩行都要
plt.show()              #顯示圖片, 兩行都要



