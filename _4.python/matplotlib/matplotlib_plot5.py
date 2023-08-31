import matplotlib.pyplot as plt
import numpy as np

x = range(20)
y = np.random.randn(20)
plt.plot(x, y)

plt.show()

x = np.linspace(0, 10, 200)
y = np.sin(5*x) / (1+x**2)

plt.bar(range(1,6), np.random.randint(1,30,5))

plt.show()


plt.bar(np.arange(0.6, 5), np.random.randint(1,30,5))
plt.show()

import sys
sys.exit()


#雙色的長條圖

x = np.arange(1,6)
plt.bar(x - 0.4, [3, 10, 8, 12, 6], width=0.4, ec='none', fc='#e63946')
plt.bar(x, [6, 3, 12, 5, 8], width=0.4, ec='none', fc='#7fb069')
plt.show()

#疊加型的資料
A = np.random.randint(2,15,5)
B = np.random.randint(2,15,5)
C = np.random.randint(2,15,5)
plt.bar(x, A, fc='#e63946', ec='none')
plt.bar(x, B, fc='#7fb069', ec='none', bottom = A)
plt.bar(x, C, fc='#e55934', ec='none', bottom = A+B)
plt.show()

#橫放的長條圖

x = np.arange(0.6, 6)
plt.barh(x, np.random.randint(1,15,6), fc='#e55934', ec='none')
plt.show()

#雙向的長條圖
x = np.arange(0.6,6)
A = np.random.randint(1,15,6)
B = np.random.randint(1,15,6)
plt.barh(x, A, fc='#e63946', ec='none')
plt.barh(x, -B, fc='#7fb069', ec='none')
plt.show()


'''

plt.plot(x, y, lw=3, label='$\sin$')
plt.plot(x, np.cos(x), lw=3, label='$\cos$')


圖例 legend

plt.legend()
plt.legend(loc=4)

可用 `loc` 去設圖例的位置, 依 1, 2, 3, ... 表示。


取得現在工作中 axes*

我們有時要設 axes 的背景啦等等的資訊。這時就要取得現在工作中的 axes。這一般有兩種方式, 第一種是設 subplot 時可以取得:

fig, ax = plt.subplot()

另一種是用 gca 函數:

ax = plt.gca()


'''

x = np.linspace(-2*np.pi, 2*np.pi, 200)
y = np.sin(x)

ax = plt.gca()
ax.set_facecolor('#69b8bb')
ax.set_xlim(-6,6)
ax.set_ylim(-1.2,1.2)
plt.plot(x,y,lw=5,c='white')


#移動 x, y 座標軸
ax = plt.gca()
ax.set_facecolor('#69b8bb')
ax.set_xlim(-6,6)
ax.set_ylim(-1.2,1.2)

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

plt.plot(x, y, lw=5 ,c = 'white')

#使用自定義的中文字型
import matplotlib.font_manager as fm
font_filename = 'C:/_git/vcs/_2.vcs/my_vcs_lesson_6/__MY/vcs_DrawPoem/vcs_DrawPoem/font/康楷體w5.TTC'
#font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'

#myfont = fm.FontProperties(fname="/Users/mac/Library/Fonts/NotoSansHant-Medium.otf")
myfont = fm.FontProperties(fname = font_filename)

plt.title("使用自定義的中文字型", fontproperties=myfont, size=24)

plt.show()

'''
#完完全全改過來
#用 matplotlib 的參數設定, rcParams, 把字型完完全全用某個中文字型

#plt.rcParams['font.sans-serif'] = ['SimHei'] # 選個普通的黑體字
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
plt.rcParams['axes.unicode_minus']=False # 負號不出問題
plt.title("使用自定義的中文字型", size=15) # 不用再設字型!


#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

'''


