import os
import sys
import time
import random

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

from color_module import Color
c = Color(15, 35, 3)

print(c)
#Color: R=15, G=35, B=3



#18.3.2 Basic use of the mathproj package

import mathproj
#Hello from mathproj init

print(mathproj.version)
#1.03


#18.3.3 Loading subpackages and submodules

import mathproj


import mathproj.comp.numeric.n1

mathproj.comp.numeric.n1.g()

#version is 1.03
#Called function h in module n2


print(mathproj.comp)
print(mathproj.comp.numeric)


from mathproj import version
from mathproj.comp import c1
from mathproj.comp.numeric.n2 import h
def g():
    print("version is", version)
    print(h())


from mathproj import version
from mathproj.comp import c1
from mathproj.comp.numeric.n2 import h

#18.4 The __all__ attribute

from mathproj import *

#Hello from mathproj.comp init

print(comp)
#<module 'mathproj.comp' from 'mathproj/comp/__init__.py'>

print(c1)

from mathproj.comp import c1
print(c1)


print('------------------------------------------------------------')	#60個



