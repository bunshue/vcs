# _*_ coding: utf-8 _*_
# 程式 13-8 (Python 2 Version)

import matplotlib.pyplot as pt
import numpy as np
from PIL import Image

sample = Image.open('sample.jpg')
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
pt.plot(ind, crop_hist, color='cyan', label='cropped')
pt.plot(ind, hist, color='black', lw=2, label='original')
pt.plot(ind, r_hist, color='red', label='Red Plane')
pt.plot(ind, g_hist, color='green', label='Green Plane')
pt.plot(ind, g_hist, color='blue', label='Blue Plane')
pt.xlim(0,255)
pt.ylim(0,8000)
pt.legend()
pt.show()