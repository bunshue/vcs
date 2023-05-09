# python import module : sys, os
# python import module : DDF 磁碟檔案資料夾操作

# os.walk


import os
cur_path = os.path.dirname(__file__) # 取得目前路徑
sample_tree = os.walk(cur_path)
for dirname,subdir,files in sample_tree:
    print("檔案路徑：", dirname)
    print("目錄串列：" , subdir)   
    print("檔案串列：", files)
    print()


import os, sys
from stat import *

def walktree(top, callback):
    '''recursively descend the directory tree rooted at top,
       calling the callback function for each regular file'''

    for f in os.listdir(top):
        pathname = os.path.join(top, f)
        mode = os.lstat(pathname).st_mode
        if S_ISDIR(mode):
            # It's a directory, recurse into it
            walktree(pathname, callback)
        elif S_ISREG(mode):
            # It's a file, call the callback function
            callback(pathname)
        else:
            # Unknown file type, print a message
            print('Skipping %s' % pathname)

def visitfile(file):
    print('visiting', file)

foldername = 'C:/_git/vcs/_1.data/______test_files2'
walktree(foldername, visitfile)

