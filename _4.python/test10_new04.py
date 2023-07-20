"""A ScrolledText widget feels like a text widget but also has a
vertical scroll bar on its right.  (Later, options may be added to
add a horizontal bar as well, to make the bars disappear
automatically when not needed, to move them to the other side of the
window, etc.)

Configuration options are passed to the Text widget.
A Frame widget is inserted between the master and the text, to hold
the Scrollbar widget.
Most methods calls are inherited from the Text widget; Pack, Grid and
Place methods are redirected to the Frame widget however.
"""

#字符串轉 md5 工具
import hashlib

string = 'lion-mouse'
print(string)

string_data = string.strip().replace("\n","").encode()

myMd5 = hashlib.md5()
myMd5.update(string_data)
myMd5_Digest = myMd5.hexdigest()
print(myMd5_Digest)


import os

'''

foldername = 'C:/_git/vcs/_1.data/______test_files2'

for cursrc, dirs, files in os.walk(foldername):
    print('----------------')
    print(cursrc, dirs, files)
    print('----------------')
'''

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

print(filename[:-4])
print(filename[:-4])
retval = os.path.basename(filename[:-4])

print(retval)

import platform
no_asm = int(platform.release().split(".")[0]) < 9
print(no_asm)



ADDRESS = r'\\.\pipe\_test_pipe-%s' % os.getpid()
print(ADDRESS)


import sys
def errprint(*args):
    sep = ""
    for arg in args:
        sys.stderr.write(sep + str(arg))
        sep = " "
    sys.stderr.write("\n")


msg = 'this is a lion-mouse'
errprint(msg)

print(msg)

print('檔頭的註解')
print(__doc__)



