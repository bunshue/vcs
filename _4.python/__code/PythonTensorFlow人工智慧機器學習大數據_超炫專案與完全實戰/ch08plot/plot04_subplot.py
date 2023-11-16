#!/usr/bin/env
# -*- coding: utf-8 -*-    
__author__ = "Powen Ko, www.powenko.com"

import matplotlib.pyplot as plt
t1=[1,2,3,4]
t2=[2,4,6,8]
plt.subplot(2,1,1,facecolor='y')
#plt.subplot(211,facecolor='y')
plt.plot(t1, t2, 'ro')
plt.subplot(2,2,3,facecolor='k')
#plt.subplot(223,facecolor='k')
plt.plot(t2, t2, 'g--')
plt.subplot(2,2,4)
#plt.subplot(224)
plt.plot(t2, t2, 'b|')
plt.show()