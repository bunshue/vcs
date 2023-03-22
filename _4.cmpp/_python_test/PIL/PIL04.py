import matplotlib.pyplot as plt

from PIL import Image
from matplotlib import patches

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

pic = plt.imshow(image)

#在圖上作畫

#pic = plt.imshow(image, alpha = 0.5)
origin = (0, 0)
w = 305*75/100
h = 400/2*75/100
#畫出矩形
patch  = patches.Rectangle(origin, w, h, fill=False, linewidth=2, color='r')
pic.axes.add_patch(patch)

#畫多邊形
vertices = []
vertices.append((0, 0))
vertices.append((100, 0))
vertices.append((100, 100))
vertices.append((50, 150))
vertices.append((0, 100))
vertices.append((0, 0))
patch = patches.Polygon(vertices, closed=True, fill=False, linewidth=2, color='g')
pic.axes.add_patch(patch)


plt.text(100, 10, "ABCDEFG", fontsize=20, weight="bold", va="bottom", color='b')  

text = "CCCCCCC"  #取得文字
plt.text(vertices[0][0], vertices[0][1], text, fontsize=20, va="top", color='b')  #列印文字

plt.axis("off")

plt.show()


print("作業完成")

