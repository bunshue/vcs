# _*_ coding: utf-8 _*_
# 程式 13-5 (Python 3 Version)

import matplotlib.pyplot as pt
import numpy as np

def f1(x):
    return int(float(bp[x])/float(school[x]))

def f2(x):
    return float(float(school[x])/float(bp[x]))

with open('school.txt', 'r') as fp:
    schools = fp.readlines()

school = list()
for s in schools:
    school.append(int(s.split()[1]))

with open('yrborn.txt', 'r') as fp:
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
pt.subplot(221)
pt.plot(yr, bp, lw=2)
pt.xlim(1986,2015)
pt.title('1986 - 2015 (Total)')

pt.subplot(222)
pt.plot(yr, school,lw=2)
pt.xlim(1986,2015)
pt.title('1986 - 2015 School Numbers')

pt.subplot(223)
pt.plot(yr, list(map(f1, ind)), lw=2)
pt.xlim(1986,2015)
pt.title('Person/School')

pt.subplot(224)
pt.plot(yr, list(map(f2, ind)), lw=2, color='r')
pt.xlim(1986,2015)
pt.title('School/Person')
pt.show()
