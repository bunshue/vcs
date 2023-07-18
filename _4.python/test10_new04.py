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

'''
foldername = 'C:/_git/vcs/_1.data/______test_files2/'

for root, dirs, files in os.walk(foldername):
    for fn in files:
        #fn = join(root, fn)
        print(fn)
'''

print('---------------------------------------------')

import platform, subprocess
print(platform.system())



testno = 20
s ='abc'
fmt = 'def'
result = 'hij'
err = 'mnp'
sys.stdout.write("xfmt%d  format  %s  '%s'  ->  \"%s\"\n" % (testno, s, fmt, result))
sys.stdout.write("xfmt%d  format  %s  '%s'  ->  '%s'\n" % (testno, s, fmt, result))
sys.stderr.write("%s  %s  %s\n" % (err, s, fmt))




import random
s = ''
for i in range(0, 10):
    s += random.choice('<>=^')
    s += random.choice('+- ')
    s += str(random.randrange(1, 100))
    s += str(random.randrange(100))
    s += random.choice(('', 'E', 'e', 'G', 'g', 'F', 'f', '%'))

print(s)




import time

randseed = int(time.time())
random.seed(randseed)



foldername = 'C:/_git/vcs/_1.data/______test_files2/'

name = os.path.basename(os.path.abspath(foldername))
print(name)
dest = os.path.abspath(os.path.join(foldername, "..", name + "Upd"))
print(dest)
#os.makedirs(dest)

#vs9to10(src, dest)

for name in os.listdir(foldername):
    path, ext = os.path.splitext(name)

    filename = os.path.normpath(os.path.join(foldername, name))
    destname = os.path.normpath(os.path.join(dest, name))
    #print("%s -> %s" % (filename, destname))

here = os.path.abspath(os.path.dirname(__file__))
par = os.path.pardir

print(here)
print(par)

ROOT = os.path.abspath(os.path.join(here, par, par))

print(ROOT)

old_cd = os.getcwd()

print(old_cd)

print('製作cmd指令')

cmd = 'dir'
if os.system(cmd) != 0:
    raise RuntimeError(cmd)


#os.chdir(os.path.join(ROOT, TK, "win"))

def cmp(f1, f2):
    bufsize = 1024 * 8
    with open(f1, 'rb') as fp1, open(f2, 'rb') as fp2:
        while True:
            b1 = fp1.read(bufsize)
            b2 = fp2.read(bufsize)
            if b1 != b2:
                return False
            if not b1:
                return True


def copy(src, dst):
    if os.path.isfile(dst) and cmp(src, dst):
        return
    shutil.copy(src, dst)



def output(string='', end='\n'):
    sys.stdout.write(string + end)


def output(*strings):
    for s in strings:
        sys.stdout.write(str(s) + "\n")



import glob
import sys

foldername = 'C:/_git/vcs/_1.data/______test_files2/'
files = glob.glob(foldername)

for file in files:
    print('aaaa')
    output(file)


'''

pos = 'abcd'
output("Lexical error at position %s" % pos)


os.system('cmd')
'''

