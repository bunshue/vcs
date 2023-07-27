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




