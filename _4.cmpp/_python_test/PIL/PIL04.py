import matplotlib.pyplot as plt

from PIL import Image

#filename = 'C:/______test_files/_emgu/lena.jpg'
filename = 'C:/______test_files/picture1.jpg'

'''
image1 = Image.open(filename)
  
image = Image.open(filename)
image_1 = image.convert('1')

plt.subplot(121)
plt.imshow(image)
plt.subplot(122)
plt.imshow(image_1)

plt.show()
'''


im=Image.open(filename)

image=im.resize((305*1, 400//2))  #修改圖像大小

plt.imshow(image)
plt.show()


print("作業完成")

