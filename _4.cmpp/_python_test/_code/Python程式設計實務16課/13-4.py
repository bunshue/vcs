# _*_ coding: utf-8 _*_
# 程式 13-4 (Python 3 Version)

import matplotlib.pyplot as pt
import numpy as np

with open('yrborn.txt', 'r') as fp:
	populations = fp.readlines()

yrborn = dict()

for p in populations:
    yr, tl, boy, girl = p.split()
    yrborn[yr] = {'boy': int(boy), 'girl': int(girl)}

ind = np.arange(1986,2016)
yrlist = sorted(list(yrborn.keys()))
bp = list()
bp_b = list()
bp_g = list()
for yr in yrlist:
    boys = yrborn[yr]['boy']
    girls = yrborn[yr]['girl']
    bp.append(boys + girls)
    bp_b.append(boys)
    bp_g.append(girls)

width = 0.35
pt.subplot(211)
pt.plot(ind, bp)
pt.xlim(1986,2015)
pt.title('1986 - 2015 (Total)')

pt.subplot(212)
pt.bar(ind, bp_b, width, color='b')
pt.bar(ind+0.35, bp_g, width, color='r')
pt.xlim(1986,2015)
pt.title('1986 - 2015 (Boy:Girl)')

pt.show()
