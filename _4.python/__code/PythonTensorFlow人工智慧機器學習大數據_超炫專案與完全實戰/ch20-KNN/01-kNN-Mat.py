#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "柯博文老師 Powen Ko, www.powenko.com"
import matplotlib.pyplot as plt
import numpy as np

plt.plot([9,9.2,9.6,9.2,6.7,7,7.6], [9.0,9.2,9.2,9.2,7.1,7.4,7.5 ], 'yx' )
plt.plot([7.2,7.3,7.2,7.3,7.2,7.3,7.3 ], [10.3,10.5,9.2,10.2,9.7,10.1,10.1 ], 'g.' )
plt.plot([7], [9], 'r^' )

circle1=plt.Circle((7,9),1.2,color='#aaaaaa')
plt.gcf().gca().add_artist(circle1)
plt.axis([6, 11, 6, 11])



plt.ylabel('H cm')
plt.xlabel('W cm')
plt.legend(('Orange','Lemons'),
           loc='upper right')
plt.show()