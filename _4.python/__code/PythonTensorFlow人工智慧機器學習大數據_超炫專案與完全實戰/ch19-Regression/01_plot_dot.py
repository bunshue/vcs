#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "柯博文老師 Powen Ko, www.powenko.com"
import matplotlib.pyplot as plt


plt.plot([9,9.2,9.6,7.5,6.7,7], [9.4,9.2,9.2,9.2,7.1,7.4 ], 'yx' )
plt.plot([7.2,7.3,7.2,7.3,7.2,7.3,7.3 ], [10.3,10.5,9.2,10.2,9.7,10.1,10.1 ], 'gx' )
plt.plot([6.5,9.0], [7.8,12.5], 'b--' )

plt.ylabel('H cm')
plt.xlabel('W cm')

plt.legend(('Orange','Lemons'),
           loc='upper right')
plt.show()