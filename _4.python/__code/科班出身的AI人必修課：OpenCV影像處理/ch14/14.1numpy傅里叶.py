import cv2
import numpy as np
import matplotlib.pyplot as plt

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
img = cv2.imread(filename, 0)

f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))

plt.subplot(121)
plt.imshow(img, cmap = 'gray')
plt.title('original')
plt.axis('off')

plt.subplot(122)
plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('result')
plt.axis('off')

plt.show()
