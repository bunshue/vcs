# scatter 集合

selected_font = 'C:/______test_files2/msch.ttf'

import matplotlib.pyplot as plt
from numpy.random import rand
import numpy as np

#plt.figure(figsize=(8,8))	#設定圖片視窗大小
plt.figure(num = 'scatter 集合', figsize=[20, 15], dpi=84, facecolor="whitesmoke", edgecolor="r", linewidth=1, frameon=True)
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

#第一張圖
plt.subplot(231)

#散點圖
a = rand(100)
b = rand(100)
plt.scatter(a,b)


#第二張圖
plt.subplot(232)

#Hyperlinks
import numpy as np
import matplotlib.pyplot as plt

s = plt.scatter([1, 2, 3], [4, 5, 6])
s.set_urls(['https://www.bbc.com/news', 'https://www.google.com/', None])
'''
filename = 'C:/______test_files3/scatter.svg'
fig.savefig(filename)
print('已存圖' + filename)
'''

#第三張圖
plt.subplot(233)

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
        t = int(l[39:47].replace(',', ''))
    except: 
        continue
    if 'Steam Two-Decker' in l:
        s2x.append(y)
        s2y.append(t)
    elif 'Steam Three-Decker' in l:
        s3x.append(y)
        s3y.append(t)
    elif 'Sail Three-Decker' in l:
        t3x.append(y)
        t3y.append(t)
    elif 'igate' in l:
        ix.append(y)
        iy.append(t)
    else:
        lx.append(y)
        ly.append(t)

ll = .7
scatter(t3x, t3y, c='b', marker='o', lw=ll, label='Sail 3-Deckers')
scatter(s3x, s3y, c='orange', marker='o', lw=ll, label='Steam 3-Deckers')
scatter(s2x, s2y, c='r', marker='o', lw=ll, label='Steam 2-Deckers')
scatter(ix, iy, c='g', marker='o', lw=ll, label='Iron-clad Frigates')
scatter(lx, ly, c='cyan', marker='o', lw=ll, label='Later Iron-clads')

legend(loc="upper left")
ylim(0, 7000)
xlim(1630, 1875)
xticks(range(1630, 1930, 50))
xlabel("Year launched")
ylabel("Tonnage (BOM)")
grid(True, ls='-', c='#a0a0a0')

#存圖命令
savefig("Weight Growth of RN First Rate Line-of-Battle Ships 1630-1875.svg")



#第四張圖
plt.subplot(234)

speed = [4, 4, 7, 7, 8, 9, 10, 10, 10, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14, 15, 15, 15, 16, 16, 17, 17, 17, 18, 18, 18, 18, 19, 19, 19, 20, 20, 20, 20, 20, 22, 23, 24, 24, 24, 24, 25]
dist = [2, 10, 4, 22, 16, 10, 18, 26, 34, 17, 28, 14, 20, 24, 28, 26, 34, 34, 46, 26, 36, 60, 80, 20, 26, 54, 32, 40, 32, 40, 50, 42, 56, 76, 84, 36, 46, 68, 32, 48, 52, 56, 64, 66, 54, 70, 92, 93, 120, 85]

plt.scatter(speed, dist)

#第五張圖
plt.subplot(235)



#第六張圖
plt.subplot(236)



plt.show()


