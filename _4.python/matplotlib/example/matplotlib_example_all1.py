from __future__ import division

"""
matplotlib 範例 大全




"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print('------------------------------------------------------------')	#60個

import sqlite3

db_filename = 'C:/_git/vcs/_1.data/______test_files1/_db/gasoline.sqlite'

print("油價走勢圖")

print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename) # 建立資料庫連線
cursor = conn.execute('SELECT * FROM prices ORDER BY gdate;')

data = []
cnt = 0
for row in cursor:
    data.append(list(row))
    cnt = cnt + 1
    """
    if cnt == 20:
        break
    """
x = np.arange(0,len(data))
dataset = [list(), list(), list()]
for i in range(0, len(data)):
    for j in range(0,3):
        dataset[j].append(data[i][j + 1])

w = np.array(dataset[0])    #92
y = np.array(dataset[1])    #95
z = np.array(dataset[2])    #98

plt.ylabel("NTD$")
plt.xlabel("Weeks ( {} --- {} )".format(data[0][0], data[len(data) - 1][0]))
plt.plot(x, w, color = "blue", label = "92")
plt.plot(x, y, color = "red", label = "95")
plt.plot(x, z, color = "green", label = "98")
plt.xlim(0,len(data))
plt.ylim(10,40)
plt.title('台灣油價走勢圖')
plt.legend()

plt.show()

print('------------------------------------------------------------')	#60個

import xlrd

book = xlrd.open_workbook('data/election_2018.xls')
sheet = book.sheet_by_index(0)

for row in range(10):
    print(sheet.row_values(row))

rows = sheet.nrows
table = list()
for row in range(rows):
    table.append(sheet.row_values(row))
for row in range(rows):
    if table[row][0] == '':
        table[row][0] = table[row-1][0]

tainan = dict()
for row in range(rows):
    if table[row][0] == '臺南市':
        tainan[table[row][1]] = table[row][6]

print(type(tainan))
print(tainan)

print('------------------------------------------------------------')	#60個

import xlrd

#pd.read_excel kilo可用  sugar不可用, sugar降版成 pandas 1.3.5 可用
data = pd.read_excel('data/election_2018.xls')

data.info()
data.head(10)

print('------------------------------------------------------------')	#60個

#pd.read_excel kilo可用  sugar不可用, sugar降版成 pandas 1.3.5 可用

data = pd.read_excel('data/election_2018.xls')
target = data.fillna(method='ffill')
target = target[['地區','姓名','出生年次','推薦政黨','得票數']]
target['年齡'] = 2018-target['出生年次']
target = target.drop('出生年次', axis=1)
target = target.set_index('地區')
target.describe()

target.hist(bins=3)

target

#pd.read_excel kilo可用  sugar不可用, sugar降版成 pandas 1.3.5 可用

data = pd.read_excel('data/election_2018.xls')
target = data.fillna(method='ffill')
target = target[['地區','姓名','出生年次','推薦政黨','得票數']]
target['年齡'] = 2018-target['出生年次']
target = target.drop('出生年次', axis=1)
target = target.set_index(['地區', '推薦政黨'])
target

#pd.read_excel kilo可用  sugar不可用, sugar降版成 pandas 1.3.5 可用

data = pd.read_excel('data/election_2018.xls')
target = data.fillna(method='ffill')
target = target[['地區','姓名','出生年次','推薦政黨','得票數']]
target['年齡'] = 2018-target['出生年次']
target = target.drop('出生年次', axis=1)
target = target.set_index(['推薦政黨', '地區']).sort_index()
target

#pd.read_excel kilo可用  sugar不可用, sugar降版成 pandas 1.3.5 可用

data = pd.read_excel('data/election_2018.xls')
target = data.fillna(method='ffill')
target = target[['地區','姓名','出生年次','推薦政黨','得票數']]
target['年齡'] = 2018-target['出生年次']
target = target.drop('出生年次', axis=1)
target = target.set_index(['推薦政黨', '地區']).sort_index()
print("國民黨：\t{:>10,d}票".format(target.loc['中國國民黨']['得票數'].sum()))
print("民進黨：\t{:>10,d}票".format(target.loc['民主進步黨']['得票數'].sum()))
print("其它：\t{:>10,d}票".format(target.loc['無黨籍及未經政黨推薦']['得票數'].sum()))

import seaborn as sns

#如果明明有的字型, matplotlib 說找不到的話, 有可能需要讓 matplotlib 清掉原本的 cache。
#matplotlib.font_manager._rebuild()
#from matplotlib.font_manager import _rebuild

#pd.read_excel kilo可用  sugar不可用, sugar降版成 pandas 1.3.5 可用

data = pd.read_excel('data/election_2018.xls')
target = data.fillna(method='ffill')
target = target[['地區','姓名','推薦政黨','得票數']].groupby(by = '推薦政黨')['得票數'].sum()
target.plot.pie(y='推薦政黨')
target

plt.show()

import seaborn as sns

#如果明明有的字型, matplotlib 說找不到的話, 有可能需要讓 matplotlib 清掉原本的 cache。
#matplotlib.font_manager._rebuild()
#from matplotlib.font_manager import _rebuild
#_rebuild()

#pd.read_excel kilo可用  sugar不可用, sugar降版成 pandas 1.3.5 可用

data = pd.read_excel('data/election_2018.xls')
target = data.fillna(method='ffill')
target = target[['地區','姓名','出生年次','推薦政黨','得票數']]
target['年齡'] = 2018-target['出生年次']
target = target.drop('出生年次', axis=1)
target = target.set_index(['地區'])
tainan = target.loc['臺南市'][['姓名','得票數']]
tainan = tainan.set_index(['姓名'])
tainan.plot.pie(y='得票數')
tainan.plot.bar()

plt.show()

print("------------------------------------------------------------")  # 60個

data = pd.read_csv('data/hualien.csv')
target = data[['年度','總人口數','平地原住民','山地原住民']]
target = target.set_index(target['年度'])
target = target.drop(['年度'], axis=1)
print(target)

print('------------------------------------------------------------')	#60個

data = pd.read_csv('data/hualien.csv')
target = pd.DataFrame(data[['年度','總人口數','平地原住民','山地原住民']])
target = target.set_index(target['年度'])
target = target.drop(['年度'], axis=1)
print(target)

print('------------------------------------------------------------')	#60個

data = pd.read_csv('data/hualien.csv')
target = pd.DataFrame(data[['年度','總人口數','平地原住民','山地原住民']])
target = target.set_index(target['年度'])
fig1 = target.drop(['年度'], axis=1)
fig2 = target.drop(['年度', '總人口數'], axis=1)
fig1.plot(ylim=(0,400000))
fig2.plot.bar(ylim=(0,80000))

plt.show()

print("------------------------------------------------------------")  # 60個

#折線圖
def lineChart(s,x):
    plt.xlabel('城市名稱')
    plt.ylabel('民調原分比')
    plt.title('各種城市喜好度比較')
    plt.plot(x, s, marker='.')

#長條圖
def barChart(s,x):
    plt.xlabel('城市名稱')
    plt.ylabel('民調原分比')
    plt.title('各種城市喜好度比較')
    plt.bar(x, s)

#橫條圖
def barhChart(s,x):
    plt.barh(x, s)

#圓餅圖
def pieChart(s,x):	 
    plt.pie(s,labels=x, autopct='%.2f%%')

#要繪圖的數據
x = ['第一季', '第二季', '第三季', '第四季']
s = [13.2, 20.1, 11.9, 14.2]

#定義子圖
plt.figure(1, figsize=(8, 6),clear=True)
plt.subplots_adjust(left=0.1, right=0.95)

plt.subplot(2,2,1)
pieChart(s,x)

x = ['程式設計概論', '多媒體概論', '計算機概論', '網路概論']
s = [3560, 4000, 4356, 1800]
plt.subplot(2,2,2)
barhChart(s,x)

x = ['新北市', '台北市', '高雄市', '台南市','桃園市','台中市']
s = [0.2, 0.3, 0.15, 0.23,0.19, 0.27]
plt.subplot(223)
lineChart(s,x)

plt.subplot(224)
barChart(s,x)

plt.show()

print('------------------------------------------------------------')	#60個

#橫條圖
def diagram_1(s,x):
	plt.barh(x, s)

#圓餅圖
def diagram_2(s,x):	 
	plt.pie(s,labels=x, autopct='%.2f%%')
#折線圖+長條圖

def diagram_4(s,x):
    plt.plot(x, s, marker='.')
    plt.bar(x, s, alpha=0.5)	

#長條圖
def diagram_3(s,x):
	plt.bar(x, s)	

#要繪圖的數據
x = ['高雄','台中','宜蘭','花蓮']
s = [89,58,63,50]

#設定子圖
plt.figure(1, figsize=(8, 8),clear=True)
plt.subplots_adjust(left=0.1, right=0.95)

plt.subplot(221)
diagram_1(s,x)

plt.subplot(222)
diagram_2(s,x)

plt.subplot(223)
diagram_3(s,x)

plt.subplot(2,2,4)
diagram_4(s,x)

plt.show()

print('------------------------------------------------------------')	#60個

# 設定圖書分類及銷售額比例
listx = ["商業理財", "文學小說", "藝術設計", "人文科普", "語言電腦", "心靈養生", "生活風格", "親子共享"]
listm = [0.14, 0.16, 0.08, 0.13, 0.16, 0.12, 0.16, 0.05]  # 男性比例
listf = [0.1, 0.19, 0.06, 0.1, 0.13, 0.13, 0.2, 0.09]  # 女性比例

# 將比例乘以100
listm = [x * 100 for x in listm]
listf = [x * 100 for x in listf]

# 設定圖表區尺寸以及使用字型
plt.figure(figsize=(12, 9))

# 男性圖書分類銷售率圖餅圖
plt.subplot(221)
plt.title("圖書分類銷售比率-男性", fontsize=16)
plt.pie(listm, labels=listx, autopct="%2.1f%%")

# 女性圖書分類銷售率圖餅圖
plt.subplot(222)
plt.title("圖書分類銷售比率-女性", fontsize=16)
plt.pie(listf, labels=listx, autopct="%2.1f%%")

# 圖書分類男女銷售率長條圖
plt.subplot(223)
width = 0.4
listx1 = [x - width / 2 for x in range(len(listx))]
listx2 = [x + width / 2 for x in range(len(listx))]

plt.title("圖書分類銷售長條圖-性別", fontsize=16)
plt.xlabel("圖書分類", fontsize=12)
plt.ylabel("銷售比率(%)", fontsize=12)

plt.bar(listx1, listm, width, label="男")
plt.bar(listx2, listf, width, label="女")
plt.xticks(range(len(listx)), labels=listx, rotation=45)
plt.legend()

# 圖書分類男女銷售率折線圖
plt.subplot(224)
plt.title("圖書分類銷售折線圖-性別", fontsize=16)
plt.xlabel("圖書分類", fontsize=12)
plt.ylabel("銷售比率(%)", fontsize=12)

plt.plot(listx, listm, marker="s", label="男")
plt.plot(listx, listf, marker="s", label="女")
plt.gca().grid(True)
plt.xticks(rotation=45)
plt.legend()

plt.show()

print('------------------------------------------------------------')	#60個

print("helmoltz coils")

#Contour plot

from matplotlib.cm import viridis as colormap  # future default colormap

"""
Setup
"""
r = 1.0
res = 200  # grid resolution. 100 may be enough, resulting in smaller SVG file)

def dist3(a, b, c, d, e, f):
    """Compute the Euclidian distance from (d, e, f) to (a, b, c),
    raised to the 3rd power (and with lower boundary `r`).
    """
    return np.maximum(r, np.sqrt((a - d)**2 + (b - e)**2 + (c - f)**2))

x = np.linspace(-150, 150, res)
y = np.linspace(-150, 150, res)
X, Y = np.meshgrid(x, y)
F = np.zeros((res, res, 3))

"""
Computing part
"""
# Loop over two coils
for coils in [1.0, -1.0]:
    # Sum field contributions from coil in 10-degree steps
    for p in np.arange(0, 360, 10):
        xc = 100 * np.sin(np.pi * p / 180.0)
        yc = 50 * coils
        zc = 100 * np.cos(np.pi * p / 180.0)
        MAG = 1.0 / ((r + dist3(X, Y, 0.0, xc, yc, zc))**3)
        # (We leave out the necessary constants that would be required
        # to get proper units because only scaling behavior will be shown
        # in the plot. This is also why a sum instead of an integral
        # can be used.)
        #
        # Due to more stringent casting rules in recent Numpy (>=1.10),
        # one builds an explicit list of all the vectors (X - xc, Y - yc, -zc)
        # instead of relying on broadcasting. One then reshapes the array Z
        # (of the cross-product results) as previously expected.
        vectors = np.array([[xval - xc, yval - yc, -zc] for (xval, yval)
                            in zip(X.reshape(-1), Y.reshape(-1))])
        Z = np.cross(vectors, (-zc, 0.0, xc))
        Z = Z.reshape(res, res, 3)
        F += Z * MAG[:,:,np.newaxis]

# Compute the B-field
B = np.sqrt(F[..., 0]**2 + F[..., 1]**2 + F[..., 2]**2)
# Scale field strength by value at center
B = B / B[res // 2, res // 2]

"""
Plotting part
"""
fig_label = "helmoltz_coils"
plt.close(fig_label)
fig, ax = plt.subplots(figsize=(6, 6), num=fig_label, frameon=False)

levels = (0.5, 0.8, 0.9, 0.95, 0.99, 1.01, 1.05, 1.1)
cs = ax.contour(x, y, B, cmap=colormap, levels=levels)

# Add wire symbols
ax.scatter((100, 100, -100, -100), (50, -50, 50, -50), s=400, color="Black")

ax.axis((-130, 130, -130, 130))
ax.set_xticks([])
ax.set_yticks([])

plt.tight_layout()

plt.show()

print("------------------------------------------------------------")  # 60個

##########
## Code for the mpl logo figure
##########

from matplotlib.cm import jet as colormap
from matplotlib.ticker import NullFormatter, MultipleLocator

t, w, r = zip((0.1, 0.4, 1), (0.9, 0.3, 5), (1.7, 0.5, 7), (2.7, 0.6, 6),
              (3.5, 0.3, 3), (4.5, 0.4, 4), (5.3, 0.3, 7))

fig, ax = plt.subplots(subplot_kw={'polar': True})
bars = ax.bar(t, r, width=w, bottom=0.0, lw=2, edgecolor='Black', zorder=2)

for r, bar in zip(r, bars):
    bar.set_facecolor(colormap(r / 9.0))
    bar.set_alpha(0.7)

ax.yaxis.set_major_locator(MultipleLocator(2))

for axis in (ax.xaxis, ax.yaxis):
    axis.set_major_formatter(NullFormatter())  # no tick labels

ax.set_ylim([0, 8])
ax.grid(True)

plt.show()

print("------------------------------------------------------------")  # 60個

#Dolphins

import matplotlib.cm as cm
from matplotlib.patches import Circle, PathPatch
from matplotlib.path import Path
from matplotlib.transforms import Affine2D

r = np.random.rand(50)
t = np.random.rand(50) * np.pi * 2.0
x = r * np.cos(t)
y = r * np.sin(t)

fig, ax = plt.subplots(figsize=(6, 6))
circle = Circle((0, 0), 1, facecolor='none',
                edgecolor=(0, 0.8, 0.8), linewidth=3, alpha=0.5)
ax.add_patch(circle)

im = plt.imshow(np.random.random((100, 100)),
                origin='lower', cmap=cm.winter,
                interpolation='spline36',
                extent=([-1, 1, -1, 1]))
im.set_clip_path(circle)

plt.plot(x, y, 'o', color=(0.9, 0.9, 1.0), alpha=0.8)

# Dolphin from OpenClipart library by Andy Fitzsimon
#   <cc:License rdf:about="http://web.resource.org/cc/PublicDomain">
#     <cc:permits rdf:resource="http://web.resource.org/cc/Reproduction"/>
#     <cc:permits rdf:resource="http://web.resource.org/cc/Distribution"/>
#     <cc:permits rdf:resource="http://web.resource.org/cc/DerivativeWorks"/>
#   </cc:License>

dolphin = """
M -0.59739425,160.18173 C -0.62740401,160.18885 -0.57867129,160.11183
-0.57867129,160.11183 C -0.57867129,160.11183 -0.5438361,159.89315
-0.39514638,159.81496 C -0.24645668,159.73678 -0.18316813,159.71981
-0.18316813,159.71981 C -0.18316813,159.71981 -0.10322971,159.58124
-0.057804323,159.58725 C -0.029723983,159.58913 -0.061841603,159.60356
-0.071265813,159.62815 C -0.080250183,159.65325 -0.082918513,159.70554
-0.061841203,159.71248 C -0.040763903,159.7194 -0.0066711426,159.71091
0.077336307,159.73612 C 0.16879567,159.76377 0.28380306,159.86448
0.31516668,159.91533 C 0.3465303,159.96618 0.5011127,160.1771
0.5011127,160.1771 C 0.63668998,160.19238 0.67763022,160.31259
0.66556395,160.32668 C 0.65339985,160.34212 0.66350443,160.33642
0.64907098,160.33088 C 0.63463742,160.32533 0.61309688,160.297
0.5789627,160.29339 C 0.54348657,160.28968 0.52329693,160.27674
0.50728856,160.27737 C 0.49060916,160.27795 0.48965803,160.31565
0.46114204,160.33673 C 0.43329696,160.35786 0.4570711,160.39871
0.43309565,160.40685 C 0.4105108,160.41442 0.39416631,160.33027
0.3954995,160.2935 C 0.39683269,160.25672 0.43807996,160.21522
0.44567915,160.19734 C 0.45327833,160.17946 0.27946869,159.9424
-0.061852613,159.99845 C -0.083965233,160.0427 -0.26176109,160.06683
-0.26176109,160.06683 C -0.30127962,160.07028 -0.21167141,160.09731
-0.24649368,160.1011 C -0.32642366,160.11569 -0.34521187,160.06895
-0.40622293,160.0819 C -0.467234,160.09485 -0.56738444,160.17461
-0.59739425,160.18173
"""

vertices = []
codes = []
parts = dolphin.split()
i = 0
code_map = {
    'M': Path.MOVETO,
    'C': Path.CURVE4,
    'L': Path.LINETO,
}

while i < len(parts):
    path_code = code_map[parts[i]]
    npoints = Path.NUM_VERTICES_FOR_CODE[path_code]
    codes.extend([path_code] * npoints)
    vertices.extend([[*map(float, y.split(','))]
                     for y in parts[i + 1:][:npoints]])
    i += npoints + 1
vertices = np.array(vertices)
vertices[:, 1] -= 160

dolphin_path = Path(vertices, codes)
dolphin_patch = PathPatch(dolphin_path, facecolor=(0.6, 0.6, 0.6),
                          edgecolor=(0.0, 0.0, 0.0))
ax.add_patch(dolphin_patch)

vertices = Affine2D().rotate_deg(60).transform(vertices)
dolphin_path2 = Path(vertices, codes)
dolphin_patch2 = PathPatch(dolphin_path2, facecolor=(0.5, 0.5, 0.5),
                           edgecolor=(0.0, 0.0, 0.0))
ax.add_patch(dolphin_patch2)

plt.show()

print("------------------------------------------------------------")  # 60個

from pylab import *

rc("xtick.major", pad=8)

data = """
   Sovereign of the Seas   90     1637   1,522                                             2,500             Sail Three-Decker                  Lavery        
   Naseby                  80     1655   1,258                                             2,100             Sail Three-Decker                  Lavery        
   Prince                 100     1670   1,403                                             2,300             Sail Three-Decker                  Lavery        
   Royal James            100     1671   1,416                                             2,300             Sail Three-Decker                  Lavery        
   Royal Charles          100     1673   1,443                                             2,400             Sail Three-Decker                  Lavery        
   Royal James            100     1675   1,422                                             2,400             Sail Three-Decker                  Lavery        
   Royal Prince            92     1663   1,432                                             2,400             Sail Three-Decker                  Lavery        
   Britannia              100     1682   1,739                                             2,900             Sail Three-Decker                  Lavery        
   Royal Sovereign        100     1701   1,883                                             3,100             Sail Three-Decker                  Lavery        
   Royal Anne             100     1703   1,722                                             2,900             Sail Three-Decker                  Lavery        
   London                 100     1706   1,685                                             2,800             Sail Three-Decker                  Lavery        
   Royal George           100     1715   1,801                                             3,000             Sail Three-Decker                  Lavery        
   Britannia              100     1719   1,895                                             3,100             Sail Three-Decker                  Lavery        
   Royal William          100     1719   1,918                                             3,200             Sail Three-Decker                  Lavery        
   Royal Sovereign        100     1728   1,883                                             3,100             Sail Three-Decker                  Lavery        
   Victory                100     1737   1,921                                             3,200             Sail Three-Decker                  Lavery        
   Royal George           100     1756   2,047                                             3,400             Sail Three-Decker                  Lavery        
   Britannia              100     1762   2,116                                             3,500             Sail Three-Decker                  Lavery        
   Victory                100     1765   2,142                                             3,600             Sail Three-Decker                  Lavery        
   Royal Sovereign        100     1786   2,175                                             3,600             Sail Three-Decker                  Lavery        
   Royal George           100     1788   2,286                                             3,800             Sail Three-Decker                  Lavery        
   Caledonia              120     1808   2,616                                             4,300             Sail Three-Decker                  Lavery        
   Ville de Paris         110     1795   2,351                                             3,900             Sail Three-Decker                  Lavery        
   Hibernia               110     1804   2,530                                             4,200             Sail Three-Decker                  Lavery        
   Queen Charlotte        100     1790   2,286                                             3,800             Sail Three-Decker                  Lavery        
   Nelson                 120     1814   2,617                                             4,300             Sail Three-Decker                  Lavery        
   St Vincent             120     1815   2,601                                             4,300             Sail Three-Decker                  Lavery        
   Howe                   120     1815   2,619                                             4,300             Sail Three-Decker                  Lavery        
   Britannia              120     1820   2,616                                             4,300             Sail Three-Decker                  Lavery        
   Prince Regent          120     1823   2,613                                             4,300             Sail Three-Decker                  Lavery        
   Queen Charlotte        104     1810   2,289                                             3,800             Sail Three-Decker                  Lavery        
   Princess Charlotte     104     1825   2,443                                             4,100             Sail Three-Decker                  Lavery        
   Royal Adelaide         104     1828   2,446                                             4,100             Sail Three-Decker                  Lavery        
   Royal George           120     1827   2,616                                             4,300             Sail Three-Decker                  Lavery        
   Neptune                120     1832   2,694                                             4,500             Sail Three-Decker                  Lavery        
   Royal William          120     1833   2,694                                             4,500             Sail Three-Decker                  Lavery        
   Waterloo               120     1833   2,694                                             4,500             Sail Three-Decker                  Lavery        
   St George              120     1840   2,694                                             4,500             Sail Three-Decker                  Lavery        
   Trafalgar              120     1841   2,694                                             4,500             Sail Three-Decker                  Lavery        
   Queen                  110     1839   3,104                                             5,100             Sail Three-Decker                  Lavery        
   Duke of Wellington     131     1852   3,759                                5,829        5,829 Steam Three-Decker (conversion from sail)      Lambert       
   Marlborough            131     1855   3,853                                6,065        6,065 Steam Three-Decker (conversion from sail)      Lambert       
   Royal Sovereign        131     1857   3,853                                6,065        6,065 Steam Three-Decker (conversion from sail)      Lambert       
   Prince of Wales        131     1860   3,853                                6,065        6,065 Steam Three-Decker (conversion from sail)      Lambert       
   Royal Albert           121     1854   3,726                                5,572        5,572 Steam Three-Decker (conversion from sail)      Lambert       
   Windsor Castle         102     1858   3,099                                             5,100 Steam Three-Decker (conversion from sail)      Lambert       
   Victoria               121     1859   4,116                                6,959        6,959             Steam Three-Decker                 Lambert       
   Howe                   121     1860   4,236                                             7,000             Steam Three-Decker                 Lambert       
   Saint Jean d'Acre      101     1853   3,200                                5,499        5,499              Steam Two-Decker                  Lambert       
   Conqueror              101     1855   3,224                                5,720        5,720              Steam Two-Decker                  Lambert       
   Donegal                101     1858   3,224                                5,720        5,720              Steam Two-Decker                  Lambert       
   Duncan                 101     1859   3,715                                5,950        5,950              Steam Two-Decker                  Lambert       
   Gibraltar              101     1860   3,715                                5,950        5,950              Steam Two-Decker                  Lambert       
   Warrior                 40     1860   6,039                                9,180        9,180             Iron-Clad Frigate              Lyon & Winfield   
   Black Prince            40     1861   6,039                                9,180        9,180             Iron-Clad Frigate              Lyon & Winfield   
   Achilles                26     1863   6,121                                9,820        9,820             Iron-Clad Frigate              Lyon & Winfield   
   Minotaur                36     1863   6,643                               10,690       10,690             Iron-Clad Frigate              Lyon & Winfield   
   Agincourt               36     1865   6,638                               10,600       10,600             Iron-Clad Frigate              Lyon & Winfield   
   Northumberland          36     1866   6,631                               10,784       10,784             Iron-Clad Frigate              Lyon & Winfield   
   Lord Clyde              24     1864   4,067                                7,750        7,750    Centre-Battery Iron-Clad Frigate       Lyon & Winfield   
   Lord Warden             16     1865   4,080                                7,842        7,842    Centre-Battery Iron-Clad Frigate       Lyon & Winfield   
   Bellerophon             15     1865   4,720                                7,551        7,551          Centre-Battery Iron-Clad          Lyon & Winfield   
   Hercules                14     1868   5,234                                8,830        8,830          Centre-Battery Iron-Clad          Lyon & Winfield   
   Monarch                  7     1868   5,102                                8,322        8,322             Masted Turret Ship             Lyon & Winfield   
   Captain                  6     1869   4,272                                7,767        7,767             Masted Turret Ship             Lyon & Winfield   
   Sultan                  12     1870   5,234                                9,540        9,540          Centre-Battery Iron-Clad          Lyon & Winfield   
   Devastation              4     1871   4,407                                9,390        9,390            Mastless Turret Ship            Lyon & Winfield   
   Thunderer                4     1872                                        9,390        9,390            Mastless Turret Ship            Lyon & Winfield   
   Alexandra               12     1875                                        9,490        9,490          Centre-Battery Iron-Clad          Lyon & Winfield   
   Dreadnought              4     1875                                       10,820       10,820            Mastless Turret Ship            Lyon & Winfield   
   Temeraire                8     1876                                        8,571        8,571          Centre-Battery Iron-Clad          Lyon & Winfield   
   Inflexible               4     1876                                       11,880       11,880        Central Citadel Turret Ship         Lyon & Winfield   
"""

s2x, s2y, s3x, s3y, t3x, t3y, ix, iy, lx, ly = [], [], [], [], [], [], [], [], [], []

for l in data.splitlines():
    if len(l) < 5:
        continue
    n = l[:26].strip()
    y = int(l[33:39])
    try:
        t = int(l[39:47].replace(",", ""))
    except:
        continue
    if "Steam Two-Decker" in l:
        s2x.append(y)
        s2y.append(t)
    elif "Steam Three-Decker" in l:
        s3x.append(y)
        s3y.append(t)
    elif "Sail Three-Decker" in l:
        t3x.append(y)
        t3y.append(t)
    elif "igate" in l:
        ix.append(y)
        iy.append(t)
    else:
        lx.append(y)
        ly.append(t)

ll = 0.7
scatter(t3x, t3y, c="b", marker="o", lw=ll, label="Sail 3-Deckers")
scatter(s3x, s3y, c="orange", marker="o", lw=ll, label="Steam 3-Deckers")
scatter(s2x, s2y, c="r", marker="o", lw=ll, label="Steam 2-Deckers")
scatter(ix, iy, c="g", marker="o", lw=ll, label="Iron-clad Frigates")
scatter(lx, ly, c="cyan", marker="o", lw=ll, label="Later Iron-clads")

legend(loc="upper left")
xticks(range(1630, 1930, 50))
xlabel("Year launched")
ylabel("Tonnage (BOM)")
grid(True, ls="-", c="#a0a0a0")


plt.show()

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個




