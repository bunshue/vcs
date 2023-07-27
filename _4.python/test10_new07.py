

print('格式化字串')

print(12345)

print('八位數 前面補0')
print('{:08d}\n{:08d}\n{:08d}'.format(123, 1234, 12345))





import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


print(__file__)
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

here = os.path.abspath(os.path.dirname(__file__))
par = os.path.pardir

print(here)
print(par)

ROOT = os.path.abspath(os.path.join(here, par, par))

print(ROOT)


import tempfile

cabname = tempfile.mktemp(suffix=".cab")
print(cabname)




import os
import time

srcdir = os.path.abspath("../..")
PCBUILD="PCbuild"
major = 3
minor = 8

dll_file = "python%s%s.dll" % (major, minor)

dll_path = os.path.join(srcdir, PCBUILD, dll_file)
print(dll_path)

current_version = "%s.%s.%s" % (major, minor, int(time.time()/3600/24))

full_current_version = current_version

print(full_current_version)


msiname = "python-%s%s.msi" % (full_current_version, 'ccccc')

print(msiname)

print()
print(os.sep)













