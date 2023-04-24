filename = 'C:/_git/vcs/_4.cmpp/_python_test/data/human2.jpg'


import os
from stat import ST_MTIME
from stat import ST_CTIME

st = os.stat(filename)

print(st)

print(st[ST_MTIME])
print(st[ST_CTIME])




#print("Serving {} on port {}, control-C to stop".format(path, port))



base = os.path.basename(filename)
print(base)

fnfilter = os.path.basename
print(fnfilter)


#os.rename(filename, backup)








    





