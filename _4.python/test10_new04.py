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






