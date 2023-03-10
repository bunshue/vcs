import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

sample = Image.open('data\sample.jpg')
im = sample.convert('L')
w, h = im.size

crop = im.crop((w/2-300, h/2-300, w/2+300, h/2+300))
crop_hist = crop.histogram()

ori = sample.resize((600,600))
im = ori.convert('L')
hist = im.histogram()

r, g, b = ori.split()
r_hist = r.histogram()
g_hist = g.histogram()
b_hist = b.histogram()

ind = np.arange(0, len(crop_hist))
plt.plot(ind, crop_hist, color='cyan', label='cropped')
plt.plot(ind, hist, color='black', lw=2, label='original')
plt.plot(ind, r_hist, color='red', label='Red Plane')
plt.plot(ind, g_hist, color='green', label='Green Plane')
plt.plot(ind, g_hist, color='blue', label='Blue Plane')
plt.xlim(0,255)
plt.ylim(0,8000)
plt.legend()

plt.show()
