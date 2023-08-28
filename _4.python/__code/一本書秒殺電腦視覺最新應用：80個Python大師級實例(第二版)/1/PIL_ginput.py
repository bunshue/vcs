from PIL import Image
from pylab import *

im = array(Image.open('house2.jpg'))
imshow(im)

print('请点击3个点')
x = ginput(3)
print('你已点击:', x)
show()
