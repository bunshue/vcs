#螺旋圖

import pylab

pylab.rc('grid', color='#aaaaaa', linewidth = 1, linestyle = '-')

pylab.figure(figsize = (6, 6))	#圖像大小[英吋]
ax = pylab.axes([0.1, 0.1, 0.8, 0.8], polar = True)

t = pylab.arange(-4 * pylab.pi, 4 * pylab.pi, .1)
pylab.polar(t, 1.19**t, linewidth = 2)

xt, yt = pylab.xticks()[0], pylab.yticks()[0]
pylab.xticks(xt, ['' for q in range(len(xt))])
pylab.yticks(yt, ['' for q in range(len(yt))])

#存圖命令
#pylab.savefig('logarithmic_spiral.svg')

pylab.show()
