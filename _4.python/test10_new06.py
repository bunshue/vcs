import os
import sys
import time
import random

print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

import shelve
book = shelve.open("addresses")

book['167'] = ('邱大熊', '0912-345678', '台北市忠孝路1號')
book['928'] = ('陳小天', '0987-654321', '新竹市中山路2號')
book.close()


import shelve
book = shelve.open("addresses")

print(book['167'] )
book.close()

print('------------------------------------------------------------')	#60個

import pathlib
path = pathlib.Path('test10_new06.py')
abs_path = path.resolve()
print(abs_path)
new_path = str(abs_path) + ".old"
print(new_path)


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



