
import time

ttt = time.time()
#returns the seconds with millisecond precision since the UNIX epoch.
print(ttt)

ttt = int(time.time())
print(ttt)

import os
user = os.getlogin()
print(user)

version = __version__ = "4.61.0.166 Unreleased"
print(version)

font_file = os.path.join(os.path.dirname(__file__), "OpenFlame.ttf")
print(font_file)



print(__doc__)
print(globals())


import sys

major, minor, micro, level, serial = sys.version_info

print('version_info')
print(sys.version_info)
print(major)
print(minor)
print(micro)
print(level)
print(serial)

level = 123
levelnum = 170
print(" * PY_RELEASE_LEVEL = %r = %s" % (level, hex(levelnum)))





import sys

usage = """Usage: %s [-cd] paths...
    -c: recognize Python source files trying to compile them
    -d: debug output""" % sys.argv[0]

print('msgsssssss', file = sys.stderr)
print(usage, file = sys.stderr)

import os
import sys

print(sys.maxsize)
print(2**32)





