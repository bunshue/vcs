import os
import sys

isympy_path = os.path.abspath(__file__)
isympy_dir = os.path.dirname(isympy_path)
sympy_top = os.path.split(isympy_dir)[0]
sympy_dir = os.path.join(sympy_top, 'sympy')

if os.path.isdir(sympy_dir):
    #sys.path.insert(0, sympy_top)
    print('is dir')

#print(__path__[0])

theano_nose = os.path.realpath(__file__)
print(theano_nose)


#print(os.listdir(cache.dirname))

print(__doc__)  # the docstring of this module above


import sympy
VERSION = sympy.__version__
print(VERSION)
