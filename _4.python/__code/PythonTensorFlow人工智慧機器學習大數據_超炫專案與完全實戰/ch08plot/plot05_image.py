#!/usr/bin/env
# -*- coding: utf-8 -*-
__author__ = "Powen Ko, www.powenko.com"

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
t=[10,20,30,40]


plt.xlabel('xlabel')
plt.ylabel('ylabel')
plt.title('title')

img=mpimg.imread('powenko.png')
imgplot = plt.imshow(img)

plt.plot(t, t, 'r--')
plt.text(70, 10, 'Hello! powenko.com')
plt.savefig('my.png')
plt.show()