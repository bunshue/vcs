import sys

import matplotlib.pyplot as plt
from PIL import Image

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/flower.jpg'

print('------------------------------------------------------------')	#60個

from PIL import Image

image = Image.open(filename)

r, g, b = image.split()

convert_image = Image.merge('RGB', (b, g, r))

plt.imshow(convert_image)
plt.show()

#convert_image.save('rgb_to_bgr.jpg')

print('------------------------------------------------------------')	#60個

from PIL import Image

image = Image.open(filename)

black_and_white = image.convert('1')

plt.imshow(black_and_white)
plt.show()

#black_and_white.save('b_and_w.jpg')

print('------------------------------------------------------------')	#60個

from PIL import Image

image = Image.open(filename)

gray_iamge = image.convert('L')

plt.imshow(gray_iamge)
plt.show()

#gray_iamge.save('gray_image.jpg') 

print('------------------------------------------------------------')	#60個

from PIL import Image

image = Image.open(filename)

rotate_image = image.transpose(Image.ROTATE_90)
plt.imshow(rotate_image)
plt.show()

#rotate_image.save('rotate_90.jpg')#儲存90度旋轉的圖片

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


