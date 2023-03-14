import math
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

selected_font = 'C:/_git/vcs/_4.cmpp/_python_test/data/msch.ttf'

#a = np.linspace(0,1,100)
a = np.linspace(-360,360,100)
#b = np.exp(-a)
b = np.sin(2*math.pi*a/360)
c = np.cos(2*math.pi*a/360)
d = np.sinc(2*math.pi*a/360)
plt.plot(a,b)
plt.plot(a,c)
plt.plot(a,d)

#plt.axis('off') #座標軸關閉
myfont = matplotlib.font_manager.FontProperties(fname=selected_font)
plt.xlabel(u'橫座標', fontproperties=myfont)
plt.ylabel(u'縱座標', fontproperties=myfont)
#plt.title('三角函數')
plt.title(u'三角函數', fontproperties=myfont)
plt.grid()

plt.show()

