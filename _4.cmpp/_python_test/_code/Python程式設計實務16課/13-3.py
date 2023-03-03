# _*_ coding: utf-8 _*_
# 程式 13-3 (Python 3 Version)

import matplotlib.pyplot as pt
import numpy as np

with open('yrborn.txt', 'r') as fp:
	populations = fp.readlines()

yrborn = dict()

for p in populations:
    yr, tl, boy, girl = p.split()
    yrborn[yr] = {'boy': int(boy), 'girl': int(girl)}

ind = np.arange(len(yrborn))
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

pt.subplot(211)
pt.plot(bp)
pt.xlim(0,len(bp)-1)
pt.title('1986 - 2015 (Total)')
pt.subplot(212)
pt.plot(bp_b)
pt.plot(bp_g)
pt.xlim(0,len(bp_b)-1)
pt.title('1986 - 2015 (Boy:Girl)')
pt.show()
