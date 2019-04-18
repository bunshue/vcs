#Á³±Û¹Ï
#!/usr/bin/env python

from pylab import *

rc('grid', color='#aaaaaa', linewidth = 1, linestyle = '-')

figure(figsize = (6, 6))
ax = axes([0.1, 0.1, 0.8, 0.8], polar = True)

t = arange(-4 * pi, 4 * pi, .1)
polar(t, 1.19**t, linewidth = 2)

xt, yt = xticks()[0], yticks()[0]
xticks(xt, ['' for q in range(len(xt))])
yticks(yt, ['' for q in range(len(yt))])

savefig('logarithmic_spiral.svg')

show()
