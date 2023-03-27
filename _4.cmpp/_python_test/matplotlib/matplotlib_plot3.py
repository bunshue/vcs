# plot 集合

selected_font = 'C:/_git/vcs/_4.cmpp/_python_test/data/msch.ttf'

import matplotlib.pyplot as plt
import numpy as np

#plt.figure(figsize=(8,8))	#設定圖片視窗大小
plt.figure(num = 'plot 集合 6', figsize=[20, 15], dpi=84, facecolor="whitesmoke", edgecolor="r", linewidth=1, frameon=True)
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

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

#共取得??筆資料 list的用法

filename = 'C:/_git/vcs/_4.cmpp/_python_test/data/yrborn.txt'
with open(filename, 'r') as fp:
	populations = fp.readlines()

yrborn = dict()

for p in populations:
    yr, tl, boy, girl = p.split()
    yrborn[yr] = {'boy': int(boy), 'girl': int(girl)}

#共取得??筆資料 dict的用法
    
yrlist = sorted(list(yrborn.keys()))
bp = list()
for yr in yrlist:
    boys = yrborn[yr]['boy']
    girls = yrborn[yr]['girl']
    bp.append(boys + girls)
yr = range(1986, 2016)
ind = np.arange(len(bp))

#第一張圖
plt.subplot(231)

plt.plot(yr, bp, lw=2)
plt.xlim(1986,2015)
plt.title('1986 - 2015 (Total)')

#第二張圖
plt.subplot(232)

plt.plot(yr, school,lw=2)
plt.xlim(1986,2015)
plt.title('1986 - 2015 School Numbers')

#第三張圖
plt.subplot(233)

plt.plot(yr, list(map(f1, ind)), lw=2)
plt.xlim(1986,2015)
plt.title('Person/School')

#第四張圖
plt.subplot(234)

plt.plot(yr, list(map(f2, ind)), lw=2, color='r')
plt.xlim(1986,2015)
plt.title('School/Person')

#第五張圖
plt.subplot(235)



#第六張圖
plt.subplot(236)

plt.show()


