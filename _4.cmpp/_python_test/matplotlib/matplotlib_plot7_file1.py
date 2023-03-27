# plot 集合

selected_font = 'C:/_git/vcs/_4.cmpp/_python_test/data/msch.ttf'

import matplotlib.pyplot as plt
import numpy as np

#plt.figure(figsize=(8,8))	#設定圖片視窗大小
plt.figure(num = 'plot 集合', figsize=[20, 15], dpi=84, facecolor="whitesmoke", edgecolor="r", linewidth=1, frameon=True)
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示


#第1~2張圖
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

#第一張圖
plt.subplot(231)

plt.plot(bp)
plt.xlim(0,len(bp)-1)
plt.title('1986 - 2015 (Total)')

#第二張圖
plt.subplot(232)

plt.plot(bp_b)
plt.plot(bp_g)
plt.xlim(0,len(bp_b)-1)
plt.title('1986 - 2015 (Boy:Girl)')


#第3~4張圖

filename = 'C:/_git/vcs/_4.cmpp/_python_test/data/yrborn.txt'

with open(filename, 'r') as fp:
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

#第三張圖
plt.subplot(233)

plt.plot(ind, bp)
plt.xlim(1986,2015)
plt.title('1986 - 2015 (Total)')

#第四張圖
plt.subplot(234)
plt.bar(ind, bp_b, width, color='b')
plt.bar(ind+0.35, bp_g, width, color='r')
plt.xlim(1986,2015)
plt.title('1986 - 2015 (Boy:Girl)')



#第五張圖
plt.subplot(235)



#第六張圖
plt.subplot(236)



plt.show()






# subplot 畫兩圖





plt.show()
