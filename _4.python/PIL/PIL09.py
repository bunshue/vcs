import sys

print('------------------------------------------------------------')	#60個

filename = 'flower.jpg'

from PIL import Image

image = Image.open(filename)

r, g, b = image.split()

convert_image = Image.merge('RGB', (b, g, r))

convert_image.show()

#convert_image.save('rgb_to_bgr.jpg')

print('------------------------------------------------------------')	#60個

from PIL import Image

image = Image.open(filename)

black_and_white = image.convert('1')

black_and_white.show()

#black_and_white.save('b_and_w.jpg')

print('------------------------------------------------------------')	#60個

from PIL import Image

image = Image.open(filename)

gray_iamge = image.convert('L')

gray_iamge.show()

#gray_iamge.save('gray_image.jpg') 

print('------------------------------------------------------------')	#60個

from PIL import Image

image = Image.open(filename)

image.transpose(Image.ROTATE_90).show()

#image.transpose(Image.ROTATE_90).save('rotate_90.jpg')#儲存90度旋轉的圖片


print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


