# plot 集合

import matplotlib.pyplot as plt
import numpy as np

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

#          編號               圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(num = 'plot 集合', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

#第一張圖
plt.subplot(231)

# 2D random walk
#fig2, ax2 = plt.subplots(num="Figure_2")

prng = np.random.RandomState(123)

x = np.linspace(0, 10, 101)

def random_walk(xy0=(0.0, 0.0), nsteps=100, std=1.0):
    xy = np.zeros((nsteps + 1, 2))
    xy[0,:] = xy0
    deltas = prng.normal(loc=0.0, scale=std, size=(nsteps, 2))
    xy[1:, :] = xy[0, :] + np.cumsum(deltas, axis=0)
    return xy

for cnt in range(3):
    traj = random_walk()
    plt.plot(traj[:, 0], traj[:, 1], label="Traj. {c}".format(c=cnt))

#ax2.legend(loc='best')


#第二張圖
plt.subplot(232)


#第三張圖
plt.subplot(233)



#第四張圖
plt.subplot(234)


#第五張圖
plt.subplot(235)


#第六張圖
plt.subplot(236)



plt.show()

print('------------------------------------------------------------')	#60個

# plot 集合

#          編號               圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(num = 'plot 集合', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

def f1(x):
    return int(float(bp[x])/float(school[x]))

def f2(x):
    return float(float(school[x])/float(bp[x]))

filename = 'C:/_git/vcs/_1.data/______test_files1/school.txt'
with open(filename, 'r') as fp:
    schools = fp.readlines()

school = list()
for s in schools:
    school.append(int(s.split()[1]))

#共取得??筆資料 list的用法

filename = 'C:/_git/vcs/_1.data/______test_files1/yrborn.txt'
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

print('------------------------------------------------------------')	#60個

# plot 集合

#          編號               圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(num = 'plot 集合', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

#第1~2張圖
filename = 'C:/_git/vcs/_1.data/______test_files1/yrborn.txt'

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

filename = 'C:/_git/vcs/_1.data/______test_files1/yrborn.txt'

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




