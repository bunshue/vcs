import matplotlib
import matplotlib.pyplot as plt
import numpy as np

selected_font = 'C:/_git/vcs/_4.cmpp/_python_test/data/msch.ttf'

# Data for plotting
t = np.arange(-2.0*np.pi, 2.0*np.pi, 0.01)
a = np.sin(t)
b = np.cos(t)
c = np.sinc(t)

fig, ax1 = plt.subplots()
ax1.plot(t, a)

fig, ax2 = plt.subplots()
ax2.plot(t, b)

fig, ax3 = plt.subplots()
#ax3.plot(t, c)
ax3.fill(t, c)

#plt.plot(t, a)
#plt.plot(t, b)
#plt.plot(t, c)

#plt.axis('off') #座標軸關閉

myfont = matplotlib.font_manager.FontProperties(fname=selected_font)

plt.xlabel(u'橫座標', fontproperties=myfont)
plt.ylabel(u'縱座標', fontproperties=myfont)
#plt.title('三角函數')
plt.title(u'三角函數', fontproperties=myfont)
plt.grid()

plt.show()

