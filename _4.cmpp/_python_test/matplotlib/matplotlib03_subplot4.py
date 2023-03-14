# subplot 畫4圖

import matplotlib.pyplot as plt
import numpy as np

def f1(x):
    return int(float(bp[x])/float(school[x]))

def f2(x):
    return float(float(school[x])/float(bp[x]))

filename = 'C:/_git/vcs/_4.cmpp/_python_test/data/school.txt'
with open(filename, 'r') as fp:
    schools = fp.readlines()

school = list()
for s in schools:
    school.append(int(s.split()[1]))

filename = 'C:/_git/vcs/_4.cmpp/_python_test/data/yrborn.txt'
with open(filename, 'r') as fp:
	populations = fp.readlines()

yrborn = dict()

for p in populations:
    yr, tl, boy, girl = p.split()
    yrborn[yr] = {'boy': int(boy), 'girl': int(girl)}

yrlist = sorted(list(yrborn.keys()))
bp = list()
for yr in yrlist:
    boys = yrborn[yr]['boy']
    girls = yrborn[yr]['girl']
    bp.append(boys + girls)
yr = range(1986, 2016)
ind = np.arange(len(bp))

plt.subplot(221)
plt.plot(yr, bp, lw=2)
plt.xlim(1986,2015)
plt.title('1986 - 2015 (Total)')

plt.subplot(222)
plt.plot(yr, school,lw=2)
plt.xlim(1986,2015)
plt.title('1986 - 2015 School Numbers')

plt.subplot(223)
plt.plot(yr, list(map(f1, ind)), lw=2)
plt.xlim(1986,2015)
plt.title('Person/School')

plt.subplot(224)
plt.plot(yr, list(map(f2, ind)), lw=2, color='r')
plt.xlim(1986,2015)
plt.title('School/Person')

plt.show()

