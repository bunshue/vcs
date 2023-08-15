import os
from os.path import abspath

def _basename(path):
    # A basename() variant which first strips the trailing slash, if present.
    # Thus we always get the last component of the path, even for directories.
    sep = os.path.sep + (os.path.altsep or '')
    return os.path.basename(path.rstrip(sep))



filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
base_name = _basename(filename)
print(base_name)



src = abspath(base_name)
print(src)


zip_filename = base_name + ".zip"

print(zip_filename)


foldername = 'C:/_git/vcs/_1.data/______test_files5'

normdir = os.path.normcase(foldername)
print(normdir)






import collections

import nt
_ntuple_diskusage = collections.namedtuple('usage', 'total used free')

def disk_usage(path):
    total, free = nt._getdiskusage(path)
    used = total - free
    return _ntuple_diskusage(total, used, free)


foldername = 'C:/_git/vcs/_1.data/______test_files5'
ret = disk_usage(foldername)
print(ret)


