print('for-test')
for i in range(4, -1, -1):
    print(i)

for i in range(0, 6):
    print(i)



 
#產生連續的整數
for num in range(10):
    print(num)

for num in range(2, 7):
    print(num)

import sys
#import somemodule as sm	#幫模組取個別名

print (sys.argv)
#print (s.argv)





import math
math.sin(math.pi * i / 2)



import os
import sys
from distutils.util import get_platform
PLAT_SPEC = "%s-%s" % (get_platform(), sys.version[0:3])
src = os.path.join("build", "lib.%s" % PLAT_SPEC)
#sys.path.append(src)
print(src)

print(sys.argv)

foldername = 'C:/_git/vcs/_1.data/______test_files2/'

for root, dirs, files in os.walk(foldername):
    for fn in files:
        #fn = join(root, fn)
        print(fn)





