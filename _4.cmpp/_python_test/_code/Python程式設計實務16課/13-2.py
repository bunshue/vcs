# _*_ coding: utf-8 _*_
# 程式 13-2 (Python 3 Version)

import matplotlib.pyplot as pt
import numpy as np

with open('popu.txt', 'r') as fp:
	populations = fp.readlines()

city = list()
popu = list()

for p in populations:
	cc, pp = p.split(',')
	city.append(cc)
	popu.append(int(pp))

ind = np.arange(len(city))

pt.bar(ind, popu)
pt.xticks(ind+0.5, city)
pt.title('Program 13-2')
pt.show()
