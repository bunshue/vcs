from PIL import Image

filename = 'C:/______test_files/picture1.jpg'

import cv2
from matplotlib import pyplot as plt

img = cv2.imread(filename)

plt.imshow(img)
plt.show()



