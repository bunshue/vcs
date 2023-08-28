# ch2_22.py
import matplotlib.pyplot as plt
import matplotlib.image as img

pict = img.imread('out2_20.png')
plt.axis('off')
plt.imshow(pict)
plt.show()


