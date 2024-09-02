"""
skimage : scikit-image SciKit (toolkit for SciPy)


"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
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

print("------------------------------------------------------------")  # 60個

"""
基本圖形的繪制

圖形包括線條、圓形、橢圓形、多邊形等。

在skimage包中，繪制圖形用的是draw模塊，不要和繪制圖像搞混了。

1、畫線條

函數調用格式為：

skimage.draw.line(r1,c1,r2,c2)

r1,r2: 開始點的行數和結束點的行數

c1,c2: 開始點的列數和結束點的列數

返回當前繪制圖形上所有點的坐標，如：

rr, cc =draw.line(1, 5, 8, 2)

表示從（1，5）到（8，2）連一條線，返回線上所有的像素點坐標[rr,cc]
"""

from skimage import draw,data
import matplotlib.pyplot as plt
img = data.chelsea()
print(img.shape)

rr, cc =draw.line(1, 150, 270, 400)
img[rr, cc] =255
plt.imshow(img,plt.cm.gray)
plt.show()

"""
如果想畫其它顏色的線條，則可以使用set_color（）函數，格式為：

skimage.draw.set_color(img, coords, color)

例：

draw.set_color(img,[rr,cc],[255,0,0])

則繪制紅色線條。
"""

from skimage import draw,data
import matplotlib.pyplot as plt
img=data.chelsea()
rr, cc =draw.line(1, 150, 270, 250)
draw.set_color(img,[rr,cc],[0,0,255])
plt.imshow(img,plt.cm.gray)
plt.show()

"""
2、畫圓

函數格式：skimage.draw.circle(cy, cx, radius）

cy和cx表示圓心點，radius表示半徑
"""

"""沒有circle
from skimage import draw,data
import matplotlib.pyplot as plt
img=data.chelsea()
rr, cc=draw.circle(150,150,50)
draw.set_color(img,[rr,cc],[255,0,0])
plt.imshow(img,plt.cm.gray)
plt.show()
"""

"""
3、多邊形

函數格式：skimage.draw.polygon(Y,X)

Y為多邊形頂點的行集合，X為各頂點的列值集合。
"""

from skimage import draw,data
import matplotlib.pyplot as plt
import numpy as np
img=data.chelsea()
Y=np.array([10,10,60,60])
X=np.array([200,400,400,200])
rr, cc=draw.polygon(Y,X)
draw.set_color(img,[rr,cc],[255,0,0])
plt.imshow(img,plt.cm.gray)
plt.show()

"""
我在此處只設置了四個頂點，因此是個四邊形。

4、橢圓

格式：skimage.draw.ellipse(cy, cx, yradius, xradius）

cy和cx為中心點坐標，yradius和xradius代表長短軸。
"""

from skimage import draw,data
import matplotlib.pyplot as plt
img=data.chelsea()
rr, cc=draw.ellipse(150, 150, 30, 80)
draw.set_color(img,[rr,cc],[255,0,0])
plt.imshow(img,plt.cm.gray)
plt.show()

"""
5、貝塞兒曲線
格式：skimage.draw.bezier_curve(y1,x1,y2,x2,y3,x3,weight)
y1,x1表示第一個控制點坐標
y2,x2表示第二個控制點坐標
y3,x3表示第三個控制點坐標
weight表示中間控制點的權重，用于控制曲線的彎曲度。
"""

from skimage import draw,data
import matplotlib.pyplot as plt
img=data.chelsea()
rr, cc=draw.bezier_curve(150,50,50,280,260,400,2)
draw.set_color(img,[rr,cc],[255,0,0])
plt.imshow(img,plt.cm.gray)
plt.show()

"""
6、畫空心圓
和前面的畫圓是一樣的，只是前面是實心圓，而此處畫空心圓，只有邊框線。
格式：skimage.draw.circle_perimeter(yx,yc,radius)
yx,yc是圓心坐標，radius是半徑
"""

from skimage import draw,data
import matplotlib.pyplot as plt
img=data.chelsea()
rr, cc=draw.circle_perimeter(150,150,50)
draw.set_color(img,[rr,cc],[255,0,0])
plt.imshow(img,plt.cm.gray)
plt.show()

"""
7、空心橢圓
格式：skimage.draw.ellipse_perimeter(cy, cx, yradius, xradius）
cy,cx表示圓心
yradius,xradius表示長短軸
"""

from skimage import draw,data
import matplotlib.pyplot as plt
img=data.chelsea()
rr, cc=draw.ellipse_perimeter(150, 150, 30, 80)
draw.set_color(img,[rr,cc],[255,0,0])
plt.imshow(img,plt.cm.gray)
plt.show()
 

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


