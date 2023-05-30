import selenium

print(selenium.__version__)


import os
import stat

print(os.name)
print(os.sep)


filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'


foldername = os.path.dirname(filename)
print(filename)
print(foldername)

mode = os.stat(filename).st_mode

print(mode)

print(stat.S_IWOTH)

print(mode & stat.S_IWOTH)

print(mode)

print(stat.S_IWGRP)

print(mode & stat.S_IWGRP)

if os.path.exists(filename):
    print('True')
else:
    print('False')
    

if os.path.isdir(filename):
    print('True')
else:
    print('False')

if os.listdir(foldername):
    print('True')
else:
    print('False')


total = 7
for i in range(0, (total+1)):
    #print(i)	# 0 ~ 7
    print(u"download: " + str(100 * i / total ) + " %.")




