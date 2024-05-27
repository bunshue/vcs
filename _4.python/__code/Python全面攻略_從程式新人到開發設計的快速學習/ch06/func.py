# -*- coding: utf-8 -*-
from math import sqrt

def func1(x):
    r = sqrt(x) * 10
    return(int(r + 0.5))

def func2(x):
    r = x / 2 + 50
    return(round(r))