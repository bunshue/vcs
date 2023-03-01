import math
import matplotlib.pyplot as plt
import numpy as np
import matplotlib 
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
myfont = matplotlib.font_manager.FontProperties(fname=r'C:/Windows/Fonts/msyh.ttf')
plt.xlabel(u'橫座標', fontproperties=myfont)
plt.ylabel(u'縱座標', fontproperties=myfont)



plt.savefig('sin_plot.svg')
plt.savefig('sin_plot111.png')
#plt.savefig('sin_plot.bmp')
#plt.savefig('sin_plot.jpg')
plt.savefig('sin_plot222.png', format='png', transparent=True, dpi=300, pad_inches = 0)    #指定分辨率
plt.savefig('sin_plot333.png', dpi = 300)

plt.show()



