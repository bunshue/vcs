# subplot 畫兩圖

import matplotlib.pyplot as plt
import numpy as np

filename = 'C:/_git/vcs/_4.cmpp/_python_test/data/yrborn.txt'

with open(filename, 'r') as fp:
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

plt.subplot(211)
plt.plot(bp)
plt.xlim(0,len(bp)-1)
plt.title('1986 - 2015 (Total)')

plt.subplot(212)
plt.plot(bp_b)
plt.plot(bp_g)
plt.xlim(0,len(bp_b)-1)
plt.title('1986 - 2015 (Boy:Girl)')

plt.show()
