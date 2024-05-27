import os
fPath = 'c:\\data\\'
if not os.path.exists(fPath):
    os.mkdir(fPath)
f = open('c:/data/file01.txt', 'w')
#f = open('c:\\data\\file01.txt', 'w')
f.close()