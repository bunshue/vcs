#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "柯博文老師 Powen Ko, www.powenko.com"

import numpy as np
a = np.zeros((2,2))
print(a) # Prints "[[ 0. 0.]
# [0. 0.]]"

b = np.ones((1,2)) # Create an array of all ones
print(b) # Prints "[[ 1. 1.]]"

c = np.full((2,2), 7) # Create a constant array
print(c)

d = np.eye(3)
print(d)


e = np.random.random((2,2)) # Create an array (lled with random values
print(e) # Might print "[[ 0.91940167 0.08143941]
# [ 0.68744134 0.87236687]]"