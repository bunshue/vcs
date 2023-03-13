import matplotlib.pyplot as plt
import numpy as np

with open('data\yrborn.txt', 'r') as fp:
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

plt.subplot(211)
plt.plot(ind, bp)
plt.xlim(1986,2015)
plt.title('1986 - 2015 (Total)')

plt.subplot(212)
plt.bar(ind, bp_b, width, color='b')
plt.bar(ind+0.35, bp_g, width, color='r')
plt.xlim(1986,2015)
plt.title('1986 - 2015 (Boy:Girl)')

plt.show()
