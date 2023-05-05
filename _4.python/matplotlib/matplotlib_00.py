'''
matplotlib 基本使用

顯示圖片

'''

filename = 'C:/______test_files2/human1.jpg'

print('使用 matplotlib 顯示一圖')
import matplotlib.pyplot as plt
import matplotlib.image as img

image = img.imread(filename)

plt.imshow(image)	#顯示圖片, 兩行都要
plt.show()              #顯示圖片, 兩行都要




