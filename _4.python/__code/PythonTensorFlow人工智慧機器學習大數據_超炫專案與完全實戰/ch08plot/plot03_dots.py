#!/usr/bin/env
# -*- coding: utf-8 -*-    
__author__ = "Powen Ko, www.powenko.com"

import matplotlib.pyplot as plt
t=[1,2,3,4]
plt.plot(t, t, 'r--')
plt.plot( t, [2,4,6,8], 'bs')
plt.plot( t, [3,6,9,12], 'g^')
plt.plot( t, [4,8,12,16], 'k:')
plt.show()